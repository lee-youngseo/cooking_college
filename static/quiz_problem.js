function createProblem(problem){
    let promptElement = $(`<div id="quiz-prompt">${problem['prompt']}</div><br><br>`);
    let responseElement = createResponse(problem['response_type']);
    $('#questions-container').append([promptElement, responseElement]);
}

function createDraggableProblem(problem, dragItems, dropImage) {
    let promptElement = $(`<div id="quiz-prompt">${problem['prompt']}</div>`);
    let dropElement = $(`<img src="${dropImage}" id="droppable" class="drop-image">`);
    let dragElement = $(`<div id="draggable-list"></div>`);
    let responseElement = createResponse(problem['response_type']);

    Object.keys(dragItems).forEach(function(key){
        let dragItem = $(`<img src="${dragItems[key]}" class="draggable" data-key="${key}">`);
        dragElement.append(dragItem);
    });

    $('#questions-container').append([promptElement, dropElement, dragElement, responseElement]);

    setupDragAndDrop();

}

function setupDragAndDrop(){
    $('.draggable').draggable({
        revert: 'invalid',
    });

    $('#droppable').droppable({
        drop: function(event, ui){
            let draggable = ui.draggable;
            let key = draggable.data('key');
            droppedItems[key] = true;
            currentDroppedItem = key;
            if (checkCurrentDroppedItem(problem['correct_response'])){
                points = points + 1/3;
                draggable.draggable('disable');
            } else {
                alert("Incorrect item dropped");
                draggable.hide();
            }
        }
    });
}

function checkCurrentDroppedItem(correctResponse){
    let currentKey = currentDroppedItem;
    return correctResponse.includes(currentKey);
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
        let submitButton = $(`<br> <div class = "button-container">
        <button id="quiz-next-button" class="navbar-link" type="submit">Next</button>
        </div>`);
        responseForm.append(submitButton);
        responseParent.append(responseForm)
    }

    else if(responseType === 'drag'){
        console.log("Draggable response");
        let submitButton = $(`<br> <div class = "button-container">
        <button id="quiz-next-button" class="navbar-link" type="submit">Next</button>
        </div>`);
        responseForm.append(submitButton);
        responseParent.append(responseForm)
    }

    return responseParent;
}

$(function() {

    if (typeof dragItems !== 'undefined' && dragItems && typeof dropImage !== 'undefined' && dropImage) {
        console.log("Draggable problem");
        createDraggableProblem(problem, dragItems, dropImage);
    } else {
        console.log("Normal problem");
        createProblem(problem);
    }

    $('#quiz-response-form').on('submit', function(event){
        event.preventDefault();

        let nextProblem = parseInt(problemId)+1;
        let point = { 'point': 0 };

        if(problem['response_type'] === 'ul'){
            let selectedResponse = parseInt($('input[name="response"]:checked').val()); // Safely get the value
            let correctResponse = parseInt(problem['correct_response']);
            point['point'] = selectedResponse === correctResponse ? 1 : 0;
        } else if(problem['response_type'] === 'drag'){
            point['point'] = points;
        }
        
        $.ajax({
            type: 'POST',
            url: window.location.pathname,
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(point),
            success: function(result){
                console.log('Redirecting to next problem:', nextProblem);

                if(nextProblem <= totalProblems) {
                    window.location.href = `/test_recipe/${quizId}/problems/${nextProblem}`;
                } else {
                    window.location.href = `/test_recipe/${quizId}/score`;
                }

            }, error: function(request, status, error){
                console.error("Error on AJAX call:", error);
            }
        });
    });
});
