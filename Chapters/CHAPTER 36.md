# Chapter 36 — Degradation and Failure Analysis

*Part VIII · Corrosion, Degradation and Surfaces*

On 3 June 1998 a high-speed train passing Eschede in northern Germany at about 200 km/h derailed and struck a road bridge; 101 people died. The cause was a steel wheel tyre, part of a rubber-sprung wheel design adopted to reduce vibration. Each revolution flexed the tyre; over years of service a fatigue crack grew from its inner surface, helped by the tyre's wear to a thinner section that raised the cyclic stress. The crack grew silently until the remaining ligament broke. No single property of the steel was inadequate on the day the wheel entered service. What failed was the link between a degradation mechanism (fatigue crack growth), its rate under real service loads, and the inspection that should have caught it. This chapter is about that link: how materials of every class lose their properties in service, how the rate of loss is modelled and extrapolated, how failures are statistically distributed, and how an engineer reconstructs a failure from the broken parts to a root cause that can be corrected.

> **By what mechanisms do metals, ceramics, polymers, composites and concrete degrade in service, and what do those mechanisms have in common?**
> **Why do life laws (Paris, Coffin–Manson, Larson–Miller, Arrhenius, square-root ingress) take the forms they do, and how far can they be extrapolated?**
> **How are failures statistically described, and how does an investigation get from fracture surfaces to a root cause?**

| Concept | Engineering destination |
|---|---|
| Driving force, mechanism, rate, end-of-life criterion | A common template for any life prediction |
| Carbonation and chloride ingress, Tuutti model | Concrete cover and durability design of bridges, tunnels, marine structures |
| Slow crack growth, hydrothermal aging of zirconia | Glass panels, ceramic implants, ceramic turbine and armour components |
| Moisture uptake, matrix cracking, delamination | Composite airframes, wind-turbine blades, pressure vessels |
| Thermo-oxidation, photo-oxidation, hydrolysis, stabilizers | Outdoor plastics, pipes, cable insulation, medical polymers |
| Arrhenius extrapolation of oven aging | Thermal ratings and service lives of polymers and adhesives |
| Paris law, Miner's rule, Larson–Miller | Inspection intervals in aircraft, rail, bridges; creep life of boilers and turbines |
| Weibull distribution, bathtub curve, B10 life | Maintenance intervals, warranty, spare-part planning, ceramic design |
| Fractography: dimples, cleavage, striations, beach marks, mirror–mist–hackle | Identifying the failure mechanism from broken parts |
| 5-why, fishbone, fault tree, 8D, FMEA | Turning a failure into a design, material or process change |

**Roadmap.** A common framework (36.1) → degradation in each material class, with concrete as a worked case (36.2) → polymer aging and weathering, with Arrhenius extrapolation (36.3) → wear-out laws and life prediction (36.4) → reliability statistics: Weibull and the bathtub curve (36.5) → failure-analysis methodology, fractography and root cause (36.6) → case studies across industries (36.7).

---

## 36.1 A common framework for degradation

Every degradation process, whatever the material, can be described by the same four questions:

1. **Driving force.** What free energy or mechanical energy is being released? Chemical potential differences drive corrosion and oxidation (Chapter 34); stored elastic energy drives crack growth (Chapter 14); interfacial and grain-boundary energy drive coarsening (Chapter 9); photon energy drives photo-oxidation.
2. **Mechanism and rate-controlling step.** Diffusion, an interfacial reaction, dislocation motion, bond rupture at a crack tip. The slowest step sets the rate, and its dependence on temperature, stress and environment sets the form of the life law.
3. **Damage variable.** What accumulates: crack length, pit depth, carbonation depth, wall loss, oxidized fraction, molecular weight, inelastic strain.
4. **End-of-life criterion.** The damage at which the component no longer performs: crack length at which $K=K_{\rm Ic}$, depth at which rebar depassivates, elongation at break falling to 50 % of its initial value, wall thickness at the pressure-design minimum.

Most life laws then take one of a few mathematical forms:

| Rate-controlling physics | Typical life law | Examples |
|---|---|---|
| Thermally activated reaction | $t\propto\exp(E_a/RT)$ | Polymer oxidation, intermetallic growth, Arrhenius aging |
| Diffusion through a growing layer | $x\propto\sqrt{t}$ | Carbonation of concrete, parabolic oxidation, case depth |
| Cyclic damage accumulation | $N\propto(\Delta\sigma)^{-m}$ or $(\Delta\varepsilon_p)^{-1/c}$ | Basquin, Coffin–Manson, Paris |
| Stress-assisted activated flow | $\dot\varepsilon\propto\sigma^n\exp(-Q/RT)$ | Creep, stress relaxation |
| Sliding contact | $V\propto Fs/H$ | Archard wear (Chapter 37) |
| Weakest-link initiation | Weibull distribution of lives | Ceramic strength, dielectric breakdown, bearing fatigue |

The power of the framework is diagnostic as much as predictive. If accelerated tests at two temperatures fail by different mechanisms, no extrapolation from one to the other is valid. If a failure shows a mechanism the design never considered, the life model was never the problem; the list of mechanisms was.

---

## 36.2 Degradation across material classes

### Metals

Corrosion in all its forms (Chapters 34–35), fatigue, creep (Chapter 14) and wear (Chapter 37) are the dominant mechanisms. Less visible but equally important are **microstructural changes in service**, where the material slowly moves toward equilibrium at its operating temperature:

