# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

mikeder.github.io is a personal portfolio and blog site built with **Hugo**, a static site generator written in Go. The site is hosted on GitHub Pages and includes content about software projects, synthesizers, electronic music, and various technical topics.

## Quick Start

**Prerequisites:** Hugo must be installed on your system

**Development server:**
```bash
make dev
```
Starts the Hugo development server with draft posts enabled (`hugo server -D --disableFastRender`). The site will be available at `http://localhost:1313`.

**Publish to GitHub Pages:**
```bash
make publish
```
This runs `scripts/publish_to_ghpages.sh`, which:
1. Verifies the working directory is clean
2. Removes and recreates the `public/` directory
3. Builds the entire site with `hugo`
4. Commits the generated site to the `gh-pages` branch
5. Pushes both main and gh-pages branches to GitHub
6. Cleans up the public directory

## Architecture & Structure

### Hugo Configuration
- **config.yaml** - Main Hugo configuration including:
  - Base URL: `https://mikeder.net/`
  - Taxonomies: categories and tags
  - Site author and social media links (Bandcamp, GitHub, Mastodon, SoundCloud, YouTube, Docker Hub)
  - Site description and language settings

### Content Organization
Located in `/content/`:
- **blog/** - Blog posts and longer-form content (jamuary logs, synthesizer repairs, technical deep-dives, devlogs)
- **projects/** - Project portfolio pages (Larpa, music, homelab, Rust server, various Rust projects)
- **synthesizers/** - Synthesizer documentation (organized by brand: DIY, Roland)
- **about/** - Static pages (resume, reviews, about)
- **_index.md** - Homepage content

Content uses front matter with title, date, draft status, and optional tags/categories. Archives are handled via the `archive/` subdirectory within blog.

### Theme & Layouts
Custom theme located in `/layouts/`:
- **_default/baseof.html** - Base template that all pages inherit from
- **_default/list.html** - List pages (categories, tags, archives)
- **_default/single.html** - Individual post/page template
- **_default/summary.html** - Post summary template
- **_default/resume.html** - Dedicated resume layout
- **index.html** - Homepage layout
- **partials/** - Reusable components:
  - `header.html` - Navigation bar with site links
  - `footer.html` - Page footer
  - `sidebar.html` - Sidebar content
  - `pagination.html` - Pagination controls
  - `image-modal.html` - Modal for lightbox-style image viewing
  - `render-image.html` - Custom image rendering hook
- **shortcodes/** - Custom Hugo shortcodes for embedded content:
  - `bandcamp-track.html` - Embeds single Bandcamp tracks
  - `bandcamp-album.html` - Embeds Bandcamp albums
  - `youtube-pl.html` - Embeds YouTube playlists
  - `slideshow.html` - Image slideshow functionality

### Static Assets
Located in `/static/`:
- **css/** - Stylesheet files
- **img/** - Images and icons
- **js/** - JavaScript for interactivity

Generated resources are cached in `/resources/_gen/`.

## Key Features & Customizations

**Font Awesome Icons** - The header includes Font Awesome 6 icons for social links and styling

**Git Info Enabled** - Hugo is configured with `enableGitInfo: true`, allowing templates to access git metadata like last modified date

**Media Embedding** - Custom shortcodes allow embedding:
- Bandcamp albums and tracks
- YouTube playlists
- Image slideshows

**Image Modal** - Custom image rendering hook provides lightbox-style viewing for images

**Section Menus** - Uses Hugo's `sectionPagesMenu: main` to automatically generate navigation from content sections

## Deployment Notes

The site uses GitHub Pages with a custom domain (CNAME file points to `mikeder.net`). The `gh-pages` branch contains generated static files. The publish script uses git worktrees to keep the gh-pages branch isolated from the main working directory. Only run `make publish` when the working directory is clean — the script checks this and will abort if there are uncommitted changes.

New content can be scaffolded with `hugo new blog/my-post.md`, which uses the archetype template.
