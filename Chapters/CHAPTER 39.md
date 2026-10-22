# Chapter 39 — Joining: Welding, Brazing and Adhesive Bonding

*Part IX · Processing and Manufacturing*

After the 1994 Northridge earthquake in Los Angeles, steel moment-frame buildings designed to bend plastically and survive were found to have cracked at more than a hundred beam-to-column connections — not in the ductile beams or columns, but at the welds joining beam flanges to columns. The cracks started at weld roots where a backing bar left a notch, ran through low-toughness weld metal, and sometimes tore into the column flange through the heat-affected zone. US connection design, filler-toughness and inspection rules were rewritten. The story is typical: a structure is only as good as its joints, and a joint is a small, locally processed region with its own microstructure, residual stresses and defects. The same lesson applies to a pipeline girth weld that cracks hours after welding, an aluminium panel that loses half its strength beside a weld, a bonded car roof that debonds in humid heat, or a carbon-fibre panel that corrodes the aluminium bolted to it.

> **What does a joining process do to the material around the joint, and why does that region so often decide the strength and life of a structure?**
> **How do we choose between fusion welding, solid-state welding, brazing, adhesive bonding and fastening — and design the joint so that it is not the weakest link?**

| Concept | Engineering destination |
|---|---|
| Arc, laser, electron-beam and resistance welding | Ship hulls, pipelines, car bodies, pressure vessels, turbine parts |
| Heat input, Rosenthal heat flow, cooling time $t_{8/5}$ | Welding procedure specifications, preheat and interpass control |
| Fusion zone and heat-affected zone metallurgy | Toughness of weld HAZs, softened zones in aluminium structures |
| Residual stress and distortion | Post-weld heat treatment, fatigue of welded details, fabrication tolerances |
| Carbon equivalent, hydrogen cracking, hot cracking | Preheat rules, consumable selection, alloy choice for welded structures |
| Friction stir welding, diffusion bonding | Aluminium rail cars and launch-vehicle tanks, titanium aero-engine structures |
| Brazing and soldering | Heat exchangers, carbide tools, ceramic–metal seals, electronics |
| Adhesive bonding and joint design | Aircraft panels, car body structures, wind-turbine blades, composite repairs |
| Fastening and dissimilar joints | Bolted steelwork, riveted aircraft, steel–aluminium car bodies, CFRP–metal joints |

**Roadmap.** Classifying joints (39.1) → fusion welding processes and heat flow (39.2–39.3) → what welding does to the metal: fusion zone, HAZ, residual stress (39.4) → weldability and cracking (39.5) → solid-state welding (39.6) → brazing and soldering (39.7) → adhesive bonding (39.8) → fastening and dissimilar materials (39.9) → choosing a joining method (39.10).

> **Boundary.** Arc physics and power-source electronics belong to electrical and manufacturing engineering, and the thermodynamics of wetting and adhesion are developed in Chapter 37. Solidification (Chapter 9), solid-state transformations in steels (Chapters 10 and 15), fatigue and fracture (Chapter 14) and galvanic corrosion (Chapter 35) are used here as tools.

---

## 39.1 Joining as a materials problem

Joining methods differ in how they make atoms on the two sides of a joint bond to each other, or whether they bond at all.

- **Fusion welding** melts the edges of both parts, usually with added filler metal, and lets the pool solidify into a continuous metallurgical bond. It gives joints as strong as the base metal in most steels, but leaves a cast fusion zone and a heat-affected zone (HAZ).
- **Solid-state welding** brings clean metal surfaces into atomic contact by pressure, plastic deformation and diffusion, without melting: friction, friction stir, diffusion, ultrasonic, explosive and roll bonding. It avoids solidification defects and joins many dissimilar pairs.
- **Brazing and soldering** melt only a filler metal, with a liquidus below the solidus of the parts, which flows into the joint gap by capillarity and bonds by wetting and limited reaction. The parts do not melt.
- **Adhesive bonding** uses a polymer that wets the surfaces as a liquid and then cures; adhesion is by intermolecular forces, chemical bonds and mechanical interlocking.
- **Mechanical fastening** — bolts, rivets, screws, clinching — clamps parts together without any material continuity.

The engineering consequences follow from where the material is altered. Fusion welding changes the parts' microstructure over millimetres; brazing changes them only slightly; adhesive bonding and fastening hardly at all. Conversely, a weld transmits load through continuous metal, while an adhesive transmits it through a thin polymer layer of modest strength and a fastener through bearing, friction and holes that concentrate stress.

---

## 39.2 Fusion welding processes

### Heat sources and power density

A fusion welding heat source is characterized by its **power density** at the work surface. A low-density source such as an oxy-acetylene flame (about 10$^6$–10$^7$ W/m$^2$) heats a wide area slowly, wastes most of its heat into the part and makes a broad, shallow weld with a wide HAZ. An arc concentrates 10$^7$–10$^9$ W/m$^2$; lasers and electron beams 10$^{10}$–10$^{12}$ W/m$^2$. Above roughly 10$^{10}$ W/m$^2$ the surface vaporizes, the recoil pressure of the vapour drills a narrow cavity, the **keyhole**, and energy is deposited along its whole depth: the weld becomes deep and narrow, with depth-to-width ratios up to about 10:1 for lasers and 30:1 for electron beams, a small HAZ and little distortion (Figure 39.1).

The heat delivered to the work per unit length of weld is the **heat input**

$$
H=\eta\,\frac{VI}{v}
$$

for arc voltage $V$, current $I$, travel speed $v$ and arc efficiency $\eta$, the fraction of electrical power reaching the workpiece. Typical efficiencies (as tabulated in welding standards) are 0.6 for gas tungsten arc welding, 0.8 for gas metal arc and shielded metal arc welding, and 1.0 for submerged arc welding, where the flux blanket traps the heat.

### Arc welding processes

- **Shielded metal arc welding (SMAW, "stick")**: a flux-coated consumable electrode whose coating shields the arc and forms slag. Portable — pipelines, site steelwork, repairs — but slow. The coating sets weld-metal hydrogen: cellulosic coatings release a lot, basic "low-hydrogen" coatings very little.
- **Gas metal arc welding (GMAW, MIG/MAG)**: a fed wire electrode under argon, CO$_2$ or mixtures; the workhorse of fabrication. **Flux-cored** wires (FCAW) raise deposition and suit outdoor work.
- **Gas tungsten arc welding (GTAW, TIG)**: a non-consumable tungsten electrode under inert gas with separate filler; slow, clean and precise, for root passes, thin stainless steel, titanium and aluminium.
- **Submerged arc welding (SAW)**: an arc under granular flux at 500–1500 A per wire and 10–40 kg/h with multiple wires; ship panels, wind-turbine towers, thick pressure vessels.
- **Plasma arc welding** constricts the arc to keyhole power densities for plates up to about 8 mm.

### High-energy-density beam welding

