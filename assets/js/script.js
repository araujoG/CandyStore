$(function(){
    $('[data-toggle = "tooltip"]').tooltip();
    /*procura estruturas com o atrivuto data-toogle = tooltip e executa o método .tooltip() em todas elas */
    $('[data-toggle = "popover"]').popover();
})
$('.carousel').carousel({
    interval: 4000
  })