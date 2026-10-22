# Chapter 11 — Elasticity and Mechanical Testing

*Part III · Mechanical Behaviour*

In 2007 a steel-truss highway bridge over the Mississippi in Minneapolis collapsed at rush hour. The investigation found that gusset plates at several joints were half the thickness they should have been, a design error that had stood unnoticed for forty years while extra concrete deck and construction equipment added load. Nothing about the steel was wrong: its modulus, yield strength and toughness were what the specification said. What failed was the chain that links those properties to a structure — the calculation of the stress each plate carried and its comparison with what the material could bear. A few years earlier, batches of zirconia femoral heads for hip replacements had been recalled after several fractured in patients; there the stresses had been calculated correctly, but a change in the sintering process had altered the population of flaws, and with it the strength distribution that the design relied upon.

Both cases turn on the vocabulary of this chapter: how stress and strain are described, how a material resists them elastically, and how the numbers that engineers put into calculations — modulus, yield strength, tensile strength, hardness, toughness — are actually measured, and with what scatter.

> **How does a solid respond to small loads, and why do stiffnesses span seven orders of magnitude from rubber to diamond?**
> **What do the standard mechanical tests measure, how should their numbers be interpreted, and why must brittle strength be treated as a statistical quantity?**

| Concept | Engineering destination |
|---|---|
| Stress and strain tensors, principal stresses | Finite-element analysis, pressure vessels, shafts, bone implants |
| Hooke's law, elastic constants | Deflection of beams, bridges and aircraft wings; bolt preload; stiffness design |
| Anisotropic elasticity | Single-crystal turbine blades, silicon MEMS, wood, composite laminates |
| Bonding origin of moduli | Choosing stiff, light materials; porous ceramics and foams |
| Entropic elasticity | Seals, tyres, vibration mounts (developed in Chapter 20) |
| Tensile test, true stress–strain | Specifications, forming limits, crash simulation |
| Hardness and nanoindentation | Quality control of heat treatment, coatings and thin films |
| Impact and toughness tests | Ship plate, pipelines, pressure vessels, cold-climate structures |
| Bend, compression and shear tests | Ceramics, concrete, adhesives, composite laminates |
| Statistics of strength | Ceramic implants, glass panels, design allowables, concrete grades |

**Roadmap.** Describing stress and strain (11.1) → linear elasticity, isotropic and anisotropic (11.2) → why moduli have the values they do (11.3) → entropic elasticity of rubbers (11.4) → the tensile test (11.5) → hardness (11.6) → impact and toughness (11.7) → bend, compression and shear tests (11.8) → strength as a statistical property (11.9).

---

## 11.1 Stress and strain and their tensors

### Traction and the stress tensor

A force applied to a body is transmitted through it from atom to atom. To describe how intensely the material is loaded at a point, imagine cutting the body by a plane through that point with unit normal $\mathbf n$. The force per unit area acting across the cut is the **traction** $\mathbf t$. It depends on the orientation of the cut: a rod in tension carries traction $F/A$ on a cross-section, but none on a plane parallel to its axis. Cauchy showed that the traction on every plane through a point is determined by nine numbers, the components of the **stress tensor** $\sigma_{ij}$:

$$
t_i=\sigma_{ij}\,n_j
$$

(summation over the repeated index). $\sigma_{ij}$ is the $i$ component of force per unit area on a plane whose normal is along $j$. The diagonal terms are **normal stresses** (positive in tension); the off-diagonal terms are **shear stresses**, often written $\tau_{xy}$, $\tau_{yz}$, $\tau_{zx}$. Balance of moments on a small cube shows that the tensor is symmetric, $\sigma_{ij}=\sigma_{ji}$, so six components are independent. Stresses are measured in pascals; engineering values are usually given in MPa (equal to N/mm²).

> **Status of the principle: Cauchy stress tensor**
> *Fundamental.* Follows from force and moment equilibrium of an infinitesimal element of a continuum; it applies to any material, elastic or not, at length scales large compared with the atomic spacing.

<!-- FIGURE 11.1 | figures/ch11/fig-11-1-stress-tensor-mohr.png | schematic | The stress tensor: components acting on the faces of a cubic element, and the Mohr circle for a two-dimensional stress state showing principal stresses and maximum shear. | Content: Left: isometric unit cube with axes x, y, z; on the three visible faces, arrows for σxx, σyy, σzz (normal) and τxy, τxz, τyx, τyz, τzx, τzy (shear), labelled. Right: Mohr circle with horizontal axis normal stress σ (−50 to 150 MPa) and vertical axis shear stress τ; example state σxx = 120 MPa, σyy = 20 MPa, τxy = 40 MPa; centre at 70 MPa, radius 64 MPa; principal stresses σ1 = 134 MPa and σ2 = 6 MPa marked; maximum in-plane shear 64 MPa marked; angle 2θp = 38.7° shown. -->

### Principal stresses, hydrostatic and deviatoric parts

Because $\sigma_{ij}$ is symmetric, there is always a set of three mutually perpendicular directions — the **principal axes** — on whose planes the shear stresses vanish. The normal stresses on them, the **principal stresses** $\sigma_1\ge\sigma_2\ge\sigma_3$, are the eigenvalues of the tensor. In two dimensions they are

$$
\sigma_{1,2}=\frac{\sigma_{xx}+\sigma_{yy}}2\pm\sqrt{\left(\frac{\sigma_{xx}-\sigma_{yy}}2\right)^2+\tau_{xy}^2}
$$

and the construction of Mohr's circle (Figure 11.1) displays the normal and shear stress on every plane through the point. For the example in the figure ($\sigma_{xx}=120$, $\sigma_{yy}=20$, $\tau_{xy}=40$ MPa) the centre is at 70 MPa and the radius $\sqrt{50^2+40^2}=64$ MPa, so $\sigma_1=134$ MPa, $\sigma_2=6$ MPa, and the maximum in-plane shear stress is 64 MPa. The largest principal stress drives brittle fracture; the maximum shear stress drives plastic yielding (Chapter 13).

Any stress state can be split into a **hydrostatic** part, the mean stress $\sigma_m=\tfrac13(\sigma_{11}+\sigma_{22}+\sigma_{33})$ acting equally in all directions, and a **deviatoric** part $s_{ij}=\sigma_{ij}-\sigma_m\delta_{ij}$. The hydrostatic part changes volume; the deviatoric part changes shape. The split matters because crystals yield by shear: plastic flow of metals is driven almost entirely by the deviatoric stress, while the hydrostatic stress governs the growth of voids in ductile fracture and the closing of cracks in compression.

Common special states include **uniaxial** tension (a tensile bar, a cable), **pure shear** (a shaft in torsion), **biaxial** tension (a thin-walled pressure vessel, with hoop stress $pr/t$ twice the axial stress $pr/2t$; a thin film on a substrate), and **plane stress** ($\sigma_{3j}=0$, valid in thin sheets) versus **plane strain** ($\varepsilon_{3j}=0$, valid deep inside thick sections, where the surrounding material prevents through-thickness contraction).

### The strain tensor

Deformation is described by the displacement $\mathbf u(\mathbf x)$ of each material point. For small displacement gradients, the **infinitesimal strain tensor** is

$$
\varepsilon_{ij}=\frac12\left(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_j}{\partial x_i}\right)
$$

