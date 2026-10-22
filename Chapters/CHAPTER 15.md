# Chapter 15 — Physical Metallurgy of Steels and Cast Irons

*Part IV · Metals, Ceramics and Construction Materials*

A gearbox manufacturer receives two batches of the same gear, both machined from bar sold as "0.4 % carbon steel", both carburized and quenched by the same subcontractor. Gears from the first batch run for years. Gears from the second batch shed teeth within weeks: the fracture surfaces show a hard, thin case on a soft core that bent under each tooth load until the case cracked. Chemical analysis shows the difference: the first batch was a Cr–Mo low-alloy steel, the second a plain-carbon steel of nearly the same carbon content. The two steels have the same equilibrium phase diagram, almost the same strength when slowly cooled, and the same price per kilogram within a few percent. What they do not share is **hardenability** — the ability to form martensite deep inside a section during a quench — and that one property decided the life of the gears.

Steel is the most widely used engineering metal, some 1.9 billion tonnes a year — far more than all other metals combined. Its dominance comes not from one outstanding property but from the range of microstructures iron and carbon, with a few percent of other elements, can form: from 200 MPa deep-drawing sheet to 2000 MPa bearing races, from non-magnetic stainless cutlery to transformer cores. Every mechanism of Chapters 7–14 is used somewhere in steel.

> **Why does a single binary system, iron–carbon, produce materials whose strength spans a factor of ten, and how is the microstructure selected by heat treatment and alloying?**
> **What makes a steel hardenable, stainless or formable, and why are cast irons a different family altogether?**

| Concept | Engineering destination |
|---|---|
| Iron allotropy and the Fe–C diagram | Every heat treatment, welding and casting operation on ferrous alloys |
| Ferrite–pearlite microstructures | Structural sections, rails, wire rod, forgings |
| Annealing, normalizing, quenching, tempering | Shafts, gears, springs, fasteners, tools |
| Hardenability, Jominy test, CCT diagrams | Choosing a steel for a section size; quench design |
| HSLA, tool and maraging steels | Pipelines, bridges, dies, rocket cases, landing gear |
| Stainless steels and the Schaeffler diagram | Chemical plant, food processing, implants, welding consumables |
| AHSS: DP, TRIP, TWIP, press hardened | Lightweight car bodies and crash structures |
| Cast irons | Engine blocks, brake discs, pipes, crankshafts, machine bases |
| Surface hardening | Gears, camshafts, bearings, crankshaft journals |

**Roadmap.** Iron and the Fe–C diagram (15.1) → plain-carbon steel microstructures (15.2) → heat treatment (15.3) → hardenability and CCT (15.4) → alloy steels: HSLA, tool, maraging (15.5) → stainless steels (15.6) → advanced high-strength steels (15.7) → cast irons (15.8) → surface hardening (15.9).

---

## 15.1 Iron and its allotropes; the Fe–C diagram revisited

### Three phases of pure iron

Pure iron is **allotropic** (Section 7.2). From room temperature to 912 °C it is body-centred cubic **α-iron (ferrite)**, ferromagnetic below the Curie temperature of 770 °C. Between 912 and 1394 °C it is face-centred cubic **γ-iron (austenite)**. From 1394 °C to the melting point of 1538 °C it is BCC again, **δ-iron**. The α→γ transition, with the close-packed phase stable at *higher* temperature, arises from magnetic and vibrational entropy of BCC iron. It is the most useful fact in ferrous metallurgy: because iron changes structure in the solid state, a steel's microstructure can be reset by heating into austenite and redesigned by the way it is cooled.

### Carbon in iron

Carbon dissolves interstitially. In FCC austenite the octahedral interstices are large (radius about 0.052 nm, compared with 0.077 nm for carbon), and austenite dissolves up to 2.14 wt% C at 1147 °C. In BCC ferrite the interstices are much smaller and distorted (octahedral site about 0.019 nm), so ferrite dissolves at most 0.022 wt% C at 727 °C and less than 0.005 wt% at room temperature. Carbon in excess forms the iron carbide **cementite**, Fe₃C (6.70 wt% C), a hard (about 800–1100 HV), brittle orthorhombic compound. Cementite is metastable: the true equilibrium is with graphite, but in steels the kinetics of graphite formation are so slow that the Fe–Fe₃C diagram is the practical one. In cast irons, with more carbon and silicon, graphite does form (Section 15.8).

<!-- FIGURE 15.1 | figures/ch15/fig-15-1-fe-fe3c-diagram.png | plot | The iron–cementite phase diagram up to 6.70 wt% C, with the steel and cast-iron ranges, critical temperatures A1, A3 and Acm, and heat-treatment temperature windows. | Content: x-axis wt% C 0–6.7 (top axis Fe3C weight fraction), y-axis temperature 400–1600 °C. Phase fields: L, δ, γ, α, α + Fe3C, γ + Fe3C, L + γ, L + Fe3C, δ + γ, L + δ. Invariant points: peritectic 1495 °C at 0.17 % C (δ 0.09, L 0.53); eutectic 1147 °C at 4.30 % C (γ 2.14 %); eutectoid 727 °C at 0.76 % C (α 0.022 %). Lines labelled A1 (727 °C), A3 (from 912 °C at 0 % C to 727 °C at 0.76 %), Acm (from 727 °C at 0.76 % to 1147 °C at 2.14 %). Vertical shaded band 0–2.14 % labelled "steels", 2.14–4.5 % "cast irons". Inset (zoom of 0–1.4 % C, 600–1000 °C): bands for full annealing (A3 + 30–50 °C), normalizing (A3/Acm + 50–80 °C), spheroidizing (just below A1), hardening (A3 + 30–50 °C for hypoeutectoid, A1 + 30–50 °C for hypereutectoid). Mark 0.45 % C vertical (worked example). -->

### The Fe–C diagram for steels

Figure 15.1 shows the iron–cementite diagram, first met in Section 7.7. Its key features, with the conventional names of the critical lines:

| Feature | Composition (wt% C) | Temperature (°C) | Reaction on cooling |
|---|---|---|---|
| Peritectic | 0.17 | 1495 | L + δ → γ |
| Eutectic | 4.30 | 1147 | L → γ (2.14 % C) + Fe₃C (ledeburite) |
| Eutectoid | 0.76 | 727 | γ → α (0.022 % C) + Fe₃C (pearlite) |
| $A_1$ line | — | 727 | Lower critical temperature |
| $A_3$ line | 0 → 0.76 | 912 → 727 | Start of ferrite formation on cooling |
| $A_{cm}$ line | 0.76 → 2.14 | 727 → 1147 | Start of cementite formation on cooling |

Steels contain up to 2.14 % C (in practice rarely above 1.5 %); cast irons contain more. Alloying elements move these lines: **austenite stabilizers** (Ni, Mn, C, N, Cu, Co) lower $A_3$ and expand the γ field; **ferrite stabilizers** (Cr, Si, Mo, W, V, Ti, Al, Nb) raise $A_3$ and contract it. With enough Ni or Mn, austenite is stable at room temperature (austenitic stainless and TWIP steels); with enough Cr or Si, the γ field closes entirely (ferritic stainless and electrical steels). In practice the critical temperatures also depend on heating or cooling rate, written $Ac_1$, $Ac_3$ on heating and $Ar_1$, $Ar_3$ on cooling.

---

## 15.2 Plain-carbon steels: microstructure versus carbon content

### Eutectoid steel and pearlite

