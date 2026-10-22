# Chapter 30 — Nanomaterials and Two-Dimensional Materials

*Part VII · Advanced and Emerging Materials*

A car tyre made in 1910 was white, wore out in a few thousand kilometres and cracked in sunlight. Within two decades every tyre in the world was black, because manufacturers had learned that adding about 30 % by mass of carbon black, a soot of fused carbon particles 20–80 nm across, raised the tread's abrasion resistance several-fold and its tear strength and UV resistance with it. Carbon black is still the largest-tonnage nanomaterial made, at over 10 million tonnes a year, and nobody called it "nano" for most of its history. Today the same length scale appears everywhere: in the 1–2 nm platinum particles that carry the catalysis in a fuel cell and a catalytic converter, the 20 nm copper lines whose resistivity is three times the handbook value, the cadmium-free quantum dots whose diameter sets the colour of a television pixel, the electrodeposited nickel with 15 nm grains that is five times harder than ordinary nickel, and the few-layer graphene platelets now blended into concrete, coatings and battery electrodes. In each case a property has stopped being a property of the substance alone and has become a property of its **size**. This chapter asks when that happens, why, and what engineering can and cannot do with it.

> **At what size does a material stop behaving like its bulk self, and which properties change first?**
> **What do nanoparticles, nanotubes, graphene and nanocrystalline metals offer engineers, how are they made and measured, and why are they mostly used as additives rather than as stand-alone materials?**

| Concept | Engineering destination |
|---|---|
| Surface-to-volume ratio, specific surface area | Catalysts, sorbents, battery electrodes, sintering of nanopowders and printed inks |
| Melting-point depression (Gibbs–Thomson) | Low-temperature sintering of silver and copper pastes, nanoparticle stability in catalysts |
| Mean-free-path size effects | Interconnect resistivity, thermal conductivity of nanostructured thermoelectrics |
| Quantum confinement, Brus equation | Quantum-dot displays and lighting, bio-imaging labels, photodetectors |
| Carbon nanotubes, chirality | Conductive additives in Li-ion electrodes, composites, field emitters |
| Graphene and other 2D materials | Barrier coatings, heat spreaders, transparent electrodes, membranes, ultrathin transistors |
| Nanocrystalline metals, inverse Hall–Petch | Wear-resistant electrodeposited coatings, high-strength conductors, MEMS |
| Nanocomposites, percolation, tortuosity | Antistatic plastics, gas-barrier packaging, low-rolling-resistance tyres |
| Top-down and bottom-up synthesis | Choosing a route that delivers the size, purity and tonnage needed |
| Nano-characterization and safety | Quality control, occupational exposure limits, regulation of nanoforms |

**Roadmap.** Why size changes properties: surfaces, melting and transport (30.1) → confinement of electrons (30.2) → zero- and one-dimensional objects: nanoparticles, quantum dots, nanowires and nanotubes (30.3) → two-dimensional materials (30.4) → nanostructured bulk: nanocrystalline metals (30.5) and nanocomposites (30.6) → how nanomaterials are made (30.7) → how they are measured and handled safely (30.8).

> **Boundary.** Quantum confinement is treated here with the particle-in-a-box and effective-mass models of Chapter 26, as a materials phenomenon; rigorous quantum mechanics belongs to Engineering Physics. The electronic-device side of nanomaterials (nanosheet and 2D-channel transistors, interconnect scaling, quantum-dot lasers) is treated in more depth in the separate Materials Core (EEE) book.

---

## 30.1 Size effects in classical materials science

### 30.1.1 Two ways size enters

Size changes material behaviour through two different mechanisms, which it helps to keep apart:

1. **Classical size effects.** The fraction of atoms at a surface or interface becomes significant, or the object becomes smaller than a characteristic length of some process: the mean free path of electrons or phonons, the spacing of dislocation sources, a magnetic domain-wall width, the critical nucleus size. No quantum mechanics beyond that already in the bulk material is needed.
2. **Quantum size effects.** The object becomes comparable to the de Broglie wavelength of its electrons (or the radius of its excitons), and their allowed energies become discrete. This is quantum confinement (Section 30.2).

Classical effects typically appear below about 100 nm. Quantum effects appear in semiconductors below about 10–20 nm, but in metals only below about 2 nm, because electrons at the Fermi level of a metal have wavelengths of about 0.5 nm. A **nanomaterial** is conventionally one with at least one external dimension, or an internal structure, between 1 and 100 nm; the European Union's regulatory definition counts a material as nano if at least half of its particles by number have one or more external dimensions in that range. The boundaries are conventions; what matters physically is which characteristic length the structure has passed below.

### 30.1.2 Surface-to-volume ratio

For a sphere of diameter $d$ the surface-to-volume ratio is $A/V=6/d$. Dividing by density gives the **specific surface area** (SSA), the surface per unit mass, which is the number that matters for catalysts, adsorbents and electrodes:

$$
\mathrm{SSA}=\frac{6}{\rho\,d}
$$

> **Status of the principle: Surface-to-volume scaling, $A/V=6/d$**
> *Derived.* Pure geometry for spheres (and, with a different constant, for any fixed shape); real powders deviate because of polydispersity, agglomeration, necks and internal porosity, which is why measured gas-adsorption areas are usually lower than the geometric estimate.

**Worked example — what fraction of atoms is at the surface?** Treat the outer shell of thickness $t\approx0.25$ nm (about one atomic layer) as surface. The fraction of the volume in that shell is

$$
f_s=1-\left(1-\frac{2t}{d}\right)^3
$$

which gives 1.5 % for $d=100$ nm, 7.3 % at 20 nm, 14 % at 10 nm, 27 % at 5 nm and 58 % at 2 nm. The specific surface area of 5 nm gold particles ($\rho=19\,300$ kg/m³) is $6/(19\,300\times5\times10^{-9})=6.2\times10^{4}$ m²/kg, that is 62 m²/g, and of 21 nm titania ($\rho=4230$ kg/m³) about 68 m²/g; the commercial titania photocatalyst made of particles that size measures about 50 m²/g by gas adsorption, because the particles are fused into aggregates. A single gram of a 2 nm platinum catalyst exposes more than 100 m², and since only surface atoms do catalysis, this is why fuel-cell and automotive catalysts are dispersed as 1–5 nm particles on porous carbon or alumina supports, and why their slow coarsening in service (Ostwald ripening, Chapter 10) is a principal cause of catalyst ageing.

