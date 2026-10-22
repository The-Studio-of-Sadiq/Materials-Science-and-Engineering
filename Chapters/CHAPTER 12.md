# Chapter 12 — Dislocation Theory

*Part III · Mechanical Behaviour*

Silicon wafers for microchips are grown as single crystals 300 mm in diameter and nearly free of dislocations. During one high-temperature furnace step, a production line found that wafers loaded too quickly into the hot tube developed lines of "slip" visible under a bright light: rows of tiny steps on the polished surface, radiating from the edges where the wafer had touched its quartz support. The thermal stress had never approached the theoretical strength of silicon — it was a few megapascals — yet the wafers had deformed plastically, and the slip lines ruined the devices that crossed them. On the other side of the materials world, a copper wire that yields at 60 MPa when annealed yields at 350 MPa after cold drawing, with no change in composition at all. A steel bridge cable, a jet-engine disc, an aluminium can and a silicon wafer all owe their plastic behaviour to the same defect: the dislocation.

Chapter 5 introduced dislocations as line defects with a Burgers vector. This chapter develops their theory: why they are needed to explain real strengths, what stress fields they carry, what forces act on them, how they move, multiply and interact, how they split into partials, how their behaviour differs between crystal structures, and how they are seen.

> **Why do crystals yield at stresses thousands of times smaller than the strength of their bonds?**
> **What controls how easily dislocations move and multiply, and why do FCC, BCC and HCP metals and ceramics behave so differently?**

| Concept | Engineering destination |
|---|---|
| Theoretical versus real strength | Whiskers, nanopillars, defect-free silicon; why strengthening is possible at all |
| Stress fields, line energy, line tension | Solute atmospheres, dislocation walls, bowing between precipitates |
| Peach–Koehler force; glide and climb | Yield under complex loads, creep at high temperature |
| Jogs, kinks, junctions, forest hardening | Work hardening of cold-worked wire, sheet and forgings |
| Frank–Read and other sources | Dislocation multiplication in forming; slip in wafers |
| Partials and stacking-fault energy | Cross-slip, recovery, TWIP/TRIP steels, stress-corrosion behaviour |
| Peierls stress and crystal structure | Ductile–brittle transition of ferritic steels, limited ductility of Mg, Ti and ceramics |
| Observing dislocations | TEM, etch pits, X-ray topography, EBSD in failure analysis and process control |

**Roadmap.** Theoretical versus real strength (12.1) → geometry recap (12.2) → stress fields and energy (12.3) → forces, glide and climb (12.4) → interactions and forest hardening (12.5) → multiplication (12.6) → partial dislocations and stacking-fault energy (12.7) → dislocations in different crystal structures (12.8) → how they are observed (12.9).

---

## 12.1 Theoretical shear strength versus real strength

### Frenkel's estimate

Imagine shearing a perfect crystal by sliding one plane of atoms rigidly over the next. The shear stress needed must be periodic in the displacement $x$, with period equal to the interatomic spacing $b$ in the slip direction, and it must vanish both at $x=0$ (the perfect crystal) and at $x=b/2$ (an unstable position halfway between sites). The simplest such function is a sine:

$$
\tau=\tau_{\max}\sin\frac{2\pi x}{b}
$$

For small displacements this must reduce to Hooke's law, $\tau=G\gamma=Gx/d$, where $d$ is the spacing between the planes. Matching slopes at $x=0$ gives Frenkel's theoretical shear strength (1926):

$$
\tau_{\max}=\frac{G}{2\pi}\,\frac bd\approx\frac G{2\pi}
$$

> **Status of the principle: Frenkel theoretical shear strength**
> *Approximate.* Assumes rigid planes and a sinusoidal force law; more realistic interatomic potentials and the existence of metastable stacking positions (stacking faults) lower the estimate to about $G/30$, but the order of magnitude, a few percent of $G$, is confirmed by atomistic calculations and by experiments on defect-free crystals.

<!-- FIGURE 12.1 | figures/ch12/fig-12-1-frenkel-and-slip.png | schematic | Rigid shear of a perfect crystal compared with slip by dislocation motion. | Content: Top panel: two rows of atoms (circles), upper row displaced by x relative to lower; below it a plot of shear stress τ versus x/b from 0 to 1, sinusoid with maximum τmax = G b/(2π d) at x/b = 0.25, labelled "theoretical shear strength ≈ G/2π ≈ 7–9 GPa for Cu", initial slope labelled "G x/d". Bottom panel: three-frame sequence of an edge dislocation (extra half-plane marked ⊥) moving across a block of 8 × 6 atoms from left to right under shear arrows τ, ending in a step of one Burgers vector b on the right surface; small inset of a carpet with a ruck being pushed across the floor labelled "a ruck moves a carpet with little force". -->

**Worked example — How weak is a real copper crystal?** For copper, the polycrystalline shear modulus is $G=48$ GPa. Slip occurs on $\{111\}$ planes, spaced $d=a/\sqrt3=0.3615/1.732=0.2087$ nm apart, in $\langle110\rangle$ directions, where the repeat distance is $b=a/\sqrt2=0.2556$ nm. Then

$$
\tau_{\max}=\frac{48\times10^9}{2\pi}\times\frac{0.2556}{0.2087}=7.64\times10^9\times1.225=9.4\ \mathrm{GPa}
$$

Measured critical resolved shear stresses of well-annealed high-purity copper single crystals are 0.5–1 MPa. The discrepancy is a factor of roughly $10^4$. With $G/30$ instead, the theoretical value is still 1.6 GPa, three orders of magnitude above experiment. No refinement of the force law can close a gap of this size; a different mechanism must operate.

### The resolution: dislocations

In 1934 Taylor, Orowan and Polanyi independently proposed that slip does not occur by rigid sliding but by the motion of a line defect — the **dislocation** — that separates slipped from unslipped regions of the plane. As the dislocation moves, only the bonds along its line are rearranged at any instant, each by a fraction of an atomic spacing, so the stress needed is a tiny fraction of the theoretical strength. When the dislocation reaches the surface, the crystal above the slip plane has been displaced by one Burgers vector, exactly as if the planes had slid rigidly (Figure 12.1). A ruck in a carpet makes the same point: the whole carpet can be moved a short distance by pushing the ruck across it with a small force, whereas dragging it all at once takes a large one.

Two lines of evidence confirm the picture. Dislocations were seen directly by transmission electron microscopy in 1956 (Section 12.9). And crystals that contain no mobile dislocations do approach theoretical strength: micrometre-sized metal **whiskers** grown from the vapour reach elastic strains of 2–5 % and shear strengths near $G/30$; copper and gold nanopillars below about 100 nm, and defect-free silicon nanowires, reach gigapascal strengths. Bulk dislocation-free silicon wafers are strong only until a dislocation is nucleated at an edge chip or scratch, after which slip spreads easily at high temperature — the opening problem of this chapter.

