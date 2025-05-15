// static/js/script.js
document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', () => {
        button.style.opacity = '0.8';
        setTimeout(() => {
            button.style.opacity = '1';
        }, 200);
    });
});