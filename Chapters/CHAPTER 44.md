# Chapter 44 — In-Situ, Operando and Correlative Methods

*Part X · Characterization, Computation and Design*

An electric-vehicle battery pack is returned after 1,200 fast-charge cycles with 22 % of its capacity gone. The cells are opened in a glovebox and the cathode is sectioned. The scanning electron microscope shows what everyone expected: the polycrystalline nickel-rich oxide particles are full of intergranular cracks, and electrolyte has crept into them. But the micrograph cannot say *when* the particles cracked. They could have cracked in the first formation cycle and done little harm afterwards; they could have cracked gradually, each crack exposing fresh surface that consumed lithium; or they could have cracked only during the drying and sectioning that prepared the sample for the microscope. Those three histories call for three different remedies — a new particle morphology, a surface coating, or a different sample-preparation protocol — and a post-mortem image cannot distinguish them. The same dilemma appears wherever materials change under load: a nickel superalloy whose dislocation structure at 900 °C relaxes on cooling, a catalyst that is metallic under reaction gas and oxidized by the time it reaches the microscope, a cement paste whose hydrates dehydrate in vacuum.

This chapter is about the methods that watch materials *while* they change, and about the methods that see what diffraction and imaging cannot: open volume, valence and local coordination. It ends with the problem these methods create — data volumes so large that analysis, not acquisition, becomes the bottleneck.

> **How can a material be observed while it is heated, strained, biased or reacting, without the observation itself changing the result?**
> **Which techniques detect vacancies, oxidation states and local atomic environments that conventional microscopy misses, and how are several techniques combined on the same region of the same sample?**

| Concept | Engineering destination |
|---|---|
| In-situ TEM/SEM heating | Precipitation and grain growth in alloys, sintering of ceramics, recrystallization during annealing |
| In-situ straining | Dislocation sources, crack-tip plasticity, twinning in Mg and Ti, fracture of thin films and coatings |
| In-situ biasing | Electromigration in interconnects, resistive switching, ferroelectric domain motion |
| Micropillar compression | Single-phase properties for crystal-plasticity models, irradiated-steel testing, coating and phase strength |
| In-situ nanoindentation | Hardness and modulus of thin films, weld zones, individual grains and phases |
| Operando battery studies | Phase transitions, particle cracking, lithium plating, solid-electrolyte interphase growth |
| Operando catalysis | Active oxidation state of catalysts in reactors, fuel-cell and electrolyser electrodes |
| Positron annihilation | Vacancies in quenched and irradiated metals, free volume in polymers, voids in semiconductors |
| Mössbauer spectroscopy | Retained austenite in steel, iron corrosion products, Fe valence in cathodes and catalysts |
| Solid-state NMR | Silicate connectivity in cement and glass, Al sites in zeolites, Li environments in electrolytes |
| Correlative workflows | Linking crack initiation to microstructure, composition to structure in the same feature |
| Automated analysis | High-throughput EBSD, 4D-STEM, segmentation of tomograms, self-driving experiments |

**Roadmap.** Why observing during change matters and what the observer does to the sample (44.1) → in-situ heating, straining and biasing in electron microscopes (44.2) → small-scale mechanical testing: micropillars and in-situ nanoindentation (44.3) → operando studies of batteries and catalysts (44.4) → positron annihilation for open-volume defects (44.5) → Mössbauer and solid-state NMR for local environment and valence (44.6) → correlating techniques on the same volume (44.7) → big data and automated analysis (44.8).

---

## 44.1 From post-mortem to operando

### Three words, three levels of ambition

Conventional characterization (Chapters 42 and 43) is mostly **ex situ**: a sample is prepared, transferred to the instrument and examined in a state that has been frozen, cooled, dried or unloaded. Three more ambitious modes are distinguished:

- **In situ** ("in place"): the stimulus — temperature, stress, electric field, gas, liquid — is applied inside the instrument, and the material is observed while it acts. A TEM specimen heated on a chip in the microscope is in situ.
- **Operando** ("working"): the material is observed inside a functioning device under realistic operating conditions, *and* the device's performance is measured at the same time. A battery cycled in a synchrotron beam while its voltage and capacity are logged is operando; a catalyst bed whose product stream is analysed by mass spectrometry while X-ray absorption is measured is operando.
- **Correlative**: two or more techniques are applied to the *same* region of the *same* specimen, so that, for example, a crystal orientation from one method, a composition from another and a defect density from a third refer to the same grain.

The distinction between in situ and operando matters because many experiments that call themselves operando are not. A thin electrode in a specially built cell with a beryllium window, cycled at a slow rate, may not behave like the same electrode in a commercial pouch cell; the experiment is honest only if the electrochemical response of the special cell matches that of the real one.

### Time and length resolution

Every in-situ experiment is a trade between spatial resolution, time resolution and field of view. Table 44.1 sets out representative numbers.

| Method | Typical spatial resolution | Typical time resolution | Typical field of view |
|---|---|---|---|
| In-situ TEM imaging (direct electron camera) | 0.1–1 nm | 0.1–10 ms per frame | 0.01–5 μm |
| In-situ SEM imaging and EBSD | 2–50 nm (imaging), 20–100 nm (EBSD) | 0.1–60 s per frame or map | 1 μm – 1 mm |
| Synchrotron powder diffraction | averages over beam (μm–mm) | 0.01–10 s per pattern | 0.01–1 mm³ |
| Synchrotron X-ray tomography | 0.3–5 μm voxels | 0.1 s – 10 min per volume | 0.5–5 mm |
| Neutron diffraction (operando cell) | averages over cm³ | 1–30 min per pattern | whole cell |
| Positron lifetime (²²Na source) | averages over ~0.1 mm depth | hours per spectrum | mm² |
| Mössbauer spectroscopy | bulk average | hours to days per spectrum | cm² absorber |

The table shows why no single method wins: the techniques that resolve individual dislocations see a few micrometres for a few seconds; the techniques that see a whole battery cell need minutes per measurement and average over billions of particles.

### The observer effect

The probe is never neutral. Three effects recur.

**Beam damage.** A 200–300 keV electron can transfer enough energy to a nucleus to displace it (knock-on damage) when the maximum transferred energy exceeds the displacement threshold of 15–40 eV; for carbon in graphene this happens above roughly 80 keV, for aluminium above about 170 keV, for copper above about 400 keV. Electrons also ionize and break bonds (radiolysis), which is why polymers, hydrates, zeolites and organic electrolytes degrade within seconds under a focused beam, and why water in a liquid cell decomposes into hydrogen, hydroxyl radicals and hydrated electrons that change pH and can deposit or etch metal. Synchrotron X-rays, more gently, heat and can reduce transition-metal ions in battery electrodes over tens of minutes of exposure.

**Geometry.** A TEM foil 50–200 nm thick has two free surfaces within a few hundred atomic spacings of every point. Dislocations feel image forces that pull them out of the foil, vacancies escape to the surfaces, and the stress state in a thin foil under tension is nearly plane stress. A process observed in a foil is therefore a valid analogue of the bulk only when its characteristic length — a dislocation-source size, a diffusion distance, a precipitate spacing — is much smaller than the foil thickness.

