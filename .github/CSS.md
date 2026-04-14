# CSS Responsive Design Guide

This guide documents the CSS organization, responsive design patterns, and maintenance practices for AIMP Labs.

---

## Responsive Design Strategy

AIMP Labs uses a **mobile-first** approach with breakpoint-based media queries.

### Why Mobile-First?
- Base CSS applies to all devices (mobile included)
- Larger screens add complexity on top via `@media` queries
- Results in smaller base CSS, progressive enhancement
- Better defaults for older/low-powered devices

### CSS Writing Pattern

```css
/* Mobile (default, no media query needed) */
.jv-section-title {
    font-size: 18px;
    padding: 10px;
}

/* Tablet and up (800px+) */
@media screen and (max-width: 800px) {
    .jv-section-title {
        font-size: 20px;
        padding: 15px;
    }
}

/* Large screens might have additional rules
   but we stop adding at tablet, keep simple */
```

**Note**: The media query uses `max-width`, which reads as "on screens 800px and smaller". This is a mobile-first approach where the base rule is the smallest and we enlarge/adjust for bigger screens.

---

## Primary Breakpoints

AIMP Labs uses these key breakpoints (`max-width` values):

| Breakpoint | Device Type | Notes |
|------------|------------|-------|
| *No query* | Mobile (0-480px) | Default CSS for all devices |
| 500px | Small mobile | Specific adjustments for very small screens |
| 550px | Mobile-to-tablet transition | Footer and gallery adjustments |
| 600px | Small tablet | Specific carousel adjustments |
| 700px | Tablet | Course program layout adjustments |
| 800px | Tablet-to-desktop transition | Major layout shifts (navbar stacking) |
| 900px | Desktop | Gallery and section layout adjustments |

### Which Breakpoint to Use?

- **500px-550px**: Very narrow screens (small phones in portrait, old phones)
- **600px-700px**: Tablet portrait or small phone landscape
- **800px**: Major layout change (navbar becomes vertical, content stacks)
- **900px**: Wider adjustments, multi-column layouts

---

## Common Responsive Patterns

### Pattern 1: Flexbox Direction Change

**Base (Mobile)**: Stack vertically
```css
.jv-container-flex {
    display: flex;
    flex-direction: column;  /* Stack on top of each other */
    align-items: flex-start;
}
```

**Tablet/Desktop**: Side-by-side
```css
@media screen and (max-width: 800px) {
    .jv-container-flex {
        flex-direction: row;  /* Side by side */
    }
}
```

**Real Example from `aimp_mainpgs.css`:**
```css
.jv-carousel-container {
    display: flex;
    flex-direction: column;  /* Mobile: stacked */
    align-items: flex-start;
    flex-basis: 70%;
    padding-right: 20px;
}

@media screen and (max-width: 800px) {
    .jv-carousel-container {
        flex-direction: row;  /* Tablet: side-by-side */
    }
}
```

### Pattern 2: Responsive Sizing and Padding

```css
/* Mobile: Smaller, tighter padding */
.jv-section-container {
    margin-top: 20px;
    padding: 10px;
}

/* Tablet: More breathing room */
@media screen and (max-width: 800px) {
    .jv-section-container {
        padding: 15px;
    }
}

/* Very small: Even tighter */
@media screen and (max-width: 500px) {
    .jv-section-container {
        padding: 5px;
    }
}
```

### Pattern 3: Font Size Scaling

```css
/* Mobile: Smaller font */
.jv-section-title {
    font-size: 18px;
    line-height: 24px;
}

/* Tablet and larger: Bigger, more readable */
@media screen and (max-width: 800px) {
    .jv-section-title {
        font-size: 24px;
        line-height: 32px;
    }
}
```

### Pattern 4: Column Hiding and Showing

```css
/* Mobile: Hide sidebar, show main content full width */
.jv-sidebar {
    display: none;
}

.jv-main-content {
    width: 100%;
}

/* Tablet: Show sidebar */
@media screen and (max-width: 800px) {
    .jv-sidebar {
        display: block;
        width: 30%;
    }

    .jv-main-content {
        width: 70%;
    }
}
```

### Pattern 5: Menu Toggle (Navigation)

```css
/* Mobile: Hide navigation links, show menu icon */
.jv-navlinks {
    display: none;  /* Hidden by default on mobile */
}

.menu-icon {
    opacity: 1;    /* Menu icon visible on mobile */
    cursor: pointer;
}

/* Tablet and larger: Show navigation, hide icon */
@media screen and (max-width: 800px) {
    .jv-navlinks {
        display: flex;
    }

    .menu-icon {
        opacity: 0;    /* Hide icon when menu is visible */
    }
}
```

---

## CSS File Organization Guide

### When to Add CSS to Which File?