<!-- FIGURE 30.1 | figures/ch30/fig-30-1-surface-fraction-melting.png | plot | As particles shrink below about 20 nm, the fraction of surface atoms rises steeply and the melting point falls below its bulk value. | Content: log x-axis particle diameter 1-1000 nm. Left y-axis: fraction of atoms in a 0.25 nm surface shell (0-1), curve f = 1-(1-0.5/d)^3 with points labelled at 2 nm (0.58), 5 nm (0.27), 10 nm (0.14), 20 nm (0.073), 100 nm (0.015). Right y-axis: melting temperature of Au (K, 600-1400), Gibbs-Thomson curve Tm = 1337(1 - 2 x 0.27/(1.23e9 x r)) giving 1220 K at 10 nm, 1102 K at 5 nm, 867 K at 2.5 nm; schematic experimental points lying close to the curve above 5 nm and below it at 2-3 nm (around 600-700 K). Bulk Tm = 1337 K dashed. Shade the 1-10 nm region "surface dominated". -->

### 30.1.3 Melting-point depression

Atoms at a surface have fewer neighbours, so a small particle has a higher Gibbs energy per atom than bulk solid. The same is true of a small liquid droplet, but the solid–liquid interface energy $\sigma_{sl}$ is what matters for melting: a solid sphere of radius $r$ inside its own melt is in equilibrium at a lower temperature than a flat interface. Applying the Gibbs–Thomson relation of Chapter 6:

$$
\frac{T_m(r)}{T_{m,\mathrm{bulk}}}\approx1-\frac{2\sigma_{sl}}{\Delta H_v\,r}
$$

where $\Delta H_v$ is the latent heat of fusion per unit volume.

> **Status of the principle: Gibbs–Thomson melting-point depression**
> *Approximate.* Continuum thermodynamics with a size-independent interface energy; it captures the $1/r$ trend down to a few nanometres, but below about 3 nm interface energies, surface pre-melting and structural changes (icosahedral clusters) make the measured depression larger.

**Worked example — gold nanoparticles.** For gold, $T_{m,\mathrm{bulk}}=1337$ K, the latent heat is 12.55 kJ/mol and the molar volume $10.2\times10^{-6}$ m³/mol, so $\Delta H_v=1.23\times10^{9}$ J/m³; take $\sigma_{sl}\approx0.27$ J/m². For a 5 nm particle ($r=2.5$ nm), $2\sigma_{sl}/(\Delta H_v r)=0.54/(1.23\times10^{9}\times2.5\times10^{-9})=0.176$, so $T_m\approx1337\times0.824=1102$ K, 235 K below bulk. At 10 nm the depression is about 120 K (1220 K), and at 2.5 nm the formula gives 867 K, while experiments find even lower values, near 600–700 K, as the status box warns (Figure 30.1).

The same physics lowers the **sintering temperature** of nanopowders. Silver nanoparticle pastes sinter into conductive joints at 200–250 °C, far below silver's melting point of 962 °C, which is how power-electronic die attach and printed conductive tracks on polymer films are made; nanocrystalline ceramic powders densify several hundred kelvin lower than micrometre powders. The driving force that makes nanopowders useful also makes them unstable: they agglomerate, coarsen and, for reactive metals, oxidise or even ignite spontaneously, so nano-aluminium and nano-iron are handled under inert gas.

### 30.1.4 Mean-free-path and characteristic-length effects

When a structure is smaller than the distance a carrier travels between scattering events, the boundaries add scattering:

- **Electrons in metals.** The electron mean free path in bulk copper at room temperature is about 39 nm. In interconnect lines 20 nm wide, surface and grain-boundary scattering raise the resistivity from 1.7 to about 4–6 µΩ cm (Chapter 25), which is driving the search for alternative interconnect metals with shorter mean free paths, such as ruthenium and molybdenum.
- **Phonons in insulators and semiconductors.** Phonon mean free paths are spread from nanometres to micrometres; nanostructuring (grain boundaries, nanoprecipitates) scatters the long-wavelength phonons that carry much of the heat, cutting thermal conductivity while leaving electrical conductivity less affected, which is the basis of modern nanostructured thermoelectrics (Chapter 32). Silicon nanowires 50 nm across conduct heat about five times worse than bulk silicon (Chapter 24).
- **Dislocations in metals.** Below about 100 nm, grains are too small to contain dislocation sources and pile-ups, which changes the strengthening law (Section 30.5).
- **Magnetic domains.** Below a critical size of tens of nanometres a magnetic particle is a single domain, and below about 10 nm thermal energy can flip its magnetization (superparamagnetism, Chapter 27), the limit for magnetic recording grains and the basis of magnetic nanoparticle contrast agents and ferrofluids.
- **Light.** Particles much smaller than the wavelength scatter weakly (Rayleigh scattering varies as $d^6/\lambda^4$), so 20–50 nm titania and zinc oxide in sunscreens absorb UV yet look transparent, whereas pigmentary 250 nm titania is a white scatterer. Metal nanoparticles show **surface plasmon resonances**: collective oscillation of their conduction electrons gives 20 nm gold particles a strong absorption near 520 nm and a ruby colour, used since Roman times in glass and today in lateral-flow (pregnancy and rapid antigen) test strips.

---

## 30.2 Quantum confinement as a materials phenomenon

### 30.2.1 When does confinement matter?

An electron in a semiconductor crystal behaves as a free particle with an **effective mass** $m^*$ (Chapter 26). Confining it to a box of size $L$ raises its lowest energy by roughly the particle-in-a-box value

$$
\Delta E\approx\frac{\hbar^2\pi^2}{2m^*L^2}
$$

This matters when $\Delta E$ is comparable to or larger than $k_BT$ (25.7 meV at 25 °C) and to the energy scale of interest. Small effective mass and small $L$ give large confinement. For GaAs ($m^*=0.067\,m_e$) a 10 nm layer raises the electron energy by about 56 meV, which is why quantum wells of that thickness define the emission wavelength of semiconductor lasers. A second length scale is the **exciton Bohr radius**, the size of the bound electron–hole pair created by light: about 5.6 nm in CdSe, 10 nm in InP, 18 nm in PbS. When a crystal is smaller than this, the exciton is squeezed and its energy rises.

### 30.2.2 Dimensionality and the density of states

Confinement in one, two or three directions gives quantum wells (2D: free motion in a plane), quantum wires (1D) and quantum dots (0D). The electronic density of states changes shape accordingly: the square-root continuum of a bulk crystal becomes a staircase in a well, a series of $1/\sqrt{E}$ spikes in a wire and a set of discrete, atom-like levels in a dot (Figure 30.2a). Concentrating states at particular energies is what makes quantum-well lasers more efficient and quantum dots emit narrow spectral lines.

