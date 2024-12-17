document.getElementById("password_visibility_toggle").addEventListener("click", function () {
    this.classList.toggle("bi-eye");
    this.classList.toggle("bi-eye-slash");

    var passwordInput = document.getElementById("password");

    if (this.classList.contains("bi-eye-slash")) {
        passwordInput.type = "password"
    }
    else {
        passwordInput.type = "text"
    }
});