- **Coarsening of strengthening precipitates**: γ′ in nickel superalloy turbine blades coarsens and rafts under stress, lowering creep strength (Chapter 33); precipitation-hardened aluminium over-ages if run warm.
- **Spheroidization and graphitization** of carbon steel boiler and refinery tubes held for decades near 450–550 °C: lamellar pearlite turns into spheroidal carbides or graphite nodules, lowering strength and creep resistance.
- **Embrittling precipitation**: temper embrittlement of Cr–Mo steels (impurity segregation to grain boundaries around 350–575 °C); 475 °C embrittlement and sigma-phase formation in ferritic and duplex stainless steels; irradiation hardening and embrittlement of reactor-pressure-vessel steels (Chapter 33).
- **Hydrogen and liquid-metal embrittlement** (Chapter 35), and strain aging that raises yield strength and lowers toughness after cold forming.

The common consequence of most embrittling processes is a rise in the ductile–brittle transition temperature (Chapter 14), monitored in nuclear plants by surveillance Charpy specimens irradiated alongside the vessel.

### Ceramics and glasses

Ceramics do not creep or corrode much at ambient temperature, but they are brittle and therefore sensitive to anything that extends existing flaws.

- **Slow crack growth (static fatigue).** Water molecules react with strained Si–O–Si bonds at a crack tip in silicate glass, breaking them at stresses below the fast-fracture value. Crack velocity follows an empirical power law, $v=v_0(K_{\rm I}/K_{\rm Ic})^{n}$, with $n$ about 15–20 for soda-lime glass in water and 30–60 for alumina and silicon nitride. A large $n$ means strength depends weakly on load duration; a small $n$ means a glass panel under permanent load (aquarium, glass floor, façade under snow) must be designed to a stress well below its short-term strength, typically a third to a half.
- **Hydrothermal aging of zirconia.** Yttria-stabilized tetragonal zirconia (3Y-TZP) can transform spontaneously to monoclinic at body or room temperature in the presence of water, starting at the surface and spreading inward with a volume increase that roughens and microcracks it. In 2001 a batch of zirconia femoral heads for hip replacements failed in vivo after a change in the sintering process accelerated this aging; zirconia-toughened alumina composites largely replaced monolithic zirconia for that application.
- **Thermal shock** (Chapter 24), **erosion** by particles, and **chemical attack** of refractories by slags and of glass by alkaline solutions.

### Polymers

Polymers degrade chemically (oxidation, hydrolysis, photolysis), physically (physical aging below $T_g$, plasticizer loss, swelling) and mechanically (creep, crazing, environmental stress cracking). Section 36.3 treats them in detail because their aging is the most strongly temperature- and environment-dependent of all classes.

### Composites

Fibre composites degrade at three length scales (Chapters 22–23):

- **Matrix.** Epoxy matrices absorb 1–6 wt % water at saturation, which plasticizes them and lowers $T_g$, roughly 10–20 °C per percent of absorbed water. The design allowables of aircraft structures are therefore set at "hot/wet" conditions. Ultraviolet light degrades unprotected matrix surfaces, which is why composite surfaces are painted or gel-coated.
- **Interface.** Water and cyclic loading weaken the fibre–matrix bond; glass fibres themselves suffer stress corrosion in water and acids (the reason for corrosion-resistant E-CR glass in chemical pipes).
- **Laminate.** Under fatigue, damage progresses through transverse matrix cracking, then delamination between plies, then fibre breakage. Stiffness falls progressively (often by 10–20 % before final failure) rather than staying constant until a single crack runs, which makes stiffness monitoring useful. Low-velocity impact can create **barely visible impact damage** (BVID), internal delaminations that reduce compressive strength by up to half; design allowables assume such damage is present and undetected.

Wind-turbine blades, where root and spar-cap laminates see about $10^8$–$10^9$ load cycles in a 20–25-year life, are the most demanding fatigue application of composites; leading-edge erosion by rain at tip speeds near 90 m/s is their main surface degradation.

### Concrete

Reinforced concrete degrades mainly through its steel. Concrete pore solution has a pH of about 12.5–13.5, which keeps the rebar passive (Chapter 34). Two processes destroy that passivity:

- **Carbonation**: atmospheric CO$_2$ diffuses in and reacts with calcium hydroxide, lowering the pH to about 9. The carbonation front advances approximately as

$$
x=k\sqrt{t}
$$

because the rate is controlled by diffusion of CO$_2$ through the already carbonated layer. The coefficient $k$ is typically 2–6 mm/year$^{1/2}$ for structural concretes sheltered from rain, lower for dense, low water–cement-ratio concrete and in permanently wet conditions.
- **Chloride ingress** from seawater or de-icing salt, described by Fick's second law with an apparent diffusion coefficient of order $10^{-12}$–$10^{-11}$ m$^2$/s. When the chloride content at the rebar exceeds a critical value, commonly taken as about 0.4 % by mass of cement, the passive film breaks down locally, giving pitting of the rebar.

> **Status of the principle: Square-root-of-time carbonation law**
> *Approximate.* Derived from diffusion through a carbonated layer with a sharp reaction front and constant boundary conditions; real coefficients are fitted to exposure data and vary with moisture, cement type and curing, and the law overestimates penetration where wetting and drying alternate.

Tuutti's model divides the service life of a reinforced-concrete element into an **initiation period**, while the carbonation or chloride front travels through the cover, and a **propagation period**, while the rebar corrodes until cracking, spalling or loss of section reaches an unacceptable level (Figure 36.1). Rust occupies two to six times the volume of the steel it replaces, so only a few tens of micrometres of corrosion are needed to crack the cover.

<!-- FIGURE 36.1 | figures/ch36/fig-36-1-tuutti-concrete-life.png | plot | Tuutti's two-stage service-life model for reinforced concrete, with square-root carbonation fronts for two concretes. | Content: left panel: x-axis time 0–100 years; y-axis carbonation depth 0–50 mm; curves x = k√t for k = 4 and k = 2 mm/yr^0.5; horizontal dashed lines at cover 20 mm and 30 mm; intersections marked at 25 y (k = 4, 20 mm), 56 y (k = 4, 30 mm), 225 y off-scale arrow (k = 2, 30 mm). Right panel: schematic damage (corrosion, cracking) versus time: flat 'initiation' segment until depassivation, then rising 'propagation' line with thresholds 'cracking', 'spalling', 'collapse risk'; CO2 and Cl⁻ labelled as initiation agents, O2 and H2O and temperature as propagation rate factors. -->