Its diagonal components are the fractional changes of length along the axes; the off-diagonal components are half the change of angle between two lines originally along the axes. Engineers commonly use the **engineering shear strain** $\gamma_{ij}=2\varepsilon_{ij}$ ($i\ne j$), the full change of angle, so care is needed with factors of two. The trace $\varepsilon_{11}+\varepsilon_{22}+\varepsilon_{33}=\Delta V/V$ is the volumetric strain. The antisymmetric part of the displacement gradient, excluded from $\varepsilon_{ij}$, is a rigid rotation and produces no stress.

> **Status of the principle: Infinitesimal strain**
> *Approximate.* Exact as the displacement gradients tend to zero; adequate for elastic strains of metals and ceramics (below about 1 %), but large-deformation problems — metal forming, rubbers, soft tissue — need finite-strain measures such as the logarithmic (true) strain or the Green–Lagrange tensor.

---

## 11.2 Linear elasticity

### The generalized Hooke's law

For small strains, the stress in an elastic solid is a linear function of the strain:

$$
\sigma_{ij}=C_{ijkl}\,\varepsilon_{kl},\qquad \varepsilon_{ij}=S_{ijkl}\,\sigma_{kl}
$$

$C_{ijkl}$ is the **stiffness tensor** and $S_{ijkl}$ the **compliance tensor**, both of rank 4 (Chapter 4). Symmetry of stress and strain reduces their 81 components to 36, and the existence of a strain-energy function $W=\tfrac12C_{ijkl}\varepsilon_{ij}\varepsilon_{kl}$ reduces them to 21 for the least symmetric (triclinic) crystal. It is convenient to use **Voigt notation**, replacing index pairs by single indices ($11\to1$, $22\to2$, $33\to3$, $23\to4$, $13\to5$, $12\to6$), so that stiffness becomes a symmetric $6\times6$ matrix $C_{mn}$ acting on the vector $(\varepsilon_1,\ldots,\varepsilon_6)$ with $\varepsilon_4=\gamma_{23}$ and so on.

> **Status of the principle: Generalized Hooke's law**
> *Approximate.* The linear term of an expansion of stress about the unstrained state, with the symmetries guaranteed by energy conservation (which are *fundamental*); accurate for metals and ceramics to strains of about 0.1–0.5 %, but not for rubbers at large strain or for polymers whose response depends on time (Chapter 14).

Crystal symmetry, through Neumann's principle (Chapter 4), reduces the number of independent constants further:

**Table 11.1 — Independent elastic constants by symmetry.**

| Symmetry | Independent constants | Examples |
|---|---|---|
| Triclinic | 21 | Some minerals, feldspars |
| Orthotropic (orthorhombic) | 9 | Wood, rolled sheet with texture, unidirectional composite lamina (in general) |
| Tetragonal | 6 | Sn, TiO₂ (rutile), martensite |
| Hexagonal / transversely isotropic | 5 | Mg, Ti, Zn, ZnO; unidirectional fibre composite; cortical bone (approximately) |
| Cubic | 3 ($C_{11},C_{12},C_{44}$) | Fe, Cu, Al, Ni, W, Si, NaCl, MgO |
| Isotropic | 2 ($E,\nu$ or $K,G$ or $\lambda,\mu$) | Glasses, untextured polycrystals, amorphous polymers |

### Isotropic solids

For an isotropic material, two constants suffice. In uniaxial tension along $x$,

$$
\varepsilon_{xx}=\frac{\sigma_{xx}}E,\qquad \varepsilon_{yy}=\varepsilon_{zz}=-\nu\,\frac{\sigma_{xx}}E
$$

which define **Young's modulus** $E$ and **Poisson's ratio** $\nu$. In general,

$$
\varepsilon_{ij}=\frac{1+\nu}{E}\,\sigma_{ij}-\frac{\nu}{E}\,\sigma_{kk}\,\delta_{ij}
$$

The **shear modulus** $G$ ($\tau=G\gamma$) and **bulk modulus** $K$ ($\sigma_m=K\,\Delta V/V$) are

$$
G=\frac{E}{2(1+\nu)},\qquad K=\frac{E}{3(1-2\nu)}
$$

> **Status of the principle: Isotropic elastic relations**
> *Derived.* Exact consequences of linear elasticity with no preferred direction; they fail for single crystals, textured polycrystals, wood and fibre composites.

Positive-definiteness of the strain energy requires $K>0$ and $G>0$, so $-1<\nu<0.5$. Most metals have $\nu\approx0.26$–$0.35$, ceramics and glasses 0.15–0.27, concrete 0.15–0.2, glassy polymers 0.33–0.40 and rubbers almost exactly 0.5, the incompressible limit at which $K\gg G$. Materials with $\nu<0$, which expand laterally when stretched, exist as engineered **auxetic** foams and lattices, used in protective padding and some stents.

For steel with $E=207$ GPa and $\nu=0.30$: $G=79.6$ GPa and $K=172.5$ GPa. Two further combinations recur. A thin film or plate constrained in its plane deforms with the **biaxial modulus** $E/(1-\nu)$; a plate in bending, a wide beam or a material under plane strain with the **plate modulus** $E/(1-\nu^2)$.

**Table 11.2 — Elastic constants of engineering materials (room temperature, typical).**

| Material | $E$ (GPa) | $\nu$ | Density (Mg/m³) | $E/\rho$ (GPa per Mg/m³) |
|---|---|---|---|---|
| Diamond | 1000–1100 | 0.07–0.10 | 3.52 | ~300 |
| Tungsten carbide (WC–Co) | 550–650 | 0.22 | 14–15 | ~42 |
| Silicon carbide | 400–440 | 0.15–0.19 | 3.15–3.2 | ~130 |
| Tungsten | 411 | 0.28 | 19.3 | 21 |
| Alumina (99.5 %) | 370–390 | 0.22 | 3.9 | ~97 |
| Silicon nitride | 300–320 | 0.27 | 3.2 | ~97 |
| Steels (carbon, low-alloy) | 200–210 | 0.29–0.30 | 7.85 | 26 |
| Nickel and superalloys (polycrystal) | 200–220 | 0.30–0.31 | 8.2–8.9 | ~25 |
| Copper | 120–130 | 0.34 | 8.96 | 14 |
| Titanium alloys (Ti–6Al–4V) | 110–120 | 0.34 | 4.43 | 26 |
| Aluminium alloys | 68–72 | 0.33 | 2.7–2.8 | 26 |
| Soda-lime glass | 70–74 | 0.22 | 2.5 | 29 |
| Magnesium alloys | 44–45 | 0.29 | 1.8 | 25 |
| Concrete | 25–40 | 0.15–0.20 | 2.3–2.4 | ~13 |
| Cortical bone (longitudinal) | 15–20 | ~0.3 | 1.9–2.0 | ~9 |
| Spruce, along grain (across grain) | 10–13 (0.5–0.8) | — | 0.40–0.45 | ~27 |
| CFRP, unidirectional, along fibres | 130–180 | 0.3 | 1.55–1.6 | ~100 |
| Epoxy | 2.5–3.5 | 0.35 | 1.2 | ~2.5 |
| PMMA | 2.4–3.3 | 0.37 | 1.18 | ~2.5 |
| HDPE | 0.8–1.2 | 0.42 | 0.95 | ~1 |
| Natural rubber (vulcanized) | 0.001–0.005 | 0.4999 | 0.92–1.0 | ~0.003 |

