$(document).ready(function(){

$("#id_discont").change(function() {
var proc = parseInt($(this).val());
if (proc >0) {
calc_price(proc);
}
else
{
calc_price(0)
}
});
function calc_price(procent) {
var ap = 0;
$("#product .price").each(function() {
ap = ap + parseInt($(this).text());
});
ap = ap - ap/100*parseInt(procent);
$("#all_price").html(ap);
}

$("#product").on('click','.remove_product', function(e) {
e.preventDefault();
$(this).closest("div").fadeOut(400, function(){
$(this).remove();
calc_price();
});
});

$("#product").bind("append", function() {
calc_price(0);
});

$("#product_sale").bind("submit", function() {
    $.ajax({
    type: 'POST',
    cache: false,
    url: '/sale/',
    data: $(this).serialize(),
    success: function(data){$('#product').html(data);}
    });
return false;
});

$("#form_searchpoint").bind("submit", function() {
if (!$("#id_pid").val())
{

return false;
}
/*
$('<div id="my-dialog">Поиск...</div>').dialog({
    title: 'Карточка товара',
    width: 1024,
    height: 768,
    modal: true,
    open: function() {
    */
var rev = null;
if ($("#reverse").is(":checked")) {
rev = 1
}
else {
rev = 0
}
    $.ajax({
    type: 'GET',
    cache: false,
    url: 'product/'+$("#id_pid").val()+'/'+rev,
    success: function(data){$('#product').prepend(data).trigger("append");}
    });
    $("#id_pid").val('');
    /*
    setTimeout("$('#my-dialog').dialog('close')",300000);
    },
    close: function() {
    
    $('#my-dialog').remove();
        parent.location.reload(true);
    }
});
*/
return false;

});

});