A steel with 0.76 % C, cooled slowly from austenite, transforms at 727 °C entirely to **pearlite**: alternating lamellae of ferrite and cementite that nucleate at austenite grain boundaries and grow as colonies by cooperative, diffusion-controlled partitioning of carbon (Section 10.5). The lever rule at just below 727 °C gives the cementite fraction in pearlite as $(0.76-0.022)/(6.70-0.022)=0.11$; the lamellae are therefore about 1:7 in thickness. The interlamellar spacing $S$ decreases as the transformation temperature falls (it scales roughly with the inverse of undercooling), from about 0.5 μm for slow furnace cooling ("coarse pearlite") to 0.1 μm or less for air cooling or isothermal transformation near 550–600 °C ("fine pearlite"). Yield strength follows a Hall–Petch-like relation in $S^{-1/2}$, and fully pearlitic steels reach 600–1200 MPa tensile strength. Cold-drawn fine pearlite — **patented and drawn wire** for bridge cables, pre-stressing strand and tyre cord — reaches 1800–2200 MPa (bridge wire) to over 3500 MPa (tyre cord), because drawing aligns the lamellae and thins them to nanometres.

### Hypoeutectoid and hypereutectoid steels

A steel with less than 0.76 % C (**hypoeutectoid**) crossing $A_3$ on cooling first forms **proeutectoid ferrite**, usually as grain-boundary allotriomorphs and then polygonal grains; the remaining austenite enriches in carbon until it reaches 0.76 % at 727 °C and transforms to pearlite. A steel above 0.76 % C (**hypereutectoid**) first precipitates **proeutectoid cementite** on the austenite grain boundaries below $A_{cm}$, then the remainder becomes pearlite. A continuous grain-boundary cementite network is brittle, which is one reason hypereutectoid tool and bearing steels are given spheroidizing anneals.

**Worked example — Phase fractions in a medium-carbon steel.** A 1045-type steel (0.45 % C) is slowly cooled. Just above 727 °C, the lever rule between ferrite (0.022 % C) and austenite (0.76 % C) gives

$$
f_\alpha^{\mathrm{pro}}=\frac{0.76-0.45}{0.76-0.022}=0.42,\qquad f_{\mathrm{pearlite}}=0.58
$$

Just below 727 °C, the total phase fractions between ferrite and cementite are

$$
f_{\mathrm{Fe_3C}}=\frac{0.45-0.022}{6.70-0.022}=0.064,\qquad f_\alpha^{\mathrm{total}}=0.936
$$

The microstructure is 42 % proeutectoid ferrite and 58 % pearlite by weight, and although only 6.4 % of the steel is cementite, its arrangement as lamellae in more than half the volume roughly doubles the strength of a ferritic steel. For a 1.0 % C hypereutectoid steel, the proeutectoid cementite fraction is $(1.0-0.76)/(6.70-0.76)=0.040$ — only 4 % by weight, but enough to form a continuous film around every prior austenite grain.

### Properties versus carbon content

**Table 15.1 — Plain-carbon steels in the normalized (air-cooled) condition (typical values).**

| Steel (AISI/SAE) | C (wt%) | Microstructure | $\sigma_y$ (MPa) | UTS (MPa) | Elongation (%) | Hardness (HB) | Typical uses |
|---|---|---|---|---|---|---|---|
| 1008 / DC04 | 0.08 | Ferrite, trace pearlite | 180–220 | 300–340 | 35–45 | 90–100 | Car body panels, cans |
| 1020 | 0.20 | Ferrite + ~25 % pearlite | 340–350 | 440–460 | 35 | 130 | Structural sections, carburizing grade |
| 1045 | 0.45 | Ferrite + ~58 % pearlite | 410–430 | 650–690 | 20–25 | 190–200 | Shafts, axles, forgings |
| 1080 | 0.80 | Fully pearlitic | 520–560 | 1000–1050 | 10–12 | 290 | Rails, springs, wire rod |
| 1095 | 0.95 | Pearlite + grain-boundary Fe₃C | 500–550 | 1000–1020 | 9–10 | 290 | Blades, springs, tools |

<!-- FIGURE 15.2 | figures/ch15/fig-15-2-properties-vs-carbon.png | plot | Hardness and strength of plain-carbon steels versus carbon content for pearlitic (normalized), spheroidized, as-quenched martensitic and tempered conditions. | Content: x-axis carbon 0–1.2 wt%; left y-axis hardness HV 0–950 (right axis approximate HRC). Curves: normalized ferrite–pearlite rising from ~100 HV at 0.05 % C to ~300 HV at 0.8 % then flat; spheroidized ~80–200 HV; as-quenched 100 % martensite rising steeply from ~400 HV (≈ 40 HRC) at 0.1 % C to ~650 HV (58 HRC) at 0.4 %, ~800 HV (64 HRC) at 0.6 %, plateau ~850–900 HV (65–66 HRC) above 0.7 % (label "retained austenite limits hardness"); tempered at 600 °C: ~200–330 HV. Secondary panel: tensile strength and elongation of normalized steels vs carbon, matching Table 15.1 (UTS 320 at 0.08 % to 1000 at 0.8 %; elongation 40 % to 10 %). -->

Figure 15.2 summarizes the trend: in the slowly cooled condition each 0.1 % C adds roughly 100 MPa of tensile strength and costs elongation and toughness, raising the Charpy transition by roughly 15–20 °C. Structural and pipeline steels have therefore been driven to ever lower carbon (Section 15.5), with strength restored by grain refinement and microalloying.

---

## 15.3 Heat treatment: annealing, normalizing, quenching, tempering

### The menu of treatments

All conventional steel heat treatments start by heating into the austenite field (or, for some, just below $A_1$) and differ in how the steel is cooled.

- **Full annealing.** Heat to $Ac_3+30$–$50$ °C for hypoeutectoid steels (above $Ac_1$ only, for hypereutectoid), hold to homogenize, and furnace cool. Produces coarse pearlite and ferrite: soft, machinable, stress-free.
- **Process (subcritical) annealing.** Heat cold-worked low-carbon steel to 550–700 °C, below $A_1$, to recrystallize ferrite (Section 10.7) between cold-forming passes in wire drawing and sheet production.
- **Spheroidizing.** Hold just below $A_1$ (or cycle around it) for many hours so cementite lamellae break up and coarsen into spheroids, driven by interfacial energy (Section 10.3). The softest, most formable and machinable condition of medium- and high-carbon steels; standard before cold heading of bolts and machining of bearing rings.
- **Normalizing.** Heat to $Ac_3$ (or $Ac_{cm}$) $+50$–$80$ °C and cool in still air. Refines and homogenizes the grain structure of castings, forgings and hot-rolled plate, giving finer pearlite and finer ferrite grains than annealing, with higher strength and toughness.
- **Stress relieving.** Heat to 550–650 °C, below $A_1$, to reduce residual stresses from welding, machining or cold work without changing the microstructure much; mandatory for thick welded pressure vessels.
- **Hardening (quenching).** Austenitize and cool faster than the critical cooling rate to form **martensite**.
- **Tempering.** Reheat quenched martensite to 150–700 °C to restore toughness.

### Martensite

When austenite is cooled so fast that carbon cannot diffuse out to form ferrite and cementite, it transforms below the **martensite-start temperature** $M_s$ by a diffusionless shear (Section 10.6) into **martensite**, a body-centred tetragonal phase supersaturated with carbon. The tetragonality $c/a\approx1+0.045\,\mathrm{wt\%\,C}$ reflects carbon atoms locked in one set of octahedral sites. The transformation is athermal: the amount formed depends on how far below $M_s$ the steel is cooled, not on time, and is complete only below the **martensite-finish temperature** $M_f$, typically 200–300 °C below $M_s$. In low-carbon steels (below about 0.6 % C) martensite forms as **laths** in packets with a high dislocation density; in high-carbon steels it forms as lenticular **plates** containing fine twins, and $M_f$ falls below room temperature so some **retained austenite** remains.

