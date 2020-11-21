/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(document).ready(function () {
    $('#inputTelefone').mask('(00) 00000-0000');
    $('#inputCpf').mask('000.000.000-00');
    $('#inputCep').mask('00.000-000');
    $('#inputCepFrete').mask('00.000-000');
    $('#inputNumero').mask('0#');
    $("a[href='#']").attr("href", "javascript:void(0);");
    maximoDeLinhas('maxLines',2);
});

$('.dropdown').hover(function () {
    $(this).find('.dropdown-menu').stop(true, true).delay(100).fadeIn(500);//strop(clearQueue, jumpToEnd)
}, function () {
    $(this).find('.dropdown-menu').stop(true, true).delay(80).fadeOut(500);
});

$(function () {
    $("#starRateAvg").rateYo({
        readOnly: true,
        rating: parseFloat($("#starRateAvg").data('av')),
        maxValue: 5,
        numStars: 5,
        starWidth: "25px"
    });
    var ratingAvg = $("#starRateAvg").rateYo("option", "rating");
    document.getElementById('starRateNumberAvg').innerHTML = "(" + ratingAvg + ")";

    $("#starRate1").rateYo({
        readOnly: true,
        rating: 3,
        maxValue: 5,
        numStars: 5,
        starWidth: "15px"
    });
    var rating1 = $("#starRate1").rateYo("option", "rating");
    document.getElementById('starRate1Number').innerHTML = "(" + rating1 + ")";

    $("#starRate2").rateYo({
        readOnly: true,
        rating: 4,
        maxValue: 5,
        numStars: 5,
        starWidth: "15px"
    });
    var rating2 = $("#starRate2").rateYo("option", "rating");
    document.getElementById('starRate2Number').innerHTML = "(" + rating2 + ")";

    $("#starRate3").rateYo({
        readOnly: true,
        rating: 3.5,
        maxValue: 5,
        numStars: 5,
        starWidth: "15px"
    });
    var rating3 = $("#starRate3").rateYo("option", "rating");
    document.getElementById('starRate3Number').innerHTML = "(" + rating3 + ")";
})

$(function () {

    $('.carousel').carousel({
        interval: 4000
    });

    $('.toast').toast('show');

    $('.alert').alert();

    var quantitiy = 0;
    $('.diminuiQuantidade').click(function (e) {
        campo = $(this).attr('data-field');
        e.preventDefault();
        var quantity = parseInt($('#' + campo + '').val());
        if (quantity > 1) {
            $('#' + campo + '').val(quantity - 1);
        }
    });

    $('.aumentaQuantidade').click(function (e) {
        campo = $(this).attr('data-field');
        e.preventDefault();
        var quantity = parseInt($('#' + campo + '').val());
        if (quantity < 999) {
            $('#' + campo + '').val(quantity + 1);
        }
    });

    $("#finalizarCadastro").click(function () {
        let nomeValido = validaIsEmpty($('#inputNome'));
        let sobrenomeValido = validaIsEmpty($('#inputSobrenome'));
        let emailValido = validaEmail($('#inputEmail'));
        let senhaValida = validaSenha($('#inputSenha'));
        let confirmaSenhaValido = validaConfirmaSenha($('#inputSenha'), $('#inputConfirmaSenha'));
        let cpfValido = validaCpf($('#inputCpf'));
        let telfoneValido = validaTelefone($('#inputTelefone'));
        let nascimentoValido = validaIsEmpty($('#inputNascimento'));
        let sexoValido = validaSexo($('#inputSexo'));
        let cepValido = validaIsEmpty($('#inputCep'));
        let estadoValido = validaIsEmpty($('#inputEstado'));
        let cidadeValido = validaIsEmpty($('#inputCidade'));
        let bairroValido = validaIsEmpty($('#inputBairro'));
        let enderecoValido = validaIsEmpty($('#inputEndereco'));
        let numeroValido = validaIsEmpty($('#inputNumero'));
    })


    $('#avRate1').ready(function () {
        let like = $("#avRate1" + " #like").data("like");
        let dislike = $("#avRate1" + " #dislike").data("dislike");
        $("#avRate1" + " #like").text("(" + like + ")");
        $("#avRate1" + " #dislike").text("(" + dislike + ")");
    });

    $('#avRate2').ready(function () {
        let like = $("#avRate2" + " #like").data("like");
        let dislike = $("#avRate2" + " #dislike").data("dislike");
        $("#avRate2" + " #like").text("(" + like + ")");
        $("#avRate2" + " #dislike").text("(" + dislike + ")");
    });

    $('#avRate3').ready(function () {
        let like = $("#avRate3" + " #like").data("like");
        let dislike = $("#avRate3" + " #dislike").data("dislike");
        $("#avRate3" + " #like").text("(" + like + ")");
        $("#avRate3" + " #dislike").text("(" + dislike + ")");
    });

    $(".likeBtn").click(function () {
        field = $(this).attr('data-field');
        like = $(field + " #like").data("like");
        dislike = $(field + " #dislike").data("dislike");

        if ($(field + " #likeBtn").data('clicked') == 0) {
            $(field + " #likeBtn i").toggleClass('far fas');
            $(field + " #likeBtn").data('clicked', 1);
            like = like + 1;
            if ($(field + " #dislikeBtn").data('clicked') == '1') {
                $(field + " #dislikeBtn i").toggleClass('fas far');
                dislike = dislike - 1;
                $(field + " #dislikeBtn").data('clicked', 0);
            }
        } else {
            $(field + " #likeBtn i").toggleClass('fas far');
            like = like - 1;
            $(field + " #likeBtn").data('clicked', 0);
        }
        $(field + " #like").data('like', like);
        $(field + " #dislike").data('dislike', dislike);
        $(field + " #like").text("(" + like + ")");
        $(field + " #dislike").text("(" + dislike + ")");
    })

    $(".dislikeBtn").click(function () {

        field = $(this).attr('data-field');
        like = $(field + " #like").data("like");
        dislike = $(field + " #dislike").data("dislike");
        if ($(field + " #dislikeBtn").data('clicked') == 0) {
            $(field + " #dislikeBtn i").toggleClass('far fas');
            $(field + " #dislikeBtn").data('clicked', 1);
            dislike = dislike + 1;
            if ($(field + " #likeBtn").data('clicked') == '1') {
                like = like - 1;
                $(field + " #likeBtn").data('clicked', 0);
                $(field + " #likeBtn i").toggleClass('fas far');
            }
        } else {
            $(field + " #dislikeBtn i").toggleClass('fas far');
            dislike = dislike - 1;
            $(field + " #dislikeBtn").data('clicked', 0);
        }
        $(field + " #like").data('like', like);
        $(field + " #dislike").data('dislike', dislike);
        $(field + " #like").text("(" + like + ")");
        $(field + " #dislike").text("(" + dislike + ")");
    })

})