The engineering consequence is profound. Because real crystals are weak *because of* the mobility of dislocations, they can be made strong by **impeding** that mobility. Every strengthening mechanism in Chapter 13 — work hardening, solutes, grain boundaries, precipitates — works by placing obstacles in the path of dislocations.

---

## 12.2 Dislocation geometry: a recap

Chapter 5 defined the essentials, summarized here for use below.

- A dislocation is characterized by its **line direction** $\boldsymbol\xi$ (a unit vector tangent to the line) and its **Burgers vector** $\mathbf b$, the closure failure of a circuit drawn around it in the crystal compared with the same circuit in a perfect crystal.
- In an **edge** dislocation $\mathbf b\perp\boldsymbol\xi$; in a **screw** dislocation $\mathbf b\parallel\boldsymbol\xi$; in general a dislocation is **mixed**, and its character changes along a curved line while $\mathbf b$ stays constant.
- A dislocation cannot end inside a crystal: it ends at a surface or grain boundary, forms a closed loop, or meets other dislocations at a **node**, where the Burgers vectors are conserved ($\sum\mathbf b_i=0$ for lines all pointing into the node).
- The plane containing both $\mathbf b$ and $\boldsymbol\xi$ is the **slip plane**. An edge dislocation has a unique slip plane; a screw dislocation, whose $\mathbf b$ and $\boldsymbol\xi$ are parallel, can glide on any plane containing its line.
- A **perfect** dislocation has a Burgers vector equal to a lattice translation and leaves a perfect crystal behind it. A **partial** dislocation has a smaller Burgers vector and leaves a stacking fault (Section 12.7).

**Table 12.1 — Burgers vectors and slip systems of common structures.**

| Structure | Burgers vector | $\lvert\mathbf b\rvert$ | Usual slip plane | Examples ($\lvert\mathbf b\rvert$ in nm) |
|---|---|---|---|---|
| FCC | $\tfrac a2\langle110\rangle$ | $a/\sqrt2$ | $\{111\}$ | Cu 0.256, Al 0.286, Ni 0.249, austenite ~0.25 |
| BCC | $\tfrac a2\langle111\rangle$ | $a\sqrt3/2$ | $\{110\}$, $\{112\}$, $\{123\}$ | Fe 0.248, W 0.274, Nb 0.286 |
| HCP | $\tfrac a3\langle11\bar20\rangle$ ($\langle a\rangle$) | $a$ | $(0001)$, $\{10\bar10\}$, $\{10\bar11\}$ | Mg 0.321, Ti 0.295, Zn 0.266 |
| HCP | $\tfrac13\langle11\bar23\rangle$ ($\langle c+a\rangle$) | $\sqrt{a^2+c^2}$ | Pyramidal $\{11\bar22\}$, $\{10\bar11\}$ | Mg 0.61, Ti 0.55 |
| Rock salt | $\tfrac a2\langle110\rangle$ | $a/\sqrt2$ | $\{110\}$ | NaCl 0.399, MgO 0.298 |
| Diamond cubic | $\tfrac a2\langle110\rangle$ | $a/\sqrt2$ | $\{111\}$ | Si 0.384, Ge 0.400 |
| Corundum | $\tfrac13\langle11\bar20\rangle$ | $a$ | $(0001)$ (high temperature) | Al₂O₃ 0.476 |

---

## 12.3 Stress fields, line energy and line tension

### The screw dislocation

The elastic field of a straight dislocation in an infinite isotropic solid can be found exactly outside a small **core** region of radius $r_0\approx b$ to $4b$, where strains are too large for linear elasticity. The screw dislocation is simplest. Cut a cylinder along a radial plane, displace one face of the cut parallel to the axis by $b$ and reglue it. The displacement $u_z=b\theta/2\pi$ produces pure shear, with the only non-zero stress component

$$
\tau_{\theta z}=\frac{Gb}{2\pi r}
$$

There is no hydrostatic stress: a screw dislocation changes shape but not volume, so it interacts only weakly with solute atoms that simply dilate the lattice.

### The edge dislocation

For an edge dislocation along $z$ with $\mathbf b$ along $x$ and slip plane $y=0$, the stresses in Cartesian coordinates are

$$
\sigma_{xx}=-D\,\frac{y(3x^2+y^2)}{(x^2+y^2)^2},\qquad
\sigma_{yy}=D\,\frac{y(x^2-y^2)}{(x^2+y^2)^2},\qquad
\sigma_{xy}=D\,\frac{x(x^2-y^2)}{(x^2+y^2)^2}
$$

with $\sigma_{zz}=\nu(\sigma_{xx}+\sigma_{yy})$ and

$$
D=\frac{Gb}{2\pi(1-\nu)}
$$

The edge dislocation has both shear and normal stresses (Figure 12.2). The mean (hydrostatic) stress is

$$
\sigma_m=\tfrac13\sigma_{kk}=-\frac23(1+\nu)\,D\,\frac{y}{x^2+y^2}
$$

compressive above the slip plane ($y>0$), where the extra half-plane is squeezed in, and tensile below it. Large solute atoms are therefore attracted to the tensile side and small ones to the compressive side, forming **Cottrell atmospheres** that pin dislocations — the origin of the yield point and strain ageing of low-carbon steels (Chapter 13).

> **Status of the principle: Elastic fields of straight dislocations**
> *Derived.* Exact solutions of isotropic linear elasticity for an infinite straight line, valid outside the core ($r\gtrsim b$); anisotropic elasticity changes the angular form, and the $1/r$ decay is modified near free surfaces and by neighbouring dislocations.

All components fall as $1/r$, so the field is long-ranged. In copper ($G=48$ GPa, $b=0.256$ nm, $\nu=0.34$), the shear stress on the slip plane 10 nm from an edge dislocation is about $D/r=Gb/[2\pi(1-\nu)r]=296$ MPa — far above the yield strength of annealed copper. Neighbouring dislocations therefore interact strongly even when tens of nanometres apart.

<!-- FIGURE 12.2 | figures/ch12/fig-12-2-edge-stress-field.png | plot | Stress field of an edge dislocation: contour maps of σxx, σxy and the hydrostatic stress around a dislocation at the origin. | Content: Three square panels, x and y from −5 to +5 nm, dislocation symbol ⊥ at origin with b along +x, slip plane y = 0 drawn dashed. Filled contours normalized by D = Gb/(2π(1−ν)) with diverging colour map (blue compressive/negative, red tensile/positive), colour bar ±0.5 D/nm, core r < 0.5 nm masked. Panel (a) σxx: two-lobed, compressive above, tensile below. Panel (b) σxy: four-lobed pattern with zero along x = ±y and x = 0. Panel (c) hydrostatic stress σm: compressive half-space above slip plane, tensile below, labelled "large solutes attracted here" below and "small solutes / vacancies attracted here" above. -->

### Line energy

The elastic energy stored per unit length of dislocation is found by integrating the strain-energy density from the core radius $r_0$ to an outer cut-off $R$:

$$
E_{\text{screw}}=\frac{Gb^2}{4\pi}\ln\frac R{r_0},\qquad E_{\text{edge}}=\frac{Gb^2}{4\pi(1-\nu)}\ln\frac R{r_0}
$$

The logarithm diverges for an isolated dislocation in an infinite body; in a real crystal $R$ is set by the distance to neighbouring dislocations of opposite sign, typically $\rho^{-1/2}$, or by the grain size. The core adds a further energy of about $Gb^2/10$. Because the logarithm varies slowly, a convenient approximation for the total line energy is

$$
E_L\approx\alpha\,Gb^2,\qquad \alpha\approx0.5\text{–}1
$$

> **Status of the principle: Line energy $E_L\approx\alpha Gb^2$**
> *Approximate.* Follows from integrating the elastic field with physically chosen cut-offs; the numerical factor depends on character, cut-off radii and core structure, but the proportionality to $Gb^2$ is robust.

**Worked example — The energy of a dislocation in copper.** Take $G=48$ GPa, $b=0.2556$ nm, $\nu=0.34$, $r_0=b$ and $R=1$ μm (the spacing at a density near $10^{12}$ m⁻²). Then $\ln(R/r_0)=\ln(3912)=8.27$ and

$$
E_{\text{screw}}=\frac{48\times10^9\times(0.2556\times10^{-9})^2}{4\pi}\times8.27=2.1\times10^{-9}\ \mathrm{J/m},\qquad E_{\text{edge}}=\frac{2.1\times10^{-9}}{0.66}=3.1\times10^{-9}\ \mathrm{J/m}
$$

The approximation $\tfrac12Gb^2=1.57\times10^{-9}$ J/m is within a factor of two. Expressed per atomic length $b$ of line, $\tfrac12Gb^2\times b=4.0\times10^{-19}$ J $=2.5$ eV.

Three consequences follow from these numbers. First, dislocations are **not equilibrium defects**: a few electron-volts per atom length of line is far more than the configurational entropy gained ($k_BT\ln(\text{few})$, a fraction of 0.1 eV at room temperature per site), so unlike vacancies, dislocations raise the free energy and are present only because of the crystal's growth and deformation history. Second, since $E\propto b^2$, dislocations with the **shortest Burgers vectors** are favoured: this is why slip in metals occurs along close-packed directions, and why a dislocation with Burgers vector $\mathbf b_1$ tends to dissociate into $\mathbf b_2+\mathbf b_3$ if $b_2^2+b_3^2<b_1^2$ (**Frank's rule**, used in Section 12.7). Third, the stored energy of a cold-worked metal, $\sim\tfrac12\rho Gb^2$, is about 1.6 MJ/m³ at $\rho=10^{15}$ m⁻² in copper — the driving force for recovery and recrystallization calculated in Chapter 10.

### Line tension

Because energy is proportional to length, a curved dislocation behaves like a stretched string with **line tension** $T\approx E_L\approx\tfrac12Gb^2$. To hold a dislocation segment curved to radius $R$ against this tension, a shear stress $\tau$ on its slip plane must supply a force $\tau b$ per unit length, so

$$
\tau=\frac{T}{bR}\approx\frac{Gb}{2R}
$$

> **Status of the principle: Line-tension approximation**
> *Approximate.* Treats the dislocation as a string of constant tension, ignoring the long-range interaction between different parts of a curved line and the dependence of energy on character; it captures the scaling of bowing, source and bypass stresses to within a factor of about two.

This simple relation underlies the stress needed to bow a dislocation between pinning points: a dislocation pinned at points $L$ apart can bow out no further than a semicircle of radius $L/2$, which requires $\tau\approx Gb/L$. It is the basis of the Frank–Read source (Section 12.6) and of the Orowan stress for bypassing precipitates (Chapter 13).

---

## 12.4 Forces on dislocations: glide and climb

### The Peach–Koehler equation

A dislocation moves because the applied stress does work when it moves. If a segment of length $l$ glides a distance $s$, the crystal above the swept area $ls$ is displaced by $\mathbf b$ relative to that below; the work done by the shear stress $\tau$ on the slip plane in the direction of $\mathbf b$ is $\tau b\,ls$. The **force per unit length** on the dislocation is therefore $\tau b$, acting perpendicular to the line in the slip plane. For an arbitrary stress tensor, Peach and Koehler (1950) showed that the force per unit length is

$$
\mathbf F=(\boldsymbol\sigma\cdot\mathbf b)\times\boldsymbol\xi
$$

> **Status of the principle: Peach–Koehler force**
> *Derived.* Follows from the work done by a stress field on a moving dislocation in linear elasticity; it gives both the glide and climb components and applies to applied, internal and image stresses alike.

