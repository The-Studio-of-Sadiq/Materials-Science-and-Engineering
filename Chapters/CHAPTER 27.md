# Chapter 27 — Magnetic Materials

*Part VI · Physical and Functional Properties*

A utility replaces a 40-year-old distribution transformer that has run at a few per cent of rated load for most of its life, and measures the old core: it has been dissipating about a kilowatt continuously, day and night, whether or not anyone was drawing power. Its replacement has a core of amorphous iron-based ribbon 25 µm thick, and dissipates about a third as much. Over a thirty-year life the saving pays for the transformer. A few kilometres away, a wind turbine's direct-drive generator holds half a tonne of neodymium–iron–boron magnets per megawatt, and its designers worry less about efficiency than about supply: most of the world's rare-earth separation happens in one country, and the dysprosium that keeps the magnets from demagnetizing when hot is scarcer still. In the hospital down the road, an MRI scanner relies on a superconducting magnet (Chapter 25), titanium implants that are only weakly paramagnetic, and gradient coils whose eddy currents must be kept out of nearby metal. Magnetic materials are everywhere in energy, transport and medicine, and nearly every one of their engineering properties is set by microstructure.

This chapter explains where magnetism in solids comes from, why a few materials are strongly magnetic, how domains and their walls make a material soft or hard, and how processing produces the electrical steels, ferrites, amorphous and nanocrystalline alloys and rare-earth magnets that engineers use. It ends with magnetostriction, magnetocalorics and spintronics. The *Materials Core (EEE)* book, Chapters 15–16, treats magnetic behaviour and core design in more depth.

> **Why are iron, cobalt and nickel strongly magnetic at room temperature when most elements are not?**
> **Why does a transformer core, made of the softest magnetic material known, still waste energy every cycle?**
> **What makes NdFeB a hundred times harder to demagnetize than transformer steel, although both are mostly iron?**
> **Why do electrical steels contain 3 % silicon, and why are amorphous ribbons only 25 µm thick?**

| Concept | Engineering destination |
|---|---|
| Atomic moments; dia-, para-, ferro-, ferri- and antiferromagnetism | MRI compatibility of implants and tools; magnetic separation; non-magnetic stainless steels |
| Exchange, saturation magnetization, Curie temperature | Maximum flux density of cores; temperature limits of magnets and sensors |
| Anisotropy, domains, walls, hysteresis | Why a material is soft or hard; designing microstructure for coercivity |
| Soft magnets | Transformers, motors, generators, inductors, magnetic shielding |
| Hard magnets and energy product | Electric-vehicle motors, wind generators, actuators, loudspeakers, sensors |
| Magnetic losses | Efficiency of transformers, motors and power-electronic inductors |
| Magnetostriction, magnetocalorics, spintronics | Sonar and actuators, transformer noise, magnetic refrigeration, hard-disk heads, MRAM |

**Roadmap.** Moments and classes of magnetism (27.1) → exchange, ferro- and ferrimagnetism, Curie temperature (27.2) → domains, walls and hysteresis (27.3) → soft magnets (27.4) → hard magnets (27.5) → magnetic losses (27.6) → magnetostrictive, magnetocaloric and spintronic materials (27.7).

---

## 27.1 Magnetic moments and classes of magnetism

### Fields and magnetization

A magnetic material responds to an applied field $\mathbf H$ (A/m) by developing a **magnetization** $\mathbf M$ (A/m), the magnetic moment per unit volume. The flux density is

$$
\mathbf B=\mu_0(\mathbf H+\mathbf M)
$$

with $\mu_0=4\pi\times10^{-7}$ H/m. For linear materials $\mathbf M=\chi\mathbf H$, where $\chi$ is the (dimensionless, SI volume) **susceptibility**, and $\mathbf B=\mu_0\mu_r\mathbf H$ with relative permeability $\mu_r=1+\chi$. For ferromagnets neither $\chi$ nor $\mu_r$ is a constant: $\mathbf M$ depends on history, and the full hysteresis loop of Section 27.3 is needed. The engineering quantities are the **saturation magnetization** $M_s$ (often quoted as the saturation polarization $J_s=\mu_0M_s$, in tesla), the **remanence** $B_r$, the **coercivity** $H_c$ and the permeability.

### Where atomic moments come from

Magnetic moments in solids come from electrons: their orbital motion and their spin, each of order one **Bohr magneton**, $\mu_B=9.27\times10^{-24}$ A m². In filled shells the moments cancel. Only atoms with partly filled shells carry a net moment, and in solids only two groups keep it:

- **3d transition metals** (Cr, Mn, Fe, Co, Ni and their ions). The 3d electrons are on the outside of the atom, so the crystal field of the neighbours **quenches** their orbital moment; the moment is mostly spin, and in metals the 3d electrons are partly itinerant, giving non-integer moments (2.22 $\mu_B$ per Fe atom, 1.72 for Co, 0.61 for Ni).
- **4f rare earths** (Nd, Sm, Gd, Tb, Dy...). The 4f shell is buried inside the 5s and 5p shells, so the orbital moment survives, giving large moments and, through the coupling of a non-spherical 4f charge cloud to the crystal field, very large **magnetocrystalline anisotropy** — the key to permanent magnets (Section 27.5).

The rules that decide each ion's moment (Hund's rules) and the quantum mechanics behind them belong to the Engineering Physics book; the materials consequence is that strong magnetism is confined to compounds and alloys of a dozen elements.

### The classes of magnetism

| Class | Origin | Typical $\chi$ (SI) | Temperature dependence | Examples |
|---|---|---|---|---|
| Diamagnetic | Induced orbital currents oppose the field | $-10^{-6}$ to $-10^{-4}$ | None | Cu ($-9.6\times10^{-6}$), water ($-9\times10^{-6}$), Bi ($-1.7\times10^{-4}$), pyrolytic graphite |
| Paramagnetic | Uncoupled moments partly aligned by the field | $10^{-6}$ to $10^{-3}$ | Curie law $\chi=C/T$ (local moments) or nearly constant (Pauli, metals) | Al ($2.2\times10^{-5}$), Ti ($1.8\times10^{-4}$), Pt, O$_2$, austenitic stainless ($\approx3\times10^{-3}$) |
| Ferromagnetic | Exchange aligns all moments parallel | Up to $10^5$ and history-dependent | Ordered below $T_C$ | Fe, Co, Ni, Gd (below 20 °C), many alloys |
| Antiferromagnetic | Exchange aligns neighbours antiparallel; net zero | $10^{-5}$–$10^{-3}$ | Ordered below Néel temperature $T_N$ | MnO, NiO, Cr, FeMn, IrMn |
| Ferrimagnetic | Antiparallel sublattices of unequal moment | Up to $10^4$ | Ordered below $T_C$ | Magnetite, spinel and hexagonal ferrites, garnets (YIG) |

