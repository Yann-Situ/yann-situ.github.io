---
title: "Stability and extension of steady and ranging persistence"
collection: publications
category: journals
permalink: /publication/2025-12-01-Stability-and-extension-of-steady-and-ranging-persistence
excerpt: 'We extend <i>steady</i> and <i>ranging</i> persistence from graphs to other categories, and provide a characterization of the features that give rise to stable <i>steady</i> and <i>ranging</i> persistent diagrams. We show examples for hypergraphs.'
excerptimg: '<img src="/images/figures/filtration-2.png" alt="hypergraph filtration">'
date: 2025-12-01
venue: 'Journal of Applied and Computational Topology'
paperurl: 'http://dx.doi.org/10.1007/s41468-025-00228-6'
bibtexurl: 'https://yann-situ.github.io/files/bibtex/2025-12-01-Stability-and-extension-of-steady-and-ranging-persistence.bib'
halurl: 'https://hal.science/hal-05477180v1'
codeurl: 'https://github.com/Yann-Situ/Hypergraph-Steady-Ranging-Persistence'
author: ' Yann-Situ Gazull'
citation: ' Yann-Situ Gazull, &quot;Stability and extension of steady and ranging persistence.&quot; Journal of Applied and Computational Topology, 2025.'
---
**Abstract**. Persistent homology is a topological data analysis tool that has been widely generalized, extending its scope beyond the field of topology. Among its extensions, steady and ranging persistence were developed to study a wide variety of graph properties. Precisely, given a feature of interest on graphs, it is possible to build two types of persistence (steady and ranging persistence) that follow the evolution of the feature along graph filtrations. This study extends steady and ranging persistence to other objects using category theory and investigates the stability of such persistence. In particular, a characterization of the features that induce balanced steady and ranging persistence is provided. The main results of this study are illustrated using a practical implementation for hypergraphs.

<div class="image-row" style="height: 170px; gap: 25px">
<img src="/images/figures/filtration-2.png" alt="hypergraph filtration"> 
</div>
<div class="image-row" style="height: 170px; gap: 25px">
<img src="/images/figures/Hgph-diagram.png" alt="hypergraph categories diagram"> 
<img src="/images/figures/Hgph-mono-diagram.png" alt="hypergraph monomorphisms diagram">
</div>
<br>

Examples were conducted with hypergraph filtrations derived from Shakespeare plays. The code can be found <a href="https://github.com/Yann-Situ/Hypergraph-Steady-Ranging-Persistence">here</a>.
Here is the <i>scene</i> hypergraph filtration of the play <i>King Lear</i> at \\(t=5\\) and \\(t=8\\):
<div class="image-row" style="height: 300px; gap: 25px">
<img src="/images/figures/H-scene-5.png" alt="King lear scene hypergraph t=5"> 
<img src="/images/figures/H-scene-8.png" alt="King lear scene hypergraph t=8"> 
</div>
<br>
Here is the steady persistence diagram of the <i>mean originality</i> feature, computed on the aforementionned hypergraph filtration:
<img src="/images/figures/king_lear-scene-steady-o.png" alt="King lear steady persistence of mean originality" width=750px> 