**Worked example — cover depth for carbonation.** A bridge pier in a sheltered urban location is made of concrete with a measured carbonation coefficient $k=4$ mm/year$^{1/2}$. How long before the carbonation front reaches the reinforcement for covers of 20 mm and 30 mm, and what does a denser concrete with $k=2$ mm/year$^{1/2}$ achieve?

$$
t=\left(\frac{c}{k}\right)^{2}:\qquad t_{20}=\left(\frac{20}{4}\right)^2=25\ \text{years},\qquad t_{30}=\left(\frac{30}{4}\right)^2=56\ \text{years}
$$

With $k=2$ mm/year$^{1/2}$ and 30 mm cover, $t=(30/2)^2=225$ years. Because time scales with the square of the cover and inversely with the square of $k$, a 50 % increase in cover more than doubles the initiation period, and halving $k$ quadruples it. This is why durability codes (EN 206 and EN 1992, ACI 318) specify both minimum cover and maximum water–cement ratio for each exposure class, and why construction tolerance on cover, often ±10 mm, is a durability parameter: a 30 mm nominal cover placed at 20 mm loses more than half its life.

Other concrete degradation mechanisms are chemical attack of the paste: **sulfate attack** (expansive ettringite and gypsum, resisted by low-C$_3$A cements), **alkali–silica reaction** (reactive silica aggregate swelling as an alkali silicate gel, which has cracked dams and bridges worldwide), **freeze–thaw damage** of saturated paste (resisted by 4–7 % entrained air), and acid and seawater attack (Chapter 18).

---

## 36.3 Polymer aging and weathering

### Thermo-oxidation

Most polymers in service oxidize. The process is a free-radical chain reaction, **autoxidation**:

- Initiation: heat, light, residual catalyst or mechanical stress generates a polymer radical, $\mathrm{RH\to R^{\bullet}}$.
- Propagation: $\mathrm{R^{\bullet}+O_2\to ROO^{\bullet}}$, then $\mathrm{ROO^{\bullet}+RH\to ROOH+R^{\bullet}}$.
- Branching: hydroperoxides decompose, $\mathrm{ROOH\to RO^{\bullet}+{}^{\bullet}OH}$, each producing two new radicals, so the reaction accelerates after an induction period.
- Termination: radicals combine.

The radicals cause **chain scission** (molecular weight falls, polymer becomes brittle: polypropylene, polyethylene) or **cross-linking** (polymer hardens and cracks: many rubbers), and they create carbonyl groups detectable by infrared spectroscopy (Chapter 42). Polypropylene, with a tertiary hydrogen on every repeat unit, oxidizes much faster than polyethylene and is useless outdoors or hot without stabilization.

**Stabilizers** interrupt the cycle: primary antioxidants (hindered phenols, aromatic amines) donate hydrogen to peroxy radicals; secondary antioxidants (phosphites, thioesters) decompose hydroperoxides harmlessly. Their consumption defines an **induction period**, during which properties barely change, followed by rapid embrittlement once the stabilizer is depleted. The remaining stabilizer is measured by the **oxidation induction time** (OIT), the time to the onset of the oxidation exotherm in a DSC at, for example, 200 °C in oxygen, a routine test for polyethylene pipes and geomembranes.

### Photo-oxidation and weathering

Solar ultraviolet radiation between 290 and 400 nm carries 300–410 kJ/mol per photon, comparable to C–C and C–H bond energies. Chromophores (carbonyl groups, catalyst residues, aromatic rings) absorb it and initiate radicals, so photo-oxidation adds to thermo-oxidation at the surface. Outdoor plastics chalk, yellow, lose gloss and develop surface microcracks that act as notches; garden furniture and unprotected polypropylene ropes embrittle in a few summers. Weathering adds moisture, temperature cycling and pollutants.

Protection comes from **UV absorbers** (benzotriazoles, benzophenones), **hindered-amine light stabilizers** (HALS), which scavenge radicals regeneratively and are the most effective for polyolefins, and **pigments**: 2–3 % of well-dispersed carbon black makes polyethylene pipe and cable jacket essentially UV-proof for decades. Accelerated weathering uses xenon-arc or fluorescent UV lamps with water spray (ISO 4892, ASTM G154/G155), but because the lamp spectrum, temperature and wetting differ from sunlight, results rank materials rather than predict outdoor life; reference outdoor sites in Florida (hot, humid) and Arizona (hot, high UV) remain the benchmarks.

### Hydrolysis, environmental stress cracking and physical aging

- **Hydrolysis** breaks ester, amide, carbonate and urethane linkages: PET and polycarbonate lose molecular weight in hot water or steam; polyester polyurethanes crumble in humid tropical climates; polyamides absorb water and some hydrolyse in hot glycol coolants. In biomedical PLA and PLGA, hydrolysis is the designed degradation route (Chapter 31).
- **Environmental stress cracking (ESC)** is the polymer analogue of SCC: a liquid that does not dissolve the polymer (detergent on polyethylene, alcohols or oils on polycarbonate and ABS, cleaning agents on medical housings) plasticizes the craze fibrils at a stressed surface and allows cracks to grow at stresses far below those needed in air. It is the most common cause of plastic part failures in practice. Slow crack growth of polyethylene pipe under internal pressure is the related long-term mechanism, which is why modern PE100 and PE100-RC pipe resins are rated for resistance to it.
- **Physical aging** of glassy polymers below $T_g$: the non-equilibrium glass slowly densifies (Chapter 20), raising modulus and yield stress and lowering toughness and creep rate, with no chemical change. It is reversible by heating above $T_g$.
- **Loss of plasticizer** from flexible PVC (cables, hoses, medical tubing) by evaporation or migration into contacting materials leaves it stiff and cracked.