*Table 27.1 — Classes of magnetism (room-temperature values; typical).*

**Diamagnetism** is present in all materials and is weak. Its extreme is the superconductor, a perfect diamagnet with $\chi=-1$ (Chapter 25). **Paramagnetism** in insulators with local moments follows the **Curie law** $\chi=C/T$, because thermal agitation competes with field alignment; in metals the conduction electrons give a small, nearly temperature-independent Pauli paramagnetism.

> **Status of the principle: Curie law $\chi=C/T$**
> *Derived.* It follows from Boltzmann statistics of non-interacting moments in the weak-field limit ($\mu B\ll k_BT$). It fails at low temperature or high field, where the magnetization saturates, and in materials whose moments interact (Section 27.2).

The weak classes matter in engineering more often than their small susceptibilities suggest. Magnetic resonance imaging produces image distortion wherever susceptibility changes abruptly, so implants are made of titanium alloys, CoCr or polymers rather than ferromagnetic steels (Chapter 31). Austenitic stainless steels are paramagnetic and are specified for non-magnetic components, but cold work can transform part of the austenite to ferromagnetic martensite (Chapter 15) — a classic source of unexpected magnetic signatures in minesweeper hulls, MRI rooms and particle-detector supports. Eddy-current separators in recycling plants (Chapter 49) and magnetic separators in mineral processing exploit the differences between classes.

---

## 27.2 Exchange, ferro- and ferrimagnetism, Curie temperature

### Exchange: the origin of spontaneous order

The magnetic dipole interaction between neighbouring atomic moments is far too weak (about 0.1 meV, equivalent to 1 K) to explain why iron stays magnetic up to 770 °C. The real coupling is **exchange**, a quantum-mechanical consequence of the Pauli principle and the Coulomb repulsion between electrons: depending on the overlap of neighbouring orbitals, parallel or antiparallel spins have lower electrostatic energy. Its strength, of order 10–100 meV, is what sets the ordering temperatures. Whether the exchange favours parallel (ferromagnetic) or antiparallel (antiferromagnetic) alignment depends on the interatomic distance relative to the size of the 3d shell — the empirical Bethe–Slater picture explains why Fe, Co and Ni are ferromagnetic while Mn and Cr are not, and why Heusler alloys such as Cu$_2$MnAl, with Mn atoms held farther apart, are ferromagnetic although none of their elements is.

> **Status of the principle: Exchange interaction**
> *Fundamental.* It follows from the antisymmetry of the electron wavefunction combined with Coulomb repulsion. Its magnitude in a specific material must be calculated (Chapter 45) or measured; simple rules such as the Bethe–Slater curve are only qualitative.

### Ferromagnetism and the Curie temperature

In a ferromagnet, exchange aligns all moments within a region, producing a **spontaneous magnetization** even without a field. Thermal agitation disorders them, and the magnetization falls with temperature, slowly at first and then steeply, vanishing at the **Curie temperature** $T_C$ (Figure 27.1). Above $T_C$ the material is paramagnetic with the **Curie–Weiss law**

$$
\chi=\frac{C}{T-\theta}
$$

where $\theta\approx T_C$. The mean-field (Weiss) model treats exchange as an internal "molecular field" proportional to the magnetization; it reproduces the shape of $M_s(T)$ and links $T_C$ to the exchange strength, though it overestimates $T_C$ and gets the behaviour near $T_C$ quantitatively wrong.

> **Status of the principle: Mean-field (Weiss) theory and Curie–Weiss law**
> *Approximate.* It replaces fluctuating neighbour interactions by their average. It describes $M_s(T)$ well below about $0.8T_C$ and $\chi(T)$ well above $T_C$, but fails in the critical region near $T_C$, where fluctuations dominate.

<!-- FIGURE 27.1 | figures/ch27/fig-27-1-ms-vs-temperature.png | plot | Saturation magnetization falls with temperature and vanishes at the Curie point; the reduced curves of different ferromagnets nearly coincide. | Content: left panel: x-axis temperature 0 to 1200 C; y-axis mu0 Ms in tesla, 0 to 2.3. Curves: Fe (2.15 T at 20 C, Tc 770 C), Co (1.76 T at 20 C, Tc 1115 C), Ni (0.61 T, Tc 354 C), Fe3O4 (0.60 T, Tc 585 C), Nd2Fe14B (1.61 T, Tc 312 C), MnZn ferrite (0.5 T, Tc about 220 C). Right panel: reduced Ms(T)/Ms(0) against T/Tc, 0 to 1.1, data points for Fe, Ni, Co near a single mean-field curve (Brillouin J = 1/2), plus 1/chi above Tc as a straight Curie–Weiss line. -->

The saturation magnetization follows directly from the moment per atom and the atomic density, so it is a property of composition and crystal structure, not microstructure.

**Worked example — the saturation magnetization of iron.** BCC iron has $a=0.2866$ nm and two atoms per cell, so the atomic density is $N=2/a^3=8.49\times10^{28}\ \mathrm{m^{-3}}$. With 2.22 $\mu_B$ per atom,

$$
M_s=N\,(2.22\mu_B)=(8.49\times10^{28})(2.22)(9.274\times10^{-24})=1.75\times10^6\ \mathrm{A/m}
$$

and $\mu_0M_s=2.20$ T. The measured room-temperature value is 1.71 MA/m (2.15 T), slightly lower because the moment of 2.22 $\mu_B$ applies at 0 K. Iron's 2.15 T is the highest saturation of any element at room temperature and is why steel is the core material of motors and transformers: the flux a core can carry, and therefore its size for a given power, is set by $\mu_0M_s$. Adding silicon to lower losses (Section 27.4) dilutes the iron and reduces $J_s$ to about 2.0 T at 3 % Si; adding cobalt raises it to 2.35–2.4 T in Fe–49Co–2V, the Slater–Pauling maximum, which is why aircraft generators accept the cost of cobalt to save mass.

### Antiferromagnetism and ferrimagnetism

In an **antiferromagnet** neighbouring moments align antiparallel in two equal sublattices, so there is no net magnetization. Order sets in below the **Néel temperature** (MnO 116 K, NiO 525 K, Cr 311 K). Antiferromagnets have few direct uses, but they are essential in spintronic devices, where a thin antiferromagnetic layer (IrMn, PtMn) pins the magnetization of an adjacent ferromagnet by **exchange bias** (Section 27.7).

