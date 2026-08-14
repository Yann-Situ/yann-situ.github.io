---
title: "Characterization of the Computed Homology and Cohomology Bases"
collection: publications
category: articles
permalink: /publication/2025-01-01-Characterization-of-the-Computed-Homology-and-Cohomology-Bases
excerpt: 'We provide a combinatorial characterization of the homology bases computed by standard computational homology methods (discrete Morse theory, standard persistent homology, modified Smith normal form, tri-partitions), using homological discrete vector fields.'
excerptimg: '<img src="/images/figures/cub-cplx1-1.png" alt="perfect hdvf">
<img src="/images/figures/cub-cplx1-2.png" alt="explicit homology basis">'
date: 2025-01-01
venue: 'Proceedings of International Conference on Discrete Geometry and Mathematical Morphology'
paperurl: 'https://dx.doi.org/10.1007/978-3-032-09544-2_12'
bibtexurl: 'https://yann-situ.github.io/files/bibtex/2025-01-01-Characterization-of-the-Computed-Homology-and-Cohomology-Bases.bib'
halurl: 'https://hal.science/hal-05357027v1'
author: ' Yann-Situ Gazull,  Aldo Gonzalez-Lorenzo,  Alexandra Bac'
citation: ' Yann-Situ Gazull,  Aldo Gonzalez-Lorenzo,  Alexandra Bac, &quot;Characterization of the Computed Homology and Cohomology Bases.&quot; Proceedings of International Conference on Discrete Geometry and Mathematical Morphology, 2025.'
---
**Abstract**. Computing homology and cohomology is at the heart of many recent works and a key issue for topological data analysis. Among homological objects, homology generators are useful to locate or understand holes (especially for geometric objects). The present paper provides a characterization of the class of homology bases that are computed by standard algorithmic methods. The proof of this characterization relies on the Homological Discrete Vector Field, a combinatorial structure for computing homology, which encompasses several standard methods (persistent homology, tri-partitions, Smith Normal Form, discrete Morse theory). These results refine the combinatorial homology theory and provide novel ideas to gain more control over the computation of homology generators.

<br>
Here is an example of a 1-homology basis (right) computed by a perfect HDVF (left):

<div class="image-row" style="height: 150px; gap: 40px">
<img src="/images/figures/cub-cplx1-1.png" alt="perfect hdvf">
<img src="/images/figures/cub-cplx1-2.png" alt="explicit homology basis">
</div>

<br>
Intuitively, a \\(q\\)-homology basis is explicit if the two following properties are satisfied:
- no generator is included in the union of other generators;
- the complex derived from the union of all homology generators has as many \\(q\\)-holes as the original complex.

Here are examples of three non-explicit homology bases. Can you see why they are not explicit?
<div class="image-row" style="height: 150px; gap: 40px">
<img src="/images/figures/cub-cplx1-4.png" alt="non-explicit homology basis">
<img src="/images/figures/cub-cplx2-2.png" alt="non-explicit homology basis">
<img src="/images/figures/cub-cplx3-1.png" alt="non-explicit homology basis">
</div>
<br>