### 30.2.3 The Brus equation for quantum dots

For a spherical dot of radius $R$, the lowest excitation energy in the effective-mass approximation (Brus, 1984) is

$$
E(R)\approx E_g+\frac{\hbar^2\pi^2}{2R^2}\left(\frac{1}{m_e^*}+\frac{1}{m_h^*}\right)-\frac{1.786\,e^2}{4\pi\varepsilon_0\varepsilon_rR}
$$

The second term is the confinement of electron and hole and grows as $1/R^2$; the third is their Coulomb attraction, screened by the dot's permittivity, which grows only as $1/R$. At small $R$ confinement wins, and the dot's absorption and emission shift to the blue as it shrinks.

> **Status of the principle: Brus equation**
> *Approximate.* Effective-mass, infinite-barrier model with parabolic bands; it gives the correct trend and order of magnitude, but overestimates the shift below about 3 nm, where band non-parabolicity, finite barriers and surface states matter. Engineering design uses measured sizing curves.

**Worked example — the colour of a CdSe quantum dot.** For CdSe take $E_g=1.74$ eV, $m_e^*=0.13\,m_e$, $m_h^*=0.45\,m_e$, $\varepsilon_r=10.6$, and the constants $\hbar^2\pi^2/2m_e=0.376$ eV nm² and $e^2/4\pi\varepsilon_0=1.440$ eV nm. For a dot of diameter 5 nm ($R=2.5$ nm):

$$
\Delta E_{\mathrm{conf}}=\frac{0.376}{2.5^2}\left(\frac{1}{0.13}+\frac{1}{0.45}\right)=0.0602\times9.91=0.596\ \mathrm{eV}
$$

$$
\Delta E_{\mathrm{Coul}}=\frac{1.786\times1.440}{10.6\times2.5}=0.097\ \mathrm{eV}
$$

so $E\approx1.74+0.596-0.097=2.24$ eV, a wavelength of $1239.8/2.24=554$ nm (green). The measured first-exciton energy of 5 nm CdSe dots is about 2.1 eV (590 nm, orange-yellow): the model overestimates the shift, as expected. At 7 nm the formula gives 1.97 eV (628 nm), at 4 nm 2.55 eV (486 nm). One composition therefore spans the visible simply by size, and a synthesis that controls diameter to ±5 % sets the colour to within about ±10 nm.

<!-- FIGURE 30.2 | figures/ch30/fig-30-2-dos-dimensionality-qd-colour.png | plot | Confinement reshapes the density of states from a continuum in bulk to steps, spikes and discrete levels, and tunes the emission of quantum dots with their size. | Content: (a) four small panels of g(E) vs E: 3D (square-root curve), 2D (staircase), 1D (1/sqrt spikes), 0D (delta lines), each with a sketch (cube, slab, wire, dot). (b) Emission energy (eV, 1.7-3.0) vs CdSe dot diameter (2.5-8 nm): Brus-equation curve (solid; 2.55 eV at 4 nm, 2.24 eV at 5 nm, 1.97 eV at 7 nm) and representative experimental first-exciton energies (points: about 2.5 eV at 2.5 nm, 2.1 eV at 5 nm, 1.95 eV at 7 nm); bulk gap 1.74 eV dashed; colour bar along right axis from red to blue. -->

---

## 30.3 Nanoparticles, quantum dots, nanowires and nanotubes

### 30.3.1 Nanoparticles

Zero-dimensional nanomaterials are by far the most used, mostly as additives:

| Nanoparticle | Typical size | Use and the property exploited |
|---|---|---|
| Carbon black | 20–80 nm primary, fused aggregates | Tyre reinforcement, pigment, conductive filler |
| Fumed (pyrogenic) silica | 7–40 nm primary | Thickener, anti-settling agent, tyre filler, insulation |
| Titania, zinc oxide | 20–50 nm | Transparent UV filters, photocatalytic self-cleaning glass |
| Pt, Pd, Rh on supports | 1–5 nm | Fuel-cell, automotive and chemical catalysts |
| Silver | 10–100 nm | Antimicrobial coatings, sintered die attach, printed conductors |
| Ceria | 5–50 nm | Chemical–mechanical polishing slurries, fuel additives, catalysts |
| Iron oxide | 5–20 nm | MRI contrast, ferrofluids, magnetic separation |
| Gold | 2–50 nm | Diagnostics (plasmonic colour), catalysis |

Colloidal nanoparticles are stabilised against aggregation by the charge, steric and ligand mechanisms of Chapter 29; gas-phase products such as carbon black and fumed silica are deliberately aggregated into branched, chain-like clusters, which is what lets them build networks in rubber and liquids.

### 30.3.2 Quantum dots

Commercial quantum dots are core–shell crystals made by colloidal synthesis (Section 30.7): an emitting core (CdSe, or cadmium-free InP or perovskite CsPbBr₃) coated with a few monolayers of a wider-gap shell (ZnS, ZnSe) that passivates surface dangling bonds, which would otherwise trap carriers and quench emission, and capped with organic ligands for solubility. Photoluminescence quantum yields above 90 % and emission linewidths of 20–35 nm make them ideal colour converters: in quantum-dot displays a blue LED backlight excites red and green dots in a film, giving a wider colour gamut than phosphors. They are also used as fluorescent labels in biology, where their brightness and photostability beat organic dyes, and are studied for solar cells and infrared detectors (PbS dots). Cadmium toxicity has pushed displays towards InP under the EU's hazardous-substance rules.

### 30.3.3 Nanowires

Nanowires have one long free dimension and diameters of 5–200 nm. Semiconductor nanowires (Si, Ge, GaN, ZnO, InP) are grown mostly by the **vapour–liquid–solid** (VLS) mechanism: a gold or other catalyst droplet dissolves vapour-phase precursor, becomes supersaturated and precipitates a single-crystal wire beneath it, so wire diameter follows droplet diameter. Their uses exploit geometry: a wire relaxes lattice-mismatch strain sideways, so heterostructures impossible in films can be grown (nanowire LEDs and solar cells); silicon nanowires and nanostructured silicon accommodate the 300 % volume expansion of lithiation without pulverising, which motivates silicon-rich battery anodes (Chapter 32); and the enormous surface sensitivity of a thin wire makes it a chemical or biological sensor. Metal nanowires (silver, copper) of high aspect ratio form percolating transparent conducting films, a flexible alternative to indium tin oxide.

