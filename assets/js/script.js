$(function () {
    var quantitiy = 0;
    $('.diminuiQuantidade').click(function (e) {
        campo = $(this).attr('data-field');
        e.preventDefault();
        var quantity = parseInt($('#' + campo + '').val());
        $('#' + campo + '').val(quantity - 1);
    });

    $('.aumentaQuantidade').click(function (e) {
        campo = $(this).attr('data-field');
        e.preventDefault();
        var quantity = parseInt($('#' + campo + '').val());
        $('#' + campo + '').val(quantity + 1);

    });

})
$('.carousel').carousel({
    interval: 4000
})

$('.toast').toast('show');