/// <reference path="js/jquery.js" />

$(function () {
    $('#loginArea').submit(function (ev) {
        ev.preventDefault();
        var loginObject = {};
        loginObject.username = $('#username').val();
        loginObject.password = $('#password').val();
        $.ajax({
            url: '/api/user', 
            data: JSON.stringify(loginObject), 
            success: function () {
                window.location = '/';
            },
            dataType: 'json',
            type: 'PUT',
            contentType: 'application/json'
        });
    });

    $('#newUserForm').submit(function (ev) {
        ev.preventDefault();
        var newUser = {};
        newUser.firstName = $('#firstName').val();
        newUser.lastName = $('#lastName').val();
        newUser.username = $('#newUsername').val();
        newUser.password = $('#newPassword').val();
        $.ajax({
            url: '/api/user',
            data: JSON.stringify(newUser),
            success: function (data) {
                //window.location = '/';
                alert(data);
            },
            dataType: 'json',
            type: 'POST',
            contentType: 'application/json'
        });
    });
});