document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();
    document.querySelector(".message-success").style.display = "block";
    setTimeout(() => {
        document.querySelector(".message-success").style.display = "none";
    }, 3000);
    this.reset();
});