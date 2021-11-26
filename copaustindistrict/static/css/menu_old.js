  
/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    const x = document.getElementById("myTopnav");
    const menuBtn =
        document.querySelector(".menu-btn");
    if (x.className === "topnav") {
        x.className += " responsive";
        menuBtn.classList.add("close");
    } else {
        x.className = "topnav";
        menuBtn.classList.remove("close");
    }
}