Martensite is hard because of interstitial solid-solution strengthening by carbon (the strongest solid-solution effect in metallurgy, Section 13.6), a dislocation density of $10^{15}$–$10^{16}$ m⁻², fine lath and block boundaries, and carbon segregation to dislocations. Its hardness depends almost entirely on carbon content (Figure 15.2): about 45–50 HRC at 0.2 % C, 56–58 HRC at 0.4 %, 64–65 HRC at 0.6 %, levelling at 65–66 HRC above about 0.7 %, where retained austenite offsets further gains. Alloying elements barely change martensite hardness; they change how easily it forms (Section 15.4).

$M_s$ falls with nearly every alloying addition. A widely used empirical expression (Andrews, 1965), in wt%, is

$$
M_s\ (^\circ\mathrm{C})=539-423\,\mathrm{C}-30.4\,\mathrm{Mn}-17.7\,\mathrm{Ni}-12.1\,\mathrm{Cr}-7.5\,\mathrm{Mo}
$$

> **Status of the principle: Andrews equation for $M_s$**
> *Empirical.* A linear regression on low-alloy steels, accurate to about ±15–25 °C for C up to about 0.6 % and moderate alloy contents; it fails for high-alloy, high-carbon or high-nitrogen steels, and does not account for austenite grain size or prior deformation.

For 1045 steel (0.45 C, 0.75 Mn), $M_s=539-190-23=326$ °C; for AISI 4340 (0.40 C, 0.70 Mn, 1.8 Ni, 0.80 Cr, 0.25 Mo), $M_s=539-169.2-21.3-31.9-9.7-1.9=305$ °C; for 1080 (0.80 C, 0.75 Mn), 178 °C. With a low $M_s$, the volume expansion of up to about 4 % on forming martensite occurs in steel that is already cold and strong, so residual stresses and **quench cracks** become likely; high-carbon steels and parts with sharp section changes are oil- or polymer-quenched, or **martempered** (quenched into a salt bath just above $M_s$, equalized, then air cooled).

### Tempering

As-quenched martensite is too brittle for most uses. **Tempering** reheats it so carbon can leave solution in controlled stages:

| Stage | Temperature (°C) | Process | Effect |
|---|---|---|---|
| 1 | 80–200 | Carbon clusters; transition carbides (ε, η) precipitate | Slight hardness loss, large toughness gain; stress relief |
| 2 | 200–300 | Retained austenite decomposes to bainite-like ferrite + carbide | Dimensional change; can embrittle |
| 3 | 250–400 | Cementite replaces transition carbides, often as films on lath boundaries | Toughness can drop (tempered-martensite embrittlement, ~250–400 °C) |
| 4 | > 500 | Cementite spheroidizes and coarsens; ferrite recovers and recrystallizes; alloy carbides (Mo₂C, VC, Cr₇C₃) precipitate in alloy steels | Large softening; in Mo, V, W steels, **secondary hardening** at 500–600 °C |

Two embrittlement windows must be avoided. **Tempered-martensite embrittlement** (about 250–400 °C) comes from interlath cementite films. **Temper embrittlement** occurs when low-alloy steels are held at or slowly cooled through 375–575 °C: P, Sn, Sb and As segregate to prior austenite grain boundaries and can raise the DBTT by 100 °C or more (Section 14.7) — a long-term hazard in thick Cr–Mo reactors and turbine rotors, controlled by limiting impurities and adding Mo.

Because tempering is thermally activated, time and temperature trade against each other. The **Hollomon–Jaffe tempering parameter**

$$
P=T\,(C+\log_{10}t)
$$

with $T$ in kelvin, $t$ in hours and $C\approx21.3-5.8\times\mathrm{wt\%\,C}$ (about 19 for a 0.4 % C steel), collapses hardness data from different tempering schedules onto one curve — the same idea as the Larson–Miller parameter of Section 14.2.

> **Status of the principle: Hollomon–Jaffe tempering parameter**
> *Empirical.* Assumes a single activation energy for softening; good for plain-carbon and low-alloy steels over moderate time ranges, less reliable where secondary hardening or several precipitation reactions overlap.

**Worked example — Equivalent tempering schedules.** A 0.4 % C Cr–Mo shaft is specified as "temper 1 h at 600 °C". The heat-treatment shop wants to know the equivalent time at 550 °C (to reduce distortion) and at 650 °C (to shorten the cycle). With $C=19$:

$P=873.15\times(19+\log_{10}1)=16\,590$.

At 550 °C (823.15 K): $\log_{10}t=16\,590/823.15-19=1.154$, so $t=14.3$ h.

At 650 °C (923.15 K): $\log_{10}t=16\,590/923.15-19=-1.029$, so $t=0.094$ h $=5.6$ min.

A 50 °C change is worth more than an order of magnitude in time. But 5.6 min is shorter than a large shaft takes to heat through, and a 14 h hold at 550 °C sits in the temper-embrittlement window, so 600 °C/1 h is the sensible compromise.

### Quenched-and-tempered properties

**Table 15.2 — Mechanical properties of quenched-and-tempered steels (oil quenched, small sections, typical).**

| Steel | Tempering temperature (°C) | $\sigma_y$ (MPa) | UTS (MPa) | Elongation (%) | Hardness | Uses |
|---|---|---|---|---|---|---|
| 1045 (water quenched) | 540 | 520–620 | 750–830 | 18–22 | 220–240 HB | Shafts, pins |
| 4140 | 205 | 1640 | 1770 | 8 | ~50 HRC | Tool holders |
| 4140 | 540 | 900–1000 | 1000–1100 | 15–18 | ~32 HRC | Crankshafts, gears, bolts (grade 10.9) |
| 4340 | 205 | 1590–1680 | 1860–1980 | 10–11 | ~53 HRC | Landing gear (often 300M variant) |
| 4340 | 650 | 860–900 | 960–1000 | 19–20 | ~28 HRC | Heavy shafts, pressure-vessel bolting |
| 52100 bearing steel | 175 | ~1900 | 2200+ | <5 | 60–64 HRC | Rolling bearings |

---

## 15.4 Hardenability: the Jominy test, alloying effects and CCT diagrams

### Hardness versus hardenability

**Hardness** — the maximum martensite can reach — depends on carbon. **Hardenability** — how deep martensite forms in a quench — depends on how slowly austenite transforms to ferrite, pearlite and bainite, which alloying and austenite grain size control. The centre of a thick part cools only as fast as conduction allows (cooling time scales with the square of section size, Chapter 24); if that is slower than the steel's critical cooling rate, the centre forms pearlite or bainite and stays soft. This is what happened to the second batch of gears.

### Continuous-cooling transformation diagrams

Isothermal TTT diagrams (Section 10.9) describe transformation at constant temperature; real quenches are continuous. **Continuous-cooling transformation** (CCT) diagrams plot the start and finish of each transformation along cooling curves of different rates (Figure 15.3). Compared with the TTT diagram for the same steel, the CCT curves are displaced to longer times and lower temperatures. The **critical cooling rate** is the slowest rate that misses the ferrite, pearlite and bainite noses entirely and forms only martensite.

