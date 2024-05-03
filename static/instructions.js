$(document).ready(function() {
    var recipeId = $('body').data('recipe-id');
    var currentStep = 1;
    var totalSteps = 0;

    $.ajax({
        url: '/get_instructions/' + recipeId,
        type: 'GET',
        success: function(result) {
            totalSteps = Object.keys(result).length;
            displayInstruction(result[currentStep]);
            updateButtons();

            $('#next_button').click(function() {
                currentStep++;
                if (currentStep <= totalSteps) {
                    displayInstruction(result[currentStep]);
                    updateButtons();
                } else {
                    alert('No more instructions.');
                }
            });

            $('#back_button').click(function() {
                if (currentStep > 1) {
                    currentStep--;
                    displayInstruction(result[currentStep]);
                    updateButtons();
                } else {
                    window.location.href = "/learn_recipe/" + recipeId;
                }
            });
        },
        error: function(xhr, status, error) {
            console.log("Error in AJAX call:", error);
        }
    });

    function displayInstruction(instruction) {
        $('#instructions_container').empty();
        console.log("Appending instruction:", instruction.step);
        $('#instructions_container').append(
            `<div class="col-4">
                <div class="subtitle">Step ${currentStep}</div>
                <div class="image-container">
                    <img src="${instruction.image}" class="view-image square" alt="${instruction.step}">
                </div>
                <div class="subtitle-button">${instruction.step}</div>
                <br>
            </div>`
    );
}


    function updateButtons() {
        if (currentStep === 1) {
            $('#back_button').text('Recipe Home');
        } else if (currentStep === totalSteps) {
            $('#back_button').text('Back to Recipe');
            $('#back_button').off('click').click(function() {
                window.location.href = "/learn_recipe/" + recipeId;
            });
            $('#next_button').hide();
        } else {
            $('#back_button').text('Back');
            $('#back_button').off('click').click(function() {
                if (currentStep > 1) {
                    currentStep--;
                    displayInstruction(result[currentStep]);
                    updateButtons();
                }
            });
            $('#next_button').show();
        }

    }
});
