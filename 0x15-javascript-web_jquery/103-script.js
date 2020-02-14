const url = 'https://fourtonfish.com/hellosalut/?lang=';
$(() => {
  $('INPUT#btn_translate').click(() =>
    $.get(url + $('INPUT#language_code').val(), (data) =>
      $('DIV#hello').html(data.hello)));
  $('INPUT#language_code').keydown((e) => {
    if (e.which === 13) {
      $.get(url + $('INPUT#language_code').val(), (data) =>
        $('DIV#hello').html(data.hello));
    } else return true;
  });
});
