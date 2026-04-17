# AIMP Labs Codebase Guide for AI Agents

## Project Overview

This is the official website for **AIMP Labs** (Artificial Intelligence & Machine Perception), a research and training organization in Kolkata, India.

- **Website**: www.aimplabs.org
- **Hosting**: GitHub Pages (automatic deployment from `main` branch)
- **Architecture**: Static HTML5/CSS3/JavaScript site (no build tools, no frameworks)
- **Production Status**: Live (v1.0+)

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Pure HTML5, CSS3, Vanilla JavaScript |
| **Fonts** | Google Fonts (Spectral for headers, Rubik for body) |
| **Icons** | Font Awesome, Material Symbols |
| **Libraries** | Marked.js (markdown), DOMPurify (sanitization), Highlight.js (syntax highlighting), MathJax (math rendering) |
| **Styling** | Custom CSS with `.jv-*` utility class convention |
| **Build Process** | **None** - Direct static file serving |

## Project Structure

```
aimplabs/
├── index.html, about.html, innovations.html, ...    # Root-level pages
├── css/
│   ├── aimp_navfoot.css          # Global nav, footer, breadcrumbs (imported everywhere)
│   ├── aimp_mainpgs.css          # Main page layouts
│   ├── aimp_blogs.css            # Blog-specific styling
│   ├── aimp_course_progs.css, aimp_gallery.css, default.min.css
├── js/
│   └── highlight.min.js          # Code syntax highlighting
├── assets/
│   ├── brand_imgs/               # Logos, branding assets
│   ├── tech_imgs/                # Hero images, diagrams
│   └── blogs/cpp_compilation/, git/, etc.
├── blogs/
│   ├── chatbot-budget2024/       # Example blog post structure
│   │   ├── index.html
│   │   └── assets/
│   └── chatbot-budget2024-colab/
├── CNAME                         # GitHub Pages domain config
└── README.md
```

## Development Conventions

### CSS Class Naming

All custom CSS classes use a `.jv-*` prefix:

```css
/* Component naming */
.jv-navbar-flex          /* Navigation container */
.jv-general-container    /* Main content wrapper */
.jv-section-title        /* Section headings */
.jv-bar-upper, .jv-bar-lower /* Decorative bars */

/* State classes */
.jv-active               /* Active/selected state */

/* Size utilities */
.sz-h1, .sz-h2, .sz-h3   /* Heading size variants */
```

**Rule**: Always use `.jv-` prefix for new classes. Never use generic names like `.container` or `.title`.

### Color Scheme (Brand Identity)

```
Primary Red:        #CF494B   (buttons, accents, active states)
Dark Gray:          #4E4E4E   (headings, main text)
Light Gray:         #f5f5f5   (backgrounds)
Neutral Gray:       #5B5B66   (secondary text, descriptions)
Secondary Grays:    #999999, #888
```

These colors appear in:
- `css/aimp_navfoot.css` (navigation highlights)
- `css/aimp_mainpgs.css` (buttons and accents)
- All page-specific stylesheets

### Typography

- **Headers**: Spectral (serif), uppercase transforms, generous letter-spacing
- **Body Text**: Rubik (sans-serif), 14-18px
- **Secondary Text**: Smaller font-sizes with `#5B5B66` color

### Layout Patterns

- **Container Max-Width**: 1200px with `margin: 0 auto`
- **Flexbox**: Used extensively (`.jv-container-flex`, `.jv-navbar-flex`)
- **Responsive Breakpoint**: `@media (max-width: 800px)` for mobile adjustments
- **Navigation**: Sidebar menu that toggles on mobile

### CSS File Organization

- **aimp_navfoot.css**: Imported on EVERY page (global styles)
- **Page-specific**: `aimp_mainpgs.css` (home), `aimp_blogs.css` (blog posts), `aimp_course_progs.css`, `aimp_gallery.css`
- **Pattern**: Modular approach with separate files per content type

## Common Development Tasks

### Adding a New HTML Page

1. Create `your-page-name.html` in root directory
2. Import the standard stylesheets:
   ```html
   <link rel="stylesheet" href="css/aimp_navfoot.css">
   <link rel="stylesheet" href="css/aimp_mainpgs.css">  <!-- or appropriate page-specific CSS -->
   ```
3. Copy the navbar structure from an existing page (e.g., `index.html`)
4. Use `.jv-*` classes for layout and styling
5. Push to `main` branch to deploy automatically

### Creating a New Blog Post

1. Create directory: `blogs/your-topic/`
2. Add `index.html` with blog post structure:
   ```
   Breadcrumbs → Author metadata → Publication date → Content sections
   ```
3. Create `blogs/your-topic/assets/` for images and related files
4. Use relative paths: `../../css/aimp_blogs.css` (adjust for nesting depth)
5. Import Highlight.js for code blocks, MathJax for equations

**Example Structure**: See [blogs/chatbot-budget2024/index.html](blogs/chatbot-budget2024/index.html)

### Modifying Navigation/Footer

- Edit [css/aimp_navfoot.css](css/aimp_navfoot.css) (affects all pages globally)
- Also update the `.jv-navbar-flex` HTML structure in root pages if needed
- Test on mobile (sidebar menu toggle)

### Adding CSS Styling

1. Use `.jv-*` prefix for all new classes
2. Add to appropriate file:
   - Global styles → `css/aimp_navfoot.css` or `css/aimp_mainpgs.css`
   - Blog-specific → `css/aimp_blogs.css`
   - Feature-specific → Create new CSS file and import in relevant pages
3. Match existing color scheme (`#CF494B`, `#4E4E4E`, etc.)
4. Test responsive design at 800px breakpoint

## Important Notes for Agents

### No Build Process
- **Direct serving**: All changes to HTML/CSS/JS are live immediately after push
- **No compilation or bundling** required
- **No npm/package manager** needed
- **CDN libraries only**: External libraries (MathJax, Highlight.js) loaded via CDN

### Copy-Paste Patterns
- Navigation bars are manually copied across pages (no template engine)
- This is **intentional** (keep site minimal and self-contained)
- When updating navigation, update the `.jv-navbar-flex` HTML in each root page

### Responsive Design Requirement
- Test changes on mobile (max-width: 800px breakpoint)
- Sidebar navigation should toggle visibility on mobile
- Use flexbox for flexible layouts

### Git Workflow
- **main** branch = production (live on www.aimplabs.org)
- **dev-aa** branch = development (if present)
- Push to main directly only if change is production-ready
- No CI/CD pipeline beyond GitHub Pages

## Useful References

- **README.md**: Minimal project info
- **CNAME**: Domain configuration for GitHub Pages
- **.gitignore**: Excludes `venv/`, `.DS_Store` (Python development environment)

## Quick Checklist for PRs/Changes

- [ ] CSS uses `.jv-*` prefix for new classes
- [ ] Colors match brand scheme (#CF494B, #4E4E4E, etc.)
- [ ] Relative paths work correctly (especially in nested blog directories)
- [ ] Responsive design tested at 800px breakpoint
- [ ] If modifying navigation, check all root pages and blogs
- [ ] No build tools required or introduced
- [ ] Changes are production-ready before push to main
