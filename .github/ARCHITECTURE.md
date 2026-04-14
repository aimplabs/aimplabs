# AIMP Labs Website Architecture Guide

This guide explains the structure, component system, and key patterns used in the AIMP Labs website and chatbot application.

## Project Structure Overview

AIMP Labs is a dual-purpose repository containing:

1. **Static Organization Website** — HTML/CSS/JS site showcasing research, innovations, and training
   - Self-contained; requires no build process
   - Served directly from any web server (GitHub Pages via CNAME)
   - Organized as: root HTML pages + reusable components + modular CSS

2. **Streamlit Legal Chatbot** — Python application for Indian legal queries
   - Separate entry point: `app.py`
   - Depends on external API: `https://abhishekaimp.pythonanywhere.com/api/chat`
   - Manages conversation state via Streamlit session variables

---

## Directory Organization

```
/                          # Root HTML pages (15+ main pages)
├── index.html             # Landing page
├── about.html             # About AIMP Labs
├── innovations.html       # Innovation showcase
├── training.html          # Training programs
├── archives.html          # Archive of past content
├── blogs.html             # Blog index
└── [other pages].html

/assets
├── brand_imgs/            # Logo and branding assets
├── tech_imgs/             # Product/innovation images
├── blogs/                 # Blog post assets (shared)
└── results/               # Result showcase images

/blogs                      # Blog post structure
├── chatbot-budget2024/
│   ├── index.html         # Blog post (standalone)
│   └── assets/            # Post-specific images and resources
├── chatbot-budget2024-colab/
│   ├── index.html
│   └── assets/

/css                       # Modular CSS files (single source of truth pattern)
├── aimp_navfoot.css       # Navigation bar and footer styles
├── aimp_mainpgs.css       # Main content pages (innovations, training, etc.)
├── aimp_blogs.css         # Blog-specific styles
├── aimp_gallery.css       # Gallery/image showcase styles
├── aimp_course_progs.css  # Course program layout styles
└── default.min.css        # Third-party code highlighting

/js                        # JavaScript utilities
├── components.js          # Reusable navbar/footer templates
├── navbar.js              # Mobile menu functionality
└── highlight.min.js       # Syntax highlighting for code blocks
```

---

## Component Extraction System

### The Problem
HTML pages traditionally require duplication of navbar, footer, and meta tags across 15+ files. This creates maintenance burden: updating one element requires changes in multiple places.

### The Solution: JavaScript Component Injection
We extract reusable components into `js/components.js` and load them dynamically at page load time.

### How It Works

**1. Component Definitions in `js/components.js`**

The navbar and footer are defined as JavaScript template strings:

```javascript
// Navbar template (static)
const navbarHTML = `
<header class="jv-navbar-container">
    <nav class="jv-navbar-flex">
        <!-- Logo and brand -->
        <!-- Navigation links -->
    </nav>
</header>
`;

// Footer template (dynamic year)
function getFooterHTML() {
    const currentYear = new Date().getFullYear();
    return `
<footer class="jv-footer-container-align">
    <!-- Footer content with dynamic year: ${currentYear} -->
</footer>
`;
}
```

**2. Loader Functions**

```javascript
function loadNavbar() {
    const container = document.getElementById('navbar-container');
    if (container) {
        container.innerHTML = navbarHTML;
        // Re-bind event handlers after insertion
        const menuIcon = container.querySelector('.menu-icon');
        if (menuIcon) {
            menuIcon.onclick = setsidenav;
        }
    }
}

function loadFooter() {
    const container = document.getElementById('footer-container');
    if (container) {
        container.innerHTML = getFooterHTML();
    }
}

// Auto-load on page ready
document.addEventListener('DOMContentLoaded', () => {
    loadNavbar();
    loadFooter();
});
```

**3. HTML Page Template**

Every HTML page includes:

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Meta tags, title, stylesheets -->
    <link rel="stylesheet" href="css/aimp_navfoot.css">
    <link rel="stylesheet" href="css/aimp_mainpgs.css">
    <!-- Other CSS files as needed -->
</head>
<body>
    <!-- Navbar injected here by components.js -->
    <div id="navbar-container"></div>

    <!-- Page-specific content -->
    <main>
        <!-- Your content here -->
    </main>

    <!-- Footer injected here by components.js -->
    <div id="footer-container"></div>

    <!-- Component loader script (runs at DOMContentLoaded) -->
    <script src="js/components.js"></script>
    <script src="js/navbar.js"></script>
