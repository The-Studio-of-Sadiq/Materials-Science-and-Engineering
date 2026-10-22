# Chapter 24 — Thermal Properties

*Part VI · Physical and Functional Properties*

On a cold morning a cook pours boiling water into a glass baking dish that has just come out of the refrigerator, and the dish shatters. Its borosilicate cousin, the laboratory beaker, survives the same treatment every day. A few kilometres away, a railway engineer checks the temperature forecast: continuously welded rail laid on a cool spring day will be in compression on a hot summer afternoon, and if the stress is high enough the track buckles sideways. At an airport, a turbofan's first-stage turbine blades run in gas several hundred kelvin hotter than the melting point of the nickel alloy they are made of, protected by a ceramic coating a quarter of a millimetre thick. In a data centre, a processor dissipating 300 W through a die the size of a postage stamp depends on a copper lid, a smear of grease and a finned aluminium block to stay below 100 °C.

Each of these is a problem in thermal properties: how much heat a material stores, how quickly it carries heat, how much it expands when heated, and what happens when expansion is resisted. This chapter traces each property to the atomic vibrations and electrons that produce it, and then follows it into stresses, shocks, coatings, insulation and thermal management across engineering.

> **Why do some solids store, conduct and expand with heat so differently from others?**
> **How do temperature changes produce stresses large enough to buckle rails, crack ceramics and spall coatings, and how are materials chosen to manage heat?**

| Concept | Engineering destination |
|---|---|
| Phonons and heat capacity | Thermal mass of brakes and buildings, cryogenic design, thermal energy storage |
| Thermal expansion | Rails and bridges, bimetals, Invar instruments, glass-to-metal seals, low-expansion cookware |
| Thermal conductivity | Heat exchangers, cookware, electronic substrates, turbine cooling, insulation |
| Thermal diffusivity and transient heat flow | Quenching of steel, cycle times of moulding, curing of mass concrete, touch temperature |
| Thermal stress and thermal shock | Cracked glassware, refractories, brake discs, ceramic engine parts |
| Thermal barrier coatings and insulation | Gas-turbine blades, furnace linings, buildings, cryogenic tanks, spacecraft |
| Thermal management materials | Electronics cooling, battery packs, LED lighting, aerospace avionics |

**Roadmap.** Storing heat: phonons and heat capacity (24.1) → expanding with heat: the anharmonic potential (24.2) → carrying heat: phonons and electrons (24.3) → how fast temperature changes travel (24.4) → when expansion is resisted: thermal stress and thermal shock (24.5) → keeping heat out: barrier coatings and insulation (24.6) → moving heat on purpose: thermal-management materials (24.7).

---

## 24.1 Phonons and heat capacity

### Definitions

The **heat capacity** of a body is the heat needed to raise its temperature by one kelvin. As a material property it is quoted per unit mass (**specific heat** $c$, J kg⁻¹ K⁻¹), per mole (J mol⁻¹ K⁻¹) or per unit volume ($\rho c$, J m⁻³ K⁻¹). For solids, $c_p$ and $c_v$ differ by $c_p-c_v=TV\beta^2K$ (with $\beta$ the volume expansion coefficient and $K$ the bulk modulus), only a few percent at room temperature; data are quoted as $c_p$, theory gives $c_v$.

> **Boundary.** The thermodynamic definitions of heat capacity and the $c_p$–$c_v$ relation belong to the Advanced Chemistry book; the quantum mechanics of the harmonic oscillator and of phonons to Engineering Physics. They are used here, not derived.

### Lattice vibrations and phonons

In a solid, heat is stored mainly in the vibrations of atoms about their equilibrium positions. Because neighbouring atoms are coupled by bonds, the vibrations are not independent: they are collective waves — **normal modes** — running through the crystal. A crystal of $N$ atoms has $3N$ normal modes, each with a wavevector $\mathbf k$ in the Brillouin zone (Chapter 4) and a frequency $\omega(\mathbf k)$ given by the **dispersion relation**. For a chain of atoms of mass $m$ connected by springs of stiffness $\kappa$ and spacing $a$,

$$
\omega(k)=2\sqrt{\frac{\kappa}{m}}\left\lvert\sin\frac{ka}{2}\right\rvert
$$

At long wavelengths ($k\to0$) this is a sound wave, $\omega=v_sk$ with $v_s=a\sqrt{\kappa/m}$; at the zone boundary the frequency saturates at $\omega_{\max}=2\sqrt{\kappa/m}$. Crystals with several atoms per primitive cell also have **optical** branches. Quantum mechanics allows each mode to hold energy only in units of $\hbar\omega$; a quantum of vibrational energy is a **phonon**. Heat capacity counts how many phonons are excited as temperature rises; thermal conductivity (Section 24.3) follows how phonons travel and scatter.

The scaling $\omega\propto\sqrt{\kappa/m}$ is the thread through this chapter: **stiff bonds and light atoms give high vibration frequencies**, which raise sound velocities, delay the excitation of modes to higher temperatures and, as we shall see, favour high thermal conductivity.

### The classical limit: Dulong–Petit

Classically each normal mode is a harmonic oscillator holding $k_BT$ of energy on average, so a mole of atoms holds $3RT$ and

$$
C_{v,m}=3R=24.9\ \mathrm{J\,mol^{-1}\,K^{-1}}
$$

This is the **Dulong–Petit law** (1819). Per unit mass it predicts $c=3R/M$, so heavy atoms have low specific heat: lead and tungsten about 120–135 J kg⁻¹ K⁻¹, copper and iron about 390–450, aluminium about 900. Per unit volume, because atomic volumes vary much less than atomic masses, almost all dense solids hold 1.5–4 MJ m⁻³ K⁻¹ (Table 24.1).

> **Status of the principle: Dulong–Petit law**
> *Approximate.* Classical equipartition applied to $3N$ harmonic modes; accurate within a few percent for most metals at and above room temperature, but it overestimates the heat capacity of solids with stiff bonds and light atoms (diamond, Si, SiC, B, Be, oxides) and of every solid at low temperature.

### Einstein's model

Measurements in the 19th century showed that diamond, boron and silicon have heat capacities far below $3R$ at room temperature, and that all solids lose heat capacity at low temperature. **Einstein** (1907) treated every atom as an independent quantum oscillator of one frequency $\omega_E$, defining an **Einstein temperature** $\theta_E=\hbar\omega_E/k_B$. The average energy of a quantum oscillator gives

$$
C_v=3R\left(\frac{\theta_E}{T}\right)^2\frac{e^{\theta_E/T}}{\left(e^{\theta_E/T}-1\right)^2}
$$

At $T\gg\theta_E$ this tends to $3R$; at $T\ll\theta_E$ it falls exponentially, because the thermal energy $k_BT$ is too small to excite even one quantum $\hbar\omega_E$ — the mode is **frozen out**. Its failure is at low temperature: measured heat capacities fall as $T^3$, much more slowly than exponentially. The reason is that a real crystal has long-wavelength acoustic modes of arbitrarily low frequency that remain excited even at very low temperatures. Einstein's single frequency describes optical modes reasonably well; it cannot describe sound waves.

### Debye's model

**Debye** (1912) replaced the single frequency by a spectrum of sound waves, $\omega=v_sk$, cut off at a maximum frequency $\omega_D$ chosen so that the total number of modes is $3N$. The **Debye temperature** $\theta_D=\hbar\omega_D/k_B$ characterizes each solid, and

