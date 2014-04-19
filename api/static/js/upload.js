$(function () {
    $('#submitStory').click(function (ev) {
        var story = {};
        story.title = $('#title').val();
        story.content = $('#content').val();
        $.ajax({
            url: '/api/story',
            data: JSON.stringify(story),
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