document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('form[data-confirm]').forEach(form => {
    form.addEventListener('submit', event => {
      if (!window.confirm(form.dataset.confirm || 'Are you sure?')) event.preventDefault();
    });
  });
  const slider = document.getElementById('length-slider');
  const lengthValue = document.getElementById('length-value');
  if (slider && lengthValue) slider.addEventListener('input', () => { lengthValue.textContent = slider.value; });
  const copyButton = document.getElementById('copy-password');
  const output = document.getElementById('password-output');
  const status = document.getElementById('copy-status');
  if (copyButton && output) copyButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(output.textContent.trim());
      if (status) status.textContent = 'Password copied to clipboard.';
    } catch (_) {
      const range = document.createRange(); range.selectNodeContents(output);
      const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
      if (status) status.textContent = 'Select and copy the highlighted password.';
    }
  });
  window.setTimeout(() => document.querySelectorAll('.message').forEach(el => el.classList.add('message-fade')), 4500);
});