$$
C_v=9R\left(\frac{T}{\theta_D}\right)^3\int_0^{\theta_D/T}\frac{x^4e^x}{(e^x-1)^2}\,dx
$$

At high temperature $C_v\to3R$. At low temperature the integral becomes a constant and

$$
C_v\approx\frac{12\pi^4}{5}R\left(\frac{T}{\theta_D}\right)^3
$$

the **Debye $T^3$ law**, valid for $T\lesssim\theta_D/50$ and approximately up to $\theta_D/10$. Because $\omega_D\propto v_s$, the Debye temperature is high for stiff, light solids: diamond about 2,230 K, SiC about 1,200 K, Al₂O₃ about 1,040 K, Si 645 K, Fe 470 K, Al 428 K, Cu 343 K, Au 165 K, Pb 105 K. The Debye temperature roughly marks where a solid's vibrations become fully classical, and Figure 24.1 shows that all solids fall on one universal curve of $C_v/3R$ against $T/\theta_D$.

> **Status of the principle: Debye model of heat capacity**
> *Approximate.* Treats lattice vibrations as an isotropic elastic continuum with a single cutoff; it reproduces the $T^3$ law and the high-temperature limit exactly, while at intermediate temperatures the detailed phonon spectrum makes the effective $\theta_D$ vary with temperature by 10–20 %. For compounds with optical branches, a Debye term for acoustic modes plus Einstein terms for optical modes works better.

### The electronic contribution

In a metal the conduction electrons also carry heat capacity, but only those within about $k_BT$ of the Fermi energy $E_F$ can be excited (Pauli exclusion), a fraction $k_BT/E_F\approx0.005$ at room temperature. The electronic heat capacity is linear in temperature, $C_{el}=\gamma T$, with $\gamma=0.695$ mJ mol⁻¹ K⁻² for copper: 0.21 J mol⁻¹ K⁻¹ at 300 K, under 1 % of the lattice term. Because the lattice term falls as $T^3$, the two become equal for copper at about 4 K, and below that electrons dominate.

**Worked example — Why diamond feels "cold" in heat capacity terms.** Compare copper ($\theta_D=343$ K, $M=63.55$ g/mol), silicon ($\theta_D=645$ K, $M=28.09$ g/mol) and diamond ($\theta_D\approx2230$ K, $M=12.01$ g/mol) at 300 K.

Dulong–Petit predicts $c=3R/M$: copper $24.94/0.06355=392$, silicon 888, diamond 2,077 J kg⁻¹ K⁻¹.

Evaluating the Debye integral numerically at $T/\theta_D=0.875$, 0.465 and 0.135 gives $C_v/3R=0.938$, 0.802 and 0.166. Hence $c_v=368$ J kg⁻¹ K⁻¹ for copper (measured $c_p=385$), 712 for silicon (measured 705) and 344 for diamond (measured 509). The Einstein model with $\theta_E\approx0.806\,\theta_D$ gives nearly the same values for copper (366) and silicon (696) — at these temperatures the models agree — but only 187 for diamond.

At room temperature copper is nearly classical, silicon has lost a fifth of its modes and diamond has lost five-sixths in the Debye estimate. Diamond's measured value corresponds to an effective $\theta_D\approx1,870$ K at 300 K, illustrating the temperature dependence of the effective Debye temperature noted in the status box. At low temperature the difference becomes extreme: at 10 K copper's lattice heat capacity is $(12\pi^4/5)R(10/343)^3=0.048$ J mol⁻¹ K⁻¹, 0.2 % of its room-temperature value. That is why small heat leaks warm cryogenic sensors so easily.

<!-- FIGURE 24.1 | figures/ch24/fig-24-1-debye-einstein-heat-capacity.png | plot | Heat capacity of solids versus reduced temperature: the Debye and Einstein models and the classical Dulong–Petit limit, with copper, silicon and diamond at room temperature. | Content: x-axis T/θ_D from 0 to 1.5 (linear); y-axis C_v/3R from 0 to 1.05. Debye curve (solid): 0.200 at T/θ_D = 0.146 (Cu at 50 K), 0.592 at 0.29, 0.867 at 0.58, 0.938 at 0.875, 0.977 at 1.46. Einstein curve with θ_E = 0.806 θ_D (dashed): falls below Debye at low T (0.003 at T/θ_D = 0.078, versus Debye 0.036). Horizontal line at 1 labelled "Dulong–Petit 3R". Markers at 300 K: Cu (T/θ_D = 0.875, 0.938), Si (0.465, 0.802), diamond (0.135, 0.166; measured value 0.245 shown as open marker). Inset log–log plot of C_v versus T for Cu 1–50 K showing the T³ lattice term and the linear electronic term γT crossing near 4 K. -->

**Table 24.1 — Heat capacity at 25 °C (typical values).**

| Material | $c_p$ (J kg⁻¹ K⁻¹) | $\rho$ (kg/m³) | $\rho c_p$ (MJ m⁻³ K⁻¹) | $\theta_D$ (K) |
|---|---|---|---|---|
| Lead | 129 | 11,340 | 1.46 | 105 |
| Tungsten | 132 | 19,300 | 2.55 | 400 |
| Copper | 385 | 8,960 | 3.45 | 343 |
| Carbon steel | 470–490 | 7,850 | 3.7–3.8 | ~470 (Fe) |
| Aluminium | 897 | 2,700 | 2.42 | 428 |
| Silicon | 705 | 2,330 | 1.64 | 645 |
| Diamond | 509 | 3,510 | 1.79 | ~2,230 |
| Alumina | 880 | 3,980 | 3.50 | ~1,040 |
| Soda-lime glass | 840 | 2,500 | 2.10 | — |
| Concrete | 750–1,000 | 2,300–2,400 | 1.8–2.3 | — |
| Polypropylene | 1,900 | 905 | 1.72 | — |
| Epoxy | 1,100 | 1,200 | 1.32 | — |
| Wood (softwood, dry) | 1,300–1,700 | 400–600 | 0.6–0.9 | — |
| Water (reference) | 4,180 | 1,000 | 4.18 | — |

### Where heat capacity matters

Heat capacity decides how much a component's temperature rises when it absorbs energy faster than conduction can remove it. Carbon–carbon aircraft brakes absorb tens of megajoules in a rejected take-off because carbon's specific heat (about 1,400 J kg⁻¹ K⁻¹ at 500 °C, rising as more modes are excited) and its tolerance of 2,000 °C let a few hundred kilograms soak up that energy. Concrete and masonry give buildings thermal mass; solar plants store heat in molten nitrate salts; **phase-change materials** (paraffins, salt hydrates) add latent heat for battery packs and building panels; and in welding and additive manufacturing the heat capacity of the surrounding metal sets the cooling rate of the melt pool (Chapters 39 and 40).

---

## 24.2 Thermal expansion and the anharmonic potential

### Why solids expand

If atoms vibrated in a perfectly harmonic (parabolic) potential, their average position would not change as the vibration amplitude increased, and solids would not expand. Real interatomic potentials are **anharmonic** (Figure 24.2): steeply repulsive when atoms are pushed together (overlapping electron shells) and shallow when they are pulled apart (the attraction fades slowly). As temperature rises and atoms vibrate with larger amplitude, they spend more time at separations larger than the equilibrium value, so the mean spacing grows.

Expanding the potential about its minimum $r_0$ as $U(x)=\tfrac12\kappa x^2-\tfrac13g x^3+\dots$ (with $x=r-r_0$ and $g>0$ for the asymmetric well) and averaging with classical statistics gives a mean displacement $\langle x\rangle=gk_BT/\kappa^2$ — linear in $T$, proportional to the asymmetry $g$ and inversely proportional to the square of the stiffness $\kappa$. Three robust trends follow:

- **Stiffly bonded, high-melting solids expand little.** Deep, narrow potential wells are also nearly symmetric near the bottom. Covalent and refractory solids (diamond 1.0, SiC 4.0, W 4.5 ppm/K) expand much less than low-melting metals (Al 23, Zn 30, Pb 29 ppm/K) and polymers (50–200 ppm/K). An empirical rule is that the linear expansion accumulated from 0 K to the melting point is roughly constant, $\alpha T_m\approx0.015$–0.03 for metals and simple ceramics.
- **Weakly bonded directions expand most.** Graphite expands about 27 ppm/K across its van der Waals-bonded layers and about −1 ppm/K within them; polymers expand mainly through their interchain contacts.
- **Expansion follows heat capacity.** At low temperature, where modes are frozen out, expansion also vanishes; above $\theta_D$, both are nearly constant.

### The Grüneisen relation

The third trend is made quantitative by the **Grüneisen relation**. Anharmonicity means that vibration frequencies depend on volume; the **Grüneisen parameter** $\gamma=-d\ln\omega/d\ln V$ measures how much. Thermodynamics then gives

$$
\alpha_V=3\alpha=\frac{\gamma\,C_v}{K\,V_m}
$$

with $\alpha_V$ the volume and $\alpha$ the linear expansion coefficient, $C_v$ the molar heat capacity, $K$ the bulk modulus and $V_m$ the molar volume. For most solids $\gamma$ lies between 1 and 3 and is nearly independent of temperature, so $\alpha(T)$ follows $C_v(T)$: proportional to $T^3$ at low temperature and nearly constant above $\theta_D$. Stiff solids (large $K$) expand less.

> **Status of the principle: Grüneisen relation**
> *Derived.* Exact thermodynamics once the Grüneisen parameter is defined; the approximation is that $\gamma$ is a single, temperature-independent number for all modes, which holds well for simple metals and ceramics and fails for anisotropic and soft-mode materials, where different modes have different (even negative) $\gamma$.

**Worked example — Expansion of copper and tungsten from Grüneisen.** For copper, $\gamma\approx2.0$, $C_v\approx24.4$ J mol⁻¹ K⁻¹ at 300 K, $K=140$ GPa and $V_m=7.11\times10^{-6}$ m³/mol:

$$
\alpha=\frac{\gamma C_v}{3KV_m}=\frac{2.0\times24.4}{3\times1.40\times10^{11}\times7.11\times10^{-6}}=1.63\times10^{-5}\ \mathrm{K^{-1}}
$$

against a measured 16.5 ppm/K. For tungsten ($\gamma\approx1.6$, $C_v\approx24.3$, $K=310$ GPa, $V_m=9.55\times10^{-6}$ m³/mol): $\alpha=1.6\times24.3/(3\times3.10\times10^{11}\times9.55\times10^{-6})=4.4$ ppm/K, against a measured 4.5 ppm/K. The factor of nearly four between them comes almost entirely from tungsten's higher bulk modulus. Hence tungsten, molybdenum and Kovar-type alloys seal to glasses and ceramics, while aluminium mismatches nearly everything bonded to it.

<!-- FIGURE 24.2 | figures/ch24/fig-24-2-anharmonic-potential.png | schematic | The anharmonic interatomic potential and the origin of thermal expansion. | Content: x-axis interatomic separation r / r_0 from 0.8 to 1.6; y-axis potential energy U (arbitrary units, negative well). Morse-type asymmetric potential well with minimum at r/r_0 = 1, steep on the left, shallow on the right; dashed harmonic parabola fitted at the bottom for comparison. Horizontal lines at increasing energies labelled T_1 < T_2 < T_3 spanning the well between turning points; their midpoints (dots) moving to larger r with increasing T, joined by a line labelled "mean separation increases: thermal expansion". For the parabola the midpoints stay at r_0 (label "harmonic: no expansion"). Inset bar chart of α (ppm/K): diamond 1.0, Invar 1.2, fused silica 0.5, W 4.5, SiC 4.0, Al2O3 8, steel 12, Cu 16.5, Al 23, Pb 29, PMMA 70, PE 150. -->

**Table 24.2 — Linear thermal expansion coefficients near room temperature (typical values).**

| Material | $\alpha$ (ppm/K) | Note |
|---|---|---|
| β-eucryptite / LAS glass-ceramic (Zerodur, Ceran) | −0.1 to +0.1 | Near-zero by design: negative-expansion crystals in a glass |
| Fused silica | 0.5 | Open tetrahedral network |
| Invar (Fe–36Ni) | 1.2 | Magnetovolume effect cancels lattice expansion below $T_C$ |
| Diamond | 1.0 | |
| Silicon | 2.6 | |
| Borosilicate glass (Pyrex type) | 3.3 | |
| Silicon nitride | 3.0–3.3 | |
| Silicon carbide | 4.0–4.5 | |
| Tungsten | 4.5 | |
| Kovar (Fe–29Ni–17Co) | 5.5 | Matches borosilicate glass and alumina for seals |
| Alumina | 7–8 | |
| Soda-lime glass | 9 | |
| Yttria-stabilized zirconia | 10–11 | Close to superalloys: why it works as a coating |
| Ti-6Al-4V | 8.6–9 | |
| Carbon steel; concrete | 11–13; 10–12 | Similar values make reinforced concrete possible |
| Austenitic stainless steel | 16–17 | |
| Copper; Ni-base superalloy | 16.5; 13–16 | |
| Aluminium | 23 | |
| Wood, along / across grain | 3–5 / 30–60 | Plus much larger moisture swelling |
| Epoxy; PMMA | 55–70; 70 | |
| HDPE; silicone rubber | 100–200; 250–300 | |

### Low and negative expansion

Two coincidences in Table 24.2 hold up whole industries. Steel and concrete have nearly equal expansion coefficients, so reinforced concrete does not tear itself apart in daily temperature cycles (Chapter 18). Yttria-stabilized zirconia expands nearly as much as nickel superalloys, which is what allows a ceramic coating to survive on a metal blade (Section 24.6).

Some materials expand little or contract on heating by design. In **Invar**, the magnetic moment of the iron–nickel alloy shrinks with rising temperature and with it a magnetovolume expansion, cancelling the normal lattice expansion up to the Curie temperature (Chapter 27); Invar is used for precision instruments, shadow masks, LNG tank membranes and composite-curing tools. **Negative-thermal-expansion** crystals such as ZrW₂O₈ and β-eucryptite (LiAlSiO₄) contract because transverse vibrations of corner-linked polyhedra pull their linking atoms closer, like a rope that shortens as it is shaken sideways. Dispersed in a glass, β-eucryptite or β-quartz solid solutions give the near-zero-expansion **glass-ceramics** of cooktops and telescope mirrors (Chapter 17), which survive thermal shocks no ordinary glass would.

---

## 24.3 Thermal conductivity: phonon and electron contributions

### Fourier's law

Heat flows from hot to cold at a rate proportional to the temperature gradient:

$$
\mathbf q=-k\,\nabla T
$$

where $\mathbf q$ is the heat flux (W/m²) and $k$ the **thermal conductivity** (W m⁻¹ K⁻¹). In anisotropic materials $k$ is a second-rank tensor (Chapter 4): graphite, wood, fibre composites and drawn polymers conduct far better along one direction than across it.