A striking feature of the table is that steel, aluminium, titanium and magnesium alloys all have almost the same **specific modulus** $E/\rho\approx25$ GPa per Mg/m³. Substituting one metal for another does not make a stiff structure lighter unless the geometry changes; the large gains come from ceramics and from carbon-fibre composites, which is why aircraft structures moved from aluminium to CFRP (Chapters 22 and 48).

### Anisotropic crystals: the cubic case

A cubic crystal has three independent constants, $C_{11}$, $C_{12}$ and $C_{44}$. It would be isotropic only if $C_{44}=(C_{11}-C_{12})/2$; the **Zener anisotropy ratio**

$$
A=\frac{2C_{44}}{C_{11}-C_{12}}
$$

measures the departure. Chapter 4 showed why cubic symmetry forces a second-rank property such as conductivity to be isotropic but leaves a fourth-rank property free to vary with direction. The Young's modulus along a direction with direction cosines $l_1,l_2,l_3$ relative to the cube axes is

$$
\frac1{E_{\langle hkl\rangle}}=S_{11}-2\left(S_{11}-S_{12}-\tfrac12S_{44}\right)\left(l_1^2l_2^2+l_2^2l_3^2+l_3^2l_1^2\right)
$$

The orientation factor $l_1^2l_2^2+\ldots$ is 0 along $\langle100\rangle$, 1/4 along $\langle110\rangle$ and 1/3 along $\langle111\rangle$, so these three directions are the extremes and the intermediate.

> **Status of the principle: Directional modulus of a cubic crystal**
> *Derived.* Exact transformation of the fourth-rank compliance tensor under rotation of axes, given the cubic symmetry.

**Worked example — How anisotropic is copper?** The single-crystal stiffnesses of copper are $C_{11}=168.4$, $C_{12}=121.4$, $C_{44}=75.4$ GPa. Inverting the cubic stiffness matrix gives the compliances $S_{11}=14.99$, $S_{12}=-6.28$ and $S_{44}=13.26$ TPa⁻¹.

Anisotropy ratio: $A=2\times75.4/(168.4-121.4)=150.8/47.0=3.21$.

Moduli: $E_{\langle100\rangle}=1/S_{11}=1/14.99\ \mathrm{TPa^{-1}}=66.7$ GPa. The bracket $S_{11}-S_{12}-\tfrac12S_{44}=14.99+6.28-6.63=14.64$ TPa⁻¹, so

$$
\frac1{E_{\langle111\rangle}}=14.99-2\times14.64\times\tfrac13=5.23\ \mathrm{TPa^{-1}},\qquad E_{\langle111\rangle}=191\ \mathrm{GPa}
$$

and similarly $E_{\langle110\rangle}=130$ GPa. A copper crystal is almost three times stiffer along the cube diagonal than along the cube edge.

An untextured polycrystal averages over all orientations. The Voigt bound (uniform strain) gives $G_V=(C_{11}-C_{12}+3C_{44})/5=54.6$ GPa, the Reuss bound (uniform stress) $G_R=5/[4(S_{11}-S_{12})+3S_{44}]=40.0$ GPa; with $K=(C_{11}+2C_{12})/3=137.1$ GPa, the Hill average $G_H=47.3$ GPa gives $E=9KG/(3K+G)=127$ GPa and $\nu=0.345$ — in agreement with the 120–130 GPa measured on annealed copper. The same calculation gives $A=2.4$ and $E_{\langle100\rangle}=132$ GPa, $E_{\langle111\rangle}=283$ GPa for iron; for aluminium, with $A=1.2$, the range is only 64–76 GPa, and tungsten ($A=1.01$) is isotropic to within 1 %.

<!-- FIGURE 11.2 | figures/ch11/fig-11-2-directional-modulus.png | plot | Directional Young's modulus of cubic single crystals of copper, iron, aluminium and tungsten in the (1-10) plane, compared with the isotropic polycrystal values. | Content: polar plot, angle from [001] (0°) through [111] (54.7°) to [110] (90°) and on to [00-1], radius E in GPa from 0 to 300. Curves computed from the compliances: Cu (E100 = 66.7, E111 = 191, E110 = 130), Fe (132, 283, 220), Al (63.9, 76.1, 72.6), W (~408 constant, drawn as near-circle, scale capped at 450 if needed — alternatively draw W in an inset). Dashed circles at polycrystal Hill averages: Cu 127, Fe 211. Mark the [001], [111], [110] directions with radial lines. -->

Elastic anisotropy has direct engineering consequences, shown in Figure 11.2:

- **Single-crystal turbine blades** of nickel superalloys are grown with $\langle001\rangle$ along the blade axis. Their modulus in that direction, about 125–130 GPa at room temperature, is roughly 60 % of a polycrystal's (about 210–220 GPa), so thermal strains during engine start-up produce proportionately lower thermal stresses and the blades survive more thermal-fatigue cycles (Chapter 33).
- **Silicon MEMS** resonators and cantilevers have moduli from 130 GPa ($\langle100\rangle$) to 188 GPa ($\langle111\rangle$) depending on the direction they are etched along.
- **Textured sheet** has a modulus varying by several percent in its plane, which matters for spring-back in forming.

### Orthotropic and transversely isotropic materials

Many materials are anisotropic because of microstructure rather than crystal symmetry. **Wood** is orthotropic, spruce being 15–25 times stiffer along the grain than across it; a **unidirectional fibre composite** is transversely isotropic with five constants (Chapters 22 and 23); **cortical bone** is approximately transversely isotropic. For all of them the full compliance matrix, not a single $E$, must enter the analysis.

---

## 11.3 Origins of elastic moduli in bonding

### The interatomic potential

Elastic deformation stretches interatomic bonds without breaking them. Two atoms at separation $r$ have a potential energy $U(r)$ with a minimum at the equilibrium spacing $r_0$, and the force between them is $F=-dU/dr$. Near $r_0$ the force is linear in displacement, with a bond stiffness $S_0=(d^2U/dr^2)_{r_0}$. Treating a solid as an array of such springs, one per area $r_0^2$ in parallel and one per length $r_0$ in series, gives

$$
E\approx\frac{S_0}{r_0}
$$

> **Status of the principle: Bond-stiffness estimate of the modulus**
> *Approximate.* Captures the magnitude and ranking of moduli across bond types; it ignores crystal geometry, angular (bond-bending) forces and many-body effects, and it does not apply to rubbers, whose stiffness is entropic (Section 11.4).

The shape of $U(r)$ is a question of chemical bonding (Advanced Chemistry); the consequences for stiffness are summarized in Table 11.3. Covalent bonds are strong and directional and resist both stretching and bending, giving the stiffest solids. Ionic bonds are strong but non-directional; metallic bonds intermediate. Polymers are covalently bonded along each chain but held to their neighbours by van der Waals or hydrogen bonds 10–100 times less stiff, and these weak links in series dominate the modulus of an unoriented polymer. Drawing the chains parallel, as in ultra-high-molecular-weight polyethylene fibre (about 100 GPa) or aramid fibre (70–140 GPa), loads the covalent backbone directly and raises the modulus by two orders of magnitude.

**Table 11.3 — Bond type and stiffness.**

