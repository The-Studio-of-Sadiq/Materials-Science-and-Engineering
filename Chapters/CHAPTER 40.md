# Chapter 40 — Additive Manufacturing

*Part IX · Processing and Manufacturing*

A jet-engine fuel nozzle tip used to be brazed together from about twenty separately machined parts. Printed by laser powder-bed fusion in a cobalt–chromium alloy, it became one part with internal cooling passages that could not have been drilled, a quarter lighter and several times more durable, and it went into service in tens of thousands of engines. In the same years, a titanium hip cup printed with a porous outer lattice let bone grow into it; a rocket maker printed combustion chambers in a copper alloy with hundreds of internal coolant channels; and a dental lab replaced hand-cast crowns with printed ones. There were also failures: printed titanium brackets that failed in fatigue at a fraction of the wrought value because of unfused powder pockets a tenth of a millimetre across; aluminium alloys that cracked like poorly welded seams; and parts whose properties changed when the same file was printed on another machine. **Additive manufacturing (AM)** — building a part layer by layer directly from a digital model — is at once a new freedom of shape and a new metallurgy. Every millimetre of a printed metal part is a weld track, solidified at rates closer to a weld or a splat than to a casting.

> **What happens to a material when it is built from millions of tiny melt pools, sintered layers or cured slices?**
> **Which process conditions avoid porosity, cracking and distortion, and how does one prove that a printed part is as good as a forged one?**

| Concept | Engineering destination |
|---|---|
| Process families (PBF, DED, binder jetting, material extrusion, vat photopolymerization) | Choice of machine and route for a part, material and batch size |
| Energy density, melt-pool modes, process windows | Parameter development, avoiding lack of fusion and keyhole porosity |
| Rapid solidification, $G$ and $R$, columnar growth | Fine strong microstructures, texture and anisotropy of printed alloys |
| Porosity, residual stress, cracking | Fatigue life of printed brackets and implants, distortion, build failures |
| HIP, heat treatment, machining | Turning as-built material into certifiable material |
| Polymer and ceramic AM | Prototypes, jigs, dental aligners, surgical guides, ceramic cores |
| Design for AM, lattices, topology optimization | Lightweight brackets, heat exchangers, porous implants, consolidated assemblies |
| Qualification and certification | Flight hardware, medical devices, pressure equipment |

**Roadmap.** What AM is (40.1) → the process families (40.2) → melt-pool physics and solidification (40.3) → microstructure and defects (40.4) → post-processing (40.5) → polymer and ceramic AM (40.6) → design for AM (40.7) → qualification and certification (40.8).

> **Boundary.** Heat flow and solidification are developed in Chapters 9 and 39 and used here; powder production and sintering in Chapters 38 and 17; photopolymer chemistry in Chapter 19. Laser optics, machine design and slicing software belong to manufacturing engineering. Process simulation is introduced in Chapter 46.

---

## 40.1 What additive manufacturing is

Subtractive manufacturing removes material from a block; formative manufacturing (casting, forging, moulding) shapes it in a die or mould. **Additive manufacturing** builds a part by joining material, usually layer upon layer, from a 3D model sliced into layers 0.02–1 mm thick. The international terminology standard ISO/ASTM 52900 groups AM processes into seven families: **powder bed fusion**, **directed energy deposition**, **binder jetting**, **material extrusion**, **vat photopolymerization**, **material jetting** and **sheet lamination**.

AM's value lies in three things that other routes do poorly:

1. **Geometric freedom.** Internal channels, lattices, undercuts and organic shapes cost nothing extra; complexity is "free" while volume and build height are not.
2. **No tooling.** The economics favour low volumes, customization (implants, dental restorations, hearing-aid shells) and fast iteration.
3. **Part consolidation.** Assemblies of many brazed or bolted pieces become one part, eliminating joints and their failure modes.

Its costs are equally clear: slow build rates (tens of cm$^3$/h per laser for metals), expensive feedstock, surface roughness, anisotropic properties and process-sensitive defects. AM therefore complements casting, forging and machining rather than replacing them, and its engineering success depends on understanding the materials science of this chapter.

---

## 40.2 Process families

### Powder-bed fusion

In **powder-bed fusion (PBF)** a thin layer of powder is spread over a build plate by a recoater blade or roller, a heat source melts (or, for polymers, sinters) the cross-section of the part, the plate drops by one layer thickness, and the cycle repeats. Unmelted powder supports the part and is recovered and sieved for reuse.

- **Laser powder-bed fusion (PBF-LB, also called SLM or DMLS)** scans one or more 200–1000 W fibre lasers, focused to 50–100 µm, at 0.5–2 m/s over layers 20–60 µm thick, under argon or nitrogen. It gives the finest features and best surface of the metal processes and dominates metal AM for Ti–6Al–4V, Inconel 718 and 625, 316L and 17-4PH stainless steels, AlSi10Mg, CoCr and copper alloys. The part is welded to the build plate and needs supports under overhangs, both to anchor it against distortion and to conduct heat away.
- **Electron-beam powder-bed fusion (PBF-EB)** scans a beam of several kilowatts in vacuum, deflected electromagnetically at speeds up to several km/s, over 50–100 µm layers. Each layer is first preheated by a defocused beam, lightly sintering the powder (which stops it being blown away by charge build-up) and keeping the whole bed hot — 650–750 °C for Ti–6Al–4V, over 1000 °C for TiAl. Residual stress is therefore low and crack-prone alloys such as γ-TiAl turbine blades and some nickel superalloys can be built, at the cost of rougher surfaces and coarser features.
- **Polymer PBF (laser sintering)** sinters polyamide 12, PA11 or TPU powder held just below its melting point; the surrounding powder supports the part, so no supports are needed (Section 40.6).

### Directed energy deposition