> **Status of the principle: Fourier's law**
> *Empirical.* A linear constitutive law confirmed over a huge range of materials and conditions; it holds when temperature varies slowly over the mean free path of the heat carriers, and fails for nanometre films, very short pulses and ballistic transport, where heat carriers cross the structure without scattering.

Thermal conductivity spans about five orders of magnitude among engineering materials, from 0.02 W m⁻¹ K⁻¹ for insulating foams to over 2,000 for diamond (Table 24.3). Two carriers are responsible: phonons in all solids, and electrons in metals.

### Phonon conduction

Phonon wave packets travel at about the speed of sound and carry the vibrational energy they hold. Treating them as a gas, kinetic theory gives

$$
k_{\mathrm{ph}}=\tfrac13\,C\,v\,\ell
$$

where $C$ is the heat capacity per unit volume, $v$ an average sound velocity and $\ell$ the phonon mean free path.

> **Status of the principle: Kinetic formula for phonon conductivity**
> *Approximate.* Replaces a spectrum of phonons, each with its own velocity and mean free path, by single averages; it explains trends among materials and with temperature, but the effective $\ell$ it yields is a weighted average over mean free paths that, in a single crystal, span from nanometres to micrometres.

For alumina ($C=3.5\times10^6$ J m⁻³ K⁻¹, $v\approx7,000$ m/s, $k=35$ W m⁻¹ K⁻¹), the formula gives $\ell=3k/(Cv)\approx4$ nm; for diamond ($k=2,200$, $v\approx12,000$ m/s, $C=1.79\times10^6$) about 300 nm. A good phonon conductor needs:

- **Fast phonons**, from stiff bonds and light atoms — the same factors that give high $\theta_D$.
- **A simple crystal structure** with few atoms per primitive cell. Complex cells have many optical branches whose phonons are slow and scatter strongly. AlN (4 atoms per primitive cell) conducts about 175 W m⁻¹ K⁻¹ as a ceramic; alumina (10) about 30–35, despite similar stiffness.
- **Long mean free paths**, limited by four kinds of scattering:
  - **Phonon–phonon (Umklapp) scattering**, which grows with temperature as more phonons are excited. Above roughly $\theta_D/3$, $k\propto1/T$: dense ceramics conduct worse when hot.
  - **Point defects** — impurities, solutes, vacancies and even isotopes — which scatter short-wavelength phonons strongly (Rayleigh-like, $\propto\omega^4$). Oxygen dissolved in AlN cuts its conductivity from a theoretical 320 to 70–180 W m⁻¹ K⁻¹; isotopically pure ¹²C diamond conducts about 50 % better than natural diamond.
  - **Grain boundaries and pores**, important in fine-grained ceramics, thin films and coatings.
  - **Disorder.** In glasses and amorphous polymers $\ell$ is only a few interatomic spacings, and $k$ is 0.1–1.5 W m⁻¹ K⁻¹ regardless of bond strength.

The best phonon conductors are therefore simple, stiff, light-atom crystals of high purity: diamond, cubic BN, BAs, SiC, BeO, AlN. Polymers are poor conductors, but orientation helps: ultra-high-molecular-weight polyethylene fibre conducts 20–100 W m⁻¹ K⁻¹ along the chain axis, against 0.4–0.5 for bulk HDPE, because heat then travels along covalent backbones rather than across van der Waals contacts.

### Electronic conduction and the Wiedemann–Franz law

In metals, free electrons carry heat as well as charge, and they are much faster than phonons (Fermi velocities about $10^6$ m/s). Electrons that carry charge and heat are scattered by the same phonons and defects, so the two conductivities are linked by the **Wiedemann–Franz law**:

$$
\frac{k_e}{\sigma T}=L_0=\frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2=2.44\times10^{-8}\ \mathrm{W\,\Omega\,K^{-2}}
$$

where $\sigma$ is the electrical conductivity and $L_0$ the **Lorenz number**.

> **Status of the principle: Wiedemann–Franz law**
> *Derived.* Follows from free-electron theory when electrons are scattered elastically (the same scattering for charge and heat); it holds well near room temperature and above and at very low temperatures, and fails at intermediate temperatures (roughly $0.1$–$0.5\,\theta_D$) where inelastic phonon scattering degrades heat current more than charge current.

**Worked example — How much of a metal's conductivity is electronic?** At 300 K, for copper ($\rho_e=1.68\times10^{-8}$ Ω m): $k_e=L_0T/\rho_e=2.44\times10^{-8}\times300/1.68\times10^{-8}=436$ W m⁻¹ K⁻¹, against a measured 401. For aluminium ($\rho_e=2.65\times10^{-8}$ Ω m): 276 against 237. The law overshoots slightly because the real Lorenz number of these metals at room temperature is about 2.2–2.3 × 10⁻⁸, but it confirms that heat in pure metals is carried almost entirely by electrons.

Now an alloy. Austenitic stainless steel 304 has $\rho_e=72\times10^{-8}$ Ω m — 43 times copper's, because the disordered solid solution scatters electrons (Matthiessen's rule, Chapter 25). Wiedemann–Franz gives $k_e=2.44\times10^{-8}\times300/72\times10^{-8}=10.2$ W m⁻¹ K⁻¹; the measured total is 16.2, so phonons contribute about 6 W m⁻¹ K⁻¹. For Ti-6Al-4V ($\rho_e=178\times10^{-8}$ Ω m), $k_e=4.1$ against a total of 6.7. Alloying collapses the electronic contribution and leaves phonon and electron terms comparable. Hence a stainless-steel pan needs a copper or aluminium base to spread heat, titanium is hard to machine because heat stays at the cutting edge, and high-conductivity copper alloys (Chapter 16) are strengthened by precipitates rather than solutes.

### Temperature dependence

Figure 24.3 summarizes how $k$ varies with temperature. In dielectric crystals, $k$ rises as $T^3$ at very low temperature (following heat capacity, with mean free path limited by sample size), peaks at roughly $\theta_D/20$, and then falls as $1/T$ as Umklapp scattering takes over. In pure metals $k$ is nearly flat from room temperature upward, because the resistivity rising as $\rho_e\propto T$ is offset by the factor $T$ in $k_e=L_0T/\rho_e$. In alloys, which are dominated by temperature-independent solute scattering, $k$ rises gently with temperature. In glasses, polymers and other amorphous solids it also rises slowly, then saturates. Porous insulators gain a radiative component that grows as $T^3$ (Section 24.6).

<!-- FIGURE 24.3 | figures/ch24/fig-24-3-conductivity-vs-temperature.png | plot | Thermal conductivity versus temperature for representative crystals, metals, alloys, glasses, polymers and insulators. | Content: x-axis temperature 200–1,300 K (linear); y-axis thermal conductivity 0.02–3,000 W/(m K) on a log scale. Curves (approximate): diamond (2,200 at 300 K falling to ~800 at 800 K); Cu (401, nearly flat, ~350 at 1,200 K); Al (237, ~220 at 800 K, ends at melting 933 K); SiC (~120 sintered at 300 K, ~50 at 1,200 K); AlN ceramic (175 at 300 K, ~80 at 800 K); Al2O3 (35 at 300 K, ~12 at 800 K, ~7 at 1,300 K); carbon steel (50 at 300 K falling to ~30 at 1,000 K); 304 stainless (16 at 300 K rising to ~25 at 1,000 K); Ti-6Al-4V (6.7 rising to ~15 at 900 K); dense YSZ (~2.5, nearly flat); plasma-sprayed YSZ coating (~1.0, flat); fused silica (1.4 rising to ~2); concrete (~1.7); HDPE (0.45, to 400 K only); mineral wool (0.035 at 300 K rising to ~0.15 at 900 K, radiation). Annotate "Umklapp: k ∝ 1/T" on crystalline ceramics, "electrons: nearly flat" on pure metals, "solute scattering: rising" on alloys, "disorder-limited" on glasses and polymers. -->

