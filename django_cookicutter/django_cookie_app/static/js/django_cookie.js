$(document).ready(function(){
    
    var quantity_func = function(plus, moins, button)  {
        $(plus).click(function(e){
        e.preventDefault();
        var quantity = parseInt($(button).val());
        $(button).val(quantity + 1);
        });

        $(moins).click(function(e){
            e.preventDefault();
            var quantity = parseInt($(button).val());
            if(quantity>0){
                $(button).val(quantity - 1);
            }
        });
    };

    quantity_func(".mint-plus", ".mint-minus", "#id_mint");
    quantity_func(".syrup-plus", ".syrup-minus", "#id_syrup");
    quantity_func(".vanilla-plus", ".vanilla-minus", "#id_vanilla");
    quantity_func(".raspberry-plus", ".raspberry-minus", "#id_raspberry");
    quantity_func(".choco-plus", ".choco-minus", "#id_choco");

    $(".ajax_form").submit(function(event){
        event.preventDefault();
        var request_method = $(this).attr("method");
        var form_data = $(this).serialize();
        $.ajax({
            url: 'http://10.211.55.7:8000/rest/order/inspect/',
            type: request_method,
            data : form_data,
            beforeSend: function (xhr, settings) {
		xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
            },
            success: function (data) {
		data = JSON.parse(JSON.stringify(data));
                if (data.id !== null){
                    window.location.href = "http://10.211.55.7:8000/orders/"+data.id;
                }
                else if (data.name !== null){
                    alert('Reload '+data.name+' in stock!')
                }
            },
            error: function(error) {
                alert("Désolé, aucun résultat trouvé.", error);
            }
	});
    });

    $("#button-action").click(function(event){
	event.preventDefault();
        var order = $(this)[0].dataset.nameOrder;
        var url = 'http://10.211.55.7:8000/rest/'+order+'/update_bucket/'
	$.ajax({
            url : url,
            type: 'POST',
            contentType: "application/json",
            data : {'order': order},
            success: function (data) {
		data = JSON.parse(JSON.stringify(data));
                console.log(data)
                location.reload();
            },
            error: function() {
                alert("T'as tout cassé.");
            }
	});
    });
});
