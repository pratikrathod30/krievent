
        document.addEventListener("DOMContentLoaded", function () {
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
        });

        document.addEventListener("DOMContentLoaded", function () {
            const cardImage = document.querySelector(".card-img");
            if (cardImage) {
                setTimeout(() => cardImage.classList.add("loaded"), 500);
            }
        });

        var myCarousel = document.querySelector('#carouselExampleCaptions');
        var carousel = new bootstrap.Carousel(myCarousel, {
            interval: 2000, // Change image every 2 seconds
            ride: 'carousel'
        });
    