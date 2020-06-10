function confirmPassword(button_id) {
    var p1 = document.getElementsByName("password1")[0].value;
    var p2 = document.getElementsByName("password2")[0].value;
    if (p1 != p2) {
        var warn = document.getElementsByClassName('form__warning')[0];
        warn.classList.remove('d-none');
    }
    else {
        document.getElementById(button_id).click();
    }
}

function searchUser() {
    var userName = document.getElementById('inputName').value;
    location.href = "/user/" + userName;
    //window.event.returnValue = false;
    }
