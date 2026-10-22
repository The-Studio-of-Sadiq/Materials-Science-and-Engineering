# Chapter 7 — Phase Diagrams

*Part II · Thermodynamics and Kinetics*

A foundry pours a batch of aluminium–copper aerospace castings and sends them for solution treatment. The furnace controller is set 15 °C higher than the specification, because the binary Al–Cu diagram in an old handbook shows that the alloy stays fully solid until well above 570 °C, and a hotter soak dissolves the copper faster. The castings come out with blistered surfaces and grain boundaries that look, under the microscope, like dried river beds: small pools of liquid had formed at the boundaries and then frozen. The alloy contained magnesium as well as copper, and the ternary Al–Cu–Mg system has a eutectic about 70 °C below the binary one. The engineer read a correct diagram for the wrong system. A few kilometres away, a refractory supplier is solving a mirror-image problem: which alumina–silica brick will survive the roof of a glass-melting furnace at 1600 °C without sagging. And at a dental laboratory a technician is choosing how much yttria to put into a zirconia crown so that it stays tetragonal at body temperature, and tough.

All three questions are answered by the same kind of map. A phase diagram records, for each temperature, pressure and overall composition, which phases are present at equilibrium, what their compositions are and how much of each there is.

> **How many phases can coexist, and how do we read their compositions and amounts from a diagram?**
> **How does the diagram predict the microstructure that forms on cooling, and where does that prediction stop being reliable?**

| Concept | Engineering destination |
|---|---|
| Gibbs phase rule | Counting what can be fixed in a furnace, a reactor or a crystal grower |
| Unary diagrams (water, iron, carbon, silica) | Pressure–temperature routes: diamond synthesis, refractory firing, steel heat treatment |
| Binary isomorphous systems | Cupronickel condenser tubes, Ni–Cu Monel, Si–Ge, solid-solution ceramics |
| Lever rule | Phase fractions in castings, steels, solders and refractories |
| Eutectic, peritectic, monotectic, eutectoid reactions | Casting alloys, solders, bearing bronzes, pearlite in steel |
| Intermediate compounds | Intermetallic strengthening phases, solder-joint interfaces, spinel refractories |
| Fe–Fe₃C diagram | Every steel and cast-iron heat treatment |
| Ceramic diagrams | Refractories, zirconia implants and thermal-barrier coatings, fuel-cell electrolytes |
| Ternary diagrams | Stainless steels, lead-free solders, slags and cement clinker |
| CALPHAD | Multicomponent alloy design, process windows, integrated computational materials engineering |

**Roadmap.** The phase rule (7.1) → one-component diagrams (7.2) → two components with complete solubility (7.3) and the lever rule (7.4) → invariant reactions and compounds (7.5) → microstructure development on cooling (7.6) → the Fe–C diagram (7.7) → ceramic systems (7.8) → three components (7.9) → computed diagrams (7.10) → reading real diagrams for design (7.11).

---

## 7.1 The Gibbs phase rule

### Phases, components and degrees of freedom

A **phase** is a region of material that is homogeneous in structure and composition and is separated from other regions by an interface: liquid aluminium, a grain of FCC austenite, a crystal of cementite, a glass. Many grains of the same crystal structure and composition are one phase. A **component** is one of the independent chemical species needed to describe the compositions of all phases: Cu and Ni in cupronickel, Fe and C in steel, Al₂O₃ and SiO₂ in a refractory (oxides are chosen as components when the oxygen content follows from them). The **degrees of freedom** $F$ are the intensive variables (temperature, pressure, phase compositions) that can be changed independently without changing the number of phases present.

Equilibrium between phases requires that temperature, pressure and the chemical potential of every component are equal in all phases (Chapter 6). Counting variables and constraints gives the **Gibbs phase rule**:

$$
F=C-P+2
$$

where $C$ is the number of components and $P$ the number of phases. Each phase contributes $C-1$ independent composition variables, so there are $P(C-1)$ composition variables plus $T$ and $p$; equality of chemical potentials imposes $C(P-1)$ constraints. Subtracting gives the rule.

Most materials processing takes place at atmospheric pressure, and condensed phases are insensitive to modest pressure changes. With pressure fixed, the **condensed phase rule** is

$$
F=C-P+1
$$

> **Status of the principle: Gibbs phase rule**
> *Fundamental.* It is a counting consequence of equilibrium thermodynamics; it fails only when the system is not at equilibrium, or when extra variables (surface energy of nanoparticles, electric or magnetic fields, stress) are significant and must be added to the count.

### What the rule tells an engineer

In a binary alloy at fixed pressure ($C=2$), a single-phase region has $F=2$: temperature and composition can both be varied. A two-phase region has $F=1$: once the temperature is chosen, the compositions of both phases are fixed (they are the ends of the tie line, Section 7.4). Three phases can coexist only at $F=0$, an **invariant point** at a single temperature with three fixed compositions. That is why a eutectic alloy freezes at one temperature, with a flat arrest on a cooling curve, while an off-eutectic alloy freezes over a range. The rule also forbids four phases from coexisting in a binary at equilibrium; if a micrograph shows four, the specimen is not at equilibrium, which is common and informative (Section 7.6).

The rule says nothing about *which* phases form or at what temperatures; that is the job of the Gibbs-energy curves of Chapter 6. And it says nothing about the *amounts* of each phase; that is the job of mass balance (Section 7.4).

---

## 7.2 Unary diagrams

With one component, $F=3-P$: single-phase areas, two-phase lines, triple points (Figure 7.1). The axes are pressure and temperature, and the slope of each two-phase line is set by the **Clausius–Clapeyron equation**,

$$
\frac{dp}{dT}=\frac{\Delta H}{T\,\Delta V}
$$

where $\Delta H$ and $\Delta V$ are the molar enthalpy and volume changes of the transformation.

> **Status of the principle: Clausius–Clapeyron equation**
> *Derived.* It follows exactly from equality of the Gibbs energies of the two phases along the coexistence line; integrated forms that treat $\Delta H$ as constant or the vapour as an ideal gas are approximations.

<!-- FIGURE 7.1 | figures/ch07/fig-7-1-unary-diagrams.png | plot | Unary phase diagrams of water, iron, carbon and silica, showing the stable phases as functions of temperature and pressure. | Content: 2x2 panels. (a) Water: log pressure 1 Pa to 1 GPa versus temperature −50 to 400 °C; ice Ih, liquid, vapour; triple point 0.01 °C / 611.657 Pa; critical point 373.9 °C / 22.06 MPa; melting line with negative slope (−13.5 MPa/K) labelled. (b) Iron: pressure 0–20 GPa versus temperature 0–1800 °C; α (BCC) to 912 °C, γ (FCC) 912–1394 °C, δ (BCC) 1394–1538 °C, liquid above 1538 °C at 1 atm; ε (HCP) above ~13 GPa at room temperature. (c) Carbon: pressure 0–20 GPa versus temperature 0–5000 K; graphite/diamond line from ~1.7 GPa at 0 K rising to ~6 GPa at 1700 K; shaded box "HPHT synthesis 5–6 GPa, 1600–1900 K, metal solvent"; label "CVD diamond: metastable, low pressure". (d) Silica at 1 atm as a horizontal temperature bar 0–1800 °C: α-quartz → β-quartz 573 °C → tridymite 870 °C → cristobalite 1470 °C → liquid 1713 °C; inset pressure axis to 12 GPa showing coesite (~2–3 GPa) and stishovite (>~8 GPa). -->