In **directed energy deposition (DED)** powder or wire is fed into a melt pool created by a laser, electron beam or arc that moves with the feed nozzle, like automated welding. Layers are 0.25–3 mm thick and deposition rates range from about 0.1 kg/h for fine laser-powder DED to several kg/h for **wire-arc additive manufacturing (WAAM)**, which uses a GMAW or plasma torch on a robot. DED builds large near-net shapes (titanium aircraft frames, steel ship propellers, large valve bodies), adds features to existing parts and **repairs** worn turbine blades, moulds and shafts. Resolution is coarse, so DED parts are machined, and the large melt pools give coarser microstructures than PBF.

### Binder jetting

**Binder jetting** spreads powder and prints a liquid binder onto each layer with inkjet heads, like a paper printer. No melting occurs during the build, so there is no residual stress, no supports and very high throughput; the whole bed can be filled with nested parts. The printed "green" part is cured, removed from the powder, debound and **sintered** (Chapter 38), shrinking 15–20 % linearly — for a green density of 55 % sintered to 97 %, the linear shrinkage is $1-(0.55/0.97)^{1/3}=17$ % — or **infiltrated** with bronze. Stainless steels, tool steels, tungsten carbide, sand moulds and cores for casting, and ceramics are printed this way. Dimensional control of sintering shrinkage and slumping is its main difficulty.

### Material extrusion

**Material extrusion (MEX)**, best known as fused filament fabrication, pushes a thermoplastic filament through a heated nozzle of 0.2–1 mm and deposits beads layer by layer. It is the cheapest and most widespread AM process — from desktop printers to large-format machines that print car moulds and boat hulls — and also deposits metal- or ceramic-filled filaments that are then debound and sintered, as well as concrete (Section 40.6).

### Vat photopolymerization

**Vat photopolymerization (VPP)** cures a liquid photopolymer resin layer by layer with ultraviolet light: a scanned laser (**stereolithography, SLA**), a projected image (**digital light processing, DLP**) or continuous variants that cure through an oxygen-permeable window. It gives the finest resolution (25–100 µm) and smoothest surfaces of common AM processes and is used for dental models and aligner moulds, hearing-aid shells, jewellery casting patterns, microfluidics and, with ceramic-filled resins, ceramic parts.

### Material jetting and sheet lamination

**Material jetting** deposits droplets of photopolymer (or wax, or metal nanoparticle inks) from inkjet heads and cures them, allowing multi-material and full-colour parts. **Sheet lamination** bonds stacked sheets — paper, polymer, or metal foils joined by ultrasonic welding (ultrasonic additive manufacturing) — and machines each layer's contour.

| Process family | Feedstock | Energy / bonding | Layer thickness | Typical resolution | Typical materials | Typical applications |
|---|---|---|---|---|---|---|
| PBF-LB (metal) | Powder 15–45 µm | Laser melting | 20–60 µm | 0.1–0.2 mm | Ti–6Al–4V, IN718, 316L, AlSi10Mg, CoCr | Brackets, fuel nozzles, implants, heat exchangers |
| PBF-EB (metal) | Powder 45–105 µm | Electron-beam melting, hot bed | 50–100 µm | 0.3–0.5 mm | Ti–6Al–4V, γ-TiAl, CoCr | Implants, TiAl blades |
| DED (laser, arc) | Powder or wire | Laser, EB or arc melting | 0.25–3 mm | 0.5–5 mm | Ti alloys, steels, Ni alloys | Large preforms, repair, cladding |
| Binder jetting | Powder 5–30 µm | Binder, then sinter | 30–100 µm | 0.1–0.3 mm | Stainless, tool steel, WC–Co, sand, ceramics | Volume metal parts, casting moulds |
| Material extrusion | Filament, pellets, paste | Melt and fuse | 0.1–1 mm | 0.2–1 mm | PLA, ABS, PC, PEEK, composites, concrete | Prototypes, jigs, tooling, buildings |
| Vat photopolymerization | Liquid resin | UV curing | 25–100 µm | 25–100 µm | Acrylates, epoxies, ceramic slurries | Dental, hearing aids, microfluidics |
| Polymer PBF | Powder 50–80 µm | Laser sintering | 80–120 µm | 0.3–0.5 mm | PA12, PA11, TPU | Functional plastic parts, ducts |

*Typical ranges.*

<!-- FIGURE 40.1 | figures/ch40/fig-40-1-am-process-families.png | schematic | Five principal additive manufacturing process families shown as simplified machine cross-sections. | Content: five panels side by side. (a) PBF-LB: build plate on piston, powder bed, recoater blade moving across, powder supply piston, laser beam from galvo scanner focused on bed, melted tracks, part with support structures, argon flow arrow. (b) DED: nozzle with coaxial powder streams (or wire) feeding a melt pool on a substrate, laser/arc from above, several tall deposited layers, robot arm hint. (c) Binder jetting: inkjet printhead depositing binder droplets on a powder layer, recoater; inset arrow to 'sinter furnace' with part shrinking ~17 %. (d) Material extrusion: heated nozzle depositing a thermoplastic bead from a filament, layers of rounded beads with voids between them. (e) Vat photopolymerization (bottom-up DLP): resin vat with transparent window, UV projector below, build platform lifting the part upward. Labels: typical layer thickness under each (30 µm, 1 mm, 50 µm, 0.2 mm, 50 µm). -->

Figure 40.1 sketches the five main families. The rest of the chapter concentrates on metal PBF and DED, where the materials science is most demanding, and returns to polymers and ceramics in Section 40.6.

---

## 40.3 Melt-pool physics and solidification

### Energy input and absorption

A laser track in PBF-LB is a miniature keyhole or conduction weld, a fraction of a millimetre wide, made in a few milliseconds. Only part of the beam power is absorbed: the **absorptivity** $\eta$ of a flat metal surface to near-infrared light is only 0.05–0.4, but a powder bed traps light by multiple reflections and absorbs more (often 0.4–0.7), and a keyhole absorbs most of it. Highly reflective, highly conductive metals — copper, silver, gold, and to a lesser extent aluminium — are the hardest to print for this reason.

The process parameters are commonly combined into a **volumetric energy density**

$$
E_v=\frac{P}{v\,h\,t}
$$

