# Chapter 41 — Thin Films, Coatings and Electronic Materials Processing

*Part IX · Processing and Manufacturing*

A carbide turning insert cuts hardened steel with a chip sliding over its rake face at 900 °C. Uncoated, its edge would crater in minutes; with 10 µm of TiCN and α-Al$_2$O$_3$ deposited by chemical vapour deposition it lasts an hour. A turbine blade survives gas hotter than its superalloy can bear because 150 µm of yttria-stabilized zirconia carries a temperature drop of more than 100 °C. Low-E architectural glass reflects infrared through ten nanometres of sputtered silver. A titanium hip stem bonds to bone through plasma-sprayed hydroxyapatite. A microprocessor is a stack of more than a hundred films, the thinnest a few atomic layers of hafnium oxide grown one monolayer at a time. In each case the bulk gives strength, shape and cost, and a thin layer made by a separate process gives the function. That layer has its own microstructure, residual stress and failure modes, and the processes that make it (vapour transport in vacuum, reactions on a hot surface, electrochemistry, droplets hitting a surface at the speed of sound) differ from casting or forging.

> **How do atoms get from a source to a surface, and what sets the deposition rate?**
> **Why does a film grow dense, porous, columnar or epitaxial?**
> **Where does film stress come from, and when does a coating crack or peel?**
> **How are the single crystals and patterned layers of electronics made, and which of those methods matter elsewhere?**

| Concept | Engineering destination |
|---|---|
| Mean free path, monolayer time, plasma sheath | Choosing vacuum level and process window |
| PVD, CVD, ALD | Tool coatings, optical and low-E glass, gate dielectrics, barrier films |
| Plating and sol–gel | Zinc and nickel on steel, Ni–P on moulds, anti-reflection glass |
| Growth modes, structure-zone models | Dense versus columnar films, quantum dots |
| Thermal and intrinsic stress, Stoney equation, delamination energy | Coating thickness limits, wafer bow, cracking of CVD coatings |
| Czochralski, float zone, Bridgman, epitaxy | Silicon wafers, sapphire, single-crystal turbine blades, LEDs |
| Oxidation, doping, lithography, etching | Microelectronics, MEMS sensors, microfluidic chips |
| Thermal spray, hard coatings | Thermal barriers, WC–Co wear coatings, implant coatings |

**Roadmap.** Why coatings exist (41.1) → vacuum and plasma (41.2) → PVD, CVD and ALD (41.3–41.5) → plating and sol–gel (41.6) → growth and microstructure (41.7) → stress and adhesion (41.8) → single crystals and epitaxy (41.9) → device processing (41.10) → thermal spray and hard coatings (41.11).

---

## 41.1 Why surfaces get their own materials

Many requirements are volume requirements (carry load, conduct heat, resist creep); many others are surface requirements (resist wear, corrosion, oxidation or reflection, bond to bone, insulate a gate). One material rarely meets both: a superalloy with enough aluminium and chromium to resist oxidation at 1100 °C would lose its creep strength (Chapter 33). The answer is a composite in thickness: a substrate optimized for the bulk carrying layers optimized for the surface. Coatings span seven orders of magnitude in thickness, and the process changes with thickness:

| Thickness | Typical processes | Examples |
|---|---|---|
| 0.1–10 nm | ALD, thermal oxidation, MBE | High-k gate oxide, Al$_2$O$_3$ passivation of solar cells |
| 10 nm–1 µm | Sputtering, evaporation, CVD, sol–gel | Low-E and anti-reflection stacks, interconnects, diffusion barriers |
| 1–20 µm | PVD/CVD hard coatings, plating, anodizing | TiAlN on tools, Ni and Cr plate, DLC on engine parts |
| 20 µm–2 mm | Thermal spray, galvanizing, weld overlay | Thermal barriers, WC–Co on shafts, zinc on steel |

Every process raises the same three questions: how material arrives, how it attaches and organizes, and what stress and adhesion it ends with.

---

## 41.2 Vacuum and plasma basics

### Mean free path

Vapour processes need vacuum so that atoms reach the substrate without excessive collisions, so that residual gases do not contaminate the film, and so that a plasma can be sustained. The first is set by the **mean free path**

$$
\lambda=\frac{k_BT}{\sqrt2\,\pi d^2 p}
$$

with $d$ the collision diameter (about 0.37 nm for N$_2$). At 298 K, $\lambda\approx68$ nm at atmospheric pressure, 6.8 mm at 1 Pa, 68 m at $10^{-4}$ Pa. The Knudsen number $\mathrm{Kn}=\lambda/L$ ($L$ the chamber size) separates ballistic transport ($\mathrm{Kn}\gg1$: evaporation, molecular-beam epitaxy) from continuum flow with boundary layers ($\mathrm{Kn}\ll1$: atmospheric CVD). Sputtering at 0.1–1 Pa lies between: atoms make a few collisions in flight.

> **Status of the principle: Mean free path from kinetic theory**
> *Derived.* Follows from the hard-sphere ideal gas with a Maxwell velocity distribution; $d$ is an effective diameter fitted to viscosity, so the result is good to tens of percent.

### Monolayer time

Contamination is usually the stricter criterion. Gas molecules strike a surface at the flux $\Phi=p/\sqrt{2\pi mk_BT}$; a surface has about $10^{19}$ sites per m$^2$, so with unit sticking it is covered in $\tau=n_s/\Phi$.

**Worked example — how good must the vacuum be?** For water ($m=18$ u) at 298 K, $\sqrt{2\pi mk_BT}=2.78\times10^{-23}$ kg m/s. At $10^{-4}$ Pa, $\Phi=3.6\times10^{18}$ m$^{-2}$s$^{-1}$ and $\tau\approx2.8$ s; a film growing at 1 nm/s (about four monolayers per second) could pick up nearly one contaminant molecule per growing monolayer. At $10^{-7}$ Pa, $\tau\approx2800$ s, about 46 minutes. That is why molecular-beam epitaxy and oxidation-sensitive films (aluminium mirrors, superconducting niobium) need ultra-high vacuum, while nitride tool coatings, which tolerate some oxygen, are made after pumping to about $10^{-3}$ Pa (Figure 41.1).