### Water

Water is the familiar example, and its oddity is instructive. Ice Ih is less dense than liquid water, so $\Delta V$ for melting is negative and the melting line slopes backwards. With $\Delta H_m=6.01$ kJ/mol, molar volumes of 19.65 cm³/mol for ice and 18.02 cm³/mol for water at 0 °C, Clausius–Clapeyron gives

$$
\frac{dp}{dT}=\frac{6010}{273.15\times(-1.63\times10^{-6})}\approx-13.5\ \mathrm{MPa/K}
$$

Lowering the melting point by 1 K needs 13.5 MPa (about 135 atm). The same expansion on freezing is what bursts water pipes and spalls concrete in freeze–thaw cycles (Chapter 18). The triple point (0.01 °C, 611.657 Pa) is a defining point of the temperature scale and the operating window of freeze-drying of pharmaceuticals and foods: below 611 Pa, ice sublimes directly to vapour.

### Iron

Pure iron at atmospheric pressure is BCC (α, ferrite) up to 912 °C, FCC (γ, austenite) from 912 °C to 1394 °C, BCC again (δ) up to the melting point at 1538 °C. The α→γ change on heating is accompanied by a volume contraction of about 1 %, because FCC packs more densely; dilatometers detect this to measure transformation temperatures in steels. At about 13 GPa at room temperature, iron transforms to hexagonal ε-iron; this matters in shock loading of armour steels and in the physics of the Earth's core. Every heat treatment of steel exploits the α/γ change, and the alloying additions of Section 7.7 and Chapter 15 move its temperatures.

### Carbon

Graphite is the stable form of carbon at ambient pressure; diamond is metastable, persisting indefinitely because converting it requires breaking and reforming strong covalent bonds. The graphite–diamond equilibrium line starts near 1.7 GPa at 0 K and rises roughly linearly, reaching about 6 GPa near 1700 K. Industrial **high-pressure, high-temperature (HPHT)** synthesis of the abrasive diamond used in saw blades, drill bits and grinding wheels operates at 5–6 GPa and 1300–1600 °C, with molten iron, nickel or cobalt as a solvent–catalyst: the diagram says where diamond is stable, and the molten metal supplies a fast kinetic path. **Chemical-vapour-deposited (CVD)** diamond, used for heat spreaders and optical windows, grows at low pressure where it is not stable at all; atomic hydrogen etches graphitic carbon faster than diamond, so kinetics, not thermodynamics, select the product.

### Silica

Silica (SiO₂) is the most important polymorphic ceramic. At atmospheric pressure the sequence is α-quartz → β-quartz at 573 °C → tridymite at 870 °C → cristobalite at 1470 °C → liquid at 1713 °C. The α–β quartz change is **displacive** (small rotations of SiO₄ tetrahedra) and therefore fast and unavoidable; it carries a volume change of about 0.8 %. Porcelain and whiteware bodies containing free quartz must be cooled slowly through 573 °C or they crack ("dunting"), and quartz-bearing concrete aggregate expands abruptly near the same temperature in a fire. The quartz → tridymite → cristobalite changes are **reconstructive** (bonds break) and so sluggish that impurities and kinetics decide what actually forms; silica refractory bricks are fired to convert as much quartz as possible to tridymite and cristobalite before service. High-pressure coesite and stishovite complete the diagram. Amorphous silica, fused silica glass, is outside the equilibrium diagram altogether (Chapter 17).

---

## 7.3 Binary isomorphous systems

### Liquidus, solidus and the two-phase field

When two components have the same crystal structure, similar atomic sizes and electronegativities (the Hume-Rothery conditions of Chapter 5), they can be completely miscible in the solid as well as the liquid. The binary diagram, drawn at fixed pressure with temperature against composition, then has just three fields: liquid L, a single solid solution α, and a lens-shaped two-phase field L + α between them. The upper boundary of the lens is the **liquidus** (above it, all liquid); the lower boundary is the **solidus** (below it, all solid).

Cu–Ni is the textbook case: both FCC, radii 0.128 and 0.125 nm. The lens runs from the melting point of copper (1085 °C) to that of nickel (1455 °C). Other isomorphous systems include Si–Ge (used in heterojunction transistors and thermoelectrics), Au–Ag, Nb–Ti (the superconducting wire in MRI magnets), Al₂O₃–Cr₂O₃ (ruby is the dilute end) and NiO–MgO.

<!-- FIGURE 7.2 | figures/ch07/fig-7-2-cu-ni-isomorphous.png | plot | The Cu–Ni isomorphous diagram with a tie line through Cu–30 wt% Ni, comparing the measured diagram with the ideal-solution prediction. | Content: x-axis wt% Ni 0–100, y-axis temperature 1000–1500 °C. Solid lines: measured liquidus and solidus from 1085 °C (Cu) to 1455 °C (Ni); at 30 wt% Ni the liquidus is ~1240 °C and solidus ~1170 °C. Dashed lines: ideal-solution liquidus and solidus computed with ΔHm(Cu) = 13.26 kJ/mol, ΔHm(Ni) = 17.48 kJ/mol (at 30 wt% Ni: liquidus 1217 °C, solidus 1193 °C). Horizontal tie line at 1205 °C on the ideal curves from C_L = 26.9 to C_α = 33.2 wt% Ni with overall composition 30 wt% Ni marked; label lengths "R" and "S" for the lever rule. Shade fields L, α, L+α. Small marker "70/30 cupronickel" on the composition axis. -->

### Where the lens comes from

Chapter 6 showed that the phase diagram is the projection of common tangents between Gibbs-energy curves. For two components that form ideal solutions in both liquid and solid, the condition that each component has the same chemical potential in both phases gives, for component $i$,

$$
\ln\frac{x_i^{S}}{x_i^{L}}=\frac{\Delta H_{m,i}}{R}\left(\frac{1}{T}-\frac{1}{T_{m,i}}\right)
$$

where $x_i^S$ and $x_i^L$ are mole fractions in solid and liquid and $\Delta H_{m,i}$, $T_{m,i}$ the enthalpy and temperature of melting of pure $i$. Writing this once for each component and using $x_A+x_B=1$ in each phase gives two equations in two unknowns at each temperature: the solidus and liquidus compositions.

> **Status of the principle: Ideal-solution liquidus and solidus**
> *Approximate.* Exact for ideal liquid and solid solutions with temperature-independent enthalpies of melting; real systems deviate as their mixing enthalpies depart from zero, and when $\Delta H_{mix}$ is strongly positive the solid develops a miscibility gap.

The ideal model reproduces the shape of the Cu–Ni lens but makes it too narrow (Figure 7.2). Real Cu–Ni solid solutions have a slight positive mixing enthalpy, enough to produce a miscibility gap below about 350 °C, which is too sluggish to matter in practice. The gap between the dashed and solid curves is a measure of the non-ideality that CALPHAD assessments (Section 7.10) capture with excess Gibbs-energy terms.