**Laser beam welding** uses fibre, disc or CO$_2$ lasers of 1–20 kW focused to 0.2–1 mm spots: **tailor-welded blanks** (sheets of different gauge or grade joined before stamping), body-in-white seams at metres per minute, low-distortion ship panels, battery tabs. Absorption is a materials issue: copper and aluminium reflect over 90 % of near-infrared light until a keyhole forms, so green and blue lasers are being adopted for copper busbars. **Electron beam welding** at 60–150 kV in vacuum gives perfect shielding for titanium, zirconium and refractory metals and single-pass penetration beyond 100 mm in steel, for aero-engine shafts and nuclear components; the chamber limits part size.

### Resistance welding

**Resistance spot welding** clamps overlapping sheets between copper-alloy electrodes and passes a current of about 8–12 kA for 0.1–0.3 s through 1 mm steel sheets. Joule heating, $I^2Rt$, is concentrated at the faying interface, where contact resistance is highest, and melts a lens-shaped **nugget**, typically required to have a diameter of at least $4\sqrt t$–$5\sqrt t$ for sheet thickness $t$ in millimetres. A steel car body has several thousand spot welds. Aluminium, with lower resistivity, needs two to three times the current and wears electrodes quickly.

| Process | Heat source | Power density (W/m²) | Typical heat input (kJ/mm) | Penetration per pass | Typical uses |
|---|---|---|---|---|---|
| Oxy-fuel | Flame | 10⁶–10⁷ | High, poorly controlled | A few mm | Repair, thin steel, cutting |
| SMAW | Arc, flux-coated electrode | 10⁷–10⁸ | 0.8–3 | 2–5 mm | Site steelwork, pipelines |
| GMAW / FCAW | Arc, wire electrode | 10⁷–10⁸ | 0.3–2.5 | 2–6 mm | General fabrication, car bodies |
| GTAW | Arc, tungsten electrode | 10⁷–10⁸ | 0.3–1.5 | 1–3 mm | Root passes, thin stainless, Ti, Al |
| SAW | Arc under flux | 10⁷–10⁸ | 1.5–6 | 5–15 mm | Ships, towers, pressure vessels |
| Plasma arc (keyhole) | Constricted arc | 10⁹–10¹⁰ | 0.5–2 | up to ≈ 8 mm | Tube, thin plate |
| Laser | Photon beam | 10¹⁰–10¹² | 0.05–0.5 | up to ≈ 20 mm | Tailor blanks, body-in-white, battery tabs |
| Electron beam | Electron beam in vacuum | 10¹⁰–10¹² | 0.05–1 | up to > 100 mm | Aero-engine, nuclear, thick Ti |
| Resistance spot | Joule heating at interface | — | — | Sheet thickness | Car bodies, appliances |

*Typical ranges; heat input varies with joint, position and procedure.*

<!-- FIGURE 39.1 | figures/ch39/fig-39-1-power-density-weld-shape.png | schematic | Weld cross-sections produced by heat sources of increasing power density, from oxy-fuel to arc to laser and electron-beam keyhole welding. | Content: top: horizontal log axis of power density 10^6 to 10^12 W/m² with bands labelled 'oxy-fuel', 'arc (SMAW, GMAW, GTAW, SAW)', 'plasma', 'laser', 'electron beam'; vertical dashed line near 10^10 W/m² labelled 'keyhole threshold'. Below: four transverse sections through a 10 mm steel plate at the same scale: oxy-fuel wide shallow bowl with very wide HAZ; GMAW bowl ~10 mm wide, 4 mm deep with HAZ ~3 mm; laser keyhole weld 2 mm wide × 10 mm deep, narrow HAZ; EB weld 1 mm wide, full penetration of a thicker 30 mm section shown as a separate narrow sliver. Fusion zone shaded dark, HAZ lighter. Labels for depth/width ratio ≈ 0.4, 0.4, 5 and 30. -->

Figure 39.1 shows how the same joint looks when made with each family.

---

## 39.3 Heat flow in welding

### The Rosenthal solution

The metallurgy of a weld is set by its thermal cycle: the peak temperature reached at each point, and how fast it cools. Rosenthal's solution treats the heat source as a point (thick plate) or line (thin plate) moving at constant speed $v$ through a solid of conductivity $k$ and diffusivity $\alpha$, with constant properties and no melting. In a frame moving with the source, a steady temperature field develops. For a **thick plate** (three-dimensional heat flow),

$$
T-T_0=\frac{\eta P}{2\pi k R}\exp\!\left[-\frac{v\,(R+\xi)}{2\alpha}\right]
$$

where $P=VI$, $\xi$ is the distance ahead of the source along the weld and $R$ the distance from it. Isotherms are compressed ahead of the source and stretched behind it into a teardrop. Along the weld centreline far behind the source, the cooling rate is

$$
\frac{dT}{dt}=-\frac{2\pi k\,(T-T_0)^2}{H}
$$

with $H=\eta P/v$ the heat input. Integrating between 800 and 500 °C gives the cooling time through the range in which austenite transforms in most structural steels:

$$
t_{8/5}=\frac{H}{2\pi k}\left(\frac{1}{500-T_0}-\frac{1}{800-T_0}\right)
$$

For **thin plates** (two-dimensional flow) the corresponding result varies as $(H/d)^2$ for plate thickness $d$, so thin plates cool much more slowly for the same heat input. Welding standards use empirically calibrated versions of both; for steels the three-dimensional form is

$$
t_{8/5}=(6700-5T_0)\,H\left(\frac{1}{500-T_0}-\frac{1}{800-T_0}\right)F_3
$$

with $H$ in kJ/mm, $T_0$ in °C, $t_{8/5}$ in seconds and a joint-shape factor $F_3$ (1 for a butt weld, about 0.67 for a fillet weld, which loses heat into three legs).

> **Status of the principle: Rosenthal heat flow and the $t_{8/5}$ formulas**
> *Approximate.* The solution of the heat equation for a moving point or line source with constant properties, no latent heat and no convection in the pool. It predicts the HAZ cooling rate well away from the pool and fails near and inside it, where the source's size, convection and latent heat matter. The standard $t_{8/5}$ equations are *empirical* calibrations of the same form.

**Worked example — Cooling time and the effect of preheat.** A 25 mm S355 steel plate is butt welded by GMAW at 28 V, 250 A and 300 mm/min (5 mm/s), with $\eta=0.8$. The heat input is

$$
H=0.8\times\frac{28\times250}{5}=1120\ \mathrm{J/mm}=1.12\ \mathrm{kJ/mm}
$$

Is the plate thick enough for three-dimensional flow? The standards' transition thickness for this heat input and $T_0=20$ °C works out at about 15.5 mm, so 25 mm is thick. Without preheat ($T_0=20$ °C):

$$
t_{8/5}=(6700-100)\times1.12\times\left(\frac{1}{480}-\frac{1}{780}\right)=6600\times1.12\times8.01\times10^{-4}=5.9\ \mathrm{s}
$$

The Rosenthal formula with $k=30$ W/m K gives $1.12\times10^{6}/(2\pi\times30)\times8.01\times10^{-4}=4.8$ s — the same order, slightly faster because it ignores the reduced conductivity and latent effects that the calibration absorbs. With a preheat of 100 °C,

