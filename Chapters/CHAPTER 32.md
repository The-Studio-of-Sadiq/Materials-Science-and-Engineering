# Chapter 32 — Materials for Energy

*Part VII · Advanced and Emerging Materials*

A city transit authority orders three hundred electric buses and must choose between two battery chemistries. Cells with a nickel-rich layered-oxide cathode store about a quarter more energy per kilogram. Cells with an iron-phosphate cathode are heavier but cheaper, contain no cobalt or nickel, survive two to three times as many cycles and are far less prone to thermal runaway in a depot full of parked vehicles. The authority picks iron phosphate. In the same month, a pipeline operator learns that fatigue cracks in the steel of a gas line it hoped to convert would grow ten to a hundred times faster in hydrogen, and an electrolyser maker discovers that the world mines less iridium in a year than its order book needs. Each was a materials decision, and in none did the best laboratory figure of merit win outright. Energy materials must be deployed at the scale of the whole energy system, last for decades and be cheap per unit of energy delivered over their life; this chapter surveys them with those constraints in view.

> **Which structural features make a material a good light absorber, battery electrode, ion conductor, catalyst, thermoelectric or capacitor electrode?**
> **Why do the materials with the best figures of merit so often lose to cheaper, more durable or more abundant ones?**

| Concept | Engineering destination |
|---|---|
| Absorber band gap, absorption coefficient, defect tolerance | Choice of photovoltaic technology; module efficiency and lifetime |
| Intercalation hosts, specific capacity, volume change | Cell chemistry for vehicles, grid storage, consumer devices, aircraft |
| Liquid, polymer and ceramic electrolytes | Solid-state batteries, safety of cells and packs |
| Proton and oxide-ion conductors, catalysts, interconnects | PEM and solid-oxide fuel cells and electrolysers |
| Hydride thermodynamics, embrittlement of steels | Hydrogen tanks, pipelines, fittings and refuelling stations |
| Seebeck coefficient, figure of merit $ZT$ | Waste-heat recovery, Peltier coolers, radioisotope generators |
| Double-layer and pseudocapacitive storage | Regenerative braking, grid frequency support, crane and lift buffers |
| Fuel and cladding requirements | Fission power (developed in Chapter 33) |
| Material intensity, critical raw materials | Supply risk and the deployable scale of each technology |

**Roadmap.** Converting light (32.1) → storing charge in electrode hosts (32.2) and carrying ions through electrolytes (32.3) → converting fuel and making hydrogen (32.4) → storing hydrogen and resisting it (32.5) → converting heat (32.6) → storing charge at surfaces (32.7) → nuclear fuels in brief (32.8) → degradation, critical materials and scale (32.9).

> **Boundary.** Electrode potentials, the Nernst equation, Faraday's laws and reaction kinetics are electrochemistry fundamentals from the Advanced Chemistry book; they are used here without derivation (Chapter 34 applies them to corrosion). Band structure and carrier transport are in Chapter 26, light absorption in Chapter 28, ionic conduction in Chapter 25. Sizing of packs, stacks, arrays and power electronics is systems engineering, outside this book. The *Materials Core (EEE)* book treats photovoltaic, thermoelectric and battery materials at greater electronic depth.

---

## 32.1 Photovoltaic absorbers

### What a good absorber must do

The thermodynamic limit for a single-junction solar cell under the unconcentrated solar spectrum is the detailed-balance (Shockley–Queisser) efficiency, about 33 % at a band gap near 1.34 eV (Chapters 26 and 28). The maximum is flat: any gap between roughly 1.1 and 1.6 eV allows more than 30 %. So the band gap narrows the search but does not decide it. A practical absorber must in addition:

1. **Absorb strongly** so that it can be thin. Direct-gap semiconductors reach absorption coefficients $\alpha$ of $10^4$–$10^5$ cm$^{-1}$ just above the gap; indirect-gap silicon manages $10^2$–$10^3$ cm$^{-1}$ in the near infrared, because a phonon must take part in each absorption event.
2. **Let carriers reach the contacts before they recombine.** The minority-carrier diffusion length $L=\sqrt{D\tau}$ must exceed the absorber thickness. The lifetime $\tau$ is set by recombination through deep levels of point defects, dislocations and grain boundaries (Chapter 5), so this is a statement about defect chemistry.
3. **Be either nearly perfect or defect-tolerant.** Silicon and GaAs succeed because they can be grown with vanishingly few deep-level defects; CdTe, CIGS and the halide perovskites succeed because their native defects and grain boundaries happen to be electrically benign or can be made so.
4. **Survive** 25–30 years of ultraviolet light, module temperatures up to about 85 °C, humidity and thermal cycling, and be made cheaply from available elements.

**Worked example — how thick must the absorber be?** By the Beer–Lambert law the fraction of light absorbed in one pass through a thickness $t$ is $1-e^{-\alpha t}$. Absorbing 90 % needs $e^{-\alpha t}=0.1$, so $t=\ln 10/\alpha=2.303/\alpha$.

- Crystalline silicon at 900 nm, $\alpha\approx306$ cm$^{-1}$: $t=2.303/306=7.5\times10^{-3}$ cm, or 75 µm.
- CdTe at 800 nm, $\alpha\approx1\times10^4$ cm$^{-1}$: $t=2.3\times10^{-4}$ cm, or 2.3 µm.
- A lead halide perovskite at 600 nm, $\alpha\approx5\times10^4$ cm$^{-1}$: $t=4.6\times10^{-5}$ cm, or 0.46 µm.

Silicon needs some thirty times the thickness of CdTe and about 160 times that of the perovskite. Surface texturing and rear reflectors lengthen the light path (ideally by up to $4n^2\approx50$ for a randomizing surface), which is why commercial wafers are 130–160 µm thick rather than several hundred. The thin-film absorbers need only micrometres, so their carriers have to travel only micrometres, and polycrystalline films deposited cheaply on glass or foil are good enough (Figure 32.1).

> **Status of the principle: Beer–Lambert absorption**
> *Approximate.* Exact for a homogeneous, non-scattering medium in a single pass; light trapping, thin-film interference and photon recycling modify it in real cells.

<!-- FIGURE 32.1 | figures/ch32/fig-32-1-pv-absorption-coefficients.png | plot | Direct-gap thin-film absorbers absorb sunlight within a micrometre or two, whereas indirect-gap silicon needs about a hundred. | Content: log y-axis absorption coefficient 10^1-10^6 cm^-1 vs photon energy 1.0-3.0 eV (top axis wavelength 1240-410 nm). Curves: c-Si (slow rise from 1.12 eV, ~3x10^2 at 1.38 eV/900 nm, ~10^3 at 1.5 eV, ~10^4 near 2.5 eV), GaAs (sharp edge at 1.42 eV to ~10^4), CdTe (edge 1.45-1.5 eV, ~10^4 at 1.55 eV/800 nm, ~5x10^4 by 2 eV), CIGS (edge ~1.15 eV), FAPbI3-type perovskite (edge ~1.55 eV, ~5x10^4 at 2.07 eV/600 nm). Right y-axis: 90 % absorption depth 2.303/alpha from 230 um to 0.046 um. Faint AM1.5G spectrum shape in background. -->

### Crystalline silicon