### Partition coefficient

At any temperature in the two-phase field, solid and liquid have different compositions. Their ratio, the **equilibrium partition coefficient**

$$
k=\frac{C_S}{C_L}
$$

measures how strongly a solute is rejected by the growing solid. In Cu–Ni, Ni is enriched in the solid ($k_{Ni}>1$) because it raises the melting point; Cu is rejected ($k_{Cu}<1$). For most impurities in metals and semiconductors $k<1$, which is the basis of segregation, zone refining and dopant non-uniformity in crystal growth (Chapter 9).

---

## 7.4 The lever rule

### Tie lines

In a two-phase field at temperature $T$, draw a horizontal line (an isotherm) through the overall alloy composition $C_0$ until it meets the phase boundaries on either side. This **tie line** connects the compositions of the two coexisting phases. Its ends give $C_L$ and $C_\alpha$; moving $C_0$ along the tie line changes only the amounts of the phases, not their compositions.

### Mass balance

Let $W_L$ and $W_\alpha$ be the mass fractions of liquid and solid. Conservation of total mass and of solute gives

$$
W_L+W_\alpha=1,\qquad W_LC_L+W_\alpha C_\alpha=C_0
$$

so that

$$
W_\alpha=\frac{C_0-C_L}{C_\alpha-C_L},\qquad W_L=\frac{C_\alpha-C_0}{C_\alpha-C_L}
$$

This is the **lever rule**: the fraction of a phase is the length of the tie-line segment on the *opposite* side of $C_0$, divided by the whole tie line. If compositions are in weight percent, the fractions are mass fractions; with atomic percent, they are mole fractions. Converting to volume fractions, which is what an image of a microstructure shows, requires the phase densities.

> **Status of the principle: Lever rule**
> *Derived.* It is pure mass conservation applied to the tie-line compositions; it holds whenever the phases have the compositions the tie line gives, which requires equilibrium (or at least local equilibrium) within each phase.

**Worked example — Freezing a cupronickel condenser tube.** Cu–30 wt% Ni (70/30 cupronickel) is used for seawater condenser and heat-exchanger tubes in ships and power stations because of its resistance to biofouling and erosion–corrosion. Use the ideal-solution model with $T_{m,Cu}=1358$ K, $\Delta H_{m,Cu}=13.26$ kJ/mol, $T_{m,Ni}=1728$ K, $\Delta H_{m,Ni}=17.48$ kJ/mol to find the phases at 1205 °C.

*Partition ratios.* At $T=1478$ K,

$$
\frac{x^S_{Cu}}{x^L_{Cu}}=\exp\!\left[\frac{13260}{8.314}\left(\frac{1}{1478}-\frac{1}{1358}\right)\right]=0.909,\qquad
\frac{x^S_{Ni}}{x^L_{Ni}}=\exp\!\left[\frac{17480}{8.314}\left(\frac{1}{1478}-\frac{1}{1728}\right)\right]=1.228
$$

*Compositions.* With $x^S_{Ni}=1.228\,x^L_{Ni}$ and $1-x^S_{Ni}=0.909\,(1-x^L_{Ni})$, solving gives $x^L_{Ni}=0.285$ and $x^S_{Ni}=0.350$, which with molar masses 63.55 (Cu) and 58.69 g/mol (Ni) are $C_L=26.9$ wt% Ni and $C_\alpha=33.2$ wt% Ni.

*Amounts.*

$$
W_\alpha=\frac{30-26.9}{33.2-26.9}=0.49,\qquad W_L=0.51
$$

At 1205 °C the alloy is about half solid, and the solid is 3 wt% richer in Ni than the alloy. The ideal model puts the liquidus of this alloy at 1217 °C and the solidus at 1193 °C, a freezing range of 24 °C; the measured range is closer to 1240–1170 °C, about 70 °C. The model explains the diagram; it cannot set a furnace. Section 7.6 shows what that composition difference does to the microstructure of a real casting.

---

## 7.5 Invariant reactions and intermediate phases

### Limited solubility and the eutectic

When the components differ in crystal structure or atomic size, solid solubility is limited. The simplest result is the **eutectic** diagram: two terminal solid solutions α and β, each with a solvus beyond which the solute no longer dissolves, and two liquidus lines falling from the melting points of the pure components to meet at the eutectic point. At the eutectic temperature $T_E$ three phases coexist:

$$
L\ \longrightarrow\ \alpha+\beta \qquad (\text{on cooling, at } T_E)
$$

Al–Si, the basis of most aluminium casting alloys, is a nearly ideal example. Aluminium melts at 660 °C; silicon at 1414 °C. The eutectic lies at 577 °C and 12.6 wt% Si. Silicon dissolves in solid aluminium up to 1.65 wt% at 577 °C (falling to almost zero at room temperature); aluminium is practically insoluble in silicon, so β is essentially pure Si. The eutectic composition melts at a temperature 83 °C below pure Al and has a narrow freezing range, the two features that make Al–Si alloys flow well and fill thin moulds: engine blocks, cylinder heads, wheels, pump housings.

<!-- FIGURE 7.3 | figures/ch07/fig-7-3-al-si-eutectic.png | plot | The Al–Si eutectic diagram with microstructures of hypoeutectic, eutectic and hypereutectic alloys. | Content: main panel x-axis wt% Si 0–30 (break, then 100), y-axis temperature 400–900 °C; Al melting 660 °C; eutectic horizontal at 577 °C from 1.65 to ~100 wt% Si; eutectic point 12.6 wt% Si; liquidus rising toward Si (≈ 800 °C at 25 wt% Si). Vertical dashed lines at 7 wt% Si (A356), 12.6 wt% (eutectic, e.g. A413) and 18 wt% Si (A390). Three circular micrograph-style insets: A356 with ~51 % primary α-Al dendrites in eutectic; eutectic with fine Al + Si lamellae/plates; A390 with ~6 % blocky primary Si crystals in eutectic. Fields labelled L, α, L+α, L+Si, α+Si. -->

Other eutectics of engineering importance: Pb–Sn at 183 °C and 61.9 wt% Sn (the classic solder), Sn–Ag–Cu near 217 °C (lead-free solder), Ag–Cu at 779 °C and 28 wt% Cu (silver brazing alloy BAg-8), Au–Si at 363 °C (die attach in microelectronics), Fe–C at 1147 °C (cast irons), Al₂O₃–ZrO₂ near 1860 °C (eutectic ceramics for abrasives), and the CaO–SiO₂–Al₂O₃ eutectics that govern slag fluidity in steelmaking.

### The other invariant reactions

Every invariant reaction in a binary involves three phases at a horizontal line. They are classified by which phase lies above or below the junction:

| Reaction | On cooling | Engineering example | Typical temperature |
|---|---|---|---|
| Eutectic | $L\to\alpha+\beta$ | Al–12.6Si casting alloys; Sn–Pb, Sn–Ag–Cu solders | 577 °C; 183 °C; ~217 °C |
| Peritectic | $L+\alpha\to\beta$ | Fe–C at 0.17 wt% C; Cu–Zn brasses; Pt–Ag | 1495 °C; 902 °C (α-brass) |
| Monotectic | $L_1\to\alpha+L_2$ | Cu–Pb leaded bronze bearings; Al–Bi, Al–Pb | 955 °C (Cu–Pb) |
| Eutectoid | $\gamma\to\alpha+\beta$ | Fe–C pearlite; Cu–Al aluminium bronze | 727 °C; ~565 °C |
| Peritectoid | $\alpha+\beta\to\gamma$ | Formation of ordered intermetallics in Ni–Mo, Ti–Al | various |

The **eutectoid** and **peritectoid** are the all-solid analogues of the eutectic and peritectic. Because they take place in the solid, where diffusion is slow, their products are fine and their kinetics matter as much as their thermodynamics (Chapter 10).

The **peritectic** reaction consumes a solid and the liquid to make a new solid. The product forms as a shell on the primary solid and then has to grow by diffusion through itself, so peritectic reactions rarely go to completion during normal cooling. In continuous casting of steel, grades with 0.09–0.17 wt% C pass through the Fe–C peritectic at 1495 °C; the δ→γ change contracts the newly solidified shell, which pulls away from the mould and causes surface depressions and cracks. Casters call these "peritectic grades" and run them with special mould powders and slower casting speeds.

In a **monotectic**, a liquid splits into a solid and a second liquid. Cu–Pb has a liquid miscibility gap: at 955 °C a liquid containing about 36 wt% Pb forms solid copper and a lead-rich liquid with about 87 wt% Pb, which finally freezes at 326 °C. The result is a copper matrix with lead pools, a self-lubricating bearing alloy used in engines and pumps. The two liquids differ in density and tend to separate under gravity, which makes such alloys hard to cast uniformly.

### Intermediate phases and compounds

Many binaries contain phases with crystal structures different from either component. Those with a narrow composition range are **line compounds** or stoichiometric **intermetallics**; those with a wide range are **intermediate solid solutions**. They divide a complicated diagram into simpler sub-diagrams.

- **Congruently melting** compounds melt to a liquid of the same composition, at a temperature maximum on the liquidus. Mg₂Si (melting near 1085 °C) is the strengthening phase of 6xxx aluminium alloys; NiAl (near 1640 °C) is a coating phase on turbine blades; MgAl₂O₄ spinel is the ceramic analogue (Section 7.8). The diagram on either side of such a compound can be read as an independent binary.
- **Incongruently melting** compounds decompose on heating into a liquid and a different solid, through a peritectic. Cu₆Sn₅, the intermetallic that forms between solder and copper pads, melts incongruently near 415 °C; mullite in the Al₂O₃–SiO₂ system is debated but is usually drawn as melting incongruently near 1890 °C.
- **Ordered phases** such as Ni₃Al (γ′), the strengthening precipitate of nickel superalloys, and Fe₃Al or CuZn (β′ brass) are intermediate phases whose atoms occupy distinct sublattices (Chapter 6).

Intermetallics are usually hard, brittle and of high melting point. That is useful when they are fine precipitates (Chapters 10 and 13) and harmful when they are thick continuous layers: a solder joint whose Cu₆Sn₅ layer has grown to 10 µm fractures at the interface under drop impact.

> **Status of the principle: Binary diagram topology rules**
> *Derived.* The rules that two single-phase fields are separated by a two-phase field, that three-phase equilibria are horizontal lines, and that boundaries meet at invariant points with extrapolations falling into two-phase fields (the "180° rule") follow from the phase rule and the shape of Gibbs-energy curves; they are used to check experimentally drawn diagrams.

---

## 7.6 Microstructure development on cooling

The phase diagram tells what phases are present at each temperature. Following an alloy down a vertical line through the diagram predicts the sequence of reactions and therefore the microstructure, which in turn sets strength, ductility and corrosion behaviour.

### Isomorphous alloys: equilibrium and coring

Cool the Cu–30Ni alloy of Section 7.4 slowly. At the liquidus the first solid forms, richer in Ni than the liquid. As the temperature falls, the tie-line ends move down the liquidus and solidus: the liquid becomes richer in Cu, and so must the solid, which requires Ni to diffuse out of the solid already formed. At the solidus, at equilibrium, the last liquid disappears and the solid has the overall composition everywhere.

Real castings cool too fast for diffusion in the solid to keep up (Chapter 8 gives the distances). Each layer of solid keeps roughly the composition it had when it formed. Dendrite centres are Ni-rich; the regions between dendrite arms, which froze last, are Cu-rich. This **coring** or **microsegregation** shows up after etching as concentration contours, lowers the effective solidus (the last liquid can be far richer in the low-melting component than the overall alloy) and causes local differences in corrosion potential. It is removed by a **homogenization** anneal, whose time is calculated in Chapter 8. Chapter 9 quantifies the non-equilibrium limit with the Scheil equation.

### Eutectic alloys

Follow three Al–Si alloys down Figure 7.3.

*Eutectic composition (12.6 wt% Si).* The liquid remains liquid down to 577 °C and then freezes at constant temperature into a two-phase eutectic mixture of α-Al and Si. Because both solids form together from the liquid, with solute diffusing sideways only a short distance, the eutectic is fine: lamellae, rods or plates a few micrometres apart.

*Hypoeutectic (less than 12.6 wt% Si).* Cooling into the L + α field produces **primary** α-Al dendrites. The remaining liquid becomes richer in Si along the liquidus, reaching the eutectic composition at 577 °C, where it freezes as eutectic. The final microstructure is primary α dendrites in a eutectic matrix.

*Hypereutectic (more than 12.6 wt% Si).* The primary phase is now silicon, which forms as hard faceted blocks, followed by eutectic.

The lever rule, applied just below and just above the eutectic temperature, gives the amounts of each constituent.

**Worked example — Constituents in two aluminium casting alloys.** A356 (Al–7 wt% Si, plus Mg for age hardening) is used for automotive wheels and suspension parts; A390 (Al–18 wt% Si) for unlined engine blocks. Use the Al–Si eutectic at 12.6 wt% Si, the α solvus at 1.65 wt% Si and treat Si as pure.

*A356, primary α.* Just above 577 °C the alloy is α (1.65 wt% Si) plus liquid of eutectic composition (12.6 wt% Si):

$$
W_{\alpha,\text{primary}}=\frac{12.6-7}{12.6-1.65}=0.51
$$

The remaining 0.49 is liquid, which becomes eutectic on further cooling.

*A356, total silicon phase.* Just below 577 °C, across the whole α + Si field,

$$
W_{Si}=\frac{7-1.65}{100-1.65}=0.054
$$

All of this 5.4 % silicon lies inside the eutectic (it is $0.054/0.49=11\,\%$ of the eutectic).

*A390, primary Si.* For the hypereutectic alloy, just above 577 °C the alloy is pure Si plus eutectic liquid:

$$
W_{Si,\text{primary}}=\frac{18-12.6}{100-12.6}=0.062
$$

