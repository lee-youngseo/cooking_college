function displayHint(){
    let hints = [displayHintOne(), displayHintTwo(), displayHintThree(), displayHintFour(), displayHintFive()];
    $('.subtitle').append(`${hint['name']}`);
    $('#recipe-redirect').append(`Go to recipe`);
    $('#hint-container').append(hints[hintID]);
}

function displayHintOne(){
    let tipOne = $(`<div class='tip'></div>`);
    let tipTwo = $(`<div class='tip'></div>`);
    let tipThree = $(`<div class='tip'></div>`);
    let steps = hint['steps'];
}

function displayHintTwo(){

}

function displayHintThree(){

}

function displayHintFour(){

}

function displayHintFive(){

}

$(function(){
    displayHint()

    $('#recipe-redirect').on('click', function(){
        window.location.href = `/learn_recipe/${hint['recipe_id']}/instructions`;

    })

})