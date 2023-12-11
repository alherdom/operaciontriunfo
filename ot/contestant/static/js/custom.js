// document.addEventListener("DOMContentLoaded", (event) => {
//     document
//       .querySelector("#arrival-search-btn")
//       .addEventListener("click", (event) => {
//         event.preventDefault();
//         const arrivalToCity = document.querySelector("#arrival-to-city").value;
//         window.location.href = `/flights/arr/${arrivalToCity}/`;
//       });
//   });

document.addEventListener("DOMContentLoaded", function () {
  var inputSearch = document.getElementById("inputSearch");
  var searchHelp = document.getElementById("searchHelp");

  inputSearch.addEventListener("focus", function () {
      searchHelp.style.display = "block";

      setTimeout(function () {
          searchHelp.style.display = "none";
      }, 2000); 
  });
});
