# Chapter 6 — Thermodynamics of Materials

*Part II · Thermodynamics and Kinetics*

A duplex stainless-steel valve body in a refinery has run for twelve years at about 320 °C without trouble. During a shutdown it is struck by a dropped tool and cracks like cast iron. Its Charpy impact energy, more than 100 J when new, has fallen below 20 J. No corrosion, no fatigue and no overload explain it. The cause is inside the ferrite: at these temperatures iron–chromium solid solutions are not stable as a single phase. Over years the ferrite has separated, on a scale of a few nanometres, into iron-rich and chromium-rich regions, and the resulting internal stresses pin dislocations. The phenomenon, "475 °C embrittlement", is predicted by a free-energy curve with a hump in it — a miscibility gap — and it is why design codes cap the service temperature of duplex and ferritic stainless steels near 250–300 °C.

In the same plant, stainless-steel tube leaving a bright-annealing furnace at 1100 °C emerges dull green instead of mirror-bright: the hydrogen atmosphere was wet enough to oxidise chromium. The maximum permissible water content of the hydrogen can be read off an Ellingham diagram in a minute. Both problems, one taking twelve years and one taking twelve minutes, are questions about which state of a material has the lowest Gibbs energy.

> **How do Gibbs energy and chemical potential decide which phases, compositions and defect populations a material adopts?**
> **How do solution models, interfaces and gas atmospheres change that answer, and how is it read off a diagram?**

| Concept | Engineering destination |
|---|---|
| Gibbs energy, chemical potential, equilibrium | Every phase diagram (Ch 7) and transformation (Ch 9–10) |
| Ideal, regular and real solutions; activity | Alloy design, slag–metal refining, braze and solder chemistry, carbon potential of furnace atmospheres |
| Gibbs–Duhem equation | Obtaining one component's activity from another's; consistency of thermodynamic databases (CALPHAD, Ch 7, 46) |
| Free-energy curves, common tangent | Phase boundaries, lever rule, driving forces for precipitation |
| Miscibility gaps and spinodals | 475 °C embrittlement, Alnico and Fe–Cr–Co magnets, phase-separated glasses, polymer blends (Ch 20) |
| Sublattice models, ordering | Interstitial steels, intermetallics (Ni$_3$Al, TiAl), ordered superalloy phases |
| Surface and interface energy, Gibbs–Thomson, wetting | Coarsening (Ch 10), nanoparticle melting (Ch 30), brazing and soldering (Ch 39), liquid-phase sintering (Ch 17) |
| Thermodynamics of point defects | Vacancy equilibrium, oxide conductivity, fuel-cell and sensor ceramics (Ch 25, 32) |
| Ellingham diagrams | Extractive metallurgy, heat-treatment atmospheres, oxidation resistance (Ch 34), brazing atmospheres |

**Roadmap.** Gibbs energy and equilibrium (6.1) → solutions and activity (6.2) → free-energy curves and the common tangent (6.3) → miscibility gaps and spinodals (6.4) → sublattices and ordering (6.5) → surfaces and interfaces (6.6) → point defects (6.7) → oxidation and reduction: Ellingham diagrams (6.8).

---

## 6.1 Gibbs energy, chemical potential and equilibrium

### The criterion

Materials processing takes place at fixed temperature and pressure — in a furnace, a mould, a reactor, the atmosphere. Under those conditions the second law of thermodynamics takes a simple form: a closed system evolves spontaneously towards lower **Gibbs energy**

$$
G=H-TS
$$

and is in equilibrium when $G$ is a minimum. $H$ is the enthalpy (for condensed phases at ordinary pressure, essentially the internal energy of bonding) and $S$ the entropy (configurational and vibrational). At low temperature the enthalpy term dominates and the most strongly bonded, most ordered state wins; at high temperature the $-TS$ term rewards disorder: mixing, vacancies, liquids, gases. Every phase transformation in this part of the book is a competition between these two terms.

The equilibrium may be **stable** (the global minimum), **metastable** (a local minimum separated from the global one by a barrier: martensite, a glass, diamond at room temperature, a supersaturated aluminium alloy) or **unstable** (no barrier at all: the inside of a spinodal, Section 6.4). Engineering materials are very often metastable; thermodynamics tells us the direction in which they would change, and kinetics (Chapters 8–10) whether they do so in a millisecond or a millennium.

### Chemical potential

For a system containing several components, the Gibbs energy depends on the amounts $n_i$ of each:

$$
dG=V\,dP-S\,dT+\sum_i\mu_i\,dn_i,\qquad \mu_i=\left(\frac{\partial G}{\partial n_i}\right)_{T,P,n_{j\ne i}}
$$

The **chemical potential** $\mu_i$ is the increase in $G$ when one mole of component $i$ is added at constant temperature, pressure and amounts of everything else. It plays the role for matter that temperature plays for heat: atoms of $i$ flow from regions or phases of high $\mu_i$ to regions of low $\mu_i$. Equilibrium between phases $\alpha,\beta,\dots$ therefore requires

$$
\mu_i^\alpha=\mu_i^\beta=\cdots\qquad\text{for every component }i
$$

together with equal temperature and pressure. This condition, applied to free-energy curves, generates every phase diagram in Chapter 7. Chemical-potential gradients, not concentration gradients, are what drive diffusion (Chapter 8); the two usually point the same way, but not always, as "uphill" diffusion of carbon in welded dissimilar steels shows.

> **Status of the principle: minimum Gibbs energy at constant $T$ and $P$**
> *Fundamental.* A consequence of the second law of thermodynamics for a closed system exchanging heat and work with surroundings at fixed temperature and pressure; it identifies the equilibrium state but says nothing about the rate of approach.

> **Boundary.** The laws of thermodynamics, the definitions of $H$, $S$ and $G$, standard states and reaction equilibrium belong to the Advanced Chemistry book. This chapter recaps them only as far as needed and applies them to solids, solutions, interfaces and defects.

### Pure substances: the $G$–$T$ diagram