### 30.3.4 Carbon nanotubes

A single-walled carbon nanotube (SWCNT) is a graphene sheet (Section 30.4) rolled into a seamless cylinder about 1 nm in diameter and up to millimetres long; multi-walled tubes (MWCNTs) are several such cylinders nested with the 0.34 nm graphite interlayer spacing, outer diameters 5–50 nm. How the sheet is rolled is given by the **chiral vector** $\mathbf{C}_h=n\mathbf{a}_1+m\mathbf{a}_2$ on the graphene lattice (Figure 30.3), which becomes the tube's circumference. The diameter follows directly:

$$
d=\frac{a\sqrt{n^2+nm+m^2}}{\pi},\qquad a=0.246\ \mathrm{nm}
$$

Tubes with $m=0$ are **zigzag**, $n=m$ are **armchair**, all others are **chiral**. Rolling quantises the electron wavevector around the circumference, and whether the allowed wavevectors pass through graphene's Dirac points (Section 30.4) decides the electrical character: a tube is metallic if $(n-m)$ is divisible by 3 and semiconducting otherwise, with a band gap $E_g\approx0.8\ \mathrm{eV}/d(\mathrm{nm})$.

> **Status of the principle: The $(n-m)\ \mathrm{mod}\ 3$ rule**
> *Approximate.* Derived from zone-folding of graphene's band structure; curvature opens small gaps (meV to tens of meV) in non-armchair "metallic" tubes, and only armchair tubes are truly metallic.

**Worked example — three tubes.** A (10,10) armchair tube has $d=0.246\sqrt{300}/\pi=1.36$ nm and $n-m=0$: metallic. A (10,0) zigzag tube has $d=0.783$ nm and $n-m=10$, not divisible by 3: semiconducting with $E_g\approx0.8/0.78\approx1.0$ eV. A (13,0) tube has $d=1.02$ nm and is semiconducting with $E_g\approx0.8$ eV. Since synthesis produces a statistical mixture, about one third of tubes are metallic, which is fatal for transistors (separation by density-gradient centrifugation or selective polymer wrapping is needed) but irrelevant for the main markets.

<!-- FIGURE 30.3 | figures/ch30/fig-30-3-cnt-chiral-map.png | schematic | The chiral vector (n,m) on the graphene lattice fixes a nanotube's diameter, chiral angle and whether it is metallic or semiconducting. | Content: (a) honeycomb lattice with unit vectors a1, a2 (a = 0.246 nm) from an origin; chiral vector C_h for (4,2) and the perpendicular translation vector T; zigzag (theta = 0) and armchair (theta = 30 deg) directions marked. (b) Map of lattice points (n,m) for 0 <= m <= n <= 12 as small hexagons: metallic ((n-m) mod 3 = 0) filled dark, semiconducting open; label (10,0) d = 0.78 nm, (13,0) d = 1.02 nm, (10,10) d = 1.36 nm. (c) Three short tube sketches: zigzag, armchair, chiral. -->

Individual nanotubes have extraordinary properties: Young's modulus about 1 TPa, tensile strength of tens of GPa measured on defect-free tubes, axial thermal conductivity of about 3000 W m⁻¹ K⁻¹, current densities above $10^{9}$ A/cm² (a thousand times copper's electromigration limit). Bulk products capture only a fraction of this, because load and current must pass between tubes through weak van der Waals contacts: CNT yarns and sheets reach 1–5 GPa strength and $10^{6}$ S/m conductivity at best. The largest market is therefore as a **conductive additive**: about 0.5–2 wt% of MWCNTs or SWCNTs in lithium-ion cathodes and silicon-containing anodes replaces several times more carbon black, freeing volume for active material; smaller markets are antistatic plastics (fuel lines, electronics trays), conductive coatings and sporting goods. Boron nitride nanotubes, insulating and stable to about 900 °C in air, and natural halloysite clay nanotubes are related one-dimensional fillers.

---

## 30.4 Graphene and other two-dimensional materials

### 30.4.1 Graphene

**Graphene** is a single layer of sp²-bonded carbon atoms in a honeycomb lattice, with C–C bond length 0.142 nm and lattice constant 0.246 nm; stacking layers at 0.335 nm gives graphite. It was isolated in 2004 by peeling graphite with adhesive tape and identifying monolayers optically on oxidised silicon, the work recognised by the 2010 Nobel Prize in Physics.

Its electronic structure is unusual. The conduction and valence bands touch at the six corners ($K$ points) of the hexagonal Brillouin zone, and near them the energy is linear in wavevector, $E=\pm\hbar v_F\lvert\mathbf{k}\rvert$ with $v_F\approx1\times10^{6}$ m/s: a **Dirac cone**, so electrons behave as massless particles. Graphene is a zero-gap semimetal whose carrier type and density are set by a gate field or by chemical doping. That gives very high mobility (above $10^{5}$ cm² V⁻¹ s⁻¹ in clean, h-BN-encapsulated samples, $10^{3}$–$10^{4}$ on SiO₂), but no off-state for digital logic, which is why graphene has not replaced silicon in transistors.

Its other properties (Table 30.1) explain where it *is* used. One atom thick and with the in-plane covalent bond of graphite, it has a Young's modulus of about 1 TPa and an intrinsic strength of about 130 GPa (measured by nanoindentation of suspended membranes), the strongest material known. It absorbs 2.3 % of visible light per layer (the value $\pi\alpha$, with $\alpha$ the fine-structure constant), so a monolayer is nearly transparent yet conductive. It is impermeable to gases, even helium, in perfect form. Its theoretical specific surface area, with both faces counted, is

$$
\mathrm{SSA}=\frac{2\times A_{\mathrm{cell}}}{2m_{\mathrm{C}}}=\frac{2\times0.0524\ \mathrm{nm^2}}{2\times1.994\times10^{-23}\ \mathrm{g}}\approx2630\ \mathrm{m^2/g}
$$

(the unit cell of area $\sqrt3a^2/2=0.0524$ nm² contains two carbon atoms), which makes it a candidate for supercapacitor electrodes (Chapter 32), though restacking of sheets loses most of that area.

**Table 30.1 — Properties of graphene and benchmarks (typical; monolayer values are for high-quality samples)**