In a **ferrimagnet** the two sublattices are antiparallel but unequal, leaving a net moment. The most important ferrimagnets are oxides: **spinel ferrites** MFe$_2$O$_4$ (M = Mn, Zn, Ni, Co, Fe), **hexagonal ferrites** BaFe$_{12}$O$_{19}$ and SrFe$_{12}$O$_{19}$, and **garnets** such as yttrium iron garnet (YIG). In the spinel structure (Chapter 2), cations occupy tetrahedral (A) and octahedral (B) sites. Exchange between them runs through intervening oxygen ions (**superexchange**) and aligns A and B antiparallel.

**Worked example — magnetite, the oldest magnet.** Fe$_3$O$_4$ is an inverse spinel: Fe$^{3+}$ on the A sites, and Fe$^{2+}$ plus Fe$^{3+}$ on the B sites. Fe$^{3+}$ (3d$^5$) carries 5 $\mu_B$ and Fe$^{2+}$ (3d$^6$) carries 4 $\mu_B$. The A and B moments are antiparallel, so the two Fe$^{3+}$ moments cancel and the net moment per formula unit is that of Fe$^{2+}$, 4 $\mu_B$. The cubic cell ($a=0.8396$ nm) contains 8 formula units, so

$$
M_s=\frac{8\times4\times9.274\times10^{-24}}{(0.8396\times10^{-9})^3}=5.0\times10^5\ \mathrm{A/m}
$$

or $\mu_0M_s=0.63$ T, against a measured 0.48 MA/m (0.60 T). The calculation is the materials-design method for ferrites: replacing Fe$^{2+}$ in the B sites with Mn$^{2+}$ (5 $\mu_B$) raises the moment; adding non-magnetic Zn$^{2+}$, which prefers A sites, removes A-site moment and, up to about 50 % Zn, increases the net moment further while lowering $T_C$. MnZn and NiZn ferrites are tuned this way. Their saturation (0.3–0.5 T) is only a quarter of iron's, but they are insulators with resistivities of $0.1$–$10^6\ \Omega\,\mathrm m$, so they suffer almost no eddy-current loss at high frequency (Section 27.6).

| Material | $\mu_0M_s$ at 20 °C (T) | $T_C$ (°C) | Note |
|---|---|---|---|
| Fe | 2.15 | 770 | Highest of the elements |
| Co | 1.76 | 1115 | HCP, high anisotropy |
| Ni | 0.61 | 354 | FCC, low anisotropy |
| Fe–49Co–2V | 2.35 | 940 | Highest of all practical alloys |
| Fe–3Si | 2.0 | 740 | Electrical steel |
| Fe$_3$O$_4$ | 0.60 | 585 | Ferrimagnetic spinel |
| MnZn ferrite | 0.4–0.5 | 150–250 | Power ferrite |
| BaFe$_{12}$O$_{19}$ | 0.48 | 450 | Hexagonal hard ferrite |
| Nd$_2$Fe$_{14}$B | 1.61 | 312 | Hard magnet phase |
| SmCo$_5$ | 1.07 | 720–750 | Hard magnet phase |
| Gd | ≈0 (above $T_C$) | 20 | Magnetocaloric reference |

*Table 27.2 — Saturation polarization and Curie temperature of magnetic materials (typical).*

---

## 27.3 Domains, walls and hysteresis

### Why domains form

If exchange aligns all moments, why is a lump of iron usually unmagnetized? Because a uniformly magnetized body has free poles on its surfaces, and their external field stores **magnetostatic energy** proportional to $\mu_0M_s^2$ times the volume — about 1 MJ/m³ for iron. The body lowers this by splitting into **domains**, regions each magnetized to saturation but in different directions, arranged so that flux closes inside the material (Figure 27.2). Domains are not a defect but an equilibrium microstructure, set by a balance of energies:

- **Exchange energy** — penalizes any change of magnetization direction between neighbours; characterized by the exchange stiffness $A$ (about $10^{-11}$ J/m).
- **Magnetocrystalline anisotropy energy** — the magnetization prefers certain crystal directions (**easy axes**: ⟨100⟩ in iron, ⟨111⟩ in nickel, the c-axis in cobalt and in most hard-magnet phases). Its strength is the anisotropy constant $K$, from $10^3$ J/m³ in soft alloys to $10^7$ J/m³ in SmCo$_5$. It arises from spin–orbit coupling, so it is large wherever orbital moment survives (rare earths, cobalt).
- **Magnetostatic (demagnetizing) energy** — from free poles; it also produces **shape anisotropy**, which makes elongated particles prefer to magnetize along their long axis.
- **Magnetoelastic energy** — coupling between magnetization and strain (magnetostriction, Section 27.7).
- **Zeeman energy** — the energy of the magnetization in the applied field, $-\mu_0\mathbf M\cdot\mathbf H$.

### Domain walls

Between domains the magnetization rotates gradually through a **domain wall** (a Bloch wall in bulk material). Exchange favours a wide wall (gentle rotation); anisotropy favours a narrow one (few moments pointing in hard directions). Minimizing their sum gives a wall width and energy per unit area

$$
\delta\approx\pi\sqrt{\frac{A}{K}},\qquad \gamma\approx4\sqrt{AK}
$$

> **Status of the principle: Domain-wall width and energy**
> *Derived.* They follow from minimizing exchange plus anisotropy energy for a one-dimensional rotation (micromagnetics). Numerical factors depend on the anisotropy symmetry; magnetostatic and magnetoelastic terms modify them in thin films and strained material.

**Worked example — walls in a soft and a hard magnet.** For iron, $A=2.1\times10^{-11}$ J/m and $K_1=4.8\times10^4$ J/m³, so

$$
\delta_{\mathrm{Fe}}=\pi\sqrt{\frac{2.1\times10^{-11}}{4.8\times10^4}}=66\ \mathrm{nm},\qquad \gamma_{\mathrm{Fe}}=4\sqrt{(2.1\times10^{-11})(4.8\times10^4)}=4.0\ \mathrm{mJ/m^2}
$$

