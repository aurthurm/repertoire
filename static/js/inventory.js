/*Drop down shownon hover*/
$(function() {
    $(".dropdown").hover(
        function(){ $(this).addClass('open') },
        function(){ $(this).removeClass('open') }
    );
});

 /*Suppliers  Page  Table bootstrap classes*/
 $('.to-affect .affect:odd').addClass('active');
 $('.to-affect .affect:even').addClass('success');

/*Drop Down Menus*/
$('.dropdown-submenu a.drop').on("click", function(e){
	$(this).next('ul').toggle();
	e.stopPropagation();
	e.preventDefault();
});

/* login modal */
$('#login-modal').modal('show');
$('#username').focus();

/* login modal */
$('#contact-developer-modal').modal('show');
$('#subject').focus();

/*glyph iconns tooltips*/
$('[data-toggle="tooltip"]').tooltip();

/*Adjustme popovers*/
$('[data-toggle="popover"]').popover({
    placement : 'right',
    trigger : 'hover'
});