**Table 24.3 — Thermal conductivity, diffusivity and effusivity near room temperature (typical values).**

| Material | $k$ (W m⁻¹ K⁻¹) | Diffusivity $a$ (mm²/s) | Effusivity $e$ (J m⁻² K⁻¹ s⁻¹ᐟ²) |
|---|---|---|---|
| Diamond (CVD, thermal grade) | 1,000–2,200 | 560–1,200 | ~40,000–60,000 |
| Copper | 401 | 116 | 37,200 |
| Aluminium | 237 | 98 | 24,000 |
| Aluminium nitride | 140–180 | 60–90 | ~16,000 |
| Silicon carbide (sintered) | 80–150 | 40–70 | ~15,000 |
| Silicon | 150 | 88 | 15,700 |
| Carbon steel | 45–55 | 12–15 | ~13,700 |
| Alumina (99 %) | 30–35 | ~10 | 11,000 |
| Stainless steel 304 | 16.2 | 4.0 | 8,000 |
| Ti-6Al-4V | 6.7 | 2.9 | 4,000 |
| Dense YSZ | 2–2.5 | ~0.7 | ~2,400 |
| Concrete | 1.4–2.0 | ~0.8 | ~1,900 |
| Soda-lime glass | 1.0 | 0.48 | 1,450 |
| Polypropylene; polycarbonate | 0.20 | 0.12–0.13 | 550–590 |
| Wood (softwood, across grain) | 0.10–0.15 | ~0.14 | ~320 |
| Mineral wool; EPS foam | 0.032–0.040 | — | — |
| PIR/PUR foam; silica aerogel | 0.020–0.025; 0.013–0.018 | — | — |
| Still air | 0.026 | 22 | 6 |

---

## 24.4 Thermal diffusivity and transient heat flow

### The heat equation and diffusivity

When temperature changes with time, conductivity alone does not decide how fast. Combining Fourier's law with conservation of energy gives the **heat equation**:

$$
\frac{\partial T}{\partial t}=a\nabla^2T,\qquad a=\frac{k}{\rho c_p}
$$

The **thermal diffusivity** $a$ (m²/s) measures how quickly a temperature disturbance spreads: high conductivity spreads heat, high volumetric heat capacity soaks it up. The heat equation is mathematically identical to Fick's second law (Chapter 8), and all the solutions developed there — error functions for a suddenly heated surface, separation of variables for slabs — carry over with $D$ replaced by $a$.

> **Status of the principle: Heat equation**
> *Derived.* Follows from energy conservation and Fourier's law with constant properties; for large temperature excursions $k$ and $c_p$ vary with $T$ and the equation becomes non-linear, and latent heat, radiation and convection must be added as source or boundary terms.

### The diffusion length and the time scale

The most useful consequence is a scaling law. A temperature change at a surface penetrates a distance

$$
L\approx\sqrt{a\,t}
$$

in time $t$; equivalently, a body of characteristic half-thickness $L$ comes to thermal equilibrium in a time of order $L^2/a$. Doubling the thickness quadruples the time. Diffusivities range from about 100 mm²/s for copper and aluminium through 13 for steel, 1 for concrete and glass, to 0.1 for polymers and wood (Table 24.3).

When a body exchanges heat with a fluid, the ratio of internal to surface resistance — the **Biot number** $\mathrm{Bi}=hL/k$, with $h$ the heat-transfer coefficient — decides whether its interior lags behind its surface. For $\mathrm{Bi}\ll0.1$ the body heats uniformly (lumped behaviour); for $\mathrm{Bi}\gg1$ steep internal gradients develop, which is when thermal stresses become serious (Section 24.5).

**Worked example — Three transient problems from three industries.**

*Quenching steel.* A carbon-steel bar ($k=50$ W m⁻¹ K⁻¹, $\rho=7,850$ kg/m³, $c_p=475$ J kg⁻¹ K⁻¹) has $a=50/(7,850\times475)=1.34\times10^{-5}$ m²/s. Quenched into agitated water ($h\approx5,000$ W m⁻² K⁻¹) its Biot number for a 25 mm half-thickness is $5,000\times0.025/50=2.5$: the surface cools much faster than the core. The time scale for the core is $L^2/a=0.025^2/1.34\times10^{-5}=47$ s; for a 50 mm half-thickness, 186 s. Since the cooling rate needed to form martensite must be reached within a few seconds in the critical range (Chapter 15), thick sections of plain-carbon steel cannot harden through — the origin of hardenability and the Jominy test.

*Injection moulding.* A polypropylene wall 2 mm thick ($a\approx1.2\times10^{-7}$ m²/s) moulded at 230 °C into a 40 °C mould must cool to an ejection temperature of 100 °C at its centre. The standard slab solution gives a cooling time

$$
t_c=\frac{s^2}{\pi^2a}\ln\!\left(\frac4\pi\,\frac{T_{\mathrm{melt}}-T_{\mathrm{mould}}}{T_{\mathrm{eject}}-T_{\mathrm{mould}}}\right)=\frac{(0.002)^2}{\pi^2\times1.16\times10^{-7}}\ln\!\left(\frac4\pi\times\frac{190}{60}\right)=4.9\ \mathrm{s}
$$

Cooling is typically more than half the cycle time, and it scales with the square of wall thickness: a 4 mm wall takes 20 s. This is why plastic parts are designed with thin, uniform walls and ribs rather than thick sections (Chapter 21).

*Mass concrete.* A foundation raft 2 m thick ($a\approx8\times10^{-7}$ m²/s) has a half-thickness of 1 m, giving $L^2/a\approx1.2\times10^6$ s, or about two weeks. Cement hydration releases heat over the first days far faster than it can escape, so the core may reach 60–70 °C while the surface cools. The resulting gradients crack the concrete unless the pour is cooled by embedded pipes, made with low-heat cement, or insulated to reduce the gradient (Chapter 18).

### Effusivity and touch temperature

When two bodies at different temperatures are suddenly brought into contact, the interface temperature is set not by conductivity or diffusivity but by the **thermal effusivity** $e=\sqrt{k\rho c_p}$. For two semi-infinite bodies,

$$
T_{\mathrm{contact}}=\frac{e_1T_1+e_2T_2}{e_1+e_2}
$$

Skin has $e\approx1,500$ J m⁻² K⁻¹ s⁻¹ᐟ². Touching steel at 0 °C ($e\approx13,700$) with skin at 33 °C gives a contact temperature of about 3 °C: steel feels icy. Touching wood at 0 °C ($e\approx320$) gives about 27 °C: wood feels warm. The same quantity explains why hot-surface safety limits are lower for metals than for plastics.


Diffusivity is measured directly by the **laser-flash** method, in which the front of a thin disc is heated by a short pulse and the rise of the rear-face temperature is timed; conductivity then follows from $k=a\rho c_p$ (Chapter 42).

---

## 24.5 Thermal stresses and thermal shock

### Constrained expansion

A free body heated uniformly expands without stress. Stress arises when expansion is **constrained** — by external supports, by bonded neighbours with a different expansion coefficient, or by the cooler parts of the same body. Three cases cover most practice.

