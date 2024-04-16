$(document).ready(function() {
    console.log("Document ready."); // This should print to the console
    $.ajax({
        url: '/get_recipes',
        type: 'GET',
        success: function(result) {
            console.log("AJAX call successful."); // This should print to the console
            console.log("Result:", result);
            $.each(result, function(id, recipe) {
                console.log("Appending recipe:", recipe.name); // This should print to the console
                $('#recipe_container').append(
                    `<div class="col-4">
                        <a href="/test_recipe/${id}" class="recipe-link">
                            <div class="image-container">
                                <img src="${recipe.image}" class="view-image square" alt="${recipe.name}">
                            </div>
                            <div class="subtitle-button">${recipe.name}</div>
                        </a>
                    </div>`
                );
            });
        },
        error: function(xhr, status, error) {
            console.log("Error in AJAX call:", error); // Any AJAX errors should print here
        }
    });
});
