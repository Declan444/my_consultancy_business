document.addEventListener('DOMContentLoaded', function() {
    console.log('Testimonial animation script loaded');
    const heading = document.querySelector('.animated-heading');
    console.log('Heading element:', heading);
    
    if (!heading) return; 
    
    const text = 'Testimonials';
    heading.innerHTML = '';
    
    text.split('').forEach((letter, index) => {
        console.log('Creating span for letter:', letter);
        const span = document.createElement('span');
        span.textContent = letter;
        span.className = 'animated-letter'; // Add a class for debugging
        heading.appendChild(span);
    });
});