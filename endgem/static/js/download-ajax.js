$('#downloads').click(function(){
	var catid;
	catid = $(this).attr("data-catid");
	$.get('/rango/download/', {category_id: catid}, function(data){
		$('#download_count').html(data);
			$('#downloads').hide();
	});
});