and the total silicon phase is $(18-1.65)/(100-1.65)=0.17$. The A390 block therefore contains about 6 % blocky primary silicon (by mass; by volume slightly more, since Si at 2.33 g/cm³ is less dense than Al at 2.70 g/cm³) dispersed in a eutectic. These primary crystals, not the total silicon, determine wear resistance and machinability, and their size is controlled by adding phosphorus to nucleate them (Chapter 9).

### Beyond equilibrium

Two warnings attach to these predictions. First, the eutectic in unmodified Al–Si forms coarse brittle silicon plates; adding 0.01–0.02 wt% strontium or sodium changes the growth mode to a fine fibrous structure and raises ductility several-fold, without changing the phase diagram at all. Second, an alloy with less solute than the maximum solubility (say Al–1 wt% Si) should freeze entirely as α, but under real casting conditions coring enriches the last liquid enough that some non-equilibrium eutectic appears between the dendrites. Phase diagrams predict which phases are possible and their equilibrium amounts; morphology and departures from equilibrium belong to Chapters 9 and 10.

---

## 7.7 The Fe–C (Fe–Fe₃C) diagram

### Stable and metastable diagrams

Steels and cast irons are the most used engineering materials, and the iron–carbon diagram is the most used phase diagram. Strictly, the stable carbon-rich phase in contact with iron is graphite. But in steels the formation of graphite is so slow that the carbide **cementite**, Fe₃C (6.70 wt% C), forms instead and persists for practical purposes indefinitely. The diagram used for steels is therefore the **metastable Fe–Fe₃C diagram**; the stable Fe–graphite diagram, with slightly shifted lines, governs grey and ductile cast irons, where silicon promotes graphite.

<!-- FIGURE 7.4 | figures/ch07/fig-7-4-fe-fe3c-diagram.png | plot | The metastable Fe–Fe₃C phase diagram with the steel and cast-iron regions and the key invariant points. | Content: x-axis wt% C 0–6.70 (top axis wt% Fe3C 0–100), y-axis temperature 400–1600 °C. Phases: δ, γ (austenite), α (ferrite), Fe3C, L. Points: peritectic 1495 °C (δ 0.09, γ 0.17, L 0.53 wt% C); eutectic 1147 °C at 4.30 wt% C, γ max solubility 2.14 wt% C; eutectoid 727 °C at 0.76 wt% C; α max solubility 0.022 wt% C at 727 °C. Lines labelled A1 (727 °C), A3 (from 912 °C at 0 C to 727 °C at 0.76 C), Acm (from 727 °C at 0.76 C to 1147 °C at 2.14 C). Bracket "steels" 0–2.14 wt% C and "cast irons" 2.14–6.70. Dashed vertical at 0.40 wt% C labelled "AISI 1040" and at 1.0 wt% C labelled "AISI 52100 bearing steel". Dotted lines for the Fe–graphite eutectic (1153 °C) and eutectoid (738 °C). -->

### The landmarks

The key features of Figure 7.4, which every metallurgist knows by heart:

| Feature | Temperature | Compositions (wt% C) |
|---|---|---|
| Melting of pure iron | 1538 °C | 0 |
| Peritectic: $\delta+L\to\gamma$ | 1495 °C | δ 0.09, γ 0.17, L 0.53 |
| Eutectic: $L\to\gamma+\mathrm{Fe_3C}$ (ledeburite) | 1147 °C | L 4.30, γ 2.14, Fe₃C 6.70 |
| Eutectoid: $\gamma\to\alpha+\mathrm{Fe_3C}$ (pearlite) | 727 °C | γ 0.76, α 0.022, Fe₃C 6.70 |
| α→γ in pure iron (A3 at 0 % C) | 912 °C | 0 |

Austenite dissolves far more carbon (up to 2.14 wt%) than ferrite (at most 0.022 wt%), because carbon sits in the larger octahedral interstices of FCC iron (Chapter 2). That difference is the whole basis of steel heat treatment: heat into γ to dissolve carbon, then cool so that the carbon must come out again, either slowly, as cementite in pearlite, or not at all, trapping it in martensite (Chapter 10). The conventional boundary between steels and cast irons is 2.14 wt% C: steels can be made fully austenitic and hot-worked; cast irons always contain eutectic and are shaped by casting.

The critical temperature lines carry their own names: **A1** is the eutectoid isotherm at 727 °C, **A3** the boundary between γ and α + γ in hypoeutectoid steels, and **Acm** the boundary between γ and γ + Fe₃C in hypereutectoid steels. Heat-treatment specifications are written in these terms: full annealing and hardening of hypoeutectoid steels at about A3 + 30–50 °C, of hypereutectoid steels between A1 and Acm.

### Microstructures of slowly cooled steels

A **eutectoid steel** (0.76 wt% C) transforms entirely at 727 °C to **pearlite**, alternating plates of ferrite and cementite. The lever rule across the α + Fe₃C field gives the cementite fraction within pearlite: $(0.76-0.022)/(6.70-0.022)=0.11$. Pearlite is about 89 % ferrite and 11 % cementite by mass, which, because the two phases have similar densities, is about 7:1 in plate thickness.

A **hypoeutectoid** steel forms **proeutectoid ferrite** at the γ grain boundaries between A3 and A1; the remaining austenite reaches 0.76 wt% C at 727 °C and becomes pearlite. A **hypereutectoid** steel forms proeutectoid cementite on the austenite grain boundaries between Acm and A1, then pearlite.

**Worked example — Ferrite, pearlite and cementite in two steels.** Consider AISI 1040 (0.40 wt% C), a medium-carbon steel for shafts, axles and connecting rods, and a 1.20 wt% C tool steel, both slowly cooled.

*1040, constituents.* Just above 727 °C the steel is α (0.022 wt% C) plus γ (0.76 wt% C):

$$
W_{\alpha,\text{pro}}=\frac{0.76-0.40}{0.76-0.022}=0.49,\qquad W_{\text{pearlite}}=0.51
$$

*1040, phases.* Just below 727 °C, across α + Fe₃C,

$$
W_\alpha=\frac{6.70-0.40}{6.70-0.022}=0.94,\qquad W_{\mathrm{Fe_3C}}=0.06
$$

*1.20 wt% C steel.* Proeutectoid cementite, just above 727 °C between γ (0.76) and Fe₃C (6.70):

$$
W_{\mathrm{Fe_3C,pro}}=\frac{1.20-0.76}{6.70-0.76}=0.074
$$

and total cementite $(1.20-0.022)/(6.70-0.022)=0.18$.

The 1040 steel is half ferrite grains, half pearlite colonies, which gives a tensile strength of roughly 520–620 MPa in the normalized condition with good ductility. The tool steel contains about 7 % cementite as a network around the former austenite grains; if left continuous, that brittle network embrittles the steel, so such steels are given a spheroidizing anneal before machining and are hardened from between A1 and Acm, where some cementite remains undissolved to resist wear (Chapter 15). Note that the constituent fractions (ferrite vs pearlite) and the phase fractions (ferrite vs cementite) answer different questions; mixing them up is a common reading error.

### Alloying elements and the limits of the diagram

