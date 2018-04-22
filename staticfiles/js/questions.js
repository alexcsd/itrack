
function fetchQuestion(data) {
    if(data.response){
        return window.location = '/result';
    }
    $(".skip").unbind("click");
    // console.log(data);
    //data.answers is a string
    json_string = data.answers;
    //you convert the string into an object with the function JSON.parse
    
    var question = data.question;
    var type = data.type;
    var answers = JSON.parse(json_string);
    if (type == 'MCQ') {
        $('#mcq .answers').html('');
        $('#mcq .question').text(question);
        for (answer in answers) {
            $('#mcq .answers').append(
                '<a class="btn btn-outline-primary animated fadeIn answer   " pk="' + answers[answer].pk + '">'
                + '<input type="radio" name="options" id="option1" autocomplete="off" checked> ' + answers[answer].fields.body + ''
                + '</a>'
            );
        }
        $('#mcq').fadeIn('fast');
    }
    if (type == 'TF') {
        $('#tf .answers').html('');
        $('#tf .question').text(question);
        for (answer in answers) {
            if (answers[answer].fields.body == 'True')
                $('#tf .answers').append(
                    '<div class="col-6">' +
                    '<a href="#" class="btn btn-outline-info btn-circle btn-xl animated fadeIn answer" pk="' + answers[answer].pk + '">True</a>' +
                    '</div>'
                );
            if (answers[answer].fields.body == 'False')
                $('#tf .answers').append(
                    '<div class="col-6">' +
                    '<a href="#" class="btn btn-outline-danger btn-circle btn-xl animated fadeIn answer" pk="' + answers[answer].pk + '">False</a>' +
                    '</div>'
                );
        }
        $('#tf').addClass(' show animated fadeIn');
    }
    var timeout = setTimeout(() => {
        $('.skip').addClass(' show');
    }, 2000);
    $('.answer').one('click', function () {
        var pk = $(this).attr('pk');
        $('#tf,#mcq').fadeOut('fast'); 
        clearTimeout(timeout);
        $('.skip').removeClass('show animated fadeIn');
        setTimeout(() => {
            $.post("/questionfetch/" + pk, fetchQuestion);
        }, 100);
    });
    return 1;
}
$(document).ready(function() {
    $('.start').one('click', function () {
       
        $('#start').animateCss('flipOutX', function () {
            $('#start').addClass(' display-none');
            $.post("/questionfetch", fetchQuestion);
        });
    });
    
})