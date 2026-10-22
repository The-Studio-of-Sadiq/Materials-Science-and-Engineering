# Chapter 1 — The Materials Discipline

*Part I · Structure of Materials*

On 16 January 1943 the tanker SS *Schenectady*, newly completed and lying at her fitting-out pier in Portland, Oregon, broke in two with a noise heard a mile away. The sea was calm, the ship was unloaded and the air was a little below freezing. She was one of several thousand Liberty ships and T2 tankers built in the United States during the Second World War, the first large ships assembled by welding rather than riveting, and over the following years hundreds of them developed serious fractures; a dozen or so broke completely. The steel met its specification for tensile strength. What nobody had specified was how that steel behaved at a few degrees below zero with a notch in it. Plain carbon steels of that era, with high sulphur and phosphorus and a low manganese-to-carbon ratio, change from tough to brittle over a narrow temperature range that happened to sit near the temperature of the North Atlantic. Welding made each hull one continuous piece of metal, so a crack that started at a sharp hatch corner or a weld defect had no rivet seam to stop it. The cure came from three directions at once: chemistry and grain size that pushed the ductile–brittle transition below service temperatures, a design that removed sharp corners and added crack-arresting strakes of tougher steel, and a test (the notched-bar impact test, now routine) that measured the property that had been missing.

The *Schenectady* is the materials discipline in one story. A material is not a name or a single number on a datasheet; it is a structure, set by its chemistry and by how it was made, and that structure fixes a whole family of properties at once. Performance in service depends on all of them, including the ones nobody checked.

> **What is the materials discipline, and how does it connect the arrangement of atoms to the performance of a bridge, an aircraft or an implant?**
> **How do we organize the tens of thousands of engineering materials so that one can be chosen rationally over another, and what limits that choice beyond the properties themselves?**

| Concept | Engineering destination |
|---|---|
| Science versus engineering of materials; the history of materials | Reading specifications critically; recognizing that each era's limiting technology was a material |
| Structure–processing–property–performance tetrahedron | Failure analysis (Chapter 36); process specifications (Chapters 38–41) |
| Length and time scales | Choosing the right model and test; multiscale simulation (Chapter 46) |
| Material classes and property ranges | First screening of candidates for any component |
| Bonding as the origin of property classes | Predicting stiffness, melting point and expansion from chemistry |
| Isotropy, anisotropy, homogeneity | Rolled sheet, wood, fibre composites, single-crystal blades |
| Property charts and selection logic | Systematic material selection (Chapter 48) |
| Economics, criticality, sustainability | Supply-chain risk, cost, embodied carbon, circular design (Chapters 32, 48–49) |

**Roadmap.** What the discipline is and how it grew (1.1) → its organizing idea, the tetrahedron (1.2) → length and time scales (1.3) → material classes and their property ranges (1.4) → bonding as the reason the classes differ (1.5) → direction dependence and spatial uniformity (1.6) → property charts and selection (1.7) → materials in the economy and the environment (1.8).

---

## 1.1 Materials science and materials engineering

### Two questions about the same objects

**Materials science** asks *why*. Why does steel become brittle in the cold while aluminium does not? Why is a single-crystal turbine blade more creep resistant than a cast blade of the same alloy? Why does a ceramic hip head survive millions of cycles in the body when a glass of similar stiffness would shatter? The answers run from the arrangement of atoms and electrons to a measurable property. The science borrows from chemistry the nature of the bond and the thermodynamics and kinetics of change, and from physics the behaviour of electrons and lattice vibrations in a solid. What it adds is attention to the *real* arrangement of atoms, including its imperfections, and to how that arrangement changes during processing and in service.

**Materials engineering** asks *how*. How do we make a steel plate for a ship hull that is tough at −40 °C and still weldable? How do we cast a nickel alloy blade as one crystal, with internal cooling passages, at an acceptable scrap rate? How do we make a concrete that reaches 100 MPa yet still flows into congested formwork? The engineer uses the explanations of science to design a structure, then designs a manufacturing route that produces that structure reliably and cheaply.

The jet-engine turbine blade shows the two halves working together. The *science* was the discovery that nickel alloys gain their high-temperature strength from a dense dispersion of ordered Ni$_3$(Al,Ti) precipitates (the γ′ phase), and that creep at high temperature proceeds largely along grain boundaries, especially those lying across the stress. The *engineering* was a sequence of processing routes that removed those boundaries: conventionally cast equiaxed blades, then directionally solidified blades with columnar grains along the blade axis, and from the early 1980s single-crystal blades with no grain boundaries at all. Each step added a few tens of kelvin of allowable metal temperature; together with ceramic thermal-barrier coatings and internal cooling, they let turbine-entry temperatures rise from about 1100 K in early jet engines to over 1900 K today, well above the melting point of the blade alloy itself (Chapters 10, 16 and 33).

A datasheet value is an engineering fact about one grade made by one route; a scientific explanation tells you which way it moves when the grade or route changes.

> **Boundary.** The types of chemical bond, the laws of thermodynamics and reaction chemistry belong to the Advanced Chemistry book; the quantum mechanics of electrons in solids belongs to Engineering Physics. This book uses those results, recapping them where needed, and concentrates on how the arrangement of atoms in a solid, and its imperfections, produce engineering properties. Where the *Materials Core (EEE)* book treats an electronic topic in more depth, the text says so.

### A short history of materials ages

Historians name the early ages of humanity after their dominant material, and the names are well chosen: in each age, what people could build was limited by what they could make materials do.

- **Stone and natural materials.** Flint, obsidian, wood, bone, hide and fibre. Obsidian is a natural volcanic glass; with no crystal planes it fractures conchoidally and gives the sharpest edge of any natural material. Fired clay pottery, the first synthetic ceramic, appears around 18 000 years ago in East Asia.
- **Copper and bronze** (from about 5000 and 3300 BCE in the Near East). Copper was smelted from its ores and alloyed, first with arsenic and then with tin. Bronze (Cu with about 10 % Sn) is harder than copper and casts better because tin lowers the melting point: the first deliberate alloy design.
- **Iron** (from about 1200 BCE). Iron ore is far more abundant than copper and tin, but iron melts at 1538 °C, beyond ancient furnaces, so it was reduced in the solid state and forged. Smiths learned empirically that carburizing, quenching and tempering made iron hard: heat treatment, the control of structure by processing, three thousand years before anyone could see a microstructure.
- **Steel, cement and the industrial age** (from the nineteenth century). Portland cement (1824) and later reinforced concrete made the modern city; the Bessemer converter (1856) made cheap tonnage steel, and with it railways, ships and skyscrapers. The Hall–Héroult process (1886) turned aluminium from a precious metal into a structural one, and the discovery of age hardening in Al–Cu alloys (Alfred Wilm, 1906) made metal aircraft frames possible.
- **Polymers** (from 1907). Bakelite, the first fully synthetic plastic, was followed by polyethylene and nylon in the 1930s and the explosion of commodity plastics after 1950, from about 2 million tonnes a year in 1950 to more than 400 million tonnes today.
- **Silicon and electronic materials** (from 1947). The transistor and the integrated circuit depend on single crystals of a purity never needed before (Chapter 26).
- **Composites and designed materials** (from the 1960s). Carbon and aramid fibres, superalloys and single-crystal blades, high-performance concrete, biomaterials designed to be accepted or resorbed by the body, and materials designed atom by atom by computation (Chapters 45–47).