for laser power $P$, scan speed $v$, hatch spacing $h$ (distance between adjacent tracks) and layer thickness $t$. Typical PBF-LB values are 50–70 J/mm$^3$ for Ti–6Al–4V and IN718, 40–60 J/mm$^3$ for AlSi10Mg and 60–100 J/mm$^3$ for 316L. For example, Ti–6Al–4V at 280 W, 1200 mm/s, 0.14 mm hatch and 30 µm layers gives $280/(1200\times0.14\times0.03)=56$ J/mm$^3$. The same numbers give the theoretical build rate per laser, $vht=5.0$ mm$^3$/s or about 18 cm$^3$/h, before recoating and scan-jump time are subtracted — which is why production machines carry four to twelve lasers.

> **Status of the principle: volumetric energy density as a process variable**
> *Empirical.* $E_v$ correlates density with parameters within one machine, alloy and parameter neighbourhood, but it is not a physical invariant: two parameter sets of equal $E_v$ can give different melt-pool shapes and defects, because $P$ and $v$ act differently on melt-pool depth. Normalized enthalpy and melt-pool-geometry criteria are more transferable.

### Melt-pool modes

As in welding (Chapter 39), the melt pool operates in one of two modes.

- **Conduction mode**: the surface melts but does not vaporize significantly; the pool is shallow and roughly semicircular in cross-section, and heat flows outward from the surface.
- **Keyhole mode**: at high power and low speed, the surface temperature exceeds the boiling point, recoil pressure from evaporation depresses the surface into a deep, narrow cavity, and absorption rises sharply. A stable keyhole gives deep penetration; an unstable one collapses intermittently and traps vapour bubbles, leaving round **keyhole pores** at the bottom of the track.

Inside the pool, the surface tension of most liquid metals decreases with temperature, so surface tension is highest at the cool edges and pulls liquid outward from the hot centre: the **Marangoni flow** that widens pools. Surface-active elements such as oxygen and sulfur can reverse the sign of $d\gamma/dT$ and deepen the pool. Fluid velocities reach around 1 m/s, so convection, not conduction alone, shapes the pool and mixes the melt.

At the other extreme, too little energy or too fast a scan produces either **lack of fusion** between tracks and layers or, at high speed, **balling**: the long, thin liquid track breaks up into droplets by the Plateau–Rayleigh instability, because a liquid cylinder longer than about its circumference is unstable. A process map in the $P$–$v$ plane (Figure 40.2) therefore shows a window of dense parts bounded by lack of fusion (low $P$, high $v$), keyholing (high $P$, low $v$) and balling (high $P$ and high $v$).

<!-- FIGURE 40.2 | figures/ch40/fig-40-2-process-window.png | map | Laser power–scan speed process map for PBF-LB of Ti–6Al–4V with 30 µm layers and 0.14 mm hatch, showing the dense-part window and the defect regimes around it. | Content: x-axis scan speed 200–2500 mm/s; y-axis laser power 50–450 W. Dashed lines of constant energy density E_v = 30, 56 and 120 J/mm³ (straight lines P ∝ v). Regions: 'lack of fusion' at low P / high v (lower right); 'keyhole porosity' at high P / low v (upper left); 'balling / humping' at high P and very high v (upper right); central 'dense (> 99.5 %)' window around the 56 J/mm³ line from ~150 W/600 mm/s to ~370 W/1600 mm/s. Marked point at 280 W, 1200 mm/s labelled 'worked example'. Arrow from that point to 280 W, 1500 mm/s crossing into lack of fusion. Inset sketches of melt-pool cross-sections: shallow conduction, deep keyhole with trapped pore, and irregular lack-of-fusion gap between tracks. -->

### Melt-pool size and the lack-of-fusion criterion

The Rosenthal solution for a moving point source (Chapter 39) gives a useful estimate of melt-pool size in conduction mode. At the high speeds of PBF the melt-pool cross-section approaches a semicircle whose width $w$ follows from maximizing the isotherm radius behind the source:

$$
w^{2}=\frac{8\,\eta P}{\pi e\,\rho c\,v\,(T_m-T_0)}
$$

with $\rho c$ the volumetric heat capacity and $e$ the base of natural logarithms; the depth is then about $w/2$. A simple geometric condition for full fusion, due to Tang, Pistorius and Beuth, requires adjacent tracks and layers to overlap: for hatch $h$, layer thickness $t$, pool width $W$ and depth $D$,

$$
\left(\frac{h}{W}\right)^{2}+\left(\frac{t}{D}\right)^{2}\le1
$$

If the sum exceeds 1, unmelted pockets remain between tracks.

**Worked example — Is this parameter set in the dense window?** Take Ti–6Al–4V with $\eta=0.5$, $P=280$ W, $v=1.2$ m/s, $\rho c=4430\times670=2.97\times10^{6}$ J/m$^3$K, solidus $T_m=1604$ °C and $T_0=35$ °C, so $T_m-T_0=1569$ K. Then

$$
w^{2}=\frac{8\times0.5\times280}{\pi\times2.718\times2.97\times10^{6}\times1.2\times1569}=2.35\times10^{-8}\ \mathrm{m^2},\qquad w=153\ \mu\mathrm{m}
$$

and the depth is about 77 µm, enough to remelt two layers of 30 µm. With $h=140$ µm,

$$
\left(\frac{140}{153}\right)^{2}+\left(\frac{30}{77}\right)^{2}=0.84+0.15=0.99\le1
$$

The parameter set just satisfies the overlap condition. Increase the scan speed to 1.5 m/s to build faster and $w$ falls as $v^{-1/2}$, to 137 µm with depth 69 µm; the sum becomes $1.04+0.19=1.24$, and lack-of-fusion porosity appears between tracks. A 25 % gain in speed has crossed the boundary in Figure 40.2. In practice the pool also contains a partial keyhole and Marangoni flow, so Rosenthal underestimates depth, and parameter development confirms windows by building cubes and measuring density; but the scaling — $w\propto\sqrt{\eta P/v}$ — is the right guide.

