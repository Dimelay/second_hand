$(document).ready(function(){
$(".date_input").change(function() {
$.ajax({
type: 'GET',
cache: false,
url: '/bar?date_input_day='+$("#id_date_input_day").val()+'&date_input_month='+$("#id_date_input_month").val()+'&date_input_year='+$("#id_date_input_year").val(),
success: function(data){$('#product_list').html(''),$('#product_list').append(data);}
});
return false;
});
});
