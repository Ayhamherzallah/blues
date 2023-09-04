   // Get the input element and plus/minus icons
    var quantityInput = document.getElementById('q');
    var plusIcon = document.getElementById('plus');
    var minusIcon = document.getElementById('minus');

    // Add a click event listener to the plus icon
    plusIcon.addEventListener('click', function () {
        // Increment the quantity value by 1
        quantityInput.value = parseInt(quantityInput.value) + 1;
    });

    // Add a click event listener to the minus icon
    minusIcon.addEventListener('click', function () {
        // Check if the quantity is greater than 1 before decrementing
        if (parseInt(quantityInput.value) > 1) {
            quantityInput.value = parseInt(quantityInput.value) - 1;
        }
    });