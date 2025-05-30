document.addEventListener('DOMContentLoaded', function() {
    const showPasswordCheckbox = document.getElementById('showPassword');
    const passwordInput = document.getElementById('password');
    const rePasswordInput = document.getElementById('rePassword');

    showPasswordCheckbox.addEventListener('change', function() {
        if (this.checked) {
            passwordInput.type = 'text';
            rePasswordInput.type = 'text';
        } else {
            passwordInput.type = 'password';
            rePasswordInput.type = 'password';

        }
    });
});

function toggleMenu() {
    const navLinks = document.getElementById("navLinks");
    const menuIcon = document.getElementById("menu-icon");
    const closeIcon = document.getElementById("close-icon");
  
    const isActive = navLinks.classList.toggle("active");
    menuIcon.style.display = isActive ? "none" : "inline";
    closeIcon.style.display = isActive ? "inline" : "none";
  }
  
  