### Arrhenius extrapolation

Thermal life is estimated by aging specimens in ovens at several elevated temperatures until a property (commonly elongation at break) falls to an end-of-life value, often 50 % of its initial value. If one reaction controls the rate at all test temperatures, the life follows

$$
L(T)=L_0\exp\!\left(\frac{E_a}{RT}\right)
$$

and a plot of $\ln L$ against $1/T$ (Figure 36.2) is a straight line that can be extrapolated to the service temperature. Standards such as IEC 60216 and UL 746B use this procedure to define thermal indices: the temperature at which life reaches a reference value such as 20 000 h. A useful consequence is the rule that life roughly halves for every 10 °C rise near the test temperature; with $E_a=113$ kJ/mol it halves every 6.7 K near 90 °C.

> **Status of the principle: Arrhenius aging extrapolation**
> *Empirical.* Its form follows from thermally activated reaction kinetics, but applied to the property loss of a real material it is a fit valid only while one mechanism dominates. Extrapolation across a glass transition or melting range, across a change from stabilizer-controlled to oxidation-controlled behaviour, or from diffusion-limited oxidation in thick specimens at high temperature (where oxygen cannot reach the interior fast enough) to homogeneous oxidation at service temperature, is unsafe.

<!-- FIGURE 36.2 | figures/ch36/fig-36-2-arrhenius-polymer-aging.png | plot | Arrhenius plot of oven-aging life of a polyolefin cable jacket with extrapolation to service temperatures, showing the sensitivity to activation energy. | Content: x-axis 1000/T in K⁻¹ from 2.3 to 3.0 with a secondary top axis in °C (160, 150, 135, 120, 100, 90, 70, 60); y-axis time to 50 % retained elongation in hours, log scale 1e2 to 1e7. Three data points: 150 °C 300 h, 135 °C 1000 h, 120 °C 3500 h. Solid fitted line Ea = 113 kJ/mol extrapolated (dashed) to 70 °C giving 5.4e5 h; second dashed line from the 150 °C point with Ea = 80 kJ/mol giving 6.0e4 h at 70 °C. Horizontal reference line at 20 000 h 'thermal index'. Shaded band beyond the data labelled 'extrapolation: mechanism must not change'. -->

**Worked example — service life of a cable jacket from oven aging.** A polyolefin cable jacket compound is aged at three temperatures, and the time for the elongation at break to fall to 50 % of its initial value is recorded:

| Aging temperature | 150 °C (423.15 K) | 135 °C (408.15 K) | 120 °C (393.15 K) |
|---|---|---|---|
| Time to end of life | 300 h | 1000 h | 3500 h |

A least-squares fit of $\ln L$ against $1/T$ gives a slope $E_a/R=1.362\times10^4$ K, so $E_a=1.362\times10^4\times8.314=113$ kJ/mol (1.17 eV). The fitted line reproduces the data to within 2 % (302, 986 and 3523 h). Extrapolating from 150 °C:

$$
L(70\ ^\circ\mathrm C)=300\times\exp\!\left[1.362\times10^4\left(\frac{1}{343.15}-\frac{1}{423.15}\right)\right]=300\times\exp(7.50)\approx5.4\times10^{5}\ \mathrm h\approx62\ \text{years}
$$

At 90 °C the same calculation gives about $6.1\times10^4$ h, roughly 7 years: a 20 K rise in conductor temperature cuts the life ninefold.

The fragility of the extrapolation is the real lesson. Three points spanning 30 K are being projected 50 K beyond the data, across more than two decades of time. If the true activation energy at lower temperatures were 80 kJ/mol rather than 113 kJ/mol (a common situation when a different, lower-barrier process dominates at low temperature), the life at 70 °C would be about $6\times10^4$ h, about 7 years instead of 62. That is why long-life ratings require test temperatures as close to service as practical, at least four temperatures, a check for linearity, and confirmation by OIT or infrared spectroscopy that the same chemistry is occurring at each temperature.

---

## 36.4 Wear-out mechanisms and life prediction

### The catalogue of life laws

Wear-out failures are those whose probability rises with age because damage accumulates. The laws that predict them have appeared in earlier chapters; collected here, they form the toolkit of life prediction:

| Mechanism | Life law | Typical parameters | Status |
|---|---|---|---|
| High-cycle fatigue | Basquin: $\sigma_a=\sigma_f'(2N_f)^b$ | $b\approx-0.05$ to $-0.12$ | Empirical |
| Low-cycle fatigue | Coffin–Manson: $\Delta\varepsilon_p/2=\varepsilon_f'(2N_f)^c$ | $c\approx-0.5$ to $-0.7$ | Empirical |
| Fatigue crack growth | Paris: $da/dN=C(\Delta K)^m$ | $m\approx3$ (steels), 3–4 (Al alloys) | Empirical |
| Variable-amplitude fatigue | Miner: $\sum n_i/N_i=1$ | failure at sum 0.3–3 in practice | Empirical |
| Creep rupture | Larson–Miller: $P=T(C+\log_{10}t_r)$ | $C\approx20$ ($t_r$ in h, $T$ in K) | Empirical |
| Thermally activated aging | Arrhenius: $L\propto\exp(E_a/RT)$ | $E_a$ 50–150 kJ/mol for polymers | Empirical |
| Humidity-driven corrosion | Peck: $L\propto\mathrm{RH}^{-n}\exp(E_a/kT)$ | $n\approx2.7$, $E_a\approx0.8$ eV | Empirical |
| Diffusion-controlled ingress | $x=k\sqrt t$ | carbonation $k$ 2–6 mm/year$^{1/2}$ | Approximate |
| Sliding wear | Archard: $V=KFs/H$ | $K$ from $10^{-8}$ to $10^{-2}$ | Empirical |