| Bond type | Typical bond stiffness $S_0$ (N/m) | Typical $E$ (GPa) | Examples |
|---|---|---|---|
| Covalent (C–C, Si–C) | 50–180 | 200–1000 | Diamond, SiC, carbon fibre (axial) |
| Ionic / ionic–covalent | 8–30 | 30–400 | Alumina, MgO, NaCl (~40) |
| Metallic | 15–75 | 40–410 | Mg, Al, Cu, Fe, W |
| Hydrogen bond | 2–5 | 2–10 | Ice (~9), cellulose cross-links |
| Van der Waals | 0.5–2 | 1–4 | Unoriented polymers, graphite between layers |

### Correlation with melting temperature

The depth of the potential well sets the melting temperature and its curvature sets the modulus; since both scale with bond strength, $E$ correlates with $T_m$. A useful estimate is $E\approx100\,kT_m/\Omega$, where $\Omega$ is the atomic volume. For copper ($\Omega=1.18\times10^{-29}$ m³, $T_m=1358$ K) it gives 159 GPa against a measured 124; for iron 212 against 211; for aluminium 78 against 70; for tungsten 322 against 411. The estimate is correct to a factor better than 1.3 across a factor of six in modulus. It also explains why modulus falls with temperature: as atoms vibrate with larger amplitude in an asymmetric well, the mean spacing increases and the curvature at the mean position decreases. Metals typically lose 10–20 % of their room-temperature modulus by half their melting temperature, and steels about 15 % by 500 °C — an effect included in the design of boilers, turbine casings and fire-exposed structures.

### Microstructure, porosity and cellular solids

Modulus is called **structure-insensitive** because cold work, grain size and modest alloying change it by only a few percent. Two microstructural features do change it strongly:

- **Second phases** in large volume fractions, as in composites, where the modulus follows rule-of-mixtures bounds (Chapter 22). Tungsten carbide particles raise the modulus of a cobalt matrix to 550–650 GPa in cemented carbides.
- **Porosity.** A widely used empirical fit for isolated pores is $E=E_0(1-1.9p+0.9p^2)$, so 5 % porosity lowers the modulus of a sintered ceramic or powder-metallurgy part by 9 % and 10 % porosity by 18 %. For highly porous **cellular solids** — polymer and metal foams, balsa, trabecular bone, additively manufactured lattices — bending of cell walls dominates and $E/E_s\approx(\rho/\rho_s)^2$, so a foam of 10 % relative density has only about 1 % of the solid's stiffness. Bone-replacement scaffolds and porous titanium implant surfaces are designed with this scaling to match the stiffness of bone and avoid **stress shielding**, the bone loss that occurs when an implant much stiffer than bone carries most of the load (Chapter 31).

<!-- FIGURE 11.3 | figures/ch11/fig-11-3-modulus-by-class.png | plot | Young's modulus of engineering materials grouped by class and bond type, on a logarithmic scale from 10⁻⁴ to 10³ GPa. | Content: horizontal bar ranges on log x-axis (E, GPa, 1e-4 to 2e3); rows grouped and colour-coded: elastomers (natural rubber 0.001–0.005, silicone 0.001–0.01), foams (PU foam 0.001–0.1), polymers (HDPE 0.8–1.2, PMMA 2.4–3.3, epoxy 2.5–3.5, PEEK 3.6–4), natural (wood across grain 0.5–0.8, along grain 10–13, cortical bone 15–20), concrete 25–40, glass 70–74, metals (Mg 45, Al 70, Ti 115, Cu 125, steel 205, W 411), technical ceramics (Si3N4 310, Al2O3 380, SiC 420, WC 600), composites (GFRP 20–45, CFRP UD 130–180), diamond 1050. Vertical annotations "van der Waals / H-bond", "metallic", "ionic–covalent", "covalent" above corresponding regions; "entropic" above elastomers. -->

Figure 11.3 summarizes the result: moduli span about seven orders of magnitude, and the main divisions follow bond type, with entropy taking over at the soft end.

---

## 11.4 Rubber and entropic elasticity (preview)

A rubber band behaves in ways that bond stretching cannot explain. Its modulus is a few MPa, a thousand times lower than a glassy polymer; it stretches reversibly to 5–10 times its length; it becomes *stiffer*, not softer, when heated; and it warms when stretched quickly. Rubber elasticity is **entropic**. Above its glass-transition temperature, a lightly cross-linked polymer consists of long, flexible chain segments between cross-links, each writhing among an enormous number of conformations. Stretching the network aligns the chains, reduces the number of available conformations and therefore the entropy. The restoring force is the thermodynamic tendency to return to the more probable, randomly coiled state — the same origin as the pressure of an ideal gas.

The simplest network theory (Chapter 20) gives a shear modulus $G=NkT$ and, since rubber is incompressible ($\nu\approx0.5$), a Young's modulus

$$
E=3NkT
$$

where $N$ is the number of network chains per unit volume. For $N=10^{26}$ m⁻³ (a typical vulcanized natural rubber), $E=3\times10^{26}\times1.38\times10^{-23}\times300=1.24$ MPa at 300 K, rising to 1.45 MPa at 350 K. The modulus is proportional to the cross-link density, which is how vulcanization with sulfur turns a sticky gum into a tyre, seal or vibration mount (Chapter 21).

> **Status of the principle: Entropic (affine network) rubber elasticity**
> *Approximate.* Derived from the statistics of ideal Gaussian chains deforming affinely with the network; it predicts the magnitude and temperature dependence of rubber moduli well at moderate strains but underestimates stiffening at large extensions (finite chain length) and ignores entanglements and fillers.

Rubber stress–strain curves are nonlinear from the start, so a single $E$ is only a small-strain description; hyperelastic models (neo-Hookean, Mooney–Rivlin, Ogden) are used in the finite-element design of seals, bearings for bridges and buildings, and soft robotics. Biological tissues such as arteries, skin and the elastin in lungs combine entropic elasticity with stiff collagen fibres that straighten at larger strains, giving their characteristic J-shaped curves.

---

## 11.5 The tensile test

### Specimens and measurement

The **tensile test** is the most widely used mechanical test and the source of most datasheet properties. A specimen with a reduced, uniform **gauge section** (round or flat, with gauge length $L_0$ often $5.65\sqrt{A_0}$ in ISO practice or $4d_0$ in ASTM) is pulled at a controlled rate while the force $F$ and the extension of the gauge length $\Delta L$ are recorded (ISO 6892-1 and ASTM E8 for metals; ISO 527 and ASTM D638 for plastics; ASTM D3039 for composites). Engineering stress and strain are

$$
\sigma=\frac F{A_0},\qquad e=\frac{\Delta L}{L_0}
$$

An **extensometer** clipped to the gauge length is essential for measuring the modulus and yield point: the crosshead displacement includes the elastic deformation of the grips and load frame, which can exceed that of the specimen in the elastic range. Strain rate matters for polymers and for metals near their melting point, and must be reported.

### Reading the engineering stress–strain curve

Figure 11.4 shows the features of a curve for a ductile metal:

- The **linear elastic region**, with slope $E$. (Moduli from tensile tests are usually less accurate than those from ultrasonic or resonance methods, which measure the sound velocity $v=\sqrt{E/\rho}$ — about 5100 m/s in steel and aluminium, 9800 m/s in alumina.)
- **Yield.** Most metals depart gradually from linearity, so the **0.2 % offset yield strength** $R_{p0.2}$ is defined as the stress at which a line parallel to the elastic slope, offset by 0.2 % strain, meets the curve. Low-carbon steels instead show a sharp **upper yield point** followed by a lower yield plateau, during which deformation propagates along the specimen as **Lüders bands**; the cause is carbon and nitrogen atoms pinning dislocations (Chapter 13), and the visible stretcher-strain markings it leaves on pressed sheet are why automotive panels use interstitial-free or temper-rolled steel.
- **Uniform plastic deformation with work hardening.** The stress rises as dislocations multiply and interact.
- The **ultimate tensile strength** (UTS, $R_m$), the maximum engineering stress, at the **uniform elongation**. Beyond it a **neck** forms, deformation localizes and the engineering stress falls until fracture.
- **Ductility**, reported as the percentage **elongation after fracture** (over a stated gauge length, because the neck contributes a fixed extension) and the **reduction of area** $RA=(A_0-A_f)/A_0$, which reflects the local ductility in the neck.

Yield strength and UTS are **structure-sensitive**: they depend strongly on grain size, dislocation density, solutes and precipitates, which is the subject of Chapter 13. The area under the curve to fracture is the **tensile toughness** (Section 11.7); the area under the elastic part to yield, $\sigma_y^2/2E$, is the **modulus of resilience**, the elastic energy a spring can store per unit volume.

### True stress and true strain

Once plastic deformation begins, the cross-section shrinks. The **true stress** uses the current area, $\sigma_T=F/A$, and the **true (logarithmic) strain** integrates increments of length relative to the current length:

$$
\varepsilon_T=\int_{L_0}^{L}\frac{dL}{L}=\ln\frac L{L_0}=\ln(1+e)
$$

Plastic deformation conserves volume ($AL=A_0L_0$), so up to the onset of necking

$$
\sigma_T=\sigma(1+e)
$$

True strains are additive for successive deformation steps — a property essential in metal-forming calculations — whereas engineering strains are not. Beyond necking the area must be measured directly, and the true strain at fracture is $\ln(A_0/A_f)$. The stress in the neck is also no longer uniaxial; the **Bridgman correction** accounts for the triaxial stress state the neck geometry creates.

The plastic part of the true curve for many metals follows the **Hollomon** relation

$$
\sigma_T=K\,\varepsilon_T^{\,n}
$$

with strength coefficient $K$ and strain-hardening exponent $n$: about 0.4–0.5 for annealed copper and austenitic stainless steel, 0.2–0.25 for low-carbon steel, 0.05–0.15 for high-strength and age-hardened alloys.

> **Status of the principle: Hollomon power law**
> *Empirical.* A two-parameter fit to true stress–strain data over roughly a decade of strain; refined forms (Ludwik, Swift, Voce) are used where the fit near yield or at large strains matters.

### Necking: the Considère criterion

Necking starts when the increase in strength from work hardening can no longer compensate for the decrease in area. At the load maximum $dF=d(\sigma_TA)=0$; with $dA/A=-d\varepsilon_T$ from volume constancy,

$$
\frac{d\sigma_T}{d\varepsilon_T}=\sigma_T
$$

For the Hollomon law this gives necking at $\varepsilon_T=n$: the strain-hardening exponent equals the uniform true strain. High-$n$ materials can be stretched further before they localize, which is why austenitic stainless steels and TWIP steels (Chapter 15) are valued for deep drawing and crash-absorbing structures.

> **Status of the principle: Considère criterion**
> *Derived.* Follows exactly from the load maximum and volume constancy; its accuracy is that of the hardening law inserted, and it ignores strain-rate sensitivity, which delays necking in superplastic alloys and polymers.

<!-- FIGURE 11.4 | figures/ch11/fig-11-4-tensile-true-engineering.png | plot | Engineering and true stress–strain curves for a normalized medium-carbon steel (worked example), showing yield, uniform elongation, necking, fracture and the Considère construction. | Content: x-axis strain 0–0.8 (engineering strain for the engineering curve, true strain for the true curve); y-axis stress 0–1200 MPa. Engineering curve: linear to ~412 MPa (0.2 % offset construction shown in an inset at strains 0–0.01), rising to UTS 623 MPa at engineering strain 0.221, falling to fracture at 0.30 with stress ~490 MPa. True curve: σT = 1050 εT^0.20 MPa from yield to εT = 0.20 (solid), then dashed extrapolation to the true fracture point (εT = 0.795, σT = 1083 MPa) marked with a cross labelled "true fracture stress (uncorrected)". Considère construction: dσT/dεT curve intersecting σT at εT = 0.20, labelled "necking". -->

**Worked example — Reducing tensile-test data.** A round bar of normalized medium-carbon steel (similar to 1045) with $d_0=12.5$ mm and $L_0=50$ mm is tested. The record gives: 0.2 % offset yield load 50.5 kN; load 67.1 kN at engineering strain 0.05; 75.6 kN at 0.15; maximum load 76.4 kN; load at fracture 60.0 kN; final gauge length 65.0 mm; diameter at the fracture 8.4 mm.

Area: $A_0=\pi(12.5)^2/4=122.7$ mm².

Engineering properties: $R_{p0.2}=50\,500/122.7=412$ MPa; UTS $=76\,400/122.7=623$ MPa; elongation $=(65.0-50.0)/50.0=30$ %; reduction of area $=1-(8.4/12.5)^2=54.8$ %.

True stress and strain at the two intermediate points: at $e=0.05$, $\sigma=547$ MPa, $\sigma_T=547\times1.05=574$ MPa, $\varepsilon_T=\ln1.05=0.0488$; at $e=0.15$, $\sigma=616$ MPa, $\sigma_T=708$ MPa, $\varepsilon_T=0.1398$.

Hollomon fit through the two points:

$$
n=\frac{\ln(708.5/574.1)}{\ln(0.1398/0.0488)}=\frac{0.2103}{1.0524}=0.200,\qquad K=\frac{574.1}{0.0488^{0.200}}=1050\ \mathrm{MPa}
$$

Consistency check with Considère: necking at $\varepsilon_T=n=0.200$, i.e. engineering strain $e^{0.200}-1=0.221$, where $\sigma_T=1050\times0.2^{0.2}=760$ MPa and the engineering stress is $760/1.221=623$ MPa — the measured UTS.

True fracture strain $=\ln(A_0/A_f)=2\ln(12.5/8.4)=0.795$; true fracture stress $=60\,000/(\pi\times4.2^2)=1083$ MPa (before Bridgman correction).

Two practical lessons. The true strain at fracture, 0.795, is nearly four times the uniform strain: most of the ductility of this steel is consumed locally in the neck, which is why reduction of area is a better guide to fracture resistance in a forming operation than elongation. And the elastic extension at a load of 20 kN is only $\sigma/E\times L_0=(163\ \mathrm{MPa}/205\ \mathrm{GPa})\times50\ \mathrm{mm}=40$ μm — comparable to the slack and elastic deflection of grips and load train, which is why modulus cannot be taken from crosshead displacement.

**Table 11.4 — Tensile properties of engineering materials (room temperature, typical).**

| Material and condition | $R_{p0.2}$ (MPa) | UTS (MPa) | Elongation (%) |
|---|---|---|---|
| Structural steel S355 (EN 10025) | ≥ 355 | 470–630 | ≥ 20–22 |
| AISI 1045, normalized | 410–430 | 620–680 | 20–25 |
| AISI 4340, quenched and tempered (425 °C) | 1350–1500 | 1500–1650 | 10–12 |
| Austenitic stainless 304, annealed | 205–290 | 515–620 | 40–60 |
| Aluminium 6061-T6 | 275 | 310 | 10–12 |
| Aluminium 7075-T6 | 500 | 570 | 10–11 |
| Ti–6Al–4V, mill-annealed | 880–950 | 950–1000 | 10–15 |
| Copper, annealed | 50–70 | 220–240 | 40–50 |
| Polycarbonate | 60–65 | 65–70 | 80–120 |
| PMMA | — (brittle) | 50–75 | 2–5 |
| Alumina | — | 250–300 (tensile) | ~0 |
| CFRP UD, along fibres | — | 1500–2500 | 1–1.8 |

