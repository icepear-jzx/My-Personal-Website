$('button.change').click(function () {
    if ($(this).children('i.fa-th').length) {
        $(this).children('i.fa-th').addClass('fa-th-list').removeClass('fa-th');
        $('div.card-lines').css('display', 'none');
        $('div.card-columns').css('display', 'block');
        // var cards = $('div.card');
        // for (let i = 0; i < cards.length; i++) {
        //   $('div.card#' + i).css('animation-delay', Math.random() + 's')
        // }
    } else {
        $(this).children('i.fa-th-list').addClass('fa-th').removeClass('fa-th-list');
        $('div.card-lines').css('display', 'inline');
        $('div.card-columns').css('display', 'none');
    }
});