The component of $\mathbf F$ in the slip plane is the **glide force** $\tau_{\text{rss}}\,b$, where $\tau_{\text{rss}}$ is the shear stress resolved on the slip plane in the direction of $\mathbf b$ (Schmid's law, Chapter 13). For a resolved shear stress of 10 MPa in copper the glide force is $10^7\times2.556\times10^{-10}=2.6\times10^{-3}$ N/m. The component perpendicular to the slip plane, which exists only for edge character, is the **climb force**, produced by normal stress along $\mathbf b$: for an edge dislocation, a compressive $\sigma_{xx}$ pushes the extra half-plane to shrink (climb up) and a tensile one to grow (climb down).

### Glide

**Glide** (slip) is motion in the slip plane. It is **conservative**: atoms only rearrange locally and no mass transport is required, so glide can occur at any temperature at which the applied stress overcomes the lattice resistance and obstacles. The relation between dislocation motion and macroscopic strain is the **Orowan equation**

$$
\dot\gamma=\rho_m\,b\,\bar v
$$

where $\rho_m$ is the density of mobile dislocations and $\bar v$ their average velocity. A strain rate of $10^{-3}$ s⁻¹ in a copper crystal with $\rho_m=10^{12}$ m⁻² requires an average velocity of only $10^{-3}/(10^{12}\times2.556\times10^{-10})=3.9$ μm/s, though in practice dislocations move in jerks between obstacles at much higher local speeds. Velocities rise steeply with stress, often as $v\propto\tau^m$ with $m$ from 2–5 in FCC metals to 20–40 in some BCC metals and ionic crystals, and are limited at very high stress by phonon drag and ultimately by the shear-wave speed.

> **Status of the principle: Orowan equation**
> *Derived.* A kinematic identity relating plastic strain rate to the flux of Burgers vector; it holds whatever controls dislocation velocity, provided the mobile density and average velocity are defined consistently.

### Cross-slip

A screw dislocation has no unique slip plane and can switch from one glide plane to another that contains its Burgers vector. This **cross-slip** lets screw dislocations bypass obstacles, annihilate with screws of opposite sign on nearby planes, and spread slip out of a single plane. In FCC metals the planes are two $\{111\}$ planes sharing a $\langle110\rangle$ direction; how easily cross-slip occurs depends strongly on the stacking-fault energy (Section 12.7). **Double cross-slip** — out of the primary plane and back onto a parallel one — is also a source of new dislocations (Section 12.6).

### Climb

An edge dislocation can move out of its slip plane only by adding or removing atoms at the edge of its extra half-plane: absorbing vacancies makes it climb up, emitting vacancies (or absorbing interstitials) makes it climb down. **Climb** is therefore **non-conservative** and requires diffusion. It is negligible at low temperature but becomes important above about $0.3$–$0.4\,T_m$, where it lets dislocations climb over obstacles they cannot cut or bypass by glide, and lets them rearrange into low-energy walls. Climb is the rate-controlling step in **recovery** (Chapter 10) and in **dislocation creep** of metals at high temperature (Chapter 14), which is why creep rates have activation energies close to that of self-diffusion.

The climb force can come from an applied normal stress or from a non-equilibrium vacancy concentration: a supersaturation $c/c_0$ produces an **osmotic** (chemical) force of $(kT/\Omega)\,b\ln(c/c_0)$ per unit length, where $\Omega$ is the atomic volume. Quenched-in vacancies, or those produced by irradiation, therefore drive climb and form prismatic loops — an important source of swelling and hardening in reactor materials (Chapter 33).

### Image forces

Near a free surface, a dislocation is attracted towards it, because its strain energy can be reduced by relaxing the stresses at the surface. The **image force** is that of an imaginary dislocation of opposite sign mirrored across the surface, about $Gb^2/[4\pi(1-\nu)\lambda]$ for an edge dislocation at distance $\lambda$. Near a stiffer layer, such as an oxide film or a hard coating, the force is repulsive. Image forces pull dislocations out of thin films and nanopillars, contributing to their "dislocation starvation" and high strength.

---

## 12.5 Interactions: junctions, jogs, kinks and forest hardening

### Interactions between parallel dislocations

Two parallel dislocations interact through their stress fields; the force on one is given by the Peach–Koehler equation using the stress of the other. Two parallel screws with the same Burgers vector repel with force $Gb^2/(2\pi r)$ per unit length; screws of opposite sign attract. For edge dislocations on parallel slip planes a distance $y$ apart, the glide force on one from the other is

$$
F_x=\frac{Gb^2}{2\pi(1-\nu)}\,\frac{x(x^2-y^2)}{(x^2+y^2)^2}
$$

For like-signed edges, $F_x$ vanishes and is stable at $x=0$: they line up one above another, forming a **tilt wall** — a low-angle grain boundary with misorientation $\theta\approx b/h$ for spacing $h$. This is **polygonization**, the basic process of recovery (Chapter 10). For opposite-signed edges the stable position is at $x=\pm y$, forming a **dipole**. Walls and dipoles screen each other's long-range stresses, which is why dislocations in deformed metals arrange themselves into **cells** with tangled walls and relatively clean interiors at strains above a few percent.

### Junctions and locks

When two dislocations gliding on intersecting planes meet, they may react to form a third segment along the line of intersection, provided this lowers the energy by Frank's rule. In FCC metals the most important are the **Lomer** and **Lomer–Cottrell locks**, formed when dislocations on two $\{111\}$ planes combine to give a segment with Burgers vector $\tfrac a2\langle110\rangle$ lying on neither glide plane — or, after dissociation, a sessile configuration with a stair-rod partial at the apex. Such junctions cannot glide and become strong obstacles that anchor the dislocations that formed them. **Glissile junctions** and **Hirth locks** are other products. Dislocation-dynamics simulations (Chapter 46) show that the strength of these junctions, more than the elastic interaction of distant dislocations, sets the forest-hardening stress.

### Jogs and kinks

When two dislocations cut through each other, each acquires a step equal to the other's Burgers vector. A step that lies **in** the slip plane of the dislocation is a **kink**; it can glide with the line and is readily removed. A step that takes the dislocation **out** of its slip plane is a **jog**. A jog on an edge dislocation lies in a plane that contains $\mathbf b$, so it can usually glide along with the line. A jog on a **screw** dislocation has edge character with a slip plane perpendicular to the screw's motion, so it can follow only by climb — producing vacancies or interstitials as it is dragged. Such **jog drag** helps explain why screw dislocations move more slowly than edges in many metals, and the point defects produced during deformation accelerate diffusion in cold-worked material.

Each jog costs energy, about $Gb^3/10$ (roughly 0.5 eV in copper), so cutting through a "forest" of dislocations threading the slip plane requires work. Together with the junction reactions, this is the origin of the major part of work hardening.

### Forest hardening: the Taylor equation

A dislocation gliding on its slip plane is obstructed by the other dislocations that thread that plane, the **forest**, with average spacing $l\approx\rho^{-1/2}$. To pass between them, it must bow out and form junctions or jogs; using the line-tension result $\tau\approx Gb/l$ and lumping the details into a constant gives the **Taylor equation**

$$
\tau=\alpha\,G\,b\,\sqrt\rho
$$

with $\alpha$ typically 0.2–0.5. In a polycrystal the tensile flow stress is $\sigma=M\tau$, with the Taylor factor $M\approx3.06$ for FCC metals (Chapter 13).

> **Status of the principle: Taylor forest-hardening equation**
> *Approximate.* Derived from the line tension and the mean spacing of forest obstacles, with $\alpha$ fitted to experiment or obtained from dislocation-dynamics simulations; the $\sqrt\rho$ dependence is confirmed over five orders of magnitude of density in FCC metals.

**Worked example — Work hardening of copper from dislocation density.** Take $\alpha=0.3$, $G=48$ GPa, $b=0.2556$ nm and $M=3.06$. Then $\alpha Gb=3.68$ N/m, and:

**Table 12.2 — Forest hardening in copper from the Taylor equation.**

| Condition | $\rho$ (m⁻²) | Spacing $\rho^{-1/2}$ | $\tau=\alpha Gb\sqrt\rho$ (MPa) | $\sigma=M\tau$ (MPa) |
|---|---|---|---|---|
| Well-annealed single crystal | $10^{10}$ | 10 μm | 0.37 | 1.1 |
| Annealed polycrystal | $10^{12}$ | 1 μm | 3.7 | 11 |
| Lightly cold-worked (~10 %) | $10^{14}$ | 100 nm | 37 | 113 |
| Heavily cold-drawn wire | $10^{15}$ | 32 nm | 116 | 356 |
| Severe plastic deformation | $10^{16}$ | 10 nm | 368 | 1130 |

The fourth row reproduces the 300–400 MPa yield strength of hard-drawn copper wire. The first two rows show that the forest contribution is negligible in annealed material, whose yield strength of 40–70 MPa comes mainly from grain boundaries and impurities; the last shows why severely deformed metals reach gigapascal strengths, until grain-boundary effects and dynamic recovery limit further increases. Figure 12.3 compares the relation with measurements.

<!-- FIGURE 12.3 | figures/ch12/fig-12-3-taylor-hardening.png | plot | Flow stress versus square root of dislocation density for FCC metals, showing the Taylor relation. | Content: x-axis √ρ from 0 to 1.2 × 10^8 m⁻¹ (i.e. ρ up to 1.44 × 10^16 m⁻²), with a secondary top axis labelled ρ at 10^12, 10^14, 10^15, 10^16 m⁻². y-axis tensile flow stress 0–1200 MPa. Solid line for Cu: σ = 3.06 × 0.3 × 48 GPa × 0.2556 nm × √ρ (passes through 356 MPa at √ρ = 3.16 × 10^7 and 1126 MPa at 10^8). Dashed lines for Al (G = 26 GPa, b = 0.286 nm) and Ni (G = 76 GPa, b = 0.249 nm), same α and M. Scattered illustrative points (open circles) clustered around the Cu line labelled "TEM and XRD measurements (schematic)". Shaded vertical band at ρ = 10^14–10^15 labelled "cold-worked sheet and wire". -->

---

## 12.6 Multiplication: Frank–Read and other sources

### Why multiplication is needed

An annealed metal contains perhaps $10^{10}$–$10^{12}$ m of dislocation line per cubic metre. If each dislocation simply glided out of the crystal, producing a step of $b$, the total available plastic strain would be tiny — of order $\rho bL$ for dislocations travelling a distance $L$, about $10^{12}\times2.6\times10^{-10}\times10^{-4}\approx0.03$ for $L=100$ μm, and the initial dislocations would soon be exhausted. Yet metals can be deformed to strains of 1 or more, and their dislocation density *rises* to $10^{15}$–$10^{16}$ m⁻². Dislocations must therefore multiply during deformation.

### The Frank–Read source

Frank and Read (1950) proposed the classic mechanism (Figure 12.4). A dislocation segment of length $L$ is pinned at both ends — by nodes of the network, by precipitates or by points where the line leaves the slip plane. Under a resolved shear stress, it bows out. Its radius of curvature decreases as the stress rises, until it becomes a semicircle of radius $L/2$; this configuration requires the maximum stress,

$$
\tau_{\text{FR}}\approx\frac{Gb}{L}
$$

Beyond it the loop becomes unstable and expands at decreasing stress, wrapping around the pinning points. The two parts of the loop that meet behind the pinning points have opposite character and annihilate, leaving a complete loop that expands outward and a regenerated segment between the pins, which starts the process again. A single source can emit hundreds of loops, each contributing one Burgers vector of slip, until the back stress of the piled-up loops (at a grain boundary, for example) stops it.

> **Status of the principle: Frank–Read source stress**
> *Approximate.* From the line-tension approximation; more exact calculations with the full self-interaction of the bowing line give $\tau\approx(Gb/2\pi L)\ln(L/r_0)$ for the critical stress, within a factor of about two of $Gb/L$ for typical $L$.

For copper with $L=1$ μm, $\tau_{\text{FR}}\approx48\times10^9\times2.556\times10^{-10}/10^{-6}=12$ MPa; for $L=10$ μm, 1.2 MPa; for $L=0.1$ μm, 120 MPa. Long segments operate first; as deformation proceeds and the forest densifies, the free segment lengths shorten, and higher stresses are needed — another way of seeing work hardening. Frank–Read sources were first observed directly as spiral etch figures and as concentric loops decorated with copper in silicon (Dash, 1956).

<!-- FIGURE 12.4 | figures/ch12/fig-12-4-frank-read-source.png | schematic | Operation of a Frank–Read source: successive configurations of a pinned dislocation segment under increasing shear stress, ending in an emitted loop and a regenerated segment. | Content: Five panels in a row on the slip plane, pinning points A and B (filled black dots) a distance L apart. (1) straight segment AB, shear stress τ arrow and Burgers vector b arrow; (2) bowed arc, radius R > L/2; (3) semicircle, radius L/2, labelled "maximum stress τ ≈ Gb/L"; (4) unstable expansion wrapping around A and B, the two back segments approaching each other, with screw and edge character labelled at different points and arrows showing the meeting point P; (5) complete expanding loop plus new straight segment AB, labelled "cycle repeats". Use one colour for the line, light grey for previous positions. -->

### Other sources

- **Double cross-slip.** A screw segment cross-slips onto a parallel primary plane; the two short segments on the cross-slip plane act as pinning points for a new Frank–Read-type source. This mechanism, observed in LiF by Johnston and Gilman, accounts for the rapid multiplication and broad slip bands in materials with easy cross-slip.
- **Bardeen–Herring climb sources.** An edge segment pinned at both ends and exposed to a vacancy supersaturation climbs into a spiral or concentric prismatic loops, the climb analogue of a Frank–Read source. It operates during quenching and in irradiated metals.
- **Grain boundaries and interfaces.** Boundary ledges, triple junctions and particle–matrix interfaces with thermal-expansion mismatch emit dislocations, the dominant sources in fine-grained and nanocrystalline metals and around reinforcing particles in metal-matrix composites (Chapter 23).
- **Surfaces and stress concentrations.** Scratches, edge chips and crack tips nucleate dislocations where local stresses approach the theoretical strength. In dislocation-free silicon this is the only route to slip; wafer handling therefore minimizes edge damage and contact stresses, and furnace ramps are limited to keep thermal stresses below the threshold for slip from the edge.
- **Homogeneous nucleation**, at stresses near $G/30$, occurs only in defect-free volumes — under a nanoindenter, in whiskers and in nanopillars — where it produces "pop-in" events in the load–displacement curve.

---

## 12.7 Partial dislocations, stacking faults and stacking-fault energy

### Dissociation in FCC metals

In an FCC crystal the $\{111\}$ planes are stacked in the sequence ABCABC. A perfect dislocation with $\mathbf b=\tfrac a2[\bar101]$ on $(111)$ moves an atom in a B position over to the next B position — a path that climbs over an A atom. The easier path goes via the "valley" through a C position, in two steps. This corresponds to splitting the perfect dislocation into two **Shockley partial dislocations**:

$$
\tfrac a2[\bar101]\;\rightarrow\;\tfrac a6[\bar211]+\tfrac a6[\bar1\bar12]
$$

Each partial has $\lvert\mathbf b_p\rvert=a/\sqrt6$. By Frank's rule the dissociation is favourable: $b^2=a^2/2$ before and $2\times a^2/6=a^2/3$ after. Between the two partials the stacking sequence is changed: the region swept by the leading partial alone becomes ABCA**C**ABC — an **intrinsic stacking fault**, a thin layer of HCP-like stacking — which has an energy per unit area $\gamma_{\text{SF}}$, the **stacking-fault energy** (SFE) (Figure 12.5). The partials repel each other elastically, and the fault pulls them together; they settle at an equilibrium separation that, in the isotropic approximation and averaging over character,

$$
d\approx\frac{Gb_p^2}{2\pi\gamma_{\text{SF}}}
$$

> **Status of the principle: Equilibrium width of a dissociated dislocation**
> *Approximate.* A balance between the isotropic elastic repulsion of two parallel partials and the fault tension; the exact width also depends on character (screws are about two to three times narrower than edges), on elastic anisotropy and on the applied stress, which can widen or constrict the ribbon.

<!-- FIGURE 12.5 | figures/ch12/fig-12-5-partials-stacking-fault.png | schematic | Dissociation of a perfect FCC dislocation into two Shockley partials bounding an intrinsic stacking fault. | Content: Left: plan view of a close-packed (111) layer of A atoms (large circles) with B and C sites marked; vector b = a/2[-101] from one B site to the next, and the two partial vectors a/6[-211] and a/6[-1-12] via the C site, forming a triangle (Frank's rule annotation b² = a²/2 > 2 × a²/6). Right: side view (cross-section) of the dissociated dislocation: leading and trailing partials (⊥ symbols) separated by width d, stacking sequence above and below annotated ABCABC outside the ribbon and ABCACABC within, fault region shaded. Inset table: d ≈ 0.7 nm (Al), 2 nm (Ni), 3.7 nm (Cu), 13 nm (austenitic stainless steel). -->

**Worked example — Partial separations in FCC metals.** For copper, $a=0.3615$ nm, so $b_p=a/\sqrt6=0.1476$ nm; $G=48$ GPa and $\gamma_{\text{SF}}=45$ mJ/m². Then

$$
d\approx\frac{48\times10^9\times(0.1476\times10^{-9})^2}{2\pi\times0.045}=\frac{1.046}{0.283}\times10^{-9}\ \mathrm m=3.7\ \mathrm{nm}
$$

about 14 perfect Burgers vectors. Repeating the calculation:

**Table 12.3 — Stacking-fault energies and dissociation widths of FCC metals (typical).**

| Metal | $\gamma_{\text{SF}}$ (mJ/m²) | $G$ (GPa) | $d$ (nm) | $d/b$ | Typical behaviour |
|---|---|---|---|---|---|
| Aluminium | 160–200 (166 used) | 26 | 0.7 | 2.4 | Easy cross-slip, wavy slip, extensive recovery, cells |
| Nickel | 120–130 | 76 | 2.0 | 8 | Cross-slip, cells |
| Copper | 40–50 | 48 | 3.7 | 14 | Intermediate; annealing twins |
| Silver | 16–22 | 30 | 8.3 | 29 | Planar slip, many annealing twins |
| Austenitic stainless steel (316) | ~20 | 77 | 13 | 52 | Planar slip, deformation twins or ε-martensite |
| Brass Cu–30Zn | 7–14 (7 used) | ~37 | ~19 | ~70 | Very planar slip, high work hardening |

### Why stacking-fault energy matters

A dissociated screw dislocation cannot cross-slip as two separate partials, because the partials' Burgers vectors are not in the cross-slip plane. The ribbon must first **constrict** to a perfect screw over a short length, which costs energy that rises with the dissociation width. Stacking-fault energy therefore controls a whole family of behaviours:

- **Cross-slip and recovery.** High-SFE metals (Al, Ni, ferritic iron) cross-slip easily, form well-defined cell structures and recover readily on annealing; low-SFE metals (Ag, brass, austenitic steels) show planar slip, tangled arrays, and recrystallize rather than recover (Chapter 10).
- **Work hardening.** Planar slip keeps dislocations confined to their planes, where they pile up and interact; low-SFE alloys therefore work-harden faster and to higher stresses, with higher strain-hardening exponents $n$. This is why brass and austenitic stainless steels are favoured for deep drawing.
- **Twinning and phase transformation.** At SFE below about 20 mJ/m², partials separate so widely that deformation twinning or the formation of HCP ε-martensite competes with slip. **TWIP** (twinning-induced plasticity) steels, Fe–(15–25)Mn–C alloys with SFE of 20–40 mJ/m², and **TRIP** steels with lower SFE exploit this to combine strengths of 800–1000 MPa with elongations of 50–60 % for automotive crash structures (Chapter 15).
- **Annealing twins** are abundant in low-SFE metals (copper, brass, austenitic steel) and rare in aluminium.
- **Environmental cracking.** Planar slip concentrates deformation in narrow bands that rupture protective films, one reason austenitic stainless steels are susceptible to chloride stress-corrosion cracking (Chapter 35).

Solute additions change the SFE: zinc and aluminium lower it in copper, nickel raises it in iron–manganese steels, which is how alloy designers select the deformation mode.

### Other partials and faults

A **Frank partial**, $\mathbf b=\tfrac a3\langle111\rangle$, bounds a stacking fault formed by inserting or removing part of a close-packed layer — for example, when a disc of condensed vacancies collapses after quenching or irradiation. Its Burgers vector is normal to the fault plane, so it is **sessile** and can move only by climb. Frank loops are a principal irradiation defect in austenitic steels used in reactor cores (Chapter 33). At the intersection of two faults on different $\{111\}$ planes, short **stair-rod** partials such as $\tfrac a6\langle110\rangle$ form, as in the Lomer–Cottrell lock. The **Thompson tetrahedron** is the standard bookkeeping device for all these Burgers vectors in FCC crystals.

---

## 12.8 Dislocations in FCC, BCC, HCP and ceramic crystals

### The Peierls stress

A dislocation moving through a perfect lattice still experiences a periodic resistance, because its core energy varies as it passes from one lattice valley to the next. The stress needed to overcome this lattice friction at 0 K is the **Peierls (Peierls–Nabarro) stress**. The classical estimate for a dislocation of core width $w$ is

$$
\tau_P\approx\frac{2G}{1-\nu}\exp\!\left(-\frac{2\pi w}{b}\right)
$$

with $w\approx d/(1-\nu)$ for an edge dislocation on planes spaced $d$ apart.

> **Status of the principle: Peierls–Nabarro stress**
> *Approximate.* From a continuum model of the core with a sinusoidal interplanar force; it correctly predicts that wide cores on widely spaced, close-packed planes have negligible lattice friction and narrow, compact cores have large friction, but absolute values can be wrong by orders of magnitude, and non-planar cores (as in BCC screws) need atomistic calculation.

The exponential is the essential feature. With $\nu=0.3$, a core of width $w=0.5b$ gives $\tau_P\approx0.12G$; $w=b$ gives $5\times10^{-3}G$; $w=1.5b$ gives $2.3\times10^{-4}G$. A change of core width by a factor of three changes the lattice friction by a factor of about 500. Wide cores and widely spaced slip planes — both features of close-packed metals — mean low friction; narrow, directional, covalent cores mean high friction. This explains the differences among structures.

### FCC metals

In FCC metals, slip on the widely spaced $\{111\}$ planes by dissociated dislocations with planar cores meets very little lattice resistance: Peierls stresses are of order $10^{-5}G$ or less, well below 1 MPa. The critical resolved shear stress of a pure FCC crystal is therefore set by other dislocations and impurities, and depends only weakly on temperature and strain rate. FCC metals stay ductile down to liquid-helium temperatures and show no ductile–brittle transition — the basis of their use in cryogenic tanks and LNG carriers (Chapter 33).

### BCC metals

BCC metals have no truly close-packed plane. Their $\tfrac a2\langle111\rangle$ screw dislocations have a compact, **non-planar core** spread over three $\{110\}$ planes of the $\langle111\rangle$ zone, and must transform the core to glide. The result is a high Peierls stress (of order $10^{-2}G$ at 0 K) and a strongly temperature-dependent flow stress. At low temperature, screws move by thermally activated nucleation of **kink pairs** — short segments that jump into the next valley and then spread sideways — so the flow stress rises steeply on cooling (Figure 12.6) below about $0.15$–$0.2\,T_m$, which for iron is around room temperature. Edge dislocations, by contrast, are mobile, so plasticity in BCC metals at low temperature is controlled by long, straight, slow screws. Slip in BCC metals occurs on $\{110\}$, $\{112\}$ and $\{123\}$ planes sharing the $\langle111\rangle$ direction, producing wavy "pencil glide" traces, and the screw-core structure causes the yield stress to depend on the sense of shear (twinning–antitwinning asymmetry) and to violate Schmid's law.

The steep rise of flow stress on cooling is the physical root of the **ductile–brittle transition** of ferritic steels and refractory metals (Chapters 11 and 14): at low temperature the stress needed to move dislocations and blunt a crack tip exceeds the stress needed for cleavage. Tungsten, molybdenum and chromium have transition temperatures above room temperature unless very pure and fine-grained, which is why tungsten plasma-facing components in fusion reactors must be operated hot.

<!-- FIGURE 12.6 | figures/ch12/fig-12-6-crss-temperature.png | plot | Temperature dependence of the critical resolved shear stress of FCC, BCC and HCP single crystals, normalized by shear modulus. | Content: x-axis homologous temperature T/Tm from 0 to 0.5; y-axis τc/G on log scale from 1e-6 to 1e-2. Curves: FCC (Cu, Al) nearly flat at ~1e-5, slight decrease with T; BCC (Fe, Nb, W) steep fall from ~5e-3 at T/Tm = 0 to ~1e-4 at the "knee" T/Tm ≈ 0.15–0.2, then flat athermal plateau; HCP Mg basal slip flat at ~1e-5 and Mg prismatic/pyramidal ⟨c+a⟩ slip falling from ~5e-3 to ~3e-4 by T/Tm = 0.5 (dashed); ceramic NaCl/MgO band at 1e-4 to 1e-3, and Al2O3 basal slip ~1e-2 falling to ~1e-3 near T/Tm = 0.5 (dotted). Annotate "Peierls-controlled (thermally activated)" over the BCC low-temperature region and "athermal (forest, solutes)" over plateaus; marker at room temperature for Fe (T/Tm ≈ 0.16). -->

### HCP metals

In HCP metals the $\langle a\rangle$ Burgers vector $\tfrac a3\langle11\bar20\rangle$ is the shortest, and the easiest slip plane depends on the axial ratio $c/a$ (ideal value 1.633) and on the electronic structure. Magnesium ($c/a=1.624$), zinc (1.856) and cadmium (1.886) slip mainly on the basal plane; titanium (1.587) and zirconium (1.593) slip mainly on prismatic $\{10\bar10\}$ planes. In either case, $\langle a\rangle$ slip cannot produce strain along the $c$ axis. That requires either pyramidal slip of $\langle c+a\rangle$ dislocations, whose Burgers vector is about twice as long and whose critical stress at room temperature is typically 10–100 times that for basal slip in magnesium, or deformation **twinning**.

The consequences are large. HCP polycrystals lack five independent easy slip systems (the von Mises requirement developed in Chapter 13), so they show limited ductility, strong anisotropy, tension–compression asymmetry and strong textures after rolling. Magnesium alloy sheet for automotive and aerospace use is difficult to form at room temperature and is usually warm-formed at 200–300 °C, where non-basal slip becomes easier. Titanium alloys are more ductile because prismatic, basal and pyramidal $\langle a\rangle$ slip and twinning together supply enough systems, and their texture is exploited in aerospace forgings and Zircaloy fuel cladding, whose properties along the tube axis and through the wall are tailored by texture.

### Ordered intermetallics

In ordered alloys such as Ni₃Al (γ′), a perfect FCC lattice translation $\tfrac a2\langle110\rangle$ is not a translation of the ordered structure: a single such dislocation leaves an **antiphase boundary** (APB) behind it. Dislocations therefore travel in pairs, as **superdislocations** joined by a ribbon of APB. The need to cut γ′ particles with pairs of dislocations is a major source of strength in nickel superalloys (Chapter 13), and the cross-slip of superdislocation segments onto cube planes, where they become locked (Kear–Wilsdorf locks), gives Ni₃Al the anomalous property of a yield strength that *increases* with temperature up to about 700 °C.

### Ceramics and covalent crystals

In ionic and covalent crystals dislocations exist, but they move with difficulty, for three reasons. **Long Burgers vectors**: the lattice translation must connect ions of the same sign, so $b$ is large (0.399 nm in NaCl; 0.476 nm in Al₂O₃ for the shortest $\tfrac13\langle11\bar20\rangle$ vector), and energy and lattice friction rise with $b$. **Electrostatic constraints**: in rock-salt crystals, slip on $\{110\}\langle1\bar10\rangle$ avoids bringing like ions face to face, but this gives only two independent systems; slip on $\{100\}$, needed for general deformation, is much harder. **Directional bonds**: in covalent solids such as silicon, SiC and diamond, moving a dislocation requires breaking and re-forming directional bonds, giving very high Peierls stresses.

As a result, ceramic single crystals such as MgO and NaCl can deform plastically at room temperature in favourable orientations, but polycrystalline ceramics fracture before enough slip systems activate. Alumina deforms by basal slip only above about 900–1000 °C. Silicon is brittle below about 500–600 °C but deforms plastically at higher temperatures — the slip that ruined the wafers in this chapter's opening, generated by thermal stresses during furnace processing, which is why wafer boats, ramp rates and furnace profiles are designed to keep the resolved shear stress below the threshold at every temperature. In semiconductors, dislocations are also electrically active, introducing levels in the band gap that act as recombination centres; GaN light-emitting diodes are remarkably tolerant of threading dislocation densities of $10^8$–$10^9$ cm⁻² ($10^{12}$–$10^{13}$ m⁻²) that would destroy GaAs devices (Chapter 26). Ceramics are toughened therefore not by encouraging dislocations but by crack bridging and transformation toughening (Chapter 14).

**Table 12.4 — Dislocation behaviour by crystal class.**

| Class | Typical Peierls stress | Temperature dependence of flow stress | Ductility at room temperature | Engineering consequence |
|---|---|---|---|---|
| FCC metals (Cu, Al, Ni, austenite) | $\lesssim10^{-5}G$ | Weak | High, to cryogenic temperature | Cryogenic and formable alloys |
| BCC metals (Fe, W, Mo, Nb) | ~$10^{-2}G$ (screws, 0 K) | Strong below ~0.2 $T_m$ | Good above transition, brittle below | Ductile–brittle transition of ferritic steels |
| HCP metals (Mg, Ti, Zn, Zr) | Low for $\langle a\rangle$ on easy plane; high for $\langle c+a\rangle$ | Strong for hard modes | Limited, anisotropic | Warm forming of Mg; texture control in Ti, Zr |
| Ordered intermetallics (Ni₃Al, TiAl) | Moderate; superdislocations | Anomalous in Ni₃Al | Low in polycrystals | High-temperature strength of γ′; brittleness of TiAl |
| Ionic ceramics (NaCl, MgO) | ~$10^{-3}G$ | Moderate | Single crystals only | Too few independent systems in polycrystals |
| Covalent and ionic–covalent (Si, SiC, Al₂O₃) | ~$10^{-2}$–$10^{-1}G$ | Very strong | Brittle below ~0.5 $T_m$ | Slip only at high temperature; brittle fracture |

---

## 12.9 Observing dislocations

Dislocations were postulated in 1934 and became directly visible only two decades later. Today a range of techniques images them across scales from the atomic core to the whole wafer.

### Etch pits and decoration

Where a dislocation meets a surface, the strained core region dissolves faster in a suitable etchant, leaving a small **etch pit**. Counting pits gives the dislocation density in units of lines per area (cm⁻²), and repeated etching after small amounts of loading tracks individual dislocations — the method Johnston and Gilman used in LiF (1959) to measure dislocation velocity as a function of stress. Etch-pit density (EPD) is still the routine specification of crystal quality for semiconductor substrates: silicon wafers are essentially dislocation-free, GaAs substrates have EPD of $10^2$–$10^4$ cm⁻², and SiC substrates for power devices are graded by their densities of threading and basal-plane dislocations. **Decoration** precipitates atoms along dislocation lines so that they can be seen by optical or infrared microscopy inside transparent crystals (silver halides, copper-decorated silicon).

### Transmission electron microscopy

The **transmission electron microscope** (TEM) made dislocations directly visible in 1956, when Hirsch, Horne and Whelan in Cambridge and Bollmann in Geneva independently observed moving dislocations in thin metal foils. Dislocations are imaged by **diffraction contrast**: the strain field near the line bends the diffracting planes locally, changing the intensity of the diffracted beam, so the line appears as a dark (or bright) band in an image formed with one strong reflection $\mathbf g$. If the diffracting planes are not distorted by the dislocation, there is no contrast; for a screw dislocation, and approximately for an edge, the **invisibility criterion** is

$$
\mathbf g\cdot\mathbf b=0
$$

By finding two reflections for which a dislocation is invisible, its Burgers vector is determined as their cross product. **Weak-beam dark-field** imaging narrows the image of a dislocation to about 1.5 nm, enough to resolve the two partials of a dissociated dislocation and measure stacking-fault energies from their separation. Densities are measured by counting intersections of lines with a test grid: $\rho=2N/(L_t\,t)$ for $N$ intersections with test lines of total length $L_t$ in a foil of thickness $t$. **In-situ** straining and heating stages show sources operating, dislocations cutting precipitates and boundaries migrating (Chapter 44).

**High-resolution TEM and aberration-corrected STEM** image the core itself as an atomic column arrangement, so that a Burgers circuit can be drawn directly around it, and atom-probe tomography (Chapter 43) reveals the solute atmospheres segregated to dislocations.

### X-ray, electron-backscatter and other methods

- **X-ray topography** (Lang, 1958) images individual dislocations over whole wafers and large crystals with micrometre resolution, using the strain contrast in a diffracted X-ray beam; synchrotron topography is used to map slip in silicon wafers and defects in SiC and diamond.
- **X-ray and neutron line broadening** (Chapter 4) gives average dislocation densities in bulk polycrystals from the strain broadening of diffraction peaks — the source of the densities in Table 12.2.
- **Electron backscatter diffraction** (EBSD) maps local lattice misorientation in the SEM. Gradients of misorientation give the density of **geometrically necessary dislocations** required to accommodate lattice curvature, around indents, cracks and grain boundaries; **electron channelling contrast imaging** (ECCI) images near-surface dislocations in bulk samples without thin-foil preparation (Chapter 42).
- **Simulation** complements observation: discrete dislocation dynamics follows millions of dislocation segments with the fields and interactions of this chapter, and atomistic simulation resolves cores, junctions and kink-pair mechanisms (Chapters 45 and 46).

**Table 12.5 — Typical dislocation densities.**

| Material and condition | $\rho$ (m⁻²) | Method usually used |
|---|---|---|
| Float-zone or Czochralski silicon | < $10^{6}$ (essentially dislocation-free) | Etch pits, X-ray topography |
| GaAs substrate | $10^{6}$–$10^{8}$ ($10^2$–$10^4$ cm⁻²) | Etch pits |
| GaN on sapphire (LED epilayers) | $10^{12}$–$10^{13}$ | TEM, cathodoluminescence |
| Well-annealed metal | $10^{10}$–$10^{12}$ | TEM, etch pits |
| Cold-worked metal (moderate) | $10^{14}$–$10^{15}$ | TEM, XRD |
| Heavily cold-drawn wire, martensite | $10^{15}$–$10^{16}$ | XRD line broadening |
| Severely deformed (HPT, ECAP) metals | up to ~$10^{16}$ | XRD, TEM |

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How does the resolved shear stress on slip systems determine yield in single crystals and polycrystals (Schmid's law, Taylor factor, von Mises criterion)? | Chapter 13 |
| How do solutes, grain boundaries and precipitates obstruct dislocations quantitatively (Hall–Petch from pile-ups, cutting versus Orowan bypass)? | Chapter 13 |
| How do twinning and superplasticity provide deformation where slip is insufficient? | Chapter 13 |
| How does climb-controlled dislocation creep differ from diffusional creep, and how is it mapped? | Chapter 14 |
| How does the competition between crack-tip dislocation emission and cleavage set the ductile–brittle transition and fracture toughness? | Chapter 14 |
| How do dislocations rearrange during recovery and recrystallization? | Chapter 10 (back reference) |
| How do TWIP and TRIP steels and nickel superalloys exploit stacking-fault energy and superdislocations? | Chapters 15 and 16 |
| How do irradiation loops and dislocations cause swelling and hardening in reactor materials? | Chapter 33 |
| Why do nanocrystalline metals soften at the smallest grain sizes? | Chapter 30 |
| How are dislocations imaged in practice and measured with uncertainty? | Chapters 42, 43 and 44 |
| How are dislocation ensembles simulated (discrete dislocation dynamics, crystal plasticity)? | Chapter 46 |

**Next:** Chapter 13 scales up from single dislocations to the plasticity of real crystals and polycrystals, deriving Schmid's law, yield criteria and the strengthening mechanisms that let engineers set yield strength over two orders of magnitude.
