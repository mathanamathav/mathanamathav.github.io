# AGENTS.md

## Background

- Minimal personal website: short intro + a markdown blog and a CV page.
- Hosted free on GitHub Pages, deployed on push to `master`.
- All content authored as markdown. One `.md` = one page.

## Stack

- Hugo (extended)
- Theme: `janraasch/hugo-bearblog` (git submodule at `themes/hugo-bearblog`, not edited)
- GitHub Actions → GitHub Pages
- Custom styling in `layouts/partials/custom_head.html`: warm light palette, Montserrat headings, Merriweather body text (self-hosted in `static/fonts/`)

## Commands

```bash
brew install hugo                 # one-time, extended build
git submodule update --init       # populate the theme after a fresh clone
hugo server -D                    # local preview with drafts at localhost:1313
hugo --gc --minify                # production build into ./public
scripts/update-cv.sh              # refresh the CV PDF + HTML from ../Latex_Resume
```

## Repo Structure

- `content/` — markdown pages. Folder layout = URL layout.
  - `content/_index.md` — home page
  - `content/cv.md` — CV → `/cv/` (PDF buttons + resume as HTML via the `cv` shortcode)
  - `content/projects.md` — projects → `/projects/`
  - `content/blog/*.md` — blog posts → `/blog/<slug>/` (auto-listed at `/blog/`)
- `hugo.toml` — site config (title, baseURL, theme, params, menu)
- `themes/hugo-bearblog/` — theme submodule
- `.github/workflows/hugo.yaml` — build + deploy

## Conventions

- Add a blog post: create `content/blog/<slug>.md` with front matter `title`, `date`, `tags`.
- Add a page: create `content/<name>.md` with front matter `title`; add a `[[menu.main]]` entry in `hugo.toml` if it should appear in the nav.
- Keep front matter minimal: `title`, `date`, `tags`. No `layout`/`permalink` (Hugo handles routing).
- Don't edit the theme submodule. To restyle, edit `layouts/partials/custom_head.html`.
- Update the CV: `scripts/update-cv.sh [path-to-Latex_Resume]` rebuilds the LaTeX resume, copies the PDF into `static/cv/`, regenerates `assets/cv/resume.html` with `scripts/tex2html.py`.
- Posts written with AI editing help get the tag `AI-assisted`; the post template then shows a small "Written by me, edited with AI help" note under the date.
- Writing style: plain, first person, no em dashes or stacked hyphen chains.

## License

- Code & templates: MIT.
- Blog content (everything under `content/`): CC BY-NC 4.0.