---

## 11.6 Hardness tests

### Indentation hardness

**Hardness** is resistance to localized plastic deformation, measured by pressing a hard indenter into the surface and measuring the size or depth of the impression. It is quick, nearly non-destructive, works on small regions and finished parts, and correlates with strength. It is the everyday quality-control test for heat treatment, case hardening and welds.

- **Brinell (HB, HBW)**: a 10 mm hard-metal ball pressed with 3000 kgf (for steels) or 500–1500 kgf (softer metals) for 10–15 s; $HB=2F/[\pi D(D-\sqrt{D^2-d^2})]$ with $F$ in kgf and $D$, $d$ (indent diameter) in mm. The large indent averages over coarse microstructures, such as cast iron and castings.
- **Vickers (HV)**: a square-based diamond pyramid with 136° between opposite faces; $HV=1.8544\,F/d^2$, with $d$ the mean diagonal in mm. Loads from 10 gf (microhardness) to 100 kgf cover everything from single phases and thin coatings to bulk steel, on one continuous scale.
- **Knoop (HK)**: an elongated pyramid giving a shallow indent, for thin coatings and brittle materials; $HK=14.229\,F/L^2$.
- **Rockwell (HRC, HRB, ...)**: the depth of penetration under a major load after a minor preload, read directly from a dial. HRC uses a diamond cone and 150 kgf for hardened steels; HRB a 1/16 in ball and 100 kgf for softer metals. Fast and automated, it is the standard on heat-treatment lines.
- **Shore durometers (A, D)**: spring-loaded indenters for elastomers and soft plastics.

### Hardness and strength: Tabor's relation

Under the indenter the plastically deforming material is constrained by the surrounding elastic material, so it must be stressed to about three times its uniaxial flow stress before the indenter sinks in. Slip-line field analysis of a rigid-plastic solid gives

$$
H\approx3\,\sigma_{y}
$$

with $H$ in pressure units (1 HV $=9.807$ MPa). Because the material under a Vickers or Brinell indenter is strained by roughly 8 %, $\sigma_y$ here is the flow stress at that **representative strain**, which for work-hardening metals lies between the yield strength and the UTS. Empirical conversions such as $\mathrm{UTS}\approx3.45\,HB$ (MPa) or $\mathrm{UTS}\approx3.2$–$3.3\,HV$ for steels, and standard conversion tables between scales (ASTM E140), are used routinely, but they are material-specific.

> **Status of the principle: Tabor's relation**
> *Approximate.* From plasticity theory for a rigid-perfectly-plastic material with a constraint factor near 3; it fails for brittle materials (cracking), for materials with low $E/\sigma_y$ such as polymers (elastic accommodation lowers the constraint) and for strongly work-hardening metals unless a representative strain is used.

**Worked example — From an indent to a strength.** A quenched-and-tempered 4140 shaft is checked with a Vickers indenter at 30 kgf. The mean diagonal is 0.400 mm.

$HV=1.8544\times30/0.400^2=1.8544\times30/0.160=348$ HV, or $H=348\times9.807=3.41$ GPa. (This corresponds to about 35 HRC.)

Tabor gives a flow stress $H/3\approx1.14$ GPa at about 8 % strain. The steel conversion $\mathrm{UTS}\approx3.3\,HV$ gives about 1150 MPa, consistent with the 1100–1200 MPa expected for 4140 tempered to this hardness; its 0.2 % yield would be roughly 950–1050 MPa. The hardness test therefore checks the heat treatment of every shaft in seconds, while a tensile test on a sample from each batch confirms the conversion.

**Table 11.5 — Representative hardness values.**

| Material | Hardness |
|---|---|
| Lead | ~5 HV |
| Pure aluminium, annealed | 20–25 HV |
| Copper, annealed | 40–50 HV |
| Aluminium 6061-T6 | ~105 HV (95 HB) |
| Low-carbon steel, hot-rolled | 120–150 HV |
| Ti–6Al–4V | 330–360 HV |
| Bearing and tool steels, hardened | 60–65 HRC (700–850 HV) |
| Cemented carbide (WC–Co) | 1300–1800 HV |
| Alumina | 1500–1900 HV |
| Silicon carbide | 2500–2800 HV |
| Cubic boron nitride | ~4500 HV |
| Diamond | 8000–10 000 HV |
| Natural rubber, vulcanized | 40–70 Shore A |
| HDPE / PMMA | 60–70 / 85–90 Shore D |

### Nanoindentation

**Nanoindentation** (instrumented indentation) records load $P$ against depth $h$ continuously, at loads from micronewtons to hundreds of millinewtons and depths of tens of nanometres to a few micrometres, usually with a three-sided Berkovich pyramid. Instead of imaging the indent, the **Oliver–Pharr method** extracts properties from the unloading curve (Figure 11.5). The initial unloading slope $S=dP/dh$ is elastic and gives the **reduced modulus**

$$
E_r=\frac{\sqrt\pi}{2\beta}\frac{S}{\sqrt{A}},\qquad \frac1{E_r}=\frac{1-\nu^2}{E}+\frac{1-\nu_i^2}{E_i}
$$

where $A$ is the projected contact area ($A\approx24.5\,h_c^2$ for an ideal Berkovich tip at contact depth $h_c$), $\beta\approx1.03$–$1.05$ a geometry correction, and the subscript $i$ refers to the diamond indenter ($E_i=1141$ GPa, $\nu_i=0.07$). Hardness is $H=P_{\max}/A$.

> **Status of the principle: Oliver–Pharr analysis**
> *Approximate.* Based on elastic contact solutions (Sneddon) applied to the unloading curve; accurate for materials that sink in around the indenter, but it overestimates $H$ and $E$ by up to 30 % for soft, non-hardening materials that pile up, and requires careful calibration of the tip area function.

Nanoindentation is the standard tool for thin films and coatings (keeping the depth below about 10 % of the film thickness so that the substrate does not dominate), individual phases, ion-irradiated surface layers in nuclear materials (Chapter 33), bone lamellae and biomaterials. At small depths, hardness rises as the indent shrinks — the **indentation size effect**, caused by geometrically necessary dislocations (Chapter 12) — so nanoindentation hardnesses of metals are not directly comparable with macroscopic values.

<!-- FIGURE 11.5 | figures/ch11/fig-11-5-indentation.png | schematic | Hardness indenter geometries and a nanoindentation load–displacement curve with the Oliver–Pharr quantities. | Content: Left half: three small sketches — Brinell ball (diameter D) with indent diameter d; Vickers 136° square pyramid with diagonals d1, d2 seen in plan view; Berkovich three-sided pyramid in plan view. Right half: plot of load P (0–10 mN) versus displacement h (0–300 nm) for fused silica-like material: loading curve rising to Pmax = 10 mN at hmax = 280 nm, short hold, unloading curve to final depth hf ≈ 150 nm. Tangent to the top of the unloading curve labelled "S = dP/dh"; depths hf, hc, hmax marked on the x-axis; shaded area between curves labelled "plastic work". -->