<!-- FIGURE 1.1 | figures/ch01/fig-1-1-materials-ages.png | plot | The relative importance of material classes over ten thousand years of engineering, with milestones marking the processes that changed it. | Content: x-axis time on a piecewise non-linear scale with ticks 10000 BCE, 5000 BCE, 0, 1000, 1500, 1800, 1900, 1950, 2000, 2025. y-axis "relative importance" 0–100 % (qualitative stacked areas) for natural materials (brown), ceramics and glass (red), metals (blue), polymers and elastomers (green), composites (purple), semiconductors (thin orange band after 1950). Metals peak around 1950–1960; polymers and composites grow after 1950. Milestone labels: bronze 3300 BCE, iron 1200 BCE, Portland cement 1824, Bessemer 1856, Hall–Héroult 1886, age hardening 1906, Bakelite 1907, transistor 1947, carbon fibre 1960s, single-crystal blades 1980s, graphene 2004. -->

Figure 1.1 sketches the changing mix. Metals peaked in the mid-twentieth century; since then polymers, composites and technical ceramics have taken share, while steel and concrete remain by far the largest materials by tonnage. The problem has shifted from finding *a* material that works to choosing the *best* one under many constraints (Sections 1.7–1.8).

---

## 1.2 The structure–processing–property–performance tetrahedron

### The four elements

- **Structure** is the arrangement of the material's constituents at every length scale: which atoms are present and how they are bonded; how they are arranged in a crystal or a glass; which defects that arrangement contains; how grains and phases are arranged in space; and the shape of the component.
- **Properties** are the material's responses to stimuli. A stress produces a strain (elastic modulus) or permanent deformation (yield strength); a temperature gradient produces a heat flow (thermal conductivity); a corrosive environment produces a reaction rate. A property is always a *relation between a stimulus and a response*, which is why it can depend on direction (Section 1.6).
- **Processing** is everything done to give the material its shape and structure: solidification, rolling and forging, heat treatment, sintering, polymerization and moulding, curing of concrete, deposition of thin films, joining, additive manufacturing. Processing is the engineer's control knob.
- **Performance** is the behaviour of the material *in a specific application*: the deflection of a floor beam, the number of flights a turbine disc survives, the wear of a hip-joint liner after twenty years, the life of a bridge deck exposed to de-icing salt. Performance combines properties with geometry, loading and environment.

<!-- FIGURE 1.2 | figures/ch01/fig-1-2-tetrahedron.png | schematic | The materials tetrahedron: processing, structure, properties and performance, with characterization at the centre, illustrated by a single-crystal turbine blade. | Content: tetrahedron in perspective with vertices Processing (bottom left), Structure (bottom right), Properties (bottom back), Performance (apex); sphere "Characterization" at the centre linked to all four. Solid arrows Processing → Structure → Properties → Performance; dashed arrow Performance → Processing labelled "redesign". Turbine-blade annotations: Processing "investment casting with grain selector; solution + ageing"; Structure "single crystal, [001] along axis, 65–70 vol % cuboidal γ′ ≈ 0.5 µm"; Properties "creep rupture ~1000 h at ~1050 °C, 140 MPa"; Performance "blade life > 20 000 h at turbine entry 1900 K". Small inset: the same tetrahedron for a concrete beam (mix design and curing → C–S–H, porosity, aggregate → 40 MPa, low chloride diffusivity → 100-year design life). -->

### The chain and its direction

The four ideas are usually drawn as a tetrahedron (Figure 1.2) or as a chain:

$$
\text{processing}\;\longrightarrow\;\text{structure}\;\longrightarrow\;\text{properties}\;\longrightarrow\;\text{performance}
$$

The chain has a definite direction of cause. Processing does not act on properties directly; it acts by changing structure. Quenching a steel does not "make it harder" by magic; it traps carbon in a distorted crystal structure (martensite) that resists dislocation motion. That is why a single structural change usually moves several properties at once, often in opposite directions from the designer's point of view. Cold-rolling an aluminium sheet multiplies its dislocations, doubling its yield strength but reducing its formability. Adding glass fibres to nylon triples its stiffness but makes it anisotropic and abrasive to moulding tools. Lowering the water–cement ratio of concrete raises its strength and its resistance to chloride penetration, but makes it harder to place and more prone to early-age shrinkage cracking. An engineer who asks for "more strength" is, without saying so, also asking for different ductility, toughness and manufacturability.

Design runs the chain backwards: from the performance required to the properties needed, to a structure that gives those properties, to a processing route that produces that structure. The step from properties to structure is the hard one, because many structures give the required value of one property but differ in the others.

### Characterization: closing the loop

The chain is useless unless each link can be measured. **Characterization** measures structure (optical and electron microscopy, X-ray and neutron diffraction, spectroscopy, tomography) and properties (mechanical, thermal, electrical and corrosion tests). It sits at the centre of the tetrahedron because it connects every link, and Part X (Chapters 42–44) is devoted to it. The Liberty-ship failures were understood only after impact tests on plates from fractured ships showed that plates in which fractures started had transition temperatures well above the water temperature.

### Structure-insensitive and structure-sensitive properties

A useful distinction separates

- **structure-insensitive** properties, fixed mainly by chemistry and crystal structure, which vary by only a few per cent between grades: density, elastic modulus of a fully dense polycrystal, melting point, heat capacity, thermal expansion, band gap; and
- **structure-sensitive** properties, controlled by defects and microstructure, which can vary by orders of magnitude between grades of the same material: yield strength, fracture toughness, fatigue limit, creep rate, corrosion rate, electrical resistivity at low temperature, magnetic coercivity, the permeability of concrete.

The Young's modulus of every carbon and low-alloy steel lies within a few per cent of 210 GPa; their yield strengths range from about 200 MPa to above 2000 MPa. Most properties that limit the life of a component belong to the second group, which is why this book spends Chapters 2–5 on structure and defects and Chapters 6–10 on the thermodynamics and kinetics that set them before it reaches mechanical behaviour.