<!-- FIGURE 41.1 | figures/ch41/fig-41-1-vacuum-regimes.png | plot | Mean free path and monolayer time versus pressure, with operating windows of vapour processes. | Content: log-log, x-axis pressure 1e-8 to 1e5 Pa. Left y-axis N2 mean free path at 298 K, 1e-8 to 1e5 m (lambda = 6.8e-3 m / p[Pa]); marks 68 nm at 1e5 Pa, 6.8 mm at 1 Pa, 68 m at 1e-4 Pa. Right y-axis H2O monolayer time (sticking 1, 1e19 sites/m2), marks 2.8 s at 1e-4 Pa and 2800 s at 1e-7 Pa. Bottom bands: MBE (1e-8 to 1e-6 Pa), evaporation (1e-5 to 1e-3 Pa), magnetron sputtering (0.1 to 1 Pa), LPCVD/PECVD (10 to 300 Pa), APCVD (1e5 Pa). Dashed line at lambda = 0.5 m labelled 'Kn = 1 for a typical chamber'. -->

Rough pumps (rotary vane, dry scroll) reach about 1 Pa; turbomolecular pumps or cryopumps take over below. The ultimate pressure is set mostly by water outgassing from the walls, hence baking of UHV systems and load-locks in production tools. Pirani gauges, capacitance manometers and ionization gauges cover the range, and a residual-gas analyser identifies what remains.

### Plasmas

A processing **plasma** is a partially ionized gas ($10^{-6}$–$10^{-2}$ ionized) far from equilibrium: electrons at 1–10 eV, ions and neutrals near room temperature. Energetic electrons dissociate molecules into radicals (F from CF$_4$, N from N$_2$, SiH$_3$ from silane) that would otherwise need a 1000 °C furnace: chemistry of a hot gas at a cold substrate. The plasma screens potentials over the **Debye length** $\lambda_D=\sqrt{\varepsilon_0k_BT_e/n_ee^2}$, about 0.1 mm for $T_e=2$ eV and $n_e=10^{16}$ m$^{-3}$. Electrons are more mobile than ions, so surfaces charge negative and a thin positive-ion **sheath** forms in front of them; ions cross it and strike the surface with energies from tens of volts (floating) to hundreds (biased). Ion energy is the key plasma process variable: it densifies films (Section 41.7), makes etching directional (Section 41.10) and, if too high, causes damage. RF excitation at 13.56 MHz is used for insulating targets; inductively coupled sources decouple plasma density from ion energy.

> **Boundary.** Sheath theory and RF coupling belong to Engineering Physics; only the outcomes (radicals and a controllable ion energy) are used here. The *Materials Core (EEE)* book treats fab plasma processes in more depth.

---

## 41.3 Physical vapour deposition

In **physical vapour deposition (PVD)** the coating material is vaporized physically (heat or momentum transfer) and condensed on the substrate; reactive variants add N$_2$, O$_2$ or C$_2$H$_2$ to form compounds.

### Evaporation

The flux leaving a heated source follows the **Hertz–Knudsen** relation $J=\alpha_e(p_e-p)/\sqrt{2\pi mk_BT}$, with $p_e$ the equilibrium vapour pressure. Useful rates need $p_e\approx1$ Pa: about 950 °C for aluminium, 1400 °C for chromium and 1700 °C for titanium; refractory metals and oxides are evaporated by electron beam from a water-cooled copper hearth. A small planar source emits with a cosine distribution, so on a parallel substrate at height $h$ the thickness falls with radius $r$:

$$
\frac{t}{t_0}=\frac{1}{\left[1+(r/h)^2\right]^2}
$$

For $h=0.5$ m and $r=0.1$ m, $t/t_0=0.925$: 7.5 % thinner at the edge of a 200 mm part, which is why optical coaters use rotating planetary fixtures.

> **Status of the principle: Cosine-law thickness distribution**
> *Approximate.* Assumes ballistic transport, a small Lambertian source and unit sticking; deep crucibles, high rates and gas scattering distort it.

Evaporated atoms arrive with only 0.1–0.2 eV, so films are porous unless the substrate is hot or ions assist the growth. Uses: optical filters (with ion assist), aluminium on packaging film at more than 10 m/s, electron-beam PVD of zirconia thermal barriers (Section 41.11) and molecular-beam epitaxy (Section 41.9).

### Sputtering

An energetic ion striking a solid starts a collision cascade that ejects surface atoms. The **sputter yield** $Y$ for Ar$^+$ at 500 eV is typically:

| Target | Al | Ti | Cr | Fe | Ni | Cu | Ag | Au | Si | W |
|---|---|---|---|---|---|---|---|---|---|---|
| $Y$ (atoms/ion) | 1.05 | 0.51 | 1.18 | 1.10 | 1.33 | 2.35 | 3.12 | 2.40 | 0.50 | 0.57 |

> **Status of the principle: Sputter yields**
> *Empirical.* Sigmund's cascade theory with fitted corrections predicts $Y$ to about a factor of 1.5; yields rise with ion energy up to a few keV, then fall as ions penetrate deeper.

A **magnetron** traps secondary electrons in crossed electric and magnetic fields over the target, sustaining tens of mA/cm$^2$ at 300–600 V and 0.1–1 Pa, and eroding a racetrack groove.

**Worked example — erosion rate of a copper target.** At 20 mA/cm$^2$ = 200 A/m$^2$ the ion flux is $200/1.602\times10^{-19}=1.25\times10^{21}$ m$^{-2}$s$^{-1}$; the sputtered flux is $2.35$ times that, $2.93\times10^{21}$ m$^{-2}$s$^{-1}$. Copper has $8.49\times10^{28}$ atoms/m$^3$, so the racetrack recedes at $3.5\times10^{-8}$ m/s, about 2 µm/min. Only a fraction reaches the substrate, giving deposition rates of order 0.1–1 µm/min. (Counting secondary electrons as ions slightly overestimates the flux.)

Sputtering deposits almost any material, transfers alloy composition from target to film (the target surface reaches a steady state, whereas evaporation loses the volatile component first), produces denser films because atoms arrive with several eV, and scales to cylindrical targets metres long for glass and photovoltaic lines. In **reactive sputtering** (TiN, AlN, Al$_2$O$_3$, indium tin oxide) the target surface becomes "poisoned" by compound as gas flow rises; the compound sputters more slowly, so the rate collapses with hysteresis, and production systems hold the unstable transition mode by feedback on plasma emission. **HiPIMS** concentrates power into short pulses that ionize much of the sputtered metal, so substrate bias can steer it into dense, smooth coatings at the cost of rate.

### Cathodic arc and ion plating

A **cathodic arc** (20–30 V, 50–150 A) burns in micrometre spots that explode cathode material into a highly ionized plasma with 20–100 eV ions. It is the dominant industrial route to TiN, TiAlN and AlCrN on cutting tools because of high rate and adhesion, but ejects molten **macroparticles** that roughen the film unless magnetically filtered. **Ion plating** is PVD with a substrate bias of 50–200 V, which sputter-cleans the surface before deposition and densifies the film during it.

---

## 41.4 Chemical vapour deposition

In **chemical vapour deposition (CVD)** gaseous precursors react on a heated surface to give a solid and gaseous by-products, for example