> **Status of the principle: Rosenthal melt-pool estimate and overlap criterion**
> *Approximate.* A point source moving over a semi-infinite solid with constant properties, no latent heat and no fluid flow. It predicts trends and order of magnitude in conduction mode; it underestimates depth in keyhole mode and ignores the powder layer, heat accumulation in thin features and the previous tracks.

### Cooling rate, thermal gradient and solidification rate

From the same solution, the cooling rate at the solidus on the track centreline is

$$
\dot T=\frac{2\pi k\,(T_m-T_0)^2\,v}{\eta P}
$$

With $k=20$ W/m K for Ti–6Al–4V near its solidus and the parameters above, $\dot T=2\pi\times20\times1569^2\times1.2/140=2.7\times10^{6}$ K/s. The thermal gradient behind the pool is $G=\dot T/v=2.2\times10^{6}$ K/m, or 2.2 K/µm, and the solidification rate on the centreline equals the scan speed, $R\approx v=1.2$ m/s, falling toward zero at the bottom of the pool. Compare a sand casting with $G\sim10^{3}$ K/m and $R\sim10^{-4}$ m/s, or an arc weld with $\dot T\sim10^{2}$–$10^{3}$ K/s. PBF solidifies three to four orders of magnitude faster than conventional welding, and DED and WAAM, with larger pools, lie in between (about 10$^2$–10$^4$ K/s).

The consequences follow from Chapter 9:

- **Fine solidification structures.** Primary dendrite or cell spacing scales roughly as $\lambda_1\propto\dot T^{-1/3}$ to $\dot T^{-1/2}$. In PBF it is 0.3–1 µm: 316L shows a cellular substructure of about 0.5 µm with Cr and Mo segregated to cell walls and a high dislocation density, which gives a yield strength of 450–550 MPa, roughly double that of annealed wrought 316L, with good ductility. AlSi10Mg forms a fine cellular network of eutectic silicon around α-Al cells, giving higher strength than the cast alloy.
- **Columnar, epitaxial growth.** Each new track remelts the one below and grows epitaxially from it, as in a multipass weld. With high $G/R$ at the pool bottom, grains grow as columns along the build direction across many layers, often with a ⟨100⟩ fibre texture along the build direction. The **columnar-to-equiaxed transition (CET)**, predicted by Hunt's criterion to occur when $G^n/R$ falls below an alloy-dependent constant (with $n\approx3$–$4$), is hard to reach in PBF because $G$ is so high; equiaxed grains need potent inoculants or alloys designed for AM.
- **Metastable phases.** Ti–6Al–4V cools fast enough to form **α′ martensite** within the columnar prior-β grains: high strength (tensile strength 1100–1300 MPa) but limited ductility (5–10 %). Rapid cooling also extends solid solubility, suppresses equilibrium precipitates in nickel alloys, and can retain austenite in martensitic steels.
- **Intrinsic heat treatment.** Each layer is reheated many times by the tracks above it, with peaks that diminish with distance. These cycles temper martensite, precipitate phases or (in PBF-EB, with its hot bed) decompose α′ into fine α+β during the build. Properties therefore vary with height and with the time between layers — a feature of AM with no counterpart in casting.

<!-- FIGURE 40.3 | figures/ch40/fig-40-3-g-r-solidification-map.png | map | Solidification map of thermal gradient G versus solidification rate R, locating casting, welding, DED and PBF and the morphology regions. | Content: log–log axes: x-axis R from 10^-6 to 10 m/s; y-axis G from 10^2 to 10^8 K/m. Diagonal lines of constant cooling rate G·R = 1, 10^2, 10^4, 10^6 K/s (finer structure toward upper right); lines of constant G/R separating 'planar' (upper left), 'cellular', 'columnar dendritic' and 'equiaxed dendritic' (lower right) regions for a generic alloy. Process ellipses: sand casting (G 10^2–10^3, R 10^-5–10^-4), directional solidification (G ~10^3–10^4, R ~10^-5), arc welding (G 10^4–10^5, R 10^-3–10^-2), DED/WAAM (G 10^4–10^6, R 10^-3–10^-2), PBF-LB (G 10^5–10^7, R 10^-2–1). Point marked for worked example: G = 2.2×10^6 K/m, R = 1.2 m/s (cooling rate 2.7×10^6 K/s). Arrow along PBF ellipse from pool bottom (low R, high G/R → columnar) to top centreline (high R). -->

Figure 40.3 locates the AM processes among other solidification routes; the high-$G$, high-$R$ corner occupied by PBF explains both its fine structure and its stubbornly columnar grains.

---

## 40.4 Microstructure and defects

### Porosity

Three kinds of pore dominate metal AM, each with a characteristic shape and cause (Figure 40.4):

- **Lack-of-fusion (LOF) pores**: irregular, flat, crack-like voids between tracks or layers, often containing unmelted powder particles, caused by insufficient energy or overlap (the criterion above), spatter particles landing on the bed, or recoating defects. They are the most damaging because they are large (50–500 µm), sharp and often oriented parallel to the layers.
- **Keyhole pores**: spherical voids of 20–100 µm at the bottom of tracks, caused by keyhole collapse at excessive energy density, particularly at the turnaround points of scan vectors where the laser slows.
- **Gas pores**: small (5–30 µm) spherical pores from argon trapped inside gas-atomized powder particles or from dissolved hydrogen (moisture on aluminium powder). They are relatively benign but cannot be removed by HIP if they contain insoluble argon.

Well-optimized PBF-LB routinely achieves 99.5–99.9 % density; the defect population that remains, and its largest member, decide fatigue.

### Spatter, powder and surface

The laser ejects **spatter** — molten droplets and entrained powder particles — that can land on the bed, become larger than the layer thickness, and cause LOF in the next layer; gas flow across the bed is designed to carry it away. Powder recycled many times picks up oxygen and coarse spatter particles, so powder chemistry and size distribution are monitored lot by lot. **Surface roughness** of as-built PBF-LB metal surfaces is typically Ra 5–20 µm (worse on down-facing surfaces, which sit on loose powder), and PBF-EB and DED surfaces are rougher still. Partly fused particles and notch-like valleys between layers act as surface cracks in fatigue.

