function tableSearch(id_input, id_table) {
    var phrase = document.getElementById(id_input);
    var table = document.getElementById(id_table);
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    var id = 0;
    var maxRow = 1;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        for (var j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
            if(i > maxRow) maxRow = i;
            table.rows[i].style.background = (id%2 == 0) ? "#323846" : "#3B414E";
            table.rows[i].cells[0].style.borderBottomLeftRadius = "0";
            table.rows[i].cells[2].style.borderBottomRightRadius = "0";
            id++;
        } else {
            table.rows[i].style.display = "none";
            table.rows[i].cells[0].style.borderBottomLeftRadius = "0";
            table.rows[i].cells[2].style.borderBottomRightRadius = "0";
        }
    }
    table.rows[maxRow].cells[0].style.borderBottomLeftRadius = "10px";
    table.rows[maxRow].cells[2].style.borderBottomRightRadius = "10px";
}
