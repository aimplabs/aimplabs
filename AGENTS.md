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
│   ├── aimp.css                  # THE stylesheet - every page loads this one file
│   └── default.min.css           # Vendor highlight.js theme (do not hand-edit)
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

Colours are **design tokens** declared once in the `:root` block at the top of
`css/aimp.css`. Reference the token, never the literal:

```css
color: var(--jv-red);        /* NOT  color: #CF494B; */
```

| Token | Value | Use |
|---|---|---|
| `--jv-red` | `#CF494B` | buttons, accents, active states |
| `--jv-ink` | `#4E4E4E` | headings, nav |
| `--jv-body` | `#515151` | body copy |
| `--jv-muted` | `#5B5B66` | secondary text |
| `--jv-heading` | `#444444` | section titles, captions |
| `--jv-surface` | `#f5f5f5` | backgrounds |

There are also tokens for fonts (`--jv-font-head`, `--jv-font-body`),
elevation (`--jv-shadow-sm/md/lg`) and geometry (`--jv-radius`,
`--jv-max-width`). Add a new token rather than a new literal.

### Typography

- **Headers**: Spectral (serif), uppercase transforms, generous letter-spacing
- **Body Text**: Rubik (sans-serif), 14-18px
- **Secondary Text**: Smaller font-sizes with `var(--jv-muted)` color

### Layout Patterns

- **Container Max-Width**: `var(--jv-max-width)` (1200px) with `margin: 0 auto`
- **Flexbox**: Used extensively (`.jv-container-flex`, `.jv-navbar-flex`)
- **Responsive Breakpoints**: exactly **two** — `900px` (tablet & below) and
  `600px` (phone). Do not introduce a third.
- **Navigation**: link row above 900px; hamburger drawer at 900px and below.
  The handoff is exact — the icon and the link row are never both live.

### CSS File Organization

`css/aimp.css` is the only hand-written stylesheet, organised in 12 numbered
sections (tokens → reset → navbar → breadcrumbs → footer → layout → typography
→ brand marks → components → page sections → chatbot → media queries). Its
header comment lists them.

**Rules:**
- Add new rules to the section they belong to, not the end of the file.
- **All** `@media` blocks live in section 12. Never scatter them.
- Never re-declare a selector that already exists — find it and edit it.
- Page-specific CSS goes in a labelled subsection here, not in an inline
  `<style>` block in the HTML.

## Common Development Tasks

### Adding a New HTML Page

1. Create `your-page-name.html` in root directory
2. Import the standard stylesheets:
   ```html
   <link rel="stylesheet" href="css/aimp.css">
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
4. Use relative paths: `../../css/aimp.css` (adjust for nesting depth)
5. Import Highlight.js for code blocks, MathJax for equations

**Example Structure**: See [blogs/chatbot-budget2024/index.html](blogs/chatbot-budget2024/index.html)

### Modifying Navigation/Footer

- Edit section 3 (Navbar) or 5 (Footer) of [css/aimp.css](css/aimp.css) — affects all pages
- Also update the `.jv-navbar-flex` HTML structure in root pages if needed
- Test on mobile (sidebar menu toggle)

### Adding CSS Styling

1. Use `.jv-*` prefix for all new classes
2. Add to appropriate file:
   - Put it in the matching numbered section of `css/aimp.css`
   - Media queries go in section 12, under the 900px or 600px block
   - Never create a second stylesheet, and never add an inline `<style>` block
3. Use the `var(--jv-*)` tokens for colour, font and shadow — never a raw literal
4. Test responsive design at both breakpoints (900px and 600px)

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
- Test changes at both breakpoints (max-width 900px and 600px)
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
- [ ] Colours use brand tokens (`var(--jv-red)`, `var(--jv-ink)`, …)
- [ ] Relative paths work correctly (especially in nested blog directories)
- [ ] Responsive design tested at 900px and 600px breakpoints
- [ ] New colours/fonts use `var(--jv-*)` tokens, not literals
- [ ] No selector declared twice; no new stylesheet or inline `<style>` block
- [ ] If modifying navigation, check all root pages and blogs
- [ ] No build tools required or introduced
- [ ] Changes are production-ready before push to main
