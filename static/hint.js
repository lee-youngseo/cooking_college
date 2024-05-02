function displayHint(hintID, hint){
    let hints = [displayHintOne(), displayHintTwo(), displayHintThree(), displayHintFour()];
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

$(function(){
    displayHint(hintID, hint)

})