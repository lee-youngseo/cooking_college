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
        console.log("responsesDict",responsesDict)
        console.log(responsesDict)
        Object.keys(responsesDict).forEach(function(key){
            console.log(responsesDict[key])
            responseForm.append($(`<div><input type="radio" id="option-${key}" value="${responsesDict[key]}" name="response"/>
                                <label for="option-${key}">${responsesDict[key]}</label></div>`))
        })
        console.log("responsesDict",responsesDict)
        responseParent.append(responseForm)
    }
    let submitButton = $(`<div id="next-problem"></div>`);

    return responseParent;
}

$(function(){

    document.getElementById('quiz-next-button').onclick = function(){
        next_prob = parseInt(problem_id) + 1

        let responseElement = $('<ul>');
        let selectedResponse = getSelectedResponse(responseElement, problem['response_type'])
        let correctResponse = problem['correct_response']

        console.log("selectedResponse",selectedResponse)
        console.log("correctResponse",correctResponse)

        if (next_prob<=3){
            window.location.href = `/test_recipe/${quizz_id}/problems/${next_prob}`
        }
        else window.location.href = `/test_recipe/${quizz_id}/score`
    }
})


$(function(){
    createProblem(problem);
})

function getSelectedResponse(responseElement, responseType) {
    if (responseType === 'ul') {
        let selectedResponse = responseElement.find('input[name="response"]:checked').val();
        return selectedResponse;
    } else {
        return null; // Return null if the response type is not supported
    }
}