> **Status of the principle: the structure–processing–property–performance paradigm**
> *Empirical.* It is an organizing framework distilled from practice rather than a law; it holds because properties are functions of structure and structure is a function of processing history, but it does not by itself predict any number.

---

## 1.3 Length and time scales from electrons to structures

### The ladder of length scales

"Structure" exists on many scales at once, and different properties are controlled at different scales (Figure 1.3).

**Electronic and atomic scale (about 0.01–1 nm).** Electrons forming bonds, the crystal structure and its unit cell, and point defects such as vacancies and solute atoms. The nearest-neighbour distance in iron is 0.248 nm; the Si–O bond in quartz and glass is 0.162 nm. Structure-insensitive properties are decided here.

**Nanoscale (about 1–100 nm).** Dislocation cores, strengthening precipitates (γ′ in superalloys, Guinier–Preston zones in aluminium alloys), the calcium silicate hydrate gel that binds concrete, the crystalline lamellae of polyethylene (10–20 nm thick), the mineral platelets in bone, thin films and coatings. When a structural dimension becomes comparable to a physical length of the electrons, phonons or dislocations that carry a property, the property itself changes (Chapter 30).

**Microscale (about 0.1–100 µm).** Grains, the phases of an alloy such as the lamellae of pearlite in rail steel, pores in a sintered ceramic, the 7 µm fibres of a carbon composite, spherulites in a polymer, wood cells, osteons in bone. This is what metallurgists usually mean by "microstructure"; strength, toughness and fatigue resistance are mostly set here.

**Meso- and macroscale (above about 0.1 mm).** Plies of a laminate, aggregate in concrete, weld beads and heat-affected zones, texture across a rolled sheet, cracks, and the shape of the component. Performance is finally determined here, by geometry combined with properties.

<!-- FIGURE 1.3 | figures/ch01/fig-1-3-length-time-scales.png | schematic | Length and time scales of materials structure and processes, from electrons to engineering structures, with the modelling methods that cover each range. | Content: x-axis length 10^-11 to 10^2 m (log), y-axis time 10^-15 to 10^10 s (log; right labels fs, ps, ns, µs, ms, s, hour, year, century). Shaded regions: "electronic structure / DFT" (10^-11–10^-9 m, 10^-15–10^-12 s); "molecular dynamics" (10^-10–10^-7 m, 10^-14–10^-8 s); "kinetic Monte Carlo, dislocation dynamics, phase field" (10^-8–10^-4 m, 10^-9–10^2 s); "crystal plasticity / continuum FEM" (10^-5–10^2 m, 10^-3–10^10 s). Labelled points: atomic vibration 10^-13 s at 0.25 nm; carbon in ferrite at 20 °C, 1 nm in 1 h; bake hardening 20 min at 180 °C over 0.33 µm; carburizing 4 h at 925 °C over 0.34 mm; precipitation ageing (hours, 10–50 nm); creep design life 10^5 h for power-plant pipe; concrete design life 100 years at 1–100 m. -->

### Time scales

Structure also lives on many *time* scales. Atoms vibrate about their sites with periods of about $10^{-13}$ s. A vacancy in copper near its melting point jumps roughly a billion times a second; at room temperature, far less often than once a second. Phase transformations take from microseconds (martensite) to hours (precipitation in aluminium alloys) to years (the slow ageing of polymers). Engineering design lives at the long end: a steam pipe is designed for $10^5$ hours of creep life, a bridge for 100 years. Between an atomic vibration and a century lie 22 orders of magnitude.

The bridge between atomic and engineering times is usually **thermal activation**. A process that requires atoms to overcome an energy barrier $Q$ runs at a rate proportional to $\exp(-Q/RT)$, where $R=8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$. For diffusion,

$$
D=D_0\exp\!\left(-\frac{Q}{RT}\right)
$$

and the typical distance an atom moves in time $t$ is of order $\sqrt{Dt}$. Chapter 8 derives both results from a random walk of atomic jumps.

> **Status of the principle: Arrhenius temperature dependence**
> *Approximate.* It follows from the Boltzmann probability of crossing a single energy barrier; it describes diffusion, creep and many reactions well over limited temperature ranges, but fails when the mechanism, and hence $Q$, changes with temperature.

**Worked example — Why carbon moves in a furnace but steel still ages at room temperature.** *Carburizing.* Gears are hardened by heating in a carbon-rich atmosphere so that carbon diffuses into austenite (face-centred cubic iron, Chapter 2), with $D_0=2.3\times10^{-5}\ \mathrm{m^2\,s^{-1}}$ and $Q=148\ \mathrm{kJ\,mol^{-1}}$. At 925 °C ($T=1198$ K),

$$
D=2.3\times10^{-5}\exp\!\left(-\frac{148\,000}{8.314\times1198}\right)=8.1\times10^{-12}\ \mathrm{m^2\,s^{-1}}
$$

and in 4 hours ($t=14\,400$ s) the characteristic depth is $\sqrt{Dt}=\sqrt{8.1\times10^{-12}\times14\,400}=3.4\times10^{-4}$ m $=0.34$ mm, the right order for a case-hardened gear tooth (the error-function solution of Chapter 8 gives case depths about twice this).

*Strain ageing.* Room temperature looks too cold for anything to happen, but carbon dissolved in ferrite (body-centred cubic iron) has a lower barrier: $D_0=1.1\times10^{-6}\ \mathrm{m^2\,s^{-1}}$, $Q=87.4\ \mathrm{kJ\,mol^{-1}}$. At 20 °C,

$$
D=1.1\times10^{-6}\exp\!\left(-\frac{87\,400}{8.314\times293.15}\right)=2.9\times10^{-22}\ \mathrm{m^2\,s^{-1}}
$$

In one hour $\sqrt{Dt}=\sqrt{2.9\times10^{-22}\times3600}=1.0\times10^{-9}$ m; in one day about 5 nm. A few nanometres is all a carbon atom needs to reach a nearby dislocation and pin it (Chapter 12). That is why mild-steel sheet stored for weeks after rolling develops a sharp yield point and shows stretcher-strain markings when pressed into a car panel. *Bake-hardening* steels turn the same physics to advantage: in the 20-minute paint bake at about 180 °C, $D$ rises to $9.3\times10^{-17}\ \mathrm{m^2\,s^{-1}}$, carbon moves about $\sqrt{9.3\times10^{-17}\times1200}=0.33$ µm, the dislocations introduced by pressing are pinned, and the yield strength of the finished panel rises by 30–60 MPa, improving dent resistance. One atomic mechanism links a furnace cycle, weeks of storage and a paint oven.

### Why scales interact

