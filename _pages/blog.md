---
layout: page
title: Blog
permalink: /blog/
---

<div class="blog-list">
  {% for blog in site.blogs reversed %}
    <article style="margin-bottom: 3rem;">
      <h2 style="margin-bottom: 0.2rem;">
        <a href="{{ blog.url }}" style="text-decoration: none; color: var(--foreground);">{{ blog.title }}</a>
      </h2>
      <p style="font-size: 0.9rem; color: var(--muted-foreground); margin-top: 0; margin-bottom: 1rem;">
        <time datetime="{{ blog.date | date_to_xmlschema }}">{{ blog.date | date: "%B %d, %Y" }}</time>
      </p>
      <p style="margin-top: 0; margin-bottom: 0.5rem; color: var(--text-secondary);">
        {{ blog.excerpt | strip_html | truncatewords: 35 }}
      </p>
      <a href="{{ blog.url }}" style="font-size: 0.95rem; font-weight: 600;">Read post &rarr;</a>
    </article>
  {% endfor %}
</div>