The electronic-specific laws (Black's equation for electromigration, TDDB models for dielectrics, Norris–Landzberg for solder joints) are developed in the Materials Core book, Ch 24.

Each law is used in the same way: measure its parameters under accelerated conditions, compute an **acceleration factor** between test and service, and convert test life to service life. Each carries the same caveat: the mechanism must be the same in test and service.

### Damage-tolerant design with the Paris law

For safety-critical structures that cannot be guaranteed crack-free (airframes, rail axles and wheels, pressure vessels, bridges), the design philosophy is **damage tolerance**: assume a crack of the largest size that inspection could miss, calculate how long it takes to grow to a critical size, and inspect at a fraction (typically half or a third) of that interval. With $\Delta K=Y\Delta\sigma\sqrt{\pi a}$ and constant $Y$, integrating the Paris law from initial size $a_0$ to critical size $a_c$ gives, for $m\neq2$,

$$
N_f=\frac{2}{(m-2)\,C\,(Y\Delta\sigma\sqrt{\pi})^{m}}\left[a_0^{(2-m)/2}-a_c^{(2-m)/2}\right]
$$

> **Status of the principle: Paris-law crack-growth integration**
> *Empirical.* The Paris law is a fit to the intermediate (stage II) region of crack-growth data; it ignores the threshold below which cracks do not grow, the acceleration near $K_{\rm Ic}$, load-sequence effects (overload retardation) and short-crack behaviour, so lives computed from it are reliable only for long cracks under roughly constant-amplitude loading.

**Worked example — inspection interval for a cracked steel plate.** A ferrite–pearlite steel plate in a crane girder carries a constant-amplitude stress range $\Delta\sigma=100$ MPa ($R=0$, so $\sigma_{\max}=100$ MPa). Ultrasonic inspection can reliably find edge cracks of 2 mm and larger. Paris constants are $C=6.9\times10^{-12}$ m/cycle and $m=3$ (with $\Delta K$ in MPa√m), $K_{\rm Ic}=100$ MPa√m, and $Y=1.12$.

*Critical crack size:*

$$
a_c=\frac{1}{\pi}\left(\frac{K_{\rm Ic}}{Y\sigma_{\max}}\right)^2=\frac{1}{\pi}\left(\frac{100}{112}\right)^2=0.254\ \mathrm m
$$

(in practice the plate width or net-section yielding would limit this first; we keep it to see its influence).

*Cycles from 2 mm to $a_c$:* with $m=3$, the bracket is $a_0^{-1/2}-a_c^{-1/2}=22.36-1.99=20.37$ m$^{-1/2}$, and $(Y\Delta\sigma\sqrt\pi)^3=(112\times1.7725)^3=(198.5)^3=7.82\times10^6$:

$$
N_f=\frac{2\times20.37}{6.9\times10^{-12}\times7.82\times10^{6}}=7.5\times10^{5}\ \text{cycles}
$$

Three sensitivities follow directly. Taking $a_c=50$ mm instead of 254 mm reduces $N_f$ only to $6.6\times10^5$ cycles: almost all the life is spent while the crack is small, so the critical size hardly matters. Halving the detectable crack to 1 mm raises $N_f$ to $1.10\times10^6$ cycles: better inspection buys life directly. Raising the stress range by 25 % to 125 MPa cuts $N_f$ to $3.8\times10^5$ cycles (and $a_c$ to 0.16 m), because life scales as $\Delta\sigma^{-3}$. At 300 lifts a day the 2 mm case allows about 7 years of crack growth, so an inspection every two to three years gives two chances to find the crack before it is critical. The Eschede tyre of the opening was an object lesson in the last sensitivity: wear thinned the section, raising the stress range in service beyond what the original assessment had assumed.

### Variable loads and Miner's rule

Real loads vary. **Miner's rule** assumes that each cycle at amplitude $\sigma_i$ consumes a fraction $1/N_i$ of life, where $N_i$ is the constant-amplitude life at that amplitude, and that failure occurs when $\sum n_i/N_i=1$. Load histories are reduced to counts of cycles by rainflow counting. The rule ignores load sequence (a high-low sequence is more damaging than low-high) and the fact that small cycles below the endurance limit become damaging once a crack exists, so design codes often limit the damage sum to 0.5 or less, or extend S–N curves below the endurance limit with a shallower slope.

### Creep life and the Larson–Miller parameter

Creep-rupture data are extrapolated with time–temperature parameters (Chapter 14). With the Larson–Miller parameter, a stress that causes rupture in 1000 h at 650 °C (923.15 K) has $P=923.15\times(20+3)=2.123\times10^4$; at the same stress and 600 °C (873.15 K), $\log_{10}t_r=2.123\times10^4/873.15-20=4.32$, so $t_r\approx2.1\times10^4$ h. A 50 K reduction in temperature buys a factor of 21 in life. Power-plant steam pipes and reformer tubes are managed this way, with remaining-life assessment by replica metallography of creep cavities on the outer surface.

---

## 36.5 Reliability statistics

### Describing a population of lives

Nominally identical components fail at different times, because flaws, loads and environments vary. Reliability engineering describes the population by:

- the cumulative failure probability $F(t)$ and the **reliability** $R(t)=1-F(t)$;
- the probability density $f(t)=dF/dt$;
- the **hazard rate** $h(t)=f(t)/R(t)$, the instantaneous failure rate of survivors, which tells whether old components are more or less likely to fail than new ones.

### The Weibull distribution

The most widely used life distribution in mechanical and materials reliability is the two-parameter Weibull:

$$
F(t)=1-\exp\!\left[-\left(\frac{t}{\eta}\right)^{\beta}\right],\qquad h(t)=\frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1}
$$