<!-- FIGURE 15.3 | figures/ch15/fig-15-3-cct-diagrams.png | plot | Continuous-cooling transformation diagrams for a plain-carbon 1045 steel and a Cr–Mo 4140 steel, with cooling curves for the surface and centre of a 50 mm bar quenched in oil. | Content: two panels side by side, x-axis time 0.1–10^5 s (log), y-axis temperature 100–900 °C. 1045 panel: Ac3 ~780 °C, Ac1 ~725 °C; ferrite start nose at ~1 s, pearlite nose ~2 s at ~550–600 °C, small bainite region; Ms 326 °C (dashed horizontal, worked example), M50 and M90 below. 4140 panel: ferrite/pearlite nose shifted to ~100 s at 650 °C, separate bainite bay at 400–550 °C starting at ~10 s; Ms 330 °C. Overlaid cooling curves (same on both panels): "surface, oil" reaching 400 °C in ~5 s; "centre of 50 mm bar, oil" reaching 400 °C in ~60 s. Label resulting microstructures at curve ends: 1045 surface "martensite + some bainite", 1045 centre "ferrite + pearlite (~20 HRC)"; 4140 surface "martensite", 4140 centre "martensite + bainite (~45 HRC)". -->

### The Jominy end-quench test

The **Jominy test** (ASTM A255, ISO 642) austenitizes a bar 25 mm in diameter and 100 mm long and quenches one end with a standard water jet, so the cooling rate falls from several hundred °C/s at the end to about 3 °C/s at 50 mm. Hardness measured along the bar gives the **Jominy curve** (Figure 15.4). Since each Jominy distance corresponds to a known cooling rate, and the surface, mid-radius and centre of quenched bars are tabulated against equivalent Jominy distances, the curve predicts the hardness profile of a real component.

<!-- FIGURE 15.4 | figures/ch15/fig-15-4-jominy-curves.png | plot | Jominy end-quench hardenability curves for 1040, 4140 and 4340 steels, with the cooling rate at each distance. | Content: x-axis distance from quenched end 0–50 mm (top axis cooling rate at 700 °C: ~300 °C/s at 1.5 mm, ~70 at 5 mm, ~30 at 10 mm, ~10 at 20 mm, ~5 at 30 mm, ~3 at 50 mm); y-axis hardness 20–60 HRC. 1040: ~55 HRC at end, falling to ~30 HRC by 6 mm and ~22 HRC by 20 mm. 4140: ~56 HRC at end, ~53 at 10 mm, ~45 at 20 mm, ~38 at 40 mm. 4340: ~55 at end, nearly flat, ~52 at 30 mm, ~50 at 50 mm. Horizontal dashed line at 50 % martensite hardness for 0.4 % C (~43 HRC). Label ideal critical diameters from worked example: 1040 ~22 mm, 4140 ~120 mm, 4340 ~170 mm. -->

### Alloying effects

Almost every element dissolved in austenite slows the diffusional transformations. Mn, Cr and Mo are the most effective per unit cost; Ni is weaker but adds toughness; and 10–30 ppm of boron, segregated to austenite grain boundaries, suppresses ferrite nucleation and multiplies the hardenability of low-carbon steels two- to threefold — the basis of press-hardening steels (Section 15.7) and cheap high-strength fasteners. Mo and Cr shift the pearlite nose more than the bainite nose, producing the separate "bainite bay" of Figure 15.3.

The **ideal critical diameter** $D_I$ — the largest bar that would harden to 50 % martensite at its centre under an infinitely severe quench — is estimated from composition by Grossmann's multiplying factors:

$$
D_I=D_{I,\mathrm{base}}(\mathrm C,\ \text{grain size})\times f_{\mathrm{Mn}}\times f_{\mathrm{Si}}\times f_{\mathrm{Cr}}\times f_{\mathrm{Ni}}\times f_{\mathrm{Mo}}\times\cdots
$$

with approximate factors (ASTM A255, for moderate contents) $f_{\mathrm{Mn}}=1+3.33\,\mathrm{Mn}$, $f_{\mathrm{Si}}=1+0.7\,\mathrm{Si}$, $f_{\mathrm{Cr}}=1+2.16\,\mathrm{Cr}$, $f_{\mathrm{Ni}}=1+0.363\,\mathrm{Ni}$, $f_{\mathrm{Mo}}=1+3.0\,\mathrm{Mo}$ (wt%).

> **Status of the principle: Grossmann multiplying factors**
> *Empirical.* The multiplicative form assumes independent, non-interacting effects of each element; it is useful for ranking and specification within the composition ranges of the data (low-alloy steels), with typical errors of 10–20 % in $D_I$, and is superseded by computed CCT diagrams and Jominy curves for alloy design.

**Worked example — Why the 4140 gears hardened and the 1040 gears did not.** Take a base $D_I$ of 0.213 in (5.4 mm) for 0.40 % C at ASTM grain size 7.

1040 (0.75 Mn, 0.25 Si): $D_I=0.213\times(1+3.33\times0.75)\times(1+0.7\times0.25)=0.213\times3.50\times1.175=0.88$ in, about 22 mm.

4140 (0.88 Mn, 0.25 Si, 0.95 Cr, 0.20 Mo): $D_I=0.213\times3.93\times1.175\times3.05\times1.60=4.8$ in, about 122 mm.

4340 (0.70 Mn, 0.25 Si, 0.80 Cr, 1.80 Ni, 0.25 Mo): $D_I=0.213\times3.33\times1.175\times2.73\times1.65\times1.75=6.6$ in, about 167 mm.

Real quenches are not infinitely severe: a well-agitated oil quench hardens a bar about one-third to one-half of $D_I$ through. A 40 mm gear blank in 1040 therefore cannot form martensite at its core in oil and barely does so even in water, while 4140 hardens it comfortably, and 4340 is used for landing gear and large crankshafts whose sections reach 100 mm or more. The equal carbon contents give equal surface hardness after quenching; the alloy content is paid for in depth. Weldability goes the other way: the IIW carbon equivalent $\mathrm{CE}=\mathrm C+\mathrm{Mn}/6+(\mathrm{Cr}+\mathrm{Mo}+\mathrm V)/5+(\mathrm{Ni}+\mathrm{Cu})/15$ is 0.78 for 4140 against 0.41 for a C–Mn structural steel, and steels above about 0.45 need preheat to avoid hydrogen cracking in the hardened HAZ (Chapter 39).

---

## 15.5 Alloy steels: HSLA, tool steels, maraging steels

### High-strength low-alloy (HSLA) steels

For structural plate, line pipe, ship hulls, offshore platforms, cranes and truck chassis, the requirements are yield strengths of 350–700 MPa, good toughness at low temperature and easy field welding. Raising carbon is excluded by weldability and toughness (Section 15.2). The solution, developed from the 1960s, is **microalloying** with 0.01–0.10 % of Nb, V or Ti combined with **thermomechanically controlled processing** (TMCP). Slabs are reheated to dissolve the carbonitrides; rolled at high temperature, where austenite recrystallizes and TiN pins its grains; finished below the recrystallization-stop temperature (raised by Nb), giving "pancaked" austenite full of ferrite nucleation sites; and cooled rapidly to very fine ferrite (3–6 μm) or acicular ferrite/bainite, while V and Nb precipitate as nanometre carbonitrides. As the X70 example of Section 13.10 showed, most of the strength comes from grain refinement, with carbon at only 0.04–0.10 %. Pipeline grades now reach X80 (555 MPa minimum yield) and X100–X120 in trials; bridge and offshore steels reach 460–690 MPa with Charpy guarantees at −40 °C or lower. **Weathering steels** (Cu, Cr, Ni, P additions) form a protective rust layer and are used unpainted for bridges.

