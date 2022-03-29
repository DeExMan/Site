from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token

from .forms import *
from .models import *
from .serializers import *

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response



def index(request):
    fighters = User.objects.all()
    clubs = Club.objects.all()
    return render(request, 'main/index.html', {'fighters': fighters, 'clubs': clubs})


def clubs(request):
    table = Club.objects.all()
    return render(request, 'main/clubs.html', {'table': table})


def profile(request):
    return render(request, 'main/profile.html')


def profile_change(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.pk)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.patronymic = form.cleaned_data.get('patronymic')
            new_club = form.cleaned_data.get('club')
            if new_club != user.club:
                club = Club.objects.get(name=new_club)
                club.fighters_counter += 1
                club.save()
                club = Club.objects.get(name=user.club)
                club.fighters_counter -= 1
                club.save()
            user.club = new_club
            user.save()
            return redirect('main:profile')
        # else:
        #     return HttpResponse("Invalid data")
    else:
        form = ChangeUserForm()
        return render(request, 'main/profile_change.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            to_email = form.cleaned_data.get('email')
            user = User.objects.get(email=to_email)
            current_site = get_current_site(request)
            message = render_to_string('main/active_email.html', {
                'user':user, 
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Активируйте свою учётную запись!'
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'main/end_register.html')
    else:
        form = RegisterUserForm()
    return render(request, 'main/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        club = Club.objects.get(name=user.club)
        club.fighters_counter += 1
        club.save()
        # login(request, user)
        return HttpResponse('Спасибо за подтверждение электронной почты. Теперь вы можете войти в свою учётную запись.')
    else:
        return HttpResponse('Ссылка активации недействительна!')


class TiltyardViewSet(viewsets.ModelViewSet):
    queryset = Tiltyard.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return TiltyardSerializerPost
        else:
            return TiltyardSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RefereesViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role = 3, tiltyard__isnull =True)
    serializer_class = UserSerializer

class FreeFightersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role = 1, tiltyard__isnull =True)
    serializer_class = FighterSerializer



class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({'token': token.key, 'id': token.user_id})