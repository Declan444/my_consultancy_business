document.addEventListener("DOMContentLoaded", () => {
    // Initialize random message fetching
    fetchMessage(); // Fetch the first random message immediately
    setInterval(fetchMessage, 30000); // Fetch a new message every 30 seconds

    // Function to fetch a random testimonial
    function fetchRandomTestimonial() {
        fetch("/testimonials/random/")
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    console.error(data.error);
                } else {
                    // Update the testimonial placeholders
                    const testimonialText = document.getElementById("testimonial-text");
                    const testimonialName = document.getElementById("testimonial-name");
                    const testimonialCompany = document.getElementById("testimonial-company");

                    if (testimonialText && testimonialName) {
                        testimonialText.textContent = data.text || "No testimonial available.";
                        testimonialName.textContent = data.name || "Anonymous";

                        if (data.company) {
                            testimonialCompany.textContent = `, ${data.company}`;
                        } else {
                            testimonialCompany.textContent = ""; // Clear if no company
                        }
                    }
                }
            })
            .catch((error) => console.error("Error fetching testimonial:", error));
    }

    // Initialize random testimonial fetching
    fetchRandomTestimonial(); // Fetch the first random testimonial immediately
    setInterval(fetchRandomTestimonial, 10000); // Fetch a new testimonial every 10 seconds
});

// Fetch a random message from the server
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
