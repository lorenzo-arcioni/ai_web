document.addEventListener('DOMContentLoaded', () => {
    // Codice esistente per l'animazione delle card
    const cards = document.querySelectorAll('.category-card');
    cards.forEach((card) => {
        const depth = parseInt(card.dataset.depth) || 0;
        card.style.animationDelay = `${0.1 * (depth + 1)}s`;
        card.style.opacity = 1;
    });
    
    // Nuovo codice per la navigazione attiva
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (currentPath === linkPath || 
            (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.classList.add('active');
        }
    });
});