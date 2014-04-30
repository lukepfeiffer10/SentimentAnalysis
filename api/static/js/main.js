$(function () {
    function logout() {
        $.ajax({
            type: 'DELETE',
            url: 'api/user',
            success: function () {
                window.location = '/login'
            }
        });
    }

    $('#logout').click(logout);
});