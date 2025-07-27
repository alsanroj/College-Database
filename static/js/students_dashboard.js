// Tab switching functionality
document
  .getElementById("dashboardLink")
  .addEventListener("click", function (e) {
    e.preventDefault();
    document.getElementById("dashboardSection").classList.add("active");
    document.getElementById("profileSection").classList.remove("active");
    this.classList.add("bg-danger", "active");
    document
      .getElementById("profileLink")
      .classList.remove("bg-danger", "active");
  });

document.getElementById("profileLink").addEventListener("click", function (e) {
  e.preventDefault();
  document.getElementById("profileSection").classList.add("active");
  document.getElementById("dashboardSection").classList.remove("active");
  this.classList.add("bg-danger", "active");
  document
    .getElementById("dashboardLink")
    .classList.remove("bg-danger", "active");
});

// Form submission
document
  .getElementById("studentInfoForm")
  .addEventListener("submit", function (e) {
    // Let the form submit normally to the backend
  });

