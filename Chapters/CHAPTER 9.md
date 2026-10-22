# Chapter 9 — Nucleation, Growth and Solidification

*Part II · Thermodynamics and Kinetics*

An aluminium rolling mill receives a batch of direct-chill cast slabs that crack along their edges during the first hot-rolling pass. The fracture surfaces show grains several centimetres long, columnar crystals that grew inward from the mould wall like the bristles of a brush, with brittle films of the last liquid between them. The previous batch, from the same alloy and the same caster, rolled without trouble; its grains were equiaxed and about 150 µm across. The difference was a reel of thin rod that an operator had forgotten to feed into the launder: aluminium–titanium–boron master alloy, added at about 1 kg per tonne of melt. Its job is to scatter roughly a million tiny TiB₂ particles through every cubic centimetre of liquid, each one a site where a new grain can start with almost no undercooling. Without them, the few grains that nucleated at the mould wall grew unchecked across the whole slab.

The phase diagram (Chapter 7) said the alloy would solidify as α-aluminium. It did not say how many grains, of what shape, with what composition differences between their centres and edges. Those depend on **nucleation**, the birth of a new phase, and **growth**, its advance into the old one. This chapter builds both from the thermodynamics of Chapter 6 and the diffusion of Chapter 8, then applies them to solidification, the most widespread processing step in materials engineering: casting of metals, welding, crystal growth of silicon and turbine blades, additive manufacturing, glass formation and even the freezing of water in clouds.

> **Why does a liquid cool below its melting point before it freezes, and what makes some particles such good starting points for crystals?**
> **What sets the shape, size and composition variations of the crystals that grow, and how fast must a melt be cooled to avoid crystallizing at all?**

| Concept | Engineering destination |
|---|---|
| Driving force and undercooling | Supercooled water in clouds and aircraft icing; precipitation in alloys |
| Homogeneous nucleation | Limits of undercooling; why pure clean melts and droplets resist freezing |
| Heterogeneous nucleation and inoculation | Grain refiners in Al and Mg, inoculation of cast iron, cloud seeding, weld-metal toughness |
| Interface- and diffusion-controlled growth | Crystal-growth rates, precipitate growth, polymer spherulites |
| JMAK kinetics and TTT diagrams | Annealing and recrystallization schedules, polymer moulding cycles, glass formation |
| Constitutional supercooling | Planar growth of semiconductor crystals; dendritic growth in castings and welds |
| Scheil equation and zone refining | Microsegregation, freezing range, purification of silicon and germanium |
| Eutectic and peritectic solidification | Al–Si and cast-iron microstructures, permanent magnets, continuous casting |
| Rapid solidification and metallic glasses | Atomized powders, additive manufacturing, amorphous transformer cores, sporting goods |

**Roadmap.** Driving force (9.1) → homogeneous nucleation (9.2) → heterogeneous nucleation and inoculation (9.3) → growth (9.4) → overall kinetics and TTT diagrams (9.5) → solidification fronts and constitutional supercooling (9.6) → segregation (9.7) → eutectic, peritectic and casting structures (9.8) → rapid solidification and metallic glasses (9.9).

---

## 9.1 Driving force for transformation

### Undercooling a liquid

At the melting temperature $T_m$, liquid and solid have equal Gibbs energies; nothing drives either to become the other. Below $T_m$ the solid has the lower Gibbs energy. Per unit volume of solid formed, the change is

$$
\Delta G_v=\Delta H_v-T\Delta S_v
$$

where $\Delta H_v$ is the latent heat released per unit volume (taken as positive here, so $\Delta G_v$ is the magnitude of the drop). At $T_m$, $\Delta G_v=0$, so $\Delta S_v=\Delta H_v/T_m$. If $\Delta H$ and $\Delta S$ change little with temperature over the range of interest,

$$
\Delta G_v\approx\frac{\Delta H_v\,\Delta T}{T_m}
$$

where $\Delta T=T_m-T$ is the **undercooling** (or supercooling).

> **Status of the principle: Linear driving force with undercooling**
> *Approximate.* It assumes the enthalpy and entropy of fusion are independent of temperature, which holds within about 20 % for undercoolings up to roughly $0.2\,T_m$ in metals; for deeply undercooled glass-forming liquids, the heat-capacity difference between liquid and crystal must be included.

The driving force is zero at the melting point and rises linearly with undercooling. For copper ($\Delta H_v=1.88\times10^9$ J/m³, $T_m=1358$ K), 100 K of undercooling gives $\Delta G_v=1.4\times10^8$ J/m³, or about 1 kJ/mol, small compared with $RT\approx10$ kJ/mol. The transformation is driven by a modest free-energy difference, which is why it can be resisted, for a while, by the cost of creating an interface.

### Solid-state driving forces

The same idea applies to any transformation. For precipitation from a supersaturated solid solution of solute concentration $C_0$ when the equilibrium solubility is $C_e$, the driving force per unit volume of precipitate is, for a dilute ideal solution, roughly

$$
\Delta G_v\approx\frac{RT}{V_m}\ln\frac{C_0}{C_e}
$$

where $V_m$ is the molar volume of the precipitate. The driving force grows with supersaturation, and supersaturation grows as the alloy is cooled further below its solvus. For eutectoid and allotropic transformations, $\Delta G_v$ scales with undercooling below the transformation temperature, as for solidification. In each case a CALPHAD database (Chapter 7) supplies the exact value.

---

## 9.2 Homogeneous nucleation

### The energy of an embryo

Small clusters of solid-like atoms form and dissolve continually in a liquid by thermal fluctuation. Consider a spherical cluster of radius $r$ forming inside the liquid, far from any wall or particle (**homogeneous** nucleation). Its volume lowers the Gibbs energy by $\Delta G_v$ per unit volume, but its surface raises it by the solid–liquid interfacial energy $\gamma_{SL}$ per unit area:

$$
\Delta G(r)=-\frac43\pi r^3\Delta G_v+4\pi r^2\gamma_{SL}
$$

For small $r$ the surface term ($\propto r^2$) dominates and the cluster is unstable; for large $r$ the volume term ($\propto r^3$) wins. $\Delta G(r)$ passes through a maximum at the **critical radius**

$$
r^*=\frac{2\gamma_{SL}}{\Delta G_v}
$$

where the barrier is

