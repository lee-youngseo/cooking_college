$(document).ready(function() {
    var recipeId = $('body').data('recipe-id');

    $.ajax({
        url: '/get_instructions/' + recipeId,
        type: 'GET',
        success: function(result) {
            $.each(result, function(id, instruction) {
                console.log("Appending instruction:", instruction.step); // This should print to the console
                $('#instructions_container').append(
                    `<div class="col-4">
                        <div class="subtitle">Step ${id}</div>
                        <div class="image-container">
                            <img src="${instruction.image}" class="view-image square" alt="${instruction.step}">
                        </div>
                        <div class="subtitle-button">${instruction.step}</div>
                        <br>
                    </div>`
                );
            });
        },
        error: function(xhr, status, error) {
            console.log("Error in AJAX call:", error); // Any AJAX errors should print here
        }
    });
});