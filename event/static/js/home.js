document.addEventListener("DOMContentLoaded", function () {
    // Reveal on Scroll Effect
    const revealElements = document.querySelectorAll(".reveal");

    function revealOnScroll() {
        revealElements.forEach((el) => {
            if (el.getBoundingClientRect().top < window.innerHeight - 50) {
                el.style.opacity = 1;
                el.style.transform = "translateY(0)";
            }
        });
    }

    window.addEventListener("scroll", revealOnScroll);
    revealOnScroll();

    // Image Load Animation
    const cardImage = document.querySelector(".card-img");
    if (cardImage) {
        setTimeout(() => {
            cardImage.classList.add("loaded");
            console.log("rathod.jpg loaded successfully!");
        }, 500);
    }

    // Bootstrap Carousel
    var myCarousel = document.querySelector('#carouselExampleCaptions');
    if (myCarousel) {
        new bootstrap.Carousel(myCarousel, {
            interval: 2000, // Change image every 2 seconds
            ride: 'carousel'
        });
    }
});
