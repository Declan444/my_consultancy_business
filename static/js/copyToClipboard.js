// static/js/copyToClipboard.js
document.getElementById('copy-button').addEventListener('click', function () {
    // Get the SWOT analysis text
    const swotText = document.getElementById('swot-result').innerText;

    // Use the Clipboard API to copy the text
    navigator.clipboard.writeText(swotText)
        .then(() => {
            alert('SWOT analysis copied to clipboard!');
        })
        .catch((err) => {
            alert('Failed to copy: ' + err);
        });
});