---

## 11.7 Impact and toughness testing

### What "toughness" means

**Toughness** is the ability to absorb energy before fracture. Three distinct measures share the name:

1. **Tensile toughness**, the area under the stress–strain curve, $U_T=\int_0^{\varepsilon_f}\sigma\,d\varepsilon$, in J/m³. For the steel of the worked example (average flow stress about 560 MPa over an engineering strain of 0.30) it is roughly $1.7\times10^{8}$ J/m³; for alumina, $\tfrac12\times300\ \mathrm{MPa}\times0.0008\approx1.2\times10^{5}$ J/m³, over a thousand times less.
2. **Impact energy**, absorbed in breaking a notched bar at high rate (this section). It is comparative and specimen-dependent, but cheap and sensitive to embrittlement.
3. **Fracture toughness** $K_{Ic}$ or $J_{Ic}$, the resistance to propagation of an existing sharp crack, a genuine material property that enters design calculations through fracture mechanics (Chapter 14).

### The Charpy and Izod tests

The **Charpy V-notch test** (ISO 148, ASTM E23) breaks a bar 10 × 10 × 55 mm with a 2 mm deep, 45° V-notch in three-point bending by a swinging pendulum striking at about 5 m/s. The energy absorbed is the difference between the pendulum's potential energy at release and at the top of its follow-through swing: a 20 kg pendulum released from 1.5 m (294 J available) that rises to 0.40 m after breaking a specimen has absorbed $20\times9.81\times(1.5-0.40)=216$ J. **Izod** tests use a cantilevered notched specimen and are common for plastics (ISO 180, ASTM D256), where results are often reported per unit width (J/m) or area (kJ/m²). **Instrumented** strikers record force against time and separate the energy for crack initiation from that for propagation.

The notch, the high strain rate and the bending all promote brittle behaviour, which is the point: the test is a sensitive detector of conditions under which a material that is ductile in a slow tensile test will fracture with little energy.

### The ductile–brittle transition

The most important use of impact testing is to find the **ductile-to-brittle transition** of ferritic (BCC) steels (Figure 11.6). At high temperature the fracture surface is fibrous and the energy is high (the **upper shelf**, often 100–300 J); at low temperature it is crystalline and shiny, made of cleavage facets, and the energy falls to a **lower shelf** of a few joules. Between them a transition range spans 30–80 °C. Specifications quote a transition temperature at a fixed energy, such as $T_{27\mathrm J}$, or a minimum energy at the service temperature: ship-plate grades, for example, require 27–34 J at 0, −20 or −40 °C depending on grade.

The engineering record makes the importance clear. Of the roughly 2700 welded Liberty ships built during the Second World War, several hundred suffered serious brittle fractures, and about a dozen broke completely in two, many in cold North Atlantic water; the plate steels had transition temperatures near or above the sea temperature. The cause in BCC metals is the steep temperature dependence of their lattice friction for dislocations (Chapter 12), which lets cleavage win over plastic blunting at low temperature. FCC metals — austenitic stainless steel, aluminium, copper, nickel — have no such transition, which is why they are used for cryogenic tanks for liquefied natural gas and liquid hydrogen (Chapter 33). Polymers show a related transition near their glass-transition temperature, and impact tests at −20 or −40 °C qualify plastic housings and pipes for cold climates.

<!-- FIGURE 11.6 | figures/ch11/fig-11-6-charpy-transition.png | plot | Charpy V-notch impact energy versus test temperature for a ferritic structural steel, a fine-grained low-temperature steel, austenitic stainless steel and an aluminium alloy. | Content: x-axis temperature −196 to +100 °C; y-axis absorbed energy 0–300 J. Curves (tanh-shaped for ferritic steels): structural steel S355J0, lower shelf ~5 J, upper shelf ~200 J, 27 J at about −10 °C, transition midpoint ~10 °C; fine-grained Ni-alloyed low-temperature steel, upper shelf ~250 J, 27 J at about −70 °C; austenitic 304 stainless steel nearly flat at ~150–200 J down to −196 °C; aluminium 5083-O nearly flat at ~30–40 J. Horizontal dashed line at 27 J labelled "typical specification level". Insets of fracture surfaces labelled "fibrous (ductile)" on upper shelf and "cleavage (brittle)" on lower shelf. -->

Impact energies cannot be converted directly into fracture toughness, but empirical correlations between Charpy energy and $K_{Ic}$ are used for screening when fracture-toughness data are unavailable, and the **master-curve** method (ASTM E1921) links small-specimen toughness tests to the transition behaviour of reactor pressure-vessel steels, whose transition temperature shifts upward with neutron irradiation (Chapter 33).

---

## 11.8 Bend, compression and shear testing

### Bend (flexural) tests

Brittle materials are hard to test in tension: gripping a ceramic bar crushes or misaligns it, and a slight bending moment from misalignment raises the stress at one surface. They are therefore tested in **bending** (ASTM C1161 / ISO 14704 for ceramics; ASTM D790 / ISO 178 for plastics; ASTM D7264 for composites). For a rectangular beam of width $b$ and depth $d$ on supports a span $L$ apart:

$$
\sigma_{3\mathrm{pt}}=\frac{3FL}{2bd^2},\qquad \sigma_{4\mathrm{pt}}=\frac{3F(L-L_i)}{2bd^2}
$$

for three-point loading (central load $F$) and four-point loading (total load $F$ on two inner rollers a distance $L_i$ apart). The result is the **flexural strength** or **modulus of rupture**. The flexural modulus follows from the load–deflection slope $m$ as $E=L^3m/(4bd^3)$ in three-point bending. Because only a small volume near the loading point is highly stressed in three-point bending, three-point strengths of brittle materials are systematically higher than four-point strengths, which in turn are higher than tensile strengths — a size effect quantified in Section 11.9.

### Compression tests

**Compression** testing is used for materials that are mainly loaded in compression or that are brittle in tension: concrete, masonry, ceramics, rock, foams, bone and polymer-matrix composites. Concrete strength classes are defined by compression of 150 mm cubes or 150 × 300 mm cylinders at 28 days; a C30/37 concrete has a characteristic cylinder strength of 30 MPa, so a cylinder fails at about $30\times10^6\times\pi\times0.075^2=530$ kN (Chapter 18). Ceramics are 5–15 times stronger in compression than in tension, because cracks close rather than open.

Platen friction restrains lateral expansion, causing **barrelling** and raising apparent strength, and slender specimens **buckle**; lubrication and a height-to-diameter ratio of 1.5–2 control both. Because compression avoids necking, hot compression tests supply the large-strain flow curves used in forging design (Chapter 38).

### Shear and torsion tests

**Torsion** of a solid round bar of diameter $d$ by torque $T$ produces pure shear, with maximum shear stress at the surface

$$
\tau_{\max}=\frac{Tr}{J}=\frac{16T}{\pi d^3}
$$

($J=\pi d^4/32$ is the polar second moment of area). A 20 mm steel drive shaft carrying 200 N m therefore sees 127 MPa at its surface. Torsion tests give the shear modulus directly from the twist angle and, because no necking occurs, flow stresses to very large strains for hot-working studies.

Other shear tests suit specific materials: **lap-shear** for adhesive joints (an average over a joint whose real stress peaks at the ends; Chapter 39), **short-beam shear** for the interlaminar strength of composites, and **V-notched** specimens for their in-plane shear.

