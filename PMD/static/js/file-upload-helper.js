$(function() {
    var maxFileSizeInBytes = 100000; // 100kB
    $('#inputFile').change(function () {
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

        fileReader.onload = function (evt) {
            $('#inputFileResult').html(evt.target.result.replace(/\n/g, '<br>'));
            $('#inputFileResult').show();
        }

        fileReader.onerror = function (evt) {
            $.bootstrapGrowl("Something went wrong", {
                type: 'danger',
                align: 'center',
                width: 'auto'
            });
            $('#inputFile').val(null);
            $('#inputFileResult').hide();
        }
    });
});