function validaSenha(senha) {

    if (senha.val() == '' || senha.val().toString().length < 4) {
        senha.addClass("is-invalid")
        senha.removeClass("is-valid")
        return false
    }
    else {
        senha.removeClass("is-invalid")
        senha.addClass("is-valid")
        return true
    }
}

function validaConfirmaSenha(senha, confirmaSenha) {
    if (confirmaSenha.val() != senha.val() || confirmaSenha.val() == "") {
        confirmaSenha.addClass("is-invalid")
        confirmaSenha.removeClass("is-valid")
        return false
    }
    else {
        confirmaSenha.removeClass("is-invalid")
        confirmaSenha.addClass("is-valid")
        return true
    }
}

function validaTelefone(telefone) {
    if (telefone.val().toString().length == 15 || telefone.val().toString().length == 14) {
        telefone.removeClass("is-invalid")
        telefone.addClass("is-valid")
        return true
    }
    else {
        telefone.addClass("is-invalid")
        telefone.removeClass("is-valid")
        return false
    }
}

function validaCpf(cpf) {
    let valido = testaCpf(cpf.cleanVal())
    if (valido) {
        cpf.removeClass("is-invalid")
        cpf.addClass("is-valid")
        return true
    }
    else {
        cpf.addClass("is-invalid")
        cpf.removeClass("is-valid")
        return false
    }
}

function testaCpf(cpfTexto) {
    var Soma;
    var Resto;
    Soma = 0;
    if (cpfTexto == "") return false;
    if (cpfTexto == "00000000000") return false;

    for (i = 1; i <= 9; i++) Soma = Soma + parseInt(cpfTexto.substring(i - 1, i)) * (11 - i);
    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(cpfTexto.substring(9, 10))) return false;

    Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(cpfTexto.substring(i - 1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(cpfTexto.substring(10, 11))) return false;
    return true;
}

function validaEmail(email) {
    const regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (regex.test(email.val())) {
        email.removeClass("is-invalid")
        email.addClass("is-valid")
        return true
    }
    else {
        email.addClass("is-invalid")
        email.removeClass("is-valid")
        return false
    }
}


function validaSexo() {
    let sexoM = $("#radioMasculino")
    let sexoF = $("#radioFeminino")
    let sexoI = $("#radioNaoInformar")

    let botoes = $("input[name='inputSexo']:checked")
    if (botoes.length === 0) {
        sexoM.addClass("is-invalid")
        sexoM.removeClass("is-valid")
        sexoF.addClass("is-invalid")
        sexoF.removeClass("is-valid")
        sexoI.addClass("is-invalid")
        sexoI.removeClass("is-valid")
        $("#sexoFeedback").addClass("d-block")
        return false
    }
    else {
        sexoM.removeClass("is-invalid")
        sexoM.addClass("is-valid")
        sexoF.removeClass("is-invalid")
        sexoF.addClass("is-valid")
        sexoI.removeClass("is-invalid")
        sexoI.addClass("is-valid")
        $("#sexoFeedback").removeClass("d-block")
        return true
    }
}

function validaIsEmpty(campo) {

    if (campo.val() == '') {
        campo.addClass("is-invalid")
        campo.removeClass("is-valid")
        return false
    }
    else {
        campo.removeClass("is-invalid")
        campo.addClass("is-valid")
        return true
    }
}

function maximoDeLinhas(classe, numLinhas) {
    var elementos = document.getElementsByClassName(classe);
    for (let i = 0; i < elementos.length; i++) {
        e = elementos[i].children[0]
        $clamp(e, { 'clamp': numLinhas})
    }
    return true;
}