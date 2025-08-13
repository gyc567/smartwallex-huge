# Technology Stack

## Build System & Framework
- **Hugo**: Static site generator (v0.146.0+, Extended version required)
- **Language**: Chinese (zh-cn) as primary language
- **Configuration**: TOML format (hugo.toml)

## Themes
The project uses a single theme via Git submodule:
- **PaperMod**: Modern blog theme (currently active)
  - Features: Dark/light mode, search, mobile-responsive, SEO optimized
  - Use for: Blog posts, articles, content-focused pages

## Development Environment
- **Hugo Extended**: Required for SCSS processing
- **Git**: Version control with submodule support
- **Node.js**: Optional for theme customization

## Common Commands

### Development
```bash
# Start development server
hugo server -D

# Start with drafts and future posts
hugo server -D -F

# Start on specific port
hugo server -p 8080
```

### Content Creation
```bash
# Create new post
hugo new posts/article-name.md

# Create new page
hugo new about.md

# Create with archetype
hugo new --kind post posts/my-post.md
```

### Build & Deploy
```bash
# Production build
hugo --minify

# Development build with drafts
hugo -D

# Build to custom directory
hugo --destination dist/
```

### Theme Management
```bash
# Initialize submodules
git submodule update --init --recursive

# Update theme
git submodule update --remote

# Theme configuration (edit hugo.toml)
theme = 'PaperMod'
```

## Content Format
- **Markdown**: Primary content format
- **Front Matter**: TOML format with +++
- **Assets**: Images, CSS, JS in respective directories
- **Static Files**: Direct serving from static/ directory

## Deployment Targets
- **GitHub Pages**: Automated via GitHub Actions
- **Netlify**: Direct Git integration
- **Vercel**: Hugo preset available
- **Traditional Servers**: Static file upload

## Performance Considerations
- Use `--minify` flag for production builds
- Optimize images before adding to static/
- Leverage Hugo's built-in asset processing
- Enable caching headers on hosting platform