About 95 % of the photovoltaic capacity installed each year is crystalline silicon: its 1.12 eV gap is near the optimum, the element is abundant, and microelectronics has made it the purest crystal produced at scale. Minority-carrier lifetimes above 1 ms in n-type wafers give millimetre diffusion lengths, more than compensating for weak absorption. The frontier is now at **surfaces and contacts**, where passivating layers (SiO$_2$ tunnel oxide plus doped polysilicon in TOPCon cells, amorphous silicon in heterojunction cells) suppress recombination; records exceed 27 % against a practical limit of about 29.4 % set by Auger recombination. Bulk degradation is point-defect chemistry: boron–oxygen complexes cause light-induced degradation in p-type wafers, one reason for the move to n-type.

### CdTe and CIGS

**Cadmium telluride** (direct gap 1.45–1.5 eV), deposited a few micrometres thick onto glass at 500–600 °C, is the most successful thin film. Its grain boundaries, normally fatal in a polycrystalline semiconductor, are made benign by a CdCl$_2$ treatment near 400 °C. Modules reach 19–20 %; the liabilities are cadmium toxicity, handled by encapsulation and take-back recycling, and tellurium supply (Section 32.9).

**Cu(In,Ga)Se$_2$ (CIGS)** is a chalcopyrite whose gap rises from 1.0 to 1.7 eV with Ga/(In+Ga); grading it through the film builds in a field that drives electrons to the junction, and alkali atoms passivate its grain boundaries. Deposited on steel or polyimide foil, it gives flexible modules for façades and vehicles, at the cost of multi-element process control and indium and gallium supply.

### Halide perovskites

Metal halide perovskites ABX$_3$ (A = methylammonium, formamidinium or Cs; B = Pb or Sn; X = I, Br, Cl) went from first use as absorbers in 2009 to certified single-junction efficiencies near 27 % in about fifteen years. Three structural features explain the speed:

- **A direct, tunable gap**, from about 1.5 eV (FAPbI$_3$) to 2.3 eV (pure bromide), adjustable by halide mixing, which suits them for the top cell of a tandem.
- **Strong absorption**: half a micrometre absorbs most above-gap light, as the worked example showed.
- **Defect tolerance**: the dominant native defects, vacancies, form shallow rather than deep levels because the band edges derive from antibonding orbitals. Films spin-coated or slot-die coated from solution and annealed near 100 °C have diffusion lengths above 1 µm.

The soft, ionic lattice that makes them easy to process is also their weakness. Halide vacancies migrate under light and field, causing hysteresis, halide segregation and electrode corrosion; moisture and heat decompose them; and each square metre contains a few grams of soluble lead. Caesium–formamidinium compositions and barrier encapsulation have improved stability greatly, though not yet to silicon's 25-year standard. The most promising route is the **perovskite-on-silicon tandem**, which has exceeded 34 %, beyond any single-junction limit.

### III–V multijunctions and the space market

Epitaxial GaAs reaches about 29 % as a single junction, closest of any material to its limit. Stacking junctions (GaInP 1.9 eV / GaAs 1.42 eV / Ge 0.67 eV, or newer four- to six-junction designs) gives each part of the spectrum a matching gap and cuts thermalization loss, to about 39 % at one sun and 47 % under concentration. Single-crystal substrates and slow epitaxy (Chapter 41) make them 100–1000 times costlier per unit area than silicon, so they are used where watts per kilogram and radiation hardness justify any cost: satellites and high-altitude aircraft (Chapter 33).

**Table 32.1 — Photovoltaic absorbers (typical values; records as of the mid-2020s, rounded).**

| Absorber | Band gap (eV) | Gap type | Typical thickness | Record cell efficiency | Main materials limitation |
|---|---|---|---|---|---|
| c-Si (monocrystalline) | 1.12 | Indirect | 130–160 µm | ≈27 % | Weak absorption; surface recombination; Ag contacts |
| CdTe | 1.45–1.5 | Direct | 2–4 µm | ≈23 % | p-doping; Te supply; Cd toxicity |
| CIGS | 1.0–1.2 (graded) | Direct | 1.5–2.5 µm | ≈23.6 % | Process complexity; In and Ga supply |
| Halide perovskite | 1.5–1.7 (to 2.3) | Direct | 0.4–0.8 µm | ≈27 % (≈34 % on Si tandem) | Ion migration; moisture and heat stability; Pb |
| GaAs | 1.42 | Direct | 1–3 µm | ≈29 % | Substrate and growth cost |
| III–V multijunction | 0.7–1.9 stack | Direct | 5–10 µm total | ≈39 % (1 sun), ≈47 % (concentrated) | Cost; space and concentrator niches |

---

## 32.2 Battery materials I: intercalation electrodes

### Storing ions in a host

A lithium-ion cell stores energy by moving Li$^+$ ions between two host materials through an electrolyte while electrons travel through the external circuit. On discharge, lithium leaves the negative electrode (conventionally the anode) and enters the positive electrode (the cathode). The best hosts work by **intercalation**: ions slide into vacant sites between layers or along channels of a crystal whose framework stays essentially intact, and an equal number of electrons reduces a transition metal (or carbon) in the host. For a layered oxide cathode,

$$
\mathrm{Li_{1-x}CoO_2}+x\,\mathrm{Li^+}+x\,e^-\ \rightleftharpoons\ \mathrm{LiCoO_2}
$$

The cell voltage equals the difference in lithium chemical potential between the two electrodes divided by the elementary charge; why that difference takes the value it does is electrochemistry. The materials questions are four: how much lithium the host accepts per unit mass (**capacity**), at what potential, how fast ions and electrons move through it (**rate**), and how much the lattice changes when they do (**cycle life**). The same logic applies to sodium-ion, magnesium-ion and other intercalation chemistries.

### Specific capacity

If a host of molar mass $M$ (g/mol) reversibly exchanges $n$ electrons and ions per formula unit, Faraday's constant gives its theoretical **specific capacity**

$$
Q=\frac{nF}{3.6\,M}\quad(\mathrm{mAh\,g^{-1}})
$$

where the factor 3.6 converts coulombs per gram into milliampere-hours per gram.

> **Status of the principle: theoretical specific capacity**
> *Derived* from Faraday's law and stoichiometry. Practical capacities are lower because only part of the lithium can be cycled without destroying the host, and because binder, conductive carbon, current collectors and electrolyte add inactive mass.

**Worked example — capacities of common electrodes.** With $F=96\,485$ C/mol:

- Graphite to LiC$_6$, one Li per six carbons, $M=6\times12.011=72.07$ g/mol: $Q=96\,485/(3.6\times72.07)=372$ mAh/g.
- LiCoO$_2$, $M=97.87$: $Q=274$ mAh/g theoretical. Only about 0.5–0.65 Li can be removed before the layered structure transforms and loses oxygen, so practical values are 140–185 mAh/g.
- LiFePO$_4$, $M=157.76$: $Q=170$ mAh/g; practical 155–165 mAh/g, since nearly all the lithium can be cycled.
- LiNi$_{0.8}$Mn$_{0.1}$Co$_{0.1}$O$_2$ (NMC811), $M=97.28$: $Q=276$ mAh/g theoretical, about 200 mAh/g practical.
- Silicon to Li$_{15}$Si$_4$, 3.75 Li per Si, $M=28.09$: $Q=3.75\times96\,485/(3.6\times28.09)=3578$ mAh/g, almost ten times graphite.
- Li$_4$Ti$_5$O$_{12}$ to Li$_7$Ti$_5$O$_{12}$, three Li per formula unit, $M=459.1$: $Q=175$ mAh/g.

### Anode materials