Three consequences recur throughout the book. **Properties are set at the scale of their carriers**: a crack a millimetre long sets the strength of a ceramic; precipitates tens of nanometres apart set the strength of an alloy. **Models are scale-specific**: electronic-structure calculations handle hundreds of atoms for picoseconds, continuum mechanics whole structures for decades; linking them is multiscale modelling (Chapter 46). **Tests are scale-specific**: when the feature that controls failure is rarer than a small specimen captures, small-specimen data overestimate strength and statistics enter (Chapters 11 and 14).

---

## 1.4 Material classes and their property ranges

### Why classify

Each class carries a recognizable *package* of properties. Knowing that a candidate is a polymer tells you, before you look at a datasheet, that it is light, insulating, poor at conducting heat, compliant, expands a lot on heating, is limited to a few hundred degrees Celsius and may creep at room temperature.

**Metals and alloys** are held together by metallic bonding, with valence electrons shared by the whole crystal (Section 1.5). The delocalized electrons give high electrical and thermal conductivity and opacity. The bonds are non-directional, so atoms pack densely (Chapter 2) and planes slide over one another by dislocation motion (Chapters 12–13), making metals ductile, tough and formable. Their strengths can be raised enormously by alloying and heat treatment. Steels are the backbone of civil and mechanical engineering; aluminium, titanium and magnesium alloys dominate where mass matters; nickel superalloys serve at the highest temperatures (Chapters 15–16).

**Ceramics** are compounds of metals with non-metals (oxides, nitrides, carbides), bonded ionically, covalently or by a mixture. They are stiff, hard, refractory, chemically stable and mostly insulating, but brittle, because dislocations hardly move in them; their tensile strength is controlled by the largest flaw and is therefore statistical (Chapter 14). Alumina and zirconia make cutting tools, hip heads and dental crowns; silicon carbide and nitride make bearings, seals and armour; refractories line furnaces; cement-based materials are ceramics too (Chapters 17–18).

**Glasses** are non-crystalline solids, usually silicate-based, though metallic and polymeric glasses exist. They share the stiffness, durability and brittleness of ceramics but, lacking crystals, are isotropic, can be transparent and are shaped as viscous liquids. Tempering and chemical strengthening, which put the surface in compression, multiply their usable strength (Chapter 17).

**Polymers and elastomers** are long-chain molecules, mostly carbon-based, bonded covalently along the chain and by weak van der Waals and hydrogen bonds between chains, or by occasional crosslinks in thermosets and elastomers. The weak interchain bonds explain their package: low density, low stiffness (typically 0.2–4 GPa; 1–10 MPa for elastomers), low softening temperatures, high expansion, low thermal conductivity and strongly time-dependent behaviour. Their advantages are easy processing into complex shapes, corrosion resistance and low cost (Chapters 19–21).

**Composites** combine materials so that the result has properties neither has alone. CFRP outperforms aluminium on stiffness and strength per unit mass; GFRP makes wind-turbine blades and boat hulls; reinforced concrete puts steel where concrete would crack in tension; wood and bone are natural composites. Their properties depend on the *arrangement* of the constituents as much as on their amounts, and they are usually strongly anisotropic (Section 1.6, Chapters 22–23).

**Semiconductors** are covalent solids whose band gap ($\sim$0.1–4 eV) lets their conductivity be controlled over many orders of magnitude by doping, temperature, light or field. Mechanically they behave like ceramics. Silicon dominates electronics and photovoltaics; SiC and GaN serve power electronics. Uniquely, they are used at near-perfect crystalline quality (Chapter 26; the *Materials Core (EEE)* book treats them in depth).

**Biomaterials** are defined by function, not bonding: materials intended to interact with the body, drawn from every other class. Titanium alloys and cobalt–chromium make joint replacements; alumina, zirconia, hydroxyapatite and bioactive glass make bearing surfaces and bone substitutes; ultra-high-molecular-weight polyethylene makes joint liners; biodegradable polyesters make sutures and scaffolds. What distinguishes them is the extra requirement of biocompatibility in a corrosive, cyclically loaded environment (Chapter 31).

### Representative property values

Table 1.1 collects typical room-temperature values; the property chapters give fuller data.

| Class | Material | Density (g cm$^{-3}$) | Young's modulus (GPa) | Strength (MPa) | Fracture toughness (MPa m$^{1/2}$) | Thermal conductivity (W m$^{-1}$ K$^{-1}$) | CTE (10$^{-6}$ K$^{-1}$) | Max. service T (°C, typical) |
|---|---|---|---|---|---|---|---|---|
| Metal | Structural steel S355 | 7.85 | 210 | 355 (yield) | 50–150 | 45–50 | 12 | 350–400 |
| Metal | Al alloy 6061-T6 | 2.70 | 69 | 275 (yield) | 25–30 | 167 | 23.6 | 150 |
| Metal | Ti-6Al-4V | 4.43 | 114 | 880 (yield) | 55–75 | 6.7 | 8.6 | 400 |
| Metal | Ni superalloy (IN718) | 8.19 | 200 | 1030 (yield) | 90–110 | 11 | 13 | 650 |
| Ceramic | Alumina (99.5 %) | 3.9 | 370 | 300–380 (flexure) | 3.5–4.5 | 30 | 8 | 1700 |
| Ceramic | Silicon carbide (sintered) | 3.15 | 410 | 400–550 (flexure) | 3–4 | 80–120 | 4.0 | 1600 |
| Ceramic | Concrete (C30/37) | 2.4 | 33 | 30–40 (compression), 2–3 (tension) | 0.2–1.4 | 1.5–2.5 | 10–12 | 300 |
| Glass | Soda-lime glass (annealed) | 2.5 | 70 | 30–70 (flexure) | 0.75 | 1.0 | 9 | 500 |
| Polymer | HDPE | 0.95–0.96 | 0.9–1.2 | 20–30 (yield) | 1–3 | 0.45–0.5 | 120–200 | 80 |
| Polymer | Epoxy (cast) | 1.2 | 2.5–3.5 | 60–80 (tension) | 0.5–0.8 | 0.2 | 55–65 | 130 |
| Elastomer | Natural rubber | 0.92 | 0.001–0.005 | 20–30 (tension) | — | 0.13 | 220 | 80 |
| Composite | CFRP, unidirectional (along fibres) | 1.55 | 135–140 | 1500–2000 (tension) | 30–45 (laminate) | 5–10 | −0.5 to 0.5 | 120–180 |
| Composite | Douglas fir (along grain) | 0.50 | 13 | 50 (compression) | 0.4–0.6 (across grain) | 0.12 (across) | 3–5 | 100 |
| Semiconductor | Silicon (single crystal) | 2.33 | 130–188 (by direction) | flaw-controlled | 0.8–0.9 | 148 | 2.6 | — |
| Biomaterial | Cortical bone | 1.9–2.0 | 15–20 | 100–150 (tension) | 2–12 | 0.3–0.6 | — | — |

