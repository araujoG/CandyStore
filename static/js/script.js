/// <reference path="../../typings/globals/jquery/index.d.ts" />

$(document).ready(function () {
    $('#inputTelefone').mask('(00) 00000-0000');
    $('#inputCpf').mask('000.000.000-00');
    $('#inputCep').mask('00.000-000');
    $('#inputNumero').mask('0#')
});

$(function () {
    $('.carousel').carousel({
        interval: 4000
    })

    $('.toast').toast('show');

    $('.alert').alert()

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
        let nomeValido = validaIsEmpty($('#inputNome'))
        let sobrenomeValido = validaIsEmpty($('#inputSobrenome'))
        let emailValido = validaEmail($('#inputEmail'))
        let senhaValida = validaSenha($('#inputSenha'))
        let confirmaSenhaValido = validaConfirmaSenha($('#inputSenha'), $('#inputConfirmaSenha'))
        let cpfValido = validaCpf($('#inputCpf'))
        let telfoneValido = validaTelefone($('#inputTelefone'))
        let nascimentoValido = validaIsEmpty($('#inputNascimento'))
        let sexoValido = validaSexo($('#inputSexo'))
        let cepValido = validaIsEmpty($('#inputCep'))
        let estadoValido = validaIsEmpty($('#inputEstado'))
        let cidadeValido = validaIsEmpty($('#inputCidade'))
        let bairroValido = validaIsEmpty($('#inputBairro'))
        let enderecoValido = validaIsEmpty($('#inputEndereco'))
        let numeroValido = validaIsEmpty($('#inputNumero'))

        

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
    if (confirmaSenha.val() != senha.val() || confirmaSenha.val()=="") {
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