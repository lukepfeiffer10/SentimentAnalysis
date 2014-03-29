/// <reference path="js/jquery.js" />

$(function () {
    $('#loginButton').click(function () {
        var loginObject = {};
        loginObject.username = $('#username').val();
        loginObject.password = $('#password').val();
        $.ajax({
            url: '/api/user', 
            data: loginObject, 
            success: function () {
                window.location = '/';
            },
            dataType: 'json',
            type: 'PUT',
            contentType: 'application/json'
        });
    });
});