Two features stand out. First, the ranges between classes are enormous: Young's modulus runs from about a megapascal for rubber to 410 GPa for silicon carbide, five orders of magnitude, and the expansion coefficients of materials that may be bonded together in one assembly (silicon 2.6, steel 12, epoxy about 60 ppm/K) differ by a factor of more than twenty, the root of the thermal-stress failures of Chapter 24. Second, within each class properties cluster: metals stiff and tough, ceramics stiff, hard and brittle, polymers compliant and light. Section 1.7 turns that clustering into a tool for selection.

### Exceptions show the logic

Classification is a starting point, not a law, and each exception has a structural reason. Diamond is an electrical insulator that conducts heat five times better than copper, because its light, stiff lattice scatters lattice vibrations little. Transformation-toughened zirconia reaches 8–12 MPa m$^{1/2}$ because a stress-induced phase change absorbs energy at a crack tip (Chapter 14). Drawn polyethylene fibres are stiffer than aluminium because their chains are loaded through their covalent backbones. Metallic glasses reach yield strengths near 2 GPa because they have no dislocations.

---

## 1.5 Bonding as the origin of property classes

### The bond types in brief

The Advanced Chemistry book develops chemical bonding; here we need only its consequences for solids.

- **Metallic.** Valence electrons are delocalized over the crystal. The bond is non-directional, so atoms pack densely and can change neighbours without the solid falling apart: hence ductility, conductivity and opacity.
- **Ionic.** Electrons are transferred and oppositely charged ions attract. The bond is strong and non-directional, but any shear that brings like ions into contact is resisted: hence stiffness, hardness, brittleness, high melting points and electrical insulation.
- **Covalent.** Atoms share electron pairs in bonds with definite directions. In a three-dimensional network (diamond, silicon, SiC, silica) the result is the hardest and stiffest of solids; in a polymer the strong bonds run only along the chain.
- **Secondary.** Van der Waals and hydrogen bonds between molecules are ten to a hundred times weaker. They hold polymer chains together, bind the layers of graphite and clays and govern the softening of thermoplastics.

Real materials usually mix bond types; the Si–O bond in silica is roughly half ionic, half covalent.

<!-- FIGURE 1.4 | figures/ch01/fig-1-4-bond-energy-curves.png | plot | Interatomic potential energy and force against separation for a strong, stiff bond and a weak, compliant bond, showing why stiffness, melting point and thermal expansion are linked. | Content: two panels, x-axis separation r/r0 from 0.7 to 2.5. (a) Morse-type U(r): deep narrow well labelled "strong bond (e.g. W, SiC), U0 ≈ 8 eV" and shallow wide well labelled "weak bond (e.g. Al, polymer interchain), U0 ≈ 1–3 eV"; minimum at r0; horizontal lines at two vibrational energies with the midpoint of each line marked by a dot, the dots drifting to larger r as energy rises, labelled "mean spacing grows → thermal expansion". (b) Force F = −dU/dr for both bonds; slope at r0 labelled "S0 = d²U/dr² → E ≈ S0/r0"; force maximum labelled "ideal strength". -->

### Stiffness from the bond curve

Figure 1.4 shows the potential energy $U(r)$ of two atoms against their separation $r$. Attraction dominates at large $r$ and repulsion at small $r$; the minimum, at the equilibrium spacing $r_0$, has depth $U_0$, the bond energy. Near the minimum the curve is close to a parabola, and the force $F=-dU/dr$ is proportional to the displacement, with stiffness

$$
S_0=\left(\frac{d^2U}{dr^2}\right)_{r=r_0}
$$

If each bond carries $F=S_0(r-r_0)$ and there is one bond per area $r_0^2$, the stress is $F/r_0^2$ and the strain $(r-r_0)/r_0$, so

$$
E\approx\frac{S_0}{r_0}
$$

Typical bond stiffnesses are 20–200 N/m for covalent bonds, 30–100 N/m for metallic bonds, 8–25 N/m for ionic bonds and only 0.5–2 N/m for van der Waals bonds; with $r_0\approx0.2$–0.3 nm these give moduli of hundreds of gigapascals for primary bonds and a few gigapascals for secondary bonds, just the spread between ceramics and metals on one hand and polymers on the other.

> **Status of the principle: modulus from bond stiffness, $E\approx S_0/r_0$**
> *Approximate.* It treats the solid as an array of independent springs; it gives the right order of magnitude and ranking for fully dense solids, but ignores bond angles, crystal anisotropy and, for elastomers, the entropic origin of stiffness (Chapters 11 and 20).

### Melting point and thermal expansion

A solid melts when thermal energy becomes comparable to a fraction of the bond energy, so deep wells mean high melting points. For metals the cohesive energy per atom divided by $k_BT_m$ ($k_B=8.617\times10^{-5}$ eV/K) is roughly 30: 29.8 for copper (3.49 eV, 1358 K), 27.4 for iron (4.28 eV, 1811 K), 28.0 for tungsten (8.90 eV, 3695 K), with outliers such as aluminium (42).

The curve is asymmetric: it rises steeply on compression and gently on extension. As an atom vibrates with more energy, the midpoint of its oscillation moves to larger $r$ (Figure 1.4a), so the solid expands on heating. Deep, symmetric wells expand little; shallow, asymmetric ones a lot. For many metals the product $\alpha T_m$ is nearly constant at about 0.02: 0.022 for copper, 0.021 for iron, 0.023 for nickel and 0.017 for tungsten. That is why refractory metals and ceramics have low expansion coefficients and polymers high ones (Chapter 24).

> **Status of the principle: correlations of bond energy with melting point and expansion ($E_{\mathrm{coh}}/k_BT_m\approx30$, $\alpha T_m\approx0.02$)**
> *Empirical.* Both are trends fitted across many metals and rationalized by the shape of the bond-energy curve; they hold to within about ±30 % for close-packed metals and fail for directional bonding or for materials whose liquid is bonded differently from the solid.

### From bond to class

| Bond type | Typical cohesive energy (eV per atom) | Example solids | Consequences for properties |
|---|---|---|---|
| Metallic | 1–9 | Na 1.1, Al 3.4, Cu 3.5, Fe 4.3, W 8.9 | Conductive, ductile, dense packing, moderate to high stiffness |
| Ionic | 3–8 (averaged over the formula) | NaCl 3.3, MgO 5.2, Al$_2$O$_3$ about 6 | Stiff, hard, brittle, insulating, high melting point |
| Covalent network | 4–8 | Si 4.6, SiC 6.3, diamond 7.4 | Hardest and stiffest solids, brittle, low density |
| Covalent chain + secondary | Chain bonds 3.5–4; interchain 0.05–0.5 | Polyethylene, nylon, epoxy | Compliant, light, low softening point, high expansion |
| Van der Waals | 0.02–0.1 | Solid Ar 0.08; graphite interlayers | Very soft, low melting point |
| Hydrogen | 0.1–0.5 | Ice; between nylon or cellulose chains | Raises stiffness and $T_g$ of polymers; water uptake |

