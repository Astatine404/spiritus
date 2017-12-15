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
});