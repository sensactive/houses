window.onload = function () {
    $('.counter').on('change', 'input[type="number"]', function () {
        var t_href = event.target;

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                $('.counter').html(data.result);
            },
        });

        event.preventDefault();
    });
}