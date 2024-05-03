function displayHint(){
    let hints = [displayHintOne(), displayHintTwo(), displayHintThree(), displayHintFour(), displayHintFive()];
    $('.subtitle').append(`${hint['name']}`);
    $('#recipe-redirect').append(`Go to recipe`);
    $('#hint-container').append(hints[hintID]);
}

function displayHintOne(){
    let tipOneContainer = $(`<div class='drain-tip col-4'></div>`);
    let tipTwoContainer = $(`<div class='drain-tip col-4'></div>`);
    let tipThreeContainer = $(`<div class='drain-tip col-4'></div>`);
    let tips = [tipOneContainer, tipTwoContainer, tipThreeContainer]
    let steps = hint['steps'];
    console.log(steps);

    for(let i=1; i<4; i++){
        tips[i-1].append(`<img src=${steps[i]['img']} alt=${steps[i]['alt']}/>`)
        tips[i-1].append(`<span class="drain-instructions col-12">${steps[i]['instructions']}</span>`)
    }

    return [tipOneContainer, tipTwoContainer, tipThreeContainer];



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