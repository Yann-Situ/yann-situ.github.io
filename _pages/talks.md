---
layout: archive
title: "Talks and presentations"
permalink: /talks/
author_profile: true
---

## Conferences and Workshops
---  
 - _GTMG 2026_. Paris (Jussieu). March 2026.\\
  Presentation: _Experiments on the Space of Homology Computations_, presented with Menjatiana Andrianabinitsoa.
 - _DGMM 2025_. Gröningen, Nederland. November 2025.\\
  Presentation: _Characterization of the Computed Homology and Cohomology bases_.
 - _CGAL Days_. Sophia Antipolis. April 2025.\\
  Presentation: _Homological Discrete Vector Fields... 1 year later..._, presented with Alexandra Bac.
 - _GTMG 2025_. Poitiers. March 2025.\\
  Presentation: _Ongoing Works about Homology Configurations_, best presentation prize.
 - _Geometry and Computing_. Marseille (CIRM). October 2024.\\
  Presentation: _A Versatile Tool for Computing and Understanding Homology_.
 - _R-GTMG_. Marseille (CIRM). March 2024.\\
  Presentation: _A Constructive Approach to Alexander Duality_.
 - _SPM 2023_. Genova, Italia. July 2023.\\
  Presentation: _Computing Geometrical Measures of Topological Holes_, second best paper award.
 - _GTMG 2021_. Online. March 2021.\\
   Presentation: _Measuring Holes of 3D Meshes_, best student presentation prize.
    
## Seminars
---

 - _Séminaires Topocs_. Marseille. May, June and November 2025.\\
Presentations: _Structures in Combinatorial Homology_, _A Constructive Approach to Alexander Duality_, _Homology Configurations_.
 - _Demi-journée du Pôle Calcul_. Marseille. December 2022.\\
    Presentation: _Étude d'Objets Homologiques Computationnels_.


{% if site.talkmap_link == true %}

<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of all the places I've given a talk!</a></p>

{% endif %}

{% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %}