where $\eta$ is the **characteristic life** (63.2 % failed) and $\beta$ the **shape parameter**. Its flexibility comes from $\beta$: $\beta<1$ gives a falling hazard (infant mortality from manufacturing defects), $\beta=1$ a constant hazard (random failures, the exponential distribution), and $\beta>1$ a rising hazard (wear-out; $\beta\approx2$–4 for fatigue and wear, larger for tightly controlled processes). Its physical justification is the weakest-link argument already used for ceramic strength (Chapter 14): a component that fails when its worst element fails follows Weibull statistics. Mean life is $\mathrm{MTTF}=\eta\,\Gamma(1+1/\beta)$. The **B10 life**, the time by which 10 % have failed, is standard for bearings and many mechanical parts:

$$
t_{B10}=\eta\left[-\ln(0.9)\right]^{1/\beta}
$$

The **lognormal** distribution is an alternative when damage grows multiplicatively (fatigue lives of many metals, electromigration); with limited data the two are hard to distinguish, but they diverge in the low-percentile tail that matters for safety.

> **Status of the principle: Weibull life distribution**
> *Empirical.* Justified by weakest-link reasoning where failure starts at the worst of many independent flaws, but in reliability practice it is a flexible fit; extrapolation to failure fractions far below those observed is sensitive to the fitted $\beta$, and mixed populations (defective plus sound) need separate distributions.

### The bathtub curve

Over the life of a product population, the hazard rate typically follows the **bathtub curve** (Figure 36.3): a falling early-failure region (defective units failing; addressed by burn-in, proof testing and process control), a flat region of random failures (overloads, accidents; addressed by margins), and a rising wear-out region (fatigue, wear, aging; addressed by life prediction and preventive replacement). The curve is a composite: each region is a different population or mechanism, and each has its own Weibull $\beta$. Many well-designed mechanical products show little flat region at all, and electronic products often wear out only after obsolescence.

<!-- FIGURE 36.3 | figures/ch36/fig-36-3-bathtub-curve.png | plot | The bathtub curve as the sum of three Weibull hazard populations. | Content: x-axis time (normalized, 0 to 1.2 of design life, linear); y-axis hazard rate h(t) (arbitrary units, linear, 0 to 5). Three dashed component hazards: infant mortality Weibull β = 0.5 decaying; random β = 1 constant at 0.5; wear-out β = 4 rising from about 0.6 of life. Solid total curve as their sum showing the bathtub. Shaded regions labelled 'early failures: burn-in, proof test, process control', 'random failures: design margin', 'wear-out: preventive replacement'. Vertical dashed line at 'design life'. -->

### Fitting data and reading the result