For Nd$_2$Fe$_{14}$B, $A=7.7\times10^{-12}$ J/m and $K_1=4.9\times10^6$ J/m³, giving $\delta=3.9$ nm and $\gamma=25$ mJ/m². The wall in iron is about 230 atomic spacings wide and is barely disturbed by a single precipitate or dislocation — it moves easily, which is what makes iron soft. The wall in NdFeB is only about five unit cells wide and interacts strongly with any local change in anisotropy, such as a grain boundary — which is why grain-boundary engineering controls the coercivity of rare-earth magnets. The same numbers give the **anisotropy field** $\mu_0H_A=2K_1/M_s$, the field needed to rotate the magnetization coherently against anisotropy: 0.056 T for iron, but 7.7 T for Nd$_2$Fe$_{14}$B ($M_s=1.28$ MA/m). This is the theoretical ceiling for coercivity.

<!-- FIGURE 27.2 | figures/ch27/fig-27-2-domains-and-wall.png | schematic | Domains form to close flux; between them the magnetization rotates through a domain wall whose width is set by exchange against anisotropy. | Content: top row, three blocks of a cubic ferromagnet: single domain with external stray field lines (high magnetostatic energy); two antiparallel domains (stray field reduced); four domains with triangular closure domains at the ends (flux closed, no stray field). Bottom: a Bloch wall shown as a row of about 15 arrows rotating 180 degrees out of the wall plane, with wall width delta marked; inset values delta about 66 nm for Fe and about 4 nm for Nd2Fe14B drawn to the same relative scale. -->

### Magnetization processes and hysteresis

Starting from a demagnetized state, an applied field magnetizes a ferromagnet first by **domain-wall motion** — domains favourably oriented grow at the expense of others — and finally, at high fields, by **rotation** of the magnetization out of easy axes toward the field. Wall motion is impeded by anything that changes the wall energy locally: inclusions, precipitates, voids, grain boundaries, dislocations and residual stress. The wall sticks at such **pinning sites** and jumps between them irreversibly (the Barkhausen jumps, audible as noise in a pickup coil and used for non-destructive evaluation of residual stress in steels). The energy dissipated in these jumps is the area of the **hysteresis loop** (Figure 27.3).

The loop is characterized by the saturation $B_s$, the **remanence** $B_r$ left at zero field, and the **coercivity** $H_c$, the reverse field that brings $B$ (or, for magnets, $M$: the intrinsic coercivity $H_{cJ}$) back to zero. The two ends of the magnetic-materials spectrum are distinguished by $H_c$, which spans about eight orders of magnitude: below 1 A/m in the best nanocrystalline alloys, above $2\times10^6$ A/m in dysprosium-rich NdFeB. Since $M_s$ varies far less, **coercivity is the property that microstructure controls**.

<!-- FIGURE 27.3 | figures/ch27/fig-27-3-soft-hard-loops.png | plot | Soft and hard magnetic materials differ mainly in coercivity: a narrow loop stores little loss per cycle, a wide loop resists demagnetization. | Content: left panel (soft): x-axis H from -100 to +100 A/m, y-axis B from -2 to +2 T; grain-oriented Si steel loop (Bs about 1.9 T at the edge, Br about 1.5 T, Hc about 8 A/m) and a nanocrystalline Fe-Si-B-Nb-Cu loop (flatter, Bs 1.2 T, Hc about 1 A/m); initial magnetization curve dashed. Right panel (hard): x-axis mu0 H from -2 to +2 T (equivalently -1600 to +1600 kA/m), y-axis J or B from -1.5 to +1.5 T; sintered NdFeB: J loop square, Br 1.3 T, HcJ about 1.6 MA/m; B loop with slope mu0 in second quadrant, HcB about 0.95 MA/m; Sr-ferrite loop for comparison (Br 0.42 T, HcJ 0.3 MA/m). Mark Br, Hc, HcJ, Bs. -->

### Coercivity and microstructure

Two mechanisms set coercivity. In **wall-pinning** materials, $H_c$ rises with the density and strength of obstacles: soft magnets therefore need large grains, few inclusions (carbon, nitrogen, sulfur and oxygen are removed to tens of ppm), no precipitates and no residual stress, all achieved by decarburizing and final annealing. Coercivity of iron and electrical steels scales roughly as $1/D$ with grain size $D$, a magnetic Hall–Petch relation.

In **nucleation-controlled** materials, walls move freely once they exist, but each grain is magnetized as a single domain and reversal requires a reversed domain to nucleate. Coercivity then depends on preventing nucleation at grain surfaces and defects, where local anisotropy is low. Below a critical size (about 20 nm for iron and 0.2–0.3 µm for Nd$_2$Fe$_{14}$B) a particle cannot lower its energy by forming a wall and remains a **single domain**; it can reverse only by coherent rotation, and its coercivity approaches the anisotropy field (the Stoner–Wohlfarth limit). Real magnets reach only 20–40 % of $H_A$ because reversal starts at imperfections.

There is a remarkable exception to the rule that fine grains make materials harder. When grains are smaller than the **exchange length** (about 20–40 nm in Fe-based alloys), exchange coupling averages the randomly oriented anisotropy of many grains, and the effective anisotropy collapses as $D^6$ (the **random-anisotropy model**). Coercivity therefore rises as $1/D$ for large grains, peaks near 0.1–1 µm, and falls steeply for nanocrystalline grains of 10–15 nm (Figure 27.4). Amorphous alloys, with no grains at all, are similarly soft. This is why the softest magnetic materials are either amorphous or nanocrystalline.

> **Status of the principle: Random-anisotropy model ($H_c\propto D^6$)**
> *Approximate.* It assumes randomly oriented, exchange-coupled grains much smaller than the exchange length and neglects stress and induced anisotropies. It explains the extreme softness of nanocrystalline Fe–Si–B–Nb–Cu; residual magnetostriction and field-induced anisotropy set the floor in practice.

<!-- FIGURE 27.4 | figures/ch27/fig-27-4-coercivity-vs-grain-size.png | plot | Coercivity against grain size: wall pinning makes coarse-grained metals harder as grains shrink, until exchange averaging makes nanocrystalline alloys extremely soft. | Content: x-axis grain size D from 1 nm to 10 mm (log); y-axis coercivity Hc from 0.1 to 1e5 A/m (log). Right-hand branch Hc proportional to 1/D: Fe-Si electrical steels (D 0.1–10 mm, Hc 5–50 A/m), permalloy, 50Ni-Fe. Peak near D about 0.1–1 um (Hc 1e3–1e4 A/m, near the single-domain size). Left-hand branch Hc proportional to D^6: nanocrystalline Fe-Cu-Nb-Si-B (D 10–15 nm, Hc 0.5–2 A/m), nanocrystalline Fe-Zr-B. Amorphous alloys plotted as a band at the left edge (Hc 1–5 A/m). Mark the exchange length Lex about 35 nm as a vertical dashed line. -->

