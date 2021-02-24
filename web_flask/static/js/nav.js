$(document).ready(function() {
    const linkLi = $( ".nav-item" );
    const linkAnchor = $( ".nav-item a" ); // anchor is require to prevent for not to direct
    linkAnchor.bind( "click", function(event) {
        var clickedItem = $( this ).parent("li:first");
        linkLi.each( function() {
            $( this ).removeClass( "active" );
        });
        clickedItem.addClass( "active" );
    });
   $( ".nav-item a[href$='"+window.location.pathname+"']" ).parent("li:first").addClass("active"); 
});