### Tool steels

Tool steels must cut, form or shape other materials. They combine high carbon (0.5–2.3 %) for hard martensite with carbide-forming elements (Cr, W, Mo, V) that form hard primary and secondary carbides and that resist softening when the tool gets hot.

**Table 15.3 — Tool steel classes (AISI designation, typical).**

| Class | Example | Key composition (wt%) | Hardness (HRC) | Characteristic | Uses |
|---|---|---|---|---|---|
| W — water hardening | W1 | 0.6–1.4 C | 58–65 | Cheap, shallow hardening | Simple punches, hand tools |
| O — oil hardening | O1 | 0.9 C, 1.2 Mn, 0.5 Cr, 0.5 W | 57–62 | Low distortion | Gauges, short-run dies |
| A — air hardening | A2 | 1.0 C, 5 Cr, 1 Mo | 57–62 | Deep hardening, stable | Blanking dies, forming rolls |
| D — high C, high Cr | D2 | 1.5 C, 12 Cr, 1 Mo, 1 V | 58–62 | Abrasion resistant (Cr₇C₃) | Long-run stamping and slitting tools |
| S — shock resisting | S7 | 0.5 C, 3.25 Cr, 1.4 Mo | 54–58 | Tough | Chisels, punches under impact |
| H — hot work | H13 | 0.4 C, 5 Cr, 1.3 Mo, 1 V | 44–52 | Resists thermal fatigue and softening to ~600 °C | Die-casting dies, forging dies, extrusion tooling |
| M — Mo high-speed | M2 | 0.85 C, 4 Cr, 6 W, 5 Mo, 2 V | 62–65 | Secondary hardening; red hardness | Drills, taps, end mills |

High-speed and hot-work steels rely on **secondary hardening**: austenitized near 1200 °C (M2) to dissolve alloy carbides, quenched, and tempered two or three times at 540–580 °C, when fine Mo₂C, W₂C and VC precipitate and *raise* hardness above the as-quenched value. These carbides resist coarsening at the 500–600 °C of a cutting edge — the "red hardness" that let Taylor and White quadruple machining speeds around 1900. Powder-metallurgy tool steels (Chapter 38) avoid coarse eutectic carbides and are much tougher.

### Maraging steels

**Maraging** steels ("martensite + ageing") take a different route to ultra-high strength. They contain almost no carbon (below 0.03 %), 18 % Ni, 8–12 % Co, 3–5 % Mo and 0.2–1.6 % Ti. On cooling from about 820 °C, even slowly, the high-Ni austenite transforms to a soft, tough, low-carbon **lath martensite** (about 30 HRC, 800 MPa yield) that can be machined. Ageing at 480–500 °C for 3–6 h then precipitates a dense dispersion of nanometre intermetallics (Ni₃Mo, Ni₃Ti, Fe₂Mo) in the dislocated martensite, raising the yield strength to 1400 MPa (grade 200), 1700 MPa (grade 250), 2000 MPa (grade 300) or 2400 MPa (grade 350). Cobalt lowers Mo solubility and promotes finer precipitation. Ageing involves no quench and a dimensional change of only about 0.05 %, so parts are finish-machined first. Maraging steels serve in rocket-motor cases, arrestor hooks, high-performance shafts and additively manufactured mould inserts (Chapter 40), wherever 2 GPa with good toughness justifies the Ni and Co cost.

---

## 15.6 Stainless steels

### Passivity from chromium

Iron rusts because its oxide film is porous and non-protective. When chromium in solid solution exceeds about 10.5–12 wt%, the surface forms a continuous, self-healing **passive film** of chromium-rich oxide only 1–3 nm thick, which reduces the corrosion rate in many environments by a factor of 1000 or more (Chapter 34). Steels with at least 10.5 % Cr are **stainless**. Corrosion resistance rises with Cr, and in chloride environments with Mo and N; the **pitting-resistance equivalent number**

$$
\mathrm{PREN}=\mathrm{Cr}+3.3\,\mathrm{Mo}+16\,\mathrm N
$$

ranks alloys for seawater and chloride service (304: about 18–19; 316: about 24; duplex 2205: about 35; super-duplex 2507: about 42; PREN above 40 is generally required for seawater at ambient temperature).

> **Status of the principle: Pitting-resistance equivalent number**
> *Empirical.* A linear ranking fitted to critical pitting temperatures; it ignores microstructure (ferrite–austenite partitioning in duplex grades, inclusions, sigma phase) and surface condition, so it ranks alloys but does not predict pitting.

### The four families

Because Cr is a ferrite stabilizer and Ni, Mn, C and N are austenite stabilizers, the balance between them selects the microstructure:

- **Ferritic** (409, 430, 444): 11–30 % Cr, little Ni, low C; BCC, magnetic, not hardenable. Cheap and immune to chloride stress-corrosion cracking, but with a DBTT and limited weldability. Exhausts (409), appliances (430), hot-water tanks (444).
- **Austenitic** (304, 316, 321, 310): 16–26 % Cr, 8–22 % Ni (Mn and N in the 200 series); FCC, non-magnetic, no DBTT (used to −269 °C), highly formable and weldable, strongly work-hardening. More than half of all stainless: food and pharmaceutical plant, sinks, cryogenic vessels, 316L implants and instruments. Weaknesses: chloride stress-corrosion cracking above about 60 °C, and **sensitization**, in which Cr₂₃C₆ precipitates on grain boundaries at 500–800 °C (weld HAZs) and depletes adjacent Cr below the passivity limit; low carbon (304L, 316L, ≤0.03 % C) or Ti/Nb stabilization (321, 347) prevents it.
- **Martensitic** (410, 420, 440C): 12–18 % Cr with 0.1–1.2 % C, quench-hardenable to 50–60 HRC, with modest corrosion resistance. Cutlery, surgical blades, steam-turbine blades, bearings (440C). The **precipitation-hardening** 17-4PH (17 Cr, 4 Ni, 4 Cu) adds Cu-rich precipitates to low-carbon martensite (1000–1300 MPa) for shafts and aerospace fittings.
- **Duplex** (2205, 2507): 22–25 % Cr, 5–7 % Ni, 3–4 % Mo, 0.15–0.3 % N, about half ferrite and half austenite. Twice the yield strength of 316, better stress-corrosion resistance, high PREN; offshore piping, desalination, chemical tankers. Sigma phase (600–950 °C) and "475 °C embrittlement" limit service to below about 250–300 °C and require controlled welding heat input.

### The Schaeffler diagram

The phases present in stainless steel welds, which solidify and cool too fast for equilibrium, are predicted from composition by the **Schaeffler diagram** (Figure 15.5). Each element's effect is converted into an equivalent amount of chromium (ferrite stabilizers) or nickel (austenite stabilizers):

$$
\mathrm{Cr_{eq}}=\mathrm{Cr}+\mathrm{Mo}+1.5\,\mathrm{Si}+0.5\,\mathrm{Nb},\qquad \mathrm{Ni_{eq}}=\mathrm{Ni}+30\,\mathrm C+0.5\,\mathrm{Mn}
$$

The diagram then shows fields of austenite (A), ferrite (F), martensite (M) and their mixtures, with lines of constant ferrite percentage in the A + F field. Later refinements — the DeLong diagram (adding $30\,\mathrm N$ to $\mathrm{Ni_{eq}}$) and the WRC-1992 diagram (ferrite number, Cu term) — are more accurate for modern nitrogen-bearing grades.