</body>
</html>
```

### Benefits
- **Single Source of Truth**: Update navbar once in `js/components.js`, all 15+ pages update automatically
- **Consistency**: Footer year updates automatically every January 1st (no manual updates)
- **No Build Process**: Works with plain HTML; no transpilation required
- **Easy Onboarding**: New contributors understand pattern immediately

---

## CSS Organization: Single Source of Truth Pattern

### The Problem
Multiple CSS files had identical class definitions, creating maintenance burden and inconsistency.

### The Solution: Modular CSS by Feature
We organize CSS into a shared base (`aimp_common.css`) and feature-specific files.

### CSS File Organization

| File | Purpose | Classes |
|------|---------|---------|
| `aimp_navfoot.css` | Navigation bar and footer styling | `.jv-navbar-*`, `.jv-footer-*`, `.jv-breadcrumb-*` |
| `aimp_mainpgs.css` | Main content pages (innovations, training, etc.) | `.jv-hero-*`, `.jv-carousel-*`, `.jv-section-*` |
| `aimp_blogs.css` | Blog post styling | `.jv-blog-*`, blog-specific responsive overrides |
| `aimp_gallery.css` | Gallery/showcase layouts | `.jv-gallery-*` |
| `aimp_course_progs.css` | Course program layouts | `.jv-course-*` |

### CSS Class Naming Convention

All custom classes use the `jv-` prefix:

```css
/* Naming pattern: .jv-{feature}-{element}-{modifier} */

.jv-navbar-flex { }           /* Feature: navbar, element: flex layout */
.jv-section-title { }         /* Feature: section, element: title */
.jv-section-title.large { }   /* Modifier: size variant */
.jv-footer-brand-desc { }     /* Feature: footer, element: brand description */
```

### Responsive Design Strategy

All CSS follows a **mobile-first approach**:

1. **Base Styles** — Mobile layout (no media query needed)
2. **Tablet Breakpoint** (~800px) — Adjust for medium screens
3. **Desktop Breakpoint** (900px+) — Full layout for large screens

```css
/* Mobile first (no media query) */
.jv-section {
    display: block;
    padding: 10px;
}

/* Tablet and larger */
@media screen and (max-width: 800px) {
    .jv-section {
        padding: 15px;
    }
}

/* Very small screens */
@media screen and (max-width: 500px) {
    .jv-section {
        padding: 5px;
    }
}
```

---

## How to Add a New Page

### Step 1: Create HTML Page
Create a new `.html` file in the root directory:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My New Page - AIMP Labs</title>
    
    <!-- CSS: Always include these for navbar/footer and main styling -->
    <link rel="stylesheet" href="css/aimp_navfoot.css">
    <link rel="stylesheet" href="css/aimp_mainpgs.css">
    
    <!-- Add feature-specific CSS if needed -->
    <!-- <link rel="stylesheet" href="css/aimp_gallery.css"> -->
    
    <!-- Material Icons for UI elements -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <!-- Navbar auto-injected here by components.js -->
    <div id="navbar-container"></div>

    <!-- Main content -->
    <main>
        <div class="jv-general-container">
            <h1 class="jv-section-title sz-h1">Welcome to My New Page</h1>
            <p class="jv-section-body">Your content here...</p>
        </div>
    </main>

    <!-- Footer auto-injected here by components.js -->
    <div id="footer-container"></div>

    <!-- Load components (navbar/footer) -->
    <script src="js/components.js"></script>
    <script src="js/navbar.js"></script>
</body>
</html>
```

### Step 2: Style Your Content
Use existing CSS classes from `aimp_mainpgs.css`:

```html
<div class="jv-general-container">
    <h1 class="jv-section-title sz-h1">Page Title</h1>
    <p class="jv-section-body">Regular paragraph text.</p>
    <p class="jv-section-body-highlight">Highlighted text for emphasis.</p>
</div>
```

### Step 3: Add Navigation Link
Update the navbar by editing `js/components.js` if adding a new main section:

```javascript
const navbarHTML = `
<header class="jv-navbar-container">
    <!-- ... -->
    <ul class="jv-navlinks">
        <li><a href="innovations.html">Innovations</a></li>
        <li><a href="your-new-page.html">Your New Page</a></li>  <!-- Add here -->
    </ul>
</header>
`;
```

### Full Example: Creating `/research.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Research - AIMP Labs</title>
    <link rel="stylesheet" href="css/aimp_navfoot.css">
    <link rel="stylesheet" href="css/aimp_mainpgs.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div id="navbar-container"></div>

    <main>
        <div class="jv-general-container">
            <h1 class="jv-section-title sz-h1">Our Research Areas</h1>
            <p class="jv-section-body">
                We focus on visual AI and machine perception...
            </p>
        </div>
    </main>

    <div id="footer-container"></div>
    <script src="js/components.js"></script>
    <script src="js/navbar.js"></script>
</body>
</html>
```

---

## Adding Features to Blog Posts

Blog posts follow the same component pattern. Each blog lives in its own directory with assets:

```
/blogs/my-new-post/
├── index.html          # Post content
└── assets/             # Post-specific images
    └── example.png