$$
\Delta G^*=\frac{16\pi\gamma_{SL}^3}{3\,\Delta G_v^2}=\frac{16\pi\gamma_{SL}^3T_m^2}{3\,\Delta H_v^2\,\Delta T^2}
$$

Figure 9.1 plots the two terms and their sum for copper. Clusters smaller than $r^*$ (**embryos**) are more likely to shrink than grow; clusters larger than $r^*$ (**nuclei**) are more likely to grow. The critical radius is the same Gibbs–Thomson condition met in Chapter 6: a particle of radius $r^*$ is in (unstable) equilibrium with the undercooled liquid because its curvature lowers its melting point by exactly $\Delta T$.

<!-- FIGURE 9.1 | figures/ch09/fig-9-1-nucleation-barrier.png | plot | Gibbs energy of a spherical solid cluster in undercooled liquid copper versus radius, showing the surface and volume terms and the critical nucleus at two undercoolings. | Content: x-axis radius r 0–6 nm, y-axis ΔG in units of 1e−18 J from −10 to +10. Copper data: γ_SL = 0.177 J/m², ΔH_v = 1.88e9 J/m³, Tm = 1358 K. Dashed curves: surface term +4πr²γ and volume term −(4/3)πr³ΔG_v for ΔT = 100 K. Solid curve: total ΔG for ΔT = 100 K, maximum at r* = 2.56 nm, ΔG* = 4.85e−18 J (marked). Second solid curve for ΔT = 236 K with r* = 1.08 nm, ΔG* = 0.87e−18 J. Label regions "embryos shrink" (r < r*) and "nuclei grow" (r > r*). -->

### The nucleation rate

The equilibrium number of critical clusters per unit volume follows a Boltzmann distribution, $N^*=N_0\exp(-\Delta G^*/kT)$, where $N_0$ is the number of atoms per unit volume. Each critical cluster becomes a growing nucleus when one more atom joins it, at a rate set by atomic jumps across the interface (a frequency $\nu$ that contains its own activation energy for atomic transport, as in Chapter 8). The steady-state **nucleation rate** is therefore

$$
I=I_0\exp\!\left(-\frac{\Delta G^*}{kT}\right),\qquad I_0\approx N_0\,\nu\sim10^{41}\text{–}10^{42}\ \mathrm{m^{-3}\,s^{-1}}\ \text{(metal melts)}
$$

with a Zeldovich factor (about 0.01–0.1) and the temperature dependence of $\nu$ absorbed into $I_0$ for a liquid metal, whose atomic mobility is high.

> **Status of the principle: Classical nucleation theory**
> *Approximate.* It treats a cluster of a few hundred atoms as a sphere with bulk properties and a sharp interface of macroscopic energy; it predicts trends and the extreme sensitivity to undercooling correctly but can miss absolute rates by many orders of magnitude, mainly because $\gamma_{SL}$ is uncertain and enters cubed.

**Worked example — How far can liquid copper undercool?** Take for copper $\gamma_{SL}=0.177$ J/m², $\Delta H_v=1.88\times10^9$ J/m³, $T_m=1358$ K, atomic volume $1.18\times10^{-29}$ m³, and $I_0=10^{42}$ m⁻³ s⁻¹.

*At $\Delta T=100$ K.* $\Delta G_v=1.88\times10^9\times100/1358=1.38\times10^8$ J/m³, so

$$
r^*=\frac{2\times0.177}{1.38\times10^8}=2.56\ \mathrm{nm},\qquad
\Delta G^*=\frac{16\pi(0.177)^3}{3(1.38\times10^8)^2}=4.85\times10^{-18}\ \mathrm J
$$

The nucleus contains $\frac43\pi r^{*3}/\Omega\approx5900$ atoms, and $\Delta G^*/kT=4.85\times10^{-18}/(1.381\times10^{-23}\times1258)=279$. The rate is $10^{42}e^{-279}\approx10^{-79}$ m⁻³ s⁻¹: effectively zero.

*At $\Delta T=236$ K.* $r^*=1.08$ nm (about 450 atoms), $\Delta G^*=8.7\times10^{-19}$ J, $\Delta G^*/kT=56$, and $I\approx10^{42}e^{-56}\approx5\times10^{17}$ m⁻³ s⁻¹: a droplet of 1 mm³ would nucleate within a few nanoseconds.

*Onset.* Solving $I=10^{6}$ m⁻³ s⁻¹ (one nucleus per cubic centimetre per second) gives $\Delta T\approx190$ K, or $0.14\,T_m$. Changing $\Delta T$ by ±20 K around this value changes $I$ from about $10^{-2}$ to $10^{12}$ m⁻³ s⁻¹.

The theory predicts that copper must undercool by roughly 200 K before homogeneous nucleation is noticeable, and that the onset is abrupt: below the threshold nothing happens, and a few tens of kelvin further the liquid freezes instantly. Turnbull's classic experiments on small droplets, each dispersed so that most contained no impurity particle, found maximum undercoolings of about $0.18\,T_m$ for many metals (236 K for copper), consistent with this estimate. In ordinary casting, metals freeze with undercoolings of only a few kelvin. Something other than homogeneous nucleation is at work.

### Water, clouds and aircraft

Water shows the same behaviour. Pure micrometre-sized cloud droplets remain liquid down to about −38 °C, the limit of homogeneous nucleation of ice. Clouds of supercooled droplets between 0 and about −20 °C are a serious aviation hazard: when an aircraft flies through them, the droplets freeze on impact on the wing leading edges, which become heterogeneous nucleation sites. Ice-protection systems (heated leading edges, pneumatic boots, icephobic coatings) are designed around this metastability.

---

## 9.3 Heterogeneous nucleation

### The spherical cap