> **Status of the principle: Schaeffler constitution diagram**
> *Empirical.* Built from measured weld-metal microstructures at typical arc-welding cooling rates; it predicts ferrite content to about ±4 % in the austenitic range but is not an equilibrium diagram and fails for very fast (laser, electron beam) or very slow cooling and for high-nitrogen alloys.

<!-- FIGURE 15.5 | figures/ch15/fig-15-5-schaeffler.png | map | Schaeffler diagram for stainless steel weld metal: phase fields of austenite, ferrite and martensite as functions of chromium and nickel equivalents, with common grades plotted. | Content: x-axis Cr_eq = Cr + Mo + 1.5Si + 0.5Nb, 0–40 %; y-axis Ni_eq = Ni + 30C + 0.5Mn, 0–32 %. Fields: A (upper left/upper), M (lower left), F (lower right), A+M, A+F (with iso-ferrite lines 0, 5, 10, 20, 40, 80, 100 % F), M+F, A+M+F. Plot points: 304 (Cr_eq 19.3, Ni_eq 11.3, ~5 % ferrite, worked example), 316L (19.9, 12.4), 2205 duplex (25.9, 6.9, ~50 % F), 430 (17, ~1, F+M region), 410 (12.5, ~3, M), mild-steel filler (~1, ~1.5). Draw a dilution tie-line between a 304 point and a mild-steel point with a 309 filler point (Cr_eq ~24, Ni_eq ~14) to illustrate dissimilar welding. Shade the zones "hot cracking (fully austenitic)", "sigma embrittlement (high ferrite)", "martensite cracking", "grain growth (ferritic)". -->

**Worked example — Ferrite in a 304 weld, and why 309 joins stainless to carbon steel.** A 304 weld metal with 18.5 Cr, 9.0 Ni, 0.05 C, 1.5 Mn and 0.5 Si (wt%) has

$$
\mathrm{Cr_{eq}}=18.5+1.5\times0.5=19.25,\qquad \mathrm{Ni_{eq}}=9.0+30\times0.05+0.5\times1.5=11.25
$$

This point lies in the A + F field with about 3–8 % ferrite. That small amount of δ-ferrite is wanted: it solidifies first, dissolves sulfur and phosphorus that would otherwise segregate to austenite grain boundaries, and prevents **solidification (hot) cracking**. Fully austenitic welds (Ni-rich, as in 310 or high-Ni alloys) are hot-crack sensitive; welds with too much ferrite embrittle by sigma formation at temperature.

Joining 304 to carbon steel with a 304 filler would dilute the weld towards the low-alloy corner, crossing into the martensite field and causing cracking. A more highly alloyed **309** filler (about 23 Cr, 13 Ni; $\mathrm{Cr_{eq}}\approx24$, $\mathrm{Ni_{eq}}\approx14$) is chosen so that a typical 30 % dilution by carbon steel still lands the weld in A + F. Selection of dissimilar-metal welding consumables is one of the most frequent everyday uses of the diagram in chemical, power and food-processing plants.

**Table 15.4 — Representative stainless steels (annealed, typical).**

| Grade (UNS) | Family | Composition (wt%) | $\sigma_y$ (MPa) | UTS (MPa) | PREN | Typical use |
|---|---|---|---|---|---|---|
| 409 (S40900) | Ferritic | 11 Cr, Ti | 210–240 | 380–450 | 11 | Exhaust systems |
| 430 (S43000) | Ferritic | 17 Cr | 280–310 | 450–520 | 17 | Appliances, trim |
| 304L (S30403) | Austenitic | 18 Cr, 9 Ni | 210–240 | 520–600 | 18–19 | Food, dairy, tanks |
| 316L (S31603) | Austenitic | 17 Cr, 11 Ni, 2.1 Mo | 220–260 | 520–600 | 24 | Pharma, marine fittings, implants |
| 410 (S41000), Q&T | Martensitic | 12.5 Cr, 0.12 C | 600–1000 | 800–1300 | 12 | Steam-turbine blades, valves |
| 17-4PH (S17400), H900 | PH martensitic | 17 Cr, 4 Ni, 4 Cu | 1170–1270 | 1310–1380 | 17 | Shafts, aerospace fittings |
| 2205 (S32205) | Duplex | 22 Cr, 5.5 Ni, 3.1 Mo, 0.17 N | 450–550 | 650–800 | 35 | Offshore, chemical tankers |
| 2507 (S32750) | Super-duplex | 25 Cr, 7 Ni, 4 Mo, 0.27 N | 550–650 | 800–950 | 42–43 | Seawater systems |

---

## 15.7 Advanced high-strength steels: dual-phase, TRIP, TWIP

### The automotive problem

A car body must be light (fuel economy, electric range), stiff, crashworthy and press-formable at a few seconds per part. Conventional strengthening trades ductility for strength along a "banana curve" (Figure 15.6): mild steel at 300 MPa UTS and 40 % elongation, HSLA at 500 MPa and 25 %, martensitic grades at 1500 MPa and 5 %. **Advanced high-strength steels** (AHSS) use multiphase microstructures or deformation-induced transformations to move above that curve.

<!-- FIGURE 15.6 | figures/ch15/fig-15-6-ahss-banana.png | map | Total elongation versus tensile strength for automotive sheet steels: conventional grades, first-generation AHSS, third-generation AHSS and TWIP/austenitic grades. | Content: x-axis tensile strength 200–2000 MPa; y-axis total elongation 0–70 %. Bubbles: IF (UTS 280–350, El 40–50); mild (300–400, 32–42); bake hardening (350–450, 30–38); HSLA (450–650, 18–28); DP (500–1200, 10–30); TRIP (600–1000, 22–35); complex phase (800–1100, 10–18); martensitic MS (1000–1700, 3–8); press-hardened 22MnB5 (1300–1600, 5–8); third-generation Q&P and medium-Mn (980–1500, 15–30); TWIP (900–1100, 45–65); austenitic stainless 301 (700–1300, 30–60). Dashed "banana" envelope for conventional steels and labels "1st generation", "3rd generation", "2nd generation (high Mn)". -->

### Dual-phase steels

**Dual-phase** (DP) steels are soft ferrite with 10–40 % hard martensite islands, made by intercritical annealing (between $Ac_1$ and $Ac_3$, where carbon-enriched austenite coexists with ferrite) and quenching. The martensite's expansion leaves mobile dislocations in the ferrite, so DP steels show no yield-point elongation, a low yield-to-tensile ratio (0.5–0.65), high early work hardening and strong bake hardening. DP600 and DP800 are the workhorses of body reinforcements, pillars and rails.

### TRIP steels

**Transformation-induced plasticity** (TRIP) steels contain 5–20 % of **retained austenite**, stabilized at room temperature by carbon enrichment to about 1–1.5 %. They are processed by intercritical annealing followed by an isothermal hold at 350–450 °C, where bainite forms and rejects carbon into the remaining austenite; 1.5 % Si or Al suppresses cementite precipitation so the carbon stays in the austenite. During forming or a crash the retained austenite transforms progressively to martensite where strain concentrates, raising local hardening there and delaying necking. TRIP steels reach UTS of 600–1000 MPa with 25–35 % elongation. The **third-generation** quenching-and-partitioning (Q&P) and medium-Mn (5–10 % Mn) steels apply the same idea at 1000–1500 MPa. Austenitic stainless steel 301 is a natural TRIP alloy, used for rail-car bodies and springs.

### TWIP steels

