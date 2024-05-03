function displayHint(){
    let hints = [displayHintOne(), displayHintTwo(), displayHintThree(), displayHintFour(), displayHintFive()];
    $('.subtitle').append(`${hint['name']}`);
    $('#recipe-redirect').append(`Go to recipe`);
    $('#hint-container').append(hints[hintID]);
}

function displayHintOne(){
    if(hintID===0) {
        let tipOneContainer = $(`<div class='drain-tip col-4'></div>`);
        let tipTwoContainer = $(`<div class='drain-tip col-4'></div>`);
        let tipThreeContainer = $(`<div class='drain-tip col-4'></div>`);
        let tips = [tipOneContainer, tipTwoContainer, tipThreeContainer]
        let steps = hint['steps'];

        for (let i = 1; i < 4; i++) {
            tips[i - 1].append(`<img src=${steps[i]['img']} alt=${steps[i]['alt']}/>`)
            tips[i - 1].append(`<span class="drain-instructions">${steps[i]['instructions']}</span>`)
        }

        return [tipOneContainer, tipTwoContainer, tipThreeContainer];
    }



}

function displayHintTwo(){
    if(hintID === 1) {
        let stepsContainer = $(`<div id="mincing-steps-container" class="col-6">
            <span id="mincing-pre">${hint['pre_step']}</span></div>`);
        let mincingImg = $(`<div id="mincing-img-container" class="col-6">
            <img id="mincing-img" src=${hint['img']} alt="${hint['alt']}"</div>`);
        let stepsList = $(`<ol id="mincing-steps"></ol>`);
        let steps = hint['steps'];


        Object.values(steps).forEach(function (step) {
            stepsList.append($(`<li class="mincing-step">${step}</li>`));
        })


        stepsContainer.append([stepsList]);
        return [mincingImg, stepsContainer];
    }

}

function displayHintThree(){
    if(hintID===2){

    }

}

function displayHintFour(){
    if(hintID===3){

    }

}

function displayHintFive(){
    if(hintID===4){

    }

}

$(function(){
    displayHint()

    $('#recipe-redirect').on('click', function(){
        window.location.href = `/learn_recipe/${hint['recipe_id']}/instructions`;

    })

})