| Property | Graphene | Benchmark |
|---|---|---|
| Young's modulus | ~1.0 TPa | Steel 200 GPa; CFRP ply 130–180 GPa |
| Intrinsic tensile strength | ~130 GPa | High-strength steel ~2 GPa; carbon fibre 3–7 GPa |
| Thermal conductivity (suspended, room T) | 2000–5000 W m⁻¹ K⁻¹ | Copper 400; diamond 2000 |
| Carrier mobility (room T) | $10^{4}$–$10^{5}$ cm² V⁻¹ s⁻¹ | Silicon electrons ~1400 |
| Optical absorption per layer | 2.3 % | ITO film ~10 % at similar sheet resistance |
| Sheet resistance (CVD, doped) | 100–500 Ω/sq | ITO 10–100 Ω/sq |
| Specific surface area | ~2630 m²/g | Activated carbon 1000–3000 m²/g |

In practice "graphene" sold by the tonne is something else: **few-layer graphene** and **graphene nanoplatelets** (5–100 layers) made by liquid-phase exfoliation of graphite, and **graphene oxide** (GO), a heavily oxidised, insulating, water-dispersible sheet made by chemical oxidation, partly reconverted to conductive **reduced graphene oxide** (rGO). These platelets are used as additives: in anticorrosion and barrier coatings, heat-spreading films in smartphones (actually graphitised polyimide or graphene-laminate films with in-plane conductivities of 1000–1900 W m⁻¹ K⁻¹), conductive inks, battery electrodes and as reinforcement in concrete and polymers. Continuous monolayer films are grown by chemical vapour deposition on copper foil (Section 30.7) and transferred, for sensors, transparent electrodes and research devices; transfer damage, wrinkles and grain boundaries make large-area quality the persistent problem.

### 30.4.2 Beyond graphene

Graphene opened a family of layered crystals that can be thinned to one or a few layers (Figure 30.4):

- **Hexagonal boron nitride (h-BN)**, "white graphene", is isostructural with graphene but has alternating B and N, a band gap near 6 eV, and an atomically flat, charge-trap-free surface. It is the ideal insulating substrate and encapsulant for other 2D materials, and bulk h-BN powder is a high-temperature lubricant and thermally conductive, electrically insulating filler.
- **Transition-metal dichalcogenides (TMDs)**, MX₂ with M = Mo, W and X = S, Se, Te: a metal layer sandwiched between two chalcogen layers. MoS₂ has an indirect gap of about 1.2–1.3 eV in bulk that becomes a direct gap of about 1.8–1.9 eV in a monolayer, so monolayers luminesce strongly; WSe₂ and MoTe₂ give other gaps. They are the leading candidates for transistor channels thinner than silicon can be made, and bulk MoS₂ has long been a solid lubricant for vacuum and aerospace mechanisms.
- **Phosphorene** (black phosphorus) has a puckered structure, a direct gap that rises from about 0.3 eV in bulk to about 1.5–2 eV in a monolayer, and strong in-plane anisotropy; it degrades rapidly in air unless encapsulated.
- **MXenes**, such as Ti₃C₂T$_x$, are made by etching the A-layer out of MAX-phase ceramics (Ti₃AlC₂), leaving metallic carbide or nitride sheets terminated by –O, –OH and –F groups ($T_x$). They combine metallic conductivity (up to about $10^{4}$ S/cm) with hydrophilicity, so they can be processed from water into films for electromagnetic-interference shielding, supercapacitor electrodes and conductive inks.
- **Van der Waals heterostructures** stack different 2D crystals (graphene, h-BN, TMDs) like Lego; because layers bond by van der Waals forces, lattice matching is unnecessary. Twisting two graphene layers to the "magic angle" of about 1.1° even produces superconductivity, an example of designing properties by stacking geometry alone.

<!-- FIGURE 30.4 | figures/ch30/fig-30-4-2d-materials-family.png | schematic | The two-dimensional materials family spans metals, semimetals, semiconductors and insulators, with band gaps from zero to about 6 eV. | Content: top row: ball-and-stick top and side views of graphene, h-BN, MoS2 (Mo between two S layers), black phosphorus (puckered), Ti3C2Tx (Ti-C-Ti-C-Ti with surface terminations). Bottom: horizontal band-gap ladder 0-6 eV placing graphene (0, semimetal, Dirac cone icon), MXene (metal), phosphorene (bar 0.3 bulk to ~1.8 mono), MoS2 (bar 1.25 bulk indirect to 1.9 mono direct), WSe2 (~1.65), h-BN (~6.0); colour code metal/semimetal/semiconductor/insulator; overlay visible-spectrum band 1.65-3.1 eV. -->

---

## 30.5 Nanocrystalline metals

### 30.5.1 Extrapolating Hall–Petch

Grain boundaries obstruct dislocations, and Chapter 13 derived the Hall–Petch relation from dislocation pile-ups:

$$
\sigma_y=\sigma_0+k_y\,d^{-1/2}
$$

Since strength rises without limit as $d\to0$ in this formula, it is natural to ask how strong a metal with nanometre grains can be. **Nanocrystalline** metals, with grain sizes below 100 nm (and *ultrafine-grained* metals at 100–1000 nm), test the question.

**Worked example — how strong could nanocrystalline copper be?** Take $\sigma_0=25$ MPa and $k_y=0.11$ MPa m^1/2 for copper. Hall–Petch predicts 60 MPa at $d=10$ µm, 135 MPa at 1 µm, $25+0.11/\sqrt{10^{-7}}=373$ MPa at 100 nm, 803 MPa at 20 nm and 1125 MPa at 10 nm. Measured yield strengths of fully dense nanocrystalline copper follow the line down to roughly 20–30 nm, reaching about 0.8–1 GPa, five to ten times annealed copper, but below about 10–15 nm strength stops rising and then falls (Figure 30.5). Extrapolation to 5 nm (1.58 GPa) would be badly wrong.

> **Status of the principle: Hall–Petch relation at the nanoscale**
> *Empirical.* Valid from coarse grains down to a few tens of nanometres; it fails below about 10–20 nm, where grains are too small to support pile-ups and grain-boundary-mediated deformation takes over.

### 30.5.2 The inverse Hall–Petch regime

The breakdown has a physical reason. A pile-up needs room: a grain of 10 nm can hold only one or two dislocations, and the Frank–Read sources of Chapter 12 need a pinned segment that cannot fit. Instead, dislocations are emitted from grain boundaries, cross the grain and are absorbed at the opposite boundary. As grains shrink further, the volume fraction of grain-boundary material approaches that of the grain interiors (the surface-fraction arithmetic of Section 30.1 applies to grain boundaries too), and deformation shifts to **grain-boundary sliding**, grain rotation and diffusion along boundaries, mechanisms that become easier, not harder, as grains shrink. Molecular-dynamics simulations (Chapter 46) and experiments place the strength maximum near 10–15 nm for copper and nickel. Below it, softening (the **inverse Hall–Petch** effect) is observed, though early reports of it were complicated by porosity and impurities in the samples.