### Residual stress, distortion and cracking

Residual stresses arise as in a weld (Chapter 39), with an AM-specific twist known as the **temperature-gradient mechanism**: the newly melted layer is hot and expands against cooler material beneath, yields in compression, and on cooling contracts and is left in tension, while the material below is put in compression. Layer upon layer, this builds tensile stresses near the top surface and the edges, often reaching the yield strength. While the part is welded to its build plate the stresses are balanced; when the part is cut off, it distorts. Stresses can also crack the part or the supports, or lift the part off the plate during the build. Remedies include preheating the plate (200 °C for aluminium, up to 500 °C or more for crack-prone alloys), island or rotating scan strategies that shorten scan vectors and change their direction every layer, adequate supports, and a **stress-relief anneal before removal** from the plate.

**Cracking** in AM follows the welding classification. **Solidification cracking** limits the high-strength aluminium alloys 2024, 6061 and 7075, whose wide freezing range and long columnar grains with continuous interdendritic liquid films make them crack in PBF just as they do in autogenous welds. Two strategies work: alloys designed for AM, such as Al–Mg–Sc–Zr, in which Al$_3$(Sc,Zr) particles formed in the melt nucleate fine equiaxed grains, and **inoculating** conventional alloys with nanoparticles (for example Zr-based or TiB$_2$ additions) that do the same — breaking the columnar structure and allowing crack-free 7075 and 6061. Nickel superalloys with high γ′ fractions (such as IN738LC and CM247LC) suffer solidification and liquation cracking and **strain-age cracking**, which PBF-EB with its hot bed partly avoids. Carbon steels and tool steels with high hardenability suffer cold cracking from martensite, mitigated by plate preheating.

### Anisotropy

Columnar grains along the build direction, crystallographic texture, layer-aligned LOF defects and the "stacking" of melt-pool boundaries make as-built AM metals **anisotropic**. Typically, Ti–6Al–4V tested with the load parallel to the build direction (vertical specimens) has lower elongation and lower fatigue strength than horizontal specimens, because flat LOF defects lie perpendicular to the load. Elastic modulus also varies with texture. Specifications therefore require testing in several build orientations, and HIP and recrystallization treatments reduce, though rarely remove, the anisotropy.

<!-- FIGURE 40.4 | figures/ch40/fig-40-4-am-defects.png | micrograph-style | Characteristic defects in laser powder-bed-fused metal: lack-of-fusion voids, keyhole pores, gas pores, columnar grains, and the residual-stress mechanism. | Content: left: schematic polished cross-section (build direction vertical, 1 mm field) showing stacked melt-pool boundaries as overlapping arcs; an irregular flat lack-of-fusion void ~200 µm wide with an unmelted powder particle between two layers; spherical keyhole pores ~50 µm at melt-pool bottoms; tiny gas pores ~10 µm; columnar prior grains crossing many layers along build direction; rough top surface with partly fused particles (Ra ~10 µm). Right: two-panel cartoon of the temperature-gradient mechanism: (1) heated top layer expanding, compressive yielding; (2) after cooling, top layer in tension (+) and layers beneath in compression (−); below, distortion of a cantilever after cutting from the build plate. -->

### Fatigue: why the largest defect matters

Static strength of well-made AM metal matches or exceeds wrought material, but fatigue does not, unless defects and surfaces are dealt with. Fatigue cracks start at the largest near-surface defect or at the rough as-built surface. Murakami's empirical $\sqrt{\mathrm{area}}$ model relates the fatigue limit to hardness and the square root of the defect's projected area normal to the stress:

$$
\sigma_w=\frac{C\,(\mathrm{HV}+120)}{\left(\sqrt{\mathrm{area}}\right)^{1/6}}
$$

with $\sigma_w$ in MPa, HV the Vickers hardness, $\sqrt{\mathrm{area}}$ in µm, and $C=1.43$ for surface defects and 1.56 for internal ones.

> **Status of the principle: Murakami's $\sqrt{\mathrm{area}}$ model**
> *Empirical.* Fitted to steels with small defects and inclusions; it treats a defect as an equivalent small crack whose threshold for growth depends on its size and the matrix hardness. It is widely used for ranking AM defects in titanium and nickel alloys, but its constants are not universal and it applies to defects small enough to behave as short cracks (roughly below 1000 µm).

**Worked example — How much does a lack-of-fusion pore cost?** For as-built Ti–6Al–4V of about 350 HV, a surface-connected LOF defect with $\sqrt{\mathrm{area}}=100$ µm gives

$$
\sigma_w=\frac{1.43\times(350+120)}{100^{1/6}}=\frac{672}{2.15}=312\ \mathrm{MPa}
$$

If HIP closes the internal defects and machining removes the surface layer so that the largest remaining defect is an internal gas pore of $\sqrt{\mathrm{area}}=30$ µm,

$$
\sigma_w=\frac{1.56\times470}{30^{1/6}}=\frac{733}{1.76}=416\ \mathrm{MPa}
$$

and for a 10 µm pore, about 500 MPa. These estimates bracket what is observed: fatigue strengths at 10$^7$ cycles of about 200–350 MPa for as-built PBF Ti–6Al–4V with as-built surfaces, against 500–600 MPa for HIPed and machined material — comparable to wrought. A defect only a tenth of a millimetre across is enough to cut the fatigue limit by a third; this is why AM qualification focuses on the size of the largest defect, not on the average density.

---

## 40.5 Post-processing

Almost no metal AM part goes into service as built. A typical sequence for a PBF-LB aerospace or medical part is:

1. **Stress relief** on the build plate (for example 650–800 °C for Ti–6Al–4V, 300 °C for AlSi10Mg, 1065 °C for IN718 in some routes) to prevent distortion and cracking on removal.
2. **Removal** from the plate by wire electrical-discharge machining or band saw, and **support removal**.
3. **Hot isostatic pressing** to close internal porosity: typically 920 °C, 100 MPa, 2 h for Ti–6Al–4V; around 1160–1200 °C and 100–150 MPa for nickel superalloys. HIP closes LOF and keyhole pores that are not connected to the surface, but not surface-connected ones, and not argon-filled gas pores, which can reappear on subsequent heat treatment. It also coarsens the microstructure: α′ martensite in Ti–6Al–4V decomposes to a lamellar α+β structure, trading strength for ductility.
4. **Heat treatment** to the required condition: solution and age for IN718 and 17-4PH, which also dissolves the Laves and δ phases that segregation creates; annealing to recrystallize and homogenize the cellular structure of 316L if corrosion or isotropy demands it; T6 for AlSi10Mg (which, unlike the cast alloy, loses strength because the fine as-built silicon network coarsens).
5. **Machining** of critical surfaces, threads and interfaces, and **surface finishing** — abrasive blasting, chemical or electrochemical polishing, abrasive-flow machining of internal channels — to remove the rough surface layer and its partly fused particles.
6. **Inspection**: computed tomography for internal defects and geometry, dye penetrant, dimensional checks, and testing of witness coupons built alongside the part.

| Ti–6Al–4V condition | Microstructure | Yield strength (MPa) | Tensile strength (MPa) | Elongation (%) | Fatigue strength at 10⁷ cycles (MPa) |
|---|---|---|---|---|---|
| PBF-LB, as built | α′ martensite in columnar prior β | 1000–1150 | 1100–1300 | 5–10 | 200–350 (as-built surface) |
| PBF-LB, stress relieved | Tempered α′ / fine α+β | 950–1050 | 1050–1150 | 8–12 | 250–400 (as-built surface) |
| PBF-LB, HIP + machined | Lamellar α+β | 850–950 | 950–1050 | 12–16 | 500–600 |
| PBF-EB, as built | Fine α+β (hot bed) | 850–950 | 950–1050 | 12–16 | 250–350 (as-built surface) |
| DED/WAAM, as deposited | Coarse columnar prior β, basketweave α | 800–950 | 900–1000 | 8–15 | — |
| Wrought, mill annealed | Equiaxed α+β | 830–900 | 900–1000 | 12–16 | 500–600 |

*Typical values; fatigue strength depends on stress ratio, surface and defect content.*

The table shows the general pattern: as-built PBF material is stronger and less ductile than wrought, HIP and machining bring it to wrought-equivalent behaviour, and fatigue — governed by surface and defects — is the property most sensitive to post-processing. Figure 40.5 shows the same pattern as S–N curves.

<!-- FIGURE 40.5 | figures/ch40/fig-40-5-ti64-fatigue-postprocessing.png | plot | Fatigue S–N curves of Ti–6Al–4V made by PBF-LB in different post-processing conditions compared with wrought material. | Content: x-axis cycles to failure 10^4–10^8 (log); y-axis maximum stress 100–1000 MPa (R = 0.1). Curves (schematic, typical): as-built surface, as built (endurance ~250 MPa at 10^7); stress relieved, as-built surface (~300 MPa); HIP, as-built surface (~350 MPa, little gain because surface dominates); machined, not HIPed (~450 MPa, internal LOF initiation, large scatter band shaded); HIP + machined (~550 MPa); wrought mill-annealed (~550–600 MPa, dashed). Inset fractograph sketches at right: crack initiation at a surface LOF defect with unmelted particles vs at an internal 30 µm pore vs at α-lath boundaries. Annotations of the worked-example Murakami estimates: 312 MPa (100 µm surface defect) and 416 MPa (30 µm internal pore). -->

---

## 40.6 Polymer and ceramic additive manufacturing

### Polymers

Polymers were the first AM materials and still account for most printed parts by number.

- **Material extrusion** deposits beads of molten thermoplastic: PLA, ABS, PETG, polycarbonate, nylon and high-temperature PEEK and PEI, often filled with chopped or continuous carbon or glass fibre. The weakness is the **interface between beads and layers**: a new bead must reheat the previous one above its glass transition long enough for chains to diffuse across the interface and entangle. The time for this healing scales with the reptation time (Chapter 21), and if the interface cools too quickly only partial interdiffusion occurs. Strength perpendicular to the layers is therefore typically 30–70 % of that along the beads, and parts are oriented so that the main loads run along the beads. Voids between rounded beads add to the anisotropy.
- **Polymer PBF** (laser sintering) holds a bed of PA12 or PA11 powder a few degrees below its melting point, inside the **sintering window** between melting on heating and recrystallization on cooling of the semicrystalline polymer; the laser supplies the last increment of energy to melt and coalesce the scanned particles. Because the whole bed stays above the recrystallization temperature during the build, the part does not curl, and because the surrounding powder supports it, no supports are needed — enabling nested batches of functional ducts, housings and orthotics. Parts are 95–97 % dense with near-isotropic properties close to moulded PA12.
- **Vat photopolymerization** cures acrylate or epoxy resins by UV-initiated radical or cationic polymerization (Chapter 19). Light is absorbed exponentially with depth (Beer–Lambert), and the resin cures where the dose exceeds a critical dose $E_c$. The cured depth follows the **Jacobs working curve**:

$$
C_d=D_p\ln\frac{E}{E_c}
$$

where $E$ is the surface exposure and $D_p$ the depth at which the light falls to $1/e$. Each layer must cure slightly deeper than the layer thickness so that it bonds to the one below.

**Worked example — Choosing the exposure.** A resin has $D_p=0.15$ mm and $E_c=10$ mJ/cm$^2$. For 0.1 mm layers with 50 % overcure, $C_d=0.15$ mm and

$$
E=E_c\exp\!\left(\frac{C_d}{D_p}\right)=10\times e^{1.0}=27\ \mathrm{mJ/cm^2}
$$

