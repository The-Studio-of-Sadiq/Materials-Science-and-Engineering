# Chapter 17 — Ceramics and Glasses

*Part IV · Metals, Ceramics and Construction Materials*

In 2001 a series of zirconia femoral heads for hip replacements began to fracture inside patients, a few years after implantation. Zirconia had been chosen precisely because it is the toughest of the oxide ceramics, with a bend strength above 900 MPa, and millions of heads had been implanted without trouble. The failed heads came from a small number of batches made after the manufacturer changed its sintering furnace. In those batches the slightly different firing had left a microstructure in which the metastable tetragonal zirconia transformed to the monoclinic form far more readily than normal, slowly and at body temperature, in the presence of water. The transformation, which in a good microstructure *toughens* the ceramic by stopping cracks, had become a degradation mechanism that roughened and microcracked the surface until the head split. Nothing in the composition had changed; only the processing had.

Ceramics and glasses are the materials in which this sensitivity is greatest. Their bonds make them hard, stiff, chemically inert and refractory, and also brittle: their strength is set not by their atoms but by their largest flaw, and the flaws are made by processing. A glass bottle, a spark plug, a silicon-nitride bearing ball, a cooktop and a furnace lining all illustrate the same rule: in these materials, processing *is* properties.

> **Why are ceramics hard, stiff, refractory and brittle, and how is their brittleness managed?**
> **How are ceramic components made from powders and glasses made from melts, and how do sintering, viscosity, tempering and crystallization set their final properties?**

| Concept | Engineering destination |
|---|---|
| Ionic–covalent bonding and crystal structure | Hardness, stiffness, melting point, chemical inertness, electrical insulation |
| Technical ceramics: alumina, zirconia, SiC, Si₃N₄ | Wear parts, seals, bearings, cutting tools, armour, implants, substrates |
| Powder processing and sintering | Shrinkage allowances, porosity, grain size, strength of every ceramic part |
| Flaws, Weibull statistics, toughening | Design stresses, proof testing, reliability of ceramic components |
| Glass formation and network structure | Composition of window, container, fibre, display and laboratory glasses |
| Viscosity–temperature behaviour | Glass forming, annealing schedules, sealing, softening limits |
| Tempering and chemical strengthening | Safety glazing, vehicle glass, phone cover glass |
| Glass-ceramics | Cooktops, telescope mirrors, dental crowns, radomes |
| Refractories | Linings for steel, glass, cement and aluminium furnaces |
| Functional ceramics | Capacitors, sensors, actuators, fuel cells, magnets, phosphors |

**Roadmap.** Bonding and structure (17.1) → traditional versus technical ceramics (17.2) → powder processing and sintering (17.3) → mechanical behaviour and toughening (17.4) → how glasses form (17.5) → viscosity, annealing and strengthening of glass (17.6) → glass-ceramics (17.7) → refractories (17.8) → functional ceramics, a pointer forward (17.9).

---

## 17.1 Structure and bonding of engineering ceramics

### Mixed ionic–covalent bonding

A ceramic is an inorganic, non-metallic solid, usually a compound of a metal or metalloid with oxygen, nitrogen, carbon or boron. Its bonds are mixtures of ionic and covalent character. Pauling's estimate of the fractional ionic character of a bond between elements of electronegativities $\chi_A$ and $\chi_B$ (a bonding result recapped from Advanced Chemistry) is

$$
f_{\mathrm{ionic}}=1-\exp\left[-\tfrac14(\chi_A-\chi_B)^2\right]
$$

With Pauling electronegativities this gives about 68 % for Mg–O, 67 % for Zr–O, 57 % for Al–O, 45 % for Si–O, 40 % for Al–N, 28 % for Si–N and only 10 % for Si–C. The oxides are predominantly ionic; the nitrides and carbides are predominantly covalent.

> **Status of the principle: Pauling fractional ionic character**
> *Empirical.* A one-parameter interpolation calibrated on dipole moments of diatomic molecules; useful for ranking bonds, not as a quantitative measure of charge transfer in solids.