Real steels contain manganese, silicon, chromium, nickel, molybdenum and other elements, and the binary diagram is only a guide. Austenite stabilizers (Ni, Mn, C, N) lower A3 and A1 and enlarge the γ field; at 8 % Ni plus 18 % Cr, austenite is retained to room temperature in 304 stainless steel. Ferrite stabilizers (Cr, Si, Mo, V, Ti) raise the critical temperatures and close the γ field ("γ loop"). More importantly, the diagram says nothing about what happens when cooling is fast: the bainite and martensite that give high-strength steels their properties are not on it at all. They live on the TTT and CCT diagrams of Chapters 9 and 10, which add time as an axis.

> **Status of the principle: Fe–Fe₃C diagram as a guide to steel microstructure**
> *Approximate.* It is a metastable equilibrium diagram, accurate for plain-carbon steels cooled slowly enough for carbon diffusion to keep pace; alloying shifts its lines, and fast cooling produces phases it does not contain.

---

## 7.8 Ceramic phase diagrams

Ceramic diagrams are read in exactly the same way, with oxides as components. Three systems cover refractories, structural and biomedical ceramics, and energy devices.

### Al₂O₃–SiO₂: refractories and porcelains

The alumina–silica system contains one intermediate compound, **mullite**, nominally 3Al₂O₃·2SiO₂ (71.8 wt% Al₂O₃), with a solid-solution range toward alumina. The two eutectics are between silica and mullite, near 1587 °C and 5–6 wt% Al₂O₃, and between mullite and corundum, near 1840–1890 °C.

The diagram tells a refractory engineer exactly what to buy. Fireclay bricks with 25–45 wt% Al₂O₃ sit in the silica–mullite field: above 1587 °C they contain liquid, and the lever rule gives its amount. A brick with 40 wt% Al₂O₃ at 1600 °C contains roughly half its mass as viscous liquid and will sag under load. Silica bricks (about 95 % SiO₂ or more) avoid this only if the alumina impurity is kept very low, because a small amount of alumina moves the composition into the liquid-forming region near the steep silica-rich liquidus; even 1 % Al₂O₃ produces a noticeable liquid fraction at 1600 °C. High-alumina bricks (above 72 wt% Al₂O₃) contain no liquid until about 1840 °C. Porcelain relies on the same diagram, with K₂O from feldspar as a third component supplying the bonding liquid during firing.

### ZrO₂–Y₂O₃: transformation-toughened and ion-conducting zirconia

Pure zirconia is monoclinic up to about 1170 °C, tetragonal up to about 2370 °C, cubic (fluorite) above that, and melts near 2710 °C. The tetragonal→monoclinic change on cooling is martensitic and expands the volume by about 4–5 %, enough to shatter a sintered pure zirconia part. Adding yttria stabilizes the higher-symmetry phases to lower temperature; the diagram (drawn in mol% YO₁.₅ or Y₂O₃) shows the tetragonal and cubic fields widening as yttria increases, with a broad two-phase t + c field.

<!-- FIGURE 7.5 | figures/ch07/fig-7-5-zro2-y2o3.png | plot | The zirconia-rich end of the ZrO₂–Y₂O₃ diagram, with the compositions used for dental and implant ceramics, thermal-barrier coatings and fuel-cell electrolytes. | Content: x-axis mol% Y2O3 0–12, y-axis temperature 0–2800 °C. Fields: monoclinic (m) at low Y and low T; tetragonal (t) from ~1170 °C at 0 % falling with Y content; cubic (c) above ~2370 °C at 0 % and extending to room temperature above ~8 mol%; two-phase t + c and m + c fields; liquid above ~2700 °C. Vertical markers: 3 mol% "3Y-TZP: crowns, hip heads (metastable t)"; ~4–4.5 mol% "7–8 wt% YSZ: thermal-barrier coatings (t′)"; 8 mol% "8YSZ: SOFC electrolytes, oxygen sensors (cubic)". Arrow at 3 mol% at room temperature labelled "t→m under crack-tip stress: transformation toughening". -->

Three compositions illustrate the engineering use of one diagram (Figure 7.5):

- **3 mol% Y₂O₃ (about 5.4 wt%), 3Y-TZP.** Fine-grained tetragonal zirconia polycrystal, metastable at room temperature because the grains are too small to transform spontaneously. At a crack tip the stress triggers the t→m change; the expansion squeezes the crack shut. This **transformation toughening** gives fracture toughness of 5–10 MPa√m, two to three times that of alumina, and makes zirconia suitable for dental crowns, bridges and femoral heads of hip replacements (Chapters 14 and 31). The same metastability is a weakness: in warm moisture the surface slowly transforms ("low-temperature degradation").
- **About 4–4.5 mol% (7–8 wt%) Y₂O₃.** Plasma-sprayed or electron-beam-deposited thermal-barrier coatings on turbine blades are quenched into a non-transformable tetragonal phase (t′) that resists both destabilization and the t→m change during thermal cycling (Chapter 33).
- **8 mol% Y₂O₃ (about 13.7 wt%), 8YSZ.** Fully cubic. Each pair of Y³⁺ ions replacing Zr⁴⁺ creates one oxygen vacancy, giving high oxide-ion conductivity at 700–1000 °C: the electrolyte of solid-oxide fuel cells and of lambda sensors in car exhausts (Chapters 8 and 32).

### MgO–Al₂O₃: spinel

MgO (melting near 2830 °C) and Al₂O₃ (2054 °C) form the compound **spinel**, MgAl₂O₄ (71.7 wt% Al₂O₃), which melts congruently near 2105 °C and dissolves excess alumina at high temperature. Eutectics lie on both sides, near 1995 °C toward MgO and near 1925 °C toward Al₂O₃. Because spinel melts congruently, the diagram splits into two simple eutectic sub-systems. Steel ladles are lined with magnesia–spinel or alumina–spinel castables, chosen because spinel resists penetration by basic slags and because its thermal expansion is moderate. Transparent polycrystalline spinel serves as infrared windows and armour (Chapter 28).

---

## 7.9 Ternary diagrams

### The Gibbs triangle

With three components and fixed pressure, two composition variables and temperature are needed, so a full ternary diagram is a triangular prism. Composition is plotted in an equilateral **Gibbs triangle**, whose corners are the pure components. The perpendicular distance from a point to the side opposite corner A, as a fraction of the triangle's height, is the fraction of A; the three fractions sum to one. In practice, gridlines parallel to each side are read directly.

Two geometric rules make the triangle useful. Any point on a line from a corner to the opposite side has a constant ratio of the other two components; adding or removing one component moves the composition along that line. And the **centre-of-gravity rule**: if an alloy of composition $P$ splits into phases of compositions $\alpha$, $\beta$, $\gamma$, then $P$ lies inside the triangle $\alpha\beta\gamma$, and the phase fractions are the weights that place the centre of gravity at $P$. Two-phase mixtures obey the ordinary lever rule along tie lines.

> **Status of the principle: Ternary phase rule and centre-of-gravity rule**
> *Derived.* With $C=3$ at fixed pressure, $F=4-P$: single-phase volumes, two-phase regions with tie lines, three-phase tie triangles at each temperature, and four-phase invariant planes; the centre-of-gravity rule is mass conservation in three components.

### Sections and projections