**Environment.** Most electron microscopes operate at $10^{-5}$ Pa or better. Hydrates lose water, catalysts reduce, lithium reacts with residual gas. Environmental TEM (differentially pumped, up to about 20 mbar of gas at the sample) and windowed gas and liquid cells (up to about 1 bar with silicon-nitride membranes 20–50 nm thick) push this limit, at the cost of resolution lost to scattering in the gas, the liquid and the windows.

> **Status of the principle: Representativeness of in-situ experiments**
> *Approximate.* An in-situ observation predicts bulk or device behaviour only when the dose, geometry and environment perturb the process less than the stimulus being studied; this must be checked by dose series, thickness series and comparison with ex-situ or bulk measurements, not assumed.

---

## 44.2 In-situ heating, straining and biasing in TEM and SEM

### Specimen holders and MEMS chips

The enabling technology of modern in-situ electron microscopy is the **MEMS chip**: a silicon die a few millimetres across carrying a suspended silicon-nitride membrane with a patterned metal or ceramic heater, electrodes, or a mechanical actuator. Because the heated volume is tiny (a membrane of a few hundred micrometres), a chip can reach 1,000–1,300 °C in milliseconds, cool equally fast, and drift by less than a nanometre per minute — a furnace-type holder that heats the whole specimen cup takes minutes to stabilize and drifts by tens of nanometres. Figure 44.1 shows the main holder types.

<!-- FIGURE 44.1 | figures/ch44/fig-44-1-insitu-holder-types.png | schematic | Four families of in-situ TEM specimen holders and the stimulus each applies. | Content: four panels in a row, each showing the holder tip in side view with the electron beam as a vertical arrow. (a) MEMS heating chip: Si frame, SiN membrane with spiral heater, specimen on electron-transparent windows, label "up to ~1,300 °C, ~10^6 °C/s". (b) Straining holder: push-to-pull MEMS device with a dog-bone specimen bridging a gap, actuator arrow, label "tension, ~nm displacement control". (c) Biasing chip: two electrodes contacting a lamella, voltage source symbol, label "field, current, electromigration". (d) Closed gas/liquid cell: two SiN windows (20–50 nm) enclosing fluid layer, inlet and outlet tubes, label "≤1 bar gas or liquid flow". Common style, grey silicon, orange heaters, blue fluid. -->

### Heating experiments

Heating in the microscope addresses three classes of question.

**Phase transformations and precipitation.** Ageing of an Al–Cu–Mg or Al–Zn–Mg alloy can be followed from Guinier–Preston zones to semi-coherent precipitates; the dissolution of carbides in a tool steel and the reversion of martensite to austenite in a maraging steel can be watched at the scale of individual laths. The kinetics measured in a foil are faster than in bulk when surfaces act as vacancy sinks or as nucleation sites, so quantitative rates are normally checked against differential scanning calorimetry (Chapter 42) on bulk samples.

**Grain growth, recrystallization and sintering.** The migration of individual grain boundaries in nanocrystalline metals, the necking between ceramic powder particles during sintering (Chapter 38), and the coarsening of supported catalyst nanoparticles can all be imaged directly. In-situ observation of sintering of zirconia and alumina nanopowders has shown, for example, that particle rotation and coalescence contribute to early-stage densification, a mechanism invisible to dilatometry.

**Thermal stability of devices and coatings.** Interdiffusion at metal–silicide contacts, crystallization of amorphous phase-change films, and the oxidation of thermal-barrier bond coats can be followed on cross-sectional lamellae.

The biggest practical uncertainty in heating experiments is the specimen temperature. The chip calibrates the heater, not the specimen; a lamella that is poorly attached, or a gas environment that cools the membrane, can sit tens of degrees below the nominal value. Good practice uses an internal standard — the melting of a small tin or aluminium particle, a known phase transition, or the thermal expansion of a reference lattice measured by electron diffraction.

### Straining experiments

Straining holders apply tension, compression or bending to a thin specimen while it is imaged. Early holders pulled a 3 mm disc mechanically; modern push-to-pull MEMS devices convert the compression of an indenter tip into tension of a small dog-bone specimen and measure both force and displacement, giving a stress–strain curve synchronized with the video.

Such experiments delivered much of the direct evidence behind the dislocation theory of Chapters 12 and 13:

- the operation of Frank–Read and single-arm (spiral) sources, and the pile-up of dislocations at grain boundaries;
- the transmission, absorption or reflection of dislocations at grain and twin boundaries, which underlies the Hall–Petch effect and the high strength of nanotwinned copper;
- the screw-dislocation motion by kink-pair nucleation that makes body-centred cubic metals strongly temperature-sensitive;
- the nucleation and growth of deformation twins in magnesium and titanium alloys, important for the formability of lightweight automotive sheet and aerospace forgings;
- the crack-tip plasticity and the formation of dislocation-free zones ahead of cracks.

In-situ straining in the **SEM** works at a coarser scale with much larger specimens. Tensile stages carrying millimetre-scale specimens with loads up to a few kilonewtons can be combined with electron backscatter diffraction (EBSD), which maps lattice rotation, and with digital image correlation (DIC) of a fine surface speckle pattern, which maps strain at the micrometre scale. The combination identifies which grain orientations and which grain-boundary types concentrate strain first — the starting point for fatigue-crack initiation in titanium aerospace alloys, nickel superalloys and dual-phase automotive steels. Heated SEM stages extend this to creep and to the high-temperature deformation of superalloys.

### Biasing experiments

Biasing chips carry electrodes that apply voltage and measure current while the specimen is imaged. Representative studies:

- **Electromigration** in copper and aluminium interconnects: void nucleation at the cathode end and hillock growth at the anode under current densities of order $10^{10}$–$10^{11}\ \mathrm{A\,m^{-2}}$, with void motion along grain boundaries and interfaces directly observed (Chapter 41).
- **Resistive switching** in oxide memory cells (HfO₂, TaOₓ): formation and rupture of conducting filaments of oxygen-deficient oxide or metal.
- **Ferroelectric and ferroelastic domain switching** in thin-film PbTiO₃ and BiFeO₃, with domain walls pinned and released by defects.
- **Solid-state batteries** in miniature: lithium plating at a solid electrolyte interface imaged in a lamella cut from a full cell.

A recurring caution: a lamella carries current through a cross-section of perhaps $5\ \mu\mathrm{m}\times100\ \mathrm{nm}$, and Joule heating in so small a conductor is removed efficiently, so electrothermal coupling can be weaker than in the real device.

> **Boundary.** The physics of electromigration, ferroelectric switching and resistive memory is treated at device depth in the *Materials Core (EEE)* book; here these are examples of what in-situ biasing can observe.

### The liquid cell