The structures follow the bonding (Chapter 2). Ionic oxides adopt structures that pack large anions around smaller cations with coordination numbers set by the radius ratio and with local charge balance (Pauling's rules): rock salt for MgO, corundum for Al₂O₃ (Al in octahedral sites of a nearly HCP oxygen array), fluorite for cubic ZrO₂ and CeO₂, perovskite for BaTiO₃, spinel for MgAl₂O₄. Covalent ceramics adopt structures dictated by directional sp³ bonds: SiC is a tetrahedral network with more than 200 stacking polytypes (3C, 4H, 6H are the common ones); Si₃N₄ consists of corner-sharing SiN₄ tetrahedra in α and β hexagonal forms; AlN is wurtzite. Silica and the silicates are built from SiO₄ tetrahedra linked through shared corners, and the many ways of linking them (isolated, chains, sheets, frameworks) produce the mineral and glass families that dominate traditional ceramics and glasses.

### Consequences of the bonding

Strong, directional or charge-constrained bonds produce the characteristic property profile:

- **High melting points**: Al₂O₃ 2054 °C, ZrO₂ 2715 °C, MgO 2852 °C; SiC and Si₃N₄ decompose (about 2700 °C and 1900 °C).
- **High stiffness and hardness**: $E$ of 300–450 GPa; Vickers hardness 15–30 GPa, against 2–8 GPa for hardened steels; low density for the covalent ceramics (2.5–3.2 Mg/m³).
- **Brittleness**: in covalent crystals the Peierls stress is a large fraction of the shear modulus; in ionic crystals slip must avoid bringing like charges together, leaving too few slip systems for polycrystal plasticity (Chapters 12–13). A crack advances by breaking bonds before any dislocation can blunt it.
- **Insulation and inertness** for the oxides (with exceptions, Section 17.9); low thermal conductivity for complex oxides but very high for simple, stiff, light-atom crystals such as SiC and AlN (Chapter 24).

| Material | Density (Mg/m³) | $E$ (GPa) | Flexural strength (MPa) | $K_{IC}$ (MPa m$^{1/2}$) | Vickers hardness (GPa) | $k$ (W m⁻¹ K⁻¹) | CTE (10⁻⁶ K⁻¹) |
|---|---|---|---|---|---|---|---|
| Alumina, 99.5 % | 3.90 | 370 | 350–450 | 3.5–4.5 | 15–18 | 30 | 8.0 |
| Alumina, 96 % | 3.75 | 300 | 300–350 | 3.5 | 12–14 | 24 | 7.5 |
| Zirconia, 3Y-TZP | 6.05 | 205 | 900–1200 | 5–10 | 12–13 | 2.5–3 | 10.5 |
| Mg-PSZ | 5.75 | 200 | 600–700 | 8–12 | 11 | 2.5 | 10 |
| Sintered SiC | 3.15 | 410 | 400–500 | 3–4 | 25 | 100–120 | 4.0 |
| Reaction-bonded SiC (SiSiC) | 3.10 | 350–390 | 250–350 | 3.5–4 | 20–25 | 125–150 | 4.3 |
| Si₃N₄, gas-pressure sintered | 3.20 | 300–320 | 700–1000 | 6–8 | 15–16 | 20–30 | 3.2 |
| AlN | 3.26 | 330 | 300–350 | 3 | 11 | 170–200 | 4.5 |
| B₄C | 2.52 | 450 | 350–450 | 2.5–3.5 | 30–35 | 30 | 5.0 |
| Soda-lime glass | 2.50 | 70 | 50–70 (as used) | 0.75 | 5.5 | 1.0 | 9.0 |
| Fused silica | 2.20 | 72 | 50–70 (as used) | 0.75 | 6–7 | 1.4 | 0.55 |

Values are typical for dense commercial grades; strengths depend strongly on processing and specimen size (Section 17.4).

---

## 17.2 Traditional versus technical ceramics

### Traditional ceramics

**Traditional** ceramics (whitewares, bricks, tiles, sanitaryware) are made from clays, feldspars and quartz. Clay minerals such as kaolinite, Al₂Si₂O₅(OH)₄, are fine sheet silicates that become plastic with water and hold their shape when dried. On firing at 1000–1400 °C the feldspar flux melts to a viscous glass that dissolves part of the clay and quartz, and mullite (3Al₂O₃·2SiO₂) needles crystallize. A **triaxial porcelain** (about 50 % clay, 25 % feldspar, 25 % quartz) ends as mullite, quartz and glass, the classic insulator and tableware material. This **vitrification**, densification by viscous flow of a liquid, is the ancestor of liquid-phase sintering. Bricks use cheaper clays fired lower and stay porous (Chapter 18).

### Technical ceramics

**Technical** (advanced, engineering) ceramics are made from synthetic, high-purity powders of controlled particle size, formed and sintered to near full density and fine grain size. Four materials account for most structural use.

**Alumina** (Al₂O₃) is the workhorse: cheap, hard, insulating and stable, in purities from 85 % to 99.9 %. Lower grades contain a grain-boundary silicate glass from liquid-phase sintering and are easier to metallize but weaker when hot. Uses include wear parts, seals, armour, substrates, spark-plug insulators and hip-joint bearings (Chapter 31).

**Zirconia** (ZrO₂) is monoclinic below about 1170 °C, tetragonal up to about 2370 °C and cubic to its melting point. The tetragonal-to-monoclinic transformation on cooling is martensitic and involves a volume increase of about 4 % that shatters pure zirconia. Dissolving Y₂O₃, MgO or CaO stabilizes the high-temperature forms (Chapter 7). With about 3 mol% Y₂O₃ and a grain size below about 0.5 μm, the tetragonal phase is retained metastably at room temperature (**3Y-TZP**, tetragonal zirconia polycrystal); in **Mg-PSZ** (partially stabilized zirconia) tetragonal precipitates sit inside cubic grains. Near a crack tip, the stress field triggers the transformation, and the expansion of the transformed zone squeezes the crack shut: **transformation toughening**, which raises $K_{IC}$ to 5–12 MPa m$^{1/2}$ (Chapter 14). The same metastability permits slow transformation in warm, moist environments (**low-temperature degradation**, the failure of the opening paragraph), controlled by grain size, yttria distribution and small alumina additions. Zirconia makes dental crowns, fibre-optic ferrules, pump plungers, oxygen sensors and fuel-cell electrolytes (Section 17.9), and turbine-blade thermal barrier coatings (Chapter 16).

**Silicon carbide** (SiC) is made by the Acheson process (carbothermal reduction of silica with coke at about 2500 °C). Dense parts are **solid-state sintered** with B and C at about 2100 °C (SSiC) or **reaction bonded** by infiltrating a SiC–carbon preform with molten silicon (SiSiC, 8–15 % free Si). SiC combines hardness, high conductivity, low expansion and resistance to acids and oxidation (protective SiO₂ to about 1600 °C): seal faces, burner and heat-exchanger tubes, armour, telescope mirrors, SiC/SiC composites (Chapter 23) and power semiconductors (Chapter 26).

**Silicon nitride** (Si₃N₄) hardly self-diffuses and decomposes before densifying, so it is sintered with 5–10 % Y₂O₃, Al₂O₃ or MgO, which form an oxynitride liquid at 1700–1850 °C under nitrogen. The α powder dissolves and reprecipitates as elongated β-Si₃N₄ grains (aspect ratio 5–10) that deflect and bridge cracks, an **in-situ toughened** ceramic with $K_{IC}$ of 6–8 MPa m$^{1/2}$. With the best strength, toughness and thermal-shock resistance of the monolithic ceramics, it makes bearing balls (light, and non-conductive, so immune to electrical arcing in motors), turbocharger rotors, cutting tools and power-electronics substrates; **SiAlONs** reduce the boundary glass.

> **Boundary.** The crystal structures (corundum, fluorite, wurtzite, perovskite, spinel) and Pauling's rules are developed in Chapter 2; ceramic phase diagrams (Al₂O₃–SiO₂, ZrO₂–Y₂O₃, MgO–Al₂O₃) in Chapter 7.

---

## 17.3 Ceramic powder processing

A metal can be melted, cast and worked. A ceramic usually cannot: its melting point is too high, its melt too reactive, and it cannot be deformed plastically to close casting porosity. Almost every technical ceramic is therefore made by **powder processing**: synthesize a powder, form it into a "green" body of the desired shape, and fire it so that the particles bond and the pores between them shrink and disappear. Every flaw the final part contains, every pore and agglomerate and inclusion, traces back to one of these steps.

### Powder synthesis

| Ceramic | Main synthesis route | Key powder characteristics |
|---|---|---|
| Al₂O₃ | Bayer process: digestion of bauxite in NaOH, precipitation of Al(OH)₃, calcination at 1100–1300 °C | 0.3–5 μm, purity 99.5–99.99 % |
| ZrO₂ (Y-doped) | Co-precipitation of mixed hydroxides from chloride solutions, or hydrothermal synthesis; calcination | 20–100 nm crystallites, yttria uniformly distributed |
| SiC | Acheson carbothermal reduction; milled and classified | Sub-micrometre α-SiC for sintering |
| Si₃N₄ | Direct nitridation of Si powder, or diimide precipitation | > 90 % α phase, sub-micrometre |
| BaTiO₃ | Solid-state reaction of BaCO₃ + TiO₂, or hydrothermal / oxalate routes | 0.1–0.5 μm for thin-layer capacitors |
| Glasses and coatings | Sol–gel: hydrolysis and condensation of alkoxides such as Si(OC₂H₅)₄ | Molecular-scale mixing, low processing temperature |

Fine powders sinter faster but agglomerate. Hard agglomerates pack poorly and leave large pores between them that do not close; the best ceramics come from powders that are fine, narrowly distributed and dispersed, often in a liquid with dispersants that control the surface charge (colloidal processing, Chapter 29).

### Forming

| Forming method | How it works | Typical products |
|---|---|---|
| Uniaxial dry pressing | Granulated powder pressed in a steel die at 50–150 MPa | Tiles, substrates, insulators, seal rings |
| Cold isostatic pressing (CIP) | Powder in a flexible mould pressed by fluid at 100–300 MPa | Spark-plug insulators, large blanks, tubes |
| Slip casting | Suspension poured into a porous plaster mould that absorbs liquid | Sanitaryware, crucibles, complex hollow shapes |
| Tape casting | Slurry spread by a doctor blade into thin sheets | Multilayer capacitors, substrates, SOFC electrolytes |
| Extrusion | Plastic paste forced through a die | Honeycomb catalyst supports, tubes, bricks |
| Ceramic injection moulding | Powder in thermoplastic binder (~40 vol%) moulded like a polymer | Small complex parts: dental brackets, ferrules, watch cases |
| Gel casting, additive manufacturing | In-situ polymerization; vat photopolymerization, binder jetting | Complex and customized parts (Chapter 40) |

The green body typically contains 50–65 % of the theoretical density. Organic binders, plasticizers and dispersants are burned out slowly (at 1–2 K/min through 200–500 °C) before sintering, or their gases will crack the part.

### The driving force for sintering

**Sintering** consolidates a powder compact by atomic transport at 0.6–0.8 of the absolute melting temperature. Its driving force is the reduction of interfacial energy (Chapter 6): for 1 μm alumina (about 1.5 m²/g, $\gamma_{sv}\approx1$ J/m²) only about 1.5 J/g, which is why sintering needs high temperatures and fine powders. Locally it appears as a curvature-driven chemical-potential difference (Gibbs–Thomson) that moves atoms from convex surfaces and grain boundaries to the concave necks.

### Stages and mechanisms

Sintering is described in three geometric stages (Figure 17.1):

1. **Initial stage**: necks form between particles; the neck radius grows as a power of time; linear shrinkage up to about 3–5 %.
2. **Intermediate stage**: pores form a continuous, interconnected network along grain edges; most densification occurs here, from about 65 % to about 92 % of theoretical density.
3. **Final stage**: above about 92 % density the pore channels pinch off into isolated pores at grain corners; the last pores close slowly, and grain growth competes with densification.

<!-- FIGURE 17.1 | figures/ch17/fig-17-1-sintering-stages.png | schematic | Stages and mechanisms of solid-state sintering, and relative density versus sintering time for solid-state and liquid-phase sintering. | Content: top row: three panels for initial (two spheres with growing neck, labelled neck radius x and particle radius a), intermediate (polyhedral grains with continuous pore channels along edges), final (isolated pores at grain corners, some trapped inside grains after boundary breakaway). Middle panel: two-particle neck with arrows for six transport paths: (1) surface diffusion, (2) lattice diffusion from surface, (3) evaporation–condensation — labelled "non-densifying, neck grows, no shrinkage"; (4) grain-boundary diffusion, (5) lattice diffusion from grain boundary, (6) plastic/viscous flow — labelled "densifying, centres approach". Bottom: x-axis time 0–4 h at temperature, y-axis relative density 0.55–1.00; solid-state curve rising from 0.55 to ~0.97 with stage boundaries marked at ~0.65 and ~0.92; liquid-phase curve rising rapidly (rearrangement) then solution–precipitation then slowly to 0.99. -->

Matter can move by several paths. **Surface diffusion**, **evaporation–condensation** and **lattice diffusion from the particle surface** move atoms from one part of the pore surface to another; they grow the necks and round the pores but do not bring particle centres together, so they cause no shrinkage. **Grain-boundary diffusion** and **lattice diffusion from the grain boundary** remove atoms from the boundary between particles and deposit them at the neck; particle centres approach, and the compact shrinks and densifies. Viscous flow plays the same densifying role in glasses. Whether a powder densifies or merely coarsens depends on which paths dominate. A high ratio of grain-boundary to surface diffusivity favours densification; fast surface diffusion at low temperature wastes the driving force by coarsening the particles without shrinkage, which is why fast heating rates sometimes give denser products.

Herring's scaling law states that if all particle sizes $G$ are scaled by a factor $\lambda$, the time to achieve the same geometric change scales as $\lambda^m$, with $m=2$ for viscous flow, 3 for lattice diffusion and 4 for grain-boundary diffusion. Halving the particle size therefore shortens the sintering time by a factor of 8 for lattice diffusion and 16 for grain-boundary diffusion, or allows sintering at a lower temperature. This is the main reason ceramic processing has moved to sub-micrometre and nanometre powders.

> **Status of the principle: Herring scaling law**
> *Derived.* Follows from dimensional analysis of curvature-driven transport when the geometry is self-similar and a single mechanism operates; real powders with size distributions, agglomerates and changing mechanisms follow it only approximately.

### Grain growth and the role of dopants

In the final stage, a boundary that breaks away from its pores strands them inside grains, far from any vacancy sink, and they never close. Coble's classic remedy for alumina was 0.05–0.25 % MgO, which segregates to boundaries, slows them, and lets the pores be eliminated, giving translucent alumina for lamp envelopes; pinning particles (Zener pinning, Chapter 10) do the same.

**Worked example — Shrinkage allowance for a sintered alumina part.** A seal ring must be 50.0 mm in outer diameter after sintering to 98 % of theoretical density. The pressed green body has 55 % of theoretical density. Mass is conserved and, if shrinkage is isotropic, the linear dimension scales as the cube root of the density ratio:

$$
\frac{L_f}{L_g}=\left(\frac{\rho_g}{\rho_f}\right)^{1/3}=\left(\frac{0.55}{0.98}\right)^{1/3}=0.825
$$

The linear shrinkage is 17.5 %, and the green part must be pressed (or machined in the green state) to $50.0/0.825=60.6$ mm. A green-density variation of ±1 % across the part (typical of uniaxial pressing, where die-wall friction leaves the corners denser than the centre) changes the local shrinkage by about ±0.3 percentage points, which on a 60 mm part is about ±0.2 mm of distortion. This is why precision ceramic parts are often isostatically pressed, ground after sintering with diamond tools, and why grinding can account for half the cost of a technical ceramic component.

### Liquid-phase sintering

Many ceramics (and cemented carbides, Chapter 38) are sintered with a small amount of liquid that wets the solid. The liquid speeds sintering in three overlapping stages: **rearrangement**, as capillary forces pull particles into closer packing; **solution–precipitation**, in which small particles and contact points dissolve in the liquid and the material reprecipitates on larger grains, flattening contacts and bringing grain centres together; and **solid-state skeleton** densification once the grains have formed a rigid network. Diffusion through a liquid is orders of magnitude faster than through a solid, so liquid-phase sintering works at lower temperatures and for materials such as Si₃N₄ and SiC that would hardly sinter otherwise. The price is a residual grain-boundary glass that softens at high temperature and reduces creep and slow-crack-growth resistance, as in 96 % alumina and in silicon nitride above about 1200 °C. The dihedral angle and wetting behaviour set by interfacial energies (Chapter 6) decide whether the liquid penetrates the grain boundaries.

### Pressure-assisted sintering

Pressure adds a driving force far larger than the capillary one. **Hot pressing** (20–50 MPa in graphite dies), **hot isostatic pressing** (gas at 100–200 MPa, also used to close residual pores after sintering) and **spark plasma sintering** (pulsed current through die and powder, densifying in minutes) reach full density with little grain growth, at a cost reserved for bearing balls, armour, transparent ceramics and cutting tools.

---

## 17.4 Mechanical behaviour of ceramics

### Strength is set by flaws

Chapter 14 showed that the fracture of a brittle solid is governed by linear-elastic fracture mechanics. A crack of depth $a$ in a surface loaded in tension fails when the stress-intensity factor reaches the fracture toughness:

$$
\sigma_f=\frac{K_{IC}}{Y\sqrt{\pi a}}
$$

with $Y\approx1.1$–$1.3$ for surface cracks. With $K_{IC}=4$ MPa m$^{1/2}$, alumina with a 30 μm flaw fails at about 370 MPa, and with a 300 μm flaw at about 120 MPa. Because $K_{IC}$ of ceramics is only 1–10 MPa m$^{1/2}$ (against 30–200 for structural metals), flaws of tens of micrometres control the strength. These flaws come from processing (pores, agglomerates, inclusions, large grains) and from machining and handling (grinding cracks, chips, contact damage). The theoretical strength of the bonds, about $E/10$, is never approached in bulk ceramics.

Three consequences follow. Ceramics are much stronger in **compression** (typically 5–15 times their tensile strength), because compressive stresses close flaws and failure requires many cracks to grow and link; ceramics are used as columns, armour faces and bearing balls, where loads are mainly compressive. Their tensile strength is **variable**, because the largest flaw differs from part to part. And it depends on **specimen size and stress distribution**, because a larger stressed volume is more likely to contain a large flaw.

### Weibull statistics

The weakest-link statistics of Chapter 14 describe this variability. The probability that a component of volume $V$ fails at or below a uniform stress $\sigma$ is

$$
P_f=1-\exp\left[-\frac{V}{V_0}\left(\frac{\sigma}{\sigma_0}\right)^m\right]
$$

where $\sigma_0$ is the characteristic strength of the reference volume $V_0$ and $m$ is the **Weibull modulus**. A large $m$ means a narrow strength distribution: $m$ is 5–10 for traditional ceramics and glass as used, 10–20 for good technical ceramics, 20–30 for the best silicon nitride, and 30–100 for metals. Data are plotted as $\ln\ln[1/(1-P_f)]$ against $\ln\sigma$, which gives a straight line of slope $m$ (Figure 17.2). For non-uniform stress fields, such as a bend test, $V$ is replaced by an **effective volume** that weights each element by $(\sigma/\sigma_{\max})^m$; for a three-point bend bar it is only a few percent of the specimen volume.

<!-- FIGURE 17.2 | figures/ch17/fig-17-2-weibull-plot.png | plot | Weibull plot of bend-strength data for two aluminas with Weibull moduli 10 and 20, and the predicted strength reduction for a component with 100 times the effective volume. | Content: x-axis ln(σ / MPa) spanning σ = 150–600 MPa (secondary top axis in MPa); y-axis ln ln(1/(1−Pf)) from −7 to 2, with secondary right axis Pf at 0.001, 0.01, 0.1, 0.5, 0.9, 0.99. Line A: m = 10, σ0 = 400 MPa (passes through ln ln = 0 at σ = 400). Line B: m = 20, σ0 = 400 MPa. ~25 scattered data points around each line. Dashed line parallel to A shifted to lower stress by factor 0.631 labelled "component, 100× effective volume". Mark worked-example points: Pf = 1e-4 (ln ln ≈ −9.2 — show with an arrow off-scale or extend y-axis to −10) at 159 MPa (test volume) and 100 MPa (component). -->

**Worked example — From test bars to a design stress.** Bend bars of an alumina have a characteristic strength $\sigma_0=400$ MPa (63.2 % failure probability) and $m=10$ for their effective volume. What stress gives a failure probability of $10^{-4}$, first for a part with the same effective volume and then for a part with 100 times the effective volume?

For the same volume, solving the Weibull equation for $\sigma$:

$$
\sigma=\sigma_0\left[-\ln(1-P_f)\right]^{1/m}=400\times(1.0\times10^{-4})^{0.1}=400\times0.398=159\ \mathrm{MPa}
$$

For 100 times the volume, the stress for equal failure probability falls by $100^{-1/m}=100^{-0.1}=0.631$, to 100 MPa. A designer who used the mean bend strength (about 380 MPa) would have been off by a factor of nearly four. With $m=20$ the same two steps give 252 MPa and 200 MPa; doubling the Weibull modulus is worth as much as doubling the mean strength. Volume scaling assumes the same flaw population in test bar and part, which fails when the part's surfaces are machined differently or when different flaws (edge chips, internal pores) dominate.

> **Status of the principle: Weibull size scaling of strength**
> *Approximate.* Follows from weakest-link statistics with a single flaw population and a power-law distribution of flaw strengths; it fails when several flaw populations coexist, when flaws are surface- rather than volume-distributed (use effective area), or when R-curve behaviour or slow crack growth changes the failure condition.

**Proof testing** loads every part above its service stress so that those with large flaws break in the test, truncating the flaw distribution, provided slow crack growth does not enlarge flaws afterwards.

### Slow crack growth and thermal shock

Silicate glasses and many oxides suffer **slow crack growth** in the presence of water, which reacts with stressed bonds at the crack tip, so cracks grow below $K_{IC}$ at a velocity $v\approx AK_I^n$, with $n$ about 15–20 for soda-lime glass, 30–50 for alumina and above 50 for silicon nitride. Long-term design stresses for glass are therefore a third or less of short-term strengths.

A sudden temperature change also produces stress. A surface cooled suddenly by $\Delta T$ is constrained by the hot interior and develops a tensile stress up to $E\alpha\Delta T/(1-\nu)$ (Chapter 24). Setting this equal to the fracture strength gives the critical temperature drop for severe quenching,

$$
\Delta T_c=\frac{\sigma_f(1-\nu)}{E\alpha}
$$

With typical values this is about 90 K for 99.5 % alumina, 230 K for sintered SiC, about 590 K for silicon nitride, 60 K for soda-lime glass, 190 K for borosilicate glass and about 1000 K for fused silica. The ranking explains why Si₃N₄ is used for turbocharger rotors and molten-metal handling, borosilicate for laboratory glassware and cookware, and fused silica for furnace windows and crucibles.

### Toughening ceramics

Because strength is $K_{IC}$ divided by flaw size, ceramics are strengthened in two ways: by **reducing flaw size** (clean powders, colloidal processing, fine grains, careful machining) and by **raising toughness**. Chapter 14 introduced the toughening mechanisms; in ceramic engineering they appear as follows:

| Mechanism | How it works | Example materials | $K_{IC}$ (MPa m$^{1/2}$) |
|---|---|---|---|
| None (single-phase, fine grains) | Crack follows the cleanest path | Fine-grained alumina, glass | 0.7–4 |
| Crack deflection and grain bridging | Elongated or large grains force the crack to tilt and leave intact ligaments behind the tip | β-Si₃N₄, coarse-grained alumina, SiC with liquid-phase sintering | 5–10 |
| Transformation toughening | Stress-induced t→m transformation of ZrO₂ shields the crack tip | 3Y-TZP, Mg-PSZ, zirconia-toughened alumina | 5–15 |
| Microcracking | A process zone of microcracks around the crack reduces local stress | ZrO₂-containing composites, some aluminas | 4–8 |
| Fibre bridging and pull-out | Fibres with weak interfaces bridge the crack over millimetres | SiC/SiC, C/SiC, oxide/oxide CMCs | 15–30 (R-curve) |

Shielding mechanisms produce a **rising R-curve**, which makes strength less sensitive to flaw size and raises the Weibull modulus, the real engineering goal; CMCs become quasi-ductile and notch-insensitive (Chapter 23).

---

## 17.5 Glass formation

### Glasses as frozen liquids

A **glass** is an amorphous solid that shows a glass transition. Any liquid can in principle become a glass if it is cooled fast enough to avoid crystallization; a good glass-former is simply a liquid in which crystallization is very slow. On cooling, a crystallizing liquid shows a discontinuous drop in volume at the melting point. A glass-forming liquid instead continues along the liquid line as a **supercooled liquid**, becoming steadily more viscous, until at the **glass transition temperature** $T_g$ its structure can no longer rearrange on the time scale of cooling. Below $T_g$ the structure is frozen and the volume follows a line parallel to that of the crystal (Figure 17.3). The temperature at which the frozen structure would have been the equilibrium liquid is the **fictive temperature**; faster cooling freezes in a higher fictive temperature, a more open structure and a slightly lower density, which is why the "glass transition temperature" depends on the cooling rate.

<!-- FIGURE 17.3 | figures/ch17/fig-17-3-volume-temperature.png | plot | Specific volume versus temperature for a glass-forming liquid, showing crystallization at Tm and the glass transition for slow and fast cooling. | Content: x-axis temperature (schematic, labelled Tg,slow, Tg,fast, Tm), y-axis specific volume (arbitrary). Liquid line from top right sloping down; at Tm a vertical drop to the crystal line (lower slope) labelled "crystallization". Supercooled liquid continues past Tm; a fast-cooled glass leaves it at Tg,fast (higher), a slow-cooled glass at Tg,slow (lower); both glass lines parallel to the crystal line. Label fictive temperatures Tf at the intersections of the glass lines extrapolated to the liquid line. Shade the region between Tm and Tg labelled "supercooled liquid". Inset: TTT curve with nose, critical cooling rate tangent line Rc; labels "SiO2: Rc ~ 1e-4 K/s", "soda-lime: ~1e-2 K/s", "metallic glass: 1e2–1e6 K/s". -->

The kinetic criterion is quantified by a time–temperature–transformation curve for crystallization (Chapter 9). The **critical cooling rate** that just misses its nose is of order $10^{-4}$ K/s for silica, so silica glass forms even in massive bodies, $10^{-2}$–$10^{-1}$ K/s for common silicate glasses, and $10^2$–$10^6$ K/s for metallic glasses (Chapter 9). A liquid forms a glass easily when its viscosity at the melting point is high (silica: about $10^{5}$–$10^{6}$ Pa s at 1723 °C, against $10^{-3}$ Pa s for water or liquid metals), when crystallization requires large rearrangements of a connected network, and when the composition is near a deep eutectic, where the liquid is stable to low temperature.

> **Status of the principle: Kinetic criterion for glass formation**
> *Fundamental.* Glass formation is avoidance of crystallization; whether a liquid vitrifies is decided by comparing the cooling rate with the nucleation and growth rates, which follow from classical nucleation theory (Chapter 9).

### Zachariasen's rules

Why do some oxides form glasses easily and others not at all? In 1932 Zachariasen proposed that a glass has the same local building blocks as the crystal, the same coordination polyhedra with the same bond lengths, but connected into a **continuous random network** without long-range periodicity (Figure 17.4). For an oxide A$_m$O$_n$ to form such a network with an energy comparable to the crystal's, he argued, four conditions should hold:

1. Each oxygen is linked to no more than two cations A.
2. The coordination number of oxygen around A is small, 3 or 4.
3. The oxygen polyhedra share corners, not edges or faces.
4. At least three corners of each polyhedron are shared (for a three-dimensional network).

SiO₂ (SiO₄ tetrahedra), GeO₂, B₂O₃ (BO₃ triangles) and P₂O₅ satisfy the rules and are the **network formers**; MgO, CaO and Na₂O, with octahedral coordination and edge sharing in their crystals, do not.

> **Status of the principle: Zachariasen's rules**
> *Empirical.* Structural criteria inferred from the crystal chemistry of known glass-formers; they successfully classify the oxides but say nothing about kinetics, and they do not apply to metallic, chalcogenide or molecular glasses.

<!-- FIGURE 17.4 | figures/ch17/fig-17-4-zachariasen-network.png | schematic | Two-dimensional representations of crystalline silica, silica glass (continuous random network) and a sodium silicate glass with non-bridging oxygens. | Content: three panels using the classic 2D analogue with triangles (A2O3-type) for clarity. (a) Crystal: ordered hexagonal rings of corner-sharing triangles. (b) Glass: same triangles, same bond lengths, but rings of 5, 6, 7, 8 members, no periodicity. (c) Modified glass: network broken at several points, non-bridging oxygens (filled small circles, labelled NBO) facing Na+ ions (large open circles labelled Na+) located in holes of the network. Legend: small black dot = network cation (Si/B), open small circle = bridging oxygen, filled = non-bridging oxygen. -->

### Network formers, modifiers and intermediates

Pure silica glass is difficult to make: it must be melted above 2000 °C. Adding alkali and alkaline-earth oxides, the **network modifiers**, breaks Si–O–Si bridges. Each Na₂O contributes an oxygen that converts one bridging oxygen into two **non-bridging oxygens** (NBOs), each charge-balanced by a nearby Na⁺:

$$
\equiv\mathrm{Si{-}O{-}Si}\equiv\ +\ \mathrm{Na_2O}\ \rightarrow\ \equiv\mathrm{Si{-}O^-\ Na^+}\ \ \ \mathrm{Na^+\ {}^-O{-}Si}\equiv
$$

The network is depolymerized: viscosity falls by orders of magnitude, the melting temperature drops to 1400–1600 °C, the thermal expansion rises, and the chemical durability falls (pure sodium silicate is "water glass", soluble in water). Alkaline-earth oxides (CaO, MgO) restore durability because the doubly charged ions bind two NBOs and are less mobile. A simple measure of depolymerization is the number of NBOs per tetrahedron, NBO/T. For a soda-lime glass of molar composition 74 SiO₂–16 Na₂O–10 CaO, each mole of modifier oxide creates two NBOs, so NBO/T $=2(16+10)/74=0.70$; on average each tetrahedron has 3.3 bridging corners, still a connected network. **Intermediates** such as Al₂O₃, TiO₂, ZnO and PbO can enter the network (Al as AlO₄⁻ tetrahedra charge-balanced by an alkali ion, which consumes NBOs and repolymerizes the network) or act as modifiers.

| Glass | Typical composition (wt%) | Key properties | Uses |
|---|---|---|---|
| Fused silica | ~100 SiO₂ | CTE 0.55 × 10⁻⁶ K⁻¹; softening ~1600 °C; UV-transparent | Furnace tubes, lithography optics, optical fibres (doped), crucibles |
| Soda-lime (float, container) | 72 SiO₂, 14 Na₂O, 9 CaO, 4 MgO, 1 Al₂O₃ | CTE 9.0 × 10⁻⁶ K⁻¹; cheap, easily melted | Windows, bottles, jars, about 90 % of all glass |
| Borosilicate | 81 SiO₂, 13 B₂O₃, 4 Na₂O, 2 Al₂O₃ | CTE 3.3 × 10⁻⁶ K⁻¹; chemical durability; thermal-shock resistance | Laboratory ware, cookware, pharmaceutical vials, fire-resistant glazing |
| Alkali aluminosilicate | ~60 SiO₂, 15–20 Al₂O₃, 12–14 Na₂O, 3–5 MgO, K₂O | Open network for fast ion exchange | Phone and display cover glass (chemically strengthened) |
| E-glass | 54 SiO₂, 14 Al₂O₃, 22 CaO+MgO, 7–10 B₂O₃, < 1 alkali | Low alkali, good electrical insulation | Reinforcing fibres (Chapter 22), circuit-board laminates |
| Lead crystal | 55–65 SiO₂, ≥ 24 PbO, K₂O | Refractive index ~1.55–1.57, high dispersion | Tableware, decorative and radiation-shielding glass |
| Non-oxide glasses | Chalcogenides (As–Se, Ge–Sb–Te), fluorides (ZrF₄–BaF₂), metallic glasses | Infrared transparency; phase-change memory; high strength | IR optics, rewritable memory (Chapter 26), springs and casings (Chapter 9) |

Boron is an unusual former: alkali first converts BO₃ triangles into BO₄⁻ tetrahedra, strengthening the network, and only beyond a certain alkali/boron ratio creates NBOs (the **boron anomaly**), one reason for the low expansion and durability of borosilicates.

---

## 17.6 Glass properties and processing

### Viscosity and the reference points

The viscosity of a glass-forming melt changes continuously by about 15 orders of magnitude between melting and room temperature, and every glass process is defined by viscosity rather than by temperature. The industry uses **reference points**:

| Reference point | Viscosity (Pa s) | Meaning | Soda-lime (°C) | Borosilicate (°C) | Fused silica (°C) |
|---|---|---|---|---|---|
| Melting | ~10 | Fining and homogenizing the melt | ~1450 | ~1600 | > 2000 |
| Working point | $10^{3}$ | Gobs formed in pressing and blowing | ~1005 | ~1250 | — |
| Softening (Littleton) point | $10^{6.6}$ | Glass deforms under its own weight | ~726 | ~821 | ~1600 |
| Annealing point | $10^{12}$ | Internal stresses relax in minutes | ~548 | ~560 | ~1100 |
| Strain point | $10^{13.5}$ | Stresses relax in hours; glass rigid for practical purposes | ~511 | ~510 | ~1000 |

Values are typical; they shift by tens of kelvin with composition within each family.

Over this range, the viscosity of most silicate melts is described well by the **Vogel–Fulcher–Tammann** (VFT) equation,

$$
\log_{10}\eta=A+\frac{B}{T-T_0}
$$

where $A$, $B$ and $T_0$ are fitted constants. For a typical soda-lime glass, with $T$ in °C and $\eta$ in Pa s, $A=-4.57$, $B=6370$ °C and $T_0=160$ °C fit the four reference points to within about 0.15 in $\log_{10}\eta$ (Figure 17.5). The divergence at $T_0$, well below $T_g$, is never reached because the melt falls out of equilibrium at $T_g$. Silica follows a nearly Arrhenius law (small $T_0$), the behaviour Angell called a **strong** liquid; depolymerized silicates, molecular liquids and polymers depart further from Arrhenius behaviour and are **fragile**. Fragility explains why soda-lime glass has a long "working range" in which it can be shaped, and why polymers soften over a narrow temperature range (the WLF equation of Chapter 20 is equivalent in form to VFT).

> **Status of the principle: Vogel–Fulcher–Tammann equation**
> *Empirical.* A three-parameter fit to viscosity data; it is accurate from the melting range to near $T_g$ for most oxide glasses, but it is not reliable for extrapolation below $T_g$, where the glass is out of equilibrium, and alternative forms (Adam–Gibbs, MYEGA) fit some data better.

<!-- FIGURE 17.5 | figures/ch17/fig-17-5-glass-viscosity.png | plot | Viscosity versus temperature for soda-lime, borosilicate and fused silica glasses with the reference points and forming, annealing and tempering windows. | Content: x-axis temperature 400–1800 °C; y-axis log10 viscosity (Pa s) 0–18. Soda-lime: VFT curve log10 η = −4.57 + 6370/(T − 160), passing through strain 511 °C (13.5), annealing 548 °C (12), softening 726 °C (6.6), working 1005 °C (3). Borosilicate: curve through strain 510, annealing 560, softening 821, working 1252 °C. Fused silica: near-Arrhenius curve through strain ~1000 °C, annealing ~1100 °C, softening ~1600 °C. Horizontal dashed lines at log η = 13.5, 12, 6.6, 3 labelled strain, annealing, softening, working points. Shade bands: "forming (pressing, blowing, float)" between 3 and 6.6; "annealing range" between 12 and 13.5; mark "tempering quench start ~620–650 °C" on the soda-lime curve; mark the worked-example points 500 °C (14.2) and 450 °C (17.4). -->

### Annealing

A formed article cools unevenly, freezing in **residual stresses** that can crack it spontaneously when cut or scratched. **Annealing** removes them: the article is held at the annealing point, where stresses relax by viscous flow, then cooled slowly through the strain point, and faster afterwards.

**Worked example — Why the annealing point is where it is.** Treat the glass as a Maxwell viscoelastic body (Chapter 14) with shear modulus $G\approx30$ GPa. Its stress-relaxation time is $\tau=\eta/G$. At the annealing point, $\eta=10^{12}$ Pa s, so $\tau=10^{12}/(3\times10^{10})=33$ s: stresses decay in minutes. At 500 °C, the VFT equation for soda-lime glass gives $\log_{10}\eta=-4.57+6370/(500-160)=14.17$, so $\eta=1.5\times10^{14}$ Pa s and $\tau\approx5000$ s, about 1.4 h. At 450 °C, $\log_{10}\eta=17.40$ and $\tau\approx8.4\times10^{6}$ s, about 97 days. Below the strain point, cooling can be fast because no stress can relax in the time of cooling, and therefore no new stress pattern is frozen in from viscous flow; the transient thermal stresses that remain must simply be kept below the strength. A container-glass lehr accordingly holds bottles near 550 °C for a few minutes, cools them at a few kelvin per minute to about 480 °C, and then cools them rapidly.

### Thermal tempering

Glass fails from surface flaws in tension, so a surface in permanent compression must be unloaded before a flaw can open. In **thermal tempering**, a soda-lime sheet at least 3 mm thick is heated to about 620–650 °C and quenched on both faces with air jets. The surfaces stiffen first; the still-fluid interior then contracts and pulls them into compression, ending itself in tension. The profile is close to a parabola: for fully tempered glass, 90–150 MPa of surface compression balanced by a mid-plane tension of half that value, crossing zero at about 21 % of the thickness from each face (Figure 17.6). The characteristic bending strength rises from about 45 MPa (annealed float) to 120 MPa or more, and a broken sheet dices into small, blunt fragments: **safety glass** for vehicles, doors and façades. It cannot be cut afterwards, and nickel sulfide inclusions occasionally break it spontaneously, hence **heat-soak testing** of façade glass.

### Chemical strengthening

Thin glass cannot be thermally tempered, because the temperature difference between surface and centre during a quench is too small. **Chemical strengthening** by ion exchange works for any thickness. The glass is immersed in molten KNO₃ at 380–450 °C for hours; Na⁺ ions in the surface exchange with K⁺ ions from the salt, and because the glass is too cold for the network to relax, the larger K⁺ ions are "stuffed" into sites sized for Na⁺, creating a compressive stress of 600–900 MPa in a layer 10–100 μm deep (the depth of layer, DOL). Alkali aluminosilicate glasses are designed for this process: aluminium opens the network and speeds interdiffusion (Chapter 8). The compression is balanced by a small central tension; for a triangular compressive profile with surface stress CS and depth DOL in a sheet of thickness $t$, force balance gives a central tension of approximately $\mathrm{CS}\cdot\mathrm{DOL}/(t-2\,\mathrm{DOL})$, or about 45 MPa for CS = 700 MPa, DOL = 40 μm and $t=0.7$ mm. The central tension must be kept below a frangibility limit, or the glass shatters violently when penetrated.

<!-- FIGURE 17.6 | figures/ch17/fig-17-6-residual-stress-profiles.png | plot | Residual stress through the thickness of a thermally tempered soda-lime sheet and a chemically strengthened aluminosilicate cover glass. | Content: two panels. (a) Thermally tempered 6 mm sheet: x-axis position z/t from 0 to 1, y-axis stress −120 to +60 MPa (compression negative); parabola with −100 MPa at both surfaces, +50 MPa at mid-plane, zero crossings at z/t = 0.211 and 0.789. (b) Chemically strengthened 0.7 mm cover glass: x-axis depth from surface 0–700 μm, y-axis stress −750 to +100 MPa; linear (triangular) profile from −700 MPa at surface to 0 at 40 μm on each side, constant central tension +45 MPa between. Dashed horizontal line at 0. Annotate a 20 μm surface flaw on each panel with arrows: "flaw inside compressive layer". -->

**Worked example — How much does strengthening help against a scratch?** A cover glass has a surface flaw 20 μm deep. With $K_{IC}=0.75$ MPa m$^{1/2}$ and $Y=1.12$, the annealed glass fails at

$$
\sigma_f=\frac{0.75}{1.12\sqrt{\pi\times20\times10^{-6}}}=84.5\ \mathrm{MPa}
$$

If the flaw lies within a thermally tempered layer with about 100 MPa of surface compression, the applied stress must first cancel the compression, so failure needs roughly $84.5+100\approx185$ MPa. If it lies within a chemically strengthened layer with 700 MPa of compression and a 40 μm depth of layer, failure needs roughly $84.5+700\approx785$ MPa, nearly ten times the annealed value. The estimate treats the residual stress as uniform over the flaw depth, which overstates the benefit for flaws approaching the depth of layer; a flaw deeper than the layer reaches the tensile core and gains little. This is the engineering logic of cover-glass development: deeper compressive layers to protect against the sharp contacts of a phone dropped on concrete, which create flaws of tens of micrometres.

> **Status of the principle: Superposition of residual and applied stress at a flaw**
> *Approximate.* Linear-elastic superposition of stress-intensity factors is exact, but treating the residual stress as uniform over the crack depth is an approximation; proper analysis integrates the residual-stress profile with a weight function.

---

## 17.7 Glass-ceramics

**Glass-ceramics** combine the formability of glass with the properties of a polycrystal. A glass is formed by any glass process, then crystallized in the solid state into a pore-free ceramic, 50–95 % crystalline with grains of 0.05–1 μm. Crystallization must start everywhere at once rather than from the surface, so a few percent of **nucleating agents** (TiO₂, ZrO₂, P₂O₅) precipitate nanocrystals during a hold just above $T_g$, where nucleation peaks, and a second, hotter hold, where growth peaks, grows the main phase on them (Chapter 9).

| System | Main crystalline phase | Key property | Applications |
|---|---|---|---|
| Li₂O–Al₂O₃–SiO₂ (LAS), transparent | β-quartz solid solution (~70 %), grains ~50 nm | CTE ≈ 0 ± 0.1 × 10⁻⁶ K⁻¹ (to ± 0.02 × 10⁻⁶ in mirror grades); transparent | Cooktop panels, fire-place windows, telescope mirror blanks, ring-laser gyroscopes |
| LAS, opaque | β-spodumene solid solution | CTE ~1 × 10⁻⁶ K⁻¹; white, strong | Oven-to-freezer cookware |
| MgO–Al₂O₃–SiO₂ (MAS) | Cordierite | Low dielectric loss, low CTE, high strength | Missile radomes |
| Li₂O–SiO₂ | Lithium disilicate, interlocking needles | Flexural strength 360–500 MPa, $K_{IC}$ ~2.5–3 MPa m$^{1/2}$, tooth-like translucency | Dental crowns and bridges |
| K₂O–MgO–Al₂O₃–SiO₂–F | Fluorophlogopite mica plates | Machinable with ordinary tools | Machinable insulators and fixtures |
| CaO–P₂O₅–SiO₂ | Apatite, wollastonite | Bonds to bone | Bone substitutes (Chapter 31) |

The near-zero expansion of LAS glass-ceramics is a structural trick. The β-quartz and β-eucryptite crystals have a *negative* expansion coefficient along their $c$ axis, and the composite of crystals with negative expansion and residual glass with positive expansion can be tuned to zero over a wide temperature range. A cooktop can then be heated locally to 700 °C while the edge stays cold without cracking; a telescope mirror does not change shape as night falls.

---

## 17.8 Refractories

**Refractories** line furnaces, kilns, reactors and ladles: non-metallic materials that keep their shape and integrity above about 1500 °C. About 60–70 % of world consumption goes to iron- and steelmaking. Unlike technical ceramics they are mostly coarse-grained and porous (10–25 %), aggregates bonded by a fine matrix, judged by survival against molten metal, slag and hot gas rather than by room-temperature strength.

### Classes

Refractories are traditionally classified by their chemistry, because the key requirement is chemical compatibility with the slag or melt they contain. An acidic (silica-rich) refractory in contact with a basic (CaO-, MgO-rich) slag forms low-melting silicates and dissolves rapidly, and vice versa.

| Class | Main constituents | Typical service | Remarks |
|---|---|---|---|
| Acidic: silica | > 93 % SiO₂ (tridymite, cristobalite) | Coke-oven walls, glass-furnace crowns | Rigid almost to melting, but quartz/cristobalite inversions make it crack if cycled below ~600 °C |
| Acidic: fireclay and high-alumina | 25–45 % Al₂O₃ (fireclay); 50–90 % Al₂O₃ (bauxite, mullite, corundum) | Ladles, blast-furnace stoves, kiln linings, aluminium furnaces | The Al₂O₃–SiO₂ diagram and mullite set refractoriness (Chapter 7) |
| Basic: magnesia and magnesia–carbon | MgO (periclase), 5–20 % graphite, metallic antioxidants | Steel converters (BOF), electric-arc furnaces, ladle slag lines | Graphite is not wetted by slag and raises thermal-shock resistance |
| Basic: magnesia–spinel, dolomite | MgO with MgAl₂O₄; CaO·MgO | Cement-kiln burning zones; secondary steelmaking | Chrome-free replacements for magnesia–chrome |
| Neutral and special | Fused-cast Al₂O₃–ZrO₂–SiO₂ (AZS), SiC, carbon, zircon | Glass-tank walls, blast-furnace hearths, aluminium cells | AZS resists glass corrosion; carbon resists molten iron |
| Insulating | Insulating firebrick, ceramic fibre, microporous silica | Backing layers, kiln cars, heat-treatment furnaces | Porosity 50–90 %; conductivity 0.03–0.5 W m⁻¹ K⁻¹ |

Refractories are supplied as fired **shaped** bricks or, increasingly, as **monolithics** (castables, gunning and ramming mixes) placed and fired in situ; low-cement castables with reactive alumina and microsilica install fast and have fewer joints for slag to attack.

### Performance

Refractories are tested for **refractoriness** (pyrometric cone equivalent), **refractoriness under load** and creep, **thermal-shock resistance**, **slag corrosion**, conductivity and abrasion. A good refractory does not avoid cracking; it limits crack propagation. Coarse aggregates, microcracks and graphite flakes deflect cracks and store little elastic energy, the opposite philosophy to a fine-grained technical ceramic.

**Worked example — A two-layer furnace lining.** A furnace wall has a hot face at 1400 °C and an outer steel shell at 60 °C. It is built from 230 mm of dense high-alumina brick ($k=1.5$ W m⁻¹ K⁻¹) backed by 115 mm of insulating firebrick ($k=0.25$ W m⁻¹ K⁻¹). In steady state the same heat flux crosses both layers in series:

$$
q=\frac{T_{\mathrm{hot}}-T_{\mathrm{cold}}}{L_1/k_1+L_2/k_2}=\frac{1400-60}{0.230/1.5+0.115/0.25}=\frac{1340}{0.153+0.460}=2.18\ \mathrm{kW\,m^{-2}}
$$

The temperature at the interface is $1400-q\,L_1/k_1=1400-2185\times0.153=1065$ °C. The insulating brick must therefore be rated for at least about 1100 °C (a grade-23 insulating firebrick, rated to 1260 °C, suffices); it could not be placed at the hot face, where it would shrink and be eroded. A wall of the same total thickness built entirely of dense brick would lose $1340/(0.345/1.5)=5.8$ kW m⁻², 2.7 times as much. Real conductivities rise or fall with temperature and the shell temperature depends on external convection, so furnace designers integrate $k(T)$ and iterate, but the two-layer logic (a dense, corrosion-resistant hot face backed by a light insulating layer) is universal.

---

## 17.9 Functional ceramics

Much of the economic value of ceramics lies not in their mechanical properties but in their electrical, magnetic, optical and electrochemical functions, which depend on point defects, domain structures and band gaps rather than on flaws. They are treated in Part VI (Chapters 24–28) and in Chapter 32; the table below is a map. Their processing is the powder processing of Section 17.3, often with extreme control of particle size, dopant distribution and layer thickness.

| Functional ceramic | Function | Key material | Where it is treated |
|---|---|---|---|
| Multilayer ceramic capacitors | High permittivity, ferroelectric | BaTiO₃ with dopants, layers ~0.5–1 μm | Chapter 25 |
| Piezoelectric actuators, sensors, ultrasound | Piezoelectricity | Pb(Zr,Ti)O₃ (PZT), lead-free (K,Na)NbO₃ | Chapters 25 and 29 |
| Soft and hard ferrites | Ferrimagnetism | MnZn, NiZn ferrites; BaFe₁₂O₁₉, SrFe₁₂O₁₉ | Chapter 27 |
| Oxygen sensors, SOFC electrolytes | Oxygen-ion conduction | Y- or Sc-stabilized ZrO₂, Gd-doped CeO₂ | Chapters 25 and 32 |
| Solid-state battery electrolytes | Li-ion conduction | Li₇La₃Zr₂O₁₂ (LLZO), sulfide glasses | Chapter 32 |
| Varistors and thermistors | Grain-boundary barriers; semiconducting oxides | ZnO–Bi₂O₃; Mn–Ni–Co spinels (NTC); doped BaTiO₃ (PTC) | Chapter 25 |
| Transparent conductors | Degenerate semiconduction | Sn-doped In₂O₃ (ITO), Al-doped ZnO | Chapters 26 and 28 |
| Substrates and heat spreaders | Insulation with high thermal conductivity | Al₂O₃, AlN, Si₃N₄ | Chapter 24 |
| Phosphors, laser hosts, transparent armour | Luminescence; transparency | Ce:YAG, Nd:YAG, spinel, AlON | Chapter 28 |
| Thermal barrier coatings | Low thermal conductivity | 7YSZ, rare-earth zirconates | Chapters 16, 24 and 33 |

> **Boundary.** The EEE-specific treatment of dielectric, piezoelectric, magnetic and substrate ceramics, including capacitor and package design, lives in the *Materials Core (EEE)* book.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How were Griffith fracture, R-curves, transformation toughening and Weibull statistics derived? | Chapter 14 (back reference) |
| How do the crystal structures and phase diagrams of ceramics follow from bonding and thermodynamics? | Chapters 2 and 7 (back references) |
| How do nucleation and crystallization kinetics set glass formation and glass-ceramic heat treatments? | Chapter 9 (back reference) |
| How is cement, the largest-volume ceramic, made and how does it harden? | Chapter 18 |
| How do glass fibres and ceramic matrices behave in composites? | Chapters 22–23 |
| How do thermal conductivity and thermal stress set the performance of TBCs, substrates and refractories? | Chapter 24 |
| How do dielectric, piezoelectric, magnetic, ionic and optical ceramics work? | Chapters 25–28 and 32 |
| Which ceramics and bioactive glasses are used in the body? | Chapter 31 |
| How do ceramics and CMCs behave in turbines, re-entry vehicles and reactors? | Chapter 33 |
| How are ceramics shaped by additive manufacturing and deposited as coatings? | Chapters 40–41 |
| How are ceramic microstructures and residual stresses characterized? | Chapters 42–43 |

**Next:** Chapter 18 turns to the materials used in the greatest tonnage of all: Portland cement and concrete, structural steel, timber, asphalt and masonry, and to the question of how a civilization can keep building with them while cutting their carbon footprint.
