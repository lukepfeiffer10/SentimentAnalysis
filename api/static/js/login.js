/// <reference path="js/jquery.js" />

$(function () {
    $('#loginArea').submit(function (ev) {
        ev.preventDefault();
        var loginObject = {};
        loginObject.username = $('#username').val();
        loginObject.password = $('#password').val();
        login(loginObject);
    });

    function login(loginObject) {
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
    }

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
                var loginObject = {}
                loginObject.username = newUser.username;
                loginObject.password = newUser.password;
                login(loginObject);
            },
            dataType: 'json',
            type: 'POST',
            contentType: 'application/json'
        });
    });
});