**Table 11.6 — Which test for which material and question.**

| Material or question | Preferred test | Reason |
|---|---|---|
| Ductile metal: specification properties | Tensile | Yield, UTS, elongation, RA in one test |
| Heat-treatment check on finished parts | Hardness (Rockwell, Vickers) | Fast, local, almost non-destructive |
| Coatings, thin films, phases | Nanoindentation | Microscale volume, gives $H$ and $E$ |
| Ceramics, glass | Four-point bend | Avoids gripping; defined stressed volume |
| Concrete, masonry, rock, foams | Compression | Service loading; tension strength low |
| Steels for cold service | Charpy V-notch at temperature | Detects ductile–brittle transition |
| Adhesive joints | Lap shear, peel | Mimics joint loading |
| Composite laminates | Tensile, compression, short-beam and in-plane shear | Anisotropy requires several tests |

---

## 11.9 The statistical nature of strength

### Why strength scatters

Repeat a tensile test on twenty bars of a ductile steel from the same heat and the yield strengths will typically fall within ±3–5 %. Repeat a bend test on twenty alumina bars and the strengths may range over ±25 % or more. The difference has a physical cause. Ductile failure is a collective process involving the whole cross-section, so it averages over many microstructural features. Brittle fracture starts at the single worst flaw — a pore, an inclusion, a machining scratch — in the stressed region, and flaw sizes vary from specimen to specimen. Strength is then a property of the flaw population, not of the material alone, and must be described statistically.

### The Weibull distribution

If a body fails when its weakest element fails (the **weakest-link** hypothesis), and the probability that a small volume contains a flaw critical at stress $\sigma$ rises as a power of $\sigma$, the probability of failure of a body of volume $V$ under uniform stress is

$$
P_f(\sigma)=1-\exp\!\left[-\frac{V}{V_0}\left(\frac{\sigma}{\sigma_0}\right)^{m}\right]
$$

where $\sigma_0$ is the **characteristic strength** of the reference volume $V_0$ (the stress at which 63.2 % of such specimens fail) and $m$ is the **Weibull modulus**. A large $m$ means little scatter: typical values are 5–10 for glass and traditional ceramics, 10–20 for technical ceramics, about 20–30 for well-controlled silicon nitride, and effectively above 50 for metals. Taking logarithms twice gives $\ln\ln[1/(1-P_f)]=m\ln\sigma+\text{const}$, so test results ranked and plotted this way fall on a straight line of slope $m$; fitting by maximum likelihood is preferred (ASTM C1239, ISO 20501).

> **Status of the principle: Weibull weakest-link statistics**
> *Empirical.* The weakest-link form follows from independent flaws and a power-law flaw-size tail, but $m$ and $\sigma_0$ are fitted to tests, and extrapolation to failure probabilities far below those tested (one in a million for a medical implant) relies on the assumed form; multiple flaw populations give kinked Weibull plots.

Two consequences follow. **Scatter**: with $m=10$, a stress of $0.8\sigma_0$ gives $P_f=1-\exp(-0.8^{10})=10$ %, so a design must sit far below the characteristic strength. **Size effect**: at equal $P_f$, $\sigma\propto V^{-1/m}$, so a larger part is weaker. For non-uniform stress, $V$ is replaced by an **effective volume** $V_E$, the volume that under the peak stress would give the same failure probability. For a rectangular bar of volume $V$ between the outer supports, $V_E=V/[2(m+1)^2]$ in three-point bending and $V_E=V(m+2)/[4(m+1)^2]$ in quarter-point four-point bending.

**Worked example — From bend bars to a ceramic component.** Alumina bars 3 mm deep and 4 mm wide are broken in three-point bending over a 40 mm span. The characteristic load is 230 N, so the characteristic flexural strength is

$$
\sigma_0=\frac{3\times230\times0.040}{2\times0.004\times0.003^2}=383\ \mathrm{MPa}
$$

and the Weibull modulus is $m=10$. The volume between supports is $V=4\times3\times40=480$ mm³.

Effective volumes: three-point, $V_E=480/(2\times11^2)=1.98$ mm³; four-point (quarter-point), $V_E=480\times12/(4\times11^2)=11.9$ mm³. The four-point characteristic strength is predicted to be $383\times(1.98/11.9)^{1/10}=383\times0.836=320$ MPa — a 16 % difference from the same material, due only to the test geometry.

A component stresses 10 cm³ ($10\,000$ mm³) in uniform tension. Its characteristic strength is $383\times(1.98/10\,000)^{1/10}=383\times0.426=163$ MPa. If the acceptable failure probability is $10^{-4}$ rather than 63.2 %, the allowable stress falls by a further factor $[-\ln(1-10^{-4})]^{1/10}=0.398$, to 65 MPa.

A material whose bend bars average nearly 400 MPa can therefore be used at only about 65 MPa in a large, uniformly stressed part. Raising $m$ — through cleaner powders, hot isostatic pressing and better surface finishing — narrows the gap far more than raising the mean strength. It is also why ceramic hip heads are individually **proof-tested** to a load above the service load: the test breaks the parts that contain the worst flaws and truncates the low-strength tail of the distribution (Chapters 14 and 31).

### Design values from scattered data

Other fields handle scatter with their own conventions. Aerospace design uses **A-basis** allowables (a value exceeded by 99 % of the population with 95 % confidence) for single load paths and **B-basis** (90 % with 95 % confidence) for redundant structure, derived from many tests on several batches. Concrete design uses the **characteristic strength** $f_{ck}$, the 5 % fractile; for a normal distribution with standard deviation $s$, $f_{ck}=f_{cm}-1.645\,s$, so a mix with mean cylinder strength 38.5 MPa and $s=5$ MPa ($38.5-8.2=30.3$ MPa) just achieves a C30 class. Steel specifications quote guaranteed minimum yield strengths, with actual mill values usually 10–20 % higher. Fatigue lives scatter by factors of ten at a given stress, and their statistics return in Chapter 14; reliability statistics in service are the subject of Chapter 36.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| Why do crystals yield at a tiny fraction of their theoretical strength? | Chapter 12 |
| How do slip systems, Schmid's law and polycrystal constraints set the yield stress, and what are the Tresca and von Mises criteria? | Chapter 13 |
| What mechanisms raise yield strength and work hardening, and why do low-carbon steels show a yield point? | Chapter 13 |
| How is fracture toughness defined and measured, and how are $K$, $G$ and $J$ used in design? | Chapter 14 |
| What causes the ductile–brittle transition, and how do fatigue and creep shorten life below the static strength? | Chapter 14 |
| How do time and temperature change polymer stiffness (viscoelasticity)? | Chapters 14 and 21 |
| How does rubber elasticity follow from chain statistics? | Chapter 20 |
| How are the stiffnesses of fibre composites and laminates built from their constituents? | Chapters 22 and 23 |
| How are concrete strength classes, structural-steel grades and timber stiffness specified? | Chapter 18 |
| How are mechanical tests performed at small scales and with what uncertainty? | Chapters 42 and 44 |
| How are tensor properties and Neumann's principle defined? | Chapter 4 (back reference) |
| How are modulus, strength and density combined to select materials? | Chapter 48 |

**Next:** Chapter 12 asks why real crystals yield at stresses thousands of times below the strength of their bonds, and finds the answer in the dislocation — its stress field, the forces on it, and how it moves, multiplies and interacts.