Nucleation almost always begins on a pre-existing surface: a mould wall, an oxide film, an inclusion, a deliberately added particle. Consider a solid nucleus forming as a spherical cap on a flat substrate, with contact (wetting) angle $\theta$ set by the balance of interfacial tensions (Young's equation, Chapter 6):

$$
\gamma_{LS'}=\gamma_{SS'}+\gamma_{SL}\cos\theta
$$

where $S'$ denotes the substrate. Repeating the calculation of Section 9.2 for the cap shows that the critical radius of curvature is unchanged, $r^*=2\gamma_{SL}/\Delta G_v$, but the cap contains fewer atoms than a full sphere, and the barrier is reduced by a geometric factor:

$$
\Delta G^*_{het}=\Delta G^*_{hom}\,f(\theta),\qquad f(\theta)=\frac{(2+\cos\theta)(1-\cos\theta)^2}{4}
$$

> **Status of the principle: Spherical-cap model of heterogeneous nucleation**
> *Approximate.* It inherits the assumptions of classical nucleation theory and assumes a flat, chemically uniform substrate with a macroscopic contact angle; real potent nucleants act through atomic-scale lattice matching, which the contact angle only parametrizes.

| Contact angle $\theta$ | $f(\theta)$ | Undercooling relative to homogeneous, $\sqrt{f}$ |
|---|---|---|
| 10° | 0.00017 | 0.013 |
| 20° | 0.0027 | 0.052 |
| 30° | 0.013 | 0.11 |
| 60° | 0.16 | 0.40 |
| 90° | 0.50 | 0.71 |
| 120° | 0.84 | 0.92 |
| 180° | 1 | 1 (no help) |

Figure 9.2 shows how steeply $f(\theta)$ falls with decreasing contact angle. Because $\Delta G^*\propto f(\theta)/\Delta T^2$, achieving the same barrier on a substrate requires an undercooling smaller by about $\sqrt{f(\theta)}$ (the third column, which neglects the smaller number of sites available on surfaces compared with atoms in the volume). With $\theta=30°$ the 190 K estimated for copper becomes about 22 K; with $\theta=20°$, about 10 K. A substrate that the solid wets well reduces the undercooling to the few kelvin observed in practice.

<!-- FIGURE 9.2 | figures/ch09/fig-9-2-heterogeneous-nucleation.png | plot | Heterogeneous nucleation: a spherical-cap nucleus on a substrate, and the barrier-reduction factor f(θ) versus contact angle. | Content: left panel schematic: flat substrate S′, liquid L above, solid cap S with radius of curvature r and contact angle θ; tension vectors γ_LS′, γ_SS′, γ_SL at the triple line. Right panel: x-axis θ 0–180°, y-axis f(θ) on log scale 1e−5 to 1, solid curve f(θ) = (2+cosθ)(1−cosθ)²/4, secondary axis √f; markers at θ = 20° (f = 0.0027), 30° (0.013), 90° (0.5); shaded region θ < 30° labelled "potent nucleants (TiB2/Al3Ti in Al, AgI for ice)". -->

### What makes a good nucleant

A low contact angle corresponds to a low interfacial energy between the nucleating solid and the substrate, which in turn requires good **lattice matching** and chemical affinity. The **planar disregistry** (lattice mismatch) between low-index planes of substrate and nucleus is a useful empirical guide: below about 6 % a substrate is usually a potent nucleant, above about 12 % rarely. Examples across engineering:

- **Aluminium grain refinement.** Al–5Ti–1B master alloy introduces TiB₂ particles of about 1–2 µm, on which a monolayer of Al₃Ti forms; Al₃Ti matches α-Al closely, and grains nucleate at undercoolings below 1 K. Grain size falls from millimetres to 100–200 µm, reducing hot tearing and porosity and making ingots workable, as in the opening example. Zirconium plays the same role in magnesium alloys.
- **Cast iron inoculation.** Ferrosilicon containing small amounts of Ca, Ba, Sr or Al, added to the ladle, creates oxide and sulphide particles that nucleate graphite and prevent the formation of hard, brittle iron carbide ("chill") in thin sections.
- **Cloud seeding.** Silver iodide has a hexagonal structure with a lattice mismatch of about 1–2 % with ice Ih; dispersed in clouds it nucleates ice at around −5 to −10 °C, far above the −38 °C homogeneous limit. Bacterial proteins (from *Pseudomonas syringae*) are even more potent and are used in snow-making.
- **Weld-metal toughness.** Fine titanium-oxide inclusions in steel weld metal nucleate acicular ferrite inside austenite grains, giving a fine interlocking microstructure with high toughness (Chapter 10).
- **Polymers.** Nucleating agents (sodium benzoate, sorbitol derivatives) in polypropylene raise the crystallization temperature during moulding, shortening cycle times and, with very fine spherulites, making the parts clear.
- **Pharmaceuticals and foods.** Seeding controls which crystal polymorph of a drug forms, which matters because polymorphs differ in solubility and bioavailability; tempering of chocolate seeds the desired cocoa-butter polymorph.

Conversely, **avoiding** heterogeneous nucleation is how deep undercooling is studied: levitated droplets, droplets in emulsions and fluxed melts (molten glass encasing the metal) remove surface sites.

---

## 9.4 Growth: interface-controlled and diffusion-controlled

Once a nucleus exceeds $r^*$, it grows. Two steps are in series: atoms must cross the interface and attach to the growing crystal, and (if the new phase has a different composition) solute must be carried to or from the interface by diffusion, while latent heat must be removed. The slower step controls the rate.

### Interface-controlled growth

When the composition does not change (pure metals, allotropic and massive transformations, crystallization of glasses and polymers) only attachment matters. The net rate at which atoms attach is the difference between forward and backward jumps across the interface, each thermally activated. For a driving force per atom $\Delta g$,

$$
v=\lambda\nu\exp\!\left(-\frac{Q_i}{kT}\right)\left[1-\exp\!\left(-\frac{\Delta g}{kT}\right)\right]\approx M\,\Delta G
$$

where the second form, with interface mobility $M$, holds for small driving forces. Growth velocity is constant in time and, at small undercooling, proportional to $\Delta T$. Rough metallic interfaces attach atoms at almost every site, so their kinetic undercooling is a fraction of a kelvin even at growth speeds of m/s. **Faceted** crystals (silicon, many intermetallics and oxides, organic molecules) have smooth, atomically flat interfaces; atoms can attach only at steps, which must be created by two-dimensional nucleation or supplied by screw dislocations. Their growth is slower and strongly anisotropic, which gives faceted shapes such as the plates of silicon in Al–Si eutectics. Polymer spherulites grow at a constant radial rate (micrometres per second), also an interface-controlled process.

### Diffusion-controlled growth

When the growing phase has a different composition from its matrix (a precipitate rich in solute, a ferrite grain that must reject carbon), solute must diffuse over growing distances, and growth slows with time. For a planar precipitate whose interface keeps local equilibrium, the thickness grows as

$$
x=\alpha\sqrt{Dt}
$$

and for a spherical precipitate in a dilute matrix

$$
r=\lambda\sqrt{Dt},\qquad \lambda\approx\sqrt{2\,\frac{C_0-C_m}{C_p-C_m}}
$$

where $C_0$ is the far-field matrix concentration, $C_m$ the matrix concentration in equilibrium with the precipitate and $C_p$ the precipitate composition. With $C_0=0.02$, $C_m=0.01$ and $C_p=0.30$ (atom fractions), $\lambda=0.26$: in the time that solute diffuses a distance $\sqrt{Dt}$, the precipitate radius grows by only about a quarter of that distance.

> **Status of the principle: Parabolic diffusion-controlled growth**
> *Derived.* It follows from Fick's laws with local equilibrium at a moving interface and a constant far-field composition; it fails when the diffusion fields of neighbouring particles overlap (soft impingement), when the interface is not at equilibrium (mixed control), and in the later stage where coarsening takes over (Chapter 10).

Heat is the analogue of solute in solidification: the latent heat must flow away, either into the cold mould (columnar growth into a positive temperature gradient) or into an undercooled liquid (free equiaxed growth). Both diffusions, of heat and of solute, decide the shapes of crystals growing from the melt (Section 9.6).

Many transformations have **mixed control**, with interface reaction dominating at first and diffusion later. The growth of ferrite from austenite in low-alloy steels, and of oxide scales (interface-controlled linear kinetics early, parabolic later, Chapter 34), are examples.

---

## 9.5 Overall transformation kinetics: JMAK and TTT

### Extended volume and the Avrami equation

A transformation in a real part involves many nuclei appearing at different times and growing until they meet. Johnson and Mehl, Avrami, and Kolmogorov solved this counting problem. Imagine first that nuclei form and grow in the *whole* volume, ignoring the fact that some of them would form in already transformed material and that grains overlap. For constant nucleation rate $I$ and constant growth velocity $v$ of spheres, this **extended** transformed fraction is

$$
f_{ext}=\int_0^t I\,\frac43\pi v^3(t-\tau)^3\,d\tau=\frac{\pi}{3}Iv^3t^4
$$

Only the untransformed fraction $(1-f)$ of any increment of extended volume is real, so $df=(1-f)\,df_{ext}$, which integrates to

$$
f=1-\exp(-f_{ext})=1-\exp(-kt^n)
$$

This is the **Johnson–Mehl–Avrami–Kolmogorov (JMAK)** equation. The time exponent $n$ (the **Avrami exponent**) reflects the nucleation and growth modes:

| Conditions | Avrami exponent $n$ |
|---|---|
| Constant nucleation rate, 3D interface-controlled growth | 4 |
| Site saturation (all nuclei at $t=0$), 3D interface-controlled growth | 3 |
| Constant nucleation rate, 3D diffusion-controlled growth | 2.5 |
| Site saturation, 3D diffusion-controlled growth | 1.5 |
| Site saturation on grain boundaries, after boundary saturation | 1 |
| Growth of plates or needles of fixed length, diffusion-controlled thickening | 1–1.5 |

> **Status of the principle: JMAK equation**
> *Derived.* Exact for randomly located nuclei in an infinite volume with constant (or simply time-dependent) nucleation and growth rates; it fits many recrystallization, crystallization and precipitation data well, but nucleation on non-random sites, changing driving forces and soft impingement make fitted exponents lose their mechanistic meaning.

A plot of $\ln[-\ln(1-f)]$ against $\ln t$ is a straight line of slope $n$. Measured values are often non-integer, and the exponent should be interpreted cautiously.

**Worked example — Recrystallization of cold-rolled aluminium.** Hardness measurements on cold-rolled aluminium sheet annealed at 300 °C indicate 10 % recrystallization after 10 min and 90 % after 60 min. Find the Avrami parameters and the time for 50 % and 99 % recrystallization.

*Exponent.* From $-\ln(1-f)=kt^n$ at the two points,

$$
n=\frac{\ln[-\ln0.1]-\ln[-\ln0.9]}{\ln60-\ln10}=\frac{\ln2.303-\ln0.1054}{\ln6}=\frac{3.084}{1.792}=1.72
$$

*Rate constant.* $k=-\ln0.9/10^{1.72}=2.0\times10^{-3}$ min$^{-1.72}$.

*Times.* $t_{50}=(\ln2/k)^{1/n}=30$ min and $t_{99}=(\ln100/k)^{1/n}=90$ min.

The exponent of 1.7, well below the ideal value of 3 or 4, is typical of recrystallization, where nuclei form preferentially at prior grain boundaries and shear bands and the driving force (stored dislocation energy, Chapter 10) is consumed unevenly. The fitted equation is nevertheless a reliable interpolation tool for setting continuous-annealing line speeds.

### From rate to TTT diagram

The JMAK rate constant $k$ depends steeply on temperature through both $I$ and $v$. Just below the equilibrium temperature, the driving force is small, $\Delta G^*$ is huge and nucleation is negligible. Far below it, the driving force is large but atomic mobility (proportional to $\exp(-Q/RT)$, Chapter 8) is small. The overall rate is the product of a factor rising with undercooling and a factor falling with it, and therefore has a maximum at an intermediate temperature.

Plotting, for each temperature, the time to reach a given fraction transformed (commonly 1 % and 99 %) gives a **time–temperature–transformation (TTT)** diagram with characteristic C-shaped curves. The nose of the C is the temperature of fastest transformation; to avoid the transformation entirely, a part must be cooled past the nose faster than the nose time. This construction applies equally to the formation of pearlite in steel (Chapter 10), precipitation in aluminium alloys during quenching, crystallization of polymers during injection moulding and the crystallization of glass-forming melts, where it gives the critical cooling rate for glass formation (Section 9.9).

<!-- FIGURE 9.3 | figures/ch09/fig-9-3-jmak-ttt.png | plot | Overall transformation kinetics: JMAK curves for several Avrami exponents, and the construction of a C-shaped TTT curve from nucleation and growth rates. | Content: left panel: x-axis log time (min) 0.1–1000, y-axis fraction transformed 0–1; JMAK curves with n = 1, 1.72 and 4 all passing through f = 0.5 at 30 min; markers at (10 min, 0.10) and (60 min, 0.90) on the n = 1.72 curve (worked example). Right panel: y-axis temperature from Te (equilibrium) downward; left sub-plot sketches nucleation rate I(T) (zero at Te, peaking at large undercooling) and growth rate v(T) (peaking closer to Te); main plot x-axis log time with C-curves for 1 % and 99 % transformed, nose labelled, and a cooling path just missing the nose labelled "critical cooling rate". -->

---

## 9.6 Solidification: fronts, dendrites and constitutional supercooling

### Pure metals: thermal supercooling

When a pure metal solidifies inward from a cold mould wall, heat flows from the liquid through the solid to the mould: the temperature gradient in the liquid ahead of the interface is **positive** (temperature rises into the liquid). A bump on the interface pokes into hotter liquid, melts back and the front stays planar. In an undercooled liquid, by contrast, such as an equiaxed crystal growing freely in the centre of a casting, the gradient in the liquid is negative; a bump finds itself in colder liquid, grows faster and becomes a branched **thermal dendrite**, with primary arms along preferred crystallographic directions (⟨100⟩ in cubic metals) and secondary and tertiary branches.

### Alloys: constitutional supercooling

Alloys behave differently even in a positive gradient. With $k<1$, the growing solid rejects solute, which piles up in a boundary layer of the liquid ahead of the interface. At steady state for a planar front moving at velocity $V$, the solid has composition $C_0$, the liquid at the interface has $C_0/k$, and the excess decays into the liquid over a distance of about $D_L/V$:

$$
C_L(x')=C_0\left[1+\frac{1-k}{k}\exp\!\left(-\frac{Vx'}{D_L}\right)\right]
$$