---

## 27.4 Soft magnets: electrical steels, ferrites, amorphous and nanocrystalline alloys

A soft magnet must carry as much flux as possible (high $B_s$), be magnetized by a small current (high permeability, low $H_c$) and waste little energy per cycle (low hysteresis and eddy-current loss). No material maximizes all three, and the selection is dominated by **operating frequency** (Table 27.3).

| Material | $B_s$ (T) | $H_c$ (A/m) | $\rho$ ($\mu\Omega\,\mathrm m$) | Form | Typical frequency and use |
|---|---|---|---|---|---|
| Low-carbon steel / pure iron | 2.1 | 50–200 | 0.1–0.15 | Solid, sheet | DC: relays, electromagnet poles, shielding |
| Non-oriented Fe–(2–3.5)Si | 1.9–2.0 | 30–80 | 0.4–0.6 | 0.2–0.65 mm laminations | 50 Hz–1 kHz: motors, generators |
| Grain-oriented Fe–3Si | 2.03 | 5–10 | 0.48–0.5 | 0.18–0.30 mm laminations | 50/60 Hz: power transformers |
| Fe–6.5Si | 1.8 | 20–40 | 0.82 | 0.1–0.3 mm sheet | 400 Hz–10 kHz: high-speed motors, reactors |
| Fe–49Co–2V | 2.35 | 50–150 | 0.4 | Laminations | Aircraft generators and actuators |
| Ni–Fe (80Ni, Mumetal) | 0.75–0.8 | 0.5–2 | 0.55–0.6 | Sheet, tape | Shielding, current sensors, signal transformers |
| Fe-based amorphous (Fe–B–Si) | 1.56 | 2–4 | 1.3 | 20–30 µm ribbon | 50 Hz distribution transformers; to 20 kHz |
| Nanocrystalline (Fe–Cu–Nb–Si–B) | 1.2–1.25 | 0.5–1.5 | 1.15–1.2 | 15–25 µm tape | 1–200 kHz: inverter chokes, EMI filters, wireless charging |
| MnZn ferrite | 0.4–0.5 | 10–20 | $10^5$–$10^7$ | Sintered ceramic | 10 kHz–2 MHz: power-supply transformers |
| NiZn ferrite | 0.3–0.4 | 50–300 | $>10^{11}$ | Sintered ceramic | 1–500 MHz: EMI suppression, RF |
| Soft magnetic composite (iron powder) | 1.5–1.8 | 150–400 | high (insulated particles) | Pressed powder | 3D-flux motors, chokes to 100 kHz |

*Table 27.3 — Soft magnetic materials (typical values).*

### Electrical steels

About 15 million tonnes of electrical steel are produced each year, and their losses amount to a few per cent of all electricity generated, so small improvements matter globally. **Silicon** is the essential alloying element. Adding 3 % Si to iron raises resistivity from 0.1 to about 0.5 $\mu\Omega\,\mathrm m$, cutting eddy currents (Section 27.6); it lowers the magnetocrystalline anisotropy and magnetostriction (lower hysteresis, less transformer hum); and it removes the $\alpha$–$\gamma$ transformation (Chapter 15), so the sheet can be annealed at high temperature for grain growth without phase change. The price is a lower saturation and brittleness: above about 3.5 % Si the alloy cannot be cold-rolled conventionally; 6.5 % Si sheet, which has nearly zero magnetostriction, is made by siliconizing 3 % sheet by chemical vapour deposition and diffusion.

**Non-oriented** (NO) steels have nearly random texture, because the flux in a motor rotates within the sheet plane. **Grain-oriented** (GO) steels for transformers, where flux runs along the strip, exploit the anisotropy of iron. Through **secondary recrystallization** (abnormal grain growth, Chapter 10), controlled by fine MnS or AlN inhibitor precipitates, a few grains with the {110}⟨001⟩ **Goss texture** consume the matrix during a final high-temperature anneal and grow to centimetres. The easy ⟨001⟩ axis then lies within a few degrees of the rolling direction. Because large grains mean widely spaced domain walls, which move fast and generate high eddy currents locally, GO steel is further improved by **domain refinement**: laser scribing or mechanical grooving introduces lines of local stress across the strip that subdivide the domains, and a tensile phosphate–silica insulating coating adds a further 10–20 % reduction. The best grain-oriented steels lose about 0.7 W/kg at 1.7 T and 50 Hz.

### Ferrites

For frequencies above about 10 kHz, the eddy-current loss of any metal becomes prohibitive, and the insulating ferrites take over. **MnZn ferrites** have high permeability (2000–15 000) and serve switch-mode power supplies, EV on-board chargers and wireless chargers from 10 kHz to about 2 MHz. **NiZn ferrites**, with resistivity above $10^{11}\ \Omega\,\mathrm m$, serve to hundreds of megahertz, as the beads clipped onto cables to suppress interference. As sintered ceramics, their properties depend on processing as much as composition: grain size, porosity, the Fe$^{2+}$ content set by the oxygen partial pressure during cooling (Chapter 5), and insulating CaO–SiO$_2$ grain boundaries that raise resistivity. Their weaknesses are low saturation, a low Curie temperature, and brittleness: ferrite cores crack under thermal shock and mechanical clamping (Chapter 17).

### Amorphous and nanocrystalline alloys

Rapid solidification (Chapter 9) on a spinning copper wheel at about $10^6$ K/s produces ribbons of **amorphous** Fe$_{78}$B$_{13}$Si$_9$ 20–30 µm thick. With no crystal structure there is no magnetocrystalline anisotropy and no grain boundaries to pin walls; the ribbon is thin, and its resistivity (1.3 $\mu\Omega\,\mathrm m$) is more than twice that of silicon steel. Its core loss at 50 Hz is about a third to a quarter of that of the best GO steel — the transformer of the opening paragraph. The costs are lower saturation (1.56 T, so larger cores), brittleness after the stress-relief anneal, a lower stacking factor and noise from higher magnetostriction.

**Nanocrystalline** alloys such as Fe$_{73.5}$Cu$_1$Nb$_3$Si$_{13.5}$B$_9$ (Finemet) start as amorphous ribbon and are annealed at about 550 °C. Copper clusters nucleate a high density of Fe–Si crystals; niobium, which partitions to the remaining amorphous matrix and diffuses slowly, prevents them from growing beyond 10–15 nm. The result combines the random-anisotropy softness of Figure 27.4 ($H_c$ below 1 A/m, permeability near $10^5$) with near-zero magnetostriction, because the positive magnetostriction of the amorphous phase and the negative one of the Fe–Si crystals cancel. A processing route designed by nucleation and growth theory produces the softest high-saturation material available.