**Fully constrained bar.** A bar held between rigid supports and heated by $\Delta T$ develops

$$
\sigma=-E\alpha\Delta T
$$

(compressive on heating). Continuously welded rail ($E=210$ GPa, $\alpha=12$ ppm/K) laid at a stress-free temperature of 20 °C and heated by the sun to 60 °C develops $210{,}000\times12\times10^{-6}\times40=101$ MPa of compression. That is far below the yield strength, but it represents a force of about 0.75 MN in a 60 kg/m rail, enough to buckle the track laterally if ballast resistance is low. Rail is therefore pre-tensioned at installation to a neutral temperature high in the local range.

**Biaxially constrained layer.** A thin film or coating bonded to a thick substrate, with mismatch $\Delta\alpha=\alpha_{\mathrm{film}}-\alpha_{\mathrm{sub}}$, cannot change its in-plane dimensions independently. A temperature change $\Delta T$ produces an equibiaxial stress

$$
\sigma_{\mathrm{film}}=-\frac{E_f}{1-\nu_f}\,\Delta\alpha\,\Delta T
$$

A ceramic coating with lower expansion than its metal substrate is put into compression on cooling from deposition — usually beneficial — and into tension on heating. The factor $1/(1-\nu)$ makes biaxial stresses 25–40 % larger than uniaxial ones. It governs glazes, enamels, thermal barrier coatings (Section 24.6), thin films (Chapter 41) and laminate residual stresses (Chapter 23).

> **Status of the principle: Thermal mismatch stress**
> *Derived.* Follows from linear elasticity for a thin layer perfectly bonded to a thick, rigid substrate with temperature-independent properties; it overestimates stress where the layer creeps, yields, cracks or relaxes, and must be integrated over temperature when $\alpha$ or $E$ vary.

**Temperature gradients.** A body with a non-uniform temperature constrains itself: hotter regions want to expand and are held back by cooler ones. For a plate whose surface is suddenly cooled, the surface wants to shrink but is held at the dimensions of the still-hot interior; the surface goes into **tension** and the interior into compression. For the limiting case of a sudden, infinitely fast surface temperature change $\Delta T$, the surface stress is

$$
\sigma_{\max}=\frac{E\alpha\Delta T}{1-\nu}
$$

Heating the surface suddenly reverses the signs: the surface goes into compression. Since brittle materials are far weaker in tension than in compression, sudden cooling is more dangerous than sudden heating — which is why the glass dish that cracked was cold and wet on the outside while hot water hit the inside, putting the cold outer surface in tension.

### Thermal shock resistance

**Thermal shock** is fracture caused by such a transient. Setting the surface stress equal to the fracture strength $\sigma_f$ gives the critical quench temperature difference for a brittle material, the first **thermal shock resistance parameter**:

$$
R=\Delta T_c=\frac{\sigma_f(1-\nu)}{E\alpha}
$$

$R$ applies when heat transfer is very fast (high Biot number). When heat transfer is slower, conduction inside the body reduces the gradient, and the relevant parameter is $R'=Rk$ (W/m), which rewards high conductivity. For moderate Biot numbers the stress is reduced by a factor $f(\mathrm{Bi})$ that can be approximated as $1/(1.5+3.25/\mathrm{Bi}-0.5e^{-16/\mathrm{Bi}})$ for a plate (Manson), so the critical $\Delta T$ is larger than $R$ by up to an order of magnitude in gentle quenches.

> **Status of the principle: Thermal shock parameters $R$ and $R'$**
> *Approximate.* Derived for a linear-elastic, isotropic body with temperature-independent properties failing when the peak surface stress reaches a single strength; they rank brittle materials reliably but ignore the statistical (Weibull) nature of strength, the time-dependence of the stress, and the material's resistance to crack growth after initiation.