**Graphite** is the near-universal anode. Lithium enters between the graphene layers in ordered stages up to LiC$_6$ at 0.05–0.25 V versus Li/Li$^+$, with only about 10 % volume expansion. The low potential is also its difficulty: no practical organic electrolyte is stable there, and on the first charge the electrolyte is reduced to a nanometre-scale **solid–electrolyte interphase** (SEI) of lithium carbonate, fluoride and organic salts. A good SEI conducts Li$^+$ but not electrons and so stops further reaction; its formation consumes 5–10 % of the cell's lithium, and its slow growth is the main ageing mechanism of most cells. At high charging rates or low temperature lithium plates as metal on the graphite instead, which usually limits fast charging.

**Silicon** stores lithium by **alloying**, at about 0.4 V, with a volume expansion of about 280 %. Micrometre particles crack on the first cycles (Chapter 14), lose contact and expose fresh surface that grows new SEI. Nanostructuring is the remedy (Chapter 30): particles below about 150 nm do not fracture, and SiO$_x$ or porous Si–C composites buffer the swelling. Commercial anodes blend 5–15 % silicon or SiO$_x$ into graphite.

**Lithium titanate** (spinel Li$_4$Ti$_5$O$_{12}$) changes volume by only about 0.2 % and works at 1.55 V, above the potential where the electrolyte is reduced, so it forms almost no SEI, cannot plate lithium and survives tens of thousands of fast-charge cycles, at the cost of 1.4 V of cell voltage and half of graphite's capacity.

**Lithium metal** (3861 mAh/g) is the limiting anode, but in liquid electrolytes it deposits unevenly as mossy or dendritic lithium; it is the main motivation for solid electrolytes (Section 32.3).

### Cathode materials

**LiCoO$_2$ (LCO)** has the layered α-NaFeO$_2$ structure, with alternating layers of Li and CoO$_2$ octahedra. It has the highest volumetric energy density of the common cathodes and still dominates phones and laptops, but cobalt is costly and its supply concentrated.

**NMC** (LiNi$_x$Mn$_y$Co$_z$O$_2$) keeps the layered structure but replaces most cobalt with nickel, the main redox-active ion, and manganese, which stays as Mn$^{4+}$ and stabilizes the lattice. Raising nickel trades stability for capacity: high-nickel cathodes release lattice oxygen at lower temperature, feeding thermal runaway, and near full charge an abrupt anisotropic lattice contraction cracks polycrystalline particles along their internal grain boundaries. Single-crystal particles, oxide coatings and nickel-rich-core, manganese-rich-shell particles are the materials responses.

**LiFePO$_4$ (LFP)** has the olivine structure, with lithium in one-dimensional channels and oxygen locked in PO$_4$ tetrahedra by strong covalent P–O bonds. That polyanion framework is why LFP does not release oxygen even when abused. Its lower potential (3.45 V) and poor conductivity (overcome by 100–300 nm carbon-coated particles) cost energy, but it is cheap, free of cobalt and nickel and long-lived, which is why it now dominates stationary storage and much of the vehicle market, as in the bus decision that opened this chapter.

**Table 32.2 — Lithium-ion electrode materials (typical values).**

| Material | Structure / mechanism | Average potential vs Li/Li$^+$ (V) | Theoretical capacity (mAh/g) | Practical capacity (mAh/g) | Volume change | Key limitation |
|---|---|---|---|---|---|---|
| Graphite | Layered, intercalation | ≈0.1 | 372 | 340–360 | ≈10 % | SEI growth; Li plating at fast charge |
| Si | Alloying | ≈0.4 | 3578 (Li$_{15}$Si$_4$) | 1000–3000 (in composites) | ≈280 % | Fracture; continual SEI growth |
| Li$_4$Ti$_5$O$_{12}$ | Spinel, intercalation | 1.55 | 175 | 160–170 | ≈0.2 % | Low cell voltage |
| Li metal | Plating | 0 | 3861 | — | No host | Dendrites; reactivity |
| LiCoO$_2$ | Layered | ≈3.9 | 274 | 140–185 | 2–3 % | Co cost; instability at deep delithiation |
| NMC811 | Layered | ≈3.75 | 276 | 190–210 | ≈5 % (abrupt near top of charge) | Particle cracking; O$_2$ release |
| LiFePO$_4$ | Olivine, two-phase | 3.45 | 170 | 155–165 | ≈6.5 % | Low conductivity; lower energy |
| LiMn$_2$O$_4$ | Spinel | ≈4.0 | 148 | 100–120 | ≈7 % | Mn dissolution above ≈50 °C |

<!-- FIGURE 32.2 | figures/ch32/fig-32-2-electrode-potential-capacity-map.png | map | Electrode materials by potential and specific capacity: cell voltage is the vertical gap between cathode and anode, and the electrolyte must survive the whole span. | Content: x-axis specific capacity 0-4000 mAh/g (broken axis: 0-400 linear, then 400-4000), y-axis potential vs Li/Li+ 0-5 V. Points with practical-capacity ellipses: LCO (160, 3.9 V), NMC811 (200, 3.75 V), LFP (160, 3.45 V), LMO (110, 4.0 V), graphite (350, 0.1 V), LTO (165, 1.55 V), Si (3578 theor., 0.4 V), Li metal (3861, 0 V). Label each with volume change (%). Shade the stability window of carbonate electrolytes (~1.0-4.3 V) and mark 'SEI forms' below it. Double arrow for cell voltage between NMC811 and graphite (~3.65 V). -->

### Matching the electrodes

Because the same charge passes through both electrodes, the masses needed per unit charge add, and the combined capacity of the pair per gram of total active material is $Q_{pair}=(1/Q_c+1/Q_a)^{-1}$ (Figure 32.2).

**Worked example — what a better anode buys.**

- LFP (160 mAh/g) with graphite (350 mAh/g): $Q_{pair}=(0.00625+0.00286)^{-1}=110$ mAh/g. At about 3.3 V, that is $110\times3.3=363$ Wh per kilogram of active material.
- NMC811 (200 mAh/g) with graphite: $Q_{pair}=(0.00500+0.00286)^{-1}=127$ mAh/g, or about 465 Wh/kg at 3.65 V.
- NMC811 with a silicon-rich anode at 2000 mAh/g: $Q_{pair}=(0.00500+0.00050)^{-1}=182$ mAh/g.
- NMC811 with lithium metal (3861 mAh/g): $Q_{pair}=190$ mAh/g.

