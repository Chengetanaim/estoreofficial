const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const signup = document.querySelector(".signup");

sign_in_btn.addEventListener("click", () => {
    signup.classList.remove("sign-up-mode");
});

sign_up_btn.addEventListener("click", () => {
    signup.classList.add("sign-up-mode");
});