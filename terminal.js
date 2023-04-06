const textarea = document.querySelector('div textarea');
const form = document.querySelector('div form');
const loading_icon = document.querySelector('.loading-icon');

getResponse = (async function (e) {
  e.preventDefault();
  inp = form.querySelector('input');
  loading_icon.hidden = false;
  response = await fetch(`/get-response/terminal`, {
    headers: {
      "cmd": inp.value
    }
  });
  text = await response.text();
  // output the text to the textarea
  payloadTimeout = setInterval(function() {
    if (text == null) {
      textarea.insertAdjacentText('beforeend', `\n{SYSTEM} The connection to the server was reset or has timed out.`);
      return 465
    } else { clearInterval(payloadTimeout) }
  }, 12000);
  textarea.insertAdjacentText('beforeend', `\n${text}`);
  loading_icon.hidden = true;
  clearInterval(payloadTimeout)
  return false
});

form.addEventListener('submit', getResponse);