A three-dimensional diagram is communicated by two-dimensional slices (Figure 7.6):

- **Isothermal sections** cut the prism at one temperature. They show single-phase areas, two-phase areas crossed by tie lines (which are not generally parallel and must be measured or computed), and three-phase tie triangles. Phase fractions can be read with the lever and centre-of-gravity rules. The 900 °C or 1100 °C sections of Fe–Cr–Ni are used to design stainless steels and to predict σ-phase formation in welds.
- **Vertical sections** (isopleths) cut the prism along a line of composition, for example constant 18 wt% Cr in Fe–Cr–Ni, or the line from Fe–C to a fixed Mn content. They look like binary diagrams but are not: tie lines generally do not lie in the plane, so the lever rule *cannot* be applied on them. They show which phases appear on heating or cooling a given alloy, which is what a heat-treatment engineer needs.
- **Liquidus projections** show the liquidus surface from above, with isotherms and the **valleys** (monovariant lines) where two solids crystallize together, meeting at ternary invariant points such as a **ternary eutectic** $L\to\alpha+\beta+\gamma$. Arrows on the valleys show the direction of falling temperature, which is the path followed by the last liquid during solidification.

<!-- FIGURE 7.6 | figures/ch07/fig-7-6-ternary-gibbs-triangle.png | schematic | Reading a ternary system: the Gibbs triangle with a composition point, an isothermal section with tie lines and a tie triangle, and a liquidus projection with a ternary eutectic. | Content: three panels. (a) Gibbs triangle A–B–C with gridlines every 10 %, point P = 50 % A, 30 % B, 20 % C marked with its three read-off lines. (b) Schematic isothermal section of a simple eutectic ternary below all binary eutectics but above the ternary eutectic: corner solid solutions α, β, γ, two-phase fields with fanning tie lines, central liquid region, three-phase tie triangles; a point inside a tie triangle with the centre-of-gravity construction. (c) Liquidus projection with binary eutectics e1, e2, e3 on the edges, three valleys with arrows of decreasing temperature meeting at ternary eutectic E; isotherms drawn every 50 °C. Optional annotation in (c): "Sn–Ag–Cu: E ≈ 217 °C near Sn–3.5Ag–0.9Cu". -->

### Engineering ternaries

**Lead-free solder.** Sn–Ag–Cu has a ternary eutectic near 217 °C, close to Sn–3.5Ag–0.9Cu. Commercial SAC305 (Sn–3.0Ag–0.5Cu) lies just off it and melts over a range of a few degrees. At room temperature the solder consists of tin with small particles of the intermetallics Ag₃Sn and Cu₆Sn₅.

**Worked example — Phase fractions in a lead-free solder joint.** Estimate the intermetallic content of SAC305 at room temperature, assuming that Ag and Cu are entirely in Ag₃Sn and Cu₆Sn₅ and that tin dissolves neither.

*Composition of the compounds.* With molar masses Ag 107.87, Cu 63.55, Sn 118.71 g/mol:

$$
w_{Ag}(\mathrm{Ag_3Sn})=\frac{3(107.87)}{3(107.87)+118.71}=0.732,\qquad
w_{Cu}(\mathrm{Cu_6Sn_5})=\frac{6(63.55)}{6(63.55)+5(118.71)}=0.391
$$

*Centre of gravity.* All silver is in Ag₃Sn, so $W_{\mathrm{Ag_3Sn}}=0.030/0.732=0.041$. All copper is in Cu₆Sn₅, so $W_{\mathrm{Cu_6Sn_5}}=0.005/0.391=0.013$. The tin fraction is $1-0.041-0.013=0.946$.

About 4 % Ag₃Sn and 1.3 % Cu₆Sn₅ by mass, fine particles that strengthen the tin matrix much as precipitates strengthen an aluminium alloy. The composition lies inside the Sn–Ag₃Sn–Cu₆Sn₅ tie triangle, so these three are the only phases expected; the joint additionally forms a Cu₆Sn₅ interfacial layer by reaction with the copper pad, which the bulk calculation does not include.

**Stainless steels.** The Fe–Cr–Ni system decides whether a stainless steel is ferritic (Fe–17Cr, 430), austenitic (Fe–18Cr–8Ni, 304), duplex (Fe–22Cr–5Ni, 2205) or martensitic. For fast-solidifying weld metal, welders use the empirical Schaeffler or WRC-1992 diagrams in chromium and nickel *equivalents* (Chapter 39).

**Oxide systems.** The CaO–Al₂O₃–SiO₂ liquidus projection is the map of slags in blast furnaces and steelmaking, of Portland cement clinker (which lies in the field of tricalcium silicate, Chapter 18), of glass compositions and of the mineral wool used in building insulation.

---

## 7.10 CALPHAD: computed phase diagrams

### Why compute?

A commercial nickel superalloy contains ten or more elements; a high-entropy alloy five in nearly equal amounts. Measuring their phase equilibria experimentally, at every composition and temperature of interest, is impossible. The **CALPHAD** (CALculation of PHAse Diagrams) method instead models the Gibbs energy of every phase as a function of temperature, pressure and composition, fits the model parameters to the experimental and first-principles data for the binary and ternary subsystems, and then predicts multicomponent equilibria by minimizing the total Gibbs energy.

### The models

For a substitutional solution phase φ of components $i$, the molar Gibbs energy is written

$$
G_m^\varphi=\sum_i x_i\,{}^\circ G_i^\varphi+RT\sum_i x_i\ln x_i+{}^{ex}G_m^\varphi
$$

The first term is the weighted sum of the pure-element Gibbs energies in the structure of φ (taken from standard "lattice-stability" databases, which give, for example, the Gibbs energy of hypothetical FCC chromium); the second is ideal mixing entropy; the third is the excess term, usually a **Redlich–Kister polynomial** for each pair,

$$
{}^{ex}G_m^\varphi=\sum_{i<j}x_ix_j\sum_{\nu=0}^{n}L_{ij}^{(\nu)}\,(x_i-x_j)^\nu
$$

where the interaction parameters $L^{(\nu)}$ are linear functions of temperature. With only $L^{(0)}$ constant, this is the regular-solution model of Chapter 6, which already predicts a symmetric miscibility gap with critical temperature $T_c=L^{(0)}/2R$ (for $L^{(0)}=20$ kJ/mol, $T_c\approx1200$ K). Ternary terms are added where binaries alone do not reproduce ternary data. Ordered phases, carbides, oxides and intermetallics are described with the **sublattice (compound-energy) models** introduced in Chapter 6, in which different species mix on distinct sublattices, for example $(\mathrm{Fe,Cr})_3(\mathrm{C})_1$ for cementite with chromium substitution, or $(\mathrm{Ni,Al})_3(\mathrm{Al,Ni})_1$ for γ′.

The equilibrium state at a given $T$, $p$ and overall composition is the set of phases, fractions and phase compositions that minimizes the total Gibbs energy; graphically, this is the multidimensional common-tangent construction of Chapter 6. Software packages (Thermo-Calc, FactSage, Pandat, and open-source tools such as OpenCalphad and pycalphad) perform this minimization and draw sections, projections, phase-fraction curves and property diagrams.

