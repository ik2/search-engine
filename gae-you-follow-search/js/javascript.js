$(window).load(function() {  document.getElementById("hideAll").style.display = "none"; });
$(document).ready(function () {
  var windowHeight = $(window).height();
  var windowWidth = $(window).width();
  var aspectRatioContent = (windowHeight - 150) / (windowWidth - 60);
  var aspectRatioImage = 1080 / 1485;
  if (aspectRatioContent > aspectRatioImage) {
    $('.main').css({
      "height": (windowWidth - 60) * aspectRatioImage + "px",
      "width": (windowWidth - 60) + "px"
    });
    $('.background').css({
      "background-size": (windowWidth - 60) + "px"
    });
    $('.content, #galleria').css({
      "min-height": (windowWidth - 60) * aspectRatioImage + "px",
      "width": (windowWidth - 60) + "px"
    });
  } else {
    $('.main').css({
      "height": windowHeight - 150 + "px",
      "width": (windowHeight - 150) * (1 / aspectRatioImage) + "px"
    });
    $('.background').css({
      "background-size": (windowHeight - 150) * (1 / aspectRatioImage) + "px"
    });
    if (windowWidth > 767) {
      $('.content').css({
        "min-height": windowHeight - 150 + "px",
        "width": (windowHeight - 150) * (1 / aspectRatioImage) - 40 + "px"
      });
      $('#galleria').css({
        "min-height": windowHeight - 200 + "px",
        "width": (windowHeight - 200) * (1 / aspectRatioImage) - 40 + "px"
      });
    } else {
      $('.content').css({
        "min-height": windowHeight - 150 + "px",
        "width": windowWidth - 40 + "px"
      });
      $('#galleria').css({
        "min-height": windowHeight - 200 + "px",
        "width": windowWidth - 40 + "px"
      });
    };
  };
  $('.sign').mouseover(function () {
    $(this).stop(true).animate({
      opacity: 0.5
    }, 200);
  });
  $('.sign').mouseout(function () {
    $(this).stop(true).animate({
      opacity: 1
    }, 200);
  });
});