A different question is how much damage a material suffers once cracks start. Hasselman's **damage resistance** parameters, such as $R''''=EG_c/[\sigma_f^2(1-\nu)]$, reward low strength and high toughness: they favour materials in which initiated cracks arrest rather than run. This is the logic of **refractories** (Chapter 17), which are deliberately porous and microcracked so that they lose some strength on the first heat-up but then survive thousands of thermal cycles without crumbling.

**Worked example — Which ceramic survives a quench?** Table 24.4 evaluates $R$ and $R'$ from typical properties.

**Table 24.4 — Thermal shock parameters of brittle materials (typical properties).**

| Material | $\sigma_f$ (MPa) | $E$ (GPa) | $\alpha$ (ppm/K) | $\nu$ | $k$ (W m⁻¹ K⁻¹) | $R=\Delta T_c$ (K) | $R'$ (W/m) |
|---|---|---|---|---|---|---|---|
| Soda-lime glass | 50 | 70 | 9.0 | 0.22 | 1.0 | 62 | 62 |
| Borosilicate glass | 50 | 64 | 3.3 | 0.20 | 1.1 | 189 | 208 |
| Fused silica | 50 | 72 | 0.55 | 0.17 | 1.4 | 1,050 | 1,470 |
| Alumina (96–99 %) | 350 | 380 | 8.0 | 0.22 | 30 | 90 | 2,700 |
| Zirconia (3Y-TZP) | 1,000 | 205 | 10.5 | 0.30 | 2.5 | 325 | 810 |
| Silicon carbide (sintered) | 450 | 410 | 4.2 | 0.19 | 120 | 212 | 25,400 |
| Silicon nitride | 800 | 310 | 3.2 | 0.27 | 25 | 589 | 14,700 |

For soda-lime glass: $R=50\times(1-0.22)/(70{,}000\times9\times10^{-6})=39/0.63=62$ K. Borosilicate, with a third of the expansion, survives about three times the temperature jump, 189 K — the difference between the shattered dish and the surviving beaker. Fused silica, with $\alpha=0.55$ ppm/K, survives being plunged red-hot into water.

Among technical ceramics, silicon nitride combines high strength with low expansion and survives a severe quench of nearly 600 K: it is the material of ceramic turbocharger rotors, bearing balls and molten-aluminium handling parts. Alumina, with twice the expansion and modest strength, survives only about 90 K and cracks if splashed with cold water when hot. Silicon carbide's lower $R$ (212 K) is offset in slower transients by its high conductivity, giving it the highest $R'$ — the reason SiC is used for kiln furniture, heat-exchanger tubes and diesel particulate filters, which must survive repeated soot burn-off. Toughened zirconia has a high $R$ but low conductivity, so it survives sharp quenches better than gradual severe heating.

<!-- FIGURE 24.4 | figures/ch24/fig-24-4-thermal-shock-ranking.png | plot | Thermal shock resistance of brittle materials: critical quench temperature difference R and the conductivity-weighted parameter R′. | Content: horizontal bar chart (log x-axis 30–3,000 K) of R = ΔT_c: soda-lime glass 62, alumina 90, borosilicate 189, SiC 212, 3Y-TZP 325, Si3N4 589, fused silica 1,050; second panel bar chart (log x-axis 30–30,000 W/m) of R′ = R k: soda-lime 62, borosilicate 208, 3Y-TZP 810, fused silica 1,470, alumina 2,700, Si3N4 14,700, SiC 25,400. Small inset: schematic of surface tensile stress versus time after a quench for Bi = 0.5, 2 and ∞, normalized by Eα∆T/(1−ν), peaking at about 0.13, 0.32 and 1.0. Annotate "rapid quench → R governs; slow heat transfer → R′ governs". -->

### Thermal shock and cycling in metals

Metals rarely shatter in one thermal transient, but they fail by **thermal fatigue** under repeated transients: brake discs crazed with radial cracks, die-casting dies with a network of "heat checks", the leading edges of turbine blades, and the cylinder heads of engines. Each heat-up drives the hot surface into compressive yield; each cool-down reverses it into tension; the plastic strain range per cycle drives low-cycle fatigue (Coffin–Manson, Chapter 14). Resistance rewards high conductivity, low expansion, and high hot strength and ductility — the combination sought in H13 hot-work tool steel and in grey cast-iron brake discs. The thermal-cycling fatigue of solder joints in electronics, a close relative driven by expansion mismatch rather than gradients, is treated in the Materials Core (EEE) book.

---

## 24.6 Thermal barrier coatings and insulation

### Thermal barrier coatings

The gas entering the high-pressure turbine of a modern jet engine is at 1,500–1,700 °C; the nickel-base superalloy blades melt at about 1,300–1,350 °C and lose strength rapidly above 1,100 °C. Two technologies close the gap: internal air cooling through serpentine passages and film-cooling holes, and a **thermal barrier coating** (TBC) on the outside (Chapter 33). The TBC is a multilayer system, each layer chosen for a different property (Figure 24.5):

- **Ceramic top coat**, 100–500 μm of zirconia stabilized with 7–8 wt% Y₂O₃ (7YSZ). YSZ combines low intrinsic conductivity (2–2.5 W m⁻¹ K⁻¹ dense, because oxygen vacancies and Y solutes scatter phonons), an expansion coefficient (10–11 ppm/K) close to the superalloy's, a metastable tetragonal (t′) phase stable to about 1,200 °C, and high toughness for a ceramic. Porosity lowers the conductivity to 0.8–1.2 W m⁻¹ K⁻¹ in plasma-sprayed coatings (splat boundaries across the heat flow) or 1.5–1.9 in electron-beam PVD coatings, whose columns give **strain tolerance**.
- **Thermally grown oxide** (TGO), a thin layer of α-Al₂O₃ that forms on the bond coat in service and protects it from further oxidation. It thickens parabolically (Chapter 34); when it reaches 5–10 μm, the mismatch stresses within and around it typically cause the top coat to spall.
- **Bond coat**, 50–150 μm of MCrAlY (M = Ni, Co) or platinum-modified nickel aluminide, an aluminium reservoir that grows the protective alumina scale.
- **Superalloy substrate**, internally cooled.

**Worked example — How much does a TBC buy?** A blade wall carries a heat flux of 0.8 MW/m². In steady state the temperature drop across each layer is $\Delta T=q\,t/k$:

- YSZ top coat, 250 μm, $k=1.0$ W m⁻¹ K⁻¹: $0.8\times10^6\times2.5\times10^{-4}/1.0=200$ K.
- Bond coat, 100 μm, $k\approx10$: 8 K.
- Superalloy wall, 1.5 mm, $k\approx25$ W m⁻¹ K⁻¹ (at temperature): 48 K.

A quarter-millimetre of ceramic produces four times the temperature drop of a wall six times thicker. That 200 K either lowers the metal temperature — which, by the Larson–Miller relation (Chapter 14), multiplies creep life many times over — or allows a hotter, more efficient cycle with less cooling air. The coating's failure modes all come from thermal properties: CTE mismatch stress on every flight cycle, sintering of the porous top coat (which raises $k$ and stiffness), TGO growth, and infiltration by molten calcium–magnesium–aluminosilicate (CMAS) sand deposits, which fill the pores and destroy strain tolerance. Lower-conductivity successors such as gadolinium zirconate pyrochlores are under active development.

> **Status of the principle: One-dimensional thermal resistance of a layer stack**
> *Approximate.* Each layer is treated as a uniform slab carrying the same heat flux in steady state ($\Delta T=qt/k$, resistances in series); valid for thin flat layers with uniform properties, but it ignores lateral spreading, contact resistances between layers, radiation through translucent ceramics and the temperature dependence of $k$.

<!-- FIGURE 24.5 | figures/ch24/fig-24-5-tbc-temperature-profile.png | schematic | A thermal barrier coating system on a cooled turbine blade wall and the temperature profile through it. | Content: left: cross-section, to approximate scale, from hot gas (top) to cooling air (bottom): hot gas ~1,500 °C with boundary layer; YSZ top coat 250 μm (porous columnar or splat structure with vertical cracks drawn); TGO ~3–5 μm (thin dark line, labelled α-Al2O3); bond coat 100 μm (MCrAlY or Pt-aluminide); superalloy wall 1.5 mm; internal cooling passage with air ~650 °C. Right: temperature versus depth plot aligned with the layers: surface of YSZ ~1,250 °C dropping linearly by 200 K across the top coat to ~1,050 °C, 8 K across the bond coat, 48 K across the metal wall to ~1,000 °C at the cooled face; gas-side and coolant-side film drops shown as steep curves. Annotate heat flux q = 0.8 MW/m², and "200 K across 0.25 mm of YSZ versus 48 K across 1.5 mm of metal". -->

### Thermal insulation

Insulating materials exploit still air (0.026 W m⁻¹ K⁻¹): the art is to keep the gas still and block radiation with as little solid as possible. Heat flows through a porous insulator by four paths in parallel: conduction through the solid skeleton, conduction through the gas, convection within the pores (negligible below pore sizes of a few millimetres), and radiation across the pores. Thus:

- **Fibrous and cellular insulators** — mineral wool and glass wool (0.032–0.040 W m⁻¹ K⁻¹), expanded and extruded polystyrene (0.030–0.038), polyurethane and polyisocyanurate foams (0.020–0.025, thanks to low-conductivity blowing gases in closed cells) — dominate building and appliance insulation. In a building wall, 100 mm of mineral wool gives a thermal resistance of $0.1/0.035=2.9$ m² K/W, a heat flow of 0.35 W per m² per kelvin of indoor–outdoor difference.
- **Aerogels** (silica, 90–99 % porosity, 0.013–0.018 W m⁻¹ K⁻¹) have pores of 10–100 nm, smaller than the mean free path of air molecules (about 70 nm), so gas conduction is suppressed (the Knudsen effect). They insulate pipelines and separate cells in battery modules.
- **Vacuum insulation panels** (0.004–0.008) and **multilayer insulation** — tens of reflective aluminized polymer films in vacuum, with effective conductivity below 10⁻⁴ W m⁻¹ K⁻¹ — remove gas conduction entirely and are used in refrigerators, LNG and liquid-hydrogen tanks, and spacecraft.
- **High-temperature insulation** — ceramic-fibre blankets, insulating firebrick, microporous silica panels — must also block radiation, which grows as $T^3$ and dominates above about 500 °C. Opacifiers (TiO₂, SiC, carbon) are added to scatter and absorb infrared. The 90 %-porous silica tiles of the Space Shuttle had such low diffusivity that a tile glowing on its face could be held by its edges.

---

## 24.7 Materials for thermal management

### The problem and the indices

Thermal management means moving heat deliberately from where it is generated to where it can be rejected, without overheating the source or overstressing the joints. It is now a limiting technology in power electronics, data centres, LED lighting, electric-vehicle batteries and motors, avionics, satellites and laser systems. The material requirements depend on the regime:

- **Steady-state heat spreading and conduction** reward high $k$. For weight-critical applications (aircraft, spacecraft, portable devices), the index is $k/\rho$.
- **Absorbing transient pulses** rewards high $\rho c_p$ (or latent heat) close to the source, and fast spreading rewards high diffusivity.
- **Bonding to a low-expansion device** (silicon, GaN, SiC dies, ceramic substrates, laser diodes) requires a CTE close to the device's to avoid thermomechanical fatigue. The combined index is high $k$ with low $\alpha$, or equivalently a low **thermal distortion parameter** $\alpha/k$ — the same index used to choose materials for precision instruments and mirrors that must not distort in non-uniform temperature fields.

Figure 24.6 plots conductivity against expansion for the candidate materials.

<!-- FIGURE 24.6 | figures/ch24/fig-24-6-k-vs-cte-map.png | map | Thermal conductivity versus thermal expansion coefficient for thermal-management materials, with the CTE window of semiconductor devices. | Content: x-axis CTE 0–25 ppm/K (linear); y-axis thermal conductivity 1–2,500 W/(m K) (log). Points or ellipses: diamond (1.0, 1,000–2,200); CVD diamond/Cu composite (6–7, 500–700); Cu (17, 401); Al (23, 237); Al-6061 (23.6, 167); AlSiC 63 % (7–8, 170–200); Cu–W 10–20 % Cu (6–8, 180–200); Cu–Mo–Cu laminate (6–8, 200–300); Kovar (5.5, 17); Invar (1.2, 10); AlN (4.6, 140–180); BeO (7.5, 250–280); SiC (4.2, 80–150); Si3N4 (3.0, 60–90 high-k grade); Al2O3 (7–8, 25–35); pyrolytic graphite in-plane (−1, 1,500–1,700) with an arrow to through-plane (25, 5–10); Si (2.6, 150); GaN (5.6, 200); stainless steel (17, 16); Ti-6Al-4V (9, 7); epoxy (60, 0.2 — off scale, arrow). Shaded vertical band 2.5–7 ppm/K labelled "Si, SiC, GaN, GaAs dies and ceramic substrates". Diagonal guide lines of constant α/k (thermal distortion) with "better" arrow towards top-left. -->

### The material families

**Metals.** Copper (401 W m⁻¹ K⁻¹) is the default heat spreader, cold plate and heat-pipe envelope; aluminium (237 for pure, 150–200 for alloys) is the default heat sink, at a third of copper's density and a better $k/\rho$. Both expand much more than semiconductors and ceramics.

**Ceramics.** Electrically insulating substrates that conduct heat — AlN (140–180), BeO (250–280, but toxic as dust), high-conductivity Si₃N₄ (60–90, much tougher), SiC and alumina (25–35, the cheap default) — carry power devices and LEDs while isolating them electrically. Hexagonal boron nitride, with a basal-plane conductivity of several hundred W m⁻¹ K⁻¹, is the filler of choice for thermally conductive polymers.

**Carbon.** Natural and synthetic graphite sheets (in-plane 400–1,700, through-plane 5–10 W m⁻¹ K⁻¹) spread heat laterally in smartphones and laptops. Pitch-based carbon fibres reach 600–1,100 W m⁻¹ K⁻¹ along the fibre, enabling satellite radiators and electronics enclosures in CFRP. CVD diamond (1,000–2,200) is the ultimate heat spreader for laser diodes, RF power transistors and GaN-on-diamond devices.

**Metal-matrix composites.** Combining a conductive metal with a low-expansion phase gives intermediate CTEs at high $k$: AlSiC (Chapter 23) with 7–8 ppm/K and 170–200 W m⁻¹ K⁻¹ for power-module baseplates and avionics; Cu–W and Cu–Mo for RF packages and laser submounts; diamond-particle composites in copper or silver reaching 500–700 W m⁻¹ K⁻¹ at 6–7 ppm/K.

**Interface materials and polymers.** The weakest link in most heat paths is an interface: two machined surfaces touch at only a few percent of their area, with air gaps between. Thermal interface materials — greases, gels, phase-change pads, solders and sintered silver — fill those gaps; they are polymer matrices filled to 50–80 vol% with Al₂O₃, BN, AlN, ZnO or metal particles, raising conductivity from 0.2 to 1–10 W m⁻¹ K⁻¹. The design rules are those of particulate composites (Chapter 22): conductivity rises slowly until particles touch and percolate, and the best fillers are those with high $k$ and good packing. Thermally conductive plastics (2–20 W m⁻¹ K⁻¹ in-plane) replace die-cast aluminium in LED housings and battery-module parts.

**Heat pipes and vapour chambers** move heat by evaporation and condensation of a working fluid, giving effective conductivities of 5,000–100,000 W m⁻¹ K⁻¹; their wick structure and fluid–envelope compatibility (water–copper, ammonia–aluminium in spacecraft) are materials choices.

**Table 24.5 — Thermal management choices across engineering.**

| Application | Requirement | Typical material choice |
|---|---|---|
| Power-electronic module (EV inverter) | High $k$, electrical isolation, CTE near Si/SiC | Si₃N₄ or AlN substrate with bonded Cu; AlSiC or Cu baseplate; sintered-silver die attach |
| CPU/GPU in a data centre | Spread very high flux, then reject | Cu lid, indium or liquid-metal TIM, vapour chamber, Cu or Al fins, liquid cold plate |
| EV battery pack | Uniform cell temperature, block runaway propagation | Al cold plates, gap fillers, aerogel or mica barriers between cells |
| Satellite electronics and radiators | High $k/\rho$, low outgassing, low $\alpha/k$ | Al alloys, pitch-carbon CFRP, ammonia–Al heat pipes |
| Laser diode, RF power transistor | Very high local flux, CTE match | CVD diamond, Cu–W, Cu–diamond submounts |
| Building envelope | Minimize heat flow, control thermal bridges | Mineral wool, PIR, aerogel blankets; thermally broken aluminium frames |

> **Boundary.** The thermal resistance networks, junction-temperature budgets and thermal-cycling fatigue of electronic packages are treated in depth in the Materials Core (EEE) book; this section gives the materials logic common to all fields.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are reciprocal space and Brillouin zones defined, and why is conductivity a second-rank tensor? | Chapter 4 (reciprocal space, tensor properties) |
| How does the same diffusion mathematics govern atoms in solids? | Chapter 8 (Fick's laws and their solutions) |
| How do quenching and cooling rate control steel microstructure and hardenability? | Chapter 15 (heat treatment, Jominy test) |
| How do glass, glass-ceramics and refractories achieve their thermal properties? | Chapter 17 (ceramics and glasses, refractories) |
| How do residual thermal stresses arise in composite laminates? | Chapter 23 (thermal loads in CLT) |
| How do electrons conduct charge, and how does alloying raise resistivity? | Chapter 25 (Drude, Matthiessen, alloy resistivity) |
| How does magnetism produce Invar behaviour and magnetocaloric cooling? | Chapter 27 (magnetic materials) |
| How do thermoelectric materials convert heat into electricity? | Chapter 32 (thermoelectric materials) |
| How do superalloys, CMCs and coatings survive in turbines and hypersonic flight? | Chapter 33 (extreme environments) |
| How fast do bond coats oxidize and TBCs fail? | Chapter 34 (high-temperature oxidation), Chapter 36 (failure analysis) |
| How is thermal conductivity reduced or raised at the nanoscale? | Chapter 30 (size effects, nanomaterials) |
| How are thermal properties measured (DSC, laser flash, TMA)? | Chapter 42 (thermal analysis) |
| How are thermal-management materials selected with performance indices? | Chapter 48 (materials selection) |

**Next:** Chapter 25 turns from heat to charge — how electrons and ions conduct, how dielectrics polarize and break down, and how superconductors carry current without loss.