where $x'$ is distance ahead of the interface. Each liquid composition has its own liquidus temperature; the liquid near the interface, rich in solute, freezes at a lower temperature than the liquid farther away. If the actual temperature gradient $G$ is shallower than the gradient of this local liquidus temperature at the interface, a zone of liquid ahead of the front is below its own liquidus: it is **constitutionally supercooled**, and a planar front becomes unstable. The criterion for stability is

$$
\frac{G}{V}\ \ge\ \frac{\Delta T_0}{D_L},\qquad \Delta T_0=\frac{m\,C_0(1-k)}{k}
$$

where $m$ is the magnitude of the liquidus slope and $\Delta T_0$ is the equilibrium freezing range of the alloy (the gap between liquidus and solidus at $C_0$).

> **Status of the principle: Constitutional-supercooling criterion**
> *Approximate.* It compares two temperature gradients and ignores the stabilizing effect of interfacial energy and the latent-heat distribution; the more complete Mullins–Sekerka stability analysis confirms it as an excellent approximation at normal growth rates and adds absolute stability at very high velocities.

As $G/V$ falls below the critical value, the front evolves from **planar** to **cellular** (an array of parallel rounded protrusions) to **columnar dendritic** (cells develop side branches), and finally to **equiaxed dendritic** grains (Figure 9.4) nucleating in the supercooled liquid ahead of the front. The product $GV$ (the cooling rate, K/s) sets the scale of the structure: higher cooling rates give finer cells and dendrites.

