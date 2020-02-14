const url = 'https://fourtonfish.com/hellosalut/?lang=';
$(() =>
  $('INPUT#btn_translate').click(() =>
    $.get(url + $('INPUT#language_code').val(), (data) =>
      $('DIV#hello').html(data.hello))));
