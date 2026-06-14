# Hugo + bearblog Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the existing Jekyll site with a minimal Hugo + `hugo-bearblog` site, deployed to GitHub Pages via GitHub Actions.

**Architecture:** Hugo (extended) compiles markdown in `content/` against the `hugo-bearblog` theme (added as a git submodule) into static HTML. GitHub Actions builds on push to `master` and publishes to Pages. No custom CSS; default theme styling with automatic dark mode.

**Tech Stack:** Hugo extended 0.163.1, `janraasch/hugo-bearblog` (git submodule), GitHub Actions, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-06-14-hugo-bearblog-migration-design.md`

---

## File Structure

| File | Responsibility |
|---|---|
| `themes/hugo-bearblog/` | Theme (git submodule) — not edited |
| `hugo.toml` | Site config: baseURL, title, theme, params, menu, image cache |
| `content/_index.md` | Home page — short intro |
| `content/cv.md` | CV page → `/cv/` |
| `content/blog/hello-world.md` | First blog post → `/blog/hello-world/` |
| `.github/workflows/hugo.yaml` | Build + deploy to Pages on push to `master` |
| `.gitignore` | Ignore Hugo build output + OS files |
| `AGENTS.md` | Canonical agent guide (stack, structure, commands, conventions) |
| `CLAUDE.md` | Pointer → AGENTS.md |
| `LICENSE` | MIT (code) |
| `README.md` | Human-facing: what it is, run locally, license split |

**Removed (Jekyll):** `Gemfile`, `Gemfile.lock`, `_config.yml`, `_layouts/`, `_pages/`, `_blogs/`, `_site/`, `assets/`.

All work happens on the `dev` branch. Shipping = PR `dev` → `master`.

---

### Task 1: Install Hugo and add the theme submodule

**Files:**
- Create: `themes/hugo-bearblog/` (submodule)
- Create/modify: `.gitmodules`

- [ ] **Step 1: Install Hugo (extended) locally**

Run:
```bash
brew install hugo
```
Expected: completes; `hugo version` prints a version string containing `extended`. (Plan pins CI to 0.163.1; a newer local Hugo is fine for preview.)

- [ ] **Step 2: Add the theme as a git submodule**

Run:
```bash
git submodule add https://github.com/janraasch/hugo-bearblog.git themes/hugo-bearblog
```
Expected: clones into `themes/hugo-bearblog`; creates `.gitmodules`.

- [ ] **Step 3: Verify submodule is populated**

Run:
```bash
git submodule status && ls themes/hugo-bearblog/exampleSite/hugo.toml
```
Expected: status line shows a commit hash for `themes/hugo-bearblog`; the `exampleSite/hugo.toml` path exists.

- [ ] **Step 4: Confirm exact `[params]` and menu key names**

Run:
```bash
cat themes/hugo-bearblog/exampleSite/hugo.toml
```
Expected: shows real param names (`description`, `dateFormat`, `favicon`, `hideMadeWithLine`, etc.) and `[[menu.main]]` entries. If any name differs from Task 3's `hugo.toml`, adjust Task 3 to match what is printed here. (The theme is the source of truth for param names.)

- [ ] **Step 5: Commit**

```bash
git add .gitmodules themes/hugo-bearblog
git commit -m "build: add hugo-bearblog theme submodule"
```

---

### Task 2: Remove the Jekyll site

**Files:**
- Delete: `Gemfile`, `Gemfile.lock`, `_config.yml`, `_layouts/`, `_pages/`, `_blogs/`, `assets/`, `_site/`

- [ ] **Step 1: Remove tracked Jekyll files**

Run:
```bash
git rm -r Gemfile Gemfile.lock _config.yml _layouts _pages _blogs assets
```
Expected: each path staged for deletion. (Content from `_pages/cv.md` and `_blogs/2025-10-02-hello-world.md` is reproduced in Tasks 4 — no information lost.)

- [ ] **Step 2: Remove the untracked build dir if present**

Run:
```bash
rm -rf _site .sass-cache .jekyll-cache .jekyll-metadata
```
Expected: no error (dirs may or may not exist).

- [ ] **Step 3: Verify Jekyll files are gone**

Run:
```bash
ls Gemfile _config.yml _pages 2>&1 | grep -c "No such file" || true
```
Expected: prints `3` (all three absent).

- [ ] **Step 4: Commit**

```bash
git commit -m "chore: remove Jekyll site (migrating to Hugo)"
```

---

### Task 3: Write the Hugo config

**Files:**
- Create: `hugo.toml`

- [ ] **Step 1: Create `hugo.toml`**

Create `hugo.toml` with:
```toml
baseURL = "https://mathanamathav.github.io/"
languageCode = "en-us"
title = "Mathan"
theme = "hugo-bearblog"