Liquid-cell TEM encloses a liquid layer, typically 50 nm – 1 μm thick, between two silicon-nitride windows. It has imaged nanoparticle nucleation and growth from solution, electrochemical deposition and dissolution of lithium and zinc, corrosion pit initiation at inclusions in stainless steel (Chapter 35) and the biomineralization of calcium phosphates relevant to bone and dental implants (Chapter 31). Resolution degrades with liquid thickness (from a few angstroms in very thin layers to a few nanometres in micrometre layers), and radiolysis must be controlled by keeping the dose rate low and, where possible, quantifying its chemistry.

---

## 44.3 Micropillar compression and in-situ nanoindentation

### Why test small volumes

Many engineering questions are about properties that cannot be measured on a conventional test bar because the material exists only in a small volume: a single grain of a coarse-grained casting, one phase of a two-phase titanium alloy, a 5 μm thermal-barrier coating, the heat-affected zone of a spot weld, the 100 μm surface layer of a reactor component damaged by ion irradiation. Small-scale mechanical testing measures those properties directly, and when performed inside an SEM or TEM it shows what the material does at the same time.

### Nanoindentation and the Oliver–Pharr method

Instrumented indentation pushes a sharp diamond tip into a surface while recording load $P$ and displacement $h$. The standard three-sided **Berkovich** pyramid has a projected contact area related to the contact depth $h_c$ by

$$
A = 24.5\,h_c^{2}
$$

for an ideal tip; real tips are blunted and calibrated on fused silica with an area function. The **Oliver–Pharr method** treats the initial unloading as elastic. Its slope, the contact stiffness $S=dP/dh$, gives the reduced modulus

$$
E_r=\frac{\sqrt{\pi}}{2\beta}\,\frac{S}{\sqrt{A}},\qquad \frac{1}{E_r}=\frac{1-\nu^{2}}{E}+\frac{1-\nu_i^{2}}{E_i}
$$

with $\beta\approx1.034$ for a Berkovich tip and $E_i=1141$ GPa, $\nu_i=0.07$ for diamond. The contact depth comes from the maximum depth corrected for elastic sink-in, $h_c=h_{max}-\epsilon P_{max}/S$ with $\epsilon=0.75$, and the hardness is

$$
H=\frac{P_{max}}{A}
$$

> **Status of the principle: Oliver–Pharr analysis**
> *Approximate.* Derived from elastic contact of a rigid axisymmetric punch on a half-space; accurate to a few percent for materials that sink in, but overestimates area-corrected hardness and modulus by up to 20–30 % in work-hardened metals that pile up around the indenter, and fails when the indent is deeper than about 10 % of a film's thickness so that the substrate contributes.

**Worked example — nanoindentation of cold-worked copper.** A Berkovich indentation into a cold-rolled copper busbar (illustrative values, typical of published measurements) reaches $P_{max}=10.0$ mN at $h_{max}=543$ nm. The unloading stiffness is $S=0.360\ \mathrm{mN\,nm^{-1}}=3.60\times10^{5}\ \mathrm{N\,m^{-1}}$. The contact depth is

$$
h_c=543-0.75\times\frac{10.0}{0.360}=543-20.8=522\ \mathrm{nm}
$$

The projected area is $A=24.5\times(522\times10^{-9})^2=6.68\times10^{-12}\ \mathrm{m^2}=6.68\ \mu\mathrm{m^2}$, and the hardness

$$
H=\frac{10.0\times10^{-3}}{6.68\times10^{-12}}=1.50\times10^{9}\ \mathrm{Pa}=1.50\ \mathrm{GPa}
$$

The reduced modulus is

$$
E_r=\frac{\sqrt{\pi}}{2\times1.034}\times\frac{3.60\times10^{5}}{\sqrt{6.68\times10^{-12}}}=0.857\times1.393\times10^{11}=1.19\times10^{11}\ \mathrm{Pa}
$$

Removing the diamond compliance, $(1-0.07^2)/1141=8.72\times10^{-4}\ \mathrm{GPa^{-1}}$ from $1/E_r=8.37\times10^{-3}\ \mathrm{GPa^{-1}}$ leaves $7.50\times10^{-3}\ \mathrm{GPa^{-1}}$, so $E=(1-0.34^2)/7.50\times10^{-3}=118$ GPa — close to the 110–130 GPa expected for polycrystalline copper. The hardness of 1.5 GPa corresponds, by the rule of thumb $H\approx3\sigma_y$ (Chapter 11), to a flow stress near 500 MPa, typical of heavily cold-worked copper. If the indent showed significant pile-up in the SEM, both numbers would be revised downward.

### In-situ indentation

Inside an SEM, the indenter can be positioned on a chosen grain or phase identified by EBSD, and the formation of slip traces, pile-up, cracks or delamination watched as the load rises. Inside a TEM, a nanoindenter pressed into the edge of a wedge-shaped specimen reveals the first dislocation nucleation event — the **pop-in** seen as a sudden displacement burst on the load–displacement curve — and the formation of cracks in hard coatings such as TiN, CrN and diamond-like carbon. The maximum shear stress beneath the tip at pop-in in a defect-free volume approaches $G/10$ to $G/20$, close to the theoretical shear strength, confirming that small enough volumes are strong because they contain no dislocation sources (Chapter 12).

### Micropillar compression

A **micropillar** is a cylinder milled by a focused ion beam (FIB) from the surface of a bulk sample or from a single grain, typically 0.2–10 μm in diameter with a height-to-diameter ratio of 2–3. A flat-ended diamond punch compresses it inside a nanoindenter or an SEM. The engineering stress is load over top cross-sectional area, and the stress–strain curve can be recorded while slip steps form on the pillar surface (Figure 44.2a).

The first such experiments, on nickel and gold single crystals around 2004–2005, revealed a striking **size effect**: pillars of identical crystals and orientations grew stronger as they got smaller, and their stress–strain curves became staircases of discrete strain bursts rather than smooth curves. Across face-centred cubic metals the flow stress follows approximately

$$
\sigma = A\,D^{-n}
$$

with $n$ typically 0.5–0.8 for FCC metals and smaller (0.2–0.5) for BCC metals at room temperature, where the intrinsic lattice friction of screw dislocations is already high. Two mechanisms explain it: **source truncation**, where Frank–Read sources in a small pillar are shorter (the pillar diameter limits their length, and the source-operation stress scales as $\mu b/L$), and **dislocation starvation**, where mobile dislocations leave through the free surface faster than they multiply.

> **Status of the principle: Power-law size effect in micropillars**
> *Empirical.* The exponent is fitted to data for each material; it applies to initially dislocated single crystals between roughly 0.1 and 20 μm, saturates towards bulk behaviour at large diameters, and depends on the initial dislocation density and on FIB damage.

