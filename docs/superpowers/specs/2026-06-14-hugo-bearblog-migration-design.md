# Hugo + bearblog Migration — Design

**Date:** 2026-06-14
**Owner:** mathanamathav
**Goal:** Replace the existing Jekyll site with a minimal Hugo site using the `janraasch/hugo-bearblog` theme, deployed free to GitHub Pages via GitHub Actions. All content authored as markdown.

---

## Decisions (locked)

| Topic | Choice |
|---|---|
| Generator | Hugo (extended) |
| Theme | `janraasch/hugo-bearblog`, default CSS, automatic dark mode |
| Theme delivery | git submodule at `themes/hugo-bearblog` |
| Scaffold approach | B — minimal manual scaffold (hand-written config + only the content we need; no `exampleSite` cruft) |
| Hosting | GitHub Pages via GitHub Actions (official workflow) |
| URL | `https://mathanamathav.github.io/` (root user site, no custom domain, no CNAME) |
| Hugo version | `0.163.1` (latest stable as of 2026-06-14) |
| Menu | Home, Blog, CV |
| Home page | Short intro only (the existing one-line bio) |
| Projects | Dropped — no projects page/section |
| Deploy branch | `master` (work happens on `dev`; ship via PR `dev` → `master`) |
| Custom CSS | None for now (no `custom_head.html`) |

---

## Target repo layout

```
.
├── .github/workflows/hugo.yaml
├── .gitignore                      # rewritten for Hugo
├── README.md                       # rewritten for Hugo
├── hugo.toml                       # site config
├── content/
│   ├── _index.md                   # home — short intro
│   ├── cv.md                       # CV page → /cv/
│   └── blog/
│       └── hello-world.md          # first post → /blog/hello-world/
└── themes/
    └── hugo-bearblog/              # git submodule
```

Removed (Jekyll): `Gemfile`, `Gemfile.lock`, `_config.yml`, `_layouts/`, `_pages/`, `_blogs/`, `_site/`, `assets/`.

---

## Config — `hugo.toml`

Param names are mirrored from `themes/hugo-bearblog/exampleSite/hugo.toml` after the submodule is added (verified, not invented). Intended shape:

```toml
baseURL = "https://mathanamathav.github.io/"
languageCode = "en-us"
title = "Mathan"
theme = "hugo-bearblog"

[params]
  description = "Developer."
  dateFormat = "2006-01-02"
  hideMadeWithLine = true
  # favicon = "..."   # optional, add if a favicon is provided

[[menu.main]]
  name = "Home"
  url = "/"
  weight = 1
[[menu.main]]
  name = "Blog"
  url = "/blog/"
  weight = 2
[[menu.main]]
  name = "CV"
  url = "/cv/"
  weight = 3

[caches]
  [caches.images]
    dir = ":cacheDir/images"   # required by the GitHub Pages workflow
```

> Exact `[params]` key names (e.g. `hideMadeWithLine`, `dateFormat`) are confirmed against the theme's `exampleSite/hugo.toml` during implementation; the values above are the intent.

---

## Content migration

| Source (Jekyll) | Target (Hugo) | URL | Notes |
|---|---|---|---|
| `_pages/about.md` | `content/_index.md` | `/` | Home. Body = existing one-line bio. Drop `layout`, `permalink`, `redirect_from`, `author_profile`. |
| `_pages/cv.md` | `content/cv.md` | `/cv/` | Body unchanged (markdown). Drop `layout`, `permalink`, `redirect_from`. |
| `_pages/blog.md` | *deleted* | — | bearblog auto-generates the `/blog/` list; manual Liquid loop not needed. |
| `_blogs/2025-10-02-hello-world.md` | `content/blog/hello-world.md` | `/blog/hello-world/` | Keep `title`, `date`, `tags`. Drop `layout`, `permalink`. Body unchanged. |

### Front matter conversions

Home (`content/_index.md`):
```markdown
---
title: "Mathan"
---

I'm Mathan, a developer who loves building things that make a tangible difference in everyday life.
```

CV (`content/cv.md`):
```markdown
---
title: "CV"
---

<existing CV markdown body unchanged>
```

Blog post (`content/blog/hello-world.md`):
```markdown
---
title: "Hello World 🤖"
date: 2025-10-02
tags: ["First Post"]
---

<existing post body unchanged>
```

> URL change: the old post lived at `/blog/2025/10/hello-world/`; the new one is `/blog/hello-world/`. Acceptable — site is new, no external inbound links to preserve.

---

## Deploy — `.github/workflows/hugo.yaml`

Official GitHub-recommended GitHub Pages flow (no third-party actions). Key adaptations from the handoff doc:

- Trigger on push to **`master`** (not `main`).
- `HUGO_VERSION: 0.163.1`.
- `submodules: recursive` to pull the theme.
- `baseURL` injected at build time from `steps.pages.outputs.base_url`.

```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches: ["master"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    shell: bash

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.163.1
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb \
            https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \
          && sudo dpkg -i ${{ runner.temp }}/hugo.deb
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive
          fetch-depth: 0
      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5
      - name: Build with Hugo
        env:
          HUGO_ENVIRONMENT: production
        run: hugo --gc --minify --baseURL "${{ steps.pages.outputs.base_url }}/"
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Manual one-time step (owner)
GitHub repo → **Settings → Pages → Source = GitHub Actions**. Required before the first deploy succeeds; cannot be done from code.

---

## `.gitignore` (rewritten)

```
# Hugo
/public/
/resources/_gen/
.hugo_build.lock

# OS
.DS_Store
```

---

## Local preview

Hugo is **not installed locally**. To preview:
```bash
brew install hugo
hugo server -D     # drafts included; http://localhost:1313
```
The scaffold itself is built by hand (approach B), so the Hugo CLI is not required to create files — only to preview/build locally.

---

## Verification

- `git submodule status` shows `themes/hugo-bearblog` populated.
- Local: `hugo server -D` renders home (`/`), `/cv/`, `/blog/`, `/blog/hello-world/` with no template errors; menu shows Home/Blog/CV.
- CI: push to a branch with the workflow (or `workflow_dispatch`) builds green; after merge to `master`, the deployed site loads at `https://mathanamathav.github.io/`.

---

## Out of scope (YAGNI)

Projects page, custom CSS/branding, analytics, comments, custom domain, favicon (unless provided). Each can be added later without reworking this foundation.
