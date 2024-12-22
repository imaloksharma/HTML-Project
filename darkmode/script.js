const modeToggle = document.getElementById("modeToggle");
const navbar = document.getElementById("navbar");

modeToggle.addEventListener("click", () => {
    navbar.classList.toggle("dark-mode");
    navbar.classList.toggle("light-mode");
});