$$
t_{8/5}=(6700-500)\times1.12\times\left(\frac{1}{400}-\frac{1}{700}\right)=6200\times1.12\times1.071\times10^{-3}=7.4\ \mathrm{s}
$$

Preheating by 80 K lengthens the cooling time by about 25 % (Figure 39.2). For many C–Mn steels, the HAZ hardness rises steeply as $t_{8/5}$ falls below roughly 5 s, so this change can move the HAZ from a crack-susceptible martensitic structure to a tougher bainitic one. Preheat also slows cooling below 300 °C, where it matters even more by giving hydrogen time to diffuse out (Section 39.5). The same calculation, run the other way, shows why very high heat inputs ($t_{8/5}$ of 30 s or more) are restricted for thermomechanically processed steels: they coarsen the HAZ grains and lose the fine structure that gave the steel its toughness (Chapter 38).

<!-- FIGURE 39.2 | figures/ch39/fig-39-2-t85-heat-input.png | plot | Cooling time from 800 to 500 °C in the heat-affected zone of a thick steel plate as a function of heat input and preheat temperature. | Content: x-axis heat input 0.5–3.0 kJ/mm; y-axis t8/5 0–40 s. Lines from the 3D formula (6700 − 5T0)H(1/(500−T0) − 1/(800−T0)) for butt welds at T0 = 20, 100 and 150 °C (at 1.12 kJ/mm: 5.9, 7.4, 8.8 s, marked with dots and the worked-example label). Dashed line for a fillet weld (F3 = 0.67) at 20 °C. Shaded horizontal band below ~5 s labelled 'martensitic HAZ, cold-cracking risk (typical C–Mn steel)'; band above ~25 s labelled 'coarse-grained HAZ, toughness loss in TMCP steels'. Secondary top axis: approximate HAZ hardness trend from ~400 HV at 3 s to ~200 HV at 30 s (schematic). -->

---

## 39.4 Welding metallurgy

A fusion weld in cross-section has three regions: the **fusion zone** (weld metal), which was fully liquid; a narrow **partially melted zone** at the fusion boundary; and the **heat-affected zone**, base metal heated enough to change its microstructure but not to melt.

### The fusion zone

The weld pool is a small casting with a peculiar mould: the hot, unmelted base metal of the same crystal structure. Solidification therefore starts without any nucleation barrier, by **epitaxial growth** from the partially melted grains at the fusion boundary, which continue across it with the same orientation. Grains then grow toward the pool's centreline along the steepest temperature gradient, and **competitive growth** favours those whose easy-growth ⟨100⟩ direction is best aligned with it. The result is columnar grains that curve toward the moving pool's trailing edge. As in Chapter 9, the solidification mode depends on the thermal gradient $G$ and growth rate $R$: high $G/R$ at the fusion boundary gives planar or cellular growth, low $G/R$ at the centreline gives columnar dendritic or even equiaxed grains, and the product $GR$ (the cooling rate) sets the scale of dendrites. Because $R=v\cos\theta$, with $\theta$ the angle between the growth direction and the welding direction, fast welding makes teardrop-shaped pools in which columnar grains meet head-on at the centreline — a weak plane where the last solute-rich liquid freezes and where solidification cracks form (Section 39.5).

Weld metal is a mixture of filler and melted base metal; the **dilution** (base-metal fraction) is typically 10–40 % for arc welds and up to 100 % for autogenous laser welds. Steel fillers add deoxidizers (Si, Mn, Ti) and are designed so that **acicular ferrite** — fine interlocking laths nucleated on titanium-oxide inclusions — dominates and gives high toughness. Titanium welds must be shielded until below about 400 °C or they absorb oxygen and embrittle (silver colour acceptable, blue or grey rejected).

### The heat-affected zone in steels

Each point in the HAZ experiences a thermal cycle with a peak temperature that falls with distance from the fusion line. Superimposing the peak temperatures on the Fe–C diagram (Figure 39.3) divides the HAZ of a steel into sub-zones:

- **Coarse-grained HAZ (CGHAZ)**, peak above about 1100–1200 °C: austenite grains grow rapidly to 100 µm or more, increasing hardenability, so on cooling this zone forms the hardest and least tough structures — martensite or upper bainite. It is the critical region for both hydrogen cracking and toughness.
- **Fine-grained HAZ (FGHAZ)**, peak about 900–1100 °C: the steel is fully austenitized but grains do not grow, and it transforms to fine ferrite–pearlite or bainite. Usually the toughest zone.
- **Intercritical HAZ (ICHAZ)**, peak between $A_{c1}$ and $A_{c3}$ (about 720–900 °C): partial austenitization of carbon-rich regions, which can transform to brittle martensite–austenite islands.
- **Subcritical HAZ**, peak below $A_{c1}$: tempering or spheroidization of the base metal; in quenched-and-tempered steels a softened band.

In multipass welds, each pass reheats the previous ones, refining some CGHAZ and creating **intercritically reheated CGHAZ** regions with local brittle zones — one reason offshore-structure specifications require HAZ toughness tests (Charpy and CTOD) at several notch positions.

<!-- FIGURE 39.3 | figures/ch39/fig-39-3-haz-regions-fe-c.png | schematic | Heat-affected-zone sub-regions of a 0.15 % C steel weld related to the peak temperature reached and the Fe–Fe3C phase diagram. | Content: left: steel-rich corner of Fe–Fe3C diagram (0–1.0 wt% C, 600–1600 °C) with vertical line at 0.15 % C, A1 (727 °C), A3 (~860 °C at 0.15 % C), solidus and liquidus marked. Right, sharing the temperature axis: half cross-section of a weld with fusion zone (columnar grains growing epitaxially), partially melted zone, coarse-grained HAZ (>1100 °C, large grains), fine-grained HAZ (900–1100 °C, small grains), intercritical HAZ (A1–A3, mixed), subcritical HAZ (<A1, tempered), unaffected base metal; horizontal dashed lines link each zone's peak temperature to the diagram. Below: peak temperature versus distance from the fusion line 0–6 mm, falling from 1500 to 500 °C. -->

### The HAZ in non-ferrous alloys

In alloys strengthened by cold work or precipitation, the HAZ is a region where that strengthening has been undone.

- **Cold-worked alloys** (strain-hardened aluminium 5xxx-H temper, cold-drawn copper) recrystallize in the HAZ and soften to the annealed (O-temper) strength.
- **Precipitation-hardened aluminium** (6xxx, 2xxx, 7xxx in T6 temper) is affected twice. Near the fusion line, precipitates dissolve; this region can partly recover by natural or artificial aging after welding. Farther out, at peak temperatures of roughly 250–400 °C, the fine β″ precipitates of a 6xxx alloy coarsen into non-strengthening β′ and β: the zone is **over-aged** and stays soft. Design codes therefore assign welded 6061-T6 an ultimate strength of about 165 MPa, compared with 260–310 MPa for the base metal, and structures place welds in low-stress regions or use friction stir welding (Section 39.6).
- **Nickel-base superalloys** and **titanium alloys** suffer coarsening of γ′ or α structures and, in the PMZ, liquation of low-melting phases.

### Residual stress and distortion