<!-- FIGURE 9.4 | figures/ch09/fig-9-4-constitutional-supercooling.png | schematic | Constitutional supercooling ahead of a solidifying alloy front, and the sequence of interface morphologies as G/V decreases. | Content: top-left: solute profile C_L(x′) decaying from C0/k at the interface to C0 over distance D_L/V. Top-right: corresponding liquidus temperature T_L(x′) rising from the solidus to the liquidus of C0, with two straight actual-temperature lines: steep G (no supercooling) and shallow G (shaded supercooled zone between T_L and the line). Bottom strip: four sketches of the interface: planar, cellular, columnar dendritic, equiaxed dendritic, under an arrow of decreasing G/V; secondary axis showing "GV increasing → finer spacing". Annotation: Al–4.5Cu, ΔT0 = 75 K, critical G/V = 2.5e10 K·s/m². -->

**Worked example — Can an aluminium–copper alloy freeze with a planar front?** For Al–4.5 wt% Cu, take the liquidus slope $m=3.4$ K per wt% Cu, $k=0.17$ and $D_L=3\times10^{-9}$ m²/s.

*Freezing range.*

$$
\Delta T_0=\frac{3.4\times4.5\times(1-0.17)}{0.17}=75\ \mathrm K
$$

*Critical ratio.* $G/V\ge\Delta T_0/D_L=75/(3\times10^{-9})=2.5\times10^{10}$ K s/m².

*Speed limit.* In a steep laboratory gradient of $G=10$ K/mm ($10^4$ K/m), a planar front requires $V\le10^4/2.5\times10^{10}=4\times10^{-7}$ m/s, or 0.4 µm/s (1.4 mm per hour). Even at 100 K/mm, the limit is only 4 µm/s.

Planar solidification of a typical engineering alloy is possible only in slow laboratory crystal growth. Every casting, weld and additively manufactured part of such an alloy solidifies dendritically. Directionally solidified and single-crystal nickel-superalloy turbine blades, grown at 3–10 K/mm and a few mm/min, are still dendritic; "single crystal" means that all the dendrites belong to one crystal, selected by a spiral "grain selector" at the base of the mould, so that no grain boundaries are available for creep cavitation (Chapter 33). Semiconductor crystals are the exception: silicon is nearly pure, dopant concentrations are tiny, so $\Delta T_0$ is small and Czochralski growth at about 1 mm/min proceeds with a planar (or smoothly curved) interface.

### Dendrite arm spacing

The spacing of secondary dendrite arms, $\lambda_2$, coarsens during solidification because small arms dissolve in favour of large ones (a ripening process, Chapter 10). It is found empirically to depend mainly on the local solidification time $t_f$:

$$
\lambda_2\approx A\,t_f^{1/3}
$$

with $A\approx10$ µm s$^{-1/3}$ for many aluminium alloys. A thin-walled pressure die casting freezing in about 1 s has $\lambda_2\approx10$ µm; a sand casting freezing in 1000 s has about 100 µm. Strength, ductility and fatigue resistance of cast aluminium improve as $\lambda_2$ decreases, because porosity and brittle interdendritic phases are finer, and homogenization time scales as $\lambda_2^2$ (Chapter 8).

> **Status of the principle: Secondary dendrite arm spacing law**
> *Empirical.* The one-third exponent is supported by coarsening theory, but the constant $A$ is fitted for each alloy family; it is used to estimate local cooling rates from micrographs of failed castings.

---

## 9.7 Segregation: the Scheil equation and zone refining

### Two limits

During solidification of an alloy with $k<1$, the first solid is purer than the alloy and the last liquid is richer. How the solute ends up distributed depends on how fast it can move in each phase. Two limits bracket reality:

- **Equilibrium (lever rule).** Complete diffusion in both liquid and solid: at each temperature, solid and liquid have the tie-line compositions of Chapter 7. The final solid is uniform.
- **Scheil–Gulliver.** Complete mixing in the liquid (by convection and fast liquid diffusion), *no* diffusion in the solid, and local equilibrium at the interface. Each layer of solid keeps the composition it froze with.

Solute balance for the Scheil case gives, as fraction solid $f_s$ grows by $df_s$,

$$
(C_L-C_S)\,df_s=(1-f_s)\,dC_L
$$

and with $C_S=kC_L$ and constant $k$,

$$
C_S=kC_0(1-f_s)^{k-1},\qquad C_L=C_0(1-f_s)^{k-1}
$$

This is the **Scheil equation**. For $k<1$, $C_L$ rises without limit as $f_s\to1$: the last liquid always reaches the eutectic composition (or the lowest-melting composition available), however dilute the alloy.

> **Status of the principle: Scheil equation**
> *Approximate.* It assumes perfect liquid mixing, no solid diffusion, local interface equilibrium and constant $k$; it is close to reality for substitutional solutes in castings, but overestimates segregation for fast-diffusing interstitials such as carbon in steel, for which back-diffusion corrections are added.

**Worked example — Non-equilibrium eutectic in an Al–Cu casting.** For Al–4.5 wt% Cu with $k=0.17$ and eutectic composition 33.2 wt% Cu, compare equilibrium and Scheil solidification.

*Equilibrium.* The maximum solubility of Cu in Al is 5.65 wt% (Chapter 7). An alloy with 4.5 wt% Cu should freeze entirely as α and contain no eutectic.

*Scheil.* The liquid reaches the eutectic composition when

$$
1-f_s=\left(\frac{C_E}{C_0}\right)^{1/(k-1)}=\left(\frac{33.2}{4.5}\right)^{-1/0.83}=0.090
$$

so 9.0 % of the casting freezes as eutectic at 548 °C.

*Coring.* The solid composition rises from $kC_0=0.77$ wt% Cu at the dendrite centres to 1.36 wt% at $f_s=0.5$ and 5.2 wt% at $f_s=0.9$.

The two limits differ qualitatively (Figure 9.5): equilibrium predicts a single-phase alloy with a solidus near 573 °C, Scheil predicts about 9 % eutectic and a final freezing temperature of 548 °C. Real castings lie close to the Scheil limit; metallographers routinely find interdendritic Al₂Cu in such alloys, and it must be dissolved by homogenization before the alloy can be solution-treated (Chapters 7, 8 and 10). The Scheil prediction of a wider freezing range also explains **hot tearing**: in the last stages, a network of dendrites holding thin liquid films cannot accommodate thermal contraction and tears.

<!-- FIGURE 9.5 | figures/ch09/fig-9-5-scheil-vs-lever.png | plot | Solid composition and liquid composition versus fraction solid for Al–4.5 wt% Cu under equilibrium (lever rule) and Scheil solidification. | Content: x-axis fraction solid f_s 0–1, y-axis wt% Cu 0–35. Curves: Scheil C_S = kC0(1−f_s)^(k−1) with k = 0.17 from 0.77 wt% (f_s = 0) through 1.36 (0.5) and 5.2 (0.9), terminating at f_s = 0.91 where C_L reaches 33.2 wt% (eutectic, horizontal dashed line); Scheil C_L curve rising to 33.2; equilibrium lever-rule C_S and C_L curves ending at f_s = 1 with C_S = 4.5 wt%. Shade the final 9 % labelled "non-equilibrium eutectic (Scheil)". Inset: schematic of a cored dendrite with Cu-rich interdendritic regions. -->

### Macrosegregation and segregation in crystal growth

Microsegregation occurs over dendrite arm spacings and can be removed by homogenization. **Macrosegregation**, composition variation over the scale of a whole ingot, arises when solute-rich liquid is moved by convection, shrinkage flow or buoyancy; it produces "A-segregates" and centre-line segregation in large steel ingots for forgings and in continuously cast slabs, which cannot be removed by heat treatment and must be controlled by casting practice.

In crystal growth the Scheil equation, called the **normal-freezing** equation, gives the axial dopant distribution. For a Czochralski silicon ingot pulled from a melt doped with boron ($k=0.8$), the dopant concentration rises from $0.80C_0$ at the seed end to $0.92C_0$ at half length and $1.27C_0$ at 90 % solidified; with phosphorus ($k=0.35$) it rises from $0.35C_0$ through $0.55C_0$ to $1.56C_0$. Because resistivity tracks dopant concentration, wafers from different parts of a phosphorus-doped ingot differ in resistivity by a factor of more than four, and only part of each ingot meets a tight specification (Chapter 26).

### Zone refining

Scheil's equation also describes **purification**. Pfann's **zone refining** (1952) passes a short molten zone of length $L$ along a solid bar. Impurities with $k<1$ are swept along with the zone toward the far end. After one pass, the solid at distance $x$ from the start has

$$
\frac{C_S}{C_0}=1-(1-k)\exp\!\left(-\frac{kx}{L}\right)
$$

For $k=0.1$ the first zone length is purified tenfold ($C_S/C_0=0.10$ at $x=0$, 0.19 at $x=L$, 0.26 at $x=2L$). Multiple passes multiply the effect, and the method produced the germanium and silicon of the first transistors with impurity levels below one part per billion, and is still used for detector-grade germanium and ultra-pure metals. Its industrial descendant, **float-zone** growth of silicon, uses an RF-heated molten zone with no crucible, giving the oxygen-free high-resistivity wafers used in power devices and radiation detectors.

---

## 9.8 Eutectic and peritectic solidification; casting microstructures

### Coupled eutectic growth

At a eutectic, two solids grow side by side from one liquid. Solute rejected by one phase is the solvent needed by the other, so atoms diffuse sideways along the interface between neighbouring lamellae or rods. Close spacing shortens the diffusion distance; but each lamella adds interface, whose energy has to be paid. The balance (Jackson–Hunt theory) gives a spacing $\lambda$ that varies with growth velocity as

$$
\lambda^2V=\text{constant}
$$