**Twinning-induced plasticity** (TWIP) steels are fully austenitic, with 15–30 % Mn, 0.4–0.8 % C and sometimes Al, adjusted so the stacking-fault energy is 20–40 mJ/m² — low enough for mechanical twinning, too high for martensite (Section 13.9). Twins subdivide the grains during straining and shorten the dislocation mean free path, so the hardening rate stays high to large strains: UTS about 1000 MPa with 50–65 % elongation, the best strength–ductility product of any steel sheet. Alloy cost, difficult welding and coating, and delayed hydrogen cracking have kept them to niche parts.

### Press-hardened steels

The highest-strength body parts — A- and B-pillars, roof rails, door intrusion beams — are made from **press-hardening** (hot-stamping) steels, typically 22MnB5 (0.22 C, 1.2 Mn, 0.003 B). Blanks are austenitized at about 900–950 °C, transferred to a water-cooled die, formed while hot and soft, and quenched in the die to fully martensitic parts of about 1500 MPa UTS (or 1900–2000 MPa in newer 34MnB5-type grades) with no springback. Boron provides the hardenability (Section 15.4), and an Al–Si coating prevents scaling during heating. Tailored soft zones absorb crash energy next to hard anti-intrusion zones.

**Table 15.5 — Automotive sheet steels (typical).**

| Grade | Microstructure | $\sigma_y$ (MPa) | UTS (MPa) | Total elongation (%) | Typical parts |
|---|---|---|---|---|---|
| IF / DC06 | Ferrite, Ti/Nb-stabilized | 120–180 | 270–330 | 40–50 | Outer panels, deep-drawn parts |
| HSLA 340 | Fine ferrite + precipitates | 340–420 | 410–510 | 21–26 | Chassis, cross members |
| DP600 | Ferrite + ~20 % martensite | 340–420 | 600–700 | 20–26 | Rails, reinforcements |
| DP980 | Ferrite + ~50 % martensite | 550–730 | 980–1100 | 10–14 | Seat frames, pillars |
| TRIP780 | Ferrite + bainite + 10–15 % retained γ | 440–550 | 780–900 | 23–28 | Crash members |
| TWIP980 | Austenite, twinning | 550–650 | 980–1100 | 50–60 | Energy-absorbing parts |
| 22MnB5, press hardened | Martensite | 1000–1200 | 1400–1600 | 5–8 | B-pillars, bumper beams |

---

## 15.8 Cast irons: grey, ductile, white, malleable

### Why cast irons are different

Cast irons contain 2.5–4.0 % C and 1–3 % Si, near the eutectic, so they melt at 1150–1250 °C (some 300 °C below steel), flow well, shrink little and are the cheapest metal to cast into shape: engine blocks, brake discs, pump bodies, machine beds, pipe, wind-turbine hubs and crankshafts.

Silicon is the key. It promotes the stable Fe–graphite eutectic over the metastable Fe–Fe₃C eutectic, raising the graphite eutectic temperature relative to the cementite one. Whether an iron solidifies **grey** (graphite) or **white** (cementite) then depends on composition and cooling rate: high C and Si and slow cooling favour graphite; thin sections, fast cooling, and carbide stabilizers (Cr, V, Mo, Mn in excess, S, Te) favour cementite. The effect of composition is summarized by the **carbon equivalent**

$$
\mathrm{CE}=\mathrm C+\frac{\mathrm{Si}+\mathrm P}{3}
$$

with the eutectic at CE ≈ 4.3. A typical grey iron with 3.4 % C, 2.2 % Si and 0.1 % P has CE $=3.4+2.3/3=4.17$, slightly hypoeutectic; a ductile iron with 3.6 % C, 2.5 % Si and 0.05 % P has CE $=4.45$, slightly hypereutectic.

> **Status of the principle: Carbon equivalent of cast iron**
> *Empirical.* Expresses the shift of the eutectic composition by Si and P as a linear correction; useful for predicting eutectic behaviour, fluidity and strength trends within normal composition ranges, but the actual structure also depends on inoculation, section size and trace elements.

The **matrix** around the graphite or carbide is determined by the subsequent solid-state transformation, just as in steel: ferritic, pearlitic, or (after heat treatment) martensitic, bainitic or ausferritic. A cast iron is therefore best thought of as a steel matrix containing graphite particles whose shape decides the properties.

### Grey iron

In **grey** iron the graphite forms interconnected **flakes** that act as internal notches: tensile strength is 150–400 MPa with under 1 % elongation, compressive strength three to four times higher. The flakes also give excellent **damping** (up to ten times that of steel) for machine bases and engine blocks, high **thermal conductivity** (45–55 W/m K) for brake discs, free machining, and near-zero solidification shrinkage, as graphite expansion offsets liquid contraction. Grades are specified by tensile strength (ASTM A48 class 20–60 in ksi; EN-GJL-150 to -350 in MPa). **Inoculation** with ferrosilicon containing Ca, Al or Sr just before pouring provides nuclei for graphite and prevents chill (white) edges in thin sections (Section 9.3).

### Ductile (spheroidal-graphite, nodular) iron

Adding 0.03–0.06 % residual magnesium (or Ce) to a low-sulfur iron makes graphite grow as **spheroids** instead of flakes. Without flake tips the iron is strong and ductile: 400–900 MPa with 18 % (ferritic) down to 2 % (pearlitic) elongation. **Ductile iron**, introduced in 1948, now makes about a third of iron castings: crankshafts, steering knuckles, wind-turbine hubs, water mains and spent-fuel casks. **Austempered ductile iron** (ADI), held at 250–400 °C after austenitizing, forms **ausferrite** (acicular ferrite plus carbon-stabilized austenite) — the same carbon-partitioning principle as TRIP steel — reaching 900–1600 MPa UTS with useful ductility, and replaces forged steel in gears and truck suspension parts at lower weight and cost. **Compacted graphite iron** (CGI), with vermicular graphite intermediate between flakes and spheroids, combines higher strength than grey iron with acceptable conductivity and damping, and is used for high-pressure diesel engine blocks and heads.

### White and malleable iron

In **white** iron all carbon is in carbides: the fracture is white, hardness 400–700 HB, ductility nil. It serves where abrasion matters and impact does not, and **high-chromium white irons** (15–30 % Cr, M₇C₃ carbides in martensite) are the standard for mill liners and slurry pumps. A long anneal at 900–950 °C turns white iron into **malleable** iron, decomposing cementite into clumps of **temper carbon** in a ferritic or pearlitic matrix with 5–18 % elongation. Ductile iron, which needs no long anneal, has largely displaced it.

**Table 15.6 — Cast irons (typical properties).**

| Type | Graphite form | Matrix | UTS (MPa) | Elongation (%) | Hardness (HB) | Uses |
|---|---|---|---|---|---|---|
| Grey EN-GJL-250 | Flakes | Pearlite | 250–350 | < 1 | 180–250 | Engine blocks, brake discs, machine bases |
| Ductile EN-GJS-400-18 | Spheroids | Ferrite | 400–450 | 18–22 | 130–175 | Pipe, wind-turbine hubs, safety parts |
| Ductile EN-GJS-700-2 | Spheroids | Pearlite | 700–800 | 2–3 | 225–305 | Crankshafts, gears |
| ADI (EN-GJS-1050-6) | Spheroids | Ausferrite | 1050–1150 | 6–8 | 320–380 | Gears, suspension parts |
| CGI (EN-GJV-450) | Vermicular | Pearlite | 450–500 | 1–2 | 200–250 | Diesel blocks and heads |
| Malleable (blackheart) | Temper carbon | Ferrite | 300–350 | 6–12 | 110–150 | Pipe fittings, hardware |
| High-Cr white iron | None (M₇C₃ carbides) | Martensite | — | ~0 | 550–700 | Mill liners, slurry pumps |

