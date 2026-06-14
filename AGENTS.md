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

```bash
brew install hugo                 # one-time, extended build
git submodule update --init       # populate the theme after a fresh clone
hugo server -D                    # local preview with drafts at localhost:1313
hugo --gc --minify                # production build into ./public
```

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