For a pure substance, $(\partial G/\partial T)_P=-S$, so $G$ falls with temperature, and it falls faster for the phase with the higher entropy. The liquid, with more entropy than the solid, has a steeper $G(T)$ curve; the two curves cross at the melting point, where $\Delta G=\Delta H_f-T_m\Delta S_f=0$, so $\Delta S_f=\Delta H_f/T_m$. For most metals $\Delta S_f\approx R$, about 8–10 J mol$^{-1}$ K$^{-1}$ (Richard's rule). Just below $T_m$, the driving force for solidification is approximately

$$
\Delta G_v\approx\frac{\Delta H_f\,\Delta T}{T_m}
$$

per mole, where $\Delta T$ is the undercooling. This simple linear result is the starting point of nucleation theory (Chapter 9). The same construction for two solid phases explains allotropy: iron is BCC below 912 °C, FCC between 912 and 1394 °C, and BCC again up to melting at 1538 °C, because the magnetic and vibrational entropy contributions of the BCC phase change with temperature differently from those of FCC.

---

## 6.2 Solutions: ideal, regular and real

### Mixing

When two components A and B are mixed to form a single solid or liquid solution with mole fractions $x_A=1-x$ and $x_B=x$, the Gibbs energy per mole of solution is

$$
G=x_AG_A^\circ+x_BG_B^\circ+\Delta G_{\mathrm{mix}},\qquad \Delta G_{\mathrm{mix}}=\Delta H_{\mathrm{mix}}-T\,\Delta S_{\mathrm{mix}}
$$

The first two terms are the weighted Gibbs energies of the pure components (a straight line in a plot of $G$ against $x$); everything interesting is in $\Delta G_{\mathrm{mix}}$.

### The ideal solution

If A and B atoms are distributed at random on the sites of one lattice and the bond energies do not depend on which atoms are neighbours, $\Delta H_{\mathrm{mix}}=0$ and the only change on mixing is the configurational entropy. Counting the arrangements of $N_A$ and $N_B$ atoms on $N$ sites with Boltzmann's formula $S=k_B\ln W$ and Stirling's approximation gives

$$
\Delta S_{\mathrm{mix}}^{\mathrm{id}}=-R\,(x_A\ln x_A+x_B\ln x_B),\qquad \Delta G_{\mathrm{mix}}^{\mathrm{id}}=RT\,(x_A\ln x_A+x_B\ln x_B)
$$

$\Delta G_{\mathrm{mix}}^{\mathrm{id}}$ is always negative, with a maximum depth of $-RT\ln2$ at $x=0.5$ ($-5.76$ kJ mol$^{-1}$ at 1000 K), and its slope is infinite at both ends. That infinite slope has a profound consequence: the first small addition of any solute always lowers the Gibbs energy, however unfavourable its bonding. **No substance is perfectly pure in equilibrium.** Ultra-pure silicon, zone-refined to parts per billion (Chapter 9), fights against this entropy term at every step.

> **Status of the principle: ideal entropy of mixing**
> *Derived.* It follows from statistical counting of random arrangements; it is exact for random mixing on equivalent sites and is the configurational part of every solution model, though real solutions also show short-range order, which lowers the entropy below the ideal value.

### The regular solution

Real atoms do care about their neighbours. In the simplest model, the **regular solution**, the atoms still mix randomly (so the entropy is ideal), but each A–B bond has an energy different from the average of A–A and B–B bonds. Counting bonds in a random mixture with coordination number $z$ gives

$$
\Delta H_{\mathrm{mix}}=\Omega\,x_Ax_B,\qquad \Omega=zN_A\left[\varepsilon_{AB}-\tfrac12(\varepsilon_{AA}+\varepsilon_{BB})\right]
$$

so that

$$
\Delta G_{\mathrm{mix}}=\Omega\,x_Ax_B+RT\,(x_A\ln x_A+x_B\ln x_B)
$$

The **interaction parameter** $\Omega$ summarises the chemistry. If unlike bonds are stronger (more negative) than the average of like bonds, $\Omega<0$: mixing is exothermic, the atoms prefer unlike neighbours and, at low temperature, may order (Section 6.5) or form compounds. If unlike bonds are weaker, $\Omega>0$: mixing is endothermic and, at low enough temperature, the solution splits into two (Section 6.4). The dimensionless ratio $\Omega/RT$ decides the shape of the curve (Figure 6.1).

<!-- FIGURE 6.1 | figures/ch06/fig-6-1-regular-solution-curves.png | plot | Gibbs energy of mixing of a regular solution for several values of Ω/RT: a single minimum for Ω/RT < 2, two minima and a central hump for Ω/RT > 2. | Content: x-axis mole fraction x_B 0–1; y-axis ΔG_mix/RT from −0.8 to +0.3. Five curves: Ω/RT = −2 (deep single minimum, label "ordering tendency"), 0 (ideal, minimum −ln2 = −0.693), 1.5, 2.0 (flat bottom, label "critical"), 3.0 (two minima at x = 0.071 and 0.929 with ΔG/RT = −0.058, hump at x = 0.5 rising to +0.057). On the Ω/RT = 3 curve mark the inflection points (spinodal, x = 0.211 and 0.789) and draw the common tangent touching the two minima. Inset: separate ΔH_mix = Ω x(1−x) and −TΔS_mix curves for Ω/RT = 3. -->

> **Status of the principle: regular-solution model**
> *Approximate.* It assumes random mixing, pairwise nearest-neighbour bonds independent of composition and temperature, and no size mismatch; it captures miscibility gaps and ordering tendencies qualitatively and fits some liquid and solid alloys well, but real interaction parameters vary with composition and temperature.

### Real solutions and excess functions

For real systems the deviation from ideality is collected into an **excess Gibbs energy**, $G^{\mathrm{ex}}=\Delta G_{\mathrm{mix}}-\Delta G_{\mathrm{mix}}^{\mathrm{id}}$. The regular solution has $G^{\mathrm{ex}}=\Omega x_Ax_B$. Computational thermodynamics (CALPHAD, Chapter 7) generalises this with a **Redlich–Kister** polynomial,

$$
G^{\mathrm{ex}}=x_Ax_B\sum_{v=0}^{n}L_v\,(x_A-x_B)^v,\qquad L_v=a_v+b_vT
$$

whose coefficients are fitted to measured phase boundaries, enthalpies of mixing and activities. Two to four terms usually suffice for a binary. The quasi-chemical model goes one step further and allows the distribution of atoms to depart from random (short-range order), which matters in strongly interacting liquids such as slags and molten salts.

> **Status of the principle: Redlich–Kister excess Gibbs energy**
> *Empirical.* A flexible polynomial fit with no physical derivation, used because it is thermodynamically consistent and extrapolates well into ternary and higher systems; its reliability is limited to the range of data fitted.

### Activity

The chemical potential of a component in a solution is written relative to a standard state (usually the pure component in the same phase) as

$$
\mu_i=\mu_i^\circ+RT\ln a_i,\qquad a_i=\gamma_i\,x_i
$$

where $a_i$ is the **activity** and $\gamma_i$ the **activity coefficient**. For an ideal solution $\gamma_i=1$ (**Raoult's law**). For a regular solution,

$$
RT\ln\gamma_A=\Omega\,x_B^2,\qquad RT\ln\gamma_B=\Omega\,x_A^2
$$

Positive $\Omega$ gives $\gamma>1$ (the component is "less at home" in the solution than pure, and escapes more readily: higher vapour pressure, more reactive). Negative $\Omega$ gives $\gamma<1$. In very dilute solutions $\gamma_B$ approaches a constant $\gamma_B^\infty$ (**Henry's law**), which is why dilute solutes — carbon, nitrogen and hydrogen in steel, dopants in silicon, impurities in copper — are often described with a 1 wt % Henrian standard state in metallurgical practice.

Activity is the quantity that controls chemical exchange with the surroundings. The carbon activity of a furnace atmosphere sets the carbon content reached in a carburized gear (Chapters 8, 15); the activity of zinc in brass determines how much zinc boils off during casting and welding; the activity of oxygen in liquid steel determines how much aluminium is needed to deoxidise it; the activity of chromium in stainless steel enters the bright-annealing calculation of Section 6.8.

### The Gibbs–Duhem equation

The chemical potentials of the components of a solution are not independent. Because $G=\sum n_i\mu_i$ and also $dG=\sum\mu_i\,dn_i$ at constant $T$ and $P$, it follows that

$$
\sum_i x_i\,d\mu_i=0\qquad\text{or, for a binary,}\qquad x_A\,d\ln a_A+x_B\,d\ln a_B=0
$$

If one component's activity is measured over a composition range — for example the vapour pressure of zinc over brass, or the EMF of a solid-electrolyte cell sensitive to one species — the activity of the other follows by integration. The equation also tests the consistency of tabulated data: any model in which the activities violate it is wrong.

> **Status of the principle: Gibbs–Duhem equation**
> *Derived.* A mathematical consequence of $G$ being a homogeneous first-order function of the amounts of the components; it holds exactly for any phase in equilibrium at fixed $T$ and $P$.

**Worked example — Activities in a gold–nickel alloy.** Gold and nickel are both FCC and mix completely at high temperature, but the large size difference (atomic radii 0.144 and 0.125 nm) makes the mixing enthalpy positive and opens a miscibility gap at low temperature, with a maximum near 810 °C (1083 K). Treat the system as a regular solution with that critical temperature; as Section 6.4 shows, $T_c=\Omega/2R$, so

$$
\Omega=2RT_c=2\times8.314\times1083=18.0\ \mathrm{kJ\,mol^{-1}}
$$

At 1200 K, for an alloy with $x_{\mathrm{Ni}}=0.20$:

$$
\ln\gamma_{\mathrm{Ni}}=\frac{\Omega\,x_{\mathrm{Au}}^2}{RT}=\frac{18\,008\times0.64}{8.314\times1200}=1.155,\qquad \gamma_{\mathrm{Ni}}=3.17,\qquad a_{\mathrm{Ni}}=0.635
$$

$$
\ln\gamma_{\mathrm{Au}}=\frac{18\,008\times0.04}{8.314\times1200}=0.0722,\qquad \gamma_{\mathrm{Au}}=1.075,\qquad a_{\mathrm{Au}}=0.860
$$

An alloy containing only 20 % nickel has a nickel activity of 0.64: the nickel behaves almost as if it were two-thirds pure, so it oxidises, evaporates and dissolves into a contacting phase far more readily than its mole fraction suggests. Differentiating the two expressions confirms that $x_{\mathrm{Au}}\,d\ln a_{\mathrm{Au}}+x_{\mathrm{Ni}}\,d\ln a_{\mathrm{Ni}}=0$ at every composition, as Gibbs–Duhem requires. Gold–nickel alloys near Au–18Ni (wt %) are high-reliability brazes for aerospace and vacuum hardware; the positive deviation explains both why they melt at a minimum temperature lower than either metal and why their solidified microstructure can phase-separate during long service at intermediate temperatures. (The real miscibility gap is asymmetric, with its maximum near 70 at.% Ni; the symmetric regular model captures its size but not its shape, which is why CALPHAD uses Redlich–Kister terms.)

---

## 6.3 Free-energy–composition curves and the common tangent

### Molar Gibbs energy and chemical potentials

A plot of molar Gibbs energy against composition at fixed temperature carries all the thermodynamic information of a binary system. Its most useful geometric property is the **tangent construction**: the tangent to the $G(x)$ curve at composition $x$ intersects the vertical axes at $x_B=0$ and $x_B=1$ at the chemical potentials $\mu_A$ and $\mu_B$ of the solution of that composition.

$$
\mu_A=G-x_B\frac{dG}{dx_B},\qquad \mu_B=G+(1-x_B)\frac{dG}{dx_B}
$$

> **Status of the principle: tangent-intercept construction**
> *Derived.* It follows directly from the definition of partial molar quantities for a binary; it holds for any $G(x)$ curve, measured or modelled.

### Two-phase equilibrium

Suppose two phases, α and β, each have their own $G(x)$ curve. An alloy of overall composition $x_0$ can exist as a single phase, or it can split into α of composition $x_\alpha$ and β of composition $x_\beta$, with mole fractions given by mass balance (the **lever rule**):

$$
f_\beta=\frac{x_0-x_\alpha}{x_\beta-x_\alpha},\qquad f_\alpha=1-f_\beta
$$

The Gibbs energy of the two-phase mixture lies on the straight line joining the points $(x_\alpha,G^\alpha)$ and $(x_\beta,G^\beta)$. The lowest such line is the **common tangent** to the two curves. At the tangent points, both phases have the same $\mu_A$ and the same $\mu_B$, which is exactly the equilibrium condition of Section 6.1. Therefore:

- for $x_0<x_\alpha$, single-phase α has the lowest $G$;
- for $x_\alpha<x_0<x_\beta$, the equilibrium state is a mixture of α at $x_\alpha$ and β at $x_\beta$, in proportions given by the lever rule;
- for $x_0>x_\beta$, single-phase β is stable.

The tangent compositions, traced as temperature changes, become the phase boundaries (solvus, solidus, liquidus) of a phase diagram (Chapter 7, Figure 6.2).

> **Status of the principle: common-tangent construction**
> *Derived.* It is the geometric statement of equal chemical potentials in coexisting phases; exact within whatever $G(x)$ curves are used, and the basis of every computed phase diagram.

<!-- FIGURE 6.2 | figures/ch06/fig-6-2-common-tangent.png | schematic | Common-tangent construction: two phases coexist at the compositions where a single straight line is tangent to both free-energy curves; the tangent's intercepts give the chemical potentials. | Content: x-axis x_B 0–1, y-axis molar G (arbitrary units). α curve (blue, minimum near x = 0.2) and β curve (orange, minimum near x = 0.75). Common tangent line touching α at x_α = 0.30 and β at x_β = 0.65, extended to x = 0 and x = 1 with intercepts labelled μ_A and μ_B. Alloy x_0 = 0.45 marked by a vertical dotted line: point on the α curve (higher) and point on the tangent (lower), the vertical gap labelled "energy gained by separating". Lever-rule bar under the axis: f_β = (x_0 − x_α)/(x_β − x_α) = 0.43. Also mark a precipitation driving force: from a supersaturated α of composition x_0, tangent to α at x_0 and its vertical distance to the β curve at the β composition labelled "ΔG_n, driving force for nucleating β" (link to Ch 9). -->

### Driving forces

The same diagram measures the **driving force** for a transformation. A supersaturated α solution of composition $x_0$ (an aluminium–copper alloy just quenched from the solution treatment, for example) has a higher $G$ than the equilibrium α + β mixture. The vertical distance between its $G$ and the common tangent is the total energy that precipitation can release; a parallel-tangent construction gives the driving force per mole of the first β nucleus. These quantities, typically a few hundred to a few thousand J mol$^{-1}$, set nucleation rates (Chapter 9) and precipitation sequences (Chapter 10). The same diagram also shows why metastable phases form first: a phase whose curve lies above the equilibrium β curve can still lie below the supersaturated α, so its precipitation is downhill, and if it nucleates more easily (coherent, low interface energy) it wins the race.

---

## 6.4 Miscibility gaps and spinodals

### The gap

When $\Omega>0$ the enthalpy term $\Omega x(1-x)$ has a maximum at $x=0.5$, while the entropy term has a minimum there. At high temperature entropy wins and $G(x)$ has a single minimum. Below a **critical temperature** $T_c$ the curve develops a central hump with two minima, and alloys between them lower their Gibbs energy by separating into two solutions of the same crystal structure but different compositions. The region of compositions and temperatures where this happens is a **miscibility gap**, bounded by the **binodal** (the locus of common-tangent points).

For a symmetric regular solution, the common tangent is horizontal, the binodal compositions are the minima of $G$, and setting $dG/dx=0$ gives

$$
\ln\frac{x}{1-x}=-\frac{\Omega\,(1-2x)}{RT}
$$

### The spinodal

Inside the gap there are two kinds of region. Where the curve is concave upward ($\partial^2G/\partial x^2>0$) a homogeneous solution is metastable: a small fluctuation in composition *raises* $G$, and separation can only start by nucleation of a distinctly different composition. Where the curve is concave downward ($\partial^2G/\partial x^2<0$) the solution is unstable: any small fluctuation lowers $G$ and grows spontaneously, with no nucleation barrier. The boundary between them, $\partial^2G/\partial x^2=0$, is the **spinodal**. For the regular solution,

$$
\frac{\partial^2G}{\partial x^2}=-2\Omega+\frac{RT}{x(1-x)}=0\quad\Rightarrow\quad x(1-x)=\frac{RT}{2\Omega}
$$

The binodal and spinodal meet at the top of the gap, where $x=\tfrac12$ and

$$
T_c=\frac{\Omega}{2R}
$$

> **Status of the principle: critical temperature $T_c=\Omega/2R$ of a regular solution**
> *Derived.* Exact within the regular-solution model; real miscibility gaps are often asymmetric and their critical temperatures are lowered by short-range order, and in crystalline solids the elastic energy of coherent composition waves depresses the observable ("coherent") spinodal below the chemical one.

**Worked example — The miscibility gap of a regular solution with $\Omega=18.0$ kJ mol$^{-1}$.** With the Au–Ni value from Section 6.2, $T_c=18\,008/(2\times8.314)=1083$ K. Solving the binodal equation numerically and the spinodal equation directly:

| $T$ (K) | Binodal $x$ | Spinodal $x$ |
|---|---|---|
| 500 | 0.015 and 0.985 | 0.133 and 0.867 |
| 700 | 0.063 and 0.937 | 0.203 and 0.797 |
| 900 | 0.169 and 0.831 | 0.295 and 0.705 |
| 1000 | 0.268 and 0.732 | 0.362 and 0.638 |
| 1083 | 0.5 | 0.5 |

At 700 K, the spinodal composition follows from $x(1-x)=RT/2\Omega=8.314\times700/36\,016=0.1616$, giving $x=0.203$. Now consider two alloys aged at 700 K. An alloy with $x=0.15$ lies between binodal and spinodal: it is metastable and decomposes only by nucleation and growth of discrete particles of composition near 0.94. An alloy with $x=0.30$ lies inside the spinodal: it decomposes spontaneously by the growth of a fine, interconnected composition wave whose wavelength is set by the balance of chemical driving force and the gradient-energy penalty for sharp composition changes (the Cahn–Hilliard picture, Chapter 10). In both cases the final state is a mixture of $x=0.063$ and $x=0.937$, and by the lever rule the alloy with $x=0.30$ ends with a fraction $(0.30-0.063)/(0.937-0.063)=0.27$ of the nickel-rich phase.

<!-- FIGURE 6.3 | figures/ch06/fig-6-3-miscibility-gap-spinodal.png | plot | Miscibility gap of a regular solution (Ω = 18.0 kJ mol⁻¹): free-energy curve at 700 K above, binodal and spinodal in temperature–composition space below. | Content: upper panel: ΔG_mix (J mol⁻¹) vs x from 0 to 1 at T = 700 K, curve ΔG = Ω x(1−x) + RT[x ln x + (1−x) ln(1−x)], value at x = 0.5 is +468 J mol⁻¹; minima at x = 0.063 and 0.937 joined by the common tangent; inflection points at x = 0.203 and 0.797 marked "spinodal". Lower panel: T (K) 400–1150 vs x; binodal (solid) through (0.015, 500), (0.063, 700), (0.169, 900), (0.268, 1000), peak (0.5, 1083); spinodal (dashed) through (0.133, 500), (0.203, 700), (0.295, 900), (0.362, 1000). Region between curves labelled "metastable: nucleation and growth"; inside spinodal "unstable: spinodal decomposition". Alloys x = 0.15 and x = 0.30 marked at 700 K with small sketches of discrete precipitates vs interconnected morphology. Dotted vertical lines connect the panels. -->

### Where miscibility gaps matter

| System | Gap | Engineering consequence |
|---|---|---|
| Fe–Cr (ferrite) | Below about 500–550 °C, α (Fe-rich) + α′ (Cr-rich) | 475 °C embrittlement of ferritic and duplex stainless steels and of cast duplex pipework in nuclear plants; service limits near 250–300 °C |
| Fe–Cr–Co, Alnico (Fe–Ni–Al–Co) | Spinodal decomposition into elongated magnetic and non-magnetic phases | Permanent magnets whose coercivity comes from the spinodal shape anisotropy (Ch 27) |
| Al–Zn | Gap below about 350 °C | Rapid natural ageing of Al–Zn alloys; Zn-rich zones in 7xxx aerospace alloys |
| Cu–Ni–Sn | Spinodal hardening | High-strength, high-conductivity spring and bearing alloys used in place of Cu–Be |
| Na$_2$O–B$_2$O$_3$–SiO$_2$ glass | Liquid–liquid immiscibility | Vycor process: leach the borate phase, sinter the silica network into near-pure silica glass |
| Polymer blends | Upper or lower critical solution temperatures | Phase-separated toughened plastics, blend compatibility (Ch 20) |
| Au–Ni, Au–Pt | Solid-solution gap | Ageing of braze joints and thermocouple alloys |

---

## 6.5 Sublattice and compound-energy models; ordering

### Why a single-lattice model is not enough

The regular solution places all atoms on one set of equivalent sites. Many important phases do not work that way. In austenite, iron occupies the FCC sites while carbon occupies some of the octahedral interstices, a second set of sites. In an ionic oxide, cations and anions live on separate sublattices, and vacancies may sit on either. In an ordered intermetallic such as Ni$_3$Al, nickel prefers the face-centre sites and aluminium the corners, but with some interchange. The **sublattice model** treats each set of sites separately.

A phase is described by a formula such as $(\mathrm{Fe})_1(\mathrm{C},\mathrm{Va})_1$ for austenite (iron on the metal sublattice; carbon or vacancy on the interstitial sublattice, one per metal atom) or $(\mathrm{Ni},\mathrm{Al})_3(\mathrm{Al},\mathrm{Ni})_1$ for γ′. Compositions are expressed as **site fractions** $y_i^{(s)}$, the fraction of sites on sublattice $s$ occupied by species $i$. Mixing is assumed random within each sublattice, so the configurational entropy is a sum over sublattices:

$$
S_{\mathrm{conf}}=-R\sum_s a_s\sum_i y_i^{(s)}\ln y_i^{(s)}
$$

where $a_s$ is the number of sites of sublattice $s$ per formula unit.

### The compound-energy formalism

For a two-sublattice phase $(A,B)_a(C,D)_c$, the reference Gibbs energy is a weighted average over the four "end-member compounds" AC, AD, BC, BD that result from filling each sublattice with one species:

$$
G=\sum_{i,j}y_i^{(1)}y_j^{(2)}\,G_{i:j}^\circ-TS_{\mathrm{conf}}+G^{\mathrm{ex}}
$$

This **compound-energy formalism** is the workhorse of CALPHAD databases. It handles interstitial solutions (the end member $\mathrm{Fe{:}Va}$ is pure iron and $\mathrm{Fe{:}C}$ a hypothetical "FeC" with every interstice filled), ionic phases with charged species and vacancies (where only charge-neutral combinations are physically accessible), and ordered intermetallics within one consistent framework. A practical consequence of the interstitial description is that the configurational entropy of carbon in austenite is counted per interstitial site, so the carbon activity rises steeply as the site fraction approaches saturation; this is why furnace carbon potentials must be controlled carefully near the Acm line in carburizing (Chapter 15).

> **Status of the principle: compound-energy formalism**
> *Approximate.* It assumes random mixing within each sublattice, with short-range order absorbed into fitted excess terms; it is highly successful for interstitial, ionic and ordered phases and is the standard model in thermodynamic databases.

### Ordering

When $\Omega<0$, unlike neighbours are favoured, and at low temperature the atoms arrange themselves into an **ordered** structure in which A and B occupy distinct sublattices: CuZn (β-brass, B2), Cu$_3$Au and Ni$_3$Al (L1$_2$), FeCo (B2), TiAl (L1$_0$). Order is measured by the **long-range order parameter** $\eta$, which is 1 for perfect order and 0 for random occupation of the two sublattices. In the simplest mean-field (Bragg–Williams) treatment of an equiatomic B2 alloy, the sublattice occupations are $y_A^{(1)}=\tfrac12(1+\eta)$ and $y_A^{(2)}=\tfrac12(1-\eta)$, and minimising $G$ with respect to $\eta$ gives the self-consistent condition

$$
\eta=\tanh\!\left(\frac{T_c}{T}\,\eta\right)
$$

where $T_c$ is proportional to the ordering energy. Below $T_c$ there is a non-zero solution; $\eta$ falls continuously to zero at $T_c$ — a second-order (continuous) transition, with no latent heat but a peak in heat capacity. Solving numerically: $\eta=0.96$ at $T/T_c=0.5$, 0.71 at 0.8, 0.53 at 0.9 and 0.17 at 0.99.

> **Status of the principle: Bragg–Williams model of ordering**
> *Approximate.* A mean-field theory that ignores correlations between neighbouring sites; it predicts the existence and continuous character of B2 ordering correctly but overestimates $T_c$ and gives the wrong shape of $\eta(T)$ close to $T_c$, and it wrongly predicts continuous ordering for L1$_2$ structures, which in fact order discontinuously.

Ordered phases are central to high-temperature engineering. In β-brass, ordering at about 460 °C is detected by the superlattice reflections of Chapter 4. Ni$_3$Al remains ordered almost to its melting point, so a dislocation crossing it must create an **antiphase boundary** (Chapter 3); this is why γ′ precipitates strengthen superalloys up to about 1000 °C (Chapters 13 and 16). FeCo alloys order near 730 °C and become brittle, which limits their use in high-saturation electrical machines unless vanadium is added. Long-range order also changes physical properties: the electrical resistivity of Cu$_3$Au drops sharply when it orders, because the periodic arrangement no longer scatters electrons.

---

## 6.6 Surfaces and interfaces

### Surface energy

Atoms at a surface have lost some of their neighbours. The excess free energy per unit area, the **surface energy** $\gamma$ (J m$^{-2}$, numerically equal to the surface tension in N m$^{-1}$ for liquids), is the work needed to create new surface reversibly. A broken-bond estimate is instructive. In copper each atom has 12 nearest neighbours, and the enthalpy of sublimation, 337 kJ mol$^{-1}$, breaks all of them (each bond shared by two atoms). An atom in a $\{111\}$ surface has lost 3 of its 12 bonds, so it carries an excess energy of $\tfrac3{12}\times337\ \mathrm{kJ\,mol^{-1}}/N_A=9.3\times10^{-20}$ J. With $1.77\times10^{19}$ atoms m$^{-2}$ on that plane,

$$
\gamma_{\{111\}}\approx0.25\times5.60\times10^{-19}\ \mathrm{J}\times1.77\times10^{19}\ \mathrm{m^{-2}}=2.5\ \mathrm{J\,m^{-2}}
$$

The measured average for solid copper is about 1.8 J m$^{-2}$. The estimate is 35 % high, because real bonds are not pairwise and surface atoms relax, but it explains the trends: surface energy scales with cohesive energy, close-packed planes have the lowest $\gamma$ (and dominate equilibrium crystal shapes), and surfaces of refractory metals are high-energy while those of polymers are low.

| Material | Surface energy (J m$^{-2}$, typical) |
|---|---|
| Tungsten (solid) | about 2.8–3.3 |
| Iron (solid) | about 2.4 |
| Copper (solid) | about 1.8 |
| Aluminium (solid) | about 1.1 |
| Liquid iron at melting point | about 1.85 |
| Liquid copper | about 1.3 |
| Liquid aluminium | about 0.9 |
| Alumina (solid) | about 0.9–1.5 |
| Silica glass | about 0.3 |
| Water at 20 °C | 0.073 |
| Polyethylene | about 0.03 |
| PTFE | about 0.019 |
| High-angle grain boundary in Cu (for comparison) | about 0.6 |

> **Status of the principle: broken-bond estimate of surface energy**
> *Approximate.* It counts nearest-neighbour bonds only; it gives the right order of magnitude and correct trends with cohesive energy and plane packing, but overestimates real values by 20–50 % because bonding is not pairwise and surfaces relax and reconstruct.

### The Gibbs–Thomson effect

A curved interface raises the Gibbs energy of the material inside it. For a spherical particle of radius $r$, interface energy $\gamma$ and molar volume $V_m$, the extra pressure is $2\gamma/r$ (Laplace) and the chemical potential is raised by

$$
\Delta\mu=\frac{2\gamma V_m}{r}
$$

Two engineering consequences follow.

**Solubility of small particles.** A small precipitate is in equilibrium with a higher solute concentration in the surrounding matrix than a large one:

$$
c(r)=c_\infty\exp\!\left(\frac{2\gamma V_m}{rRT}\right)
$$

Solute therefore diffuses from small particles to large ones, and the large grow at the expense of the small. This **Ostwald ripening** coarsens precipitates in aged aluminium alloys, γ′ in superalloys during creep, carbides in tempered steels and catalyst particles in exhaust converters (Chapter 10).

**Melting-point depression.** For a solid particle of radius $r$ in its own melt, the melting point falls by

$$
\Delta T_m\approx\frac{2\gamma_{sl}\,T_m\,V_m}{\Delta H_f\,r}
$$

where $\gamma_{sl}$ is the solid–liquid interface energy. This is the basis of low-temperature sintering of nanoparticle inks and pastes (silver and copper for printed electronics and die attach) and of the size-dependent properties of nanomaterials (Chapter 30). It also sets the critical nucleus size in solidification (Chapter 9), which is the same equation solved for $r$.

> **Status of the principle: Gibbs–Thomson relation**
> *Derived.* It follows from the Laplace pressure of a curved interface and equality of chemical potential; valid when the radius is large compared with atomic dimensions (above roughly 2 nm) and $\gamma$ is independent of size and orientation, which fails for the smallest clusters and for strongly faceted particles.

**Worked example — Small precipitates and small solder particles.** (a) A precipitate in an aluminium alloy aged at 300 °C (573 K) has an interface energy of 0.2 J m$^{-2}$ and $V_m=1.0\times10^{-5}$ m$^3$ mol$^{-1}$. The exponent is $2\gamma V_m/(rRT)=4.0\times10^{-6}/(r\times4764)$. For $r=5$ nm it is 0.168, so $c(r)/c_\infty=e^{0.168}=1.18$: the matrix next to a 5 nm particle holds 18 % more solute in equilibrium than next to a very large one. For $r=2$ nm the factor is 1.52; for $r=20$ nm only 1.04. The large concentration differences around the smallest particles are why coarsening is fast at first and then slows (Chapter 10).

(b) Tin nanoparticles have been proposed for low-temperature solder pastes. With $\gamma_{sl}\approx0.06$ J m$^{-2}$, $T_m=505$ K, $V_m=16.3\times10^{-6}$ m$^3$ mol$^{-1}$ and $\Delta H_f=7.03$ kJ mol$^{-1}$:

$$
\Delta T_m=\frac{2\times0.06\times505\times16.3\times10^{-6}}{7030\times r}=\frac{1.41\times10^{-10}\ \mathrm{K\,m}}{r}
$$

For $r=10$ nm, $\Delta T_m=14$ K; for $r=5$ nm, 28 K; for $r=50$ nm, under 3 K. Useful depression needs particles below about 10 nm in radius, which are difficult to keep from oxidising and agglomerating — the reason such pastes remain niche.

### Wetting and Young's equation

When a liquid drop rests on a solid, three interfaces meet at the contact line: solid–vapour ($\gamma_{sv}$), solid–liquid ($\gamma_{sl}$) and liquid–vapour ($\gamma_{lv}$). Balancing their tensions parallel to the solid surface gives **Young's equation** for the equilibrium contact angle $\theta$:

$$
\gamma_{sv}=\gamma_{sl}+\gamma_{lv}\cos\theta
$$

A contact angle below 90° means the liquid **wets** the solid; $\theta\to0$ means it spreads, which requires the spreading coefficient $S=\gamma_{sv}-\gamma_{sl}-\gamma_{lv}$ to be non-negative. Wetting decides whether solder or braze flows into a joint (Sn–Ag–Cu on clean copper, $\theta\approx20$–$40^\circ$; on oxidised copper, no wetting at all — hence fluxes and reducing atmospheres), whether a liquid metal infiltrates a ceramic preform to make a metal-matrix composite (aluminium on alumina is non-wetting below about 900 °C), whether paints, adhesives and coatings adhere (Chapter 37), and whether a surface is self-cleaning (water on PTFE or textured surfaces, $\theta>110^\circ$).

> **Status of the principle: Young's equation**
> *Derived.* It follows from minimising total interfacial energy at fixed liquid volume; exact for an ideal, smooth, chemically homogeneous, non-reactive surface, and modified by roughness (Wenzel, Cassie–Baxter), contact-angle hysteresis and reaction at the interface, which in brazing and soldering usually dominates.

### Dihedral angles: where a second phase sits

The same force balance at a grain boundary meeting a second phase gives the **dihedral angle** $\phi$. Where a grain boundary of energy $\gamma_{gb}$ meets a liquid (or a second solid phase) with interface energy $\gamma_{sl}$,

$$
\gamma_{gb}=2\gamma_{sl}\cos\frac{\phi}{2}
$$

If $\gamma_{gb}/\gamma_{sl}=1$, $\phi=120^\circ$ and the liquid forms isolated pockets at triple junctions. If the ratio is 1.8, $\phi=52^\circ$ and the liquid forms channels along triple lines. If $\gamma_{gb}\ge2\gamma_{sl}$, $\phi=0$ and the liquid penetrates every boundary as a continuous film. This single ratio controls the microstructure of liquid-phase-sintered ceramics and hard metals (WC–Co, silicon nitride), the high-temperature strength of materials with grain-boundary glass, and the catastrophic **liquid-metal embrittlement** of aluminium by gallium, of steels by zinc during galvanizing and welding, and of nickel alloys by bismuth or lead.

<!-- FIGURE 6.4 | figures/ch06/fig-6-4-interfaces-wetting.png | schematic | Interface thermodynamics: Young's contact angle, the dihedral angle at a grain boundary, and the Gibbs–Thomson rise of solubility around small particles. | Content: panel (a) liquid drop on a solid with tension vectors γ_sv, γ_sl, γ_lv at the contact line, θ = 30° labelled "wetting (solder on clean Cu)" and a second drop with θ = 120° labelled "non-wetting (water on PTFE)". Panel (b) grain-boundary groove/triple junction with liquid: three sketches for γ_gb/γ_sl = 1.0 (φ = 120°, isolated pockets), 1.8 (φ = 52°, channels), ≥ 2 (φ = 0, film penetrating boundary, labelled "liquid-metal embrittlement"). Panel (c) plot of c(r)/c∞ = exp(2γV_m/rRT) vs r from 1 to 30 nm for γ = 0.2 J m⁻², V_m = 1.0×10⁻⁵ m³ mol⁻¹, T = 573 K; points marked at r = 2 nm (1.52), 5 nm (1.18), 20 nm (1.04); second axis or inset curve ΔT_m vs r for Sn: 1.41×10⁻¹⁰/r K (28 K at 5 nm, 14 K at 10 nm). -->

---

## 6.7 Thermodynamics of point defects

### Vacancies as a component with a chemical potential

Chapter 5 used the equilibrium vacancy fraction; here is where it comes from. Introduce $n$ vacancies into a crystal of $N$ atoms. Each costs an enthalpy $\Delta H_v$ and adds a vibrational entropy $\Delta S_v$ (the atoms around a vacancy vibrate at lower frequencies). The configurational entropy is $k_B\ln\{(N+n)!/(N!\,n!)\}$. The Gibbs energy change is

$$
\Delta G=n\,(\Delta H_v-T\Delta S_v)-k_BT\ln\frac{(N+n)!}{N!\,n!}
$$

Using Stirling's approximation and setting $\partial\Delta G/\partial n=0$ gives

$$
\frac{n}{N+n}=c_v=\exp\!\left(\frac{\Delta S_v}{k_B}\right)\exp\!\left(-\frac{\Delta H_v}{k_BT}\right)
$$

An equivalent and more general view treats vacancies as a component with a chemical potential,

$$
\mu_v=\Delta G_v+k_BT\ln\frac{c_v}{1-c_v}
$$

Vacancies can be created and destroyed at sources and sinks (surfaces, grain boundaries, dislocations by climb), so at equilibrium no free energy is gained by creating more: $\mu_v=0$, which reproduces the result. The formulation pays off away from equilibrium. A crystal quenched from high temperature holds a vacancy supersaturation with $\mu_v>0$, which drives vacancies to sinks, makes dislocations climb and condenses vacancies into loops and voids. Under irradiation, both vacancies and interstitials are supersaturated, and their chemical potentials drive swelling (Chapter 33). Under creep stress, the vacancy chemical potential differs between boundaries in tension and compression, which drives diffusional creep (Chapter 14).

> **Status of the principle: equilibrium vacancy concentration from minimum $G$**
> *Derived.* Exact for dilute, non-interacting vacancies with a well-defined formation free energy; corrections are needed for divacancies near the melting point, for interactions with solutes, and in compounds where the vacancy chemical potential depends on the chemical potentials of the components.

### Defect equilibria in compounds: the law of mass action

In an ionic compound, defects are created by reactions that also exchange atoms with the environment, and their concentrations are linked to the activities (partial pressures) of those atoms. Consider an oxide MO with oxygen vacancies, compensating electrons and holes. Two equilibria and one neutrality condition fix the defect populations:

$$
\mathrm{O_O^\times}\;\rightleftharpoons\;\mathrm{V_O^{\bullet\bullet}}+2e'+\tfrac12\mathrm{O_2}\qquad K_R=[\mathrm{V_O^{\bullet\bullet}}]\,n^2\,p_{\mathrm{O_2}}^{1/2}
$$

$$
\mathrm{null}\;\rightleftharpoons\;e'+h^\bullet\qquad K_i=np
$$

and, if the oxide is doped with an acceptor $A'$ (Y$'_{\mathrm{Zr}}$ in zirconia, Gd$'_{\mathrm{Ce}}$ in ceria, Mg$'_{\mathrm{Al}}$ in alumina), electroneutrality

$$
2[\mathrm{V_O^{\bullet\bullet}}]+p=n+[A']
$$

Each mass-action constant is an exponential of the standard Gibbs energy of its reaction, $K=\exp(-\Delta G^\circ/RT)$, which is how defect formation energies enter. Solving the set in limiting regions, where one pair of defects dominates the neutrality condition, gives power laws in oxygen partial pressure:

| Region | Neutrality approximation | Dependences |
|---|---|---|
| Strongly reducing | $n\approx2[\mathrm{V_O^{\bullet\bullet}}]$ | $n$ and $[\mathrm{V_O^{\bullet\bullet}}]\propto p_{\mathrm{O_2}}^{-1/6}$ |
| Intermediate, acceptor-doped | $2[\mathrm{V_O^{\bullet\bullet}}]\approx[A']$ | $[\mathrm{V_O^{\bullet\bullet}}]$ constant; $n\propto p_{\mathrm{O_2}}^{-1/4}$; $p\propto p_{\mathrm{O_2}}^{+1/4}$ |
| Strongly oxidizing | $p\approx[A']$ (holes compensate the acceptor) | $p$ constant; $[\mathrm{V_O^{\bullet\bullet}}]\propto p_{\mathrm{O_2}}^{-1/2}$ |

A log–log plot of defect concentrations against $p_{\mathrm{O_2}}$, built from these straight-line segments, is a **Brouwer diagram** (Figure 6.5). It is the map engineers use to choose operating windows for oxide materials. A YSZ electrolyte must work in the middle region, where the vacancy concentration (and so the ionic conductivity) is fixed by doping and electronic conduction is negligible, across the oxygen pressures between air and fuel ($10^{-21}$ to 0.21 atm at 800 °C). A ceria-based anode or catalyst is used precisely because it enters the reducing region easily and becomes a mixed conductor. A capacitor dielectric fired in a reducing atmosphere sits on the $-1/4$ or $-1/6$ line and becomes semiconducting unless acceptors are added. A UO$_2$ fuel pellet's oxygen-to-metal ratio, set by the oxygen potential during sintering and changed by fission, controls its thermal conductivity and creep.

<!-- FIGURE 6.5 | figures/ch06/fig-6-5-brouwer-diagram.png | plot | Brouwer diagram for an acceptor-doped oxide: defect concentrations versus oxygen partial pressure, built from mass-action laws and limiting neutrality conditions. | Content: x-axis log10 pO2 (atm) from −30 to +5; y-axis log10 concentration (arbitrary, spanning ~10 decades). Three regions separated by dashed vertical lines and labelled: I "n = 2[V_O••]" (left), II "2[V_O••] = [A′]" (middle, widest), III "p = [A′]" (right). Lines: [V_O••] slope −1/6 in I, flat in II, slope −1/2 in III; n slope −1/6 in I, −1/4 in II, −1/2 in III; p slope +1/6 in I, +1/4 in II, flat in III; [A′] horizontal dotted line. Shaded band in region II from pO2 = 10⁻²¹ to 0.21 atm labelled "SOFC electrolyte window (YSZ, 800 °C)". Annotate total conductivity curve on a secondary axis showing a flat ionic plateau in II with rising n-type (left) and p-type (right) branches. -->

> **Status of the principle: mass-action treatment of defect equilibria**
> *Approximate.* Exact thermodynamics for dilute, non-interacting defects with ideal (concentration-based) activities; it fails at high defect concentrations (above roughly 1 %), where defects associate into clusters and the simple power laws bend, as in heavily doped YSZ and strongly reduced ceria.

---

## 6.8 Ellingham diagrams for oxidation and reduction

### The diagram

Whether a metal oxidises or its oxide can be reduced depends on the standard Gibbs energy of the oxidation reaction. To compare metals fairly, each reaction is written per mole of O$_2$:

$$
\tfrac{2x}{y}\mathrm{M}+\mathrm{O_2}\;\rightarrow\;\tfrac{2}{y}\mathrm{M}_x\mathrm{O}_y,\qquad \Delta G^\circ=\Delta H^\circ-T\Delta S^\circ
$$

Over temperature ranges without phase changes, $\Delta H^\circ$ and $\Delta S^\circ$ are nearly constant, so $\Delta G^\circ$ is close to a straight line in $T$. Harold Ellingham plotted these lines for many oxides on one chart in 1944 (Figure 6.6). Its features follow from simple thermodynamics.

- **Slopes.** The slope is $-\Delta S^\circ$. Forming a solid oxide from a solid metal consumes a mole of gas, so $\Delta S^\circ\approx-$ (entropy of O$_2$) and almost all metal lines rise with roughly the same slope, about $+0.17$–$0.21$ kJ mol$^{-1}$ K$^{-1}$. Kinks appear where the metal or oxide melts or boils (boiling of magnesium at 1090 °C steepens its line markedly).
- **Carbon.** $2\mathrm C+\mathrm O_2\rightarrow2\mathrm{CO}$ *creates* a mole of gas, so its line *falls* with temperature. $\mathrm C+\mathrm O_2\rightarrow\mathrm{CO_2}$ conserves gas moles and is nearly flat. This is why carbon becomes a stronger reducing agent the hotter it gets — the foundation of iron- and steelmaking.
- **Position.** The lower a line, the more stable the oxide. Any metal can reduce the oxide of any metal whose line lies above its own at that temperature: aluminium reduces chromium oxide (the aluminothermic process), magnesium reduces titanium tetrachloride (the related chloride chart underlies the Kroll process for titanium sponge).
- **Equilibrium oxygen pressure.** With pure metal and oxide (activities 1), the reaction is at equilibrium when $\Delta G^\circ=RT\ln p_{\mathrm{O_2}}$. Each line therefore also gives the oxygen partial pressure below which the oxide is reduced; nomographic scales of $p_{\mathrm{O_2}}$, $\mathrm{H_2/H_2O}$ and $\mathrm{CO/CO_2}$ ratios are printed around the edge of the chart.

> **Status of the principle: Ellingham diagram**
> *Derived* from reaction thermodynamics ($\Delta G^\circ=-RT\ln K$) with *approximate* linear fits for $\Delta G^\circ(T)$. It assumes pure condensed phases at unit activity and says nothing about rates: aluminium, chromium and silicon are thermodynamically far less noble than iron, yet resist oxidation better because their thin oxide films are protective (Chapter 34).

Representative linear fits (typical handbook values, per mole of O$_2$, valid over roughly 300–1500 K between phase changes):

| Reaction (per mol O$_2$) | $\Delta G^\circ$ (kJ mol$^{-1}$) | $\Delta G^\circ$ at 1000 K | $p_{\mathrm{O_2}}$ at 1000 K (atm) |
|---|---|---|---|
| $4\mathrm{Cu}+\mathrm O_2\rightarrow2\mathrm{Cu_2O}$ | $-337+0.140\,T$ | $-197$ | $5\times10^{-11}$ |
| $2\mathrm{Ni}+\mathrm O_2\rightarrow2\mathrm{NiO}$ | $-471+0.172\,T$ | $-299$ | $2\times10^{-16}$ |
| $2\mathrm{Fe}+\mathrm O_2\rightarrow2\mathrm{FeO}$ | $-519+0.125\,T$ | $-394$ | $3\times10^{-21}$ |
| $2\mathrm H_2+\mathrm O_2\rightarrow2\mathrm H_2\mathrm O(\mathrm g)$ | $-493+0.109\,T$ | $-384$ | — |
| $2\mathrm C+\mathrm O_2\rightarrow2\mathrm{CO}$ | $-223-0.175\,T$ | $-399$ | — |
| $\mathrm C+\mathrm O_2\rightarrow\mathrm{CO_2}$ | $-394-0.001\,T$ | $-395$ | — |
| $\tfrac43\mathrm{Cr}+\mathrm O_2\rightarrow\tfrac23\mathrm{Cr_2O_3}$ | $-747+0.170\,T$ | $-577$ | $8\times10^{-31}$ |
| $\mathrm{Si}+\mathrm O_2\rightarrow\mathrm{SiO_2}$ | $-902+0.174\,T$ | $-728$ | $9\times10^{-39}$ |
| $\mathrm{Ti}+\mathrm O_2\rightarrow\mathrm{TiO_2}$ | $-941+0.178\,T$ | $-763$ | $1\times10^{-40}$ |
| $\tfrac43\mathrm{Al}+\mathrm O_2\rightarrow\tfrac23\mathrm{Al_2O_3}$ | $-1117+0.208\,T$ | $-909$ | $3\times10^{-48}$ |
| $2\mathrm{Mg}+\mathrm O_2\rightarrow2\mathrm{MgO}$ | $-1202+0.216\,T$ (below 1363 K) | $-986$ | $3\times10^{-52}$ |

<!-- FIGURE 6.6 | figures/ch06/fig-6-6-ellingham-diagram.png | plot | Ellingham diagram for selected oxides: standard Gibbs energy of oxidation per mole of O2 versus temperature, with the C/CO line falling across the metal lines. | Content: x-axis T from 0 to 2000 °C (273–2273 K); y-axis ΔG° (kJ per mol O2) from −1200 to 0. Lines from the table: Cu/Cu2O, Ni/NiO, Fe/FeO, H2/H2O, Cr/Cr2O3, Si/SiO2, Ti/TiO2, Al/Al2O3, Mg/MgO (with kink at Mg boiling 1090 °C), C/CO (falling, slope −0.175), C/CO2 (flat). Mark crossings of C/CO with Fe/FeO at ~712 °C, Cr/Cr2O3 at ~1240 °C, Si/SiO2 at ~1670 °C, Ti/TiO2 at ~1760 °C, and Al/Al2O3 at ~2050 °C. Right-hand nomographic scale of pO2 from 10⁻⁵⁰ to 1 atm with a pivot at the origin "O" (T = 0 K, ΔG = 0); construction line drawn from O through the Cr/Cr2O3 line at 1100 °C to read pO2 ≈ 3×10⁻²⁰ atm; similar H2/H2O scale with pivot "H". Shade region above Fe/FeO at 1000 K labelled "oxidizing to Fe". -->

### Reading the diagram

Three readings cover most uses.

**Smelting.** The C/CO line crosses the Fe/FeO line at

$$
-519.2+0.1251\,T=-223.4-0.1753\,T\quad\Rightarrow\quad T=\frac{295.8}{0.3004}=985\ \mathrm K\ (712\ ^\circ\mathrm C)
$$

Above this temperature, carbon at unit activity reduces FeO with CO as the product — the chemistry of the blast furnace. The C/CO line crosses Cr$_2$O$_3$ near 1240 °C, SiO$_2$ near 1670 °C, TiO$_2$ near 1760 °C and Al$_2$O$_3$ only above 2000 °C. Ferrochromium and silicon are therefore made by carbothermic reduction in electric-arc furnaces at very high temperature, while aluminium is too stable to reduce with carbon at practical temperatures (and forms carbides instead) and is produced by electrolysis of alumina dissolved in molten cryolite — one of the most energy-intensive processes in materials production (Chapter 49). Titanium, likewise, would form carbides and dissolve oxygen, so it is made via the chloride route.

**Protective atmospheres.** For heat treatment, brazing and sintering, the atmosphere must hold the oxygen potential below the line of the most reactive alloying element that must stay metallic. Gas mixtures fix the oxygen potential: in H$_2$/H$_2$O, the ratio $p_{\mathrm{H_2O}}/p_{\mathrm{H_2}}$ does; in CO/CO$_2$, the ratio $p_{\mathrm{CO_2}}/p_{\mathrm{CO}}$. Because water vapour content is measured as a **dew point**, furnace specifications are written as dew points.

**Oxidation resistance.** The metals whose lines lie lowest — Al, Si, Cr — form the most stable oxides, and if their oxides are dense and slow-growing they protect the metal underneath. Stainless steels (chromia formers), nickel superalloys and aluminide coatings (alumina formers), and silicon carbide and silicon nitride (silica formers) are designed around this principle. Selective oxidation also has a downside: in a steel or alloy heat-treated in an atmosphere that reduces iron oxide but not chromium, manganese or silicon oxides, those elements oxidise internally just below the surface, which affects galvanizing of advanced high-strength steels (Chapter 15).

**Worked example — Bright annealing of stainless steel.** Stainless tube is annealed at 1100 °C (1373 K) in hydrogen and must emerge without a chromium-oxide tint. What is the maximum allowable water vapour content?

The relevant reaction combines the Cr$_2$O$_3$ and H$_2$O lines (subtracting the first from the second):

$$
\tfrac23\mathrm{Cr_2O_3}+2\mathrm H_2\;\rightleftharpoons\;\tfrac43\mathrm{Cr}+2\mathrm H_2\mathrm O
$$

At 1373 K, $\Delta G^\circ_{\mathrm{Cr_2O_3}}=-746.8+0.1702\times1373=-513.1$ kJ and $\Delta G^\circ_{\mathrm H_2\mathrm O}=-492.9+0.1094\times1373=-342.7$ kJ per mole of O$_2$. The reduction reaction therefore has $\Delta G^\circ=-342.7-(-513.1)=+170.4$ kJ, and

$$
K=\frac{a_{\mathrm{Cr}}^{4/3}\,(p_{\mathrm{H_2O}}/p_{\mathrm{H_2}})^2}{1}=\exp\!\left(-\frac{170\,400}{8.314\times1373}\right)=3.3\times10^{-7}
$$

For pure chromium ($a_{\mathrm{Cr}}=1$, pure Cr$_2$O$_3$), the threshold is $p_{\mathrm{H_2O}}/p_{\mathrm{H_2}}=\sqrt{3.3\times10^{-7}}=5.7\times10^{-4}$. In 1 atm of hydrogen the water partial pressure must then stay below $5.7\times10^{-4}\times101\,325=58$ Pa, a dew point of about $-26$ °C.

In a stainless steel with about 18 % Cr, the chromium activity is roughly 0.2. Since $(p_{\mathrm{H_2O}}/p_{\mathrm{H_2}})^2=K/a_{\mathrm{Cr}}^{4/3}$ at equilibrium, diluting the chromium *raises* the tolerable ratio by $0.2^{-2/3}=2.9$, to $1.7\times10^{-3}$ (170 Pa, dew point about $-15$ °C). Industrial lines nevertheless specify dew points of $-40$ °C or lower, for three reasons that the same diagram explains: silicon and manganese in the steel form oxides more stable than Cr$_2$O$_3$; the threshold ratio falls steeply with temperature — at 800 °C it is only $2.6\times10^{-5}$ for pure chromium and tubes discolour if they cool slowly through the cooler zones of the furnace; and a margin is needed for leaks and moisture released from the charge.

The same chart answers related questions in other fields: the CO/CO$_2$ ratio needed to sinter iron powder compacts without oxidation, the oxygen pressure at which nickel anodes of solid-oxide fuel cells oxidise (about $5\times10^{-11}$ atm at 1000 °C, from the Ni/NiO line), why copper can be brazed in mildly reducing "exothermic" gas while titanium must be brazed in high vacuum, and why silicon wafers can be oxidised in steam while their metal contacts are protected.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are free-energy curves turned into complete binary and ternary phase diagrams, and how does CALPHAD compute them? | Chapter 7 |
| How fast do atoms move down chemical-potential gradients, including uphill diffusion? | Chapter 8 |
| How does the driving force from a common tangent translate into nucleation rates and growth? | Chapter 9 |
| How does spinodal decomposition develop in time (Cahn–Hilliard), and how does Ostwald ripening proceed (LSW)? | Chapter 10 |
| How do surface energy, adhesion and wetting control friction, coatings and joining? | Chapters 37 and 39 |
| How do defect equilibria set ionic and electronic conductivity in ceramics? | Chapters 25 and 32 |
| How do oxide scales grow, and why do some protect while others do not? | Chapter 34 |
| How are Gibbs energies of solid phases calculated from first principles and stored in databases? | Chapters 45, 46 and 47 |
| What is the environmental cost of the high-temperature reductions read from the Ellingham diagram? | Chapter 49 |

**Next:** Chapter 7 uses free-energy curves and the phase rule to build and read the phase diagrams on which alloy and process design depend.
