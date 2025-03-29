document.addEventListener('DOMContentLoaded', (event) => {
    // Syntax highlighting
    hljs.highlightAll();

    // Fade in content
    const content = document.querySelector('.prose');
    content.style.opacity = 1;

    // MathJax rendering
    if (window.MathJax) {
        MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    }
});