Table 1.2 explains why the classes are classes, and why an engineer who needs a combination that no single bond type offers designs a composite.

---

## 1.6 Isotropy, anisotropy and homogeneity

### Properties as tensors

Many properties connect one vector or tensor to another: a temperature gradient to a heat flux, a stress to a strain. If the response is parallel to the stimulus and independent of direction,

$$
\mathbf q=-k\,\nabla T
$$

the material is **isotropic**. In general each component of the response depends on every component of the stimulus,

$$
q_i=-\sum_{j}k_{ij}\frac{\partial T}{\partial x_j},\qquad i,j\in\{1,2,3\}
$$

and the nine numbers $k_{ij}$ form a second-rank tensor. If they are not equivalent in all directions the material is **anisotropic**: heat flow is generally not parallel to the gradient. Thermal expansion and electrical conductivity are also second-rank tensors; elastic stiffness, relating stress to strain, is fourth-rank. Chapter 4 develops the tensor description and Neumann's principle; one consequence is worth stating now. Cubic crystals are isotropic in second-rank properties such as conductivity and expansion but anisotropic in elasticity: single-crystal iron has a Young's modulus of about 130 GPa along a cube edge and about 280 GPa along a body diagonal.

### Sources of anisotropy

- **Crystal structure.** Zinc expands four to five times more along its hexagonal $c$ axis than in the basal plane; graphite conducts heat several hundred times better within its layers than across them.
- **Crystallographic texture.** Processing can align the grains of a polycrystal. Textured aluminium sheet forms "ears" when deep-drawn into a beverage can; zirconium-alloy fuel cladding is given a texture so that brittle hydrides precipitate in a harmless orientation (Chapters 3 and 38).
- **Microstructural alignment.** Inclusions strung out by rolling make steel plate weaker through its thickness (a cause of lamellar tearing under welds); columnar grains form in castings and additively manufactured parts (Chapter 40).
- **Architecture.** Fibres in a composite, cells in wood, plies in a laminate, osteons in bone. Wood is about 10–20 times stiffer along the grain than across it.

Anisotropy is a resource when the loads are known: a CFRP wing skin puts its fibres along the load paths, and a single-crystal blade grown along its compliant $\langle001\rangle$ direction has lower thermal stresses.

### Homogeneity depends on the scale of observation

A material is **homogeneous** if its properties are the same at every point. The definition makes sense only once a scale is chosen. A steel beam is heterogeneous at the scale of micrometres, where grains and the ferrite and pearlite phases are visible, but homogeneous at the scale of millimetres. Concrete is heterogeneous at the scale of its aggregate and is treated as homogeneous only for volumes several times larger. The smallest volume that contains a representative sample of the microstructure is the **representative volume element** (RVE); over larger volumes the material has *effective properties*.

The idea fails when the component approaches the RVE: a stent strut 80 µm thick may hold only a few grains across its section, and such parts scatter from one to the next.

Homogeneity and isotropy are independent:

| | Isotropic | Anisotropic |
|---|---|---|
| **Homogeneous** | Glass; annealed polycrystalline steel (at mm scale) | Single-crystal turbine blade or sapphire window; textured sheet |
| **Heterogeneous** | Concrete; polymer with randomly dispersed particles | Unidirectional CFRP; wood; bone; reinforced concrete |

### Effective properties: the two simplest arrangements

For two phases with stiffnesses (or conductivities) $P_1$ and $P_2$ and volume fractions $f_1$ and $f_2=1-f_1$: when layers or fibres lie **parallel** to the load, both phases see the same strain and the responses add, like springs in parallel,

$$
P_\parallel=f_1P_1+f_2P_2
$$

and when layers lie **perpendicular** to the load, the same stress passes through each and the strains add, like springs in series,

$$
\frac{1}{P_\perp}=\frac{f_1}{P_1}+\frac{f_2}{P_2}
$$

Any other arrangement of the same phases at the same volume fractions lies between these two.

> **Status of the principle: Voigt–Reuss (Wiener) bounds**
> *Derived.* They follow from equilibrium and compatibility (equal strain or equal stress), or from flux conservation for conductivity; they are exact for ideal laminates and bound any two-phase arrangement with given volume fractions, provided the interfaces are perfect.

**Worked example — Anisotropy of a carbon-fibre ply.** A unidirectional CFRP ply contains $V_f=0.60$ carbon fibre with $E_f=230$ GPa in epoxy with $E_m=3.5$ GPa. Along the fibres,

$$
E_1=0.60\times230+0.40\times3.5=138+1.4=139.4\ \mathrm{GPa}
$$

Across the fibres,

$$
\frac{1}{E_2}=\frac{0.60}{230}+\frac{0.40}{3.5}=0.00261+0.1143=0.1169\ \mathrm{GPa^{-1}},\qquad E_2=8.6\ \mathrm{GPa}
$$

The ply is 16 times stiffer along its fibres than across them, though its composition is the same in every direction; only the arrangement differs. Measured values are about 135–140 GPa and 8–10 GPa. Two refinements explain the residual difference: carbon fibres are themselves anisotropic, with a transverse modulus of only about 15 GPa (lowering the series estimate to 6.5 GPa), and real fibres are not stacked in layers, so the transverse modulus lies above the series bound (the Halpin–Tsai equations of Chapter 22 interpolate). Laminates therefore stack plies at 0°, ±45° and 90° to give stiffness in every direction needed (Chapter 23), at the cost of a lower stiffness along any one direction, about 50–60 GPa for a quasi-isotropic layup.

---

## 1.7 Property charts and the logic of selection

### Function, constraints, objectives, free variables

Choosing a material is a design decision, made by stating clearly what is required:

- **Function**: what the component does. Support a load; contain a pressure; transmit heat; replace a joint.
- **Constraints**: requirements that must be met but bring no credit when exceeded. The beam must not deflect more than span/360; the implant must be biocompatible; the part must operate at 300 °C.
- **Objectives**: quantities to minimize or maximize. Mass, cost, embodied carbon, volume.
- **Free variables**: parameters the designer may adjust, such as a cross-section.

Constraints *screen*; objectives *rank*, through a performance index.

### Performance indices

Take a beam of square section $b\times b$ and length $L$ that must have bending stiffness at least $S$, with $b$ free and mass to be minimized:

$$
S=\frac{C\,E\,I}{L^3},\qquad I=\frac{b^4}{12},\qquad m=\rho\,b^2L
$$

where $C$ depends on loading and supports ($C=48$ for a simply supported beam loaded at mid-span). Eliminating $b$,

$$
m=\left(\frac{12\,S}{C}\right)^{1/2}L^{5/2}\;\frac{\rho}{E^{1/2}}
$$

The mass separates into a factor set by the design and a factor set by the material alone, so the best material maximizes the **performance index**

$$
M_{\mathrm{beam}}=\frac{E^{1/2}}{\rho}
$$

The same procedure gives $E/\rho$ for a stiff tie, $E^{1/3}/\rho$ for a stiff panel of free thickness and $\sigma_f^{2/3}/\rho$ for a strong beam. A tie uses its material uniformly; a beam or panel gains stiffness faster than mass by getting deeper, so a light material that can be made thicker is favoured.

> **Status of the principle: performance index**
> *Derived.* It follows algebraically from the model of the component (here elastic bending of a given shape); it is only as valid as that model and ranks materials for one objective under the stated constraints, ignoring any requirement not written into the equations.

### Property charts

A **property chart** (Ashby chart) plots one property against another for all materials on logarithmic axes (Figure 1.5). Because classes cluster, each occupies a recognizable bubble. On log axes an index becomes a straight line: $E^{1/2}/\rho=\text{constant}$ is $\log E=2\log\rho+\text{constant}$, slope 2; $E/\rho$ gives slope 1 and $E^{1/3}/\rho$ slope 3. Materials on a line perform equally well; those above it, better. Selection becomes geometric: slide the line upward until only a handful of candidates remain above it.

<!-- FIGURE 1.5 | figures/ch01/fig-1-5-modulus-density-chart.png | map | Property chart of Young's modulus against density for engineering materials, with guide lines for minimum-mass ties, beams and panels. | Content: log–log axes; x-axis density 0.01 to 30 g/cm³; y-axis Young's modulus 10^-4 to 10^3 GPa. Translucent class envelopes: foams (0.02–0.5, 10^-3–1), elastomers (0.9–1.3, 10^-3–0.1), polymers (0.9–2.2, 0.2–4), natural materials (wood along/across grain, bamboo, bone, cork: 0.1–2, 0.005–30), composites (GFRP, CFRP: 1.5–2.0, 15–220), metals (Mg 1.8/45, Al 2.7/70, Ti 4.4/114, steel 7.85/210, Cu 8.9/120, W 19.3/410), technical ceramics (alumina 3.9/370, SiC 3.15/410, Si3N4 3.2/310, diamond 3.5/1050), glasses (2.2–2.6, 60–90), concrete and stone (1.9–2.7, 20–70). Labelled points for the worked example: steel, Al alloy, Ti-6Al-4V, Mg alloy, GFRP (1.9, 25), CFRP quasi-isotropic (1.55, 60), Douglas fir along grain (0.50, 13). Parallel dashed guide lines of slope 1 "E/ρ (tie)", slope 2 "E^1/2/ρ (beam)" and slope 3 "E^1/3/ρ (panel)", arrow "search region" to upper left. -->

**Worked example — Choosing a light, stiff beam, and asking what it costs.** A simply supported beam of span $L=3$ m with square section must have mid-span stiffness $S=1.0\times10^6$ N/m ($C=48$). For steel ($E=210$ GPa, $\rho=7850\ \mathrm{kg\,m^{-3}}$),

$$
I=\frac{SL^3}{CE}=\frac{1.0\times10^6\times27}{48\times210\times10^9}=2.68\times10^{-6}\ \mathrm{m^4},\qquad b=(12I)^{1/4}=75.3\ \mathrm{mm}
$$

$$
m=7850\times(0.0753)^2\times3=133.5\ \mathrm{kg}
$$

Repeating for the other candidates, and multiplying mass by indicative prices and cradle-to-gate embodied carbon (both vary widely with grade, region and recycled content):

| Material | $E$ (GPa) | $\rho$ (kg m$^{-3}$) | $E^{1/2}/\rho$ (GPa$^{1/2}$ per Mg m$^{-3}$) | $b$ (mm) | Mass (kg) | Price (USD/kg) | Cost (USD) | CO$_2$ (kg/kg) | CO$_2$ (kg) |
|---|---|---|---|---|---|---|---|---|---|
| Steel | 210 | 7850 | 1.85 | 75.3 | 134 | 0.8 | 107 | 1.9 | 254 |
| Al alloy | 70 | 2700 | 3.10 | 99.1 | 80 | 2.5 | 199 | 12 | 954 |
| Ti-6Al-4V | 114 | 4430 | 2.41 | 87.7 | 102 | 20 | 2045 | 40 | 4091 |
| Mg alloy | 45 | 1800 | 3.73 | 110.7 | 66 | 4 | 265 | 25 | 1653 |
| GFRP | 25 | 1900 | 2.63 | 128.2 | 94 | 4 | 375 | 6 | 562 |
| CFRP (quasi-isotropic) | 60 | 1550 | 5.00 | 103.0 | 49 | 40 | 1973 | 25 | 1233 |
| Douglas fir (along grain) | 13 | 500 | 7.21 | 151.0 | 34 | 1.5 | 51 | 0.3 | 10 |

The masses follow the index exactly: any two masses are in the inverse ratio of their indices (steel to CFRP, $5.00/1.85=2.7$). Three lessons follow. First, timber is the lightest of all for a stiffness-limited beam, which is why wood, bamboo and bone are so efficient in bending; titanium, a "light" metal, loses to aluminium and magnesium here because its modulus is not high enough for its density. Second, the ranking changes completely with the objective: on cost, timber and steel win and titanium and CFRP lose by a factor of about 20; on embodied carbon, timber wins by a factor of 25 over steel, and primary aluminium is nearly four times worse than steel. Third, the index ignores everything not written into it: timber needs a 151 mm section, creeps under sustained load and is vulnerable to fire and moisture; CFRP needs different joining. An aircraft floor beam, a bicycle frame and a building joist face the same equations but weigh mass, cost and carbon differently, and so choose differently.

### The general method

The procedure, developed fully in Chapter 48, is: translate the requirement into function, constraints, objectives and free variables; screen out every material that violates a constraint; rank the survivors by the index on a property chart; examine the leaders for secondary properties, manufacturability, joining, reliability, cost and supply; decide, and document why. When objectives conflict, as mass and cost do above, no single material is best. The useful set is the **Pareto front**: materials for which no other candidate is better in one objective without being worse in another (Chapter 48).

---

## 1.8 Materials and society: economics, criticality, sustainability

### The scale of materials use

