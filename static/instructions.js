$(document).ready(function() {
    var recipeId = $('body').data('recipe-id');
    var currentStep = 1;
    var totalSteps = 0;
    var instructionResult;

    $.ajax({
        url: '/get_instructions/' + recipeId,
        type: 'GET',
        success: function(result) {
            instructionResult = result;
            totalSteps = Object.keys(result).length;
            displayInstruction(result[currentStep]);
            updateButtons();
        },
        error: function(xhr, status, error) {
            console.log("Error in AJAX call:", error);
        }
    });

    $('#next_button').click(function() {
        currentStep++;
        if (currentStep <= totalSteps) {
            displayInstruction(instructionResult[currentStep]);
            updateButtons();
        } else {
            alert('No more instructions.');
        }
    });

    $('#back_button').click(function() {
        if (currentStep > 1) {
            currentStep--;
            displayInstruction(instructionResult[currentStep]);
            updateButtons();
        } else {
            window.location.href = "/learn_recipe/" + recipeId;
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
                <div id="instructions_buttons">
                    ${(currentStep === 2 && recipeId === 3) ? `<a class="subtitle-button" href="/hints/0" target="_blank">Hints for Draining!</a> <br>` : ''}
                    ${(currentStep === 3 && recipeId === 3) ? `<a class="subtitle-button" href="/hints/1" target="_blank">Hints for Mincing Garlic!</a> <br>` : ''}
                    ${(currentStep === 1 && recipeId === 1) ? `<a class="subtitle-button" href="/hints/2" target="_blank">Hints for Cutting Avocados!</a> <br>` : ''} 
                    ${(currentStep === 2 && recipeId === 1) ? `<a class="subtitle-button" href="/hints/3" target="_blank">Microwave Safe Dishes!</a> <br>` : ''}  
                    ${(currentStep === 1 && recipeId === 2) ? `<a class="subtitle-button" href="/hints/4" target="_blank">Learn About Preheating an Oven!</a> <br>` : ''}
                </div>
                <div class= "row">
                    <div class="col-sm">
                        ${(currentStep === totalSteps && currentStep !== 1) ? `<a class="subtitle-button" href="/learn_recipe/${recipeId}">Recipe Home</a>` : ''}
                    </div>
                    <div class="col-sm">
                        ${(currentStep === totalSteps && currentStep !== 1) ? `<a class="subtitle-button" href="/test_recipe/${recipeId}">Test yourself!</a>` : ''}
                    </div>
                </div>
            </div>`
        );
    }

    function updateButtons() {
        if (currentStep === 1) {
            $('#back_button').text('Recipe Home');
        } else if (currentStep === totalSteps) {
            $('#back_button').hide();
            $('#next_button').hide();
        } else {
            $('#back_button').text('Back');
            $('#next_button').show();
        }
    }
});