A 0.2 mm cure depth needs $10\times e^{1.33}=38$ mJ/cm$^2$: cure depth grows only logarithmically with exposure. A ceramic-filled slurry scatters light strongly and might have $D_p=0.05$ mm; curing 0.075 mm then needs $10\times e^{1.5}=45$ mJ/cm$^2$, and the shallower penetration forces thinner layers. Overexposure enlarges features laterally and over-cures down-facing surfaces, so exposure, layer thickness and resolution are set together.

Polymer parts printed by VPP are post-cured under UV and heat to complete the reaction; incompletely cured resins contain residual monomer, which matters for skin-contact and dental parts.

### Ceramics

Ceramics cannot be melted layer by layer without cracking, so most ceramic AM is **indirect**: shape a powder–binder green body, then debind and sinter it (Chapters 17 and 38).

- **Vat photopolymerization of ceramic slurries** (40–60 vol% alumina, zirconia, silicon nitride or hydroxyapatite in a photocurable resin) gives the best resolution and density, reaching 99 %+ after sintering for alumina and zirconia. Debinding is slow (often days) because the polymer must leave without cracking the part, which limits wall thickness to a few millimetres. Applications include ceramic cores for turbine-blade casting, dental zirconia, and bioceramic bone scaffolds.
- **Binder jetting** of ceramic powders gives porous parts that are infiltrated or used porous (sand moulds and cores for metal casting are its largest application, eliminating patterns entirely).
- **Material extrusion of pastes** ("robocasting") prints ceramic lattices and scaffolds, and on a much larger scale, **3D concrete printing** extrudes stiff cementitious mortar to build walls without formwork. Printable concrete must be fluid enough to pump yet develop a yield stress fast enough to support the layers above it — a rheology problem — and its interlayer bond, like FFF polymers, is a weak plane (Chapter 18).
- **Direct laser melting** of ceramics is limited to special cases (eutectic oxide ceramics, small parts with preheating) because thermal shock cracks them.

Sintering shrinkage of 15–25 % linear must be compensated in the model, and like MIM (Chapter 38), uniform green density is the key to dimensional control.

---

## 40.7 Design for additive manufacturing

Design for AM exploits geometric freedom while respecting what the processes cannot do.

### Process constraints

- **Overhangs and supports.** In metal PBF, surfaces inclined at less than about 40–45° to the build plate need supports, which consume time and powder and must be removed; down-facing surfaces are rough. Designers orient parts and use self-supporting shapes (teardrop or diamond channels instead of circles).
- **Minimum features.** Walls of about 0.3–0.5 mm, holes of about 0.5–1 mm and channels that powder can be removed from; trapped powder in closed cavities is a defect.
- **Thermal mass and distortion.** Large flat areas, abrupt section changes and long scan vectors build residual stress; thin features overheat because heat cannot escape, changing microstructure locally.
- **Build orientation** sets anisotropy, surface quality on critical faces, support needs and build height (and so time and cost).

### Topology optimization and part consolidation

**Topology optimization** distributes material within a design space to minimize compliance or mass for given loads and constraints; the organic, truss-like results are often manufacturable only by AM. Typical aerospace brackets redesigned this way lose 30–60 % of their mass. **Part consolidation** replaces assemblies — the fuel-nozzle example of the opening, heat exchangers with thousands of brazed fins, hydraulic manifolds with drilled cross-holes and plugs — by single parts with internal passages shaped for flow rather than for drilling. Each eliminated joint removes a leak path and a failure mode (Chapter 39), but the consolidated part must be inspectable, and internal surfaces cannot be machined.

### Lattices and architected materials

AM can build **lattices** — periodic or stochastic cellular structures — whose properties follow the scaling laws of cellular solids. For a lattice of relative density $\bar\rho=\rho^*/\rho_s$ made of a solid with modulus $E_s$ and yield strength $\sigma_s$, Gibson–Ashby analysis gives

$$
\frac{E^*}{E_s}\approx\bar\rho^{\,2},\qquad\frac{\sigma^*}{\sigma_s}\approx0.3\,\bar\rho^{\,3/2}
$$

for **bending-dominated** lattices (such as open-cell foams and many strut lattices with low nodal connectivity), and

$$
\frac{E^*}{E_s}\approx\frac{\bar\rho}{3}
$$

for **stretch-dominated** lattices (such as the octet truss), whose struts carry axial load.

> **Status of the principle: Gibson–Ashby scaling of cellular solids**
> *Approximate.* Derived from beam theory for idealized cells, with prefactors fitted to experiment. It holds for relative densities below about 0.3; at higher densities nodes and strut thickness dominate. Printed lattices fall below the predictions when strut diameters approach the melt-track width, because of surface roughness, waviness and porosity in the struts.

**Worked example — A titanium lattice that matches bone.** A femoral stem made of solid Ti–6Al–4V ($E_s=114$ GPa) is about six times stiffer than cortical bone (15–20 GPa); the stiff implant carries load that the bone around it would otherwise carry, and the unloaded bone resorbs (**stress shielding**, Chapter 31). A bending-dominated Ti–6Al–4V lattice at $\bar\rho=0.2$ has

$$
E^*\approx114\times0.2^{2}=4.6\ \mathrm{GPa},\qquad\sigma^*\approx0.3\times950\times0.2^{1.5}=25\ \mathrm{MPa}
$$

between trabecular and cortical bone, and far closer to bone than solid titanium. At $\bar\rho=0.3$ the modulus is 10 GPa and the strength 47 MPa; a stretch-dominated octet lattice at $\bar\rho=0.2$ gives 7.6 GPa. By grading the density through the part, a designer can make an implant that is stiff where it must carry bending and compliant where it meets bone, and whose open pores of 300–700 µm allow bone ingrowth. Figure 40.6 places these lattices against bone on a log–log chart. The same scaling guides lightweight sandwich cores, energy-absorbing crash structures and heat-exchanger lattices.