Humanity uses materials in staggering quantities, dominated by a few cheap structural materials (Table 1.3).

| Material | Annual global production (order of magnitude) | Typical price (USD/kg, indicative) | Embodied CO$_2$ (kg CO$_2$e per kg, typical cradle-to-gate) |
|---|---|---|---|
| Concrete | 25–30 billion tonnes | 0.05–0.1 | 0.1–0.2 |
| Cement | about 4 billion tonnes | 0.1 | 0.6–0.9 |
| Steel | about 1.9 billion tonnes | 0.6–1 | 1.4–2.3 (primary); 0.4–0.7 (scrap-based electric arc) |
| Plastics | about 0.4 billion tonnes | 1–3 (commodity) | 2–4 |
| Glass | about 0.15 billion tonnes | 0.5–1 | 0.7–1.2 |
| Aluminium (primary) | about 70 million tonnes | 2–3 | 8–17 (depends on electricity source) |
| Copper (refined) | about 26 million tonnes | 8–10 | 3–5 |
| Carbon fibre | about 0.1–0.2 million tonnes | 20–50 | 20–40 |

Cement and steel production each account for roughly 7–8 % of global anthropogenic CO$_2$ emissions; calcining limestone (CaCO$_3$ → CaO + CO$_2$) and reducing iron oxide with carbon release CO$_2$ whatever the fuel (Chapters 18 and 49).

### Economics

Three economic facts shape material choice. **Material cost is often a small part of component cost**: for a turbine blade or an implant, processing, qualification and certification dominate; for a building, the material is a large share. **Prices are volatile**: copper, nickel, cobalt and lithium have each doubled or halved within a few years, which pushes designers toward substitutable materials. **Mass has a lifetime cost in transport**: removing a kilogram from a car saves fuel worth a few dollars over its life; from a commercial aircraft, hundreds to thousands of dollars. This value of mass saving decides whether expensive light materials pay off, and explains why CFRP is common in aircraft and rare in buildings.

### Criticality

A material is **critical** when it is economically important and its supply is at risk, because mining or refining is concentrated in a few countries, substitutes are poor, recycling is low or it is produced only as a by-product of another metal. Most rare-earth separation (about 90 %), needed for the neodymium–iron–boron magnets of wind turbines and electric motors, takes place in China; about 70 % of cobalt for battery cathodes comes from the Democratic Republic of the Congo; gallium is almost entirely a by-product of alumina refining; about 90 % of niobium for high-strength low-alloy steels comes from Brazil. Criticality assessments plot supply risk against economic importance (Figure 1.6).

<!-- FIGURE 1.6 | figures/ch01/fig-1-6-criticality-map.png | plot | A criticality assessment places each raw material by economic importance and supply risk; materials in the upper right are critical. | Content: x-axis "economic importance" 0–10, y-axis "supply risk" 0–5, shaded critical region above supply risk 1.0 and right of importance 2.8 (schematic, in the style of EU assessments). Indicative points with labels: heavy rare earths (6, 4.5), light rare earths (5, 3.8), gallium (4, 3.9), magnesium (7, 4.0), niobium (6, 3.9), tungsten (8, 1.3), cobalt (6.5, 2.5), platinum-group metals (6, 2.4), lithium (4, 1.9), natural graphite (3, 1.8), silicon metal (5, 1.2), titanium (5, 1.3), bauxite (5.5, 1.0), copper (5.5, 0.3), nickel (5, 0.5), iron ore (6.5, 0.6), limestone (3, 0.2). Annotations: "by-product metal" at Ga; "single-country supply" at rare earths and Nb. -->

Materials engineering responds by **substitution** (magnets that need less dysprosium because it is diffused only into grain boundaries; iron-phosphate battery cathodes instead of cobalt-rich ones), **thrifting** (thinner platinum catalyst layers) and **recycling** (Chapter 49). Each depends on knowing which structural feature delivers the property, so that the scarce element is used only where it matters.

### Sustainability

Sustainability adds the whole lifecycle to selection: extraction, processing, manufacture, use and end of life. Its first quantitative tools are **embodied energy** and **embodied carbon** per kilogram (Table 1.3) and the **lifecycle assessment** that combines them with the use phase (Chapter 49). The beam example of Section 1.7 shows how much the ranking changes when carbon is the objective. The use phase may dominate: a lighter car or aircraft that burns less fuel over its life can justify aluminium or CFRP, while a component sitting in a building wall for 60 years gains nothing from lightness and should minimize embodied carbon.

Three principles connect sustainability back to structure. **Durability** divides embodied impacts over more years: a bridge deck whose concrete resists chloride ingress for 100 years rather than 40 is more sustainable even if it uses more cement. **Recyclability** depends on composition: aluminium can be remelted with about 5 % of the energy of primary production, but mixing alloys accumulates iron and copper that are hard to remove, and thermoset composites are hard to separate at all. **Design for disassembly** and alloy simplification keep materials in circulation. The circular economy is ultimately a materials-engineering problem: designing structures that can be recovered without losing the properties that made them valuable.

> **Status of the principle: embodied-carbon and lifecycle figures**
> *Empirical.* They are inventory data from industrial surveys; they vary by a factor of two or more with region, electricity mix, recycled content and system boundary, so they rank options and identify hot spots rather than serving as precise constants.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are atoms arranged in metals, ceramics, silicates, glasses and polymers, and how are directions and planes named? | Chapter 2 |
| What symmetry do crystals have, and why do only certain lattices exist? | Chapter 3 |
| How are tensor properties formulated, and why are cubic crystals elastically anisotropic? | Chapter 4 |
| What defects do real materials contain, and why do structure-sensitive properties depend on them? | Chapter 5 |
| How do thermodynamics and kinetics decide which structure forms, and how are carburizing depths calculated? | Chapters 6–10 (diffusion in Chapter 8) |
| Why does steel become brittle in the cold, and how is toughness measured? | Chapters 11 and 14 |
| What controls strength, and how do pinned dislocations cause strain ageing? | Chapters 12–13 |
| How are composite stiffnesses predicted beyond the simple bounds, and laminates designed? | Chapters 22–23 |
| How are thermal stresses from expansion mismatch calculated? | Chapter 24 |
| How are single-crystal blades and other high-temperature materials designed? | Chapters 16 and 33 |
| How are multiple objectives, shape and processing combined in selection? | Chapter 48 |
| How are embodied carbon, lifecycle assessment, criticality and recycling handled quantitatively? | Chapter 49 |

**Next:** Chapter 2 describes the atomic arrangements on which everything else is built: lattices and unit cells, the crystal structures of metals, ceramics and silicates, the notation for directions and planes, polycrystals and texture, and the non-crystalline and partly ordered solids — glasses, polymers, liquid crystals and quasicrystals.
