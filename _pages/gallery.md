---
title: "Gallery"
layout: splash
permalink: /gallery/
author_profile: true
---

{% include base_path %}

<div class="gallery-tags">
  <a href="{{ relative_url }}" class="gallery-tag-all active">All</a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  {% for tag in site.gallery_tags %}
    <a href="{{ tag.url | relative_url }}" class="gallery-tag">{{ tag.title }}</a>
  {% endfor %}
</div>

<div class="gallery-grid">
  {% for post in site.gallery reversed %}
    {% if post.collection == "gallery" %}
      <a href="{{ post.target_url | relative_url }}" class="gallery-item {{ post.wide }}">
        <div class="gallery-image">
          <img
            src="{{ post.thumbnail | relative_url }}"
            alt="{{ post.title }}"
            loading="lazy">

          <div class="gallery-hover-title">
            {{ post.title }}
          </div>
        </div>
      </a>
    {% endif %}

  {% endfor %}
</div>

