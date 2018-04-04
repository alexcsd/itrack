function fetchQuestion(data) {
    // console.log(data);
    //data.answers is a string
    json_string = data.answers;
    //you convert the string into an object with the function JSON.parse
    console.log(data);
    
    var question = data.question;
    var type = data.type;
    var answers = JSON.parse(json_string);
        // for (answer in answers) {
        //     console.log(answers[answer].fields.weight);
        // }
    if (type == 'MCQ') {
        $('#mcq .answers').html('');
        $('#mcq .question').text(question);
        for (answer in answers) {
            $('#mcq .answers').append(
                '<a class="btn btn-outline-secondary animated bounceIn answer   " pk="' + answers[answer].pk + '">'
                + '<input type="radio" name="options" id="option1" autocomplete="off" checked> ' + answers[answer].fields.body + ''
                + '</a>'
            );
        }
        $('#mcq').addClass(' show animated flipInY');
    }
    if (type == 'TF') {
        $('#tf .answers').html('');
        $('#tf .question').text(question);
        for (answer in answers) {
            if (answers[answer].fields.body == 'True')
                $('#tf .answers').append(
                    '<div class="col-6">' +
                    '<a href="#" class="btn btn-outline-info btn-circle btn-xl animated bounceIn answer" pk="' + answers[answer].pk + '">True</a>' +
                    '</div>'
                );
            if (answers[answer].fields.body == 'False')
                $('#tf .answers').append(
                    '<div class="col-6">' +
                    '<a href="#" class="btn btn-outline-danger btn-circle btn-xl animated bounceIn answer" pk="' + answers[answer].pk + '">False</a>' +
                    '</div>'
                );
        }
        $('#tf').addClass(' show  flipInY');
    }
    setTimeout(() => {
        $('.skip').addClass(' show animated fadeIn');
    }, 5000);
    var clicked = false;
    $('.answer').on('click', function () {
        if(!clicked){

            console.log($(this).attr('pk'));
            
            var pk = $(this).attr('pk');
            // $('#tf,#mcq').animateCss('flipOutY', function () {
                $.post("/questionfetch/"+pk, fetchQuestion);
            // });
            setTimeout(() => {
                clicked=true;
            }, 2000);
        }

    });
}

$(document).ready(function () {
    $.post("/questionfetch", fetchQuestion);
});