document.addEventListener("DOMContentLoaded", () => {
    const togglePassword = document.querySelector("#togglePassword");
    const passwordInput = document.querySelector("#password");
    const loginForm = document.querySelector("#loginForm");

    togglePassword.addEventListener("click", () => {
        const type = passwordInput.getAttribute("type") === "password" ? "text" : "password";
        passwordInput.setAttribute("type", type);
        const icon = togglePassword.querySelector("i");
        if (type === "text") {
            icon.classList.remove("ph-eye");
            icon.classList.add("ph-eye-slash");
        } else {
            icon.classList.remove("ph-eye-slash");
            icon.classList.add("ph-eye");
        }
    });

    loginForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const btn = document.querySelector(".btn-login");
        btn.textContent = "Preparando o cafe...";
        btn.style.opacity = "0.8";
        setTimeout(() => {
            window.location.href = "cardapio.html";
        }, 1500);
    });
});