| File | Add CSS for... | Examples |
|------|---|---|
| `aimp_navfoot.css` | Navigation bar and footer styling | `.jv-navbar-*`, `.jv-footer-*`, breadcrumbs |
| `aimp_mainpgs.css` | Main content pages (home, innovations, training) | `.jv-hero-*`, `.jv-section-title`, `.jv-carousel-*` |
| `aimp_blogs.css` | Blog post-specific styling | Blog typography, code blocks, blog-specific responsive overrides |
| `aimp_gallery.css` | Image galleries and showcases | `.jv-gallery-*`, image grid layouts |
| `aimp_course_progs.css` | Course program layouts | Course cards, schedules, program-specific styles |

### Avoid Duplication

**Don't** create the same style in multiple files:

```css
/* WRONG: Defining in multiple files */
/* aimp_mainpgs.css */
.jv-section-title { font-size: 20px; }

/* aimp_blogs.css */
.jv-section-title { font-size: 20px; }  /* Duplicate! */
```

**Instead** extend from one file or move shared styles to a common location.

---

## Class Naming Conventions

All custom CSS classes follow a naming pattern:

```
.jv-{feature}-{element}-{modifier}
```

### Examples:

| Class Name | Feature | Element | Modifier | Purpose |
|-----------|---------|---------|----------|---------|
| `.jv-navbar-flex` | navbar | flex | — | Main navbar layout container |
| `.jv-section-title` | section | title | — | Section heading |
| `.jv-section-title.large` | section | title | large | Larger section heading variant |
| `.jv-footer-brand-desc` | footer | brand description | — | Brand text in footer |
| `.jv-carousel-container` | carousel | container | — | Image carousel wrapper |
| `.jv-menu-icon` | menu | icon | — | The menu toggle icon (mobile) |

---

## Responsive Testing Checklist

When adding or modifying CSS, test at these resolutions:

### Desktop (1024px+)
- [ ] Full-width layouts look correct
- [ ] Multi-column layouts are side-by-side
- [ ] Navigation is fully visible
- [ ] No text is cut off

### Tablet (768px - 900px)
- [ ] Columns adjust but remain readable
- [ ] Images scale properly
- [ ] Navigation may start to compress
- [ ] Footer layout adjusts

### Mobile (480px - 550px)
- [ ] Single-column layout
- [ ] Navigation collapses to menu icon
- [ ] Font sizes are readable on small screen
- [ ] Padding/margins scaled down
- [ ] Images fit within screen width

### Quick Testing
Use browser DevTools:
1. Open **F12** (DevTools)
2. Click **device toggle** (phone icon) in toolbar
3. Test at these widths: **480px**, **600px**, **800px**, **1024px**
4. Check all pages and components

---

## Breakpoint Consistency Across Files

### Known Breakpoints by File

**aimp_navfoot.css:**
- 500px (menu cleanup)
- 800px (navbar flex direction)

**aimp_mainpgs.css:**
- 500px (content reflow, hero layout)
- 600px (carousel adjustments)
- 800px (major layout change)
- 900px (gallery adjustments)

**aimp_blogs.css:**
- 550px (mobile text sizing)
- 900px (blog layout adjustments)

### Strategy for Consistency
- Primary breakpoint: **800px** (used in all files for major layout change)
- Secondary breakpoint: **500px** (fine-tuning for very small screens)
- Avoid: Creating breakpoints in only one file (maintain parity)

---

## Code Examples: Real Patterns from Codebase

### Example 1: Navigation Bar (from `aimp_navfoot.css`)

```css
/* Mobile: Vertical stack */
.jv-navbar-flex {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.jv-navlinks {
    display: flex;
}

.menu-icon {
    opacity: 0;      /* Hidden on desktop */
}

/* Tablet/Mobile: Stack navbar items, show menu icon */
@media screen and (max-width: 800px) {
    .jv-navbar-flex {
        flex-direction: column;
        align-items: center;
    }

    .jv-navlinks {
        display: none;   /* Hide links, show menu icon */
    }

    .menu-icon {
        opacity: 1;      /* Show menu icon */
    }
}
```

### Example 2: Hero Section (from `aimp_mainpgs.css`)

```css
/* Mobile: Content stacked */
.jv-container-flex {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    max-width: 1200px;
    margin: 0 auto;
}

.jv-carousel-container {
    flex-basis: 70%;
}

.jv-news-container {
    flex-basis: 30%;
}

/* Tablet: Adjust to side-by-side if needed */
@media screen and (max-width: 800px) {
    .jv-container-flex {
        flex-direction: row;
    }
}

/* Very small screens: Reduce width and padding */
@media screen and (max-width: 500px) {
    .jv-carousel-container {
        max-width: 100%;
        padding-right: 0;
    }
}
```

### Example 3: Gallery (from `aimp_gallery.css`)