---

## 15.9 Surface hardening: carburizing, nitriding, induction

### Why harden only the surface

Gears, camshafts, bearing races and crankshaft journals need a hard surface that carries Hertzian contact stresses without pitting, over a tough core that survives impact and bending. Surface hardening produces a hard **case** on a tough **core**, and usually leaves **compressive residual stresses** in the case — from martensite or nitride expansion constrained by the core — that raise bending- and contact-fatigue strength (Section 14.8).

### Carburizing

In **carburizing**, a low-carbon steel (0.1–0.25 % C, often alloyed: 8620, 16MnCr5, 18CrNiMo7-6) is heated in austenite, typically at 900–950 °C, in a carbon-rich atmosphere (endothermic gas, or low-pressure acetylene in vacuum furnaces) that sets the surface carbon at about 0.8–1.0 %. Carbon diffuses inward (Section 8.10), and the part is then quenched so the high-carbon case forms hard martensite (58–62 HRC) while the low-carbon core forms tough low-carbon martensite or bainite (30–45 HRC, depending on hardenability), followed by a low-temperature temper at 150–200 °C. **Carbonitriding** adds ammonia, introducing nitrogen that raises case hardenability, at slightly lower temperature, for thinner cases on cheaper steels.

The case depth follows from the error-function solution of Fick's second law for a constant surface concentration:

$$
\frac{C(x,t)-C_0}{C_s-C_0}=\operatorname{erfc}\!\left(\frac{x}{2\sqrt{Dt}}\right)
$$

**Worked example — Carburizing time for a gear.** A 0.20 % C steel gear is carburized at 925 °C with a surface carbon of 1.0 %. The specification calls for 0.45 % C at a depth of 1.0 mm. Take $D=2.3\times10^{-5}\exp(-148\,000/RT)$ m²/s for carbon in austenite.

At 1198 K: $D=2.3\times10^{-5}\exp(-148\,000/(8.314\times1198))=2.3\times10^{-5}\times e^{-14.86}=8.1\times10^{-12}$ m²/s.

Required error function: $(0.45-0.20)/(1.0-0.20)=0.3125=\operatorname{erfc}(z)$, so $z=0.714$.

$$
t=\frac{1}{D}\left(\frac{x}{2z}\right)^2=\frac{1}{8.1\times10^{-12}}\left(\frac{1.0\times10^{-3}}{2\times0.714}\right)^2=6.0\times10^4\ \mathrm s=16.8\ \mathrm h
$$

Because $x\propto\sqrt t$, halving the case depth to 0.5 mm takes a quarter of the time, 4.2 h; raising the temperature to 950 °C cuts the 1.0 mm cycle to 12.4 h. Carburizing furnace cycles of 4–20 hours for automotive and wind-turbine gears are consistent with this; high-temperature vacuum carburizing at 1000–1050 °C shortens them further, at the cost of grain growth unless the steel is microalloyed with Nb or Al.

### Nitriding and nitrocarburizing

**Nitriding** diffuses nitrogen into a steel at 490–580 °C — in the ferrite field, below $A_1$ — from ammonia gas, plasma or salt baths. No quench is needed and distortion is minimal, so finished, quenched-and-tempered parts can be nitrided. Nitrogen forms a thin surface **compound layer** (5–20 μm of ε-Fe₂₋₃N and γ′-Fe₄N, the "white layer", hard and wear and corrosion resistant) above a **diffusion zone** (0.1–0.7 mm) in which nitrogen precipitates as fine nitrides of Al, Cr, Mo and V. In steels designed for it (Nitralloy 135M with 1 % Al; 31CrMoV9; H13 tool steel) the diffusion zone reaches 900–1200 HV. Nitriding is slow (20–80 h for 0.3–0.5 mm) but gives excellent fatigue strength through compressive stresses; crankshafts, extruder screws, dies and gun barrels are nitrided. **Ferritic nitrocarburizing** (2–4 h at about 570 °C) quickly produces mainly the compound layer, for brake pistons and gas springs.

### Induction, flame and laser hardening

These methods change no chemistry. They heat only the surface layer of a medium-carbon or alloy steel (0.35–0.55 % C, e.g. 1045, 4140) into austenite and quench it, leaving the core in its prior (often quenched-and-tempered) condition. In **induction hardening**, a coil induces eddy currents concentrated within the skin depth $\delta=\sqrt{2\rho/(\omega\mu)}$ — for steel above its Curie point about 1 mm at 200 kHz and 9 mm at 3 kHz, with the hardened case a fraction of this — so frequency selects case depth, and heating takes seconds. It is used in-line for crankshaft journals, axles, gear teeth and rail heads. **Flame hardening** suits large, low-volume parts; **laser** and **electron-beam** hardening give shallow (0.2–1.5 mm), precisely placed, self-quenched cases on cutting edges and valve seats.

**Table 15.7 — Surface hardening processes compared (typical).**

| Process | Temperature (°C) | Case depth (mm) | Surface hardness | Distortion | Typical parts |
|---|---|---|---|---|---|
| Gas carburizing + quench | 900–950 | 0.5–2.5 | 58–62 HRC | Moderate to high | Transmission and wind-turbine gears |
| Carbonitriding | 820–880 | 0.1–0.7 | 58–64 HRC | Moderate | Small gears, fasteners |
| Gas or plasma nitriding | 490–580 | 0.1–0.7 (diffusion zone) | 600–1200 HV | Very low | Crankshafts, dies, extruder screws |
| Ferritic nitrocarburizing | 560–590 | 0.01–0.03 (compound layer) | 500–800 HV | Very low | Brake pistons, gas springs |
| Induction hardening | 850–1000 (surface) | 0.5–6 | 50–60 HRC | Low to moderate | Shafts, journals, rail heads |
| Laser hardening | 900–1200 (surface) | 0.2–1.5 | 55–65 HRC | Very low | Cutting edges, valve seats |

The choice balances case depth (set by the depth of maximum contact shear stress, Chapter 37), distortion, volume and steel cost: a large wind-turbine ring gear is carburized and ground, a car crankshaft induction-hardened or nitrided, an injection mould nitrided after machining — each a solution to the problem this chapter began with: hard where contact demands it, tough everywhere else.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are aluminium, titanium, nickel and copper alloys strengthened and selected, and how do they compare with steel? | Chapter 16 |
| How do structural steel specifications, timber and concrete compare in building and bridge design? | Chapter 18 |
| How do electrical steels and soft magnetic irons achieve low losses? | Chapter 27 |
| How do steels perform under neutron irradiation and at cryogenic temperatures? | Chapter 33 |
| How do stainless steels passivate, and how do they pit, crevice-corrode and crack? | Chapters 34 and 35 |
| How do surface treatments interact with wear, friction and contact fatigue? | Chapter 37 |
| How are steels rolled, forged and cast, and how does thermomechanical processing set texture? | Chapter 38 |
| What happens in the heat-affected zone of a steel weld, and how is cold cracking prevented? | Chapter 39 |
| How do additive manufacturing and rapid solidification change steel microstructures? | Chapter 40 |
| How are CCT diagrams and hardenability computed rather than measured? | Chapter 46 |
| How is steel recycled, and what is its carbon footprint? | Chapter 49 |

**Next:** Chapter 16 turns to the non-ferrous alloys — aluminium, copper, titanium, nickel, magnesium and beyond — where precipitation, solid solution and crystal structure are used to win on lightness, conductivity, corrosion resistance or temperature capability where steel cannot.
