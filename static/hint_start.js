function displayHints(hints){
    let listElement = $(`<ul id="hint-items"></ul>`);
    for(const[key,value] of Object.entries(hints)){
        console.log(key, value)
        let listItem = `<li id=hint-${key} class="hint-start">${value['name']}</li>`
        listElement.append(listItem);
    }
    $('#hints-container').append(listElement);
}


$(function(){
    displayHints(hints);

    $('.hint-start').on('click', function(){
        console.log('hi');
        let id = this.id.replace(/\D/g,"");
        window.location.href = `/hints/${id}`
    })
})