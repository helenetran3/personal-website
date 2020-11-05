(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $(".dropdown-trigger").dropdown({
      // inDuration: 300,
      outDuration: 1000,
      constrain_width: false,
      hover: true, // Activate when hover
      gutter: 0, // Spacing from edge
      belowOrigin: true, // Displays dropdown below the button
      alignment: 'left' // Displays dropdown with edge aligned to the left of button
    });


  }); // end of document ready
})(jQuery); // end of jQuery name space
