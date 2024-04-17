function createProblem(problem){
    let promptElement = $(`<div id="quiz-prompt">${problem['prompt']}</div><br>`);
    let responseElement = createResponse(problem['response_type']);
    let imageElement = $(`<div class="image-container"></div>`);
    let nextButton = $(`<div id='next-problem'></div>`)

    $('#questions-container').append([promptElement, responseElement]);
}

function createResponse(responseType){
    let responseParent = $(`<div id=quiz-response></div>`);
    let responseForm = $(`<form id="quiz-response-form"></form>`)

    if(responseType === 'ul'){
        let responsesDict = problem['responses']
        console.log(responsesDict)
        Object.keys(responsesDict).forEach(function(key){
            console.log(responsesDict[key])
            responseForm.append($(`<div><input type="radio" id="option-${key}" value="${responsesDict[key]}" name="response"/>
                                <label for="option-${key}">${responsesDict[key]}</label></div>`))
        })
        responseParent.append(responseForm)
    }
    let submitButton = $(`<div id="next-problem"></div>`);

    return responseParent;
}
$(function(){
    createProblem(problem);
})