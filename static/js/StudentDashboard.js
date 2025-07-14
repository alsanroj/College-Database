function showSection(section) {
  document.getElementById("dashboardSection").classList.add("d-none");
  document.getElementById("profileSection").classList.add("d-none");
  document.getElementById(section + "Section").classList.remove("d-none");
}

function previewImage(event) {
  const img = document.getElementById("preview");
  img.src = URL.createObjectURL(event.target.files[0]);
  img.classList.remove("d-none");
}

document
  .getElementById("combinedForm")
  .addEventListener("submit", function (e) {
    e.preventDefault();
    document.getElementById("successAlert").classList.remove("d-none");
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
