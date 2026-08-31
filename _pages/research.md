---
layout: archive
title: "Research Interests"
permalink: /research/
author_profile: true
---

I mostly like to practice mathematics that have a strong visual aspect.
My research interests are mainly related to topology and geometry, from discrete and combinatorial points of view.
In particular, I have worked a lot on _computational homology_, and around the notion of _hole_.

I have also worked on research topics related to _geometry processing_, _computer graphics_, _(hyper)graph theory_, _category theory_, _digital geometry_.

<br>

# Publications
{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}
<!-- YS adding: -->
{% if site.author.hal %}
  <div class="wordwrap">You can also find my publications on <a href="{{site.author.hal}}">HAL</a>.</div>
{% endif %}

{% include base_path %}
<!-- New style rendering if publication categories are defined -->
{% if site.publication_category %}
  {% for category in site.publication_category  %}
    {% assign title_shown = false %}
    {% for post in site.publications reversed %}
      {% if post.category != category[0] %}
        {% continue %}
      {% endif %}
      {% unless title_shown %}
## {{ category[1].title }}
---
        {% assign title_shown = true %}
      {% endunless %}
      {% include archive-single.html %}
    {% endfor %}
  {% endfor %}
{% else %}
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
{% endif %}

<br>

# Talks
## Conferences and Workshops
---
 - **GTMG 2026**. Paris (Jussieu). March 2026.\\
  Presentation: _Experiments on the Space of Homology Computations_, presented with Menjatiana Andrianabinitsoa.
 - **DGMM 2025**. Gröningen, Nederland. November 2025.\\
  Presentation: _Characterization of the Computed Homology and Cohomology bases_.
 - **CGAL Days**. Sophia Antipolis. April 2025.\\
  Presentation: _Homological Discrete Vector Fields... 1 year later..._, presented with Alexandra Bac.
 - **GTMG 2025**. Poitiers. March 2025.\\
  Presentation: _Ongoing Works about Homology Configurations_, best presentation award.
 - **Geometry and Computing**. Marseille (CIRM). October 2024.\\
  Presentation: _A Versatile Tool for Computing and Understanding Homology_.
 - **R-GTMG**. Marseille (CIRM). March 2024.\\
  Presentation: _A Constructive Approach to Alexander Duality_.
 - **SPM 2023**. Genova, Italia. July 2023.\\
  Presentation: _Computing Geometrical Measures of Topological Holes_, second best paper award.
 - **GTMG 2021**. Online. March 2021.\\
   Presentation: _Measuring Holes of 3D Meshes_, best student presentation award.
   
## Seminars
---
 - **Topocs Seminars** (topology in computer science). Marseille (LIS). May, June and November 2025.\\
    - Presentation: _Structures in Combinatorial Homology_.
    - Presentation: _A Constructive Approach to Alexander Duality_.
    - Presentation: _Homology Configurations_.
 - **Demi-journée du Pôle Calcul**. Marseille (LIS). December 2022.\\
    Presentation: _Étude d'Objets Homologiques Computationnels_.


<!-- {% if site.talkmap_link == true %}

<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of all the places I've given a talk!</a></p>

{% endif %} -->

<!-- {% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %} -->
