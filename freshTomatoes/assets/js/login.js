// Toggle Function
(function() {
    $('.toggle').click(function () {
        $('form').animate({
            height: 'toggle',
            opacity: "toggle"
        }, "slow");
    });

});