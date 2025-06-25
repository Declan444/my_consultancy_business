// index1 script

document.addEventListener("DOMContentLoaded", function () {
    const phrases = [
        "I have 40 years of Business Experience.",
        "Do you have a Business Problem?",
        "Would you like some Help?",
        "Click Take the Quiz to answer 5 questions.",
        "And let's see if I can be of help to your business.",
        
    ];
    let currentPhraseIndex = 0;

    const animatedTextElement = document.getElementById("animated-phrases");

    function updatePhrase() {
        animatedTextElement.textContent = phrases[currentPhraseIndex];
        currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
    }

    updatePhrase();
    setInterval(updatePhrase, 6000); // Change phrases every 8 seconds
});