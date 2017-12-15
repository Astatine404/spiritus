function implement_fullpage()
{
	$('#fullpage').fullpage({
			anchors: ['home', 'app'],
			sectionsColor: ['#000000', '#000000'],
		});
}

$(document).ready(function() {
	implement_fullpage();
	// cust_controls();
	$('.progress').hide();
});

function progress_bar()
{
	$('.progress').show();
	var current_progress = 0;
  	var interval = setInterval(function() {
      current_progress += parseInt(10 * Math.random());
      if (current_progress >= 100)
      	current_progress = 100;
      $("#dynamic")
      .css("width", current_progress + "%")
      .attr("aria-valuenow", current_progress)
      .text(current_progress + "% Complete");
      if (current_progress >= 100)
          clearInterval(interval);
  }, 1000);
}