$(document).ready(function() {
    var recipeId = $('body').data('recipe-id');
    var key = $('body').data('key');

    $.ajax({
        url: `/get_supplies_ingredients/${recipeId}`,
        type: 'GET',
        success: function(result) {
            $.each(result, function(section, info) {
                if (key == "Supplies") {
                    if (section === 'supplies') {
                        console.log("Supplies:", info);
                        $.each(info, function(id, supply) {
                            $('#supplies_ingredients_container').append(
                                `<div class="col-3">
                                    <div class="image-container">
                                        <img src="${supply.image}" class="view-image square" alt="${supply.name}"> 
                                    </div>
                                    <div class="label">${supply.name}</div>
                                </div>`
                            );
                        });  
                    }
                }

                if (key == "Ingredients") {
                    if (section === 'ingredients') {
                        console.log("Ingredients:", info);
                        $.each(info, function(id, ingredient) {
                            $('#supplies_ingredients_container').append(
                                `<div class="col-3">
                                    <div class="image-container">
                                        <img src="${ingredient.image}" class="view-image square" alt="${ingredient.name}"> 
                                    </div>
                                    <div class="label">${ingredient.name}</div>
                                </div>`
                            );
                        });
                    }
                }
                
            });
        }
    });
});     
