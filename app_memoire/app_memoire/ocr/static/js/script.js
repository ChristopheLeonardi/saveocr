$(document).ready(function(){
    choose_term()
    form_click_action()
})




function choose_term() {
    $('.select-result').click(function(e){
        var selected_term = $(e.target).attr("data-term")
        document.getElementById("text_search").value = selected_term
        $("input[type='submit']").click()
        e.preventDefault()
    })
}

function form_click_action(){
    $('label[for="id_image"]').click(function(e){
        $(e.target).addClass("check")
        console.log("click")
    })
}
