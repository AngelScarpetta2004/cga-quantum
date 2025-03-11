document.addEventListener("DOMContentLoaded", function () {
    const titleText = "Quantum";
    const titleElement = document.getElementById("title");
    titleElement.innerHTML = titleText
        .split("")
        .map(letter => `<span>${letter}</span>`)
        .join("");

    // Animación de entrada para las cards del equipo
    const teamCards = document.querySelectorAll(".card.team-member");
    teamCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = "1";
            card.style.transform = "translateY(0) scale(1)";
        }, index * 400);
    });
});

document.addEventListener("scroll", () => {
    const scrollPosition = window.scrollY;
    const titleContainer = document.querySelector(".title-container");
    const aboutSection = document.querySelector(".about-section");
    const missionVisionSection = document.querySelector(".mission-vision-section");
    const nichesSection = document.querySelector(".niches-section");
    const valuesSection = document.querySelector(".values-section");
    const teamSection = document.querySelector(".team-section");
    const nav = document.querySelector("nav");

    // Desvanecer el título mientras se hace scroll
    titleContainer.style.opacity = Math.max(1 - scrollPosition / 200, 0);

    // Mostrar "Sobre Nosotros" primero y la barra de navegación
    if (scrollPosition > 50) {
        aboutSection.classList.add("show");
        nav.classList.add("show");
    } else {
        aboutSection.classList.remove("show");
        nav.classList.remove("show");
    }

    // Mostrar "Misión" y "Visión" al bajar más
    if (scrollPosition > 300) {
        missionVisionSection.classList.add("show");
        aboutSection.classList.remove("show");
    } else {
        missionVisionSection.classList.remove("show");
    }

    // Mostrar "Nichos" al bajar aún más
    if (scrollPosition > 600) {
        nichesSection.classList.add("show");
        missionVisionSection.classList.remove("show");
    } else {
        nichesSection.classList.remove("show");
    }

    // Mostrar "Valores" al bajar aún más
    if (scrollPosition > 900) {
        valuesSection.classList.add("show");
        nichesSection.classList.remove("show");
    } else {
        valuesSection.classList.remove("show");
    }

    // Mostrar "Equipo" al bajar aún más
    if (scrollPosition > 1200) {
        teamSection.classList.add("show");
        valuesSection.classList.remove("show");
    } else {
        teamSection.classList.remove("show");
    }
});