<!-- FIGURE 30.5 | figures/ch30/fig-30-5-hall-petch-inverse.png | plot | Strength of copper rises with the inverse square root of grain size down to a few tens of nanometres, then saturates and falls in the inverse Hall-Petch regime. | Content: x-axis d^(-1/2) in m^(-1/2) from 0 to 15000 (top axis labelled with grain sizes 10 um, 1 um, 100 nm, 20 nm, 10 nm, 5 nm), y-axis yield strength 0-1600 MPa. Straight Hall-Petch line sigma = 25 + 0.11 d^(-1/2) MPa (60 MPa at 10 um, 135 at 1 um, 373 at 100 nm, 803 at 20 nm, 1125 at 10 nm, 1581 at 5 nm), dashed beyond 20 nm. Schematic experimental band following the line to ~25 nm, peaking at ~0.9-1.0 GPa near 10-15 nm, then falling. Shaded zones: "pile-up regime", "boundary-emitted dislocations", "grain-boundary sliding / inverse Hall-Petch". Point for nanotwinned Cu (~0.9 GPa) labelled. -->

### 30.5.3 Stability, ductility and practical nanocrystalline metals

Two problems limit bulk use. **Thermal stability**: the grain-boundary energy per unit volume is enormous, so nanocrystalline grains coarsen readily, in pure copper and aluminium even near room temperature. Stabilisation comes from solute segregation to boundaries, which lowers boundary energy (Ni–W, Cu–Ta, Fe–Zr), and from Zener pinning by fine particles (Chapter 10), as in oxide-dispersion-strengthened steels for reactor cladding (Chapter 33). **Ductility**: with no room for dislocation storage, nanocrystalline metals work-harden little, neck early and often show only a few percent uniform elongation.

**Nanotwinned** copper offers a way round. Pulsed electrodeposition can produce grains of 400–500 nm containing growth twins spaced 15–50 nm apart. Twin boundaries block dislocations like grain boundaries do, giving strength near 0.9–1 GPa, but because they are coherent, low-energy boundaries they scatter electrons very weakly, and the conductivity stays near 95 % of annealed copper, whereas ordinary nanocrystalline copper loses much more. They also allow dislocations to slip along them, which preserves some ductility.

Practical nanocrystalline metals are made in forms that do not need large bulk sections. Electrodeposited nanocrystalline nickel and nickel–tungsten or cobalt–phosphorus alloys, with grains of 10–20 nm and hardness of 5–7 GPa (about five times that of conventional nickel), are wear coatings that replace hard chromium plating, whose hexavalent-chromium chemistry is being phased out. Severe plastic deformation (Section 30.7) produces ultrafine-grained titanium for dental implants (Chapter 31) and aluminium for high-strength wires. Nanocrystalline soft magnetic alloys (Fe–Si–B–Nb–Cu, Chapter 27), with 10 nm grains in an amorphous matrix, owe their very low coercivity to grains smaller than the magnetic exchange length, another case where a characteristic length decides the effect.

---

## 30.6 Nanocomposites

Most nanomaterials reach products as fillers in a matrix. A nanocomposite differs from the conventional composites of Chapter 22 in two ways that follow from size. First, at the same volume fraction the filler has orders of magnitude more interface with the matrix, so a few percent of filler can change properties that a conventional filler changes only at 20–50 %. Second, nanoscale fillers are too small to scatter light, to act as strength-limiting flaws or to roughen a surface, so properties can be added without the usual penalties. The difficulty is that their high surface energy makes them aggregate, and an agglomerated nanofiller behaves like a poor micro-filler. Dispersion and interface chemistry decide success.

### 30.6.1 Mechanical reinforcement

The first commercial polymer nanocomposite, nylon 6 with about 4 wt% of exfoliated montmorillonite clay platelets (1 nm thick, 100–500 nm across), was developed by Toyota around 1990 for a timing-belt cover: the modulus roughly doubled and the heat-deflection temperature rose by about 80 K with no loss of density or processability. Clay, CNT and graphene stiffening follows the Halpin–Tsai estimates of Chapter 22 with the platelet or tube aspect ratio, provided the fillers are individually dispersed and bonded. **Silica** nanoparticles bonded to rubber with silane coupling agents lowered the rolling resistance of "green" passenger tyres by about 20 % while keeping wet grip, which is now standard practice; **nano-silica** and **rubber nanoparticles** toughen epoxy matrices for aerospace composites; dental restorative nanocomposites combine 20–75 nm silica and zirconia clusters with polymer resins to give polishable, wear-resistant fillings. In concrete, nano-silica accelerates hydration and densifies the C–S–H, and graphene-oxide additions of 0.01–0.05 % are marketed to reduce cement content.

### 30.6.2 Barrier properties

Impermeable platelets aligned in a film force a diffusing gas molecule to take a detour, increasing the path length. The **Nielsen** tortuosity model for platelets of aspect ratio $\alpha$ (width/thickness) at volume fraction $\phi$, aligned perpendicular to the diffusion direction, gives the ratio of composite to matrix permeability:

$$
\frac{P_c}{P_m}=\frac{1-\phi}{1+\dfrac{\alpha}{2}\phi}
$$

> **Status of the principle: Nielsen tortuosity model**
> *Approximate.* Assumes perfectly aligned, impermeable, uniformly spaced platelets and an unchanged matrix; misalignment and agglomeration reduce the benefit, while changes in matrix crystallinity or chain mobility near the filler can add to it.

**Worked example — a clay barrier film.** Adding 3 vol% clay platelets with aspect ratio 100 gives $P_c/P_m=0.97/(1+50\times0.03)=0.97/2.5=0.39$: the oxygen permeability falls by 61 %. At 5 vol% it falls to 0.27; with aspect ratio 300 at 3 vol%, to 0.18. The same reduction with a conventional filler would need far higher loadings and would cloud the film. Clay- and graphene-filled barrier layers are used in food and pharmaceutical packaging, in the inner liners of tyres (butyl rubber nanocomposites hold pressure longer) and in polymer fuel tanks and hydrogen-tank liners, where permeation of small molecules is a regulatory and safety issue.