As the weld pool cools, the hot weld metal and HAZ try to contract but are restrained by the cooler surrounding plate. The thermal strain available is enormous: for steel cooling through 600 K, $\alpha\Delta T=12\times10^{-6}\times600=0.0072$, which elastically would correspond to $E\alpha\Delta T\approx1440$ MPa, far above the yield strength. The weld region therefore yields in tension during cooling, and once cold it is left with **longitudinal residual stress approximately equal to the yield strength** of the weld or HAZ, balanced by compressive stress in the surrounding plate. Transverse residual stresses are smaller and depend on restraint.

Residual stresses have three consequences. (1) **Distortion** — shrinkage, angular distortion and buckling of thin panels — controlled by sequencing, presetting, clamping and lower heat input (laser welds distort far less than arc welds). (2) **Fatigue**: tensile residual stress at the weld toe, with the toe's geometric stress concentration and small slag intrusions, makes the fatigue strength of welded details almost independent of steel strength, so design codes classify details by geometry, not grade (Chapter 14). Toe grinding, TIG dressing and peening introduce compression and raise it. (3) **Stress-assisted failure**: residual stress adds to service stress in brittle fracture, hydrogen cracking and stress-corrosion cracking (Chapter 35).

**Post-weld heat treatment (PWHT)**, typically 580–620 °C for C–Mn pressure-vessel steels for about one hour per 25 mm of thickness, lowers the yield strength enough for creep to relax residual stresses to perhaps 20–30 % of their as-welded values, and tempers HAZ martensite. Residual stresses are measured by hole drilling, X-ray and neutron diffraction (Chapter 43) and contour methods.

> **Status of the principle: residual stress near yield in as-welded joints**
> *Approximate.* It follows from thermal strains far exceeding the elastic limit under restraint. It is a good design assumption for longitudinal stress in steel and aluminium welds; it overestimates in low-restraint thin sheet and is modified where solid-state phase transformations on cooling (martensite's volume expansion) put the weld into compression.

---

## 39.5 Weldability and weld cracking

**Weldability** is the ability of a material to be welded into a structure that performs satisfactorily, under practical fabrication conditions. It is limited mainly by cracking, of which there are two families: **cold cracking**, which occurs after the weld has cooled, and **hot cracking**, which occurs during or immediately after solidification.

### Hydrogen-induced cold cracking

Hydrogen cracking — also called cold cracking, delayed cracking or underbead cracking — is the most common cause of weld rejections in structural steels. It requires four factors at once:

1. **Hydrogen** in the weld, from moisture in fluxes and electrode coatings, from hydrocarbons and rust on the joint, or from the atmosphere. Diffusible hydrogen is classified in mL per 100 g of deposited weld metal: H5 (≤ 5), H10, H15; basic low-hydrogen electrodes and solid wires give under 5, cellulosic electrodes more than 30.
2. **A susceptible microstructure**, chiefly high-carbon martensite in the CGHAZ or weld metal. A hardness above about 350 HV is a common warning level.
3. **Tensile stress**, from residual stress and restraint.
4. **A low temperature**, below about 150–200 °C, where hydrogen is trapped and embrittling rather than diffusing out.

Cracks may appear hours or days later, as hydrogen diffuses to triaxially stressed notches and martensite (Chapter 35), so susceptible welds are inspected after a 16–48 hour delay. Prevention attacks each factor: dry low-hydrogen consumables; preheat and interpass temperature (softer HAZ, time for hydrogen to escape); a post-heat hold at about 200–250 °C; less restraint.

### Carbon equivalent

Since the susceptible microstructure depends on hardenability, empirical **carbon equivalents** combine alloying elements by their effect on HAZ hardenability. The most widely used, from the International Institute of Welding, is

$$
\mathrm{CE_{IIW}}=\mathrm{C}+\frac{\mathrm{Mn}}{6}+\frac{\mathrm{Cr}+\mathrm{Mo}+\mathrm{V}}{5}+\frac{\mathrm{Ni}+\mathrm{Cu}}{15}
$$

in wt%. Rough guidance is that steels with $\mathrm{CE_{IIW}}<0.40$ seldom need preheat in ordinary thicknesses; 0.40–0.60 need preheat of the order of 50–200 °C depending on thickness, hydrogen level and heat input; above 0.60 preheat of 200 °C or more and often PWHT are required. For low-carbon (below about 0.12 % C) microalloyed and TMCP steels the formula overweights the alloying elements and the Ito–Bessyo parameter

$$
P_{\mathrm{cm}}=\mathrm{C}+\frac{\mathrm{Si}}{30}+\frac{\mathrm{Mn}+\mathrm{Cu}+\mathrm{Cr}}{20}+\frac{\mathrm{Ni}}{60}+\frac{\mathrm{Mo}}{15}+\frac{\mathrm{V}}{10}+5\mathrm{B}
$$

is preferred. The **Graville diagram** (Figure 39.4) plots carbon content against CE and divides steels into an easily weldable zone of low carbon, a zone of higher carbon but low hardenability where controlling cooling rate suffices, and a zone of high carbon and high hardenability where preheat, low hydrogen and often PWHT are all needed.

> **Status of the principle: carbon equivalent**
> *Empirical.* The coefficients are regression fits of HAZ hardness or cracking tests on steels of particular composition ranges. They rank steels within those ranges well and should not be extrapolated: CE$_{\mathrm{IIW}}$ suits C–Mn and low-alloy steels with more than about 0.12 % C, $P_{\mathrm{cm}}$ suits lower-carbon steels, and neither applies to stainless steels.

**Worked example — Will this steel need preheat?** Compare a structural S355 plate (0.18 C, 1.40 Mn, 0.30 Si, 0.05 Cr, 0.02 Mo, 0.01 V, 0.05 Ni, 0.10 Cu) with a quenched-and-tempered AISI 4140 shaft steel (0.40 C, 0.85 Mn, 1.0 Cr, 0.20 Mo).

$$
\mathrm{CE_{S355}}=0.18+\frac{1.40}{6}+\frac{0.05+0.02+0.01}{5}+\frac{0.05+0.10}{15}=0.18+0.233+0.016+0.010=0.44
$$

$$
\mathrm{CE_{4140}}=0.40+\frac{0.85}{6}+\frac{1.0+0.20}{5}=0.40+0.142+0.240=0.78
$$

A rough check on how hard a fully martensitic HAZ would be uses Yurioka's empirical fit $H_M\approx884\,\mathrm{C}\,(1-0.3\,\mathrm{C}^2)+294$ HV:

$$
H_{M}(0.18\,\mathrm{C})=884\times0.18\times(1-0.3\times0.0324)+294=452\ \mathrm{HV},\qquad H_{M}(0.40\,\mathrm{C})=631\ \mathrm{HV}
$$

The S355 lies in the middle band: at fast cooling its CGHAZ could exceed 350 HV, so for 25 mm plate a modest preheat (of order 75–125 °C, depending on hydrogen scale and heat input, as set by standards such as EN 1011-2 or AWS D1.1) with H5 consumables makes it safe — and the previous worked example showed what a 100 °C preheat does to $t_{8/5}$. The 4140, with a potential HAZ hardness above 600 HV and CE near 0.8, needs preheat around 250–350 °C, controlled interpass temperature, low-hydrogen practice and immediate PWHT; it is better not welded at all where it can be avoided. For comparison, a modern X70 pipeline steel with 0.08 C and 1.55 Mn plus small additions has $\mathrm{CE_{IIW}}\approx0.38$ and potential martensite hardness of about 365 HV, which is why such steels can be girth welded in the field with little or no preheat.

<!-- FIGURE 39.4 | figures/ch39/fig-39-4-graville-diagram.png | map | Graville weldability diagram: carbon content versus carbon equivalent, showing zones of hydrogen-cracking susceptibility, with representative steels plotted. | Content: x-axis CE_IIW 0.2–0.9; y-axis carbon 0–0.5 wt%. Zone I (C < ~0.10 % across CE range up to ~0.6): 'easily weldable, low risk'. Zone II (C > 0.10 %, CE < ~0.45, boundary line sloping): 'control cooling rate / heat input'. Zone III (high C and high CE): 'preheat, low hydrogen, PWHT required'. Points: X70 TMCP pipeline steel (0.38, 0.08), S355 (0.44, 0.18), S690 Q&T (0.55, 0.16), AISI 4140 (0.78, 0.40), 1045 (0.6, 0.45). Labels next to each. -->

### Hot cracking

**Solidification cracking** occurs in the fusion zone at the end of solidification, by the same mechanism as hot tearing in castings (Chapter 38): at high solid fraction, thin films of solute-rich liquid along columnar grain boundaries cannot sustain the contraction strain, and they separate. Centreline cracks, where grains meet head-on, are typical. Susceptibility rises with the **freezing range** and with impurities that form low-melting films — in steels, sulfur and phosphorus (FeS melts near 988 °C), which is why steel welding consumables keep S and P low and add manganese to tie sulfur up as high-melting MnS. Bead shape matters: deep narrow beads with depth-to-width ratios above about 1 concentrate segregation at the centre.

In **aluminium alloys**, susceptibility versus solute content passes through a maximum at low solute contents (roughly 0.5–3 wt% of Si, Cu or Mg, depending on the system) and falls at higher contents where abundant eutectic liquid back-fills cracks. Alloys such as 6061 and 2024 are therefore welded with a high-solute filler — 4043 (Al–5Si) or 5356 (Al–5Mg) — that shifts the weld metal past the peak; autogenous welds crack. The 7xxx alloys are notoriously crack-prone. **Austenitic stainless steels** are protected by solidifying first as δ-ferrite: weld metal formulated to contain about 3–8 % ferrite (by the WRC-1992 or Schaeffler diagram, Chapter 15) dissolves S and P better and resists cracking, while fully austenitic weld metal is susceptible.

**Liquation cracking** occurs in the partially melted zone when grain-boundary phases or segregates melt locally (constitutional liquation of carbides and sulfides in nickel alloys, eutectics in aluminium alloys) and are pulled apart by the contracting weld.

### Other forms of weld cracking

- **Lamellar tearing**: step-like cracks parallel to the plate surface below T- and corner joints, where weld shrinkage pulls the plate through its thickness and elongated MnS inclusions decohere. Prevented by clean steels with guaranteed through-thickness ductility (for example "Z25" grades, with at least 25 % reduction of area in a through-thickness tensile test) and by joint design.
- **Reheat (stress-relief) cracking**: intergranular cracking in the CGHAZ of Cr–Mo–V and some nickel-alloy welds during PWHT, as carbides precipitate within grains and creep strain concentrates at boundaries.
- **Sensitization** of stainless-steel HAZs to intergranular corrosion by chromium-carbide precipitation (Chapter 35), avoided with low-carbon "L" grades or stabilized grades.

---

## 39.6 Solid-state welding

Solid-state processes avoid melting, so they avoid solidification cracking, porosity and the cast fusion zone, and they can join alloys that fusion welding cannot, including many dissimilar pairs. They work by bringing clean metal surfaces within atomic distances, which needs the oxide films to be broken up or dissolved and the surfaces brought into intimate contact.

### Friction stir welding

**Friction stir welding (FSW)**, invented at TWI in the UK in 1991, plunges a rotating non-consumable tool — a shoulder with a threaded or profiled pin — into the joint line between two clamped plates and traverses it along the joint. Friction under the shoulder and plastic work around the pin heat the metal to about 0.6–0.9$T_m$ (roughly 400–500 °C for aluminium alloys) without melting it. The softened metal is swept around the pin from the **advancing side** (where tool rotation and travel add) to the **retreating side** and consolidated behind it under the shoulder's forging pressure. Typical parameters for aluminium are 200–2000 rpm and 0.1–1 m/min.

The joint has three zones (Figure 39.5): the **stir zone (nugget)**, where intense deformation at high temperature produces dynamically recrystallized equiaxed grains of 2–10 µm, often finer than the base metal; the **thermomechanically affected zone (TMAZ)**, deformed and heated but not recrystallized; and the **HAZ**, heated only. In precipitation-hardened aluminium the HAZ still over-ages, but the peak temperature and time are lower than in arc welding, so joint efficiencies (weld strength over base strength) of 70–90 % are typical for 6xxx and 7xxx alloys against 50–70 % for arc welds. The previously "unweldable" 2xxx and 7xxx alloys can be friction stir welded without cracking, and residual stress and distortion are low.

FSW makes aluminium rail-car and ship-deck panels, launch-vehicle propellant tanks and electric-vehicle battery trays, and joins aluminium to copper or magnesium. Its limits are clamping forces of several tonnes, the tool's exit hole, simple joint paths and tool wear in steel and titanium (cubic boron nitride or W–Re tools). Typical defects are tunnel voids on the advancing side at low heat input and "kissing bonds" where the original oxide was not broken up.

<!-- FIGURE 39.5 | figures/ch39/fig-39-5-friction-stir-zones.png | schematic | Friction stir welding: tool, material flow and the microstructural zones of the joint in a precipitation-hardened aluminium alloy, with the hardness profile. | Content: upper left: 3D sketch of rotating tool (shoulder 18 mm, threaded pin 6 mm) traversing a butt joint between two clamped 6 mm plates; arrows for rotation, travel, advancing side (AS) and retreating side (RS), onion-ring flow pattern behind tool. Upper right: transverse section with stir zone (fine recrystallized grains 2–10 µm), TMAZ (bent elongated grains), HAZ, base metal labelled on both sides. Lower: hardness profile across the weld for 6061-T6 (base ~105 HV, HAZ minimum ~65 HV about 10 mm from centre on each side, stir zone ~70–80 HV) compared with a dashed profile for a GMAW weld of the same alloy (HAZ minimum ~55 HV, wider softened region, fusion zone of 4043 filler ~55 HV). x-axis distance from weld centre −30 to +30 mm. -->

### Other friction and pressure processes

- **Rotary and inertia friction welding** spins one part against another and then forges them together; used for drive shafts, valves, drill pipe and for joining dissimilar alloys in turbine rotor shafts. **Linear friction welding** oscillates a blade against a disc to make integrally bladed rotors (**blisks**) in titanium and nickel alloys.
- **Ultrasonic welding** vibrates sheets at about 20–40 kHz under modest pressure, scrubbing off oxides; it bonds battery tabs, wire harnesses and foils of Al and Cu with little heating.
- **Explosive welding** drives one plate obliquely into another at several hundred metres per second; a jet of surface material is ejected, and the clean surfaces bond with a characteristic wavy interface. It makes clad plate (stainless or titanium on steel) and **transition joints** for welding aluminium ship superstructures to steel decks.
- **Roll bonding** bonds ductile metals by heavy deformation that fractures surface oxide (clad coinage, brazing sheet).

### Diffusion bonding

**Diffusion bonding** holds clean, smooth surfaces in contact at high temperature (about 0.5–0.8$T_m$) under a pressure too low to cause macroscopic deformation, for times of minutes to hours. Bonding proceeds as in sintering (Chapter 17): surface asperities deform plastically and creep, voids at the interface shrink by surface, boundary and volume diffusion, and finally the interface boundary migrates away from the original plane. Titanium alloys are ideal because their oxide dissolves into the metal at high temperature. Combined with **superplastic forming** (Chapter 13) at the same temperature — Ti–6Al–4V at about 900–930 °C, with bonding pressures of about 1–2 MPa for 1–2 hours — it makes hollow fan blades and stiffened aircraft structures from stacks of sheet in which stop-off compounds prevent bonding where cavities are wanted. **Transient-liquid-phase (TLP) bonding** places a thin interlayer containing a melting-point depressant (boron or silicon in nickel alloys) at the joint; it melts, then solidifies isothermally as the depressant diffuses away, leaving a joint whose remelting temperature is that of the base metal. It is used to repair and assemble nickel-base turbine components.

---

## 39.7 Brazing and soldering

**Brazing** and **soldering** join parts with a filler metal whose liquidus is below the solidus of the parts. By convention the dividing line is 450 °C: below it the process is soldering, above it brazing. The parts do not melt, so their microstructure changes only through the thermal cycle, and dissimilar materials — steel to carbide, copper to stainless steel, metals to ceramics — can be joined.

### Wetting and capillary flow

The filler must **wet** the surfaces (contact angle $\theta$ well below 90°, Young's equation, Chapter 37) and flow into the joint gap by capillarity. For two parallel plates separated by a gap $h$, the meniscus has radius $h/(2\cos\theta)$ and the capillary pressure drawing liquid into the gap is

$$
\Delta p=\frac{2\gamma_{LV}\cos\theta}{h}
$$

Oxide films prevent wetting, so the surfaces are cleaned and protected during heating by **fluxes** (borates and fluorides for silver brazing, fluoroaluminates for aluminium, rosin and organic acids for soldering) or by **controlled atmospheres** (hydrogen, which reduces many oxides; vacuum, which lets oxides dissociate or dissolve at high temperature).

**Worked example — How far can capillarity pull a braze?** A silver-base braze ($\gamma_{LV}\approx0.9$ J/m$^2$, density about 10 000 kg/m$^3$) wets a cleaned steel joint with $\theta=20°$. For a gap of 0.05 mm,

$$
\Delta p=\frac{2\times0.9\times\cos20°}{5\times10^{-5}}=3.4\times10^{4}\ \mathrm{Pa}
$$

equivalent to a column of liquid braze $\Delta p/(\rho g)=3.4\times10^4/(10^4\times9.81)=0.34$ m high. Capillarity can therefore fill a long joint vertically against gravity. With a 0.5 mm gap the pressure falls tenfold, and the braze rises only about 34 mm; it also no longer fills uniformly and leaves voids. This is why recommended clearances for silver brazes are about 0.025–0.125 mm: small enough for strong capillary flow, large enough for the liquid to enter and for flux and gases to escape. In a properly designed lap, the brazed joint can be stronger than the filler itself because the thin layer is constrained by stronger base metal on both sides, which raises its yield stress through triaxial constraint.

### Filler metals and applications

| Filler (AWS class or common name) | Composition | Melting range (°C) | Brazing / soldering temperature (°C) | Typical applications |
|---|---|---|---|---|
| Sn–37Pb (legacy solder) | Sn–Pb eutectic | 183 | 210–240 | Electronics before RoHS, repair |
| SAC305 solder | Sn–3Ag–0.5Cu | 217–220 | 235–250 | Lead-free electronics |
| Sn–58Bi solder | Sn–Bi eutectic | 138 | 160–180 | Low-temperature assembly |
| BCuP (Cu–P, Cu–P–Ag) | Cu–6–7P (± Ag) | ≈ 645–800 | 700–815 | Copper plumbing and HVAC (self-fluxing on Cu) |
| BAg (Ag–Cu–Zn–Sn) | 40–56 Ag | ≈ 620–780 | 650–800 | Steel, stainless, copper, carbide tool tips |
| BAlSi-4 | Al–12Si | 577–582 | 590–605 | Aluminium automotive heat exchangers |
| Copper | Cu | 1083 | 1100–1150 | Furnace brazing of steel parts in H₂ |
| BNi-2 | Ni–7Cr–3Fe–4.5Si–3B | ≈ 970–1000 | 1010–1180 | Vacuum brazing of turbine and stainless parts |
| Active braze (Ag–Cu–Ti) | Ag–27Cu–2Ti | ≈ 780–815 | 830–900 | Ceramic–metal joints (alumina, Si₃N₄, diamond) |

*Typical values; exact ranges depend on the specification.*

Several materials points stand out. **Copper–phosphorus** fillers self-flux copper but form brittle phosphides on steel and nickel. **Aluminium brazing** works in a narrow window between the filler's melting (577 °C) and the base solidus (about 630–650 °C for 3xxx); radiators and condensers use **brazing sheet**, a 3xxx core clad with Al–Si, furnace brazed with fluoroaluminate flux. **Nickel braze** fillers contain boron and silicon as melting-point depressants; boron diffuses rapidly into the base metal and can form brittle borides in wide gaps, so diffusion-brazing cycles hold long enough to dissolve them. **Active brazes** containing titanium react with ceramics to form a thin wettable layer (TiO, TiN or TiC), allowing metals to be brazed to oxides, nitrides and diamond without prior metallization.

In all brazed and soldered joints, the filler reacts with the base metal to form **intermetallic compounds** at the interface — Cu$_6$Sn$_5$ and Cu$_3$Sn in tin solders on copper, Ni$_3$Sn$_4$ on nickel finishes. A thin continuous IMC layer is the bond; a thick one, grown during prolonged soldering or in service by diffusion with $x\propto\sqrt{Dt}$ (Chapter 8), is brittle and a common failure site. The detailed metallurgy of solder joints and electronic packaging is treated in the separate *Materials Core (EEE)* book.

---

## 39.8 Adhesive bonding

**Structural adhesive bonding** joins parts with a polymer layer typically 0.1–0.5 mm thick. It distributes load over an area instead of concentrating it at welds or holes, joins dissimilar and thin materials without heat damage, seals the joint and damps vibration. Aircraft have used bonded aluminium skins and honeycomb since the 1940s; modern car bodies contain 10–20 m or more of structural adhesive alongside spot welds and rivets; wind-turbine blades are two composite shells bonded along their edges and to internal shear webs; and composite repairs are bonded patches.

### How adhesives stick

Adhesion arises from (1) **intermolecular forces** — van der Waals and acid–base interactions across an intimately wetted interface; (2) **chemical bonds**, for example between epoxy hydroxyl groups or silane coupling agents and surface oxides; and (3) **mechanical interlocking** into a porous or rough surface such as an anodic oxide. All three require the liquid adhesive to wet the surface, which requires the surface energy of the adherend to exceed the surface tension of the adhesive (Chapter 37). Metals with clean oxides have high surface energies and are easily wetted; low-energy polymers such as polyethylene and polypropylene (about 30 mJ/m$^2$) are not, and must be activated.

### Surface preparation

Most service failures of adhesive bonds are interfacial and trace back to surface preparation, which must remove oils, release agents and weak oxides and leave a surface stable in moisture.

- **Aluminium**: degreasing, etching and anodizing. Aerospace **phosphoric acid anodizing** grows a porous, whiskered oxide that the primer penetrates and that resists hydration to weak hydroxide in humid service — the failure that destroyed some early bonded structures. Automotive practice uses Ti–Zr conversion coatings.
- **Steel**: degreasing and grit blasting, often with a silane primer; galvanized steel bonds to the zinc layer.
- **Composites**: abrading or removing a peel ply to expose fresh resin.
- **Polymers**: corona, flame or plasma treatment to oxidize the surface and raise its surface energy above about 40 mJ/m$^2$.

Joint durability is qualified by tests such as the **wedge test**, which drives a wedge into a bonded double-cantilever specimen exposed to hot, humid air and measures crack growth; a crack that runs along the interface rather than through the adhesive indicates poor preparation.

### Adhesive types

| Adhesive family | Cure | Typical lap-shear strength (MPa) | Service temperature (°C) | Typical use |
|---|---|---|---|---|
| Toughened epoxy (one-part, heat cured) | 120–180 °C | 25–40 | −55 to 120 (higher for some) | Aircraft structure, car bodies (crash-durable adhesives) |
| Epoxy (two-part) | Room temperature or warm | 15–30 | −40 to 80 | Composite repair, wind-turbine blades, civil strengthening |
| Structural acrylic (MMA) | Room temperature, fast | 15–25 | −40 to 100 | Marine, bus and truck panels |
| Polyurethane | Moisture or two-part | 5–15 | −40 to 90 | Windscreens, sandwich panels |
| Cyanoacrylate | Moisture, seconds | 10–20 | −40 to 80 | Small parts, medical |
| Silicone | Moisture | 1–3 | −60 to 200 | Glazing, electronics |
| Anaerobic | Absence of air, metal contact | 10–25 (in shear on threads) | −55 to 150 | Thread locking, retaining bearings |

*Typical values; strength depends strongly on adherends, preparation, bondline thickness and test.*

### Joint design: stresses in a lap joint

The single-lap shear test is the standard way to measure adhesive strength, but the stress in a lap joint is far from uniform. Because the adherends stretch under load, more at the loaded end of each, shear strain in the adhesive concentrates at the two ends of the overlap. Volkersen's **shear-lag analysis** of a lap joint between identical adherends of modulus $E$ and thickness $t$, with adhesive shear modulus $G_a$ and thickness $\eta_a$, gives a peak-to-average shear stress ratio

$$
\frac{\tau_{\max}}{\tau_{\mathrm{avg}}}=\frac{\omega L}{2}\coth\!\left(\frac{\omega L}{2}\right),\qquad\omega^{2}=\frac{2G_a}{E\,t\,\eta_a}
$$

for overlap length $L$. When $\omega L$ is small the stress is uniform; when it is large, all the load is carried within a distance of about $1/\omega$ of each end and the middle of the overlap is nearly unloaded.

> **Status of the principle: Volkersen shear-lag model**
> *Approximate.* It treats the adherends as bars in tension and the adhesive as a linear-elastic shear spring, neglecting bending and peel. It captures the end concentration of shear stress; the Goland–Reissner analysis adds the peel stresses caused by the eccentric load path, and adhesive plasticity redistributes stress before failure.

**Worked example — Does a longer overlap help?** Two 2 mm aluminium sheets ($E=70$ GPa), 25 mm wide, are bonded with a 0.2 mm epoxy layer of shear modulus 1.0 GPa. Then

$$
\omega=\sqrt{\frac{2\times1.0\times10^{9}}{70\times10^{9}\times0.002\times0.0002}}=267\ \mathrm{m^{-1}}
$$

so $1/\omega=3.7$ mm. With a 25 mm overlap, $\omega L/2=3.34$ and $\tau_{\max}/\tau_{\mathrm{avg}}=3.34\coth3.34=3.35$. If the adhesive is taken to behave elastically up to a shear stress of 30 MPa, the joint reaches that stress at the overlap ends at a load of

$$
F=\frac{30}{3.35}\times(25\times25)=5.6\ \mathrm{kN}
$$

although the average-stress estimate would suggest 18.8 kN. Doubling the overlap to 50 mm gives $\omega L/2=6.68$, a ratio of 6.68, and the elastic-limit load stays at 5.6 kN: the extra overlap carries almost nothing (Figure 39.6). Halving it to 12.5 mm gives 5.2 kN. In the elastic regime, the joint capacity is set by $\omega$, not by $L$, once $L$ exceeds a few times $1/\omega$. Real joints do better because toughened adhesives yield at the ends and spread the load, so strength rises with overlap until the plastic zones meet — which is why ductile, toughened adhesives are used in structures. The analysis also shows how to improve a joint: stiffer or thicker adherends (steel adherends of the same thickness give $\omega=154$ m$^{-1}$ and a ratio of 2.0), a more compliant or thicker adhesive layer, and **tapered** adherend ends, scarf joints or stepped laps that make the load transfer gradual.

<!-- FIGURE 39.6 | figures/ch39/fig-39-6-lap-joint-shear-lag.png | plot | Adhesive shear-stress distribution along a single-lap joint from the Volkersen shear-lag model, for different overlap lengths, with joint configurations ranked by efficiency. | Content: main plot: x-axis normalized position along overlap x/L from −0.5 to +0.5; y-axis τ/τ_avg 0–7. Curves for Al adherends 2 mm, epoxy G = 1 GPa, 0.2 mm bondline: L = 12.5 mm (ωL/2 = 1.67, peak 1.79), L = 25 mm (peak 3.35), L = 50 mm (peak 6.68), showing U-shaped distributions increasingly concentrated at the ends. Horizontal dashed line at 1 'uniform (rigid adherends)'. Secondary panel: elastic-limit joint load (kN) versus overlap length 5–60 mm for τ_allow = 30 MPa: saturating near 5.6 kN; dashed line of average-stress estimate rising linearly. Bottom strip: sketches of single lap, tapered lap, double lap, stepped lap and scarf joint, arrows indicating increasing efficiency; small icons showing peel loading to avoid. -->

### Design rules

Adhesives are strong in shear and compression and weak in **peel** and **cleavage**, where load concentrates on a line at the bond edge. Good joints load the bondline in shear (lap, double-lap, strap, scarf), and resist peel with stiff adherends, adhesive fillets and supplementary rivets or spot welds. Adhesive properties fall as the polymer approaches its glass transition (Chapter 20), and adhesives creep, so allowables are set at the maximum service temperature after humidity aging. "Kissing bonds" — surfaces in contact without adhesion — are nearly invisible to inspection, which is why primary aircraft structure relies on tight process control of surface preparation and often on fail-safe fasteners.

---

## 39.9 Mechanical fastening and joining dissimilar materials

### Bolts, rivets and clinching

**Bolted joints** in structural steelwork are either bearing-type, where bolts carry shear by bearing on the hole walls, or **preloaded (slip-resistant)** joints, where high-strength bolts (grade 8.8 or 10.9, ASTM A325/A490 types) are tightened to about 70 % of their tensile strength so that the clamping force generates friction between the plates; the load then passes by friction and the bolts see little fluctuating stress, which is excellent for fatigue. Bolt tightening is controlled by torque, turn-of-nut or direct-tension indicators. High-strength bolts above roughly 1000 MPa tensile strength are susceptible to hydrogen embrittlement from galvanizing or corrosion (Chapter 35), which is why the strongest bolt grades are not hot-dip galvanized.

**Rivets** remain the main fastener of aluminium aircraft, by the hundred thousand per fuselage. Each hole concentrates stress (factor about 3 for an open hole in tension), and fatigue cracks at rivet holes are the classic airframe failure; cold expansion of holes and interference-fit fasteners add compressive residual stress to delay them. **Self-piercing rivets**, **clinching** (an interlocking button pressed without any added part) and **flow-drill screws** join aluminium and mixed-material car bodies where spot welding is difficult. Fasteners allow disassembly and need no heat or surface preparation, but add mass, need stress-concentrating holes and create crevices for corrosion.

### Joining dissimilar materials

Lightweight structures increasingly mix steel, aluminium, magnesium, titanium and fibre composites, and every pair raises three materials problems:

1. **Metallurgical incompatibility.** Fusion welding of aluminium to steel forms brittle Fe–Al intermetallics (Fe$_2$Al$_5$, FeAl$_3$) at the interface; once the layer exceeds roughly 10 µm, the joint is brittle. Titanium to steel forms brittle Fe–Ti phases. Solutions keep the interface cold and short-lived: solid-state processes (friction stir, friction, ultrasonic, explosive welding), brazing-like processes in which only aluminium melts and wets galvanized steel, or **transition joints** — explosion-welded aluminium–steel strips welded each to its own metal, as used to attach aluminium superstructures to steel ship hulls.
2. **Galvanic corrosion.** In an electrolyte, the less noble member of a couple corrodes preferentially (Chapter 35). Aluminium against steel, magnesium against almost anything, and especially aluminium against **carbon-fibre composite** (carbon is strongly cathodic) are dangerous couples. Designs isolate them with sealants, coatings, insulating washers, a glass-fibre isolation ply between carbon composite and aluminium, or by using titanium fasteners and titanium fittings, which are compatible with carbon composites.
3. **Thermal-expansion mismatch.** Aluminium expands by about $23\times10^{-6}$ K$^{-1}$, steel by about $12\times10^{-6}$ K$^{-1}$, and carbon-fibre laminates in-plane by almost nothing. A 1 m aluminium panel fixed to a steel frame and heated by 60 K, as in a car-body paint oven, wants to grow $(23-12)\times10^{-6}\times1000\times60=0.66$ mm more than the frame. If fasteners are rigid and the adhesive is cured at that temperature, the panel buckles or the joints are loaded on cooling; joining sequences, slotted holes and compliant adhesives absorb the difference.

**Hybrid joints** cover each method's weakness: in aluminium car bodies adhesive carries shear and seals while self-piercing rivets resist peel and hold parts during cure; aircraft use bolted–bonded composite joints.

---

## 39.10 Choosing a joining method

| Criterion | Fusion welding | Solid-state welding | Brazing / soldering | Adhesive bonding | Mechanical fastening |
|---|---|---|---|---|---|
| Joint strength vs base | Up to 100 % (steel); 50–70 % (age-hardened Al) | 70–100 % | Filler-limited, high in good laps | Shear-limited; poor in peel | Hole-limited; 50–80 % in sheet |
| Heat effect on parts | Large: HAZ, residual stress, distortion | Moderate, no melting | Small to moderate (whole part heated in furnace brazing) | Little (cure temperature) | None |
| Dissimilar materials | Limited | Good | Good, including ceramics | Excellent | Excellent |
| Section thickness | Thin to very thick | Mostly moderate | Thin to moderate | Thin sheets | Any |
| Inspection | Radiography, ultrasound | Ultrasound, limited | Ultrasound, leak test | Difficult (kissing bonds) | Visual, torque checks |
| Disassembly | No | No | Possible by reheating | No | Yes |
| Typical uses | Ships, bridges, pipelines, vessels | Al tanks, blisks, clad plate | Heat exchangers, tools, electronics | Aircraft panels, car bodies, blades | Aircraft, steelwork, maintenance joints |

Where full-strength continuous metal is needed in thick weldable steel, fusion welding wins, and the materials task is to control heat input, hydrogen and composition. Where strength comes from cold work or precipitation, or alloys crack on freezing, solid-state or mechanical methods preserve it. Where heat must be kept out or dissimilar materials meet, brazing, adhesives and fasteners take over, and the task becomes surface preparation, joint geometry and corrosion protection. The joint is part of the material's processing history.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How do solidification modes, segregation and constitutional supercooling work in a weld pool? | Chapter 9 |
| How do CCT diagrams and hardenability predict HAZ microstructure in steels? | Chapters 10 and 15 |
| Why do welded details have low fatigue strength, and how is weld toughness tested? | Chapter 14 |
| How are TMCP, stainless and Ni-base alloys designed for weldability? | Chapters 15–16 |
| How do composite laminates behave in bolted and bonded joints? | Chapter 23 |
| How do galvanic corrosion, hydrogen embrittlement and stress-corrosion cracking attack joints? | Chapter 35 |
| How are failed welds and joints investigated? | Chapter 36 |
| What are the thermodynamics of wetting, surface energy and adhesion? | Chapter 37 |
| How does the melt-pool physics of welding carry over to additive manufacturing? | Chapter 40 |
| How are residual stresses in welds measured by X-ray and neutron diffraction? | Chapter 43 |
| How are welding thermal cycles and microstructures simulated? | Chapter 46 |
| How do joining costs and disassembly affect material and design choices? | Chapters 48–49 |

**Next:** Chapter 40 turns the welding heat source into a manufacturing method in its own right: additive manufacturing builds whole parts from millions of tiny weld tracks, layers of fused powder or cured resin, and inherits both the possibilities and the defects of welding.