[params]
  description = "Developer."
  dateFormat = "2006-01-02"
  hideMadeWithLine = true

[[menu.main]]
  identifier = "home"
  name = "Home"
  url = "/"
  weight = 1

[[menu.main]]
  identifier = "blog"
  name = "Blog"
  url = "/blog/"
  weight = 2

[[menu.main]]
  identifier = "cv"
  name = "CV"
  url = "/cv/"
  weight = 3

[caches]
  [caches.images]
    dir = ":cacheDir/images"
```

(If Task 1 Step 4 showed different param names, use those names with the values above.)

- [ ] **Step 2: Verify config parses**

Run:
```bash
hugo config | head -20
```
Expected: prints resolved config (includes `baseurl`, `title = mathan`) with no parse error. (Content does not exist yet — that is fine; this only checks the config loads.)

- [ ] **Step 3: Commit**

```bash
git add hugo.toml
git commit -m "feat: add Hugo site config"
```

---

### Task 4: Migrate content (home, CV, blog post)

**Files:**
- Create: `content/_index.md`, `content/cv.md`, `content/blog/hello-world.md`

- [ ] **Step 1: Create the home page `content/_index.md`**

Create `content/_index.md` with:
```markdown
---
title: "Mathan"
---

I'm Mathan, a developer who loves building things that make a tangible difference in everyday life.
```

- [ ] **Step 2: Create `content/cv.md`**

Create `content/cv.md` with (section headers converted from Jekyll's setext `======` H1s to `##` so the page has one top-level title):
```markdown
---
title: "CV"
---

## Education

- PSG College of Technology, Coimbatore, India — Integrated M.Sc. Data Science; CGPA 8.67 (June 2019 – April 2024)
- Adhyapana CBSE School, Madurai, India — Class XII (CBSE); Marks 93% (2018 – 2019)

## Experience

- DataGenie — Jr. Data Scientist & Founding Engineer (Remote) (December 2023 – Present)
    - Agentic AI chat application: Developed a core customer-facing chat application using LangChain and agent frameworks, serving as a primary interface for daily user interactions and driving customer engagement.
    - Large-scale data engineering: Built robust PySpark-based data processing pipelines handling millions of records, optimizing ETL workflows for enterprise-scale data ingestion and transformation.
    - Microservices architecture: Architected and deployed critical internal microservices including Metrics Service, Insights Service, and Airflow Service, enabling scalable application infrastructure and improved system reliability.
- ZeroDown — Software Engineer Intern (Remote) (June 2022 – December 2022)
    - Real estate market intelligence: Engineered a data analytics prototype providing comprehensive visualizations and market insights across major US housing markets, enabling data-driven decision-making.
    - Production ETL optimization: Developed and optimized enterprise-scale ETL pipelines, improving data processing efficiency and ensuring seamless integration across multiple data sources.
    - Intelligent error monitoring: Designed an automated incident routing system that analyzes tracebacks to identify responsible developers, reducing debugging time and improving system reliability.

## Selected Projects

- IntersectX: Built an AI-powered investment research platform that enables faster, data-driven decisions via coordinated multi-agent analysis; Tech: Python, LangChain, FastAPI.
- CodeForHer: Delivered a platform that supports guided learning and safer commutes through a personalized chat and voice assistant; Tech: FastAPI, LangChain, Streamlit.
- DoodleDraw: Built a real-time sketch-recognition game that classifies doodles and provides instant in-browser feedback; Tech: TensorFlow, Django, JavaScript (Canvas).
- Trust‑Me‑Bro: Built a web app that analyzes YouTube comments to estimate video credibility and flag risk; Tech: Django, YouTube Data API, Python, NLP.

## Skills

Python, PySpark, FastAPI, LangChain, Airflow, Azure, MongoDB, Flask

## Achievements

- Code For Her: Featured in coverage of Locus's Code For Her hackathon; shared publicly on LinkedIn.
- IntersectX: Featured in coverage of the Global Agent Hackathon by Agno ([PR 126](https://github.com/global-agent-hackathon/global-agent-hackathon-may-2025/pull/126)).
```

- [ ] **Step 3: Create `content/blog/hello-world.md`**

Create `content/blog/hello-world.md` with:
```markdown
---
title: "Hello World 🤖"
date: 2025-10-02
tags: ["First Post"]
---

This is my very first blog post. Think of it as a small step into trying out new things. Upcoming posts will be about my journey of learning, experimenting, and gaining fresh insights. I'll also share some of the problems I try to solve in day-to-day life—nothing revolutionary, but steady 0.1% improvements each day.

In a way, this blog is like a time machine for me: a place to log the different things I've tried so I can look back on them in the future. I'm excited to see where this goes, and I'm already looking forward to the next post. See you again soon!
```