### 30.6.3 Electrical and thermal percolation

A conducting filler in an insulating polymer forms a connected network above a **percolation threshold** $\phi_c$ (Chapter 25). For spheres $\phi_c\approx0.16$; for randomly oriented sticks of length $L$ and diameter $d$, excluded-volume arguments give $\phi_c\approx0.7\,d/L$. Nanotubes with $L/d=1000$ therefore percolate at about 0.07 vol%, roughly 0.1 wt%: some 200 times less filler than carbon black spheres need. In practice thresholds of 0.01–0.5 wt% are measured for well-dispersed tubes, rising to several percent if tubes bundle or break during mixing. Such loadings make plastics antistatic (surface resistivity $10^{6}$–$10^{9}$ Ω) for fuel systems, electronics packaging and mining equipment, without changing their mechanical behaviour. Thermal percolation is much weaker, because phonons do not tunnel efficiently across filler–filler contacts, so thermally conductive polymers still need 30–60 vol% of fillers such as h-BN or alumina (Chapter 24).

---

## 30.7 Synthesis: top-down and bottom-up

Nanomaterials are made either by carving or breaking bulk material (**top-down**) or by assembling atoms and molecules (**bottom-up**). Figure 30.6 and Table 30.2 summarise the routes.

### 30.7.1 Top-down routes

- **High-energy ball milling** fractures and cold-welds powders, producing nanocrystalline grains (10–30 nm) inside micrometre particles and mechanically alloying immiscible elements, as in ODS steels (Chapter 33). It is cheap and scalable but introduces contamination and wide size distributions.
- **Severe plastic deformation** imposes enormous strains without changing shape: **equal-channel angular pressing** (ECAP) pushes a billet repeatedly through a die with a 90° bend; **high-pressure torsion** twists a disc under several GPa. Grains refine to 100–300 nm (ECAP) or below 100 nm (HPT) in bulk, fully dense metal.
- **Lithography and etching**, the semiconductor industry's route, pattern features to below 20 nm with extreme-UV lithography (Chapter 41); electron-beam lithography is precise but slow.
- **Exfoliation** separates layered crystals: micromechanical cleavage (adhesive tape) for research-grade flakes, and **liquid-phase exfoliation** by ultrasound or shear mixing in solvents or surfactant solutions for tonnage graphene nanoplatelets and h-BN; chemical oxidation and exfoliation gives graphene oxide.

### 30.7.2 Bottom-up routes

- **Gas-phase synthesis.** Flame pyrolysis makes fumed silica (SiCl₄ burned in a hydrogen–oxygen flame), pigmentary and nano titania and carbon black, at millions of tonnes per year; laser ablation and spark discharge make research-scale metal nanoparticles.
- **Colloidal (wet-chemical) synthesis.** In the **hot-injection** method, precursors injected into a hot coordinating solvent nucleate in a short burst (a LaMer supersaturation spike, Chapter 9), after which growth without new nucleation gives size distributions of ±5 %, the basis of quantum-dot manufacture. Citrate reduction of gold salts, polyol synthesis of silver nanowires and co-precipitation of iron oxide are other examples.
- **Sol–gel and hydrothermal** routes make oxide nanoparticles, aerogels and coatings at low temperature (Chapter 41).
- **Chemical vapour deposition (CVD).** Hydrocarbons decompose on catalysts: on iron, cobalt or nickel nanoparticles they grow carbon nanotubes (fluidised-bed reactors make tonnes per year of MWCNTs); on copper foil at about 1000 °C, methane gives self-limiting monolayer graphene, because carbon is nearly insoluble in copper and growth stops once the surface is covered. VLS growth of nanowires is a CVD variant.
- **Atomic layer deposition** (ALD) builds films one atomic layer per cycle by self-limiting surface reactions, giving perfectly conformal nanometre coatings inside pores and on nanoparticles (Chapter 41).
- **Electrodeposition** with pulsed current and grain-refining additives yields nanocrystalline and nanotwinned metals directly.
- **Self-assembly** of block copolymers, surfactants and colloids (Chapter 29) builds ordered nanostructures and templates.

**Table 30.2 — Comparison of synthesis routes (indicative)**

| Route | Typical products | Size control | Throughput | Main limitation |
|---|---|---|---|---|
| Ball milling | Nanocrystalline powders, ODS alloys | Poor | High (tonnes) | Contamination, broad distribution |
| Severe plastic deformation | Bulk UFG metals | Moderate (100–300 nm) | Moderate | Size of billets, cost per kg |
| Lithography | Device features, patterned arrays | Excellent | High area, high cost | Capital cost, resolution limits |
| Liquid-phase exfoliation | Graphene and h-BN platelets | Poor in thickness | High | Defects, polydispersity |
| Flame pyrolysis | SiO₂, TiO₂, carbon black | Moderate | Very high (Mt/yr) | Aggregated particles |
| Hot-injection colloidal | Quantum dots, metal nanocrystals | Excellent (±5 %) | Low–moderate | Solvents, ligands, cost |
| CVD | CNTs, graphene films, nanowires | Good | Moderate | Transfer, catalyst residues |
| ALD | Conformal films, coatings | Atomic | Low (per layer) | Slow, precursor cost |
| Electrodeposition | Nanocrystalline coatings | Good | High | Conductive substrates only |

<!-- FIGURE 30.6 | figures/ch30/fig-30-6-synthesis-routes.png | flowchart | Top-down routes break or carve bulk material; bottom-up routes assemble atoms and molecules; the two meet in the 1-100 nm range. | Content: vertical log length-scale axis on the left from 0.1 nm (atoms) to 1 mm (bulk). Top half, arrows pointing down from "bulk material": ball milling (to 10-30 nm grains), severe plastic deformation (100-300 nm), lithography + etching (~10-20 nm), exfoliation (graphene flakes). Bottom half, arrows pointing up from "atoms/molecules": gas-phase pyrolysis (fumed silica, carbon black), hot-injection colloidal synthesis (quantum dots, +/-5 %), sol-gel, CVD on catalysts (CNT, graphene on Cu), VLS nanowires, ALD (atomic layers), electrodeposition (nc-Ni), self-assembly. Central shaded band 1-100 nm labelled "nanoscale". Small icons for each product. -->

---

## 30.8 Characterization and safety of nanomaterials

### 30.8.1 Seeing and measuring the nanoscale

No single method characterises a nanomaterial; several are combined (details in Chapters 42–44):

