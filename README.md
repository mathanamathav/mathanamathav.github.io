# Personal Static Website 🌐

This is a minimal static website powered by **Jekyll** and designed to be hosted automatically on **GitHub Pages**.

All content on this site is written purely in Markdown (`.md`) files. The simple structure makes it trivial to write and publish new posts and pages!

## 🚀 Running Locally

If you want to test and view the website on your own machine before pushing to GitHub, follow these simple steps.

### Prerequisites

You will need Ruby and Bundler installed on your system. (Macs usually come with Ruby pre-installed).
- [Ruby](https://www.ruby-lang.org/en/documentation/installation/)
- [Bundler](https://bundler.io/): install via `gem install bundler`

### 1. Install Dependencies

Open your terminal, navigate to this repository folder, and install the required Ruby gems (this ensures your local environment mirrors exactly what GitHub Pages uses):

```bash
bundle install
```

### 2. Start the Local Server

Once the dependencies are installed, you can start the Jekyll development server by running:

```bash
bundle exec jekyll serve
```

### 3. View the Site

Open your favorite web browser and navigate to:
👉 **[http://localhost:4000](http://localhost:4000)**

*Note: The server will automatically detect and apply changes when you modify the `.md` files or `_config.yml` (though changes to `_config.yml` require restarting the server).*

---

### Folder Structure

- `_posts/`: All blog posts go here. They must follow the format `YYYY-MM-DD-title.md`.
- `_pages/`: Contains all static pages (like `cv.md` or `about.md`).
- `_config.yml`: The primary settings file for site configuration (title, theme, etc.).
- `Gemfile`: Specifies the dependencies (specifically, the `github-pages` gem) for accurate local rendering.
