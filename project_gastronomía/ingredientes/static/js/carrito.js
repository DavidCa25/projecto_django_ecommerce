$(document).ready(function() {
    $(".btn-minus, .btn-plus").on("click", function() {
        var carritoItemId = $(this).data("id");
        var action = $(this).hasClass("btn-minus") ? "minus" : "plus";

        // Verificar si la cantidad actual es 1 y el usuario intenta restar
        if (action === 'minus' && $("#quantity-input-" + carritoItemId).val() == 1) {
            return;
        }

        $.ajax({
            type: "POST",
            url: "/carrito/update/",
            data: {
                csrfmiddlewaretoken: "{{ csrf_token }}",
                carrito_item_id: carritoItemId,
                action: action,
            },
            success: function(response) {
                
                if (response.error) {
                    console.log("Error:", response.error);
                } else {
                    $("#subtotal-value").text(response.subtotal);
                    $("#total-value").text(response.total);
                    $("#quantity-input-" + carritoItemId).val(response.quantity);
                }
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
    });
});