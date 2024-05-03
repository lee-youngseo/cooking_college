function displayHints(hints){
    let listElement = $(`<ul id="hint-items"></ul>`);
    for(const[key,value] of Object.entries(hints)){
        console.log(key, value)
        let listItem = `<li id=hint-${key}><a href="/hints/${key}">${value['name']}</a></li>`
        listElement.append(listItem);
    }
    $('#hints-container').append(listElement);
}


$(function(){
    displayHints(hints);
})