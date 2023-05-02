$(document).ready(function () {
    $('.btn').click(function () {
        var $this = $(this);
        if ($this.hasClass('hold')) {
            $this.removeClass().addClass('held');
        } else if ($this.hasClass('held')) {
            $this.removeClass('held').addClass('hold');
        }
    });
});