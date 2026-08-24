---
title: "Gallery"
layout: splash
permalink: /gallery/
author_profile: true
class: wide
---

{% include base_path %}

{% for category in site.gallery_category %}
  <div class="gallery-category">

    <h2>{{ category[1].title }}</h2>

    <div class="gallery-grid">
      {% for post in site.gallery reversed %}
        {% if post.category != category[0] %}
          {% continue %}
        {% endif %}

        <a href="{{ post.target_url | relative_url }}" class="gallery-item">
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

      {% endfor %}
    </div>

  </div>
{% endfor %}