$$
\mathrm{SiH_4\rightarrow Si+2H_2}\ \ (600\text{–}650\ ^\circ\mathrm{C}),\qquad \mathrm{TiCl_4+\tfrac12N_2+2H_2\rightarrow TiN+4HCl}\ \ (850\text{–}1000\ ^\circ\mathrm{C})
$$

Alumina for carbide inserts comes from AlCl$_3$, CO$_2$ and H$_2$ at about 1000 °C; SiC from methyltrichlorosilane infiltrated into fibre preforms forms the matrix of SiC/SiC composites (chemical vapour infiltration, Chapters 23 and 33). Diamond grows from a few percent methane in hydrogen activated by a hot filament or microwave plasma at 700–900 °C, where graphite is stable; atomic hydrogen etches graphitic carbon much faster than diamond, so diamond survives kinetically.

### The Grove model

Precursor diffuses through a boundary layer to the surface, adsorbs, reacts, and by-products leave; the slowest step controls the rate. Grove's model keeps two steps: transport flux $F_1=h_g(C_g-C_s)$, with $h_g$ a mass-transfer coefficient, and a first-order surface reaction $F_2=k_sC_s$. Setting $F_1=F_2$ gives the growth rate

$$
G=\frac{k_sh_g}{k_s+h_g}\,\frac{C_g}{N_1}
$$

with $N_1$ the atomic density of the film. If $k_s\ll h_g$ (low temperature) growth is **reaction-limited**, $G\approx k_sC_g/N_1$, strongly temperature-dependent but insensitive to flow; every surface in the hot zone grows at the same rate, so hundreds of wafers can be stacked in a **low-pressure CVD (LPCVD)** furnace and deep trenches are coated uniformly. If $k_s\gg h_g$ (high temperature) growth is **transport-limited**, $G\approx h_gC_g/N_1$, nearly temperature-independent but sensitive to gas flow and geometry.

> **Status of the principle: Grove model of CVD**
> *Approximate.* Assumes first-order surface kinetics and a stagnant-film boundary layer; adsorption saturation, gas-phase reactions and precursor depletion modify it, but the two-regime picture holds widely.

**Worked example — two regimes of silicon epitaxy.** Take $h_g=0.05$ m/s, $C_g=10^{22}$ m$^{-3}$ (about 0.2 % of the gas at 1 atm and 1100 °C), $N_1=5\times10^{28}$ m$^{-3}$, and $k_s=k_0\exp(-E_a/k_BT)$ with $E_a=1.6$ eV and $k_s=h_g$ at 1100 °C ($k_0=3.73\times10^4$ m/s). At 1100 °C, $G=0.025\times10^{22}/5\times10^{28}=5\times10^{-9}$ m/s $=0.30$ µm/min. At 900 °C, $k_s=4.98\times10^{-3}$ m/s and $G=0.054$ µm/min: 200 K cooler cuts the rate 5.5-fold. At 1300 °C, $k_s=0.28$ m/s and $G=0.51$ µm/min: 200 K hotter gains only 70 %. Production epitaxy runs near the knee, 1050–1150 °C, with reactors designed for uniform flow (Figure 41.2).

<!-- FIGURE 41.2 | figures/ch41/fig-41-2-cvd-grove-regimes.png | plot | Arrhenius plot of CVD growth rate showing reaction-limited and transport-limited regimes (Grove model). | Content: y-axis growth rate, log, 0.01 to 1 µm/min; x-axis 1000/T from 0.60 to 0.95 K^-1, top axis in °C. Curve G = ks*hg/(ks+hg)*Cg/N1 with hg = 0.05 m/s, Cg = 1e22 m^-3, N1 = 5e28 m^-3, ks = 3.73e4 exp(-1.6 eV/kT) m/s; points 800 °C 0.013, 900 °C 0.054, 1000 °C 0.154, 1100 °C 0.30, 1200 °C 0.43, 1300 °C 0.51 µm/min. Dashed asymptotes: reaction-limited line (Ea = 1.6 eV) and transport limit 0.6 µm/min. Second curve with hg = 0.1 m/s showing only the high-T branch moves. Regions labelled 'reaction-limited: LPCVD, conformal' and 'transport-limited: flow design matters'. -->

### Variants

| Variant | Pressure | Temperature | Typical use |
|---|---|---|---|
| APCVD | 10$^5$ Pa | 400–1200 °C | SiO$_2$ on float glass online, Si epitaxy |
| LPCVD | 10–100 Pa | 550–900 °C | Polysilicon and Si$_3$N$_4$ for MEMS |
| PECVD | 10–300 Pa | 200–400 °C | SiN$_x$ on solar cells, DLC, barrier films on polymers |
| MOCVD | 10$^3$–10$^5$ Pa | 500–1100 °C | GaN LEDs, GaAs and InP lasers |
| Thermal CVD on tools | 10$^3$–10$^5$ Pa | 850–1050 °C | TiC, TiCN, TiN, α-Al$_2$O$_3$ on WC–Co |
| Hot-filament/microwave | 10$^3$–10$^4$ Pa | 700–900 °C | Diamond coatings and windows |

PECVD coats temperature-sensitive substrates (finished solar cells, polymer film, stents) but leaves 10–25 at.% hydrogen in SiN$_x$:H and gives less dense films. Medium-temperature CVD of TiCN from acetonitrile at 700–900 °C reduces the decarburization of carbide substrates that otherwise forms a brittle η-phase (Co$_3$W$_3$C) at the interface.

---

## 41.5 Atomic layer deposition

**Atomic layer deposition (ALD)** splits CVD into two self-limiting half-reactions separated by purges. For alumina: trimethylaluminium reacts with surface OH groups until all are consumed; purge; water converts the Al–CH$_3$ surface back to Al–OH; purge. Each cycle adds a fixed **growth per cycle (GPC)**, about 0.1–0.12 nm for Al$_2$O$_3$ at 150–300 °C (less than a monolayer because bulky ligands block sites). Because each step saturates, ALD coats every exposed surface equally: trenches with aspect ratios above 50:1, catalyst pores, battery-electrode particles.

> **Status of the principle: Self-limiting ALD growth**
> *Empirical.* Saturation is observed within a temperature "ALD window" for each precursor pair; below it precursors condense, above it they decompose or desorb, so GPC is measured for each process.

**Worked example — ALD throughput.** A 10 nm Al$_2$O$_3$ moisture barrier at 0.11 nm per cycle needs $10/0.11\approx91$ cycles; at 4 s per cycle that is about 6 minutes, independent of area or topography. A 1 µm film would take ten hours. ALD therefore wins where films are thin and conformality is essential: 2 nm HfO$_2$ gate dielectrics, barriers for organic LEDs and flexible electronics, passivation of solar cells, a few cycles of Al$_2$O$_3$ on Li-ion cathode particles (Chapter 32) and anti-corrosion layers on medical devices. Spatial ALD, which moves the substrate between precursor zones, raises throughput for solar wafers and roll-to-roll film.

---

## 41.6 Electroplating, electroless plating and sol–gel

### Electroplating

The part is the cathode in a bath of metal ions (M$^{n+}$ + $ne^-$ → M). By Faraday's law the thickness grows at

$$
\frac{dh}{dt}=\frac{\eta_c\,i\,M}{nF\rho}
$$

with $i$ the current density, $M$ the molar mass, $\rho$ the deposit density, $F=96\,485$ C/mol and $\eta_c$ the **cathode current efficiency** (the fraction not wasted on hydrogen evolution).

> **Status of the principle: Faraday's law of electrolysis**
> *Fundamental.* Charge conservation applied to an electrode reaction; the uncertainty lives in the current efficiency, measured for each bath and current density.

**Worked example — nickel and hard chromium.** A Watts nickel bath at 2 A/dm$^2$ = 200 A/m$^2$ with $\eta_c=0.95$: $dh/dt=0.95\times200\times0.05869/(2\times96\,485\times8900)=6.49\times10^{-9}$ m/s $=23$ µm/h, so 25 µm takes about 1.1 h. Hard chromium from hexavalent baths has $n=6$ and $\eta_c\approx0.20$; at 40 A/dm$^2$, $dh/dt=0.20\times4000\times0.052/(6\times96\,485\times7190)$ m/s $\approx36$ µm/h, bought with twenty times the current density and four-fifths of it spent making hydrogen. That hydrogen enters the substrate, so plated high-strength steels (landing gear, fasteners above about 1000 MPa) are baked at about 190 °C to prevent hydrogen embrittlement (Chapter 35).

Current concentrates at edges, so deposits are thick on corners and thin in recesses; bath **throwing power** and additives (levellers, brighteners) even this out and refine the grain size. Additive chemistry also makes copper fill chip interconnect trenches bottom-up. Zinc is the most plated metal by tonnage (5–10 µm on electrogalvanized car sheet, protecting steel sacrificially); copper, tin, gold, silver and cadmium follow. Hexavalent chromium is carcinogenic and increasingly restricted, which drives its replacement by HVOF WC–Co and electroless Ni–P.

### Electroless plating

In **electroless** (autocatalytic) plating a chemical reducing agent replaces the current. Hypophosphite-reduced nickel co-deposits 2–13 wt% P; high-P deposits are amorphous and corrosion-resistant, about 500–600 HV as plated and 900–1000 HV after ageing at 400 °C precipitates Ni$_3$P. With no current distribution, thickness is uniform inside holes and on complex shapes: injection moulds, hydraulic parts, valves for oil and gas, aluminium hard-disk substrates. Electroless copper metallizes plastics and circuit-board holes.

> **Boundary.** Electrode potentials and electrode kinetics belong to Advanced Chemistry; corrosion electrochemistry is in Chapter 34.

### Sol–gel coatings

Metal alkoxides such as Si(OC$_2$H$_5$)$_4$ **hydrolyse** (Si–OR + H$_2$O → Si–OH + ROH) and **condense** (Si–OH + HO–Si → Si–O–Si + H$_2$O) into a sol and then an oxide gel, applied by dipping, spinning or spraying and fired at 300–600 °C. In dip coating at withdrawal speed $U$ the wet thickness at low capillary number follows the Landau–Levich relation

$$
h=0.94\,\frac{(\eta U)^{2/3}}{\gamma^{1/6}(\rho g)^{1/2}}
$$

For an alcoholic sol ($\eta=2$ mPa s, $\gamma=0.022$ N/m, $\rho=800$ kg/m$^3$), $h=3.2$ µm at 1 mm/s and 9.3 µm at 5 mm/s; drying and firing shrink this to roughly a tenth.

> **Status of the principle: Landau–Levich film thickness**
> *Approximate.* Lubrication theory for a Newtonian liquid with $\eta U/\gamma\ll1$ and no evaporation; real sols evaporate and gel during withdrawal, so the coefficient is calibrated.

Sol–gel needs no vacuum and coats large or curved parts: porous silica anti-reflection layers on solar glass (index about 1.25), photocatalytic TiO$_2$ self-cleaning glass, hybrid silica coatings that replace chromate conversion coatings on aircraft aluminium, bioactive coatings on implants. Single layers thicker than about 0.5–1 µm crack on drying, by the critical-thickness logic of Section 41.8.

---

## 41.7 Thin-film growth modes and structure-zone models

### Three growth modes

Adatoms diffuse, meet and form clusters. At equilibrium, whether the film wets the substrate is set by a surface-energy balance like Young's equation (Chapter 37), with $\gamma_s$, $\gamma_f$ and $\gamma_i$ the substrate, film and interface energies (Figure 41.3):

- **Frank–van der Merwe (layer)**, $\gamma_s\ge\gamma_f+\gamma_i$: each layer completes before the next (AlGaAs on GaAs).
- **Volmer–Weber (island)**, $\gamma_s<\gamma_f+\gamma_i$: three-dimensional islands that later coalesce. Most metals on oxides grow this way, which is why silver in a low-E stack is continuous only above about 8–10 nm and is grown on a ZnO seed layer that it wets better.
- **Stranski–Krastanov**: a wetting layer of one or a few monolayers, then islands once mismatch strain accumulates. Ge on Si (4 % mismatch) and InAs on GaAs (7 %) form self-assembled **quantum dots** (Chapter 30).

> **Status of the principle: Surface-energy criterion for growth mode**
> *Approximate.* An equilibrium argument; at high rates and low temperatures limited adatom diffusion can override it.

<!-- FIGURE 41.3 | figures/ch41/fig-41-3-growth-modes.png | schematic | The three growth modes: Frank–van der Merwe (layer), Volmer–Weber (island) and Stranski–Krastanov (layer plus island). | Content: three columns, each a substrate slab with film at coverages of 0.5, 1.5 and about 4 monolayers stacked top to bottom. Left: complete layers, label 'gamma_s >= gamma_f + gamma_i', example 'AlGaAs/GaAs'. Middle: hemispherical islands coalescing, label 'gamma_s < gamma_f + gamma_i', example 'Ag on glass'. Right: one to two wetting layers then pyramidal islands, label 'wetting layer + strain relief', example 'Ge/Si, InAs/GaAs quantum dots'. -->

### Structure-zone models

