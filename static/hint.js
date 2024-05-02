function displayHint(hintID, hint){
    let hints = [displayHintOne(), displayHintTwo(), displayHintThree(), displayHintFour(), displayHintFive()];
    $('.subtitle').append(`${hint['name']}`);
    $('#hint-container').append(hints[hintID]);
}

function displayHintOne(){

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
    displayHint(hintID, hint)

})