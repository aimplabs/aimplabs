# AIMP Labs Workspace Guidelines

This workspace contains the AIMP Labs organization website and a specialized legal AI chatbot application.

## Project Overview

**AIMP Labs** is a visual AI and machine perception research center. This repository serves two purposes:
- **Organization Website**: Static HTML/CSS/JS site showcasing research, innovations, training programs, and blog content
- **Legal AI Chatbot**: Python/Streamlit-based chatbot specializing in Indian legal law assistance (BNS, BNSS, BSA)

## Code Style

### HTML & CSS
- Use semantic HTML5 tags for structure and accessibility
- CSS class naming follows `jv-` prefix convention (e.g., `jv-navbar-flex`, `jv-hero-container`)
- Organize styles in modular feature-based files: `aimp_navfoot.css`, `aimp_mainpgs.css`, `aimp_blogs.css`, etc.
- Reference [css/aimp_mainpgs.css](css/aimp_mainpgs.css) for responsive design patterns

### Python (Streamlit App)
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Structure session state management clearly in `init_state()` functions
- See [app.py](app.py) for session state and API integration patterns

## Architecture

The project has clear separation of concerns:

1. **Static Website** (`*.html`, `css/`, `js/`, `assets/`)
   - Standalone HTML pages with CSS modules
   - Media assets organized by type (brand_imgs, tech_imgs, blog assets)
   - No build step required—serve directly from web server

2. **Streamlit Chatbot** (`app.py`)
   - Connects to external API (`https://abhishekaimp.pythonanywhere.com/api/chat`)
   - Manages conversation history via Streamlit session state
   - Provides interactive UI for legal query assistance

3. **Blog Content** (`blogs/`)
   - Nested HTML pages with standalone asset folders per blog post
   - Examples: chatbot-budget2024, git guides, C++ compilation tutorials

## Build and Test

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Streamlit Application
```bash
streamlit run app.py
```
The app will be available at `http://localhost:8501`

### Serve Static Website
- Copy HTML/CSS/JS files to any web server (Apache, Nginx, GitHub Pages)
- No build process required
- Check [requirements.txt](requirements.txt) for Python dependencies

## Conventions

### CSS Class Naming
- **Prefix**: All custom classes use `jv-` (e.g., `jv-section-title`, `jv-flex-center`)
- **Separation**: Feature-specific CSS in separate files rather than one monolithic stylesheet
- **Responsive**: Mobile-first approach with media queries for larger screens

### File Organization
- HTML pages in root directory
- Stylesheets in `css/` directory (one per feature area)
- JavaScript utilities in `js/` directory
- Navigation and footer styles in separate `aimp_navfoot.css`
- Blog posts as subdirectories with nested `index.html` and `assets/`

### API Integration
- 90-second timeout for external API calls
- Fallback messages for graceful error handling
- Session state for conversation persistence

### Python Naming
- Constants in UPPERCASE (e.g., `PAGE_TITLE`, `API_URL`, `WELCOME_MESSAGE`)
- Functions in snake_case (e.g., `init_state()`)
- Private/internal functions prefixed with underscore

## Key Files Reference

- **[index.html](index.html)** — Landing page structure and navigation layout
- **[app.py](app.py)** — Streamlit chatbot implementation and session management
- **[css/aimp_navfoot.css](css/aimp_navfoot.css)** — Navigation and footer styling patterns
- **[css/aimp_mainpgs.css](css/aimp_mainpgs.css)** — Main content pages and responsive layout
