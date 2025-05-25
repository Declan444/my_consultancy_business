document.addEventListener("DOMContentLoaded", function () {
    console.log("AOS Initialized");
    AOS.init({
      offset: 100, // Distance before the animation starts
      duration: 1000, // Animation duration
      once: true, // Animation runs only once
      debug: true, // Show some logs
      
    });
  });
  