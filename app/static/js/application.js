function showTicket () {
    $(this).closest('.confirmation').find('.ticket').slideDown();
}

$(document).ready(function() {
    $('.vacation').on('keyup', '.quantity', function() {
        var price = +$(this).closest('.vacation').data('price');
        var quantity = +$(this).val();
        $('#total').text(price * quantity);
    });

    $('.vacation_comments').on('click', '.expand', function(event) {
        event.preventDefault();
        $(this).closest('.vacation_comments').find('.mycomments').fadeToggle();
    });

    $('.confirmation').on('click', 'button', showTicket);
});