so doubling the growth rate reduces the spacing by $\sqrt2$. Lamellar structures form when both phases have comparable volume fractions; when one phase is a minor fraction (roughly below 0.3) rods are favoured, as they have less interface. Directionally solidified eutectics of Ni–TaC, Al₂O₃–ZrO₂ or Al₂O₃–YAG form aligned fibre composites in situ, which have been studied for turbine and cutting-tool applications.

> **Status of the principle: Jackson–Hunt eutectic spacing**
> *Derived.* It follows from lateral solute diffusion and interface curvature for regular (non-faceted/non-faceted) eutectics with the extremum assumption for the operating spacing; it applies poorly to irregular eutectics with a faceted phase.

**Irregular eutectics** occur when one phase is faceted. In Al–Si alloys, silicon grows as coarse, brittle plates whose sharp edges initiate cracks. Adding about 0.01–0.02 wt% strontium or sodium poisons the growth steps of silicon (by inducing twinning) and turns the plates into a fine coral-like fibrous network, raising elongation from a few percent to over 10 %. Grey cast iron is an Fe–graphite eutectic in which graphite grows as interconnected flakes, giving good damping and machinability but low tensile ductility. Treating the melt with about 0.04 wt% magnesium (or cerium) removes sulphur and oxygen, changes the growth of graphite and produces **spheroidal graphite** (ductile) iron, with elongations of 10–20 %: the material of modern crankshafts, wind-turbine hubs and water pipes (Chapter 15).

### Peritectic solidification

In a peritectic $L+\alpha\to\beta$, the product β forms first at the α–liquid interface and then separates the reactants; the reaction can continue only by diffusion through β, so it is rarely completed. Three engineering examples:

- **Steel continuous casting.** "Peritectic" steels (about 0.09–0.17 wt% C) undergo δ→γ near 1495 °C in the thin solid shell, with a contraction that pulls the shell from the mould and leads to uneven shell thickness, depressions and surface cracks (Chapter 7). Casters use special mould fluxes and reduced casting speeds.
- **Nd–Fe–B magnets.** The magnetic phase Nd₂Fe₁₄B forms peritectically from primary iron and liquid. Ingot casting leaves soft-magnetic primary α-iron dendrites that degrade the magnet; rapid **strip casting** (cooling rates of order 10³ K/s) suppresses primary iron and gives the fine, uniform alloy used for sintered magnets in electric vehicle motors and wind turbines (Chapter 27).
- **YBCO superconductors.** YBa₂Cu₃O₇₋δ forms peritectically near 1000 °C from Y₂BaCuO₅ and liquid. Slow "melt-texturing" through the peritectic grows large aligned grains for levitation magnets and current leads.

### Casting macrostructure

A metal poured into a mould typically develops three zones (Figure 9.6):

1. **Chill zone.** A thin layer of fine equiaxed grains forms against the cold mould wall, where undercooling is high and the wall provides abundant nucleation sites.
2. **Columnar zone.** Grains whose fast-growth direction (⟨100⟩ for cubic metals) is nearly parallel to the heat flow outgrow their neighbours and form long columnar grains, a natural texture.
3. **Equiaxed zone.** In the centre, the liquid becomes constitutionally supercooled; crystals nucleated on inoculant particles or formed from dendrite fragments detached by convection grow freely as equiaxed grains.

The balance between columnar and equiaxed zones is a central control in casting. Large columnar grains give anisotropic properties, hot tearing and poor workability (the opening example); inoculation, low pouring temperature, stirring (mechanical or electromagnetic) and alloying with growth-restricting solutes (such as Ti in Al, quantified by a "growth-restriction factor" proportional to $mC_0(1-k)$) promote equiaxed grains. Conversely, directional solidification deliberately eliminates equiaxed grains to produce columnar or single-crystal turbine blades whose grain boundaries are aligned with, or absent from, the stress axis.

Solidification time itself, which governs dendrite arm spacing and grain size, is estimated for sand castings by **Chvorinov's rule**, $t_s=B\,(V/A)^2$, where $V/A$ is the casting modulus (volume over cooling surface area) and $B$ is a mould constant. Feeders (risers) are designed to have a larger modulus than the section they feed, so that they freeze last and supply liquid to compensate for solidification shrinkage of 3–7 % in most metals (Chapter 38).

<!-- FIGURE 9.6 | figures/ch09/fig-9-6-casting-macrostructure.png | schematic | Macrostructure of a cast ingot: chill zone, columnar zone and equiaxed zone, with the effect of grain-refiner addition. | Content: two side-by-side half-sections of a cylindrical ingot (about 100 mm diameter). Left "no refiner": thin chill zone of fine grains at the wall (~1 mm), long columnar grains (tens of mm) growing radially inward, small central equiaxed zone; annotations "⟨100⟩ ∥ heat flow", "hot tears between columnar grains". Right "with Al–5Ti–1B": fully fine equiaxed grains of ~150 µm (drawn schematically). Below: a cooling-rate/scale bar mapping process to secondary dendrite arm spacing: sand casting (~1 K/s, λ2 ≈ 50–100 µm), permanent mould (~10 K/s), pressure die casting (~100 K/s, λ2 ≈ 10 µm), atomization and additive manufacturing (1e3–1e6 K/s, sub-micrometre cells). -->

---

## 9.9 Rapid solidification and metallic glasses

### Cooling faster

Conventional casting cools at 0.1–100 K/s. Rapid solidification processes reach $10^3$–$10^8$ K/s by making at least one dimension small and extracting heat into a good conductor:

| Process | Typical cooling rate (K/s) | Product |
|---|---|---|
| Sand casting | 0.1–10 | Large castings |
| Pressure die casting | 10–10³ | Thin-walled Al and Mg parts |
| Strip casting | 10²–10⁴ | Nd–Fe–B flake, thin steel strip |
| Gas atomization | 10²–10⁵ (finer powders faster) | Metal powders for AM, PM and thermal spray |
| Laser powder-bed fusion | 10⁴–10⁷ | Additively manufactured parts |
| Melt spinning | 10⁵–10⁶ | Amorphous and nanocrystalline ribbons 20–50 µm thick |
| Splat quenching, laser surface glazing | 10⁶–10⁸ | Foils, surface layers |

The effects of rapid solidification follow from this chapter's results. Higher cooling rates mean finer dendrites and eutectics (Sections 9.6 and 9.8), less segregation, **extended solid solubility** (solute trapped in the solid at concentrations far above the equilibrium solvus, as interface velocities approach the speed of solute diffusion and $k\to1$), and **metastable phases** that nucleate faster than the stable ones. Additively manufactured aluminium and nickel alloys owe their high as-built strength to sub-micrometre cells, and also their susceptibility to solidification cracking, to these effects (Chapter 40).