### Soft magnetic composites

Iron powder particles coated with a thin insulating layer and pressed into shape form **soft magnetic composites** (SMCs). Their permeability is low (the insulating gaps act as distributed air gaps), and their hysteresis loss is high (the plastic deformation of pressing creates dislocations; Chapter 38), but they allow three-dimensional flux paths impossible in laminated stacks — axial-flux and transverse-flux motors, and inductor cores with built-in gaps.

---

## 27.5 Hard magnets: NdFeB, SmCo, ferrites; energy product

### What a permanent magnet must do

A permanent magnet supplies a field in an air gap without consuming energy. It operates in the **second quadrant** of its hysteresis loop — the demagnetization curve — at a working point set by the geometry of the magnetic circuit: the magnet's own demagnetizing field drives it below $B_r$ toward negative $H$. Three properties matter: a high remanence $B_r$ (the flux it supplies), a high intrinsic coercivity $H_{cJ}$ (resistance to demagnetization by its own field, by the armature reaction in a motor, and by heat), and a high **maximum energy product** $(BH)_{\max}$, the largest value of $\lvert BH\rvert$ on the demagnetization curve. For a magnet of volume $V_m$ producing field $B_g$ in an air gap of volume $V_g$, the ideal relation

$$
V_m=\frac{B_g^2V_g}{\mu_0(BH)_{\max}}
$$

shows that the energy product is the magnet's performance index: the magnet volume needed for a given gap field is inversely proportional to it.

For an ideal magnet with a square $J$–$H$ loop and $H_{cJ}>B_r/\mu_0$, the $B$–$H$ demagnetization line is straight with slope $\mu_0$ and

$$
(BH)_{\max}=\frac{B_r^2}{4\mu_0}
$$

which is the theoretical upper limit for a given remanence.

> **Status of the principle: $(BH)_{\max}\le B_r^2/4\mu_0$**
> *Derived.* It follows from a straight-line demagnetization curve with recoil permeability $\mu_0$; it is reached only when the intrinsic coercivity exceeds $B_r/\mu_0$ and the loop is square. Real magnets approach it within 5–10 %; materials with low coercivity (AlNiCo) fall far short.

### The families

| Material | $B_r$ (T) | $H_{cJ}$ (kA/m) | $(BH)_{\max}$ (kJ/m³) | $T_C$ (°C) | Max. service (°C) | Coercivity mechanism |
|---|---|---|---|---|---|---|
| AlNiCo 5 | 1.2–1.3 | 50–60 | 40–45 | 860 | 500 | Shape anisotropy of aligned Fe–Co rods |
| Sr/Ba hexaferrite (sintered) | 0.38–0.45 | 250–400 | 25–38 | 450 | 250 | Magnetocrystalline; fine single-domain grains |
| SmCo$_5$ | 0.9–1.0 | 1200–2400 | 160–200 | 720–750 | 250 | Nucleation |
| Sm$_2$Co$_{17}$ (Sm(Co,Fe,Cu,Zr)$_z$) | 1.05–1.15 | 800–2000 | 190–260 | 800–850 | 350 | Wall pinning by cellular precipitate |
| NdFeB sintered | 1.2–1.45 | 900–2800 | 260–420 | 310–340 | 80–200 (grade) | Nucleation, controlled by Nd-rich boundaries |
| NdFeB bonded (polymer) | 0.6–0.7 | 700–1000 | 60–90 | 310 | 120–150 | Nanocrystalline melt-spun powder |

*Table 27.4 — Permanent-magnet materials (typical commercial ranges at 20 °C).*

**Ferrites** (SrFe$_{12}$O$_{19}$, BaFe$_{12}$O$_{19}$) are cheap, chemically inert and electrically insulating, and still make up most permanent magnets by mass — loudspeakers, small DC motors, fridge seals. Their hexagonal structure has strong uniaxial anisotropy ($\mu_0H_A\approx1.7$ T), and powders are milled to about 1 µm (near single-domain size), aligned in a field, pressed and sintered. Their low $B_r$ limits energy product. Unusually, their coercivity rises with temperature, so they are at risk of demagnetization in the cold.

**AlNiCo** alloys owe their coercivity to shape anisotropy: spinodal decomposition (Chapter 10) during a heat treatment in a magnetic field produces elongated Fe–Co-rich rods in a weakly magnetic Ni–Al matrix. Their high $B_r$ and exceptional temperature stability suit them to sensors and instruments, but their low coercivity means they are easily demagnetized.

**Samarium–cobalt** magnets (SmCo$_5$, Sm$_2$Co$_{17}$) exploit the huge anisotropy of the Sm 4f shell in a hexagonal cobalt-rich lattice. They combine high coercivity with a high Curie temperature and low temperature coefficient ($-0.03$ %/K for $B_r$), and they resist corrosion. They are used in aerospace and military actuators, high-temperature motors and precision instruments where cost matters less than stability.

**Neodymium–iron–boron** (Nd$_2$Fe$_{14}$B), discovered in 1982–84, has the highest energy product (Figure 27.5) because it combines iron's large moment with neodymium's anisotropy in a tetragonal structure. Sintered magnets are made by powder metallurgy (Chapter 38): strip-cast alloy is hydrogen-decrepitated and jet-milled to 3–5 µm, aligned in a field, pressed and liquid-phase sintered. The Nd-rich grain-boundary phase is the crucial microstructural feature: it magnetically isolates each grain so that a reversed domain nucleated in one grain does not spread to its neighbours, and it smooths grain surfaces where nucleation would start. NdFeB's weaknesses are a low Curie temperature (about 312 °C), a strongly falling coercivity with temperature (about $-0.5$ %/K) and poor corrosion resistance (coatings of Ni–Cu–Ni or epoxy are standard). For motors running at 150–200 °C, part of the Nd is replaced by **dysprosium** or terbium, whose larger anisotropy raises $H_{cJ}$ but whose moments couple antiparallel to iron and lower $B_r$. Because Dy is scarce and expensive, **grain-boundary diffusion** processes now place it only in a thin shell at each grain surface — where reversal nucleates — cutting heavy-rare-earth content by half or more.