- [ ] **Step 4: Build the site and verify expected routes render**

Run:
```bash
hugo --gc --minify && find public -name index.html | sort
```
Expected: build reports pages built with 0 errors; `find` output includes `public/index.html`, `public/cv/index.html`, `public/blog/index.html`, and `public/blog/hello-world/index.html`.

- [ ] **Step 5: Verify the menu and post list appear**

Run:
```bash
grep -o 'href="/cv/"' public/index.html | head -1 && grep -o 'hello-world' public/blog/index.html | head -1
```
Expected: prints `href="/cv/"` (menu link present on home) and `hello-world` (post listed on the blog index).

- [ ] **Step 6: Commit**

```bash
git add content
git commit -m "feat: migrate home, CV, and first blog post to Hugo content"
```

---

### Task 5: Add agent docs (AGENTS.md + CLAUDE.md)

**Files:**
- Create: `AGENTS.md`, `CLAUDE.md`

- [ ] **Step 1: Create `AGENTS.md`**

Create `AGENTS.md` with:
```markdown
# AGENTS.md

## Background

- Minimal personal website: short intro + a markdown blog and a CV page.
- Hosted free on GitHub Pages, deployed on push to `master`.
- All content authored as markdown. One `.md` = one page.

## Stack

- Hugo (extended)
- Theme: `janraasch/hugo-bearblog` (git submodule at `themes/hugo-bearblog`, not edited)
- GitHub Actions → GitHub Pages
- No custom CSS — default theme styling, automatic dark mode

## Commands

\`\`\`bash
brew install hugo                 # one-time, extended build
git submodule update --init       # populate the theme after a fresh clone
hugo server -D                    # local preview with drafts at localhost:1313
hugo --gc --minify                # production build into ./public
\`\`\`

## Repo Structure

- `content/` — markdown pages. Folder layout = URL layout.
  - `content/_index.md` — home page
  - `content/cv.md` — CV → `/cv/`
  - `content/blog/*.md` — blog posts → `/blog/<slug>/` (auto-listed at `/blog/`)
- `hugo.toml` — site config (title, baseURL, theme, params, menu)
- `themes/hugo-bearblog/` — theme submodule
- `.github/workflows/hugo.yaml` — build + deploy

## Conventions

- Add a blog post: create `content/blog/<slug>.md` with front matter `title`, `date`, `tags`.
- Add a page: create `content/<name>.md` with front matter `title`; add a `[[menu.main]]` entry in `hugo.toml` if it should appear in the nav.
- Keep front matter minimal: `title`, `date`, `tags`. No `layout`/`permalink` (Hugo handles routing).
- Don't edit the theme submodule. To restyle, add `layouts/partials/custom_head.html`.

## License

- Code & templates: MIT.
- Blog content (everything under `content/`): CC BY-NC 4.0.
```

- [ ] **Step 2: Create `CLAUDE.md`**

Create `CLAUDE.md` with:
```markdown
# CLAUDE.md

See [AGENTS.md](AGENTS.md) for stack, structure, commands, and conventions.
```

- [ ] **Step 3: Verify the build still succeeds (these files must not become pages)**

Run:
```bash
hugo --gc --minify && ls public/agents public/claude 2>&1 | grep -c "No such file" || true
```
Expected: build succeeds; prints `2` (top-level `AGENTS.md`/`CLAUDE.md` outside `content/` are not rendered as site pages).

- [ ] **Step 4: Commit**

```bash
git add AGENTS.md CLAUDE.md
git commit -m "docs: add AGENTS.md agent guide and CLAUDE.md pointer"
```

---

### Task 6: Add LICENSE and rewrite README

**Files:**
- Create: `LICENSE`
- Modify: `README.md` (full rewrite)

- [ ] **Step 1: Create `LICENSE` (MIT, code)**

Create `LICENSE` with:
```
MIT License

Copyright (c) 2026 Mathana Mathav A S

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

- [ ] **Step 2: Rewrite `README.md`**

Replace the entire contents of `README.md` with:
```markdown
# mathanamathav.github.io

My personal website — a short intro, a markdown blog, and a CV. Built with [Hugo](https://gohugo.io/) and the [hugo-bearblog](https://github.com/janraasch/hugo-bearblog) theme, deployed to GitHub Pages.

## Run locally

\`\`\`bash
brew install hugo                 # extended build, one-time
git submodule update --init       # pull the theme after a fresh clone
hugo server -D                    # http://localhost:1313
\`\`\`

## Add content

- Blog post: create `content/blog/<slug>.md` with front matter `title`, `date`, `tags`.
- Page: create `content/<name>.md` with front matter `title`.

## Deploy

Push to `master` (via PR). GitHub Actions builds with Hugo and publishes to Pages. Pages source must be set to **GitHub Actions** in repo Settings → Pages.

## License

- **Code & templates** (config, workflow, theme overrides): [MIT](LICENSE).
- **Blog content** (everything under `content/`): [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — reuse with attribution, non-commercial.
```

- [ ] **Step 3: Verify**

Run:
```bash
head -1 LICENSE && grep -c "CC BY-NC" README.md
```
Expected: prints `MIT License` and `1`.

- [ ] **Step 4: Commit**

```bash
git add LICENSE README.md
git commit -m "docs: add MIT license and Hugo README with dual-license note"
```

---

### Task 7: Rewrite .gitignore for Hugo

**Files:**
- Modify: `.gitignore` (full rewrite)

- [ ] **Step 1: Replace `.gitignore`**

Replace the entire contents of `.gitignore` with:
```
# Hugo
/public/
/resources/_gen/
.hugo_build.lock

# OS
.DS_Store
```

- [ ] **Step 2: Verify build output is ignored**

Run:
```bash
hugo --gc --minify >/dev/null && git status --porcelain public | wc -l | tr -d ' '
```
Expected: prints `0` (the freshly built `public/` is untracked-and-ignored, so it does not appear in status).

- [ ] **Step 3: Commit**

```bash
git add .gitignore
git commit -m "chore: gitignore Hugo build output"
```

---

### Task 8: Add the GitHub Pages deploy workflow

**Files:**
- Create: `.github/workflows/hugo.yaml`

- [ ] **Step 1: Create `.github/workflows/hugo.yaml`**

Create `.github/workflows/hugo.yaml` with:
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

- [ ] **Step 2: Verify YAML is valid**

Run:
```bash
python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/hugo.yaml')); print('valid')"
```
Expected: prints `valid`.

- [ ] **Step 3: Commit**

```bash
git add .github/workflows/hugo.yaml
git commit -m "ci: add GitHub Pages deploy workflow for Hugo"
```

---

### Task 9: Final local verification

**Files:** none (verification only)

- [ ] **Step 1: Clean build from scratch**

Run:
```bash
rm -rf public resources && hugo --gc --minify
```
Expected: "Total in ... ms", 0 errors/warnings about missing layouts.

- [ ] **Step 2: Confirm all expected routes exist**

Run:
```bash
for p in index cv/index blog/index blog/hello-world/index; do test -f "public/$p.html" && echo "OK $p" || echo "MISSING $p"; done
```
Expected: four `OK` lines, no `MISSING`.

- [ ] **Step 3: Spot-check the live preview (manual)**

Run:
```bash
hugo server -D
```
Then open http://localhost:1313 and confirm: home shows the intro; nav shows Home/Blog/CV; `/blog/` lists the post; `/cv/` renders sections; dark mode follows the OS setting. Stop the server with Ctrl-C.

- [ ] **Step 4: Confirm working tree is clean**

Run:
```bash
git status --porcelain
```
Expected: empty output (all changes committed; `public/`/`resources/` ignored).

---

### Task 10: Ship (manual / owner)

**Files:** none

- [ ] **Step 1: Set Pages source (one-time, cannot be scripted)**

In GitHub: repo **Settings → Pages → Source = GitHub Actions**.

- [ ] **Step 2: Push the branch and open a PR**

Run:
```bash
git push -u origin dev
gh pr create --base master --title "Migrate site to Hugo + bearblog" --body "Replaces Jekyll with Hugo + hugo-bearblog. See docs/superpowers/specs/2026-06-14-hugo-bearblog-migration-design.md"
```
Expected: PR created against `master`.

- [ ] **Step 3: Merge and verify deploy**

After merging to `master`, watch the Action:
```bash
gh run watch
```
Expected: the "Deploy Hugo site to Pages" workflow succeeds; the site loads at https://mathanamathav.github.io/.

---

## Notes for the implementer

- Hugo is **not installed locally** at plan time — Task 1 Step 1 installs it. Every verification step after that assumes `hugo` is on PATH.
- The theme is a **submodule**: a fresh clone needs `git submodule update --init` before any build.
- `hugo.toml` param names are authoritative in the **theme's** `exampleSite/hugo.toml` (Task 1 Step 4). If they differ from this plan, follow the theme.
- The old post URL was `/blog/2025/10/hello-world/`; the new one is `/blog/hello-world/`. This is an intentional, accepted change (new site, no inbound links).
- In Tasks 5 and 6, the `AGENTS.md` / `README.md` bodies contain code fences shown here as `\`\`\`` (escaped) only because they are nested inside this plan's own fences. When writing those files, use real triple-backtick fences — do not write the backslashes.