> **Status of the principle: CALPHAD phase-equilibrium predictions**
> *Approximate.* Equilibrium is exact thermodynamics, but the Gibbs-energy functions are fitted models; predictions are as good as the database coverage of the relevant subsystems, and extrapolations into untested composition ranges or to metastable phases carry uncertainties of tens of degrees.

### What CALPHAD delivers

- **Phase-fraction diagrams** for a single alloy as a function of temperature: the solvus of γ′ in a superalloy, the temperature where σ phase appears in a duplex stainless steel, the amount of liquid at each temperature in a brazing filler.
- **Solidification paths** using the Scheil–Gulliver approximation (Chapter 9), which predict the non-equilibrium freezing range and the last phases to form; essential for castability, weldability and the design of alloys for additive manufacturing (Chapter 40).
- **Thermodynamic inputs to kinetics**: driving forces for nucleation, chemical potentials and thermodynamic factors for diffusion simulations (Chapter 8) and precipitation models (Chapter 10).
- **Alloy design**: searching composition space for alloys with a target phase constitution. Computationally designed ultra-high-strength gear and landing-gear steels, developed this way (integrated computational materials engineering, ICME), reached aerospace qualification far faster than trial-and-error alloys (Chapters 45 and 47).

The essential skill for the engineer is to know which subsystems are well assessed. A prediction for an alloy whose key ternary has never been measured is a hypothesis to be checked, not a design value.

---

## 7.11 Reading real diagrams for alloy and process design

Real diagrams in handbooks and databases are dense with lines, two composition scales (weight and atomic percent), dashed uncertain boundaries, and notes on phases that are metastable or ordered. A short checklist turns them into engineering decisions.

1. **Check the system.** Is it the right number of components? The opening example of this chapter failed at this step: 2024 aluminium is Al–4.4Cu–1.5Mg–0.6Mn, and the binary Al–Cu diagram is the wrong map.
2. **Check the composition scale and the axis units.** Weight percent for alloying, atomic or mole percent for crystal chemistry and for oxides; the same eutectic can look very different on the two scales.
3. **Identify the invariant reactions** that the alloy's vertical line crosses; they are where liquid appears or disappears and where microstructure changes abruptly.
4. **Apply the lever rule** at the temperatures that matter: service, process soak, just above and below each invariant.
5. **Ask whether equilibrium is reached.** Is the process time long compared with the diffusion time (Chapter 8)? If not, expect coring, non-equilibrium eutectic, retained or metastable phases.

**Worked example — The solution-treatment window of an Al–Cu alloy.** A designer wants to dissolve all the copper of an Al–4.4 wt% Cu alloy into the α solid solution before quenching and ageing (Chapter 10). The Al–Cu binary has a eutectic at 548 °C and 33.2 wt% Cu, a maximum solubility of Cu in Al of 5.65 wt% at 548 °C, and the α solvus passes through about 4.4 wt% Cu near 500 °C.

*Lower limit.* The alloy must be above its solvus, about 500 °C, for all θ (Al₂Cu) to dissolve.

*Upper limit from the binary.* Approximating the solidus as a straight line from 660 °C (pure Al) to 548 °C (5.65 wt% Cu), the solidus at 4.4 wt% Cu is

$$
T_{sol}\approx660-\frac{660-548}{5.65}\times4.4=573\ ^\circ\mathrm{C}
$$

The binary window appears to be about 500–573 °C, a comfortable 70 °C wide.

*Correction for the real alloy.* The alloy has 1.5 % Mg. The Al–Cu–Mg ternary contains a eutectic involving α, θ and the S phase (Al₂CuMg) near 507 °C, and the coring present in a casting or a hot-worked product leaves small regions rich enough in Cu and Mg to reach it. Commercial 2024 is therefore solution-treated at about 495 °C, with a tolerance of a few degrees, and incipient melting is checked metallographically. The window that the binary showed as 70 °C wide is, in the real alloy, about 10 °C. A furnace that overshoots produces exactly the grain-boundary melting described at the start of this chapter.

The same reading habit serves elsewhere:

- **Brazing.** The Ag–Cu eutectic (779 °C, 28 wt% Cu) melts at a single temperature, which makes BAg-8 ideal for vacuum brazing in a furnace where the filler must flow all at once. Fillers with a wide melting range liquate: the low-melting liquid runs out first (Chapter 39).
- **Hot shortness.** The Fe–FeS eutectic at 988 °C leaves liquid grain-boundary films during hot rolling at 1100–1200 °C; manganese ties sulphur up as high-melting MnS.
- **Heat treatment of steels.** A3 and Acm locate the austenitizing temperature; the eutectoid composition tells whether proeutectoid ferrite or cementite will form; alloy additions move both (Chapter 15).
- **Refractory selection.** Read the liquid fraction at the service temperature with the lever rule (Section 7.8); a few percent of liquid is tolerable in a castable, tens of percent is not.
- **Crystal growth and purification.** The partition coefficient, read from the slopes of liquidus and solidus near the pure component, predicts how dopants distribute along a Czochralski silicon ingot and how efficiently zone refining removes impurities (Chapter 9).
- **Liquid-phase sintering.** Cemented carbides (WC–Co) and tungsten heavy alloys are sintered just above a binder eutectic so that a small, controlled liquid fraction speeds densification (Chapter 38).

> **Boundary.** Phase diagrams describe equilibrium. How long it takes to approach equilibrium, and what happens when it is not approached, is the subject of the next three chapters: diffusion (Chapter 8), nucleation and growth (Chapter 9) and solid-state transformations (Chapter 10). The thermodynamic laws used to build the diagrams are recapped in Chapter 6 and belong in full to the Advanced Chemistry book.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| Where do the Gibbs-energy curves behind each diagram, the common tangent and the miscibility gap come from? | Chapter 6 |
| How fast does a cored casting homogenize, and how far does carbon move during carburizing? | Chapter 8 |
| Why does a liquid undercool before freezing, and what sets dendrite spacing, segregation and the non-equilibrium (Scheil) freezing path? | Chapter 9 |
| What microstructures form when steels and aluminium alloys are cooled too fast for the equilibrium diagram, and what are TTT and CCT diagrams? | Chapter 10 |
| How do the phases on a diagram translate into strength through precipitation and grain size? | Chapter 13 |
| How are steels and cast irons designed with the Fe–C diagram and alloying additions? | Chapter 15 |
| Which non-ferrous alloy systems (Al, Ti, Ni, Cu, Mg) rely on which invariant reactions? | Chapter 16 |
| How are zirconia, alumina and silicate ceramics processed and toughened? | Chapter 17 |
| How do clinker phases in the CaO–SiO₂–Al₂O₃ system become cement? | Chapter 18 |
| How do welding and brazing use eutectics, and how is weld-metal ferrite controlled? | Chapter 39 |
| How are phase diagrams measured by thermal analysis and diffraction? | Chapter 42 |
| How are first-principles energies and machine learning combined with CALPHAD? | Chapters 45 and 47 |

**Next:** Chapter 8 supplies the clock that phase diagrams lack, deriving how atoms move through solids and how far they travel in the time a process allows.
