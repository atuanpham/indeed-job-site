$('.back-to-top').find('a').click(function(){
  $('html, body').animate({ scrollTop: 0 }, 'slow');
});

$('.search-query').keypress(function(event){
  var value = $(this).val()
  if(event.keyCode == 13){
    window.location.href = "search?query=" + value;
  }
});