Failure times are ranked, each is assigned an estimated cumulative probability by **median ranks**, $F_i\approx(i-0.3)/(n+0.4)$ (Bernard's approximation), and $\ln[-\ln(1-F)]$ is plotted against $\ln t$. A straight line confirms the Weibull form; its slope is $\beta$ and its intercept gives $\eta$ (Figure 36.4). Maximum-likelihood estimation is preferred for censored data (units still running when the test ends).

**Worked example — Weibull analysis of hydraulic pump seals.** Ten seals from a test rig fail at 410, 620, 780, 900, 1020, 1130, 1260, 1400, 1590 and 1900 h. Median ranks run from $F_1=0.7/10.4=0.067$ to $F_{10}=9.7/10.4=0.933$. A least-squares fit of $\ln[-\ln(1-F_i)]$ on $\ln t_i$ gives

$$
\beta=2.42,\qquad \eta=1252\ \mathrm h
$$

The shape parameter well above 1 identifies wear-out. The B10 life is

$$
t_{B10}=1252\times(0.1054)^{1/2.42}=1252\times0.395=495\ \mathrm h
$$

and the mean life is $\mathrm{MTTF}=1252\times\Gamma(1.413)=1252\times0.887=1110$ h (the sample mean is 1101 h). The hazard rate rises from $5.2\times10^{-4}$ per hour at 500 h to $2.5\times10^{-3}$ per hour at 1500 h, nearly fivefold. Because failures are wear-out, preventive replacement pays: replacing seals at 500 h accepts about a 10 % chance of an in-service failure per seal, whereas running to failure would see half of them fail before 1080 h. If instead $\beta$ had come out near 1, preventive replacement would be pointless, since a new seal would be no more reliable than an old one. Ten failures give $\beta$ with a 90 % confidence interval of roughly ±40 %, so a decision that depends on the B1 life rather than the B10 would need more data.

<!-- FIGURE 36.4 | figures/ch36/fig-36-4-weibull-seals.png | plot | Weibull probability plot of ten pump-seal failures with the fitted line, characteristic life and B10 life. | Content: x-axis time to failure in h, log scale 200–3000; y-axis ln(−ln(1−F)) from −3 to 1.5 with right-hand labels F = 5 %, 10 %, 20 %, 50 %, 63.2 %, 90 %, 95 %. Ten data points at t = 410, 620, 780, 900, 1020, 1130, 1260, 1400, 1590, 1900 h with median ranks (i−0.3)/10.4. Fitted line β = 2.42, η = 1252 h. Horizontal dashed lines at F = 10 % and 63.2 % with vertical drops at 495 h (B10) and 1252 h (η). Text box 'β = 2.42: wear-out'. -->

---

## 36.6 Failure analysis: methodology, fractography and root cause

### Principles

Failure analysis is the systematic reconstruction of how and why a component failed. Three principles govern it:

1. **Preserve evidence.** Fracture surfaces are damaged by fitting broken halves together, by cleaning, by corrosion after the event and by careless sectioning. Every destructive step removes information; proceed from non-destructive to destructive and document each step.
2. **Collect the history.** Design drawings, material certificates, manufacturing and repair records, operating loads and environment, time in service and similar failures elsewhere. Clustering of failures by production lot, supplier, site or season points directly to a class of causes.
3. **Distinguish mechanism from root cause.** "Fatigue crack from a weld toe" is a mechanism. The root cause is why the conditions for it existed: a weld detail with a high stress concentration, a change in welding procedure, a load spectrum underestimated in design, an inspection that missed the crack. Only a root cause can be corrected.

### The workflow

Figure 36.5 summarizes the standard sequence.

<!-- FIGURE 36.5 | figures/ch36/fig-36-5-failure-analysis-workflow.png | flowchart | Failure-analysis workflow from the failed part to verified corrective action. | Content: top-to-bottom flowchart: (1) 'Background: service history, loads, environment, drawings, material certificates, similar failures'; (2) 'Preserve and document: photographs, chain of custody, protect fracture surfaces'; (3) 'Non-destructive examination: visual, stereo microscope, dye penetrant, magnetic particle, ultrasonic, eddy current, X-ray CT'; (4) 'Fractography: macro (origin, beach marks, chevrons, shear lips) and SEM (dimples, cleavage, striations, intergranular)'; (5) 'Metallography and testing: sections, hardness, chemistry (OES, EDS), tensile and Charpy, FTIR/DSC for polymers'; (6) 'Mechanism identified'; (7) 'Root cause: 5-why, fishbone, fault tree' with side input 'compare with sound parts and design assumptions'; (8) 'Verify: stress analysis, reproduce failure'; (9) 'Corrective action: design, material, process, inspection; 8D report, FMEA update'. Dashed feedback arrow from 9 to 'design and specifications'. Non-destructive steps green, destructive orange, reasoning steps blue. -->

Non-destructive examination comes first: visual inspection and stereo microscopy to locate the origin and the sequence of fracture; dye-penetrant and magnetic-particle inspection to find other cracks; ultrasonic, eddy-current and radiographic or CT inspection to find subsurface defects. Then the fracture surfaces are examined macroscopically and in the SEM, sections are cut through the origin for metallography (Chapter 42), hardness and chemical composition are checked against specification, and mechanical tests on material from the failed part confirm or exclude a materials deficiency. For polymers, FTIR, DSC and molecular-weight measurements reveal oxidation, wrong grade or degradation in moulding. Stress analysis, by hand or finite elements, checks whether the loads the evidence implies are consistent with the design.

### Reading fracture surfaces

Fractography is the most powerful single tool, because the fracture surface records how the crack grew (Figure 36.6).

| Feature | Scale | Meaning |
|---|---|---|
| Beach marks (clamshell marks) | Macroscopic | Successive positions of a fatigue crack front, from changes in load or environment; they point back to the origin |
| Ratchet marks | Macroscopic | Steps between multiple fatigue origins; many ratchets indicate high stress or a stress concentration |
| Chevron (herringbone) marks | Macroscopic | Fast brittle fracture in plate; the chevrons point back toward the origin |
| Shear lips | Macroscopic | Ductile final fracture under plane stress near free surfaces; small lips mean low toughness or high constraint |
| Dimples (microvoid coalescence) | SEM, 1–50 µm | Ductile overload; elongated or parabolic dimples indicate shear or tearing |
| Cleavage facets with river patterns | SEM | Brittle transgranular fracture in BCC metals below the transition temperature |
| Intergranular facets | SEM | Weak grain boundaries: temper embrittlement, hydrogen, SCC, creep cavitation, sensitization |
| Fatigue striations | SEM, 0.1–1 µm spacing | One striation per load cycle in ductile metals; spacing gives local crack growth rate |
| Branched cracks | Section | Stress-corrosion cracking |
| Mirror, mist and hackle | Glass, ceramics | Smooth mirror around the origin, then misty and rough hackle zones as the crack accelerates and branches |
| Crazes, stretched fibrils, slow-crack-growth bands | Polymers | Environmental stress cracking or slow crack growth |

Two quantitative readings are routine. Striation spacing measured at several distances from the origin, compared with the Paris law, estimates the stress range that grew the crack. In glasses and ceramics, the mirror radius $r_m$ is related to the fracture stress by $\sigma_f\sqrt{r_m}=A$, with mirror constant $A\approx2$ MPa√m for soda-lime glass; a mirror of radius 0.5 mm therefore indicates a fracture stress of about $2/\sqrt{5\times10^{-4}}\approx89$ MPa, which tells the analyst whether the pane broke at a normal service load from a damaged edge or under an abnormal load.

<!-- FIGURE 36.6 | figures/ch36/fig-36-6-fractography-features.png | micrograph-style | Characteristic fracture-surface features used to identify failure mechanisms. | Content: six-panel montage of stylized SEM/macro views, each with a scale bar and label: (a) macro view of a fatigued shaft cross-section with origin at a keyway, beach marks and a final-overload zone (scale 10 mm); (b) fatigue striations, spacing ~0.5 µm (scale 2 µm); (c) equiaxed ductile dimples with inclusions at their bottoms (scale 10 µm); (d) cleavage facets with river patterns converging in the propagation direction (scale 20 µm); (e) intergranular facets showing smooth grain faces (scale 20 µm); (f) glass fracture origin with mirror, mist and hackle zones and the mirror radius r_m marked (scale 0.5 mm). -->

> **Status of the principle: Fracture-mirror relation**
> *Empirical.* The relation $\sigma_f\sqrt{r_m}=A$ follows dimensionally from crack-branching at a critical stress intensity, but $A$ is measured for each material and the relation assumes a sharp origin and nearly uniform stress over the mirror.

### Root-cause tools

- **5-why analysis**: asking *why* repeatedly until a controllable cause is reached. For a fatigued pump shaft: Why did it break? Fatigue from the keyway. Why? Rotating bending stress above the fatigue strength at the keyway corner. Why? The corner radius was 0.1 mm instead of the drawn 0.5 mm. Why? A worn cutter was used and the radius is not inspected. Why? The inspection plan lists the radius as non-critical. The last answer is actionable.
- **Ishikawa (fishbone) diagrams**: candidate causes grouped under materials, methods, machines, measurement, environment and people, so none is overlooked.
- **Fault-tree analysis**: top-down logical decomposition of the failure into AND/OR combinations of basic events, used where several conditions must coincide (SCC needs stress AND environment AND susceptible material).
- **8D** (eight disciplines): team, problem description, containment, root cause and escape point, corrective action, validation, prevention of recurrence, closure. The materials engineer's work concentrates in root cause and validation.
- **FMEA**: the forward-looking counterpart, listing for a new design each potential failure mode, its effect, cause and controls, and ranking it before release. The mechanisms of Chapters 34–37 are the vocabulary of a good FMEA, and lessons from failure analysis feed back into it.

> **Boundary.** Formal reliability engineering (confidence bounds, accelerated-test planning, system reliability block diagrams) and the statistics behind it belong to The Mathematics Universe and engineering-management courses; the electronic failure mechanisms and their FA techniques (emission microscopy, OBIRCH, decapsulation) are treated in the Materials Core book, Ch 24.

---

## 36.7 Case studies across industries

The value of case studies is in the pattern. In almost every major materials failure the mechanism was known at the time; what failed was the recognition that the mechanism applied, the estimate of its rate, or the inspection meant to catch it.

| Case | Industry | Mechanism | Root cause and lesson |
|---|---|---|---|
| Liberty ships and T2 tankers (1940s) | Marine | Brittle fracture of welded hulls in cold seas | Steel with high ductile–brittle transition temperature, welded continuous hulls letting cracks run between plates, square hatch corners; led to Charpy toughness requirements and modern fracture mechanics |
| de Havilland Comet (1954) | Aerospace | Fatigue of pressurized fuselage | Cyclic pressurization stresses at cut-out corners underestimated; led to full-scale fatigue testing and fail-safe design |
| Silver Bridge, Ohio (1967) | Civil | Brittle fracture of an eyebar from a small crack grown by stress corrosion and corrosion fatigue | Non-redundant eyebar chain, a crack hidden in an uninspectable location; led to US national bridge inspection standards |
| Aloha Airlines 243 (1988) | Aerospace | Multiple-site fatigue at fuselage lap joints after disbonding and corrosion | High-cycle, humid, salt environment; inspection intervals based on flight hours not cycles; led to aging-aircraft programmes |
| Space Shuttle Challenger (1986) | Aerospace | Loss of elastomer resilience at low temperature in field-joint O-rings | Seals operated far below qualified temperature; viscoelastic recovery too slow to follow joint opening (Chapter 14) |
| Eschede ICE (1998) | Rail | Fatigue fracture of a resilient wheel tyre | Cyclic stresses in a thinning tyre underestimated; inspection unable to detect internal cracks |
| Zirconia femoral heads (2001) | Biomedical | Hydrothermal aging and fracture of 3Y-TZP | Process change in sintering altered microstructure in some batches; showed that a processing change can create a new degradation mechanism |
| Davis-Besse reactor head (2002) | Energy | Boric-acid wastage of carbon-steel head, after PWSCC of a nozzle let coolant leak | Leak indications missed for years; only the stainless cladding held pressure |
| Metal-on-metal hip implants (2010 recalls) | Biomedical | Wear and corrosion debris causing tissue reactions | Wear in edge-loading conditions not captured by standard simulator tests (Chapter 37) |
| Silver-sulfide resistor failures | Electronics | Sulfidation of silver electrodes through termination gaps | Office-environment components used in sulfur-rich industrial air (Materials Core, Ch 24) |

Three lessons recur.

**First, interactions defeat single-mechanism analysis.** Silver Bridge needed a stress-corrosion crack to start a brittle fracture; Davis-Besse needed SCC to create the leak that drove wastage; Aloha needed disbonding to load the rivets that fatigued. Fault trees with AND gates describe these failures better than any single life law.

**Second, the service condition, not the material, was usually misjudged.** Comet's designers knew about fatigue; they underestimated the stress at the corners. Challenger's O-ring compound was suitable within its qualified temperature range. Eschede's tyre steel was adequate for the stress the design assumed. The engineering response is a materials engineer's insistence on the real environment, real loads and real temperature, measured not assumed.

**Third, processing changes are silent design changes.** A sintering change made zirconia heads age; a welding procedure change or a new supplier's steel can move a transition temperature. Every process change to a safety-critical part therefore needs the same qualification as the original design.

> **Status of the principle: Case-study lessons**
> *Empirical.* Generalizations drawn from investigated failures; they are heuristics for where to look, not laws, and each case report should be read in its original investigation for the details that matter.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| Electrochemical thermodynamics and kinetics behind corrosion damage | Chapter 34 |
| Forms of corrosion, hydrogen embrittlement and corrosion fatigue in detail | Chapter 35 |
| Fracture mechanics, fatigue laws, creep and Weibull strength of ceramics | Chapter 14 |
| Composition, curing and durability design of concrete | Chapter 18 |
| Molecular structure behind polymer oxidation and physical aging | Chapters 19 and 20 |
| Moisture and fatigue damage in laminates; composite design allowables | Chapters 22 and 23 |
| Wear, friction and surface fatigue as life-limiting mechanisms | Chapter 37 |
| Radiation, high-temperature and cryogenic degradation | Chapter 33 |
| Weld defects and residual stresses as origins of failure | Chapter 39 |
| Characterization tools used in failure analysis (SEM, EDS, XRD, FTIR, DSC) | Chapter 42 |
| Choosing materials so that the dominant degradation mechanism is slow enough; lifecycle impact of replacement | Chapters 48 and 49 |
| Electromigration, dielectric breakdown and solder-joint life in electronics | Materials Core (EEE), Ch 24 |

**Next:** Chapter 37 turns to the surface itself, where adhesion, friction and wear are decided, and to the engineering of surfaces that resist them.
