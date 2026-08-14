# Computing Geometrical Measures of Topological Holes
halurl: 'https://hal.science/hal-04322031v1'
codeurl: 'https://github.com/Yann-Situ/Hole-Measures'

excerpt: 'We define and compute two specific balls for every hole of a geometric object. One ball corresponds to the <i>thickness</i> (~fragility, in red), whereas the other corresponds to the <i>breadth</i> (~size, in blue) of the hole.'
excerptimg: '<img src="/images/figures/eight-m-01.png" alt="eight hole balls"> 
<img src="/images/figures/gear-m-1.png" alt="gear hole balls"> 
<img src="/images/figures/knot-m-01.png" alt="knot hole balls"> 
<img src="/images/figures/triakis-tetrahedron-m-1.png" alt="triakis hole balls">'

<img src="/images/figures/graphical-abstract.png" alt="hole balls graphical abstract" width="750">
# A constructive approach of Alexander duality

excerpt: 'We prove a combinatorial and geometric version of Alexander duality with a constructive proof, based on HDVFs.
This allow us to define four different representations of homological holes, named <i>homology quartets</i>.'
excerptimg: '<img src="/images/figures/2D-T-K-HC.png" alt="HDVF on a complex K"> 
  <img src="/images/figures/2D-T-Kc-HC.png" alt="HDVF on its complementary complex Kc"> 
  <img src="/images/figures/2D-T-sphere-HC-KcupKc.png" alt="HDVF on S2"> 
  <img src="/images/figures/homology-quartet.png" alt="homology quartets">'
halurl: 'https://hal.science/hal-05003653v1'

**Abstract**. Alexander duality establishes the relation between the homology of an object and the cohomology of its complement in a sphere. For instance, if \\(X\\) is a subset of the 2-dimensional sphere \\(\mathbb{S}^2\\), then each hole of \\(X\\) corresponds to a connected component of \\(\mathbb{S}^2 \backslash X\\), and by symmetry, each hole of corresponds to a connected component of \\(\mathbb{S}^2 \backslash X\\). In this paper, we present a new combinatorial and constructive proof of Alexander duality that provides an explicit isomorphism. The proof shows how to compute this isomorphism using a combinatorial tool called the homological discrete vector field. It also provides a one-to-one map between the holes of the object and the holes of its complement, which we use for representing the holes of an object embedded in \\(\mathbb{R}^3\\).

<div class="image-row" style="height: 170px; gap: 25px">
  <img src="/images/figures/2D-T-K-HC.png" alt="HDVF on a complex K"> 
  <img src="/images/figures/2D-T-Kc-HC.png" alt="HDVF on its complementary complex Kc"> 
  <img src="/images/figures/2D-T-sphere-HC-KcupKc.png" alt="HDVF on S2"> 
  <img src="/images/figures/homology-quartet.png" alt="homology quartets">
</div>
Some homology quartets, which can be also visualized <a href="https://pageperso.lis-lab.fr/aldo.gonzalez-lorenzo/papers/alexander-duality/quartets.html">here</a>:
<div class="image-row">
  <img src="/images/figures/quartet-bone.png" alt="quartets of a bone" width="750">
</div>
<div class="image-row">
  <img src="/images/figures/quartet-link.png" alt="quartets of a link" width="750">
</div>


# Stability and extension of steady and ranging persistence
halurl: 'https://hal.science/hal-05477180v1'
codeurl: 'https://github.com/Yann-Situ/Hypergraph-Steady-Ranging-Persistence'
excerpt: 'We extend <i>steady</i> and <i>ranging</i> persistence from graphs to other categories, and provide a characterization of the features the give rise to stable <i>steady</i> and <i>ranging</i> persistent diagrams. We show examples for the category of hypergraphs.'
excerptimg: '<img src="/images/figures/filtration-2.png" alt="hypergraph filtration">'

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

# Characterization of the Computed Homology and Cohomology Bases
halurl: 'https://hal.science/hal-05357027v1'
excerpt: 'We provide a combinatorial characterization of the homology bases computed by standard computational homology methods (discrete Morse theory, standard persistent homology, modified Smith normal form, tri-partitions), using homological discrete vector fields.'
excerptimg: '<img src="/images/figures/cub-cplx1-1.png" alt="perfect hdvf">
<img src="/images/figures/cub-cplx1-2.png" alt="explicit homology basis">'

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