<!-- FIGURE 44.2 | figures/ch44/fig-44-2-micropillar-size-effect.png | plot | Micropillar compression of single-crystal nickel: staircase stress–strain curves and the power-law size effect. | Content: (a) engineering stress (0–700 MPa) vs engineering strain (0–0.10) for pillar diameters 5, 2, 1 and 0.5 μm; the 5 μm curve smooth, flowing near 150 MPa; smaller pillars with flat strain bursts and flow stresses near 260, 390 and 600 MPa. Inset sketch of a tapered pillar with slip steps. (b) log–log plot of flow stress at 5 % strain (100–1,000 MPa) vs diameter (0.1–10 μm), points at 5, 2, 1, 0.5, 0.2 μm on a line of slope −0.6 (150 MPa at 5 μm to ~1,030 MPa at 0.2 μm); bulk single-crystal level as horizontal dashed line labelled "bulk". -->

**Worked example — designing a micropillar test.** A 5 μm nickel pillar flows at 150 MPa at 5 % strain (an illustrative value, typical of published tests). Assume $n=0.6$. The flow stress expected at other diameters is $\sigma(D)=150\,(D/5\ \mu\mathrm{m})^{-0.6}$:

| Diameter (μm) | 5 | 2 | 1 | 0.5 | 0.2 |
|---|---|---|---|---|---|
| Predicted flow stress (MPa) | 150 | 260 | 394 | 597 | 1035 |

A 0.5 μm pillar at 597 MPa carries a load $F=\sigma\pi D^2/4=597\times10^{6}\times\pi\times(0.5\times10^{-6})^2/4=1.17\times10^{-4}$ N $=117\ \mu$N, well within a nanoindenter's range (resolution near 0.1 μN) but small enough that a 1 μN offset in the zero-load reference would change the stress by about 1 %. The experimental design consequences follow from the numbers: (1) the punch must be flat and aligned to better than about 0.5° or the pillar bends; (2) the FIB-damaged surface layer, about 10–20 nm deep for 30 kV gallium ions, is 4–8 % of the radius of a 0.5 μm pillar and contributes measurably, so small pillars are finished at low ion energy or milled with a xenon plasma FIB; (3) a taper of 2–3° makes the top stress higher than the base stress by an amount comparable to the scatter. These are the reasons that small-scale strength data should always be quoted with diameter, taper and preparation route.

### Engineering uses

Micropillars and microcantilevers have become a production tool in three areas. **Nuclear materials:** ion irradiation damages only the top 1–5 μm of a steel or tungsten sample, so the change of strength with dose can be measured only by small-scale tests, avoiding months of reactor exposure and the handling of activated specimens (Chapter 33). **Microstructure-informed modelling:** the critical resolved shear stresses of individual slip systems in α and β titanium, or of the γ and γ′ phases of a superalloy, are input parameters for the crystal-plasticity simulations of Chapter 46. **Coatings and interfaces:** notched microcantilevers milled across a coating–substrate interface give the fracture toughness of the interface, and micropillars with an inclined interface give its shear strength — the quantities that decide whether a thermal-barrier coating spalls or a hard coating on a cutting tool chips.

---

## 44.4 Operando battery and catalyst studies

### Why batteries need operando methods

A lithium-ion cell is a closed, reactive system. Its active materials change phase with every cycle; its graphite anode can plate lithium metal at high charge rates and low temperatures; its electrolyte decomposes into a solid-electrolyte interphase (SEI) a few tens of nanometres thick; and nearly all of these states are metastable. Opening the cell relaxes concentration gradients, lets lithiated graphite react with air, and dissolves part of the SEI in washing solvent. Operando methods avoid this, and they deliver information that ex-situ work cannot: which phase is present at *which* state of charge, and how inhomogeneous the electrode is during fast charge (Chapter 32).

### The toolkit

**Operando X-ray diffraction** in coin or pouch cells with X-ray-transparent windows (beryllium, Kapton, or simply the thin aluminium pouch at high synchrotron energies) records the evolution of phases and lattice parameters. With a laboratory diffractometer a pattern takes minutes; at a synchrotron, seconds or less. Typical observables:

- Graphite stages: lithium intercalates first into dilute stages, then forms LiC₁₂ and finally LiC₆, the (002) interlayer spacing expanding from 3.35 Å to about 3.70 Å (Figure 44.3).
- Two-phase reactions such as LiFePO₄ ↔ FePO₄ (6.5 % volume change), where the phase fractions vary linearly with charge passed.
- Solid-solution reactions in layered oxides (LiNiₓMnᵧCo_zO₂, "NMC"), where lattice parameters vary continuously. In nickel-rich NMC the $c$ parameter expands and then collapses abruptly above about 4.1 V vs Li/Li⁺, an anisotropic contraction of several percent in unit-cell volume that drives the intergranular cracking described in the opening of this chapter.

**Operando X-ray absorption spectroscopy** (XANES and EXAFS, Chapter 43) tracks the oxidation state of each transition metal separately — whether nickel, cobalt or manganese, or the oxygen sublattice, provides the charge compensation.

**Operando tomography** at micrometre resolution follows particle cracking, gas evolution, electrode swelling and lithium dendrite growth in three dimensions; in silicon anodes, which expand by about 280 % to Li₁₅Si₄, it shows how particles detach from the conductive network.

**Operando neutron diffraction** sees lithium (which scatters X-rays weakly) and probes whole commercial cells, because neutrons penetrate steel cans. **Operando ⁷Li NMR** (Section 44.6) distinguishes lithium in the electrolyte, in intercalated graphite and in metallic deposits by their chemical or Knight shifts, so it quantifies lithium plating directly.

<!-- FIGURE 44.3 | figures/ch44/fig-44-3-operando-xrd-graphite.png | plot | Operando X-ray diffraction of a graphite anode during the first lithiation, showing staging transitions alongside the voltage profile. | Content: left panel: colour contour map, x-axis 2θ-equivalent interlayer spacing d(00l) from 3.30 to 3.75 Å, y-axis time 0–5 h (C/5 lithiation); intensity bands shifting from 3.35 Å (graphite) through ~3.47–3.52 Å (dilute stages) to 3.53 Å (LiC12, stage 2) and abrupt jump to 3.70 Å (LiC6, stage 1) in the last ~45 % of capacity. Right panel sharing y-axis: cell voltage vs Li/Li+ 0.0–0.3 V with plateaus at ~0.21, ~0.12 and ~0.085 V labelled. Annotation: "one pattern every 5 min = 1.7 % state of charge". -->

**Worked example — time resolution of an operando experiment.** A pouch cell of 3.0 mAh capacity with a graphite anode is charged at C/5, so the current is $3.0/5=0.60$ mA and a full lithiation takes 5 h. A laboratory diffractometer needs 5 min per pattern. Each pattern therefore averages over a change of state of charge of

$$
\frac{5\ \mathrm{min}}{5\times60\ \mathrm{min}}=0.0167=1.7\ \%
$$

and a full lithiation yields 60 patterns — enough to resolve the main staging transitions. Fast charging at 3C changes the picture: the full lithiation takes 20 min, so the same 5 min pattern would average over 25 % of the charge and blur the LiC₁₂ → LiC₆ transition entirely. To keep 1.7 % per pattern the acquisition must fall to 20 s, which demands a synchrotron. As a check on the capacity: the theoretical capacity of graphite, one lithium per six carbons, is

$$
\frac{F}{3.6\,M_{\mathrm{C_6}}}=\frac{96485}{3.6\times72.07}=372\ \mathrm{mAh\,g^{-1}}
$$

so a 3.0 mAh anode needs only about 8 mg of graphite when fully used — illustrating how little material an operando cell contains and how carefully it must be built to represent a commercial electrode.

> **Status of the principle: Linear lattice-parameter–composition relations (Vegard's law) in operando analysis**
> *Empirical.* Converting a measured lattice parameter to lithium content assumes a calibrated, approximately linear relation within a single-phase field; it fails across phase transitions, in strained or defective particles, and where several phases overlap, so it must be calibrated with ex-situ reference compositions.

### Operando catalysis

In heterogeneous catalysis the active state of a catalyst is often not the state that is loaded into the reactor. Copper–zinc oxide methanol-synthesis catalysts, platinum fuel-cell electrocatalysts and iridium oxide electrolyser anodes all reconstruct under reaction conditions, and their surfaces are covered by adsorbates that disappear on cooling. Operando catalysis studies therefore combine a structural or spectroscopic probe with simultaneous activity measurement — gas chromatography or mass spectrometry of the product stream, or the current of an electrochemical cell:

| Probe | What it reveals | Typical conditions |
|---|---|---|
| XAS (XANES, EXAFS) | Oxidation state and coordination of the metal under reaction | Fixed-bed capillary reactors, up to tens of bar and 500 °C |
| Ambient-pressure XPS | Surface composition and oxidation states of the outer 1–3 nm | Up to about 20–100 mbar gas |
| Infrared (DRIFTS, ATR) and Raman | Adsorbed intermediates, surface oxides, coke | Reactor cells at full pressure |
| Environmental TEM | Particle shape, sintering, surface faceting | ≤ 20 mbar (ETEM) or ≤ 1 bar (closed cell) |
| X-ray diffraction and PDF analysis | Bulk and nanoparticle phase, size | Capillary reactors |

A recurring lesson is the **pressure gap**: surface-science studies at ultra-high vacuum often find surface states that are not present at industrial pressures, and the active phase identified under realistic conditions may be minority, transient or amorphous. Operando studies of platinum alloy cathode catalysts in fuel cells, for example, showed that the less noble metal leaches from the particle surface during potential cycling, leaving a platinum-rich shell whose strained lattice raises activity — and that the same leaching later drives particle coarsening and loss of surface area.

---

## 44.5 Positron annihilation spectroscopy

### Positrons as defect probes

Diffraction is blind to isolated vacancies at concentrations below about $10^{-3}$, and even atom-resolved microscopy sees them only in favourable cases. The **positron**, the antiparticle of the electron, is a uniquely sensitive vacancy detector. Positrons from a radioactive source (usually ²²Na) or a positron beam enter the sample, slow to thermal energies within a few picoseconds, diffuse about 100 nm, and annihilate with an electron, emitting two photons of 511 keV.

A thermalized positron is repelled by the positive ion cores. In a perfect lattice it occupies the interstitial region; at a vacancy, a vacancy cluster, a dislocation core or a void, where an ion core is missing, it sees an attractive potential well of about 1 eV and becomes **trapped**. Because the electron density at the open-volume site is lower, the trapped positron lives longer before annihilating. Three measurable quantities follow:

- **Positron lifetime**. The ²²Na decay emits a 1.27 MeV gamma ray almost simultaneously with the positron, which serves as a start signal; the 511 keV annihilation photon is the stop signal. The lifetime spectrum is a sum of exponentials, one per positron state.
- **Doppler broadening** of the 511 keV line, caused by the momentum of the annihilating electron. Annihilation with low-momentum valence electrons (typical of vacancies) gives a narrower line, measured by the shape parameter $S$; annihilation with high-momentum core electrons gives intensity in the wings, measured by $W$, which also carries a chemical fingerprint of the atoms surrounding the defect.
- **Angular correlation** of the two photons, a more detailed momentum measurement.

Table 44.2 gives representative lifetimes.

| Material | Bulk lifetime (ps) | Monovacancy lifetime (ps) | Notes |
|---|---|---|---|
| Aluminium | 160–165 | 240–250 | quenched-in vacancies, Al alloy clustering |
| Copper | 110–120 | 175–180 | |
| α-iron | 105–110 | 170–175 | irradiation damage in reactor steels |
| Nickel | 105–110 | 170–180 | |
| Silicon | 218–222 | 250–270 (divacancy ~300) | implantation damage |
| Large voids (> 1 nm) | — | 400–500 | vacancy clusters, swelling |
| Polymers (ortho-positronium) | — | 1,000–4,000 | free volume holes 0.2–0.5 nm radius |

In polymers, porous silica and other insulators, the positron binds with an electron to form **positronium**. Its long-lived ortho state is localized in free-volume holes, and its lifetime is related to hole size by the Tao–Eldrup model; positron lifetime is a standard measurement of free volume across the glass transition of polymers (Chapter 20) and of pore sizes in low-dielectric-constant films and membranes.

### The trapping model

The simplest analysis treats one defect type with trapping rate $\kappa$, a bulk annihilation rate $\lambda_b=1/\tau_b$ and a defect annihilation rate $\lambda_v=1/\tau_v$. The rate equations predict a two-component spectrum with

$$
\tau_1=\frac{1}{\lambda_b+\kappa},\qquad \tau_2=\tau_v,\qquad \kappa=\frac{I_2}{I_1}\left(\lambda_b-\lambda_v\right)
$$

and the trapping rate is proportional to defect concentration, $\kappa=\mu c_v$, with a specific trapping coefficient $\mu$ of order $10^{14}$–$10^{15}\ \mathrm{s^{-1}}$ for vacancies in metals. A consistency check is that the bulk lifetime recomputed from the components, $1/\tau_b=I_1/\tau_1+I_2/\tau_2$, matches the known defect-free value.

> **Status of the principle: Two-state positron trapping model**
> *Approximate.* Derived from first-order rate equations assuming one defect type, no detrapping and spatially uniform defects; it holds for vacancies in metals at low temperature and moderate concentration, fails when several defect types or shallow traps (such as dislocations with thermal detrapping) are present, and saturates when nearly every positron is trapped (vacancy fractions above roughly $10^{-4}$).

**Worked example — vacancies in an irradiated iron alloy.** A ferritic steel specimen irradiated with neutrons gives a positron lifetime spectrum (illustrative values, typical of published measurements) decomposed into $\tau_1=88$ ps with intensity $I_1=60\ \%$ and $\tau_2=175$ ps with $I_2=40\ \%$ (Figure 44.4). The second lifetime matches the iron monovacancy. Check consistency first: $1/\tau_b=0.60/88+0.40/175=6.82\times10^{-3}+2.29\times10^{-3}=9.10\times10^{-3}\ \mathrm{ps^{-1}}$, so $\tau_b=110$ ps, the value for defect-free iron — the one-defect model is consistent. The trapping rate is

$$
\kappa=\frac{0.40}{0.60}\left(\frac{1}{110\ \mathrm{ps}}-\frac{1}{175\ \mathrm{ps}}\right)=0.667\times(9.09-5.71)\times10^{9}\ \mathrm{s^{-1}}=2.25\times10^{9}\ \mathrm{s^{-1}}
$$

With $\mu\approx1.1\times10^{15}\ \mathrm{s^{-1}}$, the vacancy-type defect fraction is $c_v=2.25\times10^{9}/1.1\times10^{15}=2.0\times10^{-6}$, or two vacant sites per million — far below anything diffraction or electron microscopy could detect, yet enough to influence radiation-enhanced diffusion and embrittlement (Chapters 8 and 33). The fraction of positrons that annihilate in traps is $\kappa/(\lambda_b+\kappa)=2.25/(9.09+2.25)=0.20$, which shows the method is far from saturation; the mean lifetime $\bar\tau=I_1\tau_1+I_2\tau_2=123$ ps is the robust number to monitor during post-irradiation annealing.

<!-- FIGURE 44.4 | figures/ch44/fig-44-4-positron-lifetime-spectrum.png | plot | Positron lifetime spectra of well-annealed and irradiated iron, with the two-component decomposition. | Content: semi-log plot, counts (10^0 to 10^6) vs time after start signal (0–2 ns). Annealed Fe: single exponential with τ = 110 ps after the instrument resolution peak (FWHM ~200 ps). Irradiated Fe: two components, τ1 = 88 ps (60 %) and τ2 = 175 ps (40 %), each drawn as a dashed line, sum as solid line; constant background ~10 counts. Inset: schematic of a positron (red) trapped at a vacancy in a square lattice, with potential-energy well sketch (~1 eV). -->

### Variable-energy beams and uses

A radioactive source gives positrons with a broad energy spectrum that penetrate about 0.1 mm into metals, so it measures bulk averages. **Slow positron beams**, moderated and re-accelerated to 0.1–30 keV, implant positrons at controlled depths from a few nanometres to a few micrometres; depth-profiled Doppler broadening reveals ion-implantation damage in silicon, porosity in low-$k$ dielectrics, and the defect layer beneath machined or shot-peened surfaces. Large-facility beams (reactor- or accelerator-based) give enough intensity for lifetime measurement with a beam.

Engineering applications include:

- tracking quenched-in vacancies and early solute clustering in age-hardening aluminium alloys, which controls natural ageing of automotive 6xxx sheet between stamping and paint bake;
- following radiation damage and its recovery in reactor-pressure-vessel steels and fusion materials;
- characterizing free volume, physical ageing and gas permeability in polymer membranes and packaging films;
- detecting vacancy-type defects in compound semiconductors and oxides (Ga vacancies in GaN, Zn vacancies in ZnO), which act as compensating acceptors.

---

## 44.6 Mössbauer spectroscopy and solid-state NMR

Both techniques probe the nucleus as a sensor of its immediate electronic and magnetic environment. Neither needs long-range order, so they work equally well on crystals, glasses, nanoparticles, corrosion products and hydrated cements — materials that defeat diffraction.

### Mössbauer spectroscopy

**Principle.** A ⁵⁷Co source decays to an excited ⁵⁷Fe nucleus that emits a 14.4 keV gamma ray. In a solid, a fraction of these emissions occur with no recoil energy lost to the lattice (the **recoil-free fraction**, the Mössbauer effect), so the gamma ray carries the full transition energy with an extremely narrow natural width. An absorber containing ⁵⁷Fe (natural abundance 2.1 %) absorbs it resonantly only if its nuclear levels match. They are scanned by moving the source at a few millimetres per second, Doppler-shifting the gamma energy by

$$
\Delta E=E_\gamma\frac{v}{c}
$$

> **Status of the principle: Doppler energy shift**
> *Fundamental.* First-order Doppler shift of photon energy, exact to order $v/c$; at mm/s velocities the second-order term is negligible except as a small temperature-dependent shift.

For $E_\gamma=14.4$ keV and $v=1\ \mathrm{mm\,s^{-1}}$, $\Delta E=14.4\times10^{3}\times(10^{-3}/2.998\times10^{8})=4.80\times10^{-8}$ eV. The natural linewidth, set by the 141 ns mean lifetime of the excited state, is $\Gamma=\hbar/\tau=6.58\times10^{-16}/1.41\times10^{-7}=4.67\times10^{-9}$ eV, equivalent to 0.097 mm/s; the narrowest observable line (source plus absorber) is about 0.19 mm/s. An energy resolution of a few parts in $10^{13}$ is what lets the spectrometer read the tiny hyperfine interactions of the nucleus with its surroundings.

**Hyperfine parameters.** Three quantities are extracted:

- **Isomer shift** $\delta$, from the s-electron density at the nucleus, which depends on oxidation and spin state: high-spin Fe³⁺ typically 0.3–0.5 mm/s, high-spin Fe²⁺ 0.9–1.3 mm/s (relative to α-Fe at room temperature).
- **Quadrupole splitting** $\Delta E_Q$, a doublet from an electric-field gradient at a non-cubic site; large for high-spin Fe²⁺ (often 1.5–3 mm/s).
- **Magnetic hyperfine field** $B_{hf}$, splitting the line into a sextet in magnetically ordered phases: 33.0 T for α-Fe (outer lines at ±5.3 mm/s), about 51.7 T for hematite, about 49 and 46 T for the two magnetite sites at room temperature.

Relative areas of subspectra give phase fractions, after correction for differences in recoil-free fraction.

<!-- FIGURE 44.5 | figures/ch44/fig-44-5-mossbauer-steel-rust.png | plot | Room-temperature ⁵⁷Fe Mössbauer spectra of a quenched steel and of an atmospheric corrosion product. | Content: two stacked panels, transmission (normalized, 0.90–1.00) vs source velocity −10 to +10 mm/s. (a) Quenched and tempered steel: six-line sextet of ferrite/martensite (B_hf ≈ 33 T, outer lines ±5.3 mm/s) plus a single central line of paramagnetic retained austenite at δ ≈ −0.09 mm/s, area ~8 %, labelled. (b) Rust layer on weathering steel: broad sextet of goethite (B_hf ~ 38 T reduced by small particle size) plus central Fe3+ doublet (δ ≈ 0.37 mm/s, ΔEQ ≈ 0.6 mm/s) of superparamagnetic or lepidocrocite fraction. Velocity axis ticks every 2 mm/s. -->

**Engineering uses.** Mössbauer spectroscopy measures **retained austenite** in quenched and carburized steels, which is paramagnetic and gives a single line distinct from the sextet of ferrite and martensite (Figure 44.5a); retained austenite in bearing and gear steels governs dimensional stability and contact fatigue (Chapter 15). It identifies the iron oxyhydroxides in corrosion products (goethite, lepidocrocite, akaganeite, magnetite), including nanocrystalline forms that give no X-ray diffraction pattern, which is how the protective patina on weathering steels was characterized (Chapter 35). It measures the Fe²⁺/Fe³⁺ ratio in glasses (which sets their colour and redox state), in iron-phosphate battery cathodes during cycling, and in iron-containing catalysts and minerals. Other Mössbauer isotopes — ¹¹⁹Sn for tin-based anodes and solders, ¹⁵¹Eu, ¹²¹Sb — extend the method to further systems. Its limitations are low count rates (hours to days per spectrum), the need for a suitable isotope, and bulk averaging over the absorber.

### Solid-state NMR

**Principle.** Nuclei with spin (¹H, ⁷Li, ¹³C, ¹⁹F, ²³Na, ²⁷Al, ²⁹Si, ³¹P, ⁸⁹Y and many more) precess in a strong magnetic field (typically 9–23 T, proton frequencies of 400–1,000 MHz). Their exact resonance frequency, expressed as the **chemical shift** in parts per million, reflects the local electron distribution and therefore the coordination and bonding of the atom. In liquids rapid tumbling averages away anisotropic interactions and gives sharp lines; in solids, chemical-shift anisotropy, dipolar coupling and, for spins above 1/2, quadrupolar coupling broaden lines to kilohertz or more.

**Magic-angle spinning (MAS).** Spinning the sample rapidly about an axis inclined at $\theta_m=54.74°$ to the field, where $3\cos^2\theta_m-1=0$, averages the first-order anisotropic interactions that share this angular dependence. Rotor speeds of 10–60 kHz are routine and above 100 kHz are possible for small rotors. Quadrupolar nuclei such as ²⁷Al and ²³Na retain a second-order broadening that requires higher fields or multiple-quantum techniques.

**What it delivers.** Solid-state NMR is quantitative (peak areas count nuclei, given full relaxation) and works on amorphous as well as crystalline solids. Characteristic uses:

| Nucleus | Material | What the shift distinguishes |
|---|---|---|
| ²⁹Si | Glasses, cement, zeolites | $Q^n$ species (Si bonded through $n$ bridging oxygens): $Q^0$ about −71 ppm, $Q^2$ about −85 ppm, $Q^3$ about −95 to −100 ppm, $Q^4$ about −105 to −115 ppm |
| ²⁷Al | Zeolites, C–A–S–H, glasses | tetrahedral Al (about 50–80 ppm) vs octahedral Al (about 0–15 ppm) |
| ⁷Li, ⁶Li | Electrodes, solid electrolytes | Li sites, Li-ion hopping rates; metallic Li (Knight shift about 260 ppm) |
| ¹³C, ¹H | Polymers, composites | tacticity, crystallinity, chain dynamics, cure of resins |
| ³¹P, ¹⁹F | Bioglasses, phosphates, fluoropolymers | network connectivity, local order |

In **cement** (Chapter 18), ²⁹Si MAS NMR follows the conversion of the $Q^0$ silicate monomers of clinker to the $Q^1$ and $Q^2$ chains of calcium silicate hydrate, giving the degree of hydration and the mean silicate chain length — a structure that is nanocrystalline and essentially invisible to diffraction. In **zeolite catalysts**, ²⁷Al NMR distinguishes framework from extra-framework aluminium after steaming, which controls acid-site density. In **glasses** for displays and bioactive implants, ²⁹Si and ³¹P NMR quantify network connectivity, which controls dissolution rate (Chapter 31). In **battery materials**, ⁷Li operando NMR quantifies metallic lithium deposits during fast charge, and relaxation measurements give lithium-ion hopping rates in solid electrolytes. Dynamic nuclear polarization (DNP) boosts sensitivity by orders of magnitude for surface sites, such as the active sites of supported catalysts.

The limitations are sensitivity (many interesting nuclei have low abundance or low gyromagnetic ratio), paramagnetic broadening in materials containing unpaired electrons (many cathode oxides), and the need for complementary modelling: assigning shifts in complex structures increasingly relies on the first-principles calculations of Chapter 45.

---

## 44.7 Correlative multimodal workflows

### Why one technique is never enough

Each method answers a narrow question. EBSD gives crystal orientation but not composition below a few percent; atom-probe tomography (Chapter 43) gives composition with near-atomic resolution but poor crystallography; X-ray tomography sees a whole component but not its grain structure; TEM sees dislocations but in a foil whose location in the part is often unknown. The scientifically interesting events — the grain where a fatigue crack started, the inclusion where a pit nucleated, the particle that cracked in a battery — are rare, and statistics on one population and mechanism on another do not combine. Correlative workflows apply several techniques to the same feature, usually across scales.

<!-- FIGURE 44.6 | figures/ch44/fig-44-6-correlative-workflow.png | flowchart | A correlative multiscale workflow from a whole component to atomic resolution, with registration at each step. | Content: left-to-right chain of five boxes with characteristic voxel/pixel size and field of view: (1) lab X-ray CT of component, 10 μm voxels, cm field — "locate crack or defect"; (2) synchrotron or lab nano-CT of extracted region, 0.5 μm, mm — "3D context"; (3) SEM/EBSD/EDS of section, 50 nm, 100 μm — "grain orientation, phases"; (4) FIB-SEM lift-out and TEM/4D-STEM, 0.1–1 nm, μm — "dislocations, interfaces"; (5) atom-probe tomography, ~0.3 nm, 100 nm — "solute segregation". Between boxes: arrows labelled "fiducial marks / registration / transfer under inert gas or cryo". Bottom bar: arrow labelled "increasing resolution, decreasing volume (≈10^12 ×)". Side box: "shared data model and coordinate system". -->

### Building blocks

**Scale bridging.** A typical chain (Figure 44.6) begins with X-ray computed tomography of a whole component or coupon, which locates a crack, pore or inclusion of interest. A section is cut through that location for SEM, EDS and EBSD. A focused-ion-beam lift-out then extracts a TEM lamella or an atom-probe needle from a chosen grain boundary or interface. The volume examined shrinks by about twelve orders of magnitude from first to last step.

**Registration.** Data sets must be mapped into a common coordinate frame. This uses fiducial marks (FIB-milled crosses, deposited platinum markers, deliberate indents), features present in both data sets (pores, grain boundaries) and image-registration algorithms that compute the transformation — rigid, affine or non-linear to account for distortion in each instrument.

**Transfer.** Air-sensitive, hydrated or beam-sensitive samples — lithium metal, magnesium alloys exposed to hydrogen, hydrated tissue, cement pastes — need inert-gas or vacuum transfer shuttles, or cryogenic transfer that keeps them frozen between instruments.

**Same-specimen, sequential stimulus.** A powerful variant repeats observation after each increment of a stimulus: the same region of a dual-phase steel is mapped by EBSD and DIC after 0, 2, 5 and 10 % strain, or the same battery particle is imaged after each cycle.

### Examples across engineering

- **Aerospace fatigue.** In titanium alloy Ti-6Al-4V, fatigue cracks initiate in "macrozones" of similarly oriented α grains. Correlating fractography, EBSD of the initiation site, and HR-EBSD or TEM of slip activity has shown that facets form on basal planes of grains loaded nearly perpendicular to their $c$-axis — a finding that changed forging-route specifications for jet-engine discs.
- **Additive manufacturing.** X-ray CT finds lack-of-fusion pores in a laser-powder-bed part; sectioning and EBSD show the columnar grains and melt-pool boundaries around them; fatigue testing of the same coupons links pore size and location to life (Chapter 40).
- **Corrosion.** Pit initiation sites on stainless steel are located by in-situ optical or electrochemical microscopy; SEM-EDS and TEM identify the manganese sulfide inclusions at their centres; atom-probe tomography reveals the chromium-depleted zone around the inclusion.
- **Biomaterials.** Correlative light and electron microscopy (CLEM) locates fluorescently labelled cells on an implant surface by light microscopy, then images the same cell–implant interface by FIB-SEM tomography, linking biological response to surface topography and chemistry (Chapter 31).
- **Batteries.** Operando X-ray tomography locates particles that crack early; the same electrode is then sectioned for EBSD and TEM of those particles, distinguishing cracks along grain boundaries of particular misorientation.

### Pitfalls

Correlation multiplies the uncertainty of registration with the uncertainties of each technique. Preparation for one method may alter the feature before the next: FIB lift-out introduces gallium, ion milling heats, polishing removes the surface oxide that XPS should have seen. The order of techniques must therefore be planned from least damaging to most damaging, and every step documented so that an artefact introduced in step 3 is not mistaken for a material feature in step 5.

---

## 44.8 Big data and automated analysis

### The data deluge

Modern detectors produce data faster than people can look at it. A **4D-STEM** experiment records a full two-dimensional diffraction pattern at each point of a two-dimensional scan (Chapter 43). With a $256\times256$ scan, a $256\times256$-pixel detector and 16-bit pixels, one data set is

$$
256^4\times2\ \mathrm{bytes}=8.59\times10^{9}\ \mathrm{bytes}\approx8.6\ \mathrm{GB}
$$

At 10,000 frames per second the scan takes 6.6 s and the camera streams 1.3 GB/s. A series of in-situ heating experiments repeating such scans every minute fills tens of terabytes in a day. Synchrotron tomography beamlines produce volumes of $2048^3$ voxels (about 17 GB at 16 bit) every second in fast mode. EBSD systems index more than 3,000 patterns per second. In-situ TEM video at 400 frames per second from a 4k camera overwhelms any manual analysis.

**Worked example — 4D-STEM data budget.** A group plans in-situ heating of a precipitation-hardening aluminium alloy, recording a $256\times256$ 4D-STEM scan every 30 s for a 2-hour anneal at 180 °C. The number of scans is $7200/30=240$, and the total data is $240\times8.59\ \mathrm{GB}=2.06\times10^{12}$ bytes ≈ 2.1 TB. Saving full patterns is possible but analysis on a workstation reading at 1 GB/s would take $2.06\times10^{12}/10^{9}\approx2{,}060$ s just to read once; any iterative fitting needs many passes. Two common decisions follow. Either reduce data at acquisition (compute strain maps or virtual images on the fly and keep only those, about 0.5 MB each instead of 8.6 GB), or bin the detector to $128\times128$, cutting the volume fourfold at some cost in angular resolution. The point is that the data plan must be designed with the experiment, not after it.

### Automated analysis

Three families of tools make such data useful.

**Physics-based processing pipelines.** Drift correction, background subtraction, pattern indexing, strain mapping by template matching, Rietveld refinement of thousands of diffraction patterns in sequence, and principal-component or non-negative matrix factorization of spectral images. **Dictionary indexing** of EBSD patterns compares each measured pattern with a library of simulated ones, recovering orientations from noisy patterns of deformed or fine-grained material where conventional Hough-based indexing fails.

**Machine-learning segmentation and classification.** Convolutional neural networks (the U-Net architecture is the workhorse) segment grains, pores, cracks, phases and precipitates in micrographs and tomograms after being trained on a few dozen annotated images; they classify dislocation types, identify defects in atomic-resolution images, and flag the rare frames of an in-situ video where something happens. Chapter 47 develops these methods.

**Autonomous and adaptive experiments.** When analysis runs as fast as acquisition, the instrument can decide what to measure next: a microscope that scans at low resolution, identifies grain boundaries or interfaces, and returns for high-resolution spectroscopy only there; a beamline that adapts the temperature ramp of an operando experiment to where a phase transition appears; a robot that synthesizes, characterizes and reformulates samples in a closed loop. These are the "self-driving laboratories" of Chapter 47.

Put side by side, these rates show that nearly every modern in-situ method produces data faster than a person, and many faster than a single workstation, can process.

### Reproducibility and data stewardship

Large automated data sets raise their own risks. Machine-learning segmentations can be confidently wrong on images unlike their training set; a pipeline with an undocumented threshold makes a result impossible to reproduce; and the selection of "representative" frames from terabytes of video can turn a rare event into an apparent rule. Good practice now includes:

- recording metadata (instrument, calibration, dose, temperature, timestamps) automatically with the data;
- following **FAIR** principles — data Findable, Accessible, Interoperable and Reusable — with open formats and persistent identifiers;
- publishing analysis code and trained models alongside results;
- reporting uncertainties, including those of the model (Chapter 47), and validating automated results against a manually analysed subset.

> **Status of the principle: Automated, data-driven analysis of characterization data**
> *Empirical.* Machine-learned segmentations and classifications are only as reliable as their training data and validation; they interpolate well within the conditions they were trained on and can fail silently outside them, so they need explicit uncertainty estimates and spot-checks against physics-based analysis.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How do the laboratory techniques (SEM, EBSD, TEM, XRD, DSC) used as the ex-situ baseline work? | Chapter 42 |
| How do synchrotron, neutron, atom-probe and aberration-corrected STEM methods produce the data used operando? | Chapter 43 |
| How are Mössbauer, NMR and positron parameters computed from first principles to assign spectra? | Chapter 45 |
| How are micropillar and in-situ straining results simulated with molecular dynamics, dislocation dynamics and crystal plasticity? | Chapter 46 |
| How are machine-learning models trained, validated and used for autonomous experiments? | Chapter 47 |
| What dislocation mechanisms do in-situ straining experiments reveal, and how do they set strength? | Chapters 12 and 13 |
| How do vacancies and their concentrations govern diffusion and ageing? | Chapters 5 and 8 |
| How do the battery and catalyst materials studied operando work and degrade? | Chapter 32 |
| How does irradiation damage form in reactor materials? | Chapter 33 |
| How are corrosion products and passive films formed and identified? | Chapters 34 and 35 |
| How are failures diagnosed in service by combining these methods? | Chapter 36 |

**Next:** Chapter 45 turns from measurement to calculation, showing how electronic-structure methods — density-functional theory above all — compute energies, structures and spectra from the Schrödinger equation, and where those calculations can and cannot be trusted.
