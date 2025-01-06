async function fetchMessage() {
    try {
        console.log("Fetching message...");

        const messageContainer = document.getElementById("message-container");
        const imagePlaceholder = document.getElementById("image-placeholder");

        // Check if elements exist
        if (!messageContainer || !imagePlaceholder) {
            throw new Error("Required DOM elements are missing.");
        }

        const response = await fetch("/get-random-message/");
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log("Fetched message:", data);
        console.log("Message content:", data.message);
        console.log("Image URL:", data.image_url);

        // Update the DOM with the fetched data
        messageContainer.textContent = data.message || "No message available.";
        if (data.image_url) {
            imagePlaceholder.src = data.image_url;
            imagePlaceholder.alt = data.message || "Random image";
        } else {
            imagePlaceholder.src = "";
            imagePlaceholder.alt = "No image available.";
        }
    } catch (error) {
        console.error("Error fetching message:", error);
    }
}

// Run the fetchMessage function every 30 seconds
document.addEventListener("DOMContentLoaded", () => {
    fetchMessage(); // Fetch the first message immediately
    setInterval(fetchMessage, 10000); // Fetch a new message every 30 seconds//
});