**Worked example — magnet volume for an air gap.** A motor needs $B_g=1.0$ T across an air gap of area 10 cm² and length 1 mm, so $V_g=10^{-6}$ m³. First compare ideal limits: a sintered NdFeB magnet with $B_r=1.30$ T has $(BH)_{\max}\le1.30^2/(4\mu_0)=336$ kJ/m³; a ferrite with $B_r=0.40$ T has at most 32 kJ/m³. Taking realistic values of 400 kJ/m³ for a top NdFeB grade ($B_r\approx1.42$ T) and 30 kJ/m³ for ferrite:

$$
V_{m,\mathrm{NdFeB}}=\frac{(1.0)^2(10^{-6})}{(4\pi\times10^{-7})(400\times10^3)}=2.0\times10^{-6}\ \mathrm{m^3}=2.0\ \mathrm{cm^3},\qquad V_{m,\mathrm{ferrite}}=26.5\ \mathrm{cm^3}
$$

The ferrite design also needs flux concentration, because its remanence of 0.4 T is below the 1.0 T required in the gap, so the ferrite magnet must have a pole face at least 2.5 times the gap area. Thirteen times the magnet volume, plus the iron to concentrate the flux, is why NdFeB took over every application where mass or size is critical: electric-vehicle traction motors (about 1–2 kg of NdFeB each), direct-drive wind generators (about 600 kg per MW), hard-disk actuators, phone vibrators and earbuds.

<!-- FIGURE 27.5 | figures/ch27/fig-27-5-energy-product-history.png | plot | A century of permanent magnets: the maximum energy product has risen about a hundredfold through new phases and microstructures. | Content: x-axis year 1900 to 2025; y-axis (BH)max in kJ/m3, 0 to 480 (log or linear). Points: carbon/tungsten steel (about 2, 1900), cobalt steel KS steel (8, 1917), AlNiCo (10 to 45, 1931–1960), Ba ferrite (28, 1952), Sr ferrite (38, 1970s), SmCo5 (160–200, 1967–1970), Sm2Co17 (240–260, 1977), sintered NdFeB (280 in 1984 rising to 420–440 by 2010s), with the theoretical limit of Nd2Fe14B, (mu0 Ms)^2/4mu0 about 515 kJ/m3, as a dashed horizontal line. Secondary annotation: relative magnet volume for a fixed air-gap energy. -->

### Criticality

Rare-earth magnets illustrate the materials-supply problem of Chapter 49. Light rare earths (Nd, Pr) are not geologically rare, but separating them from each other is a long, chemically intensive solvent-extraction process concentrated in a few countries; heavy rare earths (Dy, Tb) come mainly from a few ion-adsorption clay deposits. Responses span the materials discipline: grain-boundary diffusion to use less Dy, finer-grained magnets with higher intrinsic coercivity, Ce-substituted magnets, recycling of magnets from hard drives and motors, and motor designs (induction, wound-field synchronous, switched-reluctance) that avoid permanent magnets at some cost in efficiency or power density.

---

## 27.6 Magnetic losses

Every time a soft magnet is cycled, energy is lost as heat. The **core loss** per unit mass is usually separated into three parts:

$$
P=P_h+P_{cl}+P_{ex}
$$

