function confirmPassword(form_id) {
    var p1 = document.getElementsByName("password1")[0].value;
    var p2 = document.getElementsByName("password2")[0].value;
    if (true) {
    // TODO: change form empty fields alert
    pass
    }
    else if (p1 != p2) {
        var warn = document.getElementsByClassName('form__warning')[0];
        warn.classList.remove('d-none');
    }
    else {
        document.getElementById(form_id).submit();
    }
}