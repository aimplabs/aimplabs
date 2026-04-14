/**
 * Navbar mobile menu toggle
 */

function setsidenav() {
    let menu = document.querySelector(".menu-icon");

    if (menu.childNodes[1].textContent == 'menu') {
        menu.childNodes[1].textContent = 'close';
        document.querySelector('.jv-navlinks').style.display = 'flex';
    } else if (menu.childNodes[1].textContent == 'close') {
        menu.childNodes[1].textContent = 'menu';
        document.querySelector('.jv-navlinks').style.display = 'none';
    }
}

// Apply media query listener for responsive behavior
var x = window.matchMedia("(max-width: 500px)");
removeNavRt(x); // Call listener function at run time