```css
/* Mobile: Single column */
.jv-gallery-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 20px;
}

/* Tablet: 2 columns */
@media screen and (max-width: 800px) {
    .jv-gallery-grid {
        grid-template-columns: 1fr 1fr;
    }
}

/* Desktop: 3 columns */
@media screen and (min-width: 1024px) {
    .jv-gallery-grid {
        grid-template-columns: 1fr 1fr 1fr;
    }
}
```

---

## Text and Typography Scaling

AIMP Labs uses semantic HTML and CSS to scale typography across breakpoints:

```css
/* Heading sizes scale by breakpoint */

.jv-section-title.sz-h1 {
    font-family: 'Spectral', serif;
    font-size: 32px;  /* Mobile */
    line-height: 40px;
    font-weight: 700;
}

@media screen and (max-width: 800px) {
    .jv-section-title.sz-h1 {
        font-size: 28px;  /* Tablet: slightly smaller */
    }
}

@media screen and (max-width: 500px) {
    .jv-section-title.sz-h1 {
        font-size: 22px;  /* Small mobile: even smaller */
    }
}
```

---

## Maintenance Best Practices

### Do's ✅

- **DO** test at multiple breakpoints after CSS changes
- **DO** use the established breakpoints (500px, 800px, 900px)
- **DO** follow the `jv-` naming convention for new classes
- **DO** put responsive CSS in the appropriate feature file
- **DO** comment media queries with the device type they target

```css
/* Tablet and smaller screens */
@media screen and (max-width: 800px) {
    /* CSS here */
}
```

### Don'ts ❌

- **DON'T** add breakpoints randomly (use standard ones)
- **DON'T** duplicate CSS across multiple files
- **DON'T** ignore mobile when writing desktop CSS
- **DON'T** forget to test on actual mobile devices

---

## Adding New Responsive CSS

### Template for Adding a New Component

```css
/* Component Name - Mobile First */

.jv-new-component {
    display: flex;
    flex-direction: column;  /* Mobile: stack */
    padding: 10px;           /* Mobile: tight padding */
    font-size: 16px;         /* Mobile: readable */
}

/* Tablet and larger */
@media screen and (max-width: 800px) {
    .jv-new-component {
        flex-direction: row;   /* Tablet: side-by-side */
        padding: 15px;         /* More breathing room */
        font-size: 18px;       /* Bigger for easier reading */
    }
}

/* Very small screens */
@media screen and (max-width: 500px) {
    .jv-new-component {
        flex-direction: column; /* Back to stack on tiny screens */
        padding: 5px;           /* Minimal space */
    }
}
```

### Checklist for New CSS:

1. [ ] Follows `jv-` naming convention
2. [ ] Mobile-first base styles (no media query)
3. [ ] Includes 800px breakpoint (if has responsive behavior)
4. [ ] Tested at 480px, 800px, and 1024px widths
5. [ ] No duplication with existing classes
6. [ ] Added to correct CSS file (see file guide above)
7. [ ] Comments explain breakpoint purpose

---

## Common Issues and Solutions

### Issue: Text Too Small on Mobile
```css
/* Problem */
.jv-body-text {
    font-size: 14px;  /* Too small on mobile */
}

/* Solution */
.jv-body-text {
    font-size: 16px;  /* Readable on mobile */
}

@media screen and (max-width: 800px) {
    .jv-body-text {
        font-size: 14px;  /* Smaller on tablet */
    }
}
```

### Issue: Images Overflow on Mobile
```css
/* Problem */
img {
    width: 100%;
    max-width: 1200px;  /* Too wide on mobile */
}

/* Solution */
img {
    width: 100%;        /* Use full width */
    max-width: 100%;    /* Never exceed container */
    height: auto;       /* Maintain aspect ratio */
}
```

### Issue: Columns Don't Stack on Mobile
```css
/* Problem */
.jv-two-column {
    display: flex;
    flex-direction: row;  /* Always side-by-side */
}

/* Solution */
.jv-two-column {
    display: flex;
    flex-direction: column;  /* Mobile: stack */
}

@media screen and (max-width: 800px) {
    .jv-two-column {
        flex-direction: row;  /* Tablet: side-by-side */
    }
}
```

---

## Key Takeaways

1. **Mobile First**: Write base CSS for mobile, add complexity with media queries
2. **Consistent Breakpoints**: Use 500px, 800px, 900px (don't create random breakpoints)
3. **No Duplication**: Extend existing classes, don't define same style in multiple files
4. **Naming**: All custom classes start with `jv-`
5. **Test Always**: Verify at 480px, 800px, and 1024px before committing
6. **Feature-Specific**: Keep blog CSS in `aimp_blogs.css`, gallery in `aimp_gallery.css`, etc.
7. **Comment Breakpoints**: Document which device type each media query targets

---

## Related Documentation

For architecture and component system details, see [ARCHITECTURE.md](ARCHITECTURE.md).

For coding conventions, see [copilot-instructions.md](copilot-instructions.md).
