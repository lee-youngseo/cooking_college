function displayHint(){
    let hints = [displayHintOne(), displayHintTwo(), displayHintThree(), displayHintFour(), displayHintFive()];
    $('.subtitle').append(`${hint['name']}`);
    $('#hint-container').append(hints[hintID]);
    $('#recipe-redirect').append(`Go to recipe`);
}

function displayHintOne(){
    if(hintID===0) {
        let tipOneContainer = $(`<div class='tip col-4'></div>`);
        let tipTwoContainer = $(`<div class='tip col-4'></div>`);
        let tipThreeContainer = $(`<div class='tip col-4'></div>`);
        let tips = [tipOneContainer, tipTwoContainer, tipThreeContainer]
        let steps = hint['steps'];

        for (let i = 1; i < 4; i++) {
            tips[i - 1].append(`<img src=${steps[i]['img']} alt=${steps[i]['alt']}/>`)
            tips[i - 1].append(`<span class="tip-instructions">${steps[i]['instructions']}</span>`)
        }

        return tips;
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
        let tipOneContainer = $(`<div class='tip col-3'></div>`);
        let tipTwoContainer = $(`<div class='tip col-3'></div>`);
        let tipThreeContainer = $(`<div class='tip col-3'></div>`);
        let tipFourContainer = $(`<div class='tip col-3'>`)
        let tips = [tipOneContainer, tipTwoContainer, tipThreeContainer, tipFourContainer]
        let steps = hint['steps'];

        for (let i = 1; i < 5; i++) {
            tips[i - 1].append(`<img src=${steps[i]['img']} alt=${steps[i]['alt']}/>`)
            tips[i - 1].append(`<span class="tip-instructions">${steps[i]['instructions']}</span>`)
        }

        return tips;

    }

}

function displayHintFour(){
    if(hintID===3) {
        let safeContainer = $(`<div id='safe-tips-container' class="col-6"><span id="safe-title">Safe</span></div>`);
        let unsafeContainer = $(`<div id='unsafe-tips-container' class="col-6">
            <span id="unsafe-title">Not Safe</span></div>`);
        let safeList = $("<ul id='safe-list'></ul>");
        let unsafeList = $("<ul id='unsafe-list'></ul>")

        let safeItems = hint['safe'];
        let unsafeItems = hint['unsafe'];

        safeItems.forEach(function (item) {
            safeList.append($(`<li class='safe-item'>${item}</li>`));

        })
        unsafeItems.forEach(function (item) {
            unsafeList.append($(`<li class='unsafe-item'>${item}</li>`))
        })

        safeContainer.append(safeList);
        unsafeContainer.append(unsafeList);

        return [safeContainer, unsafeContainer];
    }
}

function displayHintFive(){
    if(hintID===4){
        let tipOneContainer = $(`<div class='tip col-6'></div>`);
        let tipTwoContainer = $(`<div class='tip col-6'></div>`);
        let tips = [tipOneContainer, tipTwoContainer];
        let steps = hint['steps'];

        for (let i = 1; i < 3; i++) {
            tips[i - 1].append(`<img src=${steps[i]['img']} alt=${steps[i]['alt']}/>`)
            tips[i - 1].append(`<span class="tip-instructions">${steps[i]['instructions']}</span>`)
        }

        return tips;

    }

}

$(function(){
    displayHint()

    $('#recipe-redirect').on('click', function(){
        window.location.href = `/learn_recipe/${hint['recipe_id']}/instructions`;
    })

})