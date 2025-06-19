
$('.success').hide()

$('#form_state').submit((e)=>{
    e.preventDefault()

    console.log($('#poussee').val())

    let valeurs = $('input[name="aliments"]:checked')
    .map(function () {
        return $(this).val();
    })
    .get();

    valeurs = valeurs.join(", ")

    let coloscopie = $('#coloscopie').val()
    let sang = $('#sang').val()
    let echo = $('#echo').val()


    let poussee = $('#poussee').val()
    let symp = $('input[name="symp"]:checked')
    .map(function () {
        return $(this).val();
    })
    .get()

    symp = symp.join(", ")

    $.ajax({
        type:'POST',
        url:'/post-state/',
        data:{
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            aliments:valeurs,
            coloscopie,
            sang,
            echo,
            poussee,
            symp
        },
        success:(response)=>{
            if(response.done){
                $('.success').slideDown()
                setTimeout(() => {
                    $('.success').slideUp()
                }, 5000);
            }
        }
    })


})




$('.form-operation').submit((e)=>{
    e.preventDefault()
    let type = $('#type').val()
    let date = $('#date').val()
    let detail = $('#detail').val()

    $.ajax({
        type:'POST',
        url:'/post-operation/',
        data:{
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            type,
            date,
            detail            
        },
        success:(response)=>{
            if(response.done){
                $('.success').slideDown()
                setTimeout(() => {
                    $('.success').slideUp()
                }, 5000);
            }
        }
    })

})