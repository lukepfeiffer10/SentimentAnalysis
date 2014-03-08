/// <reference path="js/jquery.js" />

$(function () {
    $('#loginButton').click(function () {
        var loginObject = {};
        loginObject.username = $('#username').val();
        loginObject.password = $('#password').val();
        $.post('/api/user/login', loginObject, function () {
            window.location = '/';
        });
    });
});