<!-- FIGURE 40.6 | figures/ch40/fig-40-6-lattice-scaling.png | plot | Relative modulus of printed lattices versus relative density, comparing bending- and stretch-dominated architectures with bone. | Content: log–log axes: x-axis relative density 0.01–1; y-axis modulus E* 0.01–200 GPa for Ti–6Al–4V (E_s = 114 GPa), secondary axis E*/E_s. Lines: bending-dominated E* = E_s ρ̄² (slope 2), stretch-dominated E* = E_s ρ̄/3 (slope 1), meeting near ρ̄ = 1. Points: worked example at ρ̄ = 0.2 (4.6 GPa bending, 7.6 GPa stretch) and ρ̄ = 0.3 (10.3 GPa). Shaded horizontal bands: trabecular bone 0.1–2 GPa, cortical bone 15–20 GPa. Scatter of typical measured PBF lattice data lying slightly below the bending line. Small unit-cell sketches: body-centred cubic strut cell (bending), octet truss (stretch), gyroid sheet (intermediate). -->

---

## 40.8 Qualification and certification

A forged aircraft part is trusted because its material comes from a mature specification — a defined alloy, a controlled melting and forging process, and decades of statistical property data. An AM part breaks that model: the material is created at the same moment as the part, by a process with dozens of parameters, on machines whose behaviour can drift, and its properties depend on geometry, orientation and location on the build plate. **Qualification** is the demonstration that a material, process and machine reliably produce parts with the required properties; **certification** is a regulator's or customer's acceptance that a particular part meets requirements for its application.

### The elements of AM qualification

1. **Feedstock control**: powder chemistry (particularly oxygen, nitrogen and hydrogen), size distribution, morphology, flowability and reuse limits; wire chemistry for DED.
2. **A frozen process**: machine, software, parameter set, scan strategy, gas flow, plate preheat and post-processing are fixed and documented; any change triggers requalification. Machine qualification checks laser power, beam focus, recoater and gas-flow performance.
3. **Material property databases**: tensile, fatigue, fracture-toughness and crack-growth data from many builds, machines and powder lots, in several orientations, giving statistically based design allowables (for example values that 99 % or 90 % of the population exceed with 95 % confidence, as for conventional aerospace materials).
4. **Part qualification**: first-article inspection, CT scanning, destructive sectioning of sample parts, proof testing.
5. **Production control**: **witness coupons** built with each lot and tested; **in-situ monitoring** of melt-pool emission, layer images and thermal fields, which can detect recoater streaks, spatter and LOF as they occur and is increasingly used to flag parts for extra inspection; and statistical process control.
6. **Defect-tolerant design**: since the largest defect governs fatigue, designs use damage-tolerance analysis with an assumed initial flaw size set by what inspection can reliably find, and **classify parts by criticality**, from non-structural parts that need little qualification to fracture-critical parts that need the most.

Standards organizations (ISO/ASTM, SAE's Aerospace Material Specifications, ASME, NASA, and medical-device regulators) have published AM-specific standards covering terminology, feedstock, process control, testing and inspection, and the number grows each year. In medicine, porous printed titanium acetabular cups and spinal cages have been cleared for routine clinical use, with patient-specific implants and surgical guides regulated as custom devices.

### Why qualification is hard, and how it is getting easier

The fundamental difficulty is that AM properties are path-dependent at fine scale. A change in part geometry changes local heat accumulation, which changes melt-pool size, cooling rate, porosity and microstructure. Two approaches reduce the cost of proving each new part: **process–structure–property models** (melt-pool, solidification and microstructure simulations linked to property models in an ICME framework, Chapter 46) that predict where in a part defects and weak microstructures will occur, and **in-situ monitoring plus closed-loop control**, which aims to certify the part by its own build record rather than by sacrificial testing. Neither yet replaces testing for critical parts, but together they are moving AM from "qualify every part" toward "qualify the process".

| Concern | Root cause | Control | Verification |
|---|---|---|---|
| Lack of fusion | Low energy, poor overlap, spatter, recoating faults | Parameter window, gas flow, powder quality | CT, density cubes, in-situ layer imaging |
| Keyhole porosity | Excess energy, scan turnarounds | Parameter window, scan-strategy design | CT, metallography |
| Residual stress and distortion | Thermal gradients | Plate preheat, scan strategy, supports, stress relief | Dimensional inspection, diffraction |
| Cracking | Alloy freezing range, hardenability | Alloy design, inoculants, preheat | CT, penetrant, metallography |
| Anisotropy | Columnar grains, texture, oriented defects | Orientation choice, HIP, heat treatment | Tests in several orientations |
| Surface-initiated fatigue | Roughness, partly fused particles | Machining, polishing | Surface metrology, fatigue coupons |
| Powder degradation | Oxygen pick-up, spatter in reused powder | Reuse limits, sieving, lot testing | Chemistry and size analysis |

---

## What remains open

| Open question | Where it is answered |
|---|---|
| What sets dendrite spacing, CET and segregation during rapid solidification? | Chapter 9 |
| How do martensite, precipitation and recrystallization respond to AM thermal cycles and post-build heat treatment? | Chapter 10 |
| How do defects and surfaces control fatigue and fracture? | Chapter 14 |
| How are Ti, Ni and Al alloys designed and processed conventionally for comparison? | Chapter 16 |
| How are ceramic powders sintered, and polymers processed and degraded? | Chapters 17 and 21 |
| How do printed implants interact with bone, and what is stress shielding? | Chapter 31 |
| How are AM parts used in high-temperature and aerospace service? | Chapter 33 |
| How is surface roughness modified by finishing and coating? | Chapters 37 and 41 |
| How are porosity, texture and residual stress measured (CT, EBSD, synchrotron and neutron methods)? | Chapters 42–43 |
| How do in-situ X-ray imaging and melt-pool monitoring reveal defect formation? | Chapter 44 |
| How are melt pools, microstructures and properties simulated and linked in ICME? | Chapter 46 |
| How is AM chosen against casting, forging and machining on cost and performance, and what is its environmental footprint? | Chapters 48–49 |

**Next:** Chapter 41 moves from bulk parts to layers — films and coatings from nanometres to millimetres thick — and to the crystal growth and device processing on which electronic materials depend.
