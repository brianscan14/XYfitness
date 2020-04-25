$(function() {

    $("#payment-form").submit(function() {
        let form = this;
        let card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val() 
        };

        Stripe.createToken(card, stripeCreateHandler);

        return false;
    });
});

    function stripeCreateHandler(status, response) {
        let form = document.getElementById('payment-form');

        if (response.error) {

            $("#stripe-error-message").text(response.error.message);
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
            
        } else {
            
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
        }

    };
