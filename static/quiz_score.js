$(function(){

    document.getElementById('recipe-restart-button').onclick = function(){
        recipe_id = parseInt(quiz_id)
        // console.log(recipe_id)
        window.location.href = `/learn_recipe/${recipe_id}`
    }
})