- **Hysteresis loss** $P_h$, the loop area times frequency: $P_h\propto f\,B_p^{\,n}$ with $n\approx1.6$–2 (Steinmetz's empirical law). It is reduced by everything that makes walls move freely: purity, large grains, low anisotropy, stress relief.
- **Classical eddy-current loss** $P_{cl}$. A changing flux induces circulating currents in a conducting core. For a lamination of thickness $d$ and resistivity $\rho$ with sinusoidal peak induction $B_p$ at frequency $f$, assuming uniform magnetization,

$$
P_{cl}=\frac{\pi^2d^2B_p^2f^2}{6\rho\,d_m}\quad(\mathrm{W/kg})
$$

where $d_m$ is the density. It grows as the square of thickness and of frequency, and falls with resistivity — the reasons for thin laminations, silicon additions and insulating ferrites.
- **Excess (anomalous) loss** $P_{ex}$, due to the fact that magnetization changes not uniformly but by the jerky motion of a few domain walls, which produces local eddy currents much larger than the uniform-magnetization estimate. It scales roughly as $f^{1.5}$ and is reduced by domain refinement (Section 27.4).

> **Status of the principle: Loss separation and the Steinmetz law**
> *Empirical* for the Steinmetz exponent and the excess term; *derived* for the classical eddy term, which follows from Maxwell's equations for a thin sheet under the assumption of uniform magnetization and negligible skin effect. The separation is a useful accounting, not three independent physical processes.

**Worked example — why laminations get thinner as frequency rises.** For non-oriented 3 % Si steel ($\rho=0.52\ \mu\Omega\,\mathrm m$, $d_m=7650$ kg/m³) 0.35 mm thick at $B_p=1.5$ T and 50 Hz:

$$
P_{cl}=\frac{\pi^2(0.35\times10^{-3})^2(1.5)^2(50)^2}{6(0.52\times10^{-6})(7650)}=0.28\ \mathrm{W/kg}
$$

The measured total loss of such a grade is about 2.5 W/kg; hysteresis and excess loss dominate at 50 Hz. Plain low-carbon steel 0.5 mm thick ($\rho=0.15\ \mu\Omega\,\mathrm m$) would have a classical eddy loss of 2.0 W/kg at the same induction — seven times more — which is why silicon matters. Now raise the frequency to 400 Hz, as in an aircraft generator or a high-speed EV motor, and lower the induction to 1.0 T: the 0.35 mm lamination's classical loss becomes 8.1 W/kg, and switching to 0.20 mm sheet brings it down to 2.6 W/kg. At 20 kHz and above, no lamination thin enough can be rolled economically, and the designer moves to 20 µm amorphous or nanocrystalline tape or to insulating ferrite (Figure 27.6). The skin depth $\delta_s=\sqrt{\rho/(\pi f\mu_0\mu_r)}$, 0.73 mm at 50 Hz but 0.26 mm at 400 Hz for silicon steel with $\mu_r=5000$, marks the same transition: once the lamination is thicker than about the skin depth, the interior carries little flux.

<!-- FIGURE 27.6 | figures/ch27/fig-27-6-core-loss-vs-frequency.png | plot | Core loss against frequency for soft magnetic materials: each family dominates a frequency band set by its resistivity and thickness. | Content: x-axis frequency 10 Hz to 10 MHz (log); y-axis specific core loss 0.1 to 10000 W/kg (log), at a fixed peak induction of 0.1 T for all curves (with a second set at 1.0 T for metals below 1 kHz). Curves: NO Fe-Si 0.35 mm (steepest rise, f^2 above 400 Hz); GO Fe-Si 0.23 mm; Fe-6.5Si 0.10 mm; Fe-based amorphous 25 um; nanocrystalline 18 um (lowest up to about 100 kHz); MnZn power ferrite (lowest from about 100 kHz to 1 MHz); NiZn ferrite (above 1 MHz). Shade typical application bands: grid 50/60 Hz, aircraft 400 Hz, motor drives 1 kHz, SMPS 100 kHz–1 MHz, RF. -->

Core losses add up. A large power transformer of 60 t core mass with a loss of 0.9 W/kg dissipates 54 kW continuously, 470 MWh a year; at 0.3 W/kg (amorphous) it would dissipate 160 MWh. Loss also matters for heat: motor cores at high frequency run hot, and NdFeB rotor magnets heated by eddy currents induced by inverter harmonics can lose coercivity — which is why magnets themselves are segmented into insulated pieces.

---

## 27.7 Magnetostriction, magnetocaloric and spintronic materials

### Magnetostriction

When a ferromagnet is magnetized, it changes shape: the **magnetostriction** $\lambda=\Delta L/L$ arises from the same spin–orbit coupling that produces anisotropy, which makes the bond lengths depend on magnetization direction. Saturation magnetostriction $\lambda_s$ is about $-7\times10^{-6}$ for iron, $-34\times10^{-6}$ for nickel, and as large as $1000$–$2000\times10^{-6}$ in **Terfenol-D** (Tb$_{0.3}$Dy$_{0.7}$Fe$_2$), whose rare-earth 4f shells give giant magnetoelastic coupling. Galfenol (Fe–19Ga, $\lambda_s\approx250$–$350\times10^{-6}$) is ductile and machinable.

Magnetostriction is a nuisance and a tool. It causes the 100 Hz hum of 50 Hz transformers (the strip lengthens twice per cycle), and the push to low-noise substations favours low-$\lambda$ 6.5 % Si steel and well-annealed GO steel. Conversely, Terfenol-D drives low-frequency high-power sonar projectors and precision actuators: a 50 mm rod at $1600\times10^{-6}$ strain moves 80 µm with forces of kilonewtons. The inverse (Villari) effect — stress changes permeability — gives torque and force sensors, and the Barkhausen and magnetoelastic responses are used to measure residual stress in steel components non-destructively. Magnetic shape-memory alloys (Ni–Mn–Ga), which reach strains of several per cent by field-driven twin-boundary motion, are discussed with smart materials in Chapter 29.

### Magnetocaloric materials

Magnetizing a ferromagnet near its Curie temperature aligns moments and lowers the magnetic entropy; under adiabatic conditions the lattice warms to compensate. Removing the field cools it. This **magnetocaloric effect** is largest where magnetization changes most steeply with temperature, near $T_C$. Gadolinium ($T_C=20$ °C) warms by about 3 K per tesla. Materials with a first-order magnetostructural transition — Gd$_5$(Si,Ge)$_4$, La(Fe,Si)$_{13}$H$_x$, MnFe(P,Si) — show "giant" effects, and their transition temperatures can be tuned by composition so that a cascade of alloys covers a refrigerator's span. Magnetic refrigeration avoids greenhouse refrigerant gases; its materials challenges are hysteresis (which wastes work), mechanical fragmentation from the volume change at the transition, corrosion, and the cost of permanent-magnet field sources. At very low temperatures, adiabatic demagnetization of paramagnetic salts has long been used to reach millikelvin temperatures.

### Spintronic materials

Electrons carry spin as well as charge, and in a ferromagnetic metal the two spin channels conduct differently. In a stack of two ferromagnetic layers separated by a thin non-magnetic metal, the resistance depends on whether their magnetizations are parallel or antiparallel: **giant magnetoresistance** (GMR, discovered 1988, Nobel Prize 2007), about 10–20 % at room temperature in practical spin valves. Replacing the metal spacer by a 1–2 nm crystalline MgO tunnel barrier between CoFeB electrodes gives **tunnelling magnetoresistance** (TMR) of 200–600 % at room temperature, because the MgO lattice filters electrons of one symmetry that are highly spin-polarized in the electrodes — an effect that exists only because the barrier and electrodes are crystallized epitaxially during annealing.

These stacks are materials engineering at the nanometre scale: one layer is pinned by exchange bias to an antiferromagnet (IrMn or PtMn), often via a synthetic antiferromagnet of two Co–Fe layers coupled antiparallel through 0.8 nm of Ru; the other layer is free to follow an external field or to be switched. They are used as read heads in every hard disk, as magnetic sensors in cars (wheel-speed, steering-angle and current sensors), and as **magnetic random-access memory** (MRAM), in which a spin-polarized current switches the free layer by **spin-transfer torque**. MRAM is non-volatile, radiation-hard and fast, and is embedded in microcontrollers and in spacecraft electronics. Spin–orbit torque from heavy-metal layers (Pt, W, Ta), skyrmions and antiferromagnetic spintronics are active research directions.

> **Boundary.** The quantum mechanics of atomic moments, exchange and spin-dependent transport belongs to the Engineering Physics book; the design of transformer, motor and inductor cores, and of magnetic shielding, is developed in the *Materials Core (EEE)* book, Chapter 16.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How does superconductivity, the perfect diamagnetism of Section 27.1, produce the magnets of MRI and fusion? | Chapter 25 |
| How do magnetostriction and magnetic shape-memory effects serve as actuators? | Chapter 29 |
| How do magnetic nanoparticles behave (superparamagnetism, hyperthermia, ferrofluids)? | Chapter 30 |
| Which magnetic materials are used in implants and MRI-compatible devices? | Chapter 31 |
| What magnetic materials do wind generators and electric vehicles need, and how scalable are they? | Chapter 32 |
| How do magnets and soft cores degrade through corrosion and high temperature? | Chapters 33 and 35 |
| How are rapid solidification and powder processing used to make amorphous ribbons and sintered magnets? | Chapters 9 and 38 |
| How are spintronic multilayers deposited with sub-nanometre control? | Chapter 41 |
| How are domains and magnetic properties measured (VSM, Kerr microscopy, Mössbauer, neutron diffraction)? | Chapters 42 and 43 |
| How are magnetic properties and anisotropy computed, and new magnet phases screened? | Chapters 45 and 47 |
| How are rare-earth magnets recycled, and how is criticality weighed in selection? | Chapters 48 and 49 |

**Next:** Chapter 28 turns from the response of materials to magnetic fields to their response to the electromagnetic field of light, and asks what makes materials transparent, coloured, luminous and able to guide light.
