$(function() {
    var fileText;

    var maxFileSizeInBytes = 100000; // 100kB
    $('#inputFile').change(function () {
        fileText = null;
        $('#inputFileResult').hide();

        var file = this.files[0];

        if (file.type != 'text/plain' && file.type != '') {
            $.bootstrapGrowl("Only plain text files are allowed", {
                type: 'danger',
                align: 'center',
                width: 'auto'
            });
            $('#inputFile').val(null);
            return;
        }

        if (file.size > maxFileSizeInBytes) {
            $.bootstrapGrowl("File is too big", {
                type: 'danger',
                align: 'center',
                width: 'auto'
            });
            $('#inputFile').val(null);
            return;
        }

        var fileReader = new FileReader();
        fileReader.readAsText(file);

        fileReader.onload = function(event) {
            fileText = event.target.result;
            $('#inputFileResult').html(fileText.replace(/\n/g, '<br>'));
            $('#inputFileResult').show();
        }

        fileReader.onerror = function(event) {
            $.bootstrapGrowl("Something went wrong", {
                type: 'danger',
                align: 'center',
                width: 'auto'
            });
            $('#inputFile').val(null);
            $('#inputFileResult').hide();
        }
    });

    $('#fileUploadSubmit').click(function() {
        if (fileText == null) {
            $.bootstrapGrowl("Choose a file", {
                type: 'danger',
                align: 'center',
                width: 'auto'
            });
        } else {
            $.post('upload', {text : fileText}, function(data) {
                console.log(data);
            });
        }
    });
});