- **Transmission electron microscopy** images individual particles, tubes and grain boundaries at atomic resolution, and electron diffraction identifies phases; it samples only a tiny amount of material, so statistics need many images and automated analysis.
- **Scanning electron microscopy** shows morphology and agglomeration of powders and composites down to a few nanometres.
- **Atomic force microscopy** measures the thickness of 2D flakes (a graphene monolayer appears 0.3–1 nm high depending on substrate and adsorbates) and maps surface topography and mechanical properties.
- **X-ray diffraction** gives crystallite size from peak broadening (the Scherrer and Williamson–Hall analyses of Chapter 4) averaged over billions of crystals; small-angle X-ray scattering gives particle size distributions in dispersions.
- **Dynamic light scattering** measures the hydrodynamic diameter of particles in liquid from their Brownian motion, which includes ligand shells and reports agglomerates.
- **Gas adsorption (BET)** measures specific surface area, comparable with the $6/(\rho d)$ estimate of Section 30.1.
- **Raman spectroscopy** is the workhorse for carbon: the G band near 1580 cm⁻¹ (in-plane C–C stretching), the D band near 1350 cm⁻¹ (activated only by defects) and the 2D band near 2700 cm⁻¹, whose shape distinguishes monolayer from few-layer graphene. The D/G intensity ratio measures defect density, and radial breathing modes give nanotube diameters.
- **Optical spectroscopy**: the first-exciton absorption peak of quantum dots gives their size via sizing curves; the plasmon peak position and width of gold and silver particles report size and aggregation.

Reporting a nanomaterial properly means giving the size distribution (not just a mean), the method and its basis (number-, volume- or intensity-weighted), the state of agglomeration, the surface chemistry and the specific surface area. A "graphene" product should state layer number distribution, lateral size and oxygen content; surveys of commercial graphene have found many products to be mostly graphite.

### 30.8.2 Why nanomaterials raise safety questions

Risk is hazard multiplied by exposure, and nanomaterials raise both in specific ways:

- **Dose metric.** For poorly soluble particles, lung inflammation in animal studies correlates better with the *surface area* inhaled than with the mass, so the same mass of a nanopowder can be more toxic than its micrometre counterpart. Recommended exposure limits reflect this: NIOSH recommends 0.3 mg/m³ for ultrafine titania against 2.4 mg/m³ for fine titania.
- **Reactivity.** High surface area and surface defects can generate reactive oxygen species; soluble particles such as silver, zinc oxide and copper oxide release ions locally.
- **Translocation.** Particles below about 100 nm deposit efficiently in the deep lung, and a small fraction crosses into the blood; very small particles can reach other organs.
- **The fibre paradigm.** Long, thin, biopersistent fibres that macrophages cannot engulf (longer than about 15–20 µm) cause chronic inflammation, fibrosis and mesothelioma, as asbestos did. Long, rigid multi-walled carbon nanotubes behave this way in animal studies, and one type (MWNT-7) is classified as possibly carcinogenic to humans. NIOSH recommends an exposure limit of 1 µg/m³ for carbon nanotubes and nanofibres. Short, tangled or flexible tubes are much less hazardous.
- **Environment.** Nanoparticles released from products (silver from antimicrobial textiles during washing, titania from sunscreens and paints) enter waste-water and soils, where aggregation, dissolution and transformation (silver to silver sulfide) usually reduce toxicity, but the life-cycle fate is still being studied.

Exposure occurs mainly during manufacture and handling of dry powders, and during machining, sanding or burning of nanocomposites, rather than in using finished products, where the nanomaterial is bound in a matrix. Engineering control is therefore familiar industrial hygiene: handling dispersions or masterbatches instead of dry powder, enclosure and local exhaust ventilation, HEPA filtration (which captures nanoparticles very efficiently, because they diffuse to fibres), and respiratory protection. Regulation now treats nanoforms explicitly: since 2020 the EU REACH regulation requires registrants to characterise nanoforms separately, cosmetics containing nanomaterials must be notified and labelled "(nano)", and international standards (ISO/TR 12885 on occupational health and safety; ISO 80004 on vocabulary) define terms and practices. **Safe-by-design** asks the materials engineer to choose shapes, sizes, coatings and matrices that deliver the function at least hazard: shorter or tangled tubes, dissolvable or bound forms, surface coatings that suppress reactivity.

> **Status of the principle: Surface-area dose metric for nanoparticle toxicity**
> *Empirical.* Fitted to inhalation studies of poorly soluble, low-toxicity particles; it does not apply to soluble particles (where released ions dominate) or to fibres (where length and biopersistence dominate).

### 30.8.3 Why nanomaterials are mostly additives

Looking back over the chapter, a pattern emerges. Nanomaterials have succeeded where a small amount of a very fine phase changes a bulk property (carbon black, silica, CNT conductive additives, clay barriers, catalysts, pigments and UV filters), where size itself is the function (quantum-dot colour, plasmonic test strips) or where a thin layer is all that is needed (coatings, ALD films, electrodeposits). They have struggled where the outstanding property of an individual object (a nanotube's strength, graphene's mobility) must survive assembly into a macroscopic part, because the weak links between nano-objects, defects introduced during processing, and cost then dominate. The same structure–property logic that governs any material governs this one: a material is as good as its worst connection, and processing decides what the connections are.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How do surface energy and the Gibbs–Thomson effect follow from thermodynamics? | Chapter 6 |
| How do nucleation bursts and Ostwald ripening control particle size distributions? | Chapters 9 and 10 |
| How are dislocation pile-ups and Hall–Petch derived for coarse grains? | Chapter 13 |
| How do micromechanics models (Halpin–Tsai, shear lag) predict the stiffness of filled polymers? | Chapter 22 |
| What sets electron and phonon transport in bulk conductors and semiconductors? | Chapters 24–26 |
| How are nanomaterials used in batteries, supercapacitors, catalysts and thermoelectrics? | Chapter 32 |
| How do nanoscale oxide dispersions make steels resistant to radiation and creep? | Chapter 33 |
| How are thin films and ALD layers grown and patterned? | Chapter 41 |
| How do atom-probe tomography and aberration-corrected STEM resolve nanostructures? | Chapter 43 |
| Can molecular dynamics predict the inverse Hall–Petch transition and 2D-material properties? | Chapters 45 and 46 |
| How are the environmental footprint and end-of-life of nanomaterials assessed? | Chapter 49 |

**Next:** Chapter 31 places materials inside the human body, where the environment is warm, wet, salty and alive, and asks what makes a material biocompatible.
