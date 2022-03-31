from django.contrib import admin

from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'role', 'club', 'rating')
    list_display_links = ('last_name',)
    search_fields = ('last_name', 'club')
    list_filter = ('club',)


class ClubsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fighters_counter', 'rating')
    list_display_links = ('name',)
    search_fields = ('name',)

@admin.register(Tiltyard)
class TiltyardModel(admin.ModelAdmin):
    list_filter = ('name', 'nomination')
    list_display = ('id', 'name', 'nomination', 'age_category', 'league', 'state', 'referee')

admin.site.register(User, UsersAdmin)
admin.site.register(Club, ClubsAdmin)
