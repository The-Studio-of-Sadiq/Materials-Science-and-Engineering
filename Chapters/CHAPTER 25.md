# Chapter 25 — Electrical, Dielectric and Superconducting Materials

*Part VI · Physical and Functional Properties*

A wind-farm operator commissions a 30 km export cable from an offshore substation. Two years later a joint in the cable fails and the line is out of service for four months while a repair vessel is chartered. The post-mortem draws three materials lessons from one metre of cable. The copper conductor had been specified by cross-section, but an aluminium alternative of 1.6 times the area would have weighed half as much and carried the same current. The cross-linked polyethylene insulation was in good condition everywhere except next to the joint, where a sharp edge on a connector had concentrated the field, and a small cavity in the hand-applied joint insulation had sustained partial discharges for months until an electrical tree bridged the wall. And the monitoring sensors in the joint, piezoelectric acoustic detectors that might have heard the discharges, had been fitted but not connected.

This chapter treats materials that carry current by electrons or by ions, materials that block it while storing field energy, materials whose polarization couples to stress and temperature, and materials that carry current with no resistance at all. Semiconductors, where the carrier density itself is the design variable, follow in Chapter 26. The *Materials Core (EEE)* book, Chapters 7–9 and 17, treats each topic in more depth.

> **Why does a small addition of almost any element lower the conductivity of copper, and why do engineers accept it?**
> **How can a ceramic conduct electricity well enough to be the electrolyte of a fuel cell?**
> **Why does a polymer insulator that withstands 200 kV/mm in a laboratory film fail at 20 kV/mm in a cable?**
> **Why do practical superconducting magnets use alloys and brittle compounds rather than the elements that superconduct best?**

| Concept | Engineering destination |
|---|---|
| Drude conductivity, mobility, scattering | Conductor sizing in power, aerospace and automotive wiring; electrical heating elements |
| Matthiessen and Nordheim rules | Choosing conductor alloys that trade conductivity for strength (overhead lines, springs, welding electrodes) |
| Ionic conduction, Nernst–Einstein relation | Solid-oxide fuel cells, oxygen sensors in car exhausts, solid-state batteries |
| Permittivity, polarization mechanisms, loss tangent | Capacitors, cable insulation, PCB laminates, radomes, microwave and RF heating |
| Breakdown, partial discharge, ageing | High-voltage cables, motor windings, outdoor insulators, battery-pack insulation |
| Ferro-, piezo- and pyroelectricity | Ultrasound probes, fuel injectors, sonar, structural health monitoring, infrared detectors |
| Superconductivity and flux pinning | MRI and NMR magnets, particle accelerators, fusion magnets, power cables, SQUID sensors |

**Roadmap.** Conduction in metals and alloys (25.1) → ionic conduction and solid electrolytes (25.2) → dielectric polarization, permittivity and loss (25.3) → breakdown and insulation (25.4) → ferroelectric, piezoelectric and pyroelectric materials (25.5) → superconductivity (25.6).

---

## 25.1 Conduction in metals: Drude, Matthiessen and alloy resistivity

### Resistivity as a material property

A uniform bar of length $L$ and cross-section $A$ has resistance

$$
R=\rho\,\frac{L}{A}
$$

where the **resistivity** $\rho$ ($\Omega\,\mathrm m$) depends only on the material and its state; its reciprocal is the conductivity $\sigma=1/\rho$ ($\mathrm{S/m}$). The local form, $\mathbf J=\sigma\mathbf E$, is Ohm's law at a point. In cubic metals $\sigma$ is a scalar; in graphite, many oxides and fibre composites it is a second-rank tensor (Chapter 4), so the current need not flow along the field.

Resistivity spans more than 25 orders of magnitude at room temperature, from silver ($1.6\times10^{-8}\ \Omega\,\mathrm m$) to PTFE (above $10^{16}\ \Omega\,\mathrm m$), with superconductors at exactly zero. In practice two engineering units are common: **% IACS**, the conductivity as a percentage of annealed standard copper ($\rho=1.7241\ \mu\Omega\,\mathrm{cm}$, i.e. 58.0 MS/m), and **sheet resistance** $R_s=\rho/t$ in ohms per square for films and coatings.

### The Drude model

Treat the conduction electrons of a metal as a gas of $n$ free carriers per unit volume, of charge $-e$ and mass $m$, accelerated by the field and randomized by collisions at an average interval $\tau$ (the **relaxation time**). In steady state the mean (drift) velocity is $v_d=e\tau E/m$, and the current density $J=nev_d$ gives

$$
\sigma=\frac{ne^2\tau}{m}=ne\mu,\qquad \mu=\frac{e\tau}{m}
$$

where $\mu$ is the **mobility**, drift velocity per unit field. The two factors separate what the engineer cannot change from what they can: $n$ is fixed by the electronic structure (about one to three conduction electrons per atom in simple metals), while $\tau$ is set by scattering from lattice vibrations, solute atoms, vacancies, dislocations, grain boundaries and surfaces — all of which are microstructure.

> **Status of the principle: Drude conductivity $\sigma=ne^2\tau/m$**
> *Approximate.* It assumes one relaxation time for free carriers. The form survives in band theory with $m$ replaced by an effective mass and $\tau$ evaluated at the Fermi energy (Chapter 26 and the Engineering Physics book); the classical model gets the electron speed and heat capacity wrong but the conductivity formula right.

**Worked example — what limits current in a copper conductor.** Copper has $n=8.47\times10^{28}\ \mathrm{m^{-3}}$ (one electron per atom) and $\rho=1.68\times10^{-8}\ \Omega\,\mathrm m$ at 20 °C. The relaxation time is

$$
\tau=\frac{m}{ne^2\rho}=\frac{9.11\times10^{-31}}{(8.47\times10^{28})(1.602\times10^{-19})^2(1.68\times10^{-8})}=2.49\times10^{-14}\ \mathrm s
$$

and the mobility $\mu=e\tau/m=4.39\times10^{-3}\ \mathrm{m^2/(V\,s)}$, or 44 cm²/(V s) — far lower than in silicon (1350 cm²/(V s), Chapter 26). Copper conducts well not because its electrons are mobile but because there are so many of them. At a typical design current density of 5 A/mm² ($5\times10^6\ \mathrm{A/m^2}$) the drift velocity is $v_d=J/(ne)=3.7\times10^{-4}\ \mathrm{m/s}$, less than half a millimetre per second. The electrons that carry the current actually move at the Fermi velocity, $v_F=1.57\times10^6\ \mathrm{m/s}$, so the mean free path between collisions is $\ell=v_F\tau=39$ nm. That length is the key to size effects: once a wire, film or grain approaches tens of nanometres, its surfaces and boundaries become extra scatterers and resistivity rises — the reason on-chip copper interconnects narrower than about 40 nm have two or more times the bulk resistivity.

The current-carrying limit of a conductor is therefore never the electrons; it is heating ($I^2R$ loss against the thermal rating of the insulation, Section 25.4), voltage drop, and at very high current densities in microelectronics, electromigration (Chapter 36).

### Temperature dependence and Matthiessen's rule

Above roughly a third of the Debye temperature (Chapter 24), the number of phonons is proportional to $T$, so the phonon-limited resistivity rises linearly: copper's temperature coefficient of resistance (TCR) is $\alpha\approx3.9\times10^{-3}\ \mathrm{K^{-1}}$, so its resistance rises 39 % from 20 °C to 120 °C. Below about 30 K the phonons freeze out and the resistivity falls to a constant **residual resistivity** set by impurities and defects. Because independent scattering mechanisms add their rates, the resistivities add:

$$
\rho(T)=\rho_{\mathrm{ph}}(T)+\rho_{\mathrm{imp}}+\rho_{\mathrm{def}}
$$

This is **Matthiessen's rule** (Figure 25.1). Solute atoms add a temperature-independent term, roughly proportional to concentration at low levels; cold work adds a small term from dislocations and vacancies (typically a few per cent for copper); grain boundaries add a term that matters only when grains are smaller than about a micrometre. The ratio of room-temperature to 4.2 K resistance, the **residual resistance ratio** (RRR), is a sensitive purity test: oxygen-free copper has RRR 100–300, and superconductor stabilizer copper (Section 25.6) is specified above 100.

> **Status of the principle: Matthiessen's rule**
> *Empirical.* It follows from adding independent scattering rates. The mechanisms are not strictly independent, so deviations of a few per cent of the residual term are common, and the rule fails in concentrated alloys and magnetic systems; it remains the standard first estimate.

<!-- FIGURE 25.1 | figures/ch25/fig-25-1-matthiessen-rho-vs-t.png | plot | Matthiessen's rule: solute and defects shift the resistivity–temperature curve upward without changing its slope. | Content: x-axis temperature 0 to 400 K; y-axis resistivity 0 to 5 micro-ohm cm. Curves: high-purity annealed Cu (residual about 0.002, 1.7 at 293 K, linear above about 100 K, T^5 knee below about 40 K); Cu + 0.5 at.% Ni (same shape shifted up by about 0.56, reaching about 2.26 at 293 K); the same alloy cold-worked (shifted up a further 0.04). Vertical arrows at 300 K labelling rho_ph(T), rho_imp, rho_def. Inset: RRR = R(293 K)/R(4.2 K), with values 100–300 for OFE Cu. -->

### Alloy resistivity: Nordheim's rule and the strength–conductivity trade

In a disordered binary solid solution A$_{1-x}$B$_x$ the residual resistivity follows **Nordheim's rule**,

$$
\rho_{\mathrm{imp}}=C\,x(1-x)
$$

a parabola with its maximum at 50 at.%. For dilute solutions it reduces to $\rho_{\mathrm{imp}}\approx Cx$. The constant $C$ grows with the difference in valence and electronic structure between solute and solvent: in copper, 1 at.% of silver adds only about 0.14 $\mu\Omega\,\mathrm{cm}$, 1 at.% of nickel about 1.1, and 1 at.% of phosphorus or iron several $\mu\Omega\,\mathrm{cm}$ — which is why phosphorus-deoxidized copper for plumbing is unsuitable for conductors and why conductor copper is refined to 99.95 % or better. Ordered alloys break the rule: the Cu$_3$Au and CuAu ordered phases have far lower resistivity than the same compositions quenched disordered, because a periodic arrangement does not scatter Bloch waves.

The engineering consequence is the **strength–conductivity trade-off**. Every mechanism that strengthens a metal (Chapter 13) also scatters electrons, but not equally. Solid-solution strengthening is expensive in conductivity, because each solute atom is a scatterer. Precipitation and dispersion strengthening are cheap: a small volume fraction of coarse precipitates scatters little, so an age-hardened alloy whose solute has been pulled out of solution can be both strong and conductive. Cold work is cheaper still. Table 25.1 shows the result across conductor alloys.

| Material (condition) | Conductivity (% IACS) | Yield strength (MPa) | Typical use |
|---|---|---|---|
| Oxygen-free Cu (annealed) | 101 | 60–70 | Busbars, windings, superconductor stabilizer |
| Cu (hard-drawn) | 97 | 300–380 | Contact wire for railways |
| Cu–Cr–Zr (aged) | 75–85 | 350–450 | Resistance-welding electrodes, rocket-engine liners |
| Cu–Ni–Si (aged) | 40–50 | 550–750 | Connector springs, lead frames |
| Cu–Be C17200 (aged) | 20–25 | 1000–1200 | Springs, non-sparking tools |
| Brass Cu–30Zn | 27–28 | 100–450 | Terminals, cheap contacts |
| Al 1350 (EC grade, H19) | 61–62 | 160–190 | Overhead line strands, cable conductors |
| Al 6101/6201 (T6/T81) | 52–57 | 200–310 | Self-supporting overhead conductors, busbars |
| Constantan Cu–45Ni | 3.5 | 200–450 | Strain gauges, thermocouples (low TCR) |
| Nichrome Ni–20Cr | 1.6 | 300–400 | Heating elements to 1150 °C |

*Table 25.1 — Representative conductivity and strength of conductor and resistance alloys at room temperature (typical values; strength varies with temper).*

At the other extreme, high resistivity is the goal. Heating elements (Ni–Cr, Fe–Cr–Al) need resistivity above 1 $\mu\Omega\,\mathrm m$ and a protective oxide scale (Chapter 34). Precision resistors and strain gauges need a near-zero TCR: in constantan and manganin the residual resistivity is so large that the small phonon term barely changes it, giving TCRs of order $10^{-5}\ \mathrm{K^{-1}}$.

**Worked example — copper or aluminium for a conductor of fixed resistance?** A conductor of length $L$ must have resistance $R$; its area is $A=\rho L/R$ and its mass $m=dAL=(\rho d)L^2/R$, where $d$ is the density. The material index to minimize is $\rho d=d/\sigma$. For annealed copper, $\sigma=58.0$ MS/m and $d=8960\ \mathrm{kg/m^3}$; for EC aluminium, $\sigma=35.5$ MS/m and $d=2700\ \mathrm{kg/m^3}$. The aluminium conductor needs $58.0/35.5=1.63$ times the cross-section, but its mass ratio is

$$
\frac{(d/\sigma)_{\mathrm{Al}}}{(d/\sigma)_{\mathrm{Cu}}}=\frac{2700/35.5}{8960/58.0}=0.49
$$

Aluminium carries the same current at half the weight. That is why overhead transmission lines (where the span weight sets tower spacing), aircraft power feeders and many electric-vehicle battery busbars use aluminium, while copper keeps the jobs where volume is scarcer than mass (motor windings, transformers, printed circuits) and where joints must be simple — aluminium's oxide, creep under bolt pressure and galvanic couple with copper make its joints the weak point (Chapter 35).

---

## 25.2 Ionic conduction and solid electrolytes

### Ions as carriers

In ionic solids, glasses and some polymers, the carriers are ions moving by thermally activated jumps between lattice sites, through the vacancy and interstitial mechanisms of Chapter 8. The conductivity has the same form as for electrons, $\sigma=nq\mu$, but now the mobility is tied to diffusion through the **Nernst–Einstein relation**:

$$
\sigma=\frac{nq^2D}{k_BT}
$$

where $n$ is the concentration of mobile ions of charge $q$ and $D$ their diffusion coefficient. Because $D=D_0\exp(-E_m/k_BT)$ and the number of mobile defects may itself be activated, the conductivity is Arrhenius:

$$
\sigma T=A\exp\!\left(-\frac{E_a}{k_BT}\right)
$$

with activation energies typically 0.2–1.2 eV. A useful solid electrolyte must therefore satisfy three structural conditions: a high concentration of mobile defects (vacancies or interstitials), a connected network of energetically similar sites to jump between, and a low barrier between them. Equally important, its electronic conductivity must be negligible, so that the material passes ions but blocks electrons — otherwise a fuel cell or battery would short-circuit internally.

> **Status of the principle: Nernst–Einstein relation**
> *Derived.* It follows from the fluctuation–dissipation link between random-walk diffusion and drift in a field. It holds exactly for independent, non-interacting carriers; in concentrated or correlated conductors the measured conductivity differs from the tracer-diffusion value by the Haven ratio, typically 0.3–1.

### Defect engineering: doped zirconia and ceria

Pure ZrO$_2$ is a poor conductor. Substituting Y$^{3+}$ for Zr$^{4+}$ does two things. It stabilizes the cubic fluorite structure (Chapter 7, ZrO$_2$–Y$_2$O$_3$), and, by the Kröger–Vink charge balance of Chapter 5, every two Y$^{3+}$ ions create one oxygen vacancy:

$$
\mathrm{Y_2O_3}\xrightarrow{\mathrm{ZrO_2}}2\mathrm{Y'_{Zr}}+3\mathrm{O_O^{\times}}+\mathrm{V_O^{\bullet\bullet}}
$$

At 8 mol% Y$_2$O$_3$ (8YSZ) about 4 % of the oxygen sites are vacant, and oxide ions hop through them. Conductivity rises with dopant level up to about 8–10 mol%, then falls, because vacancies bind to dopant cations and to each other — a clean example of defect chemistry setting a property maximum. Gadolinium-doped ceria (GDC) and strontium- and magnesium-doped lanthanum gallate (LSGM) conduct better at lower temperature, but ceria is partly reduced in hydrogen and becomes a mixed conductor.

These materials are the core of **solid-oxide fuel cells and electrolysers** (Chapter 32), of the zirconia **lambda sensor** that controls the air–fuel ratio of every petrol engine (an oxygen concentration cell whose voltage follows the Nernst equation), and of oxygen pumps for industrial gas analysis.

### The family of fast-ion conductors

| Electrolyte | Mobile ion | Conductivity (S/cm) at temperature | Application |
|---|---|---|---|
| 8YSZ (cubic ZrO$_2$–Y$_2$O$_3$) | O$^{2-}$ | 0.03 at 800 °C | SOFC, lambda sensor |
| Gd-doped CeO$_2$ | O$^{2-}$ | 0.02–0.03 at 600 °C | Intermediate-temperature SOFC |
| Na $\beta''$-alumina | Na$^+$ | 0.2–0.4 at 300 °C | Sodium–sulfur and ZEBRA batteries |
| $\alpha$-AgI (above 147 °C) | Ag$^+$ | 1–2 at 150 °C | Model superionic conductor |
| Li$_7$La$_3$Zr$_2$O$_{12}$ garnet (LLZO, doped) | Li$^+$ | $10^{-4}$–$10^{-3}$ at 25 °C | Solid-state lithium batteries |
| Li$_{10}$GeP$_2$S$_{12}$ (sulfide) | Li$^+$ | $\approx10^{-2}$ at 25 °C | Solid-state lithium batteries |
| LiPF$_6$ in carbonate (liquid, reference) | Li$^+$ | $\approx10^{-2}$ at 25 °C | Commercial Li-ion cells |
| Nafion (hydrated) | H$^+$ | $\approx0.1$ at 80 °C | PEM fuel cells and electrolysers |
| Soda-lime glass | Na$^+$ | $\approx10^{-13}$ at 25 °C | (an insulator, but ions drift under DC) |

*Table 25.2 — Representative ionic conductivities (typical; values depend on dopant, density and microstructure).*

<!-- FIGURE 25.2 | figures/ch25/fig-25-2-ionic-conductivity-arrhenius.png | plot | Arrhenius plot of ionic conductivity: fast-ion conductors reach liquid-electrolyte values, but most oxide conductors need high temperature. | Content: x-axis 1000/T from 0.8 to 3.6 K^-1 with a secondary top axis in degrees C (1000, 800, 600, 400, 200, 25); y-axis log10 sigma from -8 to 0 (S/cm). Straight lines: 8YSZ (0.03 S/cm at 800 C, Ea 0.95 eV, about 2.9e-3 at 600 C); Gd-doped CeO2 (about 0.025 at 600 C, Ea 0.7 eV); Na beta''-alumina (0.3 at 300 C, Ea 0.3 eV); LLZO garnet (5e-4 at 25 C, Ea 0.35 eV); Li10GeP2S12 (1e-2 at 25 C, Ea 0.25 eV); alpha-AgI segment above 147 C at about 1 to 2 S/cm with a vertical jump at the transition; Nafion (0.1 at 80 C, short segment). Horizontal dashed band at 1e-2 labelled liquid Li-ion electrolyte. Shaded target region sigma > 1e-2 S/cm. -->

Figure 25.2 compares them on an Arrhenius plot. Several structural motifs recur. In $\beta$-alumina the Na$^+$ ions move in loosely packed planes between spinel blocks, so conduction is two-dimensional. In $\alpha$-AgI the iodide sublattice offers many more interstitial sites than there are silver ions, so the cation sublattice is effectively molten. In sulfide lithium conductors the large, polarizable S$^{2-}$ anions lower the hopping barrier. In Nafion, protons move through hydrated nanochannels formed by phase separation of the sulfonated side chains — a polymer conductor whose performance depends on keeping its water content. Even soda-lime glass conducts by sodium drift, which is why it is avoided in high-voltage DC insulators.

Microstructure enters through **grain boundaries**. In polycrystalline YSZ and LLZO the boundaries carry a space-charge layer depleted of mobile defects, and at low temperature the grain-boundary resistance can exceed the bulk value by an order of magnitude. Impedance spectroscopy (Chapter 42) separates the two. Densification is equally critical: porosity both lowers conductivity and, in lithium garnets, lets lithium dendrites grow along voids and boundaries to short the cell.

**Worked example — how thin must a fuel-cell electrolyte be?** An SOFC loses voltage across its electrolyte in proportion to the area-specific resistance $\mathrm{ASR}=t/\sigma$. Take 8YSZ with $\sigma=0.030$ S/cm at 800 °C and $E_a=0.95$ eV. A 150 µm self-supporting electrolyte has $\mathrm{ASR}=0.015\ \mathrm{cm}/0.030\ \mathrm{S\,cm^{-1}}=0.50\ \Omega\,\mathrm{cm^2}$, which at a typical 0.5 A/cm² wastes 0.25 V of a cell voltage of about 0.8 V. A 10 µm film on a porous anode support gives $0.033\ \Omega\,\mathrm{cm^2}$, a loss of only 17 mV. Lowering the operating temperature to 600 °C (cheaper steel interconnects, slower degradation) reduces the conductivity by the Arrhenius factor:

$$
\sigma_{600}=0.030\exp\!\left[-\frac{0.95\ \mathrm{eV}}{k_B}\left(\frac{1}{873\ \mathrm K}-\frac{1}{1073\ \mathrm K}\right)\right]=2.9\times10^{-3}\ \mathrm{S/cm}
$$

a factor of 10.5 lower. The same 10 µm film now has ASR 0.35 $\Omega\,\mathrm{cm^2}$; to keep it below a target of 0.15 $\Omega\,\mathrm{cm^2}$ the film would have to be about 4 µm thick and pinhole-free over the whole cell, which is why intermediate-temperature cells switch to GDC or LSGM instead. The design problem is solved by defect chemistry (a better conductor) and thin-film processing (Chapter 41), not by geometry alone.

---

## 25.3 Dielectric polarization, permittivity and loss

### Polarization and permittivity

An insulator in an electric field does not conduct, but its charges shift: bound electrons relative to nuclei, cations relative to anions, permanent molecular dipoles toward the field. The dipole moment per unit volume is the **polarization** $\mathbf P$, and for a linear isotropic dielectric

$$
\mathbf D=\varepsilon_0\mathbf E+\mathbf P=\varepsilon_0\varepsilon_r\mathbf E,\qquad \mathbf P=\varepsilon_0(\varepsilon_r-1)\mathbf E
$$

The **relative permittivity** $\varepsilon_r$ (dielectric constant) is the factor by which the material increases the capacitance of a capacitor over vacuum: $C=\varepsilon_0\varepsilon_rA/t$ for a parallel plate. It also sets signal speed, $v=c/\sqrt{\varepsilon_r}$, in cables and circuit boards.

Four mechanisms contribute, each with its own structural origin and its own speed:

- **Electronic polarization** — distortion of electron clouds. Present in every material, it responds up to optical frequencies and sets the refractive index, $n^2\approx\varepsilon_{r,\infty}$ (Chapter 28). Typical contribution 2–3 in polymers and glasses, up to 5–7 in high-index oxides.
- **Ionic (atomic) polarization** — relative displacement of cation and anion sublattices. It responds up to the infrared (around $10^{13}$ Hz) and is large in ionic crystals: it is why alumina has $\varepsilon_r\approx9.8$ while its optical $n^2$ is only 3.1.
- **Orientational (dipolar) polarization** — rotation of permanent dipoles (water, C–Cl and C=O groups in polymers). It is strongly temperature-dependent and slow, relaxing between kilohertz and gigahertz. Water has $\varepsilon_r\approx80$ for this reason.
- **Interfacial (space-charge, Maxwell–Wagner) polarization** — accumulation of mobile charges at grain boundaries, filler interfaces and electrodes. It dominates at low frequency in composites, moist materials and ceramics with conductive grains.

The local field acting on an atom in a dense solid is larger than the applied field because of the neighbours' polarization. For cubic or isotropic materials this gives the **Clausius–Mossotti relation**,

$$
\frac{\varepsilon_r-1}{\varepsilon_r+2}=\frac{N\alpha}{3\varepsilon_0}
$$

linking the macroscopic permittivity to the number density $N$ and polarizability $\alpha$ of the constituents. It fails, as the denominator approaches zero, where ferroelectric instability sets in (Section 25.5).

> **Status of the principle: Clausius–Mossotti relation**
> *Approximate.* It assumes a Lorentz local field, valid for cubic or random isotropic arrangements of non-interacting point dipoles. It works well for gases, non-polar liquids and simple cubic crystals, and fails for polar liquids, low-symmetry crystals and near ferroelectric transitions.

### Complex permittivity, relaxation and loss

No polarization is instantaneous. In an alternating field the polarization lags, and the permittivity becomes complex, $\varepsilon_r^*=\varepsilon'-i\varepsilon''$. The real part $\varepsilon'$ stores energy; the imaginary part $\varepsilon''$ dissipates it. The ratio is the **loss tangent**:

$$
\tan\delta=\frac{\varepsilon''}{\varepsilon'}
$$

The power dissipated per unit volume in a field of amplitude $E_0$ (rms $E$) at angular frequency $\omega$ is

$$
p=\omega\varepsilon_0\varepsilon''E^2=\omega\varepsilon_0\varepsilon'\tan\delta\,E^2
$$

For a relaxing dipole population with a single relaxation time $\tau$, the **Debye equation** gives

$$
\varepsilon^*(\omega)=\varepsilon_\infty+\frac{\varepsilon_s-\varepsilon_\infty}{1+i\omega\tau}
$$

so $\varepsilon'$ falls in a step from its static value $\varepsilon_s$ to $\varepsilon_\infty$ around $\omega\tau=1$, and $\varepsilon''$ shows a loss peak there. Ionic and electronic polarization appear as resonances in the infrared and ultraviolet (Figure 25.3). Because $\tau$ is thermally activated, loss peaks move to higher frequency on heating; the polymer relaxations of Chapter 20 appear this way, and dielectric spectroscopy is one way to measure $T_g$.

> **Status of the principle: Debye relaxation**
> *Approximate.* It assumes identical, non-interacting dipoles with one relaxation time. Real polymers and glasses show broadened, asymmetric peaks (fitted by Cole–Cole or Havriliak–Negami forms) because their environments are disordered.

<!-- FIGURE 25.3 | figures/ch25/fig-25-3-dielectric-spectrum.png | plot | The dielectric spectrum: each polarization mechanism drops out above its characteristic frequency, with a loss peak or resonance where it does. | Content: x-axis frequency 1e0 to 1e17 Hz (log), with bands labelled power (50 Hz), RF, microwave, IR, visible, UV. Top panel: epsilon' stepping down from about 12 (interfacial + dipolar + ionic + electronic) through plateaus 8, 4.5, 2.3 with steps near 1e2 Hz (interfacial), 1e8 Hz (dipolar, Debye step), 1e13 Hz (ionic resonance, with overshoot), 1e15 Hz (electronic resonance). Bottom panel: epsilon'' with a broad Debye loss peak at the dipolar step, sharp resonance peaks at the ionic and electronic frequencies. Annotate n^2 = epsilon_inf in the optical region. Generic material, not a specific one. -->

Representative values are in Table 25.3. Non-polar polymers (PE, PP, PTFE) combine low permittivity with very low loss and are the materials of choice for cable insulation, film capacitors and high-frequency substrates. Polar polymers (PVC, nylon, epoxy) have higher loss. Ceramics range from the low-loss single crystals and aluminas used in microwave windows and satellite filters to the very high permittivity, lossier perovskites used in capacitors.

| Material | $\varepsilon_r$ | $\tan\delta$ | Frequency | Typical use |
|---|---|---|---|---|
| PTFE | 2.1 | $2\times10^{-4}$ | 1 MHz–10 GHz | RF cables, radomes, high-frequency boards |
| Polyethylene / XLPE | 2.3 | $2$–$5\times10^{-4}$ | 50 Hz–1 MHz | Power-cable insulation |
| Polypropylene (biaxially oriented) | 2.2 | $2\times10^{-4}$ | 50 Hz–1 MHz | Film capacitors for power electronics |
| PVC (plasticized) | 4–8 | 0.05–0.1 | 1 kHz–30 MHz | Low-voltage cable sheathing |
| Epoxy (cured) | 3.5–4.5 | 0.01–0.03 | 1 MHz | Potting, cast insulators |
| FR-4 glass–epoxy laminate | 4.3–4.7 | 0.015–0.02 | 1 GHz | Printed circuit boards |
| Fused silica | 3.8 | $\approx10^{-4}$ | 1 MHz–10 GHz | Optical and microwave windows |
| Alumina (99.5 %) | 9.8 | $1$–$3\times10^{-4}$ | 1 MHz–10 GHz | Substrates, vacuum feedthroughs, spark plugs |
| Electrical porcelain | 5–7 | 0.01–0.02 | 50 Hz | Line and station insulators |
| Mica (muscovite) | 6–7 | $2\times10^{-4}$ | 1 MHz | Motor and generator insulation |
| Water (liquid, 20 °C) | 80 | 0.1 at 2.45 GHz | — | The reason moisture ruins insulation |
| BaTiO$_3$-based (X7R) | 2000–4000 | 0.01–0.025 | 1 kHz | Multilayer ceramic capacitors |

*Table 25.3 — Room-temperature permittivity and loss of common dielectrics (typical values).*

### Loss as heat: a nuisance and a tool

In cables and capacitors dielectric loss is a nuisance. It heats the insulation and, because $\varepsilon''$ usually rises with temperature, can run away into thermal breakdown (Section 25.4). In high-frequency circuits and radomes it attenuates the signal. In processing it is a tool: microwave heating of food at 2.45 GHz relies on the relaxation loss of water; radio-frequency (27.12 MHz) welding of PVC sheets for medical bags, tarpaulins and inflatable structures relies on the dipolar loss of C–Cl groups.

**Worked example — why PVC can be RF-welded and polyethylene cannot.** Apply a field of 1 kV/mm ($10^6$ V/m rms) at 27.12 MHz. For plasticized PVC take $\varepsilon''\approx0.2$; for polyethylene $\varepsilon''=2.3\times2\times10^{-4}=4.6\times10^{-4}$. The volumetric heating rate is $p=2\pi f\varepsilon_0\varepsilon''E^2$:

$$
p_{\mathrm{PVC}}=2\pi(27.12\times10^6)(8.854\times10^{-12})(0.2)(10^6)^2=3.0\times10^8\ \mathrm{W/m^3}
$$

With density 1380 kg/m³ and specific heat 1000 J/(kg K) the PVC heats at $3.0\times10^8/(1380\times1000)=220$ K/s — it reaches its welding temperature in under a second. Polyethylene, with $p=6.9\times10^5\ \mathrm{W/m^3}$, density 950 kg/m³ and specific heat 2300 J/(kg K), heats at only 0.3 K/s; it is welded by hot plates, hot gas or ultrasound instead. The property that makes polyethylene the best cable insulation is the same one that makes it impossible to RF-weld.

---

## 25.4 Dielectric breakdown and insulation

### Dielectric strength is not a single number

Every insulator fails if the field is high enough: a conducting channel forms, the material is punctured, and in solids the damage is permanent. The **dielectric strength** is the field at breakdown, but unlike permittivity it is not a material constant. It depends on thickness (thin films are stronger), electrode shape, waveform (DC, AC, impulse), duration of stress, temperature, and above all on defects. Table 25.4 shows why: thin, defect-free polymer films withstand hundreds of kilovolts per millimetre; the same polymers in thick industrial insulation are designed to work at a few kilovolts per millimetre.

| Material | Short-term dielectric strength (kV/mm) | Typical design stress (kV/mm) |
|---|---|---|
| Air (1 atm, uniform field, 1 cm gap) | 3 | — |
| SF$_6$ gas (1 atm) | 8.9 | Gas-insulated switchgear at 4–6 bar |
| Transformer mineral oil (standard test gap) | 10–15 | 2–5 (oil–paper) |
| XLPE (cable, thick) | 30–50 (AC) | 5–15 at conductor screen |
| BOPP film (capacitor, 5–10 µm) | 600–700 | 150–250 |
| Mica | 100–200 | 2–3 (in mica-tape windings) |
| Epoxy (cast) | 20–30 | 3–5 |
| Alumina (96 %) | 10–35 | 2–5 |
| Electrical porcelain | 10–20 | 1–3 |
| Thermal SiO$_2$ film (10 nm) | $\approx1000$ | 300–500 in MOS gates |

*Table 25.4 — Dielectric strength and practical working stress of insulating materials (typical; strength depends on thickness, waveform and test method).*

### Mechanisms of breakdown

- **Intrinsic (electronic) breakdown.** In a perfect insulator a few free electrons gain energy from the field faster than they can lose it to phonons, ionize atoms, and multiply in an avalanche. This sets an upper limit of order $10^2$–$10^3$ kV/mm, approached only in thin, clean films.
- **Thermal breakdown.** Dielectric loss and leakage current heat the insulation; both increase with temperature; if heat cannot escape fast enough, temperature and current run away together. It dominates in thick insulation, at high frequency and at high ambient temperature.
- **Electromechanical breakdown.** The electrostatic pressure of the electrodes, $\tfrac12\varepsilon_0\varepsilon_rE^2$, compresses a soft insulator; as it thins, the field rises. Relevant to soft polymers near or above $T_g$, and exploited in dielectric-elastomer actuators (Chapter 29).
- **Discharge and erosion (long-term) breakdown.** Gas-filled voids, delaminations and surface films see a field enhanced by the permittivity mismatch and break down first. These **partial discharges** do not bridge the electrodes immediately, but each one erodes the cavity wall with ions, ultraviolet light, ozone and heat. Over months they grow branching channels called **electrical trees** that eventually cross the insulation — the failure of the opening example. In polymers exposed to water and AC fields, slower **water trees** grow from defects and contaminants and later initiate electrical trees.
- **Surface tracking and flashover.** On outdoor insulators, contamination plus moisture forms a conductive surface film; leakage current dries bands of it; arcs across the dry bands carbonize organic surfaces into conductive tracks. Porcelain and glass resist tracking because they cannot carbonize; silicone rubber resists it because its surface is hydrophobic and recovers hydrophobicity by migrating low-molar-mass chains to the surface.

The statistics of breakdown are weakest-link statistics, the same as brittle fracture (Chapter 14): the breakdown field of a large area or a long cable is lower than that of a small test sample, and is described by Weibull distributions. The design response is to remove the largest defect: super-clean compounds, triple extrusion of the screens with the insulation so no interface voids form, and smooth field grading at joints.

**Worked example — field and loss in an HV cable.** A 132 kV cable has a conductor of radius $a=15.5$ mm and 18 mm of XLPE ($\varepsilon_r=2.3$, $\tan\delta=3\times10^{-4}$), so the outer radius is $b=33.5$ mm. The phase-to-earth voltage is $U_0=132/\sqrt3=76.2$ kV. The coaxial field is $E(r)=U_0/[r\ln(b/a)]$, highest at the conductor screen:

$$
E_{\max}=\frac{76.2\times10^3}{(0.0155)\ln(33.5/15.5)}=6.4\ \mathrm{kV/mm},\qquad E_{\min}=\frac{76.2\times10^3}{(0.0335)\ln(33.5/15.5)}=3.0\ \mathrm{kV/mm}
$$

The maximum working stress is about a fifth of the short-term strength of thick XLPE, a margin set by long-term ageing and the size effect, not by short-term tests. The capacitance per metre is $C=2\pi\varepsilon_0\varepsilon_r/\ln(b/a)=166$ pF/m, and the dielectric loss per metre is

$$
P=\omega CU_0^2\tan\delta=2\pi(50)(166\times10^{-12})(76.2\times10^3)^2(3\times10^{-4})=0.091\ \mathrm{W/m}
$$

or 91 W per kilometre, small beside the conductor's resistive loss. But the loss scales with $U_0^2$ and with $\varepsilon'\tan\delta$: at 400 kV (a factor 9.2 in $U_0^2$) with the older oil-impregnated paper ($\varepsilon_r\approx3.5$, $\tan\delta\approx2.5\times10^{-3}$), dielectric loss becomes a significant part of the cable's thermal budget. This is one reason XLPE displaced paper at extra-high voltage.

### Insulation systems and ageing

Real insulation is a system of several materials: in a motor winding, enamel on the wire, mica tape, glass-fibre backing and impregnating resin; in a transformer, oil, cellulose paper and pressboard; in a power-module package, silicone gel over a ceramic substrate. Insulation is classified by its continuous temperature rating (IEC thermal classes 105 (A), 130 (B), 155 (F), 180 (H) and above, in °C), and its life follows thermal-ageing kinetics. A common rule is that every 8–10 K above the rated temperature halves the life — the Arrhenius law of Chapter 8 with an activation energy of about 1 eV. Moisture is the other enemy: water raises permittivity and loss, lowers resistivity, and in cellulose catalyses depolymerization. Fast-switching SiC inverters in 800 V vehicle drives (Chapter 26) add a new stress: steep voltage pulses trigger partial discharge in winding enamels that were adequate at 400 V.

> **Status of the principle: Thermal life halving every 8–10 K**
> *Empirical.* It is an Arrhenius rule fitted to accelerated ageing of organic insulation over a limited temperature range; extrapolation far outside the tested range or across a change in degradation mechanism is unreliable.

---

## 25.5 Ferroelectric, piezoelectric and pyroelectric materials

### Symmetry decides which effects are possible

A crystal can couple electrical polarization to stress or temperature only if its symmetry allows it (Neumann's principle, Chapter 3). Of the 32 crystallographic point groups, 11 have a centre of symmetry and show no such coupling. Of the 21 non-centrosymmetric classes, 20 are **piezoelectric**: stress produces polarization, and a field produces strain. Ten of those are **polar** — they have a unique axis along which a spontaneous polarization $P_s$ exists — and are **pyroelectric**: a temperature change alters $P_s$ and releases charge. A subset of the polar materials are **ferroelectric**: their spontaneous polarization can be reversed by an applied field. Every ferroelectric is therefore pyroelectric and piezoelectric, but quartz is piezoelectric without being pyroelectric, and wurtzite AlN and ZnO are pyroelectric without being switchable.

| Class | Condition | Examples |
|---|---|---|
| Dielectric (all) | Any | All insulators |
| Piezoelectric | Non-centrosymmetric (20 classes) | Quartz, AlN, ZnO, GaN, bone collagen |
| Pyroelectric | Polar (10 classes) | AlN, ZnO, LiTaO$_3$, tourmaline |
| Ferroelectric | Polar and switchable | BaTiO$_3$, PZT, LiNbO$_3$, PVDF |

*Table 25.5 — The symmetry hierarchy of functional dielectrics.*

A polycrystalline ceramic of randomly oriented grains is macroscopically centrosymmetric even when each grain is polar, so it shows no net piezoelectricity. Only ferroelectrics can be made piezoelectric as ceramics, because their domains can be aligned by **poling**: a strong DC field (2–4 kV/mm) applied above room temperature switches domains toward the field direction. This is why almost all engineering piezoelectric ceramics are ferroelectric, and why they lose their activity if heated near the Curie temperature.

### Ferroelectricity in perovskites

Barium titanate is the archetype. Above its **Curie temperature** $T_C\approx120$–130 °C it is cubic perovskite, with Ti$^{4+}$ at the centre of an oxygen octahedron. On cooling, the Ti ion shifts off-centre along a cube edge, the cell stretches to tetragonal ($c/a\approx1.01$), and a spontaneous polarization of about 0.26 C/m² appears. Further transitions to orthorhombic (about 5 °C) and rhombohedral (about −90 °C) symmetries follow. Above $T_C$ the permittivity follows the **Curie–Weiss law**,

$$
\varepsilon_r\approx\frac{C}{T-T_0}
$$

with $C\approx1.7\times10^5$ K for BaTiO$_3$ — the divergence predicted by the failure of the Clausius–Mossotti denominator. Near $T_C$ the permittivity reaches 10 000 or more, which is exploited (after chemical flattening with dopants) in multilayer ceramic capacitors: more than a trillion are made every year, each a sintered stack of hundreds of BaTiO$_3$ layers a few micrometres thick with nickel electrodes.

The polarization below $T_C$ is organized into **domains**, separated by 180° and 90° walls, which form to reduce depolarizing fields and elastic strain energy. Switching under a field traces a **hysteresis loop** (P–E loop) characterized by the remanent polarization $P_r$ and the coercive field $E_c$ (Figure 25.4) — a direct analogue of the magnetic hysteresis of Chapter 27. Ferroelectric memories store a bit in the sign of $P_r$, now in thin films of silicon-compatible doped HfO$_2$.

### Lead zirconate titanate and the morphotropic phase boundary

The workhorse piezoelectric is lead zirconate titanate, PbZr$_{1-x}$Ti$_x$O$_3$ (PZT). Its phase diagram has a nearly vertical **morphotropic phase boundary** (MPB) near $x\approx0.48$ between rhombohedral (Zr-rich) and tetragonal (Ti-rich) ferroelectric phases. At the boundary the two phases are nearly degenerate, the polarization can rotate easily between their directions, poling is most complete, and the piezoelectric and dielectric coefficients peak. The Curie temperature at the MPB is about 390 °C, far above that of BaTiO$_3$, so PZT holds its poling in service. Commercial compositions are tuned by dopants: donor-doped "soft" PZT (PZT-5A, -5H) has large coefficients but higher loss, for sensors and actuators; acceptor-doped "hard" PZT (PZT-4, -8) has lower loss and is used in high-power ultrasonic transducers and sonar.

<!-- FIGURE 25.4 | figures/ch25/fig-25-4-pzt-mpb-and-loop.png | plot | PZT: the morphotropic phase boundary where piezoelectric response peaks, and the ferroelectric hysteresis loop of a poled ceramic. | Content: left panel: phase diagram of PbZrO3–PbTiO3, x-axis mol% PbTiO3 0 to 100, y-axis temperature 0 to 500 C; cubic paraelectric above a Curie line rising from about 230 C (PbZrO3) to 490 C (PbTiO3); rhombohedral FE(R) on Zr-rich side, tetragonal FE(T) on Ti-rich side, near-vertical MPB at about 48 mol% PbTiO3; antiferroelectric region near 0–5 %. Overlay on secondary y-axis: d33 (pC/N) vs composition peaking at about 400 at the MPB, falling to about 100 at 30 and 70 %. Right panel: P–E loop, E from -4 to +4 kV/mm, P from -0.4 to +0.4 C/m2, Pr about 0.3 C/m2, Ec about 1 kV/mm, labels Ps, Pr, Ec. -->

### Piezoelectric coefficients and applications

The direct and converse effects are described by tensor coefficients (Chapter 4). In engineering notation,

$$
D_i=d_{ij}\sigma_j+\varepsilon_{ik}^{\sigma}E_k,\qquad S_j=s_{jk}^{E}\sigma_k+d_{ij}E_i
$$

where $d_{ij}$ (pC/N, or equivalently pm/V) gives both the charge per unit force and the strain per unit field. For poled ceramics, axis 3 is the poling direction; $d_{33}$ describes response along it and $d_{31}$ transverse to it. The **electromechanical coupling factor** $k$ ($k^2$ = fraction of input energy converted to the other form) measures efficiency for transducers.

| Material | $d_{33}$ (pC/N) | $k_{33}$ | $T_C$ (°C) | Uses |
|---|---|---|---|---|
| Quartz (single crystal, $d_{11}$) | 2.3 | 0.1 | 573 (α–β) | Oscillators, force sensors |
| AlN (thin film) | 5–6 | 0.3 | none (no switching) | RF filters in phones, MEMS |
| ZnO | 12 | 0.4 | none | Thin-film transducers, sensors |
| PVDF (poled film) | −20 to −33 | 0.2 | ≈170 (melts first) | Hydrophones, flexible sensors |
| BaTiO$_3$ ceramic | 190 | 0.5 | 120–130 | Early transducers, capacitors |
| PZT-4 (hard) | 290 | 0.70 | 330 | Sonar, ultrasonic cleaners, welders |
| PZT-5H (soft) | 590 | 0.75 | 190–200 | Actuators, medical ultrasound, sensors |
| KNN-based (lead-free) | 200–400 | 0.5–0.6 | 200–400 | Replacement for PZT under RoHS pressure |
| PMN–PT (single crystal) | 1500–2500 | 0.9 | 130–170 | High-end medical imaging probes |

*Table 25.6 — Piezoelectric properties at room temperature (typical values).*

The applications span every field. In mechanical and automotive engineering: piezoelectric stack actuators open diesel injectors in about 0.1 ms; accelerometers monitor engines and machinery. In civil and aerospace engineering: bonded piezo wafers send and receive guided ultrasonic waves for structural health monitoring of bridges and composite wings, and ultrasonic testing of welds uses PZT probes. In biomedical engineering: imaging probes contain arrays of hundreds of PZT or PMN–PT elements. In electronics: quartz and AlN resonators time and filter almost every radio signal. The search for lead-free replacements (KNN, BNT–BT, BCZT) is driven by the toxicity of lead (Chapter 49).

**Worked example — a fuel-injector actuator.** A diesel injector needle must lift about 40 µm. A PZT stack of 160 layers, each 80 µm thick, is driven at 160 V. Each layer sees a field $E=160/(80\times10^{-6})=2.0$ kV/mm, below the depolarizing limit of soft PZT for unipolar drive. With an effective large-signal $d_{33}=600$ pm/V, each layer extends $d_{33}V=600\times10^{-12}\times160=9.6\times10^{-2}$ µm, and the stack of 160 layers gives

$$
\Delta L=n\,d_{33}V=160\times(600\times10^{-12})(160)=15.4\ \mu\mathrm m
$$

from a total active length of 12.8 mm — a strain of 0.12 %. Since 15 µm is less than the required lift, injectors use a hydraulic or lever amplifier, trading force for stroke; the stack's attraction is its speed and its force (kilonewtons), not its displacement. The multilayer design is the key materials-processing idea: tape-casting thin PZT layers with interleaved electrodes and co-firing them lets a modest voltage produce a high field.

### Pyroelectric materials

In a polar material a temperature change $\Delta T$ alters the spontaneous polarization by $\Delta P=p\,\Delta T$, where $p$ is the **pyroelectric coefficient** (C/(m² K)). On an electroded element of area $A$ this releases a charge $Q=pA\Delta T$. Lithium tantalate ($p\approx2\times10^{-4}$ C/(m² K), $T_C\approx600$ °C), PZT ($\approx3\times10^{-4}$), triglycine sulfate (high $p$ but a low Curie point) and PVDF ($\approx3\times10^{-5}$) are used in passive infrared motion sensors, flame detectors, gas analysers and uncooled thermal-imaging arrays. A 1 mm² LiTaO$_3$-class element with $p=3\times10^{-4}$ C/(m² K) warmed by 1 mK releases only 0.3 pC, so detectors are made thin (low heat capacity), thermally isolated and read by high-impedance amplifiers; the useful figure of merit is $p/(c_v\varepsilon_r)$, which favours materials with high pyroelectric coefficient but modest permittivity.

---

## 25.6 Superconductivity

### Zero resistance and the Meissner effect

Below a **critical temperature** $T_c$, many metals, alloys and oxides lose all DC resistance. Currents set up in superconducting rings have persisted for years without measurable decay, which puts the resistivity below $10^{-25}\ \Omega\,\mathrm m$, at least seventeen orders of magnitude below copper. Zero resistance alone, however, would describe a "perfect conductor". The defining property is the **Meissner effect**: a superconductor cooled in a magnetic field expels it, the field decaying inside within the **London penetration depth** $\lambda_L$ (typically 40–200 nm). Superconductivity is therefore a thermodynamic phase with its own free energy, not merely a limit of high conductivity.

The microscopic picture (BCS theory, belonging to Engineering Physics) is that electrons near the Fermi surface form bound **Cooper pairs** through an attraction mediated by lattice vibrations, condensing into a single coherent quantum state separated from excited states by an energy gap of order $3.5k_BT_c$. Two lengths characterize it: $\lambda_L$, over which fields are screened, and the **coherence length** $\xi$, over which the pair density can vary. This explains why Cu, Ag and Au do not superconduct: the weak electron–phonon coupling that makes their resistivity low also prevents pairing.

> **Status of the principle: Meissner effect and BCS pairing**
> *Fundamental* for the Meissner effect, which follows from the thermodynamics of a phase with zero magnetic induction inside. BCS theory is fundamental for conventional (phonon-mediated) superconductors; the pairing mechanism of the cuprates and iron pnictides is still unresolved.

### Critical parameters and Type I versus Type II

Superconductivity is destroyed by too high a temperature, field or current density. The three critical parameters $T_c$, $B_c$ and $J_c$ define a critical surface; a magnet must operate inside it with margin. The field dependence is approximately parabolic, $B_c(T)\approx B_c(0)[1-(T/T_c)^2]$.

How the field is excluded divides superconductors into two types, decided by the **Ginzburg–Landau parameter** $\kappa=\lambda/\xi$:

- **Type I** ($\kappa<1/\sqrt2$): mostly pure elements (Pb, Sn, Al, Hg). The surface energy between normal and superconducting regions is positive, so field is excluded completely up to a single, low critical field ($B_c=0.080$ T for Pb, 0.03 T for Sn, 0.01 T for Al), then the material goes normal. Useless for magnets.
- **Type II** ($\kappa>1/\sqrt2$): alloys, compounds and oxides with short mean free paths and short coherence lengths. Above a lower critical field $B_{c1}$ (typically tens of millitesla) it becomes energetically favourable for the field to enter as quantized **flux vortices**, each carrying one flux quantum $\Phi_0=h/2e=2.07\times10^{-15}$ Wb in a normal core of radius about $\xi$. The material stays superconducting in this **mixed state** up to an upper critical field

$$
B_{c2}=\frac{\Phi_0}{2\pi\xi^2}
$$

which can exceed 100 T (Figure 25.5). Alloying shortens the electron mean free path and hence $\xi$, so impure, disordered materials have higher $B_{c2}$ — the reverse of what a conductor designer wants in Section 25.1, and a good example of the same microstructural variable serving opposite goals.

<!-- FIGURE 25.5 | figures/ch25/fig-25-5-type-i-ii-magnetization.png | plot | Type I and Type II superconductors respond to an applied field differently: complete exclusion up to Bc, versus partial flux entry between Bc1 and Bc2. | Content: two panels, x-axis applied field B (arbitrary units), y-axis -mu0 M. Left (Type I): straight line rising with slope 1 to Bc, then vertical drop to zero; inset of field lines bending around a sphere. Right (Type II): linear rise to Bc1 (small), then gradual decline to zero at Bc2 (about 20 times Bc1); dashed Type I curve with the same thermodynamic Bc for comparison. Inset: hexagonal vortex lattice viewed along the field, cores of radius xi, field decaying over lambda. Label Meissner state, mixed state, normal state. -->

### Flux pinning: why microstructure sets $J_c$

A current flowing through the mixed state exerts a Lorentz force $\mathbf J\times\mathbf B$ on the vortices. If they move, they dissipate energy and the superconductor shows resistance. Useful current therefore requires **flux pinning**: microstructural defects that pin the normal vortex cores, since a vortex core sitting on a non-superconducting defect saves condensation energy. The best pins are of size comparable to $\xi$ (a few nanometres) and spaced like the vortex lattice. The critical current density is therefore not an intrinsic property at all; it is engineered by processing:

- In **Nb–Ti**, cold drawing followed by precipitation heat treatments produces nanometre-thick ribbons of $\alpha$-Ti at the grain boundaries, which pin flux; $J_c$ reaches about 3000 A/mm² at 5 T and 4.2 K.
- In **Nb$_3$Sn**, the grain boundaries of the A15 compound are the pins, so the reaction heat treatment is designed to give fine grains (100–200 nm).
- In **REBCO** coated conductors, nanorods of BaZrO$_3$ or BaHfO$_3$ self-assemble in the film during deposition and act as columnar pins.

This is the materials-science core of applied superconductivity: the same Hall–Petch-like logic of Chapter 13, with flux vortices playing the role of dislocations and precipitates and boundaries obstructing them.

### The practical superconductors

| Material | Structure | $T_c$ (K) | $B_{c2}$ (T) at 4.2 K | Form and main uses |
|---|---|---|---|---|
| Nb | BCC element | 9.2 | 0.4 | Superconducting RF accelerator cavities, Josephson junctions |
| Nb–47Ti | BCC alloy | 9.5 | 10.5–11 | Wire; MRI, NMR, LHC dipoles; >90 % of the market |
| Nb$_3$Sn | A15 compound | 18 | 25–27 | Brittle wire reacted after winding; NMR, ITER, HL-LHC |
| MgB$_2$ | Hexagonal | 39 | 15–20 (at 0 K) | Wire; cryogen-free MRI, power cables at 20 K |
| YBa$_2$Cu$_3$O$_{7-\delta}$ (REBCO) | Layered perovskite cuprate | 92 | > 100 | Coated tape; fusion magnets, high-field inserts, fault-current limiters |
| Bi$_2$Sr$_2$CaCu$_2$O$_8$ (Bi-2212) | Layered cuprate | 85 | > 100 | Round wire; high-field inserts |
| (Bi,Pb)$_2$Sr$_2$Ca$_2$Cu$_3$O$_{10}$ (Bi-2223) | Layered cuprate | 110 | > 100 | Silver-sheathed tape; current leads, cables |
| Iron pnictides (e.g. Ba-122) | Layered | up to 55 | > 50 | Developmental wires |

*Table 25.7 — The principal practical superconductors (typical values).*

<!-- FIGURE 25.6 | figures/ch25/fig-25-6-superconductor-bc2-vs-t.png | plot | Upper critical field against temperature for the practical superconductors, with the operating windows of liquid helium, cryocoolers and liquid nitrogen. | Content: x-axis temperature 0 to 100 K; y-axis upper critical field (or irreversibility field for cuprates) 0 to 50 T, curves clipped at 50 with arrows for higher values. Curves (approx. Bc2(0)[1-(T/Tc)^2]): Nb-Ti (14.5 T, Tc 9.5 K, about 11.7 T at 4.2 K); Nb3Sn (30 T, Tc 18 K); MgB2 (wire, about 15 T at 0 K, Tc 39 K); REBCO (H parallel c, irreversibility line, well above 50 T below 30 K, reaching 0 at 92 K); Bi-2223 irreversibility line (much lower than REBCO at 77 K, about 0.2 T). Vertical bands at 1.9 K (superfluid He), 4.2 K (liquid He), 10-20 K (cryocooler), 77 K (liquid N2). Mark LHC operating point (8.3 T, 1.9 K) and MRI (3 T, 4.2 K). -->

The family divides naturally (Figure 25.6). **Low-temperature superconductors** (Nb–Ti, Nb$_3$Sn) are cooled with liquid helium at 4.2 K or superfluid helium at 1.9 K. Nb–Ti is ductile, so it can be co-drawn with copper into fine multifilamentary wire, wound and used directly; it dominates because it is easy to make, not because it is the best superconductor. Nb$_3$Sn has double the $T_c$ and $B_{c2}$ but is a brittle intermetallic: wire is drawn from ductile precursors (Nb filaments in Cu–Sn bronze or with internal tin sources), wound into a coil, and only then reacted at 650–700 °C for days to form the compound, after which the coil cannot be bent. **High-temperature superconductors**, the cuprates, are layered oxides in which the superconductivity lives in CuO$_2$ planes. They are strongly anisotropic, their grain boundaries block current unless the grains are aligned within a few degrees, and their coherence lengths are only 1–2 nm. REBCO conductor is therefore made as a thin-film "coated conductor": a 1–2 µm epitaxial film deposited on a biaxially textured buffer stack on a Hastelloy tape, a triumph of thin-film processing (Chapter 41). MgB$_2$, discovered in 2001, sits between: cheap elements, 39 K, operable with cryocoolers at 10–20 K.

A practical conductor is always a composite. Superconducting filaments are embedded in a copper or aluminium **stabilizer** of high RRR, which carries the current if a region goes normal and conducts heat away to prevent a local hot spot from spreading — a **quench**. Filaments are made fine (a few to tens of micrometres) and twisted to limit magnetization and AC losses. In a magnet, where the stored energy density at 3 T is $B^2/2\mu_0=3.6\ \mathrm{MJ/m^3}$, quench protection is a central design problem.

**Worked example — the winding of an MRI magnet.** A whole-body MRI solenoid produces 3 T in its bore. For a long solenoid, $B=\mu_0NI/L$, so the required ampere-turns per metre of length are

$$
\frac{NI}{L}=\frac{B}{\mu_0}=\frac{3}{4\pi\times10^{-7}}=2.39\times10^6\ \mathrm{A/m}
$$

Take Nb–Ti with $J_c=3000$ A/mm² at the peak field in the winding and 4.2 K, in a wire with copper-to-superconductor ratio 1.5, so the engineering current density over the wire is $3000/2.5=1200$ A/mm². With insulation and packing reducing that to 80 %, the winding current density is $960$ A/mm² $=9.6\times10^8$ A/m². The radial build of winding needed is then

$$
\frac{2.39\times10^6\ \mathrm{A/m}}{9.6\times10^8\ \mathrm{A/m^2}}=2.5\ \mathrm{mm}
$$

at the critical current, or about 3.6 mm if the magnet is run at 70 % of critical current to leave a temperature and field margin. A copper solenoid at a typical 5 A/mm² would need a winding about half a metre thick and dissipate megawatts. Real magnets need more conductor (end corrections, shielding coils), but the comparison shows why superconductivity enables MRI, NMR, accelerators (the LHC's 1232 Nb–Ti dipoles run at 8.3 T and 1.9 K) and fusion magnets (REBCO coils have reached 20 T near 20 K).

Beyond magnets, superconductors are used in power cables and fault-current limiters (cuprates cooled by cheap liquid nitrogen at 77 K), in high-Q niobium RF cavities for accelerators, in SQUID magnetometers sensitive to femtotesla fields, and in the Josephson-junction circuits of superconducting quantum computers. Hydrides such as H$_3$S superconduct above 200 K, but only above 100 GPa; room-temperature superconductivity at ambient pressure remains unachieved.

> **Boundary.** BCS theory, Ginzburg–Landau theory and the quantum mechanics of the Josephson effect belong to the Engineering Physics book; conductor design, AC losses and quench protection are developed in depth in the *Materials Core (EEE)* book, Chapter 17.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| What makes some solids metals and others semiconductors or insulators? How are carrier density and mobility set in semiconductors? | Chapter 26 |
| How does the magnetic analogue of ferroelectric domains and hysteresis work, and what limits core losses? | Chapter 27 |
| How does the electronic polarization of Section 25.3 produce refractive index, dispersion and electro-optic effects? | Chapter 28 |
| How are piezoelectric and electrostrictive materials used in actuators, and how do dielectric elastomers work? | Chapter 29 |
| How do size effects change conduction in nanowires and graphene? | Chapter 30 |
| How are solid electrolytes used in fuel cells, electrolysers and solid-state batteries? | Chapter 32 |
| How do superconductors and insulators behave under irradiation and cryogenic conditions? | Chapter 33 |
| How do electromigration, contact corrosion and insulation ageing appear in failure analysis? | Chapters 35 and 36 |
| How are thin conductors, dielectrics and superconducting coated conductors deposited? | Chapter 41 |
| How are resistivity, permittivity and ionic conductivity measured (four-point probe, impedance spectroscopy)? | Chapter 42 |
| How are conductor and insulator choices made systematically with indices and cost? | Chapter 48 |

**Next:** Chapter 26 turns to the materials whose carrier density is not fixed but designed — semiconductors — and asks how band gaps, doping, mobility and interfaces make them the engine of electronics, photovoltaics and power conversion.