Practical polycrystalline films are far from equilibrium; their microstructure depends on how far arriving atoms move before burial. That mobility scales with the **homologous temperature** $T_s/T_m$ and, in plasma processes, with ion bombardment. The **structure-zone model** (Movchan–Demchishin for evaporation, extended by Thornton for sputtering pressure and Anders for ion energy) classifies the result (Figure 41.4):

| Zone | Approx. $T_s/T_m$ | Mechanism | Microstructure and properties |
|---|---|---|---|
| 1 | below 0.2–0.3 | Shadowing, negligible diffusion | Tapered columns with voids; porous, rough, poor barrier |
| T | 0.2–0.4 (sputtering, ion assist) | Surface diffusion plus bombardment | Dense fibrous grains, smooth, often compressive stress |
| 2 | 0.3–0.5 | Surface diffusion | Columnar grains through the thickness, faceted surface |
| 3 | above 0.5 | Bulk diffusion, recrystallization | Equiaxed, bulk-like grains |

> **Status of the principle: Structure-zone models**
> *Empirical.* Zone boundaries come from micrographs of many evaporated and sputtered films and shift with rate, impurities and ion energy; they guide process design qualitatively.

Refractory compounds have high $T_m$ (TiN about 3200 K), so at 450 °C ($T_s/T_m\approx0.23$) they would grow porous in zone 1; the energetic ions of arc and HiPIMS push them into dense zone T, which is as important as their chemistry. Electron-beam PVD zirconia thermal barriers are grown deliberately columnar at about 1000 °C: the separated columns open and close as the metal expands, giving strain tolerance (Chapter 33). Oblique incidence produces tilted, porous columns by shadowing, exploited in glancing-angle deposition of optical films and a defect on tool flanks.

<!-- FIGURE 41.4 | figures/ch41/fig-41-4-structure-zone-model.png | schematic | Structure-zone model for sputtered films: microstructure versus homologous temperature and ion bombardment. | Content: Thornton-style pseudo-3D diagram; x-axis Ts/Tm 0 to 1.0; depth axis Ar pressure 0.1 to 4 Pa (equivalently decreasing ion energy). Cross-section sketches: zone 1 (Ts/Tm < 0.25 at high pressure) tapered voided columns; zone T (0.2-0.4, widening at low pressure) dense fibrous grains; zone 2 (0.3-0.5) straight columns; zone 3 (> 0.5) equiaxed grains. Annotations: 'TiN at 450 °C: 0.23', 'Al at 25 °C: 0.32', 'EB-PVD YSZ at 1000 °C: 0.43'. -->

---

## 41.8 Film stress and adhesion

Nearly every film is stressed. Tensile stress cracks coatings, compressive stress buckles and spalls them, and either bends the substrate.

### Thermal stress

A film deposited at $T_d$ and cooled to $T$ on a thick substrate must follow the substrate's contraction. For an isotropic film in equi-biaxial plane stress

$$
\sigma_{th}=\frac{E_f}{1-\nu_f}\,(\alpha_s-\alpha_f)(T-T_d)
$$

where $E_f/(1-\nu_f)$ is the **biaxial modulus**. A film that expands more than its substrate ends in tension after cooling.

> **Status of the principle: Thermal mismatch stress**
> *Derived.* Linear thermoelasticity for a thin film on a much thicker substrate; fails if the film yields, creeps or cracks during cooling, or if properties vary strongly with temperature.

**Worked example — why CVD tool coatings crack.** TiN ($\alpha_f=9.4\times10^{-6}$ K$^{-1}$, $E_f=450$ GPa, $\nu_f=0.25$) deposited by CVD at 1000 °C on cemented carbide ($\alpha_s=5.5\times10^{-6}$ K$^{-1}$) and cooled to 20 °C has mismatch strain $(5.5-9.4)\times10^{-6}\times(20-1000)=+3.82\times10^{-3}$ and

$$
\sigma_{th}=\frac{450}{0.75}\ \mathrm{GPa}\times3.82\times10^{-3}=+2.3\ \mathrm{GPa}
$$

tensile, above the coating's strength. CVD inserts leave the furnace with fine **thermal cracks** perpendicular to the surface, tolerated because they do not enter the tough substrate (post-coat blasting adds compression). PVD at 450 °C gives a thermal term of only about $+1$ GPa, outweighed by compressive growth stress, so PVD coatings are crack-free; hence PVD for sharp tools in interrupted cutting, CVD for thick alumina on turning inserts. The same formula gives about $-180$ MPa in thermal SiO$_2$ on silicon cooled from 1000 °C (biaxial modulus 87 GPa).

### Intrinsic stress

- **Tension from grain coalescence**: islands that touch "zip up" into grain boundaries, stretching elastically; low-mobility evaporated metals reach hundreds of MPa.
- **Compression from atomic peening**: energetic particles drive atoms into interstitial sites and boundaries; biased PVD hard coatings reach $-3$ to $-6$ GPa and DLC up to $-10$ GPa. Higher sputtering pressure thermalizes the particles and swings stress toward tension.
- **Chemistry and phase change**: densification on annealing (sol–gel, hydrogen loss from PECVD films) gives tension; oxide growth with a larger volume gives compression (Pilling–Bedworth ratio, Chapter 34).

### The Stoney equation

A stressed film bends its substrate. For $h_f\ll h_s$,

$$
\sigma_f=\frac{E_s}{1-\nu_s}\,\frac{h_s^2}{6h_f}\left(\frac1R-\frac1{R_0}\right)
$$

Only substrate constants appear, which is why wafer-curvature measurement is the industrial standard; heating while measuring separates thermal from intrinsic stress. X-ray diffraction measures stress through lattice strain instead (Chapter 42).

> **Status of the principle: Stoney equation**
> *Approximate.* Assumes $h_f\ll h_s$ (below about 5 %), uniform equi-biaxial stress, small deflection and an isotropic substrate.

**Worked example — a silicon nitride film.** A 1.0 µm PECVD SiN$_x$ film on a 725 µm (100) silicon wafer (biaxial modulus 180.5 GPa) bends a flat wafer to $R=40$ m:

$$
\sigma_f=180.5\times10^9\times\frac{(725\times10^{-6})^2}{6\times1.0\times10^{-6}}\times\frac1{40}=395\ \mathrm{MPa}
$$

tensile if the film side is concave. That would buckle or crack a MEMS membrane, so MEMS nitride is tuned to 50–200 MPa tension by mixing plasma frequencies.

### Adhesion as interface fracture

Adhesion is a fracture-mechanics problem (Chapter 14): an interface crack grows when the energy it releases, $G$, exceeds the interface toughness $\Gamma_i$. A long interface crack under a film of thickness $h$ and biaxial stress $\sigma$ releases, in steady state under plane strain,

$$
G_{ss}=\frac{(1-\nu_f^2)\,\sigma^2h}{2E_f}\qquad\Longrightarrow\qquad h_c=\frac{2E_f\,\Gamma_i}{(1-\nu_f^2)\,\sigma^2}
$$

so films thicker than $h_c$ delaminate. Compressive films show buckling blisters ("telephone cords"); tensile films first crack in channels, with the same $\sigma^2h/E$ scaling.

> **Status of the principle: Steady-state delamination energy**
> *Derived.* Linear-elastic fracture mechanics for a thin film on a rigid substrate; needs a pre-existing interface flaw and neglects plasticity, which in metals raises the effective $\Gamma_i$.

**Worked example — thickness limit of a hard coating.** PVD TiN with $\sigma=-4$ GPa, $E_f=450$ GPa, $\nu_f=0.25$ on steel with $\Gamma_i=50$ J/m$^2$: $h_c=2\times450\times10^9\times50/(0.9375\times1.6\times10^{19})=3.0$ µm. With a poorly cleaned interface ($\Gamma_i=20$ J/m$^2$), $h_c=1.2$ µm. This is why stressed PVD coatings are kept to 2–5 µm, and why ion etching before deposition and graded Cr or CrN interlayers matter.

| Adhesion test | What it gives | Typical use |
|---|---|---|
| Tape (cross-hatch) | Pass/fail | Paints, decorative PVD |
| Pull-off stud | Tensile detachment stress (limited by glue, about 70–90 MPa) | Thermal spray, paints |
| Scratch test | Critical load $L_c$ for cracking or spallation (50–100 N for good TiN on steel) | Hard coatings |
| Four-point bend, double cantilever beam | Interface fracture energy $\Gamma_i$ (J/m$^2$) | Microelectronic stacks |

Only the last gives a material parameter; scratch loads depend on substrate hardness and thickness and are comparative.

---

## 41.9 Crystal growth for electronics and beyond

Silicon wafers need single crystals because grain boundaries scatter carriers and trap dopants; turbine blades because grain boundaries are where creep cavities form; quartz oscillators and sapphire windows for their optical and acoustic perfection. Growing them is solidification (Chapter 9) controlled so that only one nucleus grows.

### Czochralski growth

In the **Czochralski (CZ)** process, silicon melted at 1414 °C in a silica crucible is touched by an oriented seed, which is slowly withdrawn while seed and crucible counter-rotate. A thin **Dash neck** grown first lets dislocations from the thermal shock grow out; the crystal then widens to full diameter (300 mm, 2 m long). GaAs (under a boron-oxide encapsulant), sapphire and lithium niobate are pulled similarly.

The latent heat must be conducted away through the crystal, which bounds the pull rate:

$$
v_{max}=\frac{k_s}{\rho_s L_f}\left(\frac{dT}{dx}\right)_s
$$

For silicon ($k_s\approx22$ W m$^{-1}$K$^{-1}$ at the melting point, $\rho_s=2330$ kg/m$^3$, $L_f=1.8\times10^6$ J/kg) and 30 K/cm, $v_{max}=1.6\times10^{-5}$ m/s, about 0.9 mm/min, close to practice. The ratio of pull rate to gradient also decides whether excess vacancies (forming voids) or interstitials (forming loops) dominate the wafer.

Dopants with an equilibrium segregation coefficient $k_0=C_s/C_l<1$ are rejected into the melt. With a well-mixed melt and no solid diffusion, the Scheil equation (Chapter 9) gives

$$
C_s=k_0C_0(1-f)^{k_0-1}
$$

> **Status of the principle: Scheil segregation in crystal growth**
> *Approximate.* Assumes complete melt mixing, no back-diffusion and interface equilibrium; at real pull rates $k_{eff}$ lies between $k_0$ and 1 (Burton–Prim–Slichter), and crucible oxygen follows convection instead.

**Worked example — resistivity variation along an ingot.** With $k_0\approx0.8$ (B), 0.35 (P), 0.3 (As) and 0.008 (Ga), the concentration at $f=0.8$ relative to the seed end is $0.2^{k_0-1}$: 1.38, 2.85, 3.09 and 4.94. A boron-doped ingot thus varies by about 38 % along most of its length, a phosphorus-doped one by nearly a factor of three, so less of an n-type ingot meets a tight resistivity specification. Gallium, chosen for solar wafers because it avoids boron–oxygen light-induced degradation, rises fivefold, so solar makers sort by resistivity or recharge the melt continuously (Figure 41.5).

<!-- FIGURE 41.5 | figures/ch41/fig-41-5-cz-segregation.png | plot | Dopant concentration along a Czochralski silicon ingot (Scheil equation) for B, P, As and Ga, with a sketch of the puller. | Content: x-axis fraction solidified f, 0 to 0.95; y-axis Cs/C0, log, 0.005 to 5. Curves Cs/C0 = k0 (1-f)^(k0-1): B k0 = 0.8 (0.80 at f=0, 0.92 at 0.5, 1.10 at 0.8, 1.27 at 0.9); P 0.35 (0.35, 0.55, 1.00, 1.56); As 0.30 (0.30, 0.49, 0.93, 1.50); Ga 0.008 (0.008, 0.016, 0.040, 0.079). Inset: CZ puller with silica crucible, heaters, melt, counter-rotating seed and crystal with Dash neck, shoulder and body, argon flow. -->

### Float zone, Bridgman and other methods

**Float-zone (FZ)** growth passes an RF-heated molten zone along a rod held at its ends; with no crucible, oxygen is one to two orders of magnitude below the ~$10^{18}$ cm$^{-3}$ of CZ silicon, and repeated passes zone-refine. FZ silicon serves high-voltage power devices and detectors, limited to about 200 mm by the surface tension that holds the zone. **Bridgman** and gradient-freeze methods solidify a melt in a crucible moving through a gradient: GaAs, CdTe detectors and, with a spiral grain selector that passes only one grain from a chill, **single-crystal superalloy turbine blades** (Chapters 9 and 33). Sapphire for LED substrates and phone covers is grown by Kyropoulos and edge-defined film-fed growth, quartz hydrothermally at 300–400 °C and 100–150 MPa, and SiC by physical vapour transport at 2200–2400 °C (Chapter 26).

### Epitaxy

**Epitaxy** grows a crystalline film whose orientation is fixed by the substrate: homoepitaxy (Si on Si, for different doping) or heteroepitaxy (GaN on sapphire, SiGe on Si, YBCO superconductor on SrTiO$_3$). The lattice mismatch $f=(a_f-a_s)/a_s$ can be taken up elastically in a **pseudomorphic** layer until a critical thickness, beyond which **misfit dislocations** relax it. For 60° dislocations in a diamond-cubic film the Matthews–Blakeslee balance gives

$$
h_c=\frac{b\,(1-\nu\cos^2\alpha)}{8\pi f(1+\nu)\cos\lambda}\left[\ln\frac{h_c}{b}+1\right]
$$

with $b=a/\sqrt2$ and $\alpha=\lambda=60^\circ$.

> **Status of the principle: Matthews–Blakeslee critical thickness**
> *Approximate.* An equilibrium force balance giving where dislocations *can* form; nucleation barriers allow metastable layers several times thicker at low growth temperature.

**Worked example — strained SiGe.** By Vegard's law Si$_{0.8}$Ge$_{0.2}$ has $a=0.5431+0.2\times0.0227=0.5476$ nm and $f=0.84$ %. With $b=0.384$ nm and $\nu=0.28$, iteration gives $h_c\approx12$ nm; at 30 % Ge, $h_c\approx7$ nm. Strained SiGe below these thicknesses raises hole mobility in transistors. GaN on sapphire (16 % mismatch) is far beyond any coherent limit; grown on a low-temperature nucleation layer, it carries $10^8$–$10^9$ threading dislocations per cm$^2$, yet LEDs work because carriers localize in InGaN quantum wells (Chapter 28).

Epitaxial tools are vapour-phase epitaxy and MOCVD (Section 41.4) for production, **molecular-beam epitaxy** (elemental beams in UHV, growth followed layer by layer by electron diffraction) for quantum wells and superlattices, and pulsed laser deposition for complex oxides.

> **Boundary.** Wafer preparation, gettering, SOI substrates and device consequences of crystal defects are in the *Materials Core (EEE)* book; doping physics is in Chapter 26.

---

## 41.10 Oxidation, diffusion, implantation, lithography and etching: an overview

Integrated circuits are built from a few unit operations repeated hundreds of times; the same operations, at relaxed dimensions, make MEMS accelerometers and pressure sensors, inkjet heads, microfluidic chips and neural probes.

### Thermal oxidation

Silicon's native oxide is an excellent insulator with a low-defect interface. Oxidant diffuses through the SiO$_2$ and reacts at the Si/SiO$_2$ interface; equating the two fluxes gives the **Deal–Grove** relation

$$
x^2+Ax=B(t+\tau)
$$

with $B$ the parabolic constant (diffusion), $B/A$ the linear constant (interface reaction) and $\tau$ an offset for initial oxide. Thin oxides grow linearly, thick ones parabolically, the same law as metal oxidation (Chapter 34).

> **Status of the principle: Deal–Grove oxidation model**
> *Approximate.* A steady-state diffusion-plus-reaction model with fitted Arrhenius constants; good for wet oxidation and dry oxides above about 25–30 nm, but it underestimates the fast initial growth of very thin dry oxides.

**Worked example — dry versus wet oxidation at 1000 °C.** For (100) Si in dry O$_2$, $A=0.165$ µm, $B=0.0117$ µm$^2$/h, $\tau=0.37$ h. Solving, $x=\tfrac{A}{2}\left[\sqrt{1+(t+\tau)/(A^2/4B)}-1\right]$ with $A^2/4B=0.582$ h; one hour gives $0.0825\times(\sqrt{1+1.37/0.582}-1)=0.069$ µm = 69 nm, four hours 158 nm, and 100 nm needs $(0.01+0.0165)/0.0117-0.37=1.9$ h. In steam ($A=0.226$ µm, $B=0.287$ µm$^2$/h, $\tau=0$) one hour gives 435 nm. Water's higher solubility in silica makes wet oxidation about 25 times faster in the parabolic regime: thick field oxides are grown wet, thin gate oxides dry (Figure 41.6). Each nanometre of silicon consumed yields 2.2 nm of oxide, which stresses corners of patterned structures.

<!-- FIGURE 41.6 | figures/ch41/fig-41-6-deal-grove.png | plot | Oxide thickness versus time for dry and wet oxidation of (100) silicon at 1000 °C (Deal–Grove model). | Content: x-axis time 0 to 10 h; y-axis thickness 0 to 1700 nm, both linear. Dry O2 (A = 0.165 µm, B = 0.0117 µm^2/h, tau = 0.37 h): 69 nm at 1 h, 103 nm at 2 h, 158 nm at 4 h, 275 nm at 10 h. Wet H2O (A = 0.226 µm, B = 0.287 µm^2/h, tau = 0): 435, 653, 964, 1585 nm at the same times. Log-log inset (0.1 to 10 h) for wet: slope 1 (linear) at short times, 1/2 (parabolic) at long times. Side sketch: Si, SiO2, oxidant fluxes to surface, through oxide, reacting at Si/SiO2 interface. -->

### Diffusion doping and ion implantation

Diffusion from a surface source at 900–1200 °C gives erfc (constant surface concentration) or Gaussian (fixed dose) profiles with depth scale $2\sqrt{Dt}$ (Chapter 8); with $D\sim10^{-13}$ cm$^2$/s for B and P at 1100 °C, an hour moves dopant about 0.1 µm. Diffusion still forms the phosphorus emitter of most silicon solar cells and is the twin of carburizing steel (Chapter 15). **Ion implantation** sets dose exactly (counted from beam current) and depth by energy; ions stop in an approximately Gaussian profile

$$
N(x)=\frac{Q}{\sqrt{2\pi}\,\Delta R_p}\exp\left[-\frac{(x-R_p)^2}{2\Delta R_p^2}\right]
$$

For 30 keV boron in Si, $R_p\approx0.10$ µm and $\Delta R_p\approx0.039$ µm; a dose of $10^{15}$ cm$^{-2}$ peaks at $10^{15}/(2.507\times3.9\times10^{-6}\ \mathrm{cm})=1.0\times10^{20}$ cm$^{-3}$. Heavy doses amorphize the lattice; rapid thermal or laser annealing regrows it and activates the dopant with nanometres of diffusion. Nitrogen implantation also hardens titanium joint replacements and tool steels.

### Lithography

**Photolithography** projects a mask pattern into a photoresist. Resolution scales as

$$
R=k_1\frac{\lambda}{\mathrm{NA}}
$$

with $k_1\ge0.25$ for one exposure. ArF immersion ($\lambda=193$ nm, NA 1.35, $k_1\approx0.28$) resolves about 40 nm; EUV at 13.5 nm with NA 0.33 and $k_1\approx0.4$ about 16 nm, and high-NA EUV (0.55) about 10 nm. Depth of focus scales as $\lambda/\mathrm{NA}^2$, so wafers are polished flat by chemical–mechanical polishing.

> **Status of the principle: Lithographic resolution**
> *Approximate.* The $\lambda/\mathrm{NA}$ scaling follows from diffraction-limited imaging (as in the optical microscope, Chapter 42); $k_1$ lumps illumination, mask and resist effects and is empirical.

Chemically amplified resists, in which one photon releases an acid that catalyses many reactions, are materials problems in their own right. Outside chips, lithography patterns MEMS, PDMS microfluidic moulds and drug-delivery microneedles; electron-beam lithography and nanoimprint make nanostructures.

### Etching

Etches are judged by **selectivity** and **anisotropy**. Wet etches are mostly isotropic (HF removes SiO$_2$ but not Si, undercutting the mask), with one important exception: KOH or TMAH etch silicon {111} planes 50–100 times slower than {100}, so a square window on a (100) wafer becomes a pit bounded by {111} walls at 54.7°. A cavity of depth $d$ narrows by $2d/\tan54.7^\circ=1.41d$, so a 1 mm membrane after a 500 µm etch needs a 1.71 mm mask window; this is how piezoresistive pressure sensors (engine manifolds, disposable blood-pressure transducers) are made. **Reactive ion etching** combines radicals with ion bombardment, accelerating chemistry where ions strike the trench floor; the **Bosch process** alternates SF$_6$ etching and C$_4$F$_8$ sidewall passivation to cut vertical trenches hundreds of micrometres deep for MEMS gyroscopes, through-silicon vias and microfluidics.

> **Boundary.** Full process integration, CMP, metallization and contamination control are in the *Materials Core (EEE)* book.

---

## 41.11 Thermal spray and hard coatings

### Thermal spray

**Thermal spraying** heats powder or wire to a molten or softened state and propels it onto a grit-blasted surface. Each particle flattens into a **splat** a few micrometres thick that solidifies in microseconds; the coating is a stack of splats with oxide films, unmelted particles and pores. Coatings of 50 µm to several millimetres go on at kilograms per hour without heating the substrate above about 150 °C. The families trade particle temperature against velocity:

| Process | Gas temperature | Particle velocity | Porosity | Bond strength | Typical coatings |
|---|---|---|---|---|---|
| Flame | about 3000 °C | 40–100 m/s | 10–15 % | 10–30 MPa | Zn and Al on bridges |
| Arc wire | about 4000 °C | 100–200 m/s | 5–10 % | 20–40 MPa | Zn, Al, steel rebuild |
| Atmospheric plasma | 10 000–15 000 °C | 100–300 m/s | 2–20 % (designed) | 30–70 MPa | YSZ, Al$_2$O$_3$, hydroxyapatite |
| HVOF | about 2800 °C | 400–800 m/s | below 1 % | above 70 MPa | WC–Co, Cr$_3$C$_2$–NiCr, MCrAlY |
| Cold spray | below particle melting | 500–1200 m/s | below 0.5 % | 30–80 MPa | Cu, Al, Ti; aerospace repair |

Only plasma melts zirconia (2700 °C); high velocity gives density and adhesion with little oxidation. HVOF WC–Co (1100–1400 HV) is replacing hard chromium on landing-gear cylinders and hydraulic rods. **Cold spray** particles stay solid and bond by adiabatic shear instability above a critical velocity, giving oxide-free, compressively stressed deposits for repair and large-scale additive manufacturing (Chapter 40). Plasma-sprayed **thermal barriers** carry 10–20 % designed porosity and microcracks, lowering YSZ conductivity from about 2.3 to 0.8–1.0 W m$^{-1}$K$^{-1}$ and adding strain tolerance; EB-PVD columnar coatings are more durable on rotating blades, APS cheaper for combustors and vanes (Chapter 33). Plasma-sprayed **hydroxyapatite** (50–150 µm) on titanium hip stems and dental implants speeds bone bonding, with its crystallinity controlling dissolution in the body (Chapter 31).

### The hard-coating family

| Coating | Process | Thickness | Hardness (HV) | Oxidation limit in air | Typical use |
|---|---|---|---|---|---|
| Hard chromium | Electroplating | 20–500 µm | 800–1000 | about 400 °C (softens) | Hydraulic rods (being replaced) |
| Electroless Ni–P | Autocatalytic | 10–100 µm | 500–600; 900–1000 aged | — | Moulds, valves |
| TiN | PVD, CVD | 2–10 µm | 2000–2400 | 500–600 °C | General tools, implants, decorative |
| TiAlN/AlTiN | PVD | 2–5 µm | 3000–3500 | 800–900 °C | Dry, high-speed machining |
| CrN | PVD | 2–20 µm | 1800–2200 | about 700 °C | Forming tools, piston rings |
| α-Al$_2$O$_3$ | CVD | 3–15 µm | about 2000 | stable | Heat barrier on turning inserts |
| DLC | PECVD, PVD | 1–3 µm | 1500–5000 | about 350 °C | Fuel injectors, cam followers, low friction |
| CVD diamond | Hot-filament/microwave CVD | 5–30 µm | about 10 000 | about 600 °C | Machining Al–Si and CFRP |
| WC–Co | HVOF | 100–300 µm | 1100–1400 | about 500 °C | Landing gear, pump sleeves |

Two ideas run through modern hard coatings. **Nanolayers and nanocomposites** (TiN/CrN superlattices, nanocrystalline TiN in amorphous Si$_3$N$_4$) block dislocations and cracks, raising hardness and toughness: boundary strengthening (Chapter 13) at the nanometre scale. **Self-protection**: aluminium-rich nitrides grow a thin alumina scale at the hot edge, so TiAlN cuts dry where TiN fails. Substrate support matters too: a hard coating on a soft substrate cracks like an eggshell when the substrate yields, so steels are nitrided before PVD coating (a **duplex treatment**).

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are thickness, stress, texture and composition of a finished coating measured? | Chapter 42 |
| How can a 2 nm interfacial layer or a single grain boundary be analysed atom by atom? | Chapter 43 |
| How do films evolve while growing or in service? | Chapter 44 |
| Can adsorption energies and epitaxial strain be predicted from first principles? | Chapter 45 |
| How are growth morphologies simulated? | Chapter 46 (kinetic Monte Carlo, phase field) |
| How does one choose between PVD, CVD, spray and plating on cost? | Chapter 48 |
| What are the environmental costs of chromium plating, fluorinated etch gases and vacuum processing? | Chapter 49 |
| Why do thermal barriers and tool coatings ultimately fail? | Chapters 33, 36 and 37 (back reference) |
| Where does the diffusion physics of oxidation and doping come from? | Chapter 8 (back reference) |

**Next:** Chapter 42 opens Part X by asking how the structures discussed throughout this book (grains, phases, films, defects) are actually seen and measured in a materials laboratory.
