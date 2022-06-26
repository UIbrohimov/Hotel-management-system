$('.fa-star').click(function(){

    console.log("clicked")

    $(this).prevAll().addClass('checked');
    $(this).addClass('checked');
    $(this).nextAll().removeClass('checked');
    const rate = $(this).prevAll().length + 1;
    $('input[name="review[rating]"]').val(rate)
    if ($('input[name="review[rating]"]').val()) {
        $('#submitComment').attr('disabled', false)
        $('#rateWarning').fadeOut()
    } else {
        $('#submitComment').attr('disabled', true)
        $('#rateWarning').show()
    }
})