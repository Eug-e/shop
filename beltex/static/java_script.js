
$(document).ready(function() {
    $('#btn').click(function(e){
    x = $("#volume").val()
    if (x.indexOf('0')!=-1) {
        alert ('введите число')
        e.preventDefault()
    }
 })
})


$(document).ready(function() {
    $('#id48').click(function(e){
        $.post(
            "line11",
            {
                'a':'hello'
            },
            function (response){
                alert(response.message)
            }
        );
    })
});

$(document).ready(function() {
    $('#id49').click(function(e){
        $.post(
            "line12",
            {
                'a':'15'
            },
            function (response){
                alert(response.mess)
            }
        );
    })
});
