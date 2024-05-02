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
                if (problem['points'] === 1){
                    points = points + 1;
                } else  if (problem['points'] === 3){
                    points = points + 1/3; 
                }
                draggable.draggable('disable');
            } else {
                if (problem['points'] === 1){
                    points = points - 1;
                } else  if (problem['points'] === 3){
                points = points - 1/3 
                }
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

    if(responseType === 'dl'){
        let submitButton = $(`<br> <div class = "button-container">
        <button id="quiz-next-button" class="navbar-link" type="submit">Finished Chopping!</button>
        </div>`);
        // $(`<button id="cooking-mama-button" type="submit">Finished Chopping!</button>`);
        responseForm.append(submitButton);
        responseParent.append(responseForm)
    }

    else if(responseType === 'ul'){
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

let mama_score = 1.0;
let currChopped = 0.0;
function createChopping(problem) {
    // Check if the prompt matches a specific string
    if (problem.q_type === 'chop') {

        console.log("its choppy")
        
        let game_container = document.createElement('div');
        game_container.className = 'quiz_box';


        let knifeElement = document.createElement('img');
        knifeElement.id = 'knife';
        knifeElement.src = 'https://png.pngtree.com/png-clipart/20220730/ourmid/pngtree-cartoon-knife-png-image_6093279.png';
        knifeElement.width = '100';
        knifeElement.draggable = true;

        // Append the knife element to the questions-container div
        game_container.appendChild(knifeElement);
        let currScallion = 1;
        
        // Get the scallion image element
        let scallionElement = document.createElement('img');
        scallionElement.id = 'scallion';
        scallionElement.src = cooking_mama[quizId]['images'][currScallion]; // Initialize with the first image
        scallionElement.width = '250';
        scallionElement.height = '100';
        game_container.appendChild(scallionElement);

        // Create a side panel for chopped images
        let sidePanel = document.createElement('div');
        sidePanel.id = 'chopped-panel';
        sidePanel.style.float = 'right';
        sidePanel.style.width = '400px';
        game_container.appendChild(sidePanel);

        document.getElementById('alternative-container').appendChild(game_container);

        // Add dragstart event listener to the knife element
        knifeElement.addEventListener('dragstart', (event) => {
            // Set data to be transferred during drag
            event.dataTransfer.setData('text/plain', 'knife');
        });

        // Add dragover event listener to the scallion element
        scallionElement.addEventListener('dragover', (event) => {
            
            event.preventDefault();
        });

        // Add drop event listener to the scallion element
        scallionElement.addEventListener('drop', (event) => {
            // Prevent default behavior
            event.preventDefault();

            // Get the data that was transferred during drag
            const data = event.dataTransfer.getData('text/plain');

            // Check if the dropped item is the knife
            if (data === 'knife' && currScallion<=6) {
                // Change the scallion image source to the next image in the sequence
                currScallion +=1
                scallionElement.src = cooking_mama[quizId]['images'][currScallion];

                // Clear the side panel before adding the new chopped image
                sidePanel.innerHTML = '';

                // Display corresponding chopped image in the side panel
                let choppedImage = document.createElement('img');
                currChopped += 1
                choppedImage.src = cooking_mama[quizId]['choppedImages'][currChopped];
                choppedImage.width = '100';
                if (currChopped >=4){
                    choppedImage.width = '220';
                }
                sidePanel.appendChild(choppedImage);
            }
        });

    }
}

$(function() {
    if (typeof dragItems !== 'undefined' && dragItems && typeof dropImage !== 'undefined' && dropImage) {
        console.log("Draggable problem");
        createDraggableProblem(problem, dragItems, dropImage);
    } else {
        console.log("Normal problem");
        createProblem(problem);
        createChopping(problem);
    }

    $('#quiz-response-form').on('submit', function(event) {
        event.preventDefault();
        console.log("A button was pressed for the quiz");

        let nextProblem = parseInt(problemId) + 1;
        let point = { 'point': 0 };

        if (problem['response_type'] === 'ul') {
            let selectedResponse = parseInt($('input[name="response"]:checked').val()); // Safely get the value
            let correctResponse = parseInt(problem['correct_response']);
            point['point'] = (selectedResponse === correctResponse) ? 1 : 0;
            console.log("In MCQ if");
        } else if (problem['response_type'] === 'drag') {
            point['point'] = points;
            console.log("In drag if");
        } else if (problem['response_type'] === 'dl') {
            point['point'] = mama_score;
        }

        if (problem['response_type'] === 'dl' && currChopped !== Object.keys(cooking_mama[quizId]['choppedImages']).length) {
            console.log("going to send alert")
            alert("Nope, there's still more to chop! Keep going (-0.2 pts)");
            mama_score -= 0.2;
        } else {
            console.log("otherwise")
            $.ajax({
                type: 'POST',
                url: window.location.pathname,
                dataType: 'json',
                contentType: 'application/json; charset=utf-8',
                data: JSON.stringify(point),
                success: function(result) {
                    console.log('Redirecting to next problem:', nextProblem);

                    if (nextProblem <= totalProblems) {
                        window.location.href = `/test_recipe/${quizId}/problems/${nextProblem}`;
                    } else {
                        window.location.href = `/test_recipe/${quizId}/score`;
                    }
                },
                error: function(request, status, error) {
                    console.error("Error on AJAX call:", error);
                }
            });
        }
    });
});
