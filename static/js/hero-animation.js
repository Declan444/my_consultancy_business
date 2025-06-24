// index1 script

document.addEventListener("DOMContentLoaded", function () {
    const phrases = [
        "I have 40 years of Business Experience.",
        "Do you have a Business Problem?",
        "Would you like some Help?",
        "Take the Quiz to answer 5 questions.",
        "And let's see if I can help you.",
        
    ];
    let currentPhraseIndex = 0;

    const animatedTextElement = document.getElementById("animated-phrases");

    function updatePhrase() {
        animatedTextElement.textContent = phrases[currentPhraseIndex];
        currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;
    }

    updatePhrase();
    setInterval(updatePhrase, 8000); // Change phrases every 8 seconds
});