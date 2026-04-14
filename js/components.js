/**
 * Reusable HTML Components (Navbar, Footer)
 * Loaded dynamically at DOMContentLoaded
 */

const navbarHTML = `
<header class="jv-navbar-container">
    <nav class="jv-navbar-flex">
        <div class="jv-logo-container">
            <img class="jv-brand-logo" src="assets/brand_imgs/aimplogo_small.png" alt="AIMP Logo">
            <div class="jv-brand-statements">
                <div class="jv-brand-name"><a href="index.html">AIMP LABS</a></div>
                <div class="jv-brand-desc"><a href="index.html">Private AI Research & Training Center</a></div>
            </div>
        </div>
        <div class="menu-icon" onclick="setsidenav()">
            <span class="material-symbols-outlined">menu</span>
        </div>    
        <ul class="jv-navlinks">
            <li><a href="innovations.html" class="jv-navlink">Innovations</a></li>
            <li><a href="training.html" class="jv-navlink">Training</a></li>
            <li><a href="archives.html" class="jv-navlink">Archives</a></li>
            <li><a href="blogs.html" class="jv-navlink">Blogs</a></li>
        </ul>
    </nav>
</header>
`;

const footerHTML = `
<footer class="jv-footer-container-align">
    <div class="jv-footer-container">
        <ul class="jv-footer-container-left">
            <li>
                <a href="https://github.com/aimplabs"><i class="fa-brands fa-github" style="color: gray;"></i> <span class="jv-ftnotes-icontxt">Codes/Data</span></a>
            </li>
            <li>
                <a href="https://twitter.com/aimplabs"><i class="fa-brands fa-twitter" style="color: #1DA1F2 ;"></i> <span class="jv-ftnotes-icontxt">Get updates/news</span></a>
            </li>
            <li>
                <a href="https://youtube.com/@aimplabs"> <i class="fa-brands fa-youtube" style="color: red;"></i> <span class="jv-ftnotes-icontxt">Video tutorials</span></a>
            </li>
            <li>
                <a href="https://www.facebook.com/aimplabs"> <i class="fa-brands fa-facebook" style="color: #1877F2;"></i> <span class="jv-ftnotes-icontxt">Trends & News</span></a>
            </li>             
        </ul>
        <div class="jv-footer-container-middle">
            <div class="jv-footer-brand-statements">
                <div class="jv-footer-brand-name" style="letter-spacing: 4px; font-family:'Spectral', serif; font-size: 18px; line-height: 30px;">AIMP LABS</div>
                <div class="jv-footer-brand-desc">A Private AI Research & Training Center</div>
                <div class="jv-footer-brand-desc">Computer Vision | Machine Learning | Cloud & Edge Computing </div>
                <div class="jv-footer-brand-desc">Copyright 2019 - <script>document.write(new Date().getFullYear());</script></div>
            </div>
        </div>
        <div class="jv-footer-container-right">
            <div class="jv-footer-brand-statements">
                <div class="jv-footer-brand-name">Contact us at contact@aimplabs.org</div>
                <div class="jv-footer-brand-desc"><a href="rudev.html">Are you a student developer/researcher?</a></div>
                <div class="jv-footer-brand-desc"><a href="about.html">About us</a></div>
            </div>
        </div>
    </div>
</footer>
`;

/**
 * Load navbar and footer into placeholder divs
 */
function loadNavbar() {
    const container = document.getElementById('navbar-container');
    if (container) {
        container.innerHTML = navbarHTML;
        // Re-bind onclick handler after inserting
        const menuIcon = container.querySelector('.menu-icon');
        if (menuIcon) {
            menuIcon.onclick = setsidenav;
        }
    }
}

function loadFooter() {
    const container = document.getElementById('footer-container');
    if (container) {
        container.innerHTML = footerHTML;
    }
}

/**
 * Auto-load components when DOM is ready
 */
document.addEventListener('DOMContentLoaded', () => {
    loadNavbar();
    loadFooter();
});
