document.addEventListener("DOMContentLoaded", function () {
    const signupBtn = document.getElementById("signup-btn");
    const signinBtn = document.getElementById("signin-btn");
    const signupFormContainer = document.getElementById("signup-id");
    const signinFormContainer = document.getElementById("signin-id");

    // Initial display settings
    signupFormContainer.style.display = "none";
    signinFormContainer.style.display = "block";

    signupBtn.addEventListener("click", function (event) {
      event.preventDefault();
      signinFormContainer.style.display = "none";
      signupFormContainer.style.display = "block";
    });

    signinBtn.addEventListener("click", function (event) {
      event.preventDefault();
      signupFormContainer.style.display = "none";
      signinFormContainer.style.display = "block";
    });
  });