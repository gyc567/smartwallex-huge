# Project Structure

## Directory Organization

```
├── archetypes/          # Content templates
│   └── default.md       # Default post template with TOML front matter
├── assets/              # Processed assets (CSS, JS, images)
├── content/             # Site content (Markdown files)
│   ├── posts/           # Blog posts and articles
│   └── *.md             # Static pages (about.md, etc.)
├── data/                # Data files (YAML, JSON, TOML)
├── i18n/                # Internationalization files
├── layouts/             # Custom layout overrides
├── static/              # Static assets (served directly)
├── themes/              # Theme submodule
│   └── PaperMod/        # Blog theme (Git submodule)
├── public/              # Generated site output (ignored in Git)
├── hugo.toml            # Main configuration file
├── .gitmodules          # Git submodule configuration
└── 部署技术文档.md       # Deployment documentation (Chinese)
```

## Content Organization

### Posts Structure
- **Location**: `content/posts/`
- **Format**: Markdown with TOML front matter
- **Categories**: 公告 (announcements), 教程 (tutorials)
- **Tags**: crypto, smart-money, defi, blockchain, 入门

### Front Matter Convention
```toml
+++
date = '2025-08-12T10:41:58+08:00'
draft = false
title = 'Article Title'
tags = ['crypto', 'smart-money', 'defi', 'blockchain']
categories = ['公告']
+++
```

### Static Pages
- **About**: `content/about.md` - Site information and contact details
- **Custom Pages**: Direct placement in `content/` root

## Theme Structure

### PaperMod Theme (Active)
- **Purpose**: Blog and content presentation
- **Features**: Search, dark/light mode, responsive design
- **Customization**: Override layouts in project `layouts/` directory

## Asset Management

### Images and Logos
- **Theme Logos**: `themes/webstack/static/assets/images/logos/`
- **Custom Assets**: `static/` directory for direct serving
- **Processed Assets**: `assets/` directory for Hugo processing

### CSS and JavaScript
- **Theme Assets**: Managed within theme directories
- **Custom Styles**: Place in `assets/css/` for processing
- **Static Scripts**: Place in `static/js/` for direct serving

## Configuration Files

### Main Configuration
- **File**: `hugo.toml`
- **Format**: TOML
- **Sections**: Basic settings, params, markup configuration

### Theme Configuration
- **PaperMod**: Configured via `[params]` in hugo.toml

## Build Output
- **Directory**: `public/`
- **Status**: Generated, not tracked in Git
- **Structure**: Mirrors content organization with HTML output

## Development Workflow

### Content Creation
1. Use `hugo new posts/filename.md` for new posts
2. Edit content in `content/` directory
3. Test with `hugo server -D`
4. Build with `hugo --minify` for production

### Theme Management
1. Current theme: PaperMod (configured in `hugo.toml`)
2. Restart development server after configuration changes
3. Customize via `layouts/` directory overrides

## File Naming Conventions
- **Posts**: Use descriptive, URL-friendly names
- **Images**: Organize by content type or date
- **Pages**: Use simple, clear names matching URL structure
- **Chinese Content**: UTF-8 encoding, mixed Chinese/English naming acceptable