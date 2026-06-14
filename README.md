# mathanamathav.github.io

My personal website — a short intro, a markdown blog, and a CV. Built with [Hugo](https://gohugo.io/) and the [hugo-bearblog](https://github.com/janraasch/hugo-bearblog) theme, deployed to GitHub Pages.

## Run locally

```bash
brew install hugo                 # extended build, one-time
git submodule update --init       # pull the theme after a fresh clone
hugo server -D                    # http://localhost:1313
```

## Add content

- Blog post: create `content/blog/<slug>.md` with front matter `title`, `date`, `tags`.
- Page: create `content/<name>.md` with front matter `title`.

## Deploy

Push to `master` (via PR). GitHub Actions builds with Hugo and publishes to Pages. Pages source must be set to **GitHub Actions** in repo Settings → Pages.

## License

- **Code & templates** (config, workflow, theme overrides): [MIT](LICENSE).
- **Blog content** (everything under `content/`): [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) — reuse with attribution, non-commercial.