A nearly sixfold increase in anode capacity raises the pair by 43 %, and going on to lithium metal adds only another 4–5 %, because the cathode now dominates the active mass. The cathode is the bottleneck of lithium-ion energy density, which is why most research effort goes into cathode nickel content and voltage. (Lithium metal's real advantage is volumetric and in removing the host altogether.) A finished cell reaches roughly half the active-material figure, 160–300 Wh/kg, once electrolyte, separator, current collectors and casing are added.

### Beyond lithium-ion

**Sodium-ion** cells apply intercalation to abundant sodium, with **hard-carbon** anodes (graphite barely accepts sodium) and layered-oxide, phosphate or Prussian-blue cathodes: 20–30 % less energy than LFP, but no lithium, cobalt or nickel, and aluminium instead of copper foil. **Conversion chemistries** (Li–S, metal–air) promise more energy because the host disappears, which is exactly why they suffer the volume changes and poor reversibility that intercalation avoids.

---

## 32.3 Battery materials II: electrolytes and the solid-state cell

### What an electrolyte must do

The standard liquid electrolyte, LiPF$_6$ in mixed carbonates, conducts Li$^+$ at about $10^{-2}$ S/cm, but it is flammable, decomposes above about 4.3 V and below about 1 V versus Li/Li$^+$ (it survives only behind passivating interphases, which sacrificial additives such as fluoroethylene carbonate help build), and cannot stop lithium dendrites. A **solid electrolyte** with comparable conductivity would allow a lithium-metal anode and a non-flammable cell. It needs a room-temperature conductivity above about $10^{-3}$ S/cm with negligible electronic leakage, a transference number near 1, stability against lithium and a 4 V cathode (or a self-limiting interphase), mechanical properties that keep contact and resist filament growth, and low processing cost.

### Ion transport in solids

Ions move through a crystal by thermally activated hops between sites, via vacancies or interstitials (Chapters 8 and 25). The conductivity follows

$$
\sigma T=A\exp\left(-\frac{E_a}{k_BT}\right)
$$

> **Status of the principle: Arrhenius ionic conductivity**
> *Empirical* in practice. The form follows from activated hopping (Chapter 8), but $A$ and $E_a$ are fitted, and many electrolytes show curvature or a change of slope at phase transitions or, in polymers, near the glass transition.

**Superionic conductors** reach liquid-like conductivity because their structure offers many more equivalent sites than mobile ions, joined by wide bottlenecks, so the barrier falls to 0.2–0.4 eV; large, polarizable anions (S$^{2-}$ more than O$^{2-}$) lower it further, which is why sulfides conduct best.

### The main solid-electrolyte families

**Garnet oxides.** Cubic Li$_7$La$_3$Zr$_2$O$_{12}$ (LLZO, doped with Al, Ga or Ta) is stable against lithium metal. Its problems are a ceramic's (Chapter 17): sintering above 1100 °C while lithium evaporates, stiffness (about 150 GPa) and brittleness that spoil contact with electrodes, and an insulating Li$_2$CO$_3$ skin in moist air. Lithium filaments still penetrate it near 1 mA/cm² along grain boundaries and from surface flaws: a lithium-filled crack is driven by pressure like a hydraulic fracture (Chapter 14), so stiffness alone does not stop dendrites.

**Sulfides.** Li$_{10}$GeP$_2$S$_{12}$ (LGPS) matches liquids; the argyrodites Li$_6$PS$_5$X (X = Cl, Br) give 1–5 mS/cm without germanium. Sulfides are soft (20–30 GPa) and densify by cold pressing, giving good particle contact without sintering. But they are reduced by lithium and oxidized by cathodes above about 2.5 V, so cathode particles need coatings, and moisture releases toxic H$_2$S, so cells are made in dry rooms.

**NASICON phosphates** such as LATP are air-stable and tolerate high-voltage cathodes, but their Ti$^{4+}$ is reduced by lithium; the sodium analogues, with sodium β″-alumina, serve hot sodium–sulfur grid batteries. **Polymers** such as PEO–LiTFSI are easy to process, but ions move only with polymer segments above the glass transition, so such cells run warm, at 60–80 °C.

**Table 32.3 — Ionic conductors for batteries, fuel cells and electrolysers (typical values; Figure 32.3).**

| Electrolyte | Mobile ion | Conductivity (S/cm) | At | $E_a$ (eV) | Main limitation |
|---|---|---|---|---|---|
| LiPF$_6$ in carbonates (liquid reference) | Li$^+$ and anions | $10^{-2}$ | 25 °C | ≈0.1–0.2 | Flammable; narrow window; dendrites |
| PEO–LiTFSI | Li$^+$ | $10^{-5}$ / $10^{-4}$–$10^{-3}$ | 25 / 60–80 °C | ≈0.5–1 | Low room-temperature conductivity |
| LLZO (doped garnet) | Li$^+$ | $10^{-4}$–$10^{-3}$ | 25 °C | 0.3–0.4 | Brittle; sintering; Li$_2$CO$_3$ |
| Li$_6$PS$_5$Cl (argyrodite) | Li$^+$ | $1$–$5\times10^{-3}$ | 25 °C | 0.2–0.3 | Narrow window; H$_2$S |
| Li$_{10}$GeP$_2$S$_{12}$ | Li$^+$ | $1.2\times10^{-2}$ | 25 °C | ≈0.25 | Ge cost; reduced by Li |
| LATP (NASICON) | Li$^+$ | $10^{-4}$–$10^{-3}$ | 25 °C | 0.3–0.4 | Ti$^{4+}$ reduced by Li |
| Na-β″-alumina | Na$^+$ | 0.2–0.4 | 300 °C | ≈0.3 | Brittle; hot operation |
| 8YSZ | O$^{2-}$ | 0.01 / 0.1 | 700 / 1000 °C | 0.8–1.0 | Needs high temperature |
| Nafion (hydrated) | H$^+$ | ≈0.1 | 80 °C, humidified | ≈0.1–0.2 | Needs water; below 100 °C |

<!-- FIGURE 32.3 | figures/ch32/fig-32-3-ionic-conductivity-arrhenius.png | plot | Arrhenius plot of ionic conductors: sulfides rival liquid electrolytes at room temperature, while oxide-ion conductors need several hundred degrees. | Content: y-axis log10 sigma (S/cm) from -7 to 0; bottom x-axis 1000/T (K^-1) 0.7-3.7; top axis temperature in degC (1000, 700, 500, 300, 100, 25). Lines: liquid LiPF6/EC-DMC (1e-2 at 25 C, shallow), LGPS (1.2e-2 at 25 C), Li6PS5Cl (3e-3), LLZO (5e-4), LATP (3e-4), PEO-LiTFSI (curved, 1e-5 at 25 C to 1e-3 at 80 C), Nafion (0.1 at 80 C, ends at 100 C), 8YSZ (0.1 at 1000 C, 0.01 at 700 C, slope 0.9 eV), GDC (above YSZ at 500-700 C), Na-beta''-alumina (0.2-0.4 at 300 C). Horizontal dashed target line at 1e-3 S/cm. -->

### Interfaces are the real problem

A liquid wets every particle; a solid touches its neighbours only at points. Cycling particles swell and shrink, opening gaps; reactions grow resistive interphases. Stack pressures of several megapascals, nanometre interlayers deposited by atomic-layer deposition (Chapter 41) and composite cathodes are the current remedies, and operando methods (Chapter 44) are how these interfaces are studied.

---

## 32.4 Fuel-cell and electrolyser materials

A fuel cell is an electrochemical cell fed continuously with fuel at the anode and oxygen at the cathode, separated by an electrolyte that passes ions but not electrons. An electrolyser runs the same reactions backwards to make hydrogen from water and electricity. Every layer of both is a materials problem (Figure 32.4).

### Proton-exchange membrane cells

**Membrane.** Perfluorosulfonic-acid (PFSA) ionomers such as Nafion have a PTFE-like backbone with side chains ending in sulfonic acid groups. When hydrated, the acid groups cluster into nanometre water channels that carry protons; dry, the membrane hardly conducts. Membranes 10–50 µm thick conduct about 0.1 S/cm at 80 °C when humidified, which keeps operation below about 100 °C; swelling and shrinking with humidity cycles fatigues them and opens pinholes.

**Catalyst layer.** At 80 °C oxygen reduction is slow and only platinum-group metals catalyse it adequately: Pt or Pt alloy particles 2–5 nm across on carbon, in a porous layer that must also conduct protons (ionomer), electrons (carbon) and gas (pores), a three-phase nanocomposite. Loadings have fallen to 0.1–0.4 mg Pt/cm², a few tenths of a gram per kilowatt. Bipolar plates of graphite composite or coated stainless steel or titanium must resist warm acid without growing an insulating oxide: the passivity of Chapter 34 is here a liability.

**Degradation.** Under voltage cycling, platinum nanoparticles dissolve and redeposit on larger ones, Ostwald ripening driven by the Gibbs–Thomson effect (Chapter 10); the carbon support oxidizes during start-up and shut-down; and peroxide radicals attack the membrane.

### Solid oxide cells

Solid oxide fuel cells (SOFCs) use an oxide-ion conductor and run at 600–1000 °C, hot enough that no precious metal is needed and hydrocarbon fuels can be used.

**Electrolyte.** Yttria-stabilized zirconia (8 mol% Y$_2$O$_3$, "8YSZ") stabilizes the cubic fluorite phase, and each pair of Y$^{3+}$ ions substituting for Zr$^{4+}$ creates one oxygen vacancy, written in Kröger–Vink notation (Chapter 5) as

$$
\mathrm{Y_2O_3}\xrightarrow{\mathrm{ZrO_2}}2\,\mathrm{Y'_{Zr}}+3\,\mathrm{O_O^\times}+\mathrm{V_O^{\bullet\bullet}}
$$

Oxide ions hop through these vacancies. Gadolinium-doped ceria (GDC) and scandia-stabilized zirconia conduct better at lower temperatures, though ceria becomes partly electronically conducting in reducing gas.

**Electrodes and interconnects.** The anode is a porous Ni–YSZ cermet in which nickel conducts electrons and catalyses fuel oxidation, YSZ conducts oxide ions, and pores admit fuel, so reaction occurs at the triple-phase boundary; the cathode is a perovskite such as (La,Sr)(Co,Fe)O$_3$. Interconnects are ferritic stainless steels with about 22 % Cr, whose expansion (11–12 ppm/K) matches the cell, but whose chromia scale evaporates chromium species that poison the cathode unless coated. Matching the expansion of every layer is the central thermomechanical problem (Chapter 24).

**Worked example — electrolyte thickness and operating temperature.** A cell is useful only if the electrolyte's area-specific resistance $\mathrm{ASR}=t/\sigma$ is below about 0.15 Ω cm². 8YSZ conducts about 0.1 S/cm at 1000 °C with $E_a=0.9$ eV. At 700 °C (973 K) its conductivity is lower by

$$
\frac{\sigma(1273\ \mathrm K)}{\sigma(973\ \mathrm K)}=\frac{973}{1273}\exp\left[\frac{0.9}{8.617\times10^{-5}}\left(\frac1{973}-\frac1{1273}\right)\right]=0.764\times12.55=9.6
$$

so $\sigma(700\ ^\circ\mathrm C)\approx0.010$ S/cm.

- An electrolyte-supported cell with $t=150$ µm (0.015 cm): ASR $=0.015/0.1=0.15$ Ω cm² at 1000 °C, acceptable, but $0.015/0.0104=1.4$ Ω cm² at 700 °C, about ten times too high.
- An anode-supported cell with a 10 µm electrolyte at 700 °C: ASR $=0.001/0.0104=0.096$ Ω cm².

Making the electrolyte fifteen times thinner allows operation 300 °C cooler, which permits stainless-steel interconnects and slows every diffusion-driven degradation process. Modern SOFCs are therefore anode-supported, with a thin dense electrolyte film on a thick porous cermet, and cells for 500–650 °C move to GDC.

<!-- FIGURE 32.4 | figures/ch32/fig-32-4-pemfc-sofc-cross-sections.png | schematic | PEM and solid-oxide cells are layered materials systems: every layer must conduct the right species and match its neighbours chemically and thermally. | Content: two side-by-side cross-sections, not to scale, layer thicknesses labelled. (a) PEMFC at 80 C: bipolar plate with flow channels (graphite or coated steel), gas-diffusion layer carbon paper (~200 um), anode catalyst layer Pt/C + ionomer (5-10 um) with zoom of 3 nm Pt particles on 30 nm carbon, PFSA membrane (15-25 um) with H+ arrows, cathode catalyst layer, GDL, plate; H2 in, O2/air in, water out. (b) Anode-supported SOFC at 700 C: Fe-22Cr interconnect, porous Ni-YSZ support (300-500 um), Ni-YSZ functional layer (~10 um), dense 8YSZ electrolyte (10 um) with O2- arrows, GDC barrier (~2 um), porous LSCF cathode (~30 um), triple-phase-boundary zoom. Thermal expansion per layer: Ni-YSZ ~12.5, YSZ 10.5, LSCF ~15, Fe-22Cr ~11.5 ppm/K. -->

### Electrolysers

Water electrolysis is a fuel cell in reverse, and the slow step becomes oxygen evolution at the anode, whose catalyst must survive strongly oxidizing potentials.

- **PEM electrolysers** have an acidic membrane, so only **iridium oxide** is both active and stable at the anode. At 1–2 mg Ir/cm², a few hundred kilograms of iridium per gigawatt, against world production of about 7–8 tonnes a year, deployment at hundreds of gigawatts is impossible; tenfold lower loadings and iridium-free catalysts are urgent targets.
- **Alkaline electrolysers** run in 25–30 wt% KOH, where nickel is passive (Chapter 34), so nickel-based electrodes avoid precious metals entirely, at lower current density.
- **Solid-oxide electrolysers** reuse SOFC materials at 700–850 °C, where heat supplies part of the energy; the oxygen electrode tends to delaminate.

---

## 32.5 Hydrogen storage and hydrogen embrittlement

### Storing hydrogen

Hydrogen carries more energy per unit mass than any fuel, about 120 MJ/kg (lower heating value), but very little per unit volume: about 40 kg/m³ as a gas at 700 bar and 71 kg/m³ as a liquid at 20 K. Compressed storage is a composites problem. Type IV vessels wind carbon fibre in epoxy (Chapters 22 and 23) over a polyamide or high-density polyethylene liner that blocks permeation and has no metal to embrittle; the fibre carries the pressure and accounts for most of the tank's cost. Liquid storage is a cryogenic-materials problem (Chapter 33).

**Metal hydrides** store hydrogen as atoms in interstitial sites and exceed the volumetric density of liquid hydrogen. Because the entropy of formation is roughly the same for all hydrides (the loss of gaseous H$_2$ entropy), the formation enthalpy decides the temperature of release at 1 bar through the van 't Hoff relation (Advanced Chemistry): near-ambient cycling needs about −30 kJ per mol H$_2$.

**Worked example — mass of hydride to store 5 kg of hydrogen.** The gravimetric capacity is the mass fraction of hydrogen in the hydride.

- MgH$_2$: $2.016/(24.305+2.016)=7.66$ wt%. Storing 5 kg of H$_2$ needs $5/0.0766=65$ kg of MgH$_2$.
- LaNi$_5$H$_6$: $6.048/(432.4+6.048)=1.38$ wt%. Storing 5 kg needs $5/0.0138=362$ kg of hydride.

LaNi$_5$H$_6$ cycles quickly at a few bar near room temperature, but 362 kg is far too heavy for a car, even though it occupies only about 53 L (at 6.9 g/cm³) against 125 L for the gas at 700 bar. MgH$_2$ is light, but its formation enthalpy of about −75 kJ/mol H$_2$ means it releases hydrogen at 1 bar only near 300 °C, and slowly unless catalysed and nanostructured. This is the central trade-off: **strong metal–hydrogen bonds give light, dense storage that is hard to release; weak bonds release easily but only from heavy transition-metal hosts.** Hydrides therefore find use where weight is welcome or irrelevant: forklift counterweights, submarines, stationary buffers and hydrogen compressors that exploit the steep pressure–temperature dependence.

**Table 32.4 — Hydrogen storage options (approximate material-level values).**

| Medium | Gravimetric H (wt%) | Volumetric H (kg/m³) | Release conditions | Comment |
|---|---|---|---|---|
| Compressed gas, 700 bar | 100 (gas); ≈5–6 (system) | ≈40 | Ambient | Composite tanks; compression energy |
| Liquid H$_2$, 20 K | 100 (liquid); ≈5–7 (system) | 71 | 20 K | Boil-off; liquefaction uses ≈30 % of LHV |
| LaNi$_5$H$_6$ | 1.4 | ≈115 | ≈2 bar, 20–40 °C | Heavy; rare earth |
| TiFeH$_2$ | 1.9 | ≈100 | Few bar, ambient | Cheap; needs activation |
| MgH$_2$ | 7.7 | ≈110 | 1 bar at ≈300 °C | Slow kinetics; high enthalpy |
| NaAlH$_4$ (Ti-doped) | 5.6 (total) | ≈95 | 100–180 °C | Two-step release; limited reversibility |
| Ammonia (as carrier) | 17.8 | ≈120 (liquid) | Catalytic cracking, >400 °C | Toxic; established shipping |

### Hydrogen embrittlement

Atomic hydrogen, from dissociating H$_2$ gas or from cathodic reactions in corrosion, plating or cathodic protection, diffuses interstitially into metals and collects at dislocations, grain boundaries and, above all, in the dilated region ahead of a crack tip. There it lowers lattice cohesion and localizes plastic flow, so a ductile metal fails well below its usual strength, often after a delay (mechanisms and tests in Chapter 35). The factors that matter for energy infrastructure:

- **Strength.** Susceptibility rises steeply with yield strength; steels above about 800–1000 MPa, as in fittings, bolts and compressor springs, are at serious risk.
- **Crystal structure.** Hydrogen diffuses fast in BCC ferrite and very slowly in FCC austenite.
- **Fatigue.** In pressurized hydrogen, fatigue-crack growth in pipeline steels rises ten- to a hundredfold, which limits conversion of gas pipelines; hydrogen codes cap pipe grade (about X52–X70) and weld hardness.
- **Hydride formers.** Ti, Zr and Nb precipitate brittle hydrides instead (Chapter 33).

**Worked example — why austenite resists hydrogen.** Take room-temperature lattice diffusion coefficients of hydrogen of $D\approx1\times10^{-8}$ m²/s in pure ferrite and $D\approx1\times10^{-16}$ m²/s in austenite. In one hour ($t=3600$ s) the diffusion length $\sqrt{Dt}$ (Chapter 8) is

$$
\sqrt{10^{-8}\times3600}=6.0\times10^{-3}\ \mathrm m=6\ \mathrm{mm}\quad\text{(ferrite)},\qquad \sqrt{10^{-16}\times3600}=6\times10^{-7}\ \mathrm m=0.6\ \mu\mathrm m\quad\text{(austenite)}
$$

Hydrogen reaches a crack tip in ferritic steel within minutes but barely penetrates austenite in a year of service (trapping slows real steels below the pure-lattice value, but the ratio of about $10^4$ in distance remains). Stable austenitic stainless steels, such as 316L with enough nickel that strain does not transform it to martensite, together with aluminium and copper alloys, are therefore the preferred materials for hydrogen valves, tubing and tank bosses.

---

## 32.6 Thermoelectric materials

### Seebeck, Peltier and the figure of merit

When one end of a conductor is hotter than the other, the hot carriers diffuse toward the cold end until an opposing voltage builds up. The open-circuit voltage per kelvin is the **Seebeck coefficient** $S=-\Delta V/\Delta T$, positive for p-type and negative for n-type material. In metals it is a few µV/K, enough for thermocouples but not for power; in optimally doped semiconductors it is 150–250 µV/K. The reverse **Peltier effect** pumps heat $\Pi I$ at a junction carrying current $I$, with $\Pi=ST$. A module connects p- and n-type legs electrically in series and thermally in parallel between a hot and a cold plate, so their voltages add (Figure 32.5).

Three properties compete inside each leg: $S$ generates voltage, the electrical resistivity wastes it as Joule heat, and the thermal conductivity $\kappa$ leaks heat from hot to cold without generating anything. For a leg between $T_h$ and $T_c$ with constant properties and an optimized load, the maximum efficiency is

$$
\eta_{max}=\frac{T_h-T_c}{T_h}\cdot\frac{\sqrt{1+Z\bar T}-1}{\sqrt{1+Z\bar T}+T_c/T_h},\qquad Z\bar T=\frac{S^2\sigma}{\kappa}\bar T,\quad \kappa=\kappa_e+\kappa_L
$$

with $\bar T$ the mean temperature. The first factor is the Carnot efficiency; the second, which approaches 1 only as $ZT\to\infty$, depends entirely on the material through the dimensionless **figure of merit** $ZT$. The product $S^2\sigma$ is the **power factor**.

> **Status of the principle: thermoelectric efficiency in terms of $ZT$**
> *Derived* from the coupled heat and charge transport equations for a single leg with constant properties. With temperature-dependent properties it remains a good estimate when an averaged $ZT$ is used; contact resistance and heat losses lower real module efficiency further.

**Worked example — exhaust heat recovery.** A generator on an industrial furnace flue or a truck exhaust runs between $T_h=800$ K and $T_c=300$ K, so the Carnot efficiency is $500/800=0.625$.

- With $Z\bar T=1$: $\sqrt2=1.414$, and $\eta_{max}=0.625\times0.414/(1.414+0.375)=0.625\times0.232=0.145$, or 14.5 %.
- With $Z\bar T=2$: $\sqrt3=1.732$, and $\eta_{max}=0.625\times0.732/(1.732+0.375)=0.625\times0.347=0.217$, or 21.7 %.

Doubling $ZT$ raises efficiency by half, and even at $ZT=2$ a thermoelectric reaches only a third of Carnot, whereas a steam or organic Rankine cycle reaches well over half. For the same 800 K source, a material with $ZT=1$ in a 300–500 K window would give only about 8 %. Thermoelectrics win where their other virtues dominate: no moving parts, silence, scalability down to milliwatts and decades of unattended operation.

### Why $ZT$ is hard to raise

The properties are tied together through the carrier concentration $n$. Conductivity $\sigma=ne\mu$ rises with $n$; the Seebeck coefficient falls, roughly as $n^{-2/3}$ in a degenerate semiconductor with one parabolic band (the Pisarenko relation, *Approximate*), because in a metal all carriers sit near the Fermi level and carry nearly the same energy; and $\kappa_e$ rises with $\sigma$ by the Wiedemann–Franz law, $\kappa_e=L\sigma T$ (Chapter 24). The power factor therefore peaks in heavily doped semiconductors at $n\approx10^{19}$–$10^{20}$ cm$^{-3}$. For a p-type Bi$_2$Te$_3$ alloy at 300 K with $S=200$ µV/K, $\sigma=1\times10^5$ S/m and $\kappa=1.5$ W m$^{-1}$ K$^{-1}$, the power factor is $(2\times10^{-4})^2\times10^5=4\times10^{-3}$ W m$^{-1}$ K$^{-2}$ and $ZT=4\times10^{-3}\times300/1.5=0.80$; the electronic part of $\kappa$ is $2.44\times10^{-8}\times10^5\times300=0.73$ W m$^{-1}$ K$^{-1}$, about half. That half cannot be removed without losing conductivity. The lattice half can, and three structural strategies attack it or the band structure:

1. **Band engineering.** Many degenerate band valleys (band convergence, as in PbTe at high temperature) raise the density-of-states effective mass and hence $S$ without lowering mobility much.
2. **Heavy atoms and soft or anharmonic bonds.** Bi, Pb, Te, Sb and Se give low sound velocities; "rattler" atoms in cage structures (skutterudites, clathrates) and strongly anharmonic bonds (SnSe) scatter phonons.
3. **Phonon glass, electron crystal.** Phonons that carry heat have mean free paths from nanometres to micrometres, while electrons in doped semiconductors scatter over shorter distances. Point defects from alloying, nanoprecipitates and grain boundaries at all length scales scatter phonons while leaving electrons almost untouched; alloying (SiGe, Bi$_2$Te$_3$–Sb$_2$Te$_3$) and nanostructuring have each roughly halved $\kappa_L$.

<!-- FIGURE 32.5 | figures/ch32/fig-32-5-thermoelectric-tradeoff.png | plot | Seebeck coefficient falls and electrical conductivity rises with carrier concentration, so the power factor and ZT peak in heavily doped semiconductors. | Content: log x-axis carrier concentration 10^17-10^22 cm^-3 with bands labelled insulators / semiconductors / metals. Curves on normalized or separate log axes: S falling from ~500 to ~5 uV/K, sigma rising, S^2 sigma peaking near 10^19-10^20, kappa_e rising above a constant kappa_L, ZT peaking near 10^19.5 at ~1. Inset: module with p and n legs between hot plate (top) and cold plate (bottom), current path and heat-flow arrows. -->

### Material families

Table 32.5 lists the main families. **Bi$_2$Te$_3$ alloys**, layered compounds of heavy atoms, are in essentially every Peltier cooler, from laser-diode stabilization to laboratory PCR machines, but cleave easily and are weak. **PbTe** powers the radioisotope generators of Mars rovers, and **SiGe**, whose alloy disorder makes it outperform both elements, powered Voyager and Cassini. Half-Heuslers are the robust candidates for vehicle exhausts.

**Table 32.5 — Thermoelectric materials (typical peak values).**

| Material | Type | Peak-$ZT$ temperature (K) | Peak $ZT$ | $\kappa$ (W m$^{-1}$ K$^{-1}$) | Notes |
|---|---|---|---|---|---|
| Bi$_2$Te$_3$ alloys | p and n | 300–400 | 0.9–1.2 | 1.2–1.6 | All Peltier coolers; Te supply |
| PbTe-based | p and n | 600–850 | 1.5–2.2 | 0.8–1.5 | Space generators; Pb toxicity |
| Si$_{80}$Ge$_{20}$ | n / p | 1100–1200 | ≈1.0 / ≈0.7 | 3–5 | Rugged; Ge cost |
| Filled CoSb$_3$ | n and p | 700–850 | 1.2–1.7 | 2–3 | Sb sublimation |
| Half-Heusler | n / p | 900–1000 | 1.0–1.5 | 3–5 | Mechanically strong |
| SnSe (single crystal) | p | 900–930 | ≈2.6 (one axis) | 0.3–0.5 | Brittle, anisotropic |
| Mg$_3$(Sb,Bi)$_2$ | n | 300–700 | 0.8–1.5 | ≈1 | Te-free |

Real modules are limited as often by **interfaces** as by $ZT$: contact resistance below about $10^{-6}$ Ω cm², diffusion barriers that keep solder out of the legs, and joints that survive expansion mismatch during thermal cycling.

---

## 32.7 Supercapacitor materials

### The double layer

At an electrode in an electrolyte, ions of opposite sign accumulate within a fraction of a nanometre of the surface, forming the **electric double layer**. To first order it is a parallel-plate capacitor whose gap $d$ is about the radius of a solvated ion:

$$
\frac CA\approx\frac{\varepsilon_0\varepsilon_r}{d}
$$

> **Status of the principle: Helmholtz double-layer estimate**
> *Approximate.* A parallel-plate model that ignores the diffuse layer, the ion-size distribution and confinement in sub-nanometre pores (where capacitance per unit area anomalously rises); it gives the right order of magnitude.

**Worked example — from surface area to stored energy.** With $\varepsilon_r\approx6$ for the oriented solvent in the layer and $d\approx0.5$ nm, $C/A=8.854\times10^{-12}\times6/(0.5\times10^{-9})=0.106$ F/m², about 10 µF/cm², consistent with measured values of 5–20 µF/cm². An activated carbon of 2000 m²/g would therefore give about $2000\times0.106=212$ F/g. Measured values are 100–150 F/g in organic electrolytes, because not all the area is accessible to ions.

A symmetric cell has two electrodes in series, so for equal masses its capacitance per gram of total active material is a quarter of the single-electrode value: 120 F/g per electrode gives 30 F/g for the cell. At 2.7 V, the stability limit of acetonitrile-based electrolytes,

$$
E=\tfrac12CV^2=\tfrac12\times30\times2.7^2=109\ \mathrm{J/g}=30\ \mathrm{Wh/kg}
$$

of active material, and 5–8 Wh/kg for a packaged cell: twenty to forty times less than a lithium-ion cell. But charge is stored by ion adsorption, without chemical change or solid-state diffusion, so a supercapacitor delivers 5–10 kW/kg and survives $10^5$–$10^6$ cycles. Because energy scales as $V^2$, the electrolyte's stability window matters as much as the electrode: about 1 V for aqueous, 2.5–2.85 V for organic and 3–4 V for ionic-liquid electrolytes. These properties suit jobs measured in seconds: braking-energy recovery in trams and cranes, wind-turbine pitch systems and aircraft emergency actuators.

### Carbons and pseudocapacitors

**Activated carbons**, made by steam or KOH activation of coconut shell, wood or pitch, dominate because they are cheap and have 1000–2500 m²/g of surface in 0.5–5 nm pores. The engineering variable is **pore size**: pores matched to the desolvated ion use their area best, but a connected network of wider pores is needed for fast transport. Graphene and nanotubes serve mainly as conductive additives (Chapter 30).

**Pseudocapacitive** materials (hydrous RuO$_2$, MnO$_2$, MXenes such as Ti$_3$C$_2$T$_x$) store charge by fast surface or near-surface redox reactions whose response looks capacitive. MnO$_2$ is the cheap case: one electron per Mn over 0.8 V would give about $96\,485/(86.94\times0.8)\approx1400$ F/g, but poor conductivity limits real electrodes to 150–300 F/g. The boundary with batteries is kinetic: current proportional to sweep rate means capacitive storage; current proportional to its square root means solid-state diffusion control, which is battery-like.

---

## 32.8 Nuclear fuels and cladding

Fission releases about 200 MeV per event, so a gram of uranium-235 fully fissioned yields about $200\times10^6\times1.602\times10^{-19}\times6.022\times10^{23}/235\approx8\times10^{10}$ J, some two million times the chemical energy of a gram of oil. Nuclear energy is therefore limited not by fuel energy but by what the surrounding materials survive.

The workhorse fuel is **uranium dioxide**, a fluorite-structured ceramic chosen for its high melting point (about 2850 °C), chemical stability in water and ability to hold fission products in its lattice. Its weakness is low thermal conductivity, about 2.5–3 W m$^{-1}$ K$^{-1}$ at operating temperature, which makes pellet centres run near 1000–1500 °C. **Zirconium alloys** (Zircaloy, Zr–Nb) clad it because zirconium absorbs few thermal neutrons; their oxidation, hydrogen pick-up and violent reaction with steam above about 1200 °C are the reasons for accident-tolerant fuels with chromium-coated cladding, FeCrAl alloys or SiC/SiC composites. Radiation damage, nuclear fuels, cladding, reactor-vessel steels and fusion first-wall materials are developed in Chapter 33.

---

## 32.9 Degradation, critical raw materials and scalability

### Degradation is a materials property

Every technology in this chapter fails through mechanisms rooted in its structure (Table 32.6).

**Table 32.6 — Characteristic degradation mechanisms of energy materials.**

| Technology | Dominant degradation | Structural origin |
|---|---|---|
| c-Si PV | Light-induced degradation, LeTID | Point-defect complexes (B–O, H) |
| Perovskite PV | Ion migration; moisture and heat decomposition | Soft ionic lattice; volatile organic cation |
| Li-ion graphite anode | SEI growth; Li plating | Electrolyte instability at low potential |
| High-Ni cathode | Particle cracking; O$_2$ release | Anisotropic lattice change; unstable high-valent Ni |
| PEM fuel cell / electrolyser | Pt and Ir dissolution and ripening; carbon corrosion | Nanoparticle surface energy; potential cycling |
| SOFC / SOEC | Ni coarsening; Cr poisoning; delamination | High-temperature diffusion; volatile Cr |
| Thermoelectric | Sublimation; contact interdiffusion; cracking | Volatile Sb, Te; expansion mismatch |
| Hydrogen infrastructure | Embrittlement; accelerated fatigue | Interstitial H at crack tips |

Degradation is accelerated by temperature, often with an Arrhenius dependence, which is the basis of accelerated tests used to predict 10–30-year lives from months of data (Chapter 36).

### Critical raw materials

A material can be technically superb and still unusable at scale if its elements are scarce, geographically concentrated, produced only as by-products, or toxic. Energy technologies are uniquely exposed because they must be deployed at the size of the whole energy system; the elements in Table 32.7 appear on most national critical-raw-materials lists.

**Table 32.7 — Critical elements in energy materials (approximate, mid-2020s).**

| Element | Where used | Annual primary production (approx.) | Supply feature |
|---|---|---|---|
| Li | All Li-ion cells | ≈200–250 kt (as Li) | Few producers; refining concentrated |
| Co | LCO, NMC cathodes | ≈200–250 kt | ≈70 % from one country |
| Ni | NMC cathodes; alloys | ≈3.5 Mt | Majority from one country |
| Natural graphite | Anodes | ≈1.5 Mt | >90 % of processing in one country |
| Nd, Dy | NdFeB magnets in wind turbines and motors (Chapter 27) | Nd ≈40 kt oxide; Dy ≈2 kt | Mining and separation concentrated |
| Pt | PEM cathodes | ≈180 t | ≈70 % from one country |
| Ir | PEM electrolyser anodes | ≈7–8 t | By-product of Pt mining |
| Te | CdTe, Bi$_2$Te$_3$ | ≈500–700 t | By-product of Cu refining |
| In, Ga | CIGS, III–V, transparent contacts | In ≈1000 t; Ga several hundred t | By-products of Zn and Al refining |
| Ag | c-Si contacts | ≈25,000 t | PV uses over a tenth |

**Worked example — lithium for a terawatt-hour of batteries.** Take an LFP cell at an average 3.3 V. One kilowatt-hour requires $1000/3.3=303$ Ah of charge, or $303\times3600=1.09\times10^6$ C. Each Li$^+$ carries one elementary charge, so the lithium that must shuttle is

$$
m_{Li}=\frac{1.09\times10^6}{96\,485}\times6.941=78\ \mathrm g\ \text{per kWh}
$$

Real cells contain more (SEI losses, incomplete cycling, lithium in the electrolyte salt): about 0.1 kg of lithium per kilowatt-hour. Producing 1 TWh of cells a year therefore needs about $10^9\times0.1=10^8$ kg, or 100 kt, of lithium, around half of mid-2020s world production, and several TWh a year implies a several-fold expansion of mining and refining. Lithium is not geologically scarce, but mines and refineries take 5–15 years to build, so recycling and sodium-ion cells are supply strategies, not only environmental ones.

> **Status of the principle: material-intensity scaling limits**
> *Approximate.* A first-order bound from production rates and material intensity; supply responds to price and technology changes intensity, but the calculation correctly identifies which materials will constrain growth.

The same arithmetic applied to CdTe gives about 6 g of tellurium per square metre of 2 µm absorber, or about 33 t of tellurium per gigawatt at 19 % efficiency; the world's roughly 600 t of annual tellurium production could then support only about 18 GW of new CdTe modules a year, against several hundred gigawatts of total PV installations (Figure 32.6). Silicon, made from the crust's second most abundant element, faces no such ceiling for its absorber, though its silver contacts, at roughly 10 mg per watt, already consume over a tenth of world silver output.

### Cost and scalability

Three lessons recur throughout this chapter.

1. **Abundant beats optimal.** Silicon beat better absorbers, LFP is overtaking NMC, and coconut-shell carbon beats graphene: at system scale, cost and availability outweigh a 20 % gain in a figure of merit.
2. **Processing sets cost.** A film coated from solution at 100 °C or a ceramic sintered in air is cheaper than one grown epitaxially in vacuum or made in a dry room (Chapters 38–41).
3. **Lifetime is part of cost.** The cost per unit of energy stored or generated divides capital cost by lifetime throughput, so a cell with twice the cycle life at the same price halves the cost of stored energy. Degradation science is therefore as central to energy materials as performance.

Recycling closes the loop for valuable elements such as Co, Ni, Li, Pt, Ir, Ag and Te, but only if devices are designed to be separated; lifecycle assessment and the circular economy are the subject of Chapter 49, and the formal trade-off between performance, cost and supply risk is the selection methodology of Chapter 48.

<!-- FIGURE 32.6 | figures/ch32/fig-32-6-material-intensity-supply.png | plot | Material intensity times deployment rate, compared with world production, shows which elements constrain each energy technology. | Content: horizontal bar chart on log x-axis 'fraction of current world primary production needed' from 0.01 to 10 (1 = all current production, vertical red line). Bars: Li for 1 TWh/yr Li-ion (~0.45), Li for 4 TWh/yr (~1.8), Co for 1 TWh/yr all-NMC811 at ~83 g Co/kWh (~0.35), Te for 100 GW/yr CdTe (~5.5), Ir for 100 GW/yr PEM electrolysers at 0.4 g/kW (~5) and at 0.04 g/kW (~0.5), Ag for 500 GW/yr c-Si at 10 mg/W (~0.2), Dy for 100 GW/yr wind with NdFeB at ~10 kg Dy/MW (~0.5). Label each bar with assumed intensity. Note: order-of-magnitude illustration. -->

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How do radiation, extreme heat and cryogenic temperatures degrade fuels, cladding, turbine blades and hydrogen tanks? | Chapter 33 |
| What are the electrochemical thermodynamics and kinetics behind electrode potentials, catalysts and corrosion of cell components? | Chapter 34; Advanced Chemistry |
| How does hydrogen embrittlement proceed, and how is it tested and prevented? | Chapter 35 |
| How are lifetimes of cells, modules and stacks predicted, and how are failures analysed? | Chapter 36 |
| How are absorbers, electrolyte films and catalyst layers deposited and sintered? | Chapters 17, 41 |
| How are capacity, ionic conductivity and interphase growth measured while a cell operates? | Chapters 42, 44 |
| How are candidate energy materials screened computationally? | Chapters 45, 47 |
| How are energy materials compared on cost, lifetime, supply risk and recyclability? | Chapters 48, 49 |

**Next:** Chapter 33 takes materials into the harshest service conditions engineers impose on them, from turbine blades and reactor cores to cryogenic tanks and hypersonic leading edges.
