const textarea = document.querySelector('div textarea');
const form = document.querySelector('div form');

getResponse = (async function (e) {
  e.preventDefault();
  inp = form.querySelector('input');
  response = await fetch(`/get-response/ai`, {
    headers: {
      "question": inp.value
    }
  });
  text = await response.text();
  // output the text to the textarea
  textarea.insertAdjacentText('beforeend', `\n{User} ${inp.value}`)
  textarea.insertAdjacentText('beforeend', `\n{Response} ${text}`);
  return false
});

form.addEventListener('submit', getResponse);