```

**Blog HTML Template:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Blog Post - AIMP Labs</title>
    
    <link rel="stylesheet" href="../../css/aimp_navfoot.css">
    <link rel="stylesheet" href="../../css/aimp_blogs.css">
    <!-- Note: Use ../../ to go up two directories to root -->
</head>
<body>
    <div id="navbar-container"></div>

    <main>
        <div class="jv-general-container">
            <h1 class="jv-section-title sz-h1">Blog Post Title</h1>
            <img src="assets/featured.png" alt="Featured image">
            <p class="jv-section-body">Blog content...</p>
        </div>
    </main>

    <div id="footer-container"></div>
    <script src="../../js/components.js"></script>
    <script src="../../js/navbar.js"></script>
</body>
</html>
```

**Important**: Use relative paths (`../../`) when referencing assets and scripts from nested blog directories.

---

## Streamlit App Integration

The Streamlit chatbot (`app.py`) is separate from the static website:

- **Entry point**: `app.py`
- **Dependencies**: Listed in `requirements.txt`
- **API**: Connects to external chatbot API for legal queries
- **Deployment**: Can run locally (`streamlit run app.py`) or deploy to Streamlit Cloud

The static website and Streamlit app are **independent** but share the same repository for convenience.

---

## Troubleshooting

### Navbar/Footer Not Appearing
**Symptom**: Page loads but navbar and footer are missing.

**Cause**: Missing placeholder divs or script loading.

**Fix**:
1. Verify `<div id="navbar-container"></div>` is in `<body>`
2. Verify `<div id="footer-container"></div>` is in `<body>`
3. Verify `<script src="js/components.js"></script>` is included at end of `<body>`
4. Check browser console (F12) for JavaScript errors

**Example (Correct):**
```html
<body>
    <div id="navbar-container"></div>
    <!-- Page content -->
    <div id="footer-container"></div>
    <script src="js/components.js"></script>
</body>
```

### Styling Issues / Classes Not Applied
**Symptom**: Text isn't styled as expected when using `.jv-section-title`, etc.

**Cause**: Missing CSS file or incorrect file order.

**Fix**:
1. Verify all required CSS files are linked in `<head>`
2. Check file order: `aimp_navfoot.css` before feature-specific CSS
3. Verify CSS file paths are relative to HTML location

**Example (Order Matters):**
```html
<link rel="stylesheet" href="css/aimp_navfoot.css">      <!-- Foundation -->
<link rel="stylesheet" href="css/aimp_mainpgs.css">     <!-- Feature-specific -->
<!-- More specific CSS after general CSS -->
```

### Relative Path Issues in Blog Posts
**Symptom**: Images don't load in blog post, or styles don't apply.

**Cause**: Incorrect relative paths from nested `blogs/post-name/index.html`.

**Fix**: Use `../../` to go up two directory levels.

**Correct Paths from `blogs/my-post/index.html`:**
```html
<!-- CSS files in root/css/ -->
<link rel="stylesheet" href="../../css/aimp_navfoot.css">

<!-- JS files in root/js/ -->
<script src="../../js/components.js"></script>

<!-- Assets in same blog directory -->
<img src="assets/image.png">

<!-- Assets in root assets -->
<img src="../../assets/brand_imgs/logo.png">
```

### Mobile Menu Not Opening
**Symptom**: Menu icon appears on mobile but doesn't toggle the menu.

**Cause**: `js/navbar.js` not loaded, or `setsidenav()` function is missing.

**Fix**:
1. Verify `<script src="js/navbar.js"></script>` is included
2. Verify `js/navbar.js` contains the `setsidenav()` function
3. Verify browser console shows no JavaScript errors

---

## Deployment

### Static Website
1. Copy all files (except `app.py` and `requirements.txt`) to web server
2. Configure server to serve `index.html` as default for directory requests
3. No build step required
4. For GitHub Pages: push to repository and configure CNAME for custom domain

### Streamlit App
```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py

# Access at http://localhost:8501
```

---

## Key Takeaways

1. **Component System**: Navbar and footer are extracted to `js/components.js` and injected on page load — update once, deploy everywhere
2. **CSS Organization**: Modular files with single source of truth; extend shared CSS, don't duplicate
3. **CSS Naming**: All custom classes use `jv-` prefix following `jv-{feature}-{element}` pattern
4. **Mobile First**: CSS written for mobile first, with media queries for larger screens
5. **No Build Process**: Pure HTML/CSS/JS; works with any web server
6. **Easy Expansion**: New pages reuse components and CSS; scaling is simple

---

## Related Documentation

For CSS responsive design patterns and breakpoints, see [CSS.md](CSS.md).

For coding conventions, see [copilot-instructions.md](copilot-instructions.md).