### Bypassing crystallization: metallic glasses

If a liquid is cooled fast enough to pass the nose of its crystallization TTT curve (Figure 9.3), it never crystallizes. Its viscosity rises continuously until, at the **glass transition temperature** $T_g$, the atomic structure freezes into an amorphous solid. Silicate liquids do this at ordinary cooling rates because their viscosity near the melting point is already enormous (Chapter 17). Simple metallic liquids have viscosities like water and crystallize within microseconds, so a glass forms only above a **critical cooling rate** $R_c$ given approximately by the nose of the TTT curve:

$$
R_c\approx\frac{T_l-T_n}{t_n}
$$

where $T_l$ is the liquidus, and $T_n$ and $t_n$ are the temperature and time of the nose.

The first metallic glass, Au₇₅Si₂₅, was made by splat quenching in 1960 by Duwez, with $R_c$ of order $10^6$ K/s. Since the thickness that can be cooled at a given rate is limited by heat conduction, the critical thickness scales roughly as $x_c\approx\sqrt{\alpha\,\Delta T/R_c}$, with thermal diffusivity $\alpha\approx2\times10^{-6}$ m²/s and a temperature drop $\Delta T\approx600$ K from liquidus to glass transition. That gives about 35 µm for $R_c=10^6$ K/s (the thickness of melt-spun ribbon), about 1 mm for $10^3$ K/s and about 35 mm for 1 K/s: an order-of-magnitude estimate that matches the observed hierarchy.

**Glass-forming ability** is improved by anything that slows crystallization:

- **Deep eutectics.** Alloys near deep eutectics have a low liquidus, so the liquid reaches high viscosity sooner. Turnbull's **reduced glass-transition temperature** $T_{rg}=T_g/T_l$ is the usual measure; $T_{rg}\gtrsim2/3$ indicates easy glass formation.
- **Confusion principle (Inoue's rules).** At least three elements, atomic size differences above about 12 %, and negative heats of mixing; complex liquids find it hard to rearrange into the crystal structures available.
- **Clean melts.** Heterogeneous nucleation on oxides must be avoided, often by fluxing or high-purity processing.

> **Status of the principle: Glass-forming-ability criteria ($T_{rg}$, Inoue's rules)**
> *Empirical.* They summarize the nucleation and growth physics of this chapter and correlate well with measured critical thicknesses, but many exceptions exist, and no single parameter predicts glass formation reliably.

**Bulk metallic glasses** with $R_c$ of 1–100 K/s can be cast into parts millimetres to centimetres thick. Vitreloy 1 (Zr₄₁.₂Ti₁₃.₈Cu₁₂.₅Ni₁₀Be₂₂.₅) has $T_g\approx625$ K and $T_l\approx993$ K, so $T_{rg}\approx0.63$, and an $R_c$ of about 1 K/s; Pd–Cu–Ni–P glasses form rods several centimetres in diameter.

### Properties and uses

Having no crystal lattice and therefore no dislocations, metallic glasses yield at stresses near their theoretical limit: Zr-based glasses reach about 1.8–2 GPa with an elastic strain limit of about 2 %, compared with 0.5 % or less for crystalline alloys, and store large elastic energy per unit volume (Chapter 11). Their weakness is that deformation localizes in narrow **shear bands** with no work hardening, so in tension they fail with almost no plastic strain; composites containing ductile crystalline dendrites improve toughness. Because they soften above $T_g$ like a polymer, they can be thermoplastically moulded with nanometre precision.

| Application | Material | Property exploited |
|---|---|---|
| Distribution-transformer cores | Fe–Si–B ribbon (melt-spun) | Core loss about 60–75 % lower than grain-oriented Si steel; no grain boundaries or magnetocrystalline anisotropy (Chapter 27) |
| Anti-theft tags, magnetic sensors | Co- and Fe-based ribbons | Soft magnetism, magnetostriction |
| Golf club faces, springs, watch parts | Zr- and Ti-based bulk glasses | High elastic strain and resilience |
| Precision gears for micromotors, surgical blades | Zr-, Ni-based glasses | Net-shape moulding, sharp edges, wear |
| Nanocrystalline alloys (Finemet) | Fe–Si–B–Nb–Cu annealed glass | Controlled crystallization to 10 nm grains: very soft magnets |

The last row closes a circle: annealing a metallic glass just above $T_g$ triggers copious homogeneous nucleation, with Cu clusters acting as heterogeneous sites and Nb restricting growth. The result is a nanocrystalline magnet with 10–15 nm grains, an example of using the nucleation and growth theory of this chapter as a design tool rather than a hazard.

> **Boundary.** The thermodynamics of interfaces (interfacial energy, Gibbs–Thomson, Young's equation) are developed in Chapter 6 and the statistical mechanics of fluctuations belongs to the Engineering Physics book. Heat-transfer analysis of castings and welds is part of the thermal-engineering curriculum; this chapter takes cooling rates and gradients as inputs.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| Where do the driving forces, interfacial energies and the Gibbs–Thomson effect come from? | Chapter 6 |
| Which phases and compositions does solidification follow, and what are the eutectic and peritectic points? | Chapter 7 |
| How fast does solute diffuse, and how long does homogenization take? | Chapter 8 |
| How do nucleation and growth operate in solid-state transformations: precipitation, pearlite, bainite, martensite, recrystallization? | Chapter 10 |
| How do grain size, dendrite spacing and porosity control strength and fatigue? | Chapters 13 and 14 |
| How are cast irons and steels inoculated, cast and heat-treated? | Chapter 15 |
| How are glasses formed and glass-ceramics crystallized? | Chapter 17 |
| How do polymers crystallize, and how is crystallinity controlled in moulding? | Chapter 20 |
| How are silicon crystals grown and doped for devices? | Chapter 26 |
| How are casting, welding and additive manufacturing processes designed around solidification? | Chapters 38, 39 and 40 |
| How are nucleation and dendritic growth simulated by phase-field and atomistic methods? | Chapter 46 |

**Next:** Chapter 10 carries nucleation and growth into the solid state, where strain energy, coherency and diffusionless shear produce the precipitates, pearlite, bainite and martensite that give engineering alloys their strength.
