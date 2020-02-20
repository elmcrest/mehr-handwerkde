// dynamically addEventListener, the in-tag 'onclick' doesn't work
document
  .querySelector("#burgerCloseArea")
  .addEventListener("click", burgerMenu);
function burgerMenu() {
  burgerIncredients = [
    ...document.querySelectorAll(
      "#burgerContent",
      "#burgerOpenIcon",
      "#burgerCloseArea",
      "#burgerCloseIcon"
    )
  ];
  burgerIncredients = [
    document.querySelector("#burgerContent"),
    document.querySelector("#burgerOpenIcon"),
    document.querySelector("#burgerCloseArea"),
    document.querySelector("#burgerCloseIcon")
  ];
  burgerIncredients.forEach(element => {
    element.classList.toggle("hidden");
  });
}
