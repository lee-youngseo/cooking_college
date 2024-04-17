function createProblem(problem){
    let promptElement = $(`<div id="quiz-prompt">${problem['prompt']}</div><br>`);
    let responseElement = createResponse(problem['response_type']);
    let imageElement = $(`<div class="image-container"></div>`);

    $('#questions-container').append([promptElement, responseElement]);
}

function createResponse(responseType){
    let responseParent = $(`<div id=quiz-response></div>`);
    let responseForm = $(`<form id="quiz-response-form"></form>`)

    if(responseType === 'ul'){
        let responsesDict = problem['responses']
        Object.keys(responsesDict).forEach(function(key){
            responseForm.append($(`<div><input type="radio" id="option-${key}" value="${key}" name="response"/>
                                <label for="option-${key}">${responsesDict[key]}</label></div>`))
        })
        let submitButton = $(`<button id="quiz-next-button" type="submit">Next</button>`);
        responseForm.append(submitButton);
        responseParent.append(responseForm)
    }

    return responseParent;
}

$(function(){
    createProblem(problem);

    $('#quiz-response-form').on('submit', function(event){
        let nextProblem = parseInt(problem_id)+1;

        let selectedResponse = parseInt(document.querySelector('input[name="response"]:checked').value);
        let correctResponse = parseInt(problem['correct_response']);
        let point = selectedResponse === correctResponse?{'point':1}:{'point':0};

        $.ajax({
            type: 'POST',
            url: window.location.href,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(point),
            success: function(result){
                if(nextProblem <= totalProblems) window.location.href = `/test_recipe/${quiz_id}/problems/${nextProblem}`;
                else window.location.href = `/test_recipe/${quiz_id}/score`;

            }, error: function(request, status, error){
                console.log("Error");
                console.log(request);
                console.log(status);
                console.log(error);
            }
        })

        event.preventDefault();
    })
})
