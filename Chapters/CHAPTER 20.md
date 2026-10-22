# Chapter 20 — Polymer Physics and Morphology

*Part V · Polymers and Composites*

A manufacturer of disposable medical syringes switches from one isotactic polypropylene grade to another with the same melt flow index and the same nominal density, to save cost. The syringes mould perfectly. Six weeks later the hospital returns cartons in which the barrels have turned cloudy and a few have cracked at the luer tip after gamma sterilization. Nothing about the chemistry has changed; what has changed is the morphology. The new grade lacked the nucleating agent of the old one, so it crystallized into large spherulites that scatter light, and it had a lower fraction of the chain segments that bridge neighbouring crystals, so the radiation-induced chain scission broke more of the few connections that held the crystals together. In the same hospital, a nurse finds that a silicone catheter has become sticky after weeks in contact with a lipid emulsion: the oil has dissolved into the rubber network and swollen it. Both problems are questions of polymer physics, not chemistry: how chains are arranged, how they mix with other molecules, and how they pack into crystals and glasses.

Chapter 19 described how chains are made. This chapter treats what the chains then do: how a single chain coils, why a network of coils is a rubber, when two polymers or a polymer and a solvent mix, how chains fold into crystals, and why, below a characteristic temperature, the whole assembly freezes into a glass.

> **What shape does a long, flexible chain adopt, and why does a network of such chains resist stretching?**
> **What decides whether a polymer mixes, crystallizes or vitrifies, and how do these states set the stiffness and temperature range of a plastic part?**

| Concept | Engineering destination |
|---|---|
| Random-walk chain, Kuhn length, end-to-end distance | Coil size in solutions and melts, membrane pores, entanglement, light scattering |
| Entropic rubber elasticity | Seals, tyres, bearings, vibration mounts, rubber springs in civil base isolation |
| Flory–Huggins theory and theta conditions | Solvent selection, paint and adhesive formulation, swelling of seals in fuels and oils |
| Blend miscibility | Toughened plastics, Noryl housings, recycled mixed-plastic streams |
| Block-copolymer microphase separation | Thermoplastic elastomers, nanolithography, drug-delivery micelles |
| Crystallization and crystallinity | Stiffness and creep of HDPE pipe, clarity of PP, barrier of PET bottles |
| Glass transition, WLF | Upper service temperature of amorphous plastics, brittleness at low temperature, damping |
| Liquid-crystalline polymers | Aramid fibres for armour and ropes, thin-wall connectors, low-CTE substrates |

**Roadmap.** Chain statistics (20.1) → entropic elasticity of networks (20.2) → mixing with solvents (20.3) and with other polymers, including block copolymers (20.4) → crystallization and morphology (20.5) → the glass transition (20.6) → rigid chains that form liquid crystals (20.7).

---

## 20.1 Chain conformations

### Rotational isomers and flexibility

A polyethylene backbone is a chain of carbon atoms joined by bonds of length $l=0.154$ nm at a fixed valence angle of about 109.5°. The bond lengths and angles are stiff, but rotation about each C–C bond is relatively easy. Looking along a bond, the substituents on adjacent carbons can sit in a **trans** position (energy minimum) or in one of two **gauche** positions (about 2–3 kJ/mol higher), separated by barriers of roughly 12–15 kJ/mol. Since $RT\approx2.5$ kJ/mol at room temperature, a polyethylene chain in a melt switches between rotational states roughly $10^{10}$ times per second, and each bond is gauche about a third of the time. A chain of 7,000 bonds therefore has an astronomical number of shapes available, and in a melt or solution it continually explores them. This conformational freedom, not any special chemistry, is the origin of rubber elasticity, of the high viscosity of melts and of the glass transition.

The flexibility of a chain depends on the rotation barrier and on the bulk of the side groups. Polydimethylsiloxane, with long Si–O bonds and a wide Si–O–Si angle, is extremely flexible; polystyrene, with a phenyl ring on every second carbon, is stiffer; a chain of para-linked aromatic rings (Kevlar) is essentially a rigid rod (Section 20.7).

### The freely jointed chain

The simplest model replaces the real chain by $n$ links of length $l$, each pointing in a direction completely independent of the others — a three-dimensional random walk. The end-to-end vector is $\mathbf R=\sum_i\mathbf l_i$, and because cross terms $\langle\mathbf l_i\cdot\mathbf l_j\rangle$ vanish for independent links,

$$
\langle R^2\rangle_0 = n\,l^2
$$

The root-mean-square end-to-end distance grows only as the square root of the chain length, whereas the fully stretched **contour length** grows linearly. For large $n$, the central-limit theorem makes the probability density of $\mathbf R$ Gaussian:

$$
P(\mathbf R)=\left(\frac{3}{2\pi\langle R^2\rangle_0}\right)^{3/2}\exp\!\left(-\frac{3R^2}{2\langle R^2\rangle_0}\right)
$$

The **radius of gyration**, the root-mean-square distance of the segments from the centre of mass, is the quantity measured by light and neutron scattering; for a Gaussian coil $\langle R_g^2\rangle=\langle R^2\rangle_0/6$.

### Real chains: characteristic ratio and Kuhn length

Real bonds are not freely jointed. Fixed valence angles and the preference for trans states make successive bonds point in correlated directions, and the coil is larger than the freely jointed estimate. The correlations nonetheless die out after a few bonds, so a long real chain is still a random walk on large scales, only with a larger step. Two equivalent descriptions are used:

- The **characteristic ratio** $C_\infty$ defined by $\langle R^2\rangle_0=C_\infty\,n\,l^2$ for large $n$.
- The **Kuhn model**: the real chain is replaced by an equivalent freely jointed chain of $N_K$ segments of **Kuhn length** $b$, chosen so that it has the same contour length $R_{max}=N_Kb$ and the same mean-square end-to-end distance $\langle R^2\rangle_0=N_Kb^2$. Then $b=\langle R^2\rangle_0/R_{max}$.

> **Status of the principle: Gaussian random-walk statistics of chains**
> *Derived.* Follows from the central-limit theorem for any chain whose orientational correlations decay over a finite distance; it holds in melts and in theta solvents (where excluded-volume effects cancel) and fails for short or rigid chains and at large extensions approaching the contour length.

| Polymer | $C_\infty$ (typical) | Kuhn length $b$ (nm, typical) | Comment |
|---|---|---|---|
| Polydimethylsiloxane | 5.2–6.3 | 1.1–1.3 | Very flexible; Tg about −125 °C |
| Polyethylene | 6.7–7.4 | 1.3–1.5 | Flexible; reference polymer |
| Isotactic polypropylene | 5.7–6.2 | 1.1–1.3 | Helical in crystal |
| Poly(ethylene oxide) | 4.0–5.6 | 0.9–1.1 | Water-soluble |
| Polystyrene (atactic) | 9.5–10 | 1.6–1.8 | Bulky phenyl side group |
| PMMA (atactic) | 8–9 | 1.5–1.7 | Stiffer, Tg about 105 °C |
| Polycarbonate | 2.4 (per repeat-unit "virtual bond") | about 1.4 | Aromatic backbone with flexible links |
| DNA (double helix) | — | about 100 | Semi-flexible, persistence length 50 nm |
| Kevlar (PPTA) | — | more than 30 | Rigid rod; forms liquid crystals |

<!-- FIGURE 20.1 | figures/ch20/fig-20-1-random-walk-chain.png | schematic | A polyethylene chain as a three-dimensional random walk, with its end-to-end vector, radius of gyration and the equivalent Kuhn chain. | Content: left panel: 2D projection of a simulated random walk of 700 steps (representing 7130 bonds grouped into Kuhn segments of 1.26 nm), coloured from blue (start) to red (end); arrow for end-to-end vector R labelled "√⟨R²⟩ ≈ 34 nm"; dashed circle of radius Rg ≈ 14 nm around the centre of mass. Right panel: short section of the real zig-zag backbone (bond 0.154 nm, angle 109.5°, trans and gauche states marked) overlaid with the straight Kuhn segments of length b. Scale bar 10 nm. Note "contour length 897 nm". -->

**Worked example — size of a polyethylene coil.** A polyethylene chain of $M=100{,}000$ g/mol contains $2M/28.05=7{,}130$ backbone C–C bonds. As a freely jointed chain it would have $\sqrt{\langle R^2\rangle}=\sqrt{7130}\times0.154=13.0$ nm. With $C_\infty=6.7$, $\langle R^2\rangle_0=6.7\times7130\times0.154^2=1133$ nm², so $\sqrt{\langle R^2\rangle_0}=33.7$ nm and $R_g=33.7/\sqrt6=13.7$ nm. The fully extended all-trans zig-zag has contour length $R_{max}=nl\cos(35.25^\circ)=7130\times0.154\times0.817=897$ nm. The Kuhn length is $b=1133/897=1.26$ nm and the chain contains $N_K=897/1.26\approx710$ Kuhn segments. Three conclusions follow. First, the coil is 27 times shorter end to end than the stretched chain, so the molecule can be extended enormously before its bonds are loaded — the basis of the large strains of rubbers and of fibre drawing. Second, the coil occupies a volume of order $R_g^3\approx2.6\times10^3$ nm³, while the chain's own atoms fill only $M/(\rho N_A)\approx195$ nm³ (melt density 0.85 g/cm³); so in a melt the pervaded volume of each coil is shared with roughly a dozen other chains. This interpenetration is what makes entanglement (Chapter 21) unavoidable. Third, the coil size $R_g\approx14$ nm is comparable with the wavelength of X-rays scattered at small angles and of neutrons, which is how such numbers are measured.

### Excluded volume and solvent quality

A random walk can cross itself; a real chain cannot, since two segments cannot occupy the same space. In a good solvent, where segments prefer solvent contacts to each other, this **excluded volume** swells the coil, and Flory's argument gives $R\propto N^{\nu}$ with $\nu\approx3/5$ (more precisely 0.588) instead of 1/2. In a poor solvent the segments attract and the coil contracts. At one temperature, the **theta temperature**, the attraction exactly cancels the excluded volume and the chain is ideal again (Section 20.3). In a melt, a chain is surrounded by other chains of the same kind; the excluded-volume interactions are screened, and the chain is ideal with $\nu=1/2$ — Flory's theorem, confirmed by neutron scattering on deuterium-labelled chains in the 1970s.

---

## 20.2 Rubber elasticity derived from entropy

### The puzzle

Stretch a rubber band rapidly and hold it against your lip: it warms up. Hang a weight on a rubber strip and heat the strip: it contracts and lifts the weight. Both behaviours are the opposite of what a metal spring does, and both follow from a single fact: the restoring force of a rubber comes from entropy, not from stretching bonds.

### Entropy of a single chain

The number of conformations available to a chain whose ends are held a vector $\mathbf R$ apart is proportional to $P(\mathbf R)$. By Boltzmann's relation $S=k\ln\Omega$, the conformational entropy of the chain is

$$
S(\mathbf R)=S_0-\frac{3kR^2}{2\langle R^2\rangle_0}
$$

Pulling the ends apart reduces the number of available conformations and lowers the entropy. If the internal energy does not depend on $R$ (an ideal chain whose rotational states have equal energies), the Helmholtz free energy is $A=-TS$, and the force required to hold the ends apart is

$$
f=\frac{\partial A}{\partial R}=\frac{3kT}{\langle R^2\rangle_0}\,R
$$

The chain is a linear spring whose stiffness is proportional to absolute temperature: an **entropic spring**. For the polyethylene coil of the worked example, $3kT/\langle R^2\rangle_0=3\times4.11\times10^{-21}/(1.133\times10^{-15})\approx1.1\times10^{-5}$ N/m at 25 °C — tens of millions of times softer than the stretching stiffness of a C–C bond (several hundred N/m).

### From chains to a network

A rubber is a network of such chains joined at crosslinks (Chapter 19). The **affine network model** assumes that the crosslinks move with the macroscopic deformation, so that every chain end-to-end vector is stretched in the same proportion as the sample, and that the network chains are Gaussian. For a deformation with principal stretch ratios $\lambda_1,\lambda_2,\lambda_3$ and $\nu$ network chains per unit volume, summing the entropy change over all chains gives the elastic free energy per unit volume

$$
W=\frac{G}{2}\left(\lambda_1^2+\lambda_2^2+\lambda_3^2-3\right),\qquad G=\nu kT=\frac{\rho RT}{M_c}
$$

where $\rho$ is the density and $M_c$ the molar mass between crosslinks. Rubbers are nearly incompressible (Poisson's ratio 0.4995), so in uniaxial tension $\lambda_1=\lambda$ and $\lambda_2=\lambda_3=\lambda^{-1/2}$, and the nominal (engineering) stress is

$$
\sigma=G\left(\lambda-\frac{1}{\lambda^2}\right)
$$

At small strain, $\lambda=1+\varepsilon$, this becomes $\sigma\approx3G\varepsilon$, so Young's modulus is $E=3G$.

> **Status of the principle: Entropic (Gaussian) rubber elasticity**
> *Derived.* Follows from Gaussian chain statistics and the affine assumption. It predicts the right modulus magnitude and its proportionality to $T$ and to $1/M_c$, but is quantitative only to within a factor of about two, and fails at large stretch (finite chain extensibility, strain-induced crystallization) and in moderate stretch where crosslinks fluctuate (the phantom network model gives $G=(1-2/\phi)\nu kT$ for junction functionality $\phi$).

Three predictions are worth emphasizing.

1. **The modulus of a rubber is tiny and set by crosslink density.** A typical $M_c$ of 5,000 g/mol gives $G$ of order 0.5 MPa, against 80 GPa for steel. This is the right order of magnitude for every vulcanized rubber, and it is why the modulus of a seal or a tyre compound is controlled by the sulfur dose (Chapter 21) and by reinforcing filler.
2. **The modulus increases with temperature.** At constant length, the force on a stretched rubber is proportional to $T$; heated, it contracts (the **Gough–Joule effect**). At small strains the effect is masked by ordinary thermal expansion (thermoelastic inversion near 10 % strain), but at larger strains it dominates.
3. **Stretching releases heat.** An adiabatic extension lowers the conformational entropy, and because total entropy cannot fall in an adiabatic reversible process, the vibrational entropy — and therefore the temperature — rises.

**Worked example — a natural-rubber bridge bearing.** Elastomeric bearings made of natural rubber (density 920 kg/m³) support bridge decks and isolate buildings from earthquakes. A compound with $M_c=5{,}000$ g/mol at 25 °C (298 K) has $G=\rho RT/M_c=920\times8.314\times298/5.0=4.56\times10^{5}$ Pa $=0.46$ MPa, and $E=3G=1.37$ MPa. Stretched to $\lambda=2$ (100 % strain), the predicted nominal stress is $\sigma=0.456\times(2-0.25)=0.80$ MPa. At 75 °C (348 K) the same compound has $G=0.53$ MPa, 17 % stiffer — the opposite of every metal and glassy polymer. The stored elastic energy at $\lambda=3$ is $W=\tfrac12G(9+\tfrac23-3)=1.52$ MJ/m³; if all of it appeared as heat in an adiabatic extension, with heat capacity 1,900 J/(kg·K), the temperature would rise by $1.52\times10^6/(920\times1900)=0.87$ K. The warming felt on the lip is larger, a few kelvin, because natural rubber crystallizes on stretching and releases latent heat — a reminder that the Gaussian model describes only the entropic part of the response. In bearing design the shear modulus is what matters ($G$ of 0.4–1.2 MPa is specified), with bonded steel shims stiffening the bearing in compression while leaving it soft in shear.

### Where the simple theory fails

Measured stress–strain curves of natural rubber (Figure 20.2) follow the Gaussian prediction up to about $\lambda=1.5$, then fall somewhat below it in the range $\lambda=1.5$–4 (crosslink junctions fluctuate and chains are not deformed affinely), and then rise steeply above $\lambda\approx5$. The upturn has two causes: the chains between crosslinks approach their contour length, where the Gaussian approximation fails (non-Gaussian Langevin statistics, used in the Arruda–Boyce model), and natural rubber crystallizes under strain, the crystals acting as additional stiff crosslinks. Strain crystallization also stops cracks from growing and explains why natural rubber, not synthetic SBR, is used in aircraft tyres and heavy truck tyres. Engineering finite-element codes describe rubber with hyperelastic strain-energy functions — neo-Hookean (the Gaussian result), Mooney–Rivlin, Ogden, Arruda–Boyce — fitted to tension, compression and shear tests.

> **Status of the principle: Mooney–Rivlin and other hyperelastic laws**
> *Empirical.* Phenomenological strain-energy functions with fitted constants; reliable within the strain range and deformation modes used for the fit and unreliable when extrapolated beyond it.

<!-- FIGURE 20.2 | figures/ch20/fig-20-2-rubber-stress-strain.png | plot | Nominal stress versus stretch ratio for a natural-rubber network compared with the Gaussian affine prediction. | Content: x-axis stretch ratio λ from 1 to 7; y-axis nominal stress σ from 0 to 8 MPa. Solid line: Gaussian theory σ = G(λ − 1/λ²) with G = 0.46 MPa (passing 0.80 MPa at λ = 2). Points: representative experimental NR curve (Treloar-type) following theory to λ ≈ 1.5, lying 10–25 % below between λ = 2 and 4, then turning sharply upward beyond λ ≈ 5 to about 7 MPa at λ = 6.5. Annotations: "crosslink fluctuations", "finite extensibility + strain crystallization". Inset: force at fixed λ = 3 versus temperature 0–100 °C, straight line through origin when extrapolated to 0 K (entropic). -->

---

## 20.3 Polymer solutions: Flory–Huggins theory and theta conditions

### Why polymers dissolve reluctantly

Polymers dissolve slowly and in few solvents. Polystyrene dissolves in toluene but not in hexane or ethanol; polyethylene dissolves in nothing at room temperature; cross-linked rubber only swells. The reason is entropic. When small molecules mix, each can occupy any site, and the entropy of mixing is large. When a polymer mixes, its segments are tied together, and the number of distinct arrangements is far smaller. Polymer mixing is therefore much more sensitive to unfavourable interactions than ordinary mixing.

### The Flory–Huggins lattice model

Flory and Huggins (1941–42) placed solvent molecules and polymer segments on a lattice of sites, each segment occupying one site of the same volume as a solvent molecule. For a mixture with polymer volume fraction $\phi$ and chains of $N$ segments, the free energy of mixing per lattice site is

$$
\frac{\Delta G_{mix}}{kT}=\frac{\phi}{N}\ln\phi+(1-\phi)\ln(1-\phi)+\chi\,\phi(1-\phi)
$$

The first two terms are the combinatorial entropy; the polymer term is divided by $N$ because a chain of $N$ segments moves as one unit. The third term is the interaction energy, governed by the dimensionless **Flory–Huggins parameter** $\chi$, which measures the energy cost, in units of $kT$, of replacing a segment–segment and a solvent–solvent contact by two segment–solvent contacts. In practice $\chi$ has an enthalpic part that falls as $1/T$ and an entropic part, $\chi=A+B/T$.

> **Status of the principle: Flory–Huggins free energy of mixing**
> *Approximate.* A mean-field lattice theory that assumes random mixing, equal segment and solvent volumes and no volume change on mixing; it captures phase separation, swelling and the role of chain length, but $\chi$ fitted to experiment depends on concentration and temperature, and the theory fails in dilute solution (where coils are isolated) and for strongly interacting systems such as hydrogen-bonding polymers in water.

The model makes several predictions that engineers use.

- **Phase separation.** For $\chi$ above a critical value the free-energy curve develops two minima and the solution splits into a polymer-rich and a solvent-rich phase (the common-tangent construction of Chapter 6). For a polymer in a solvent the critical point is at $\phi_c=1/(1+\sqrt N)$ and $\chi_c=\tfrac12(1+1/\sqrt N)^2$, which tends to $\tfrac12$ for long chains. The phase diagram has an upper critical solution temperature (UCST) that rises with molar mass, which is exploited in fractionation and in membrane formation by thermally induced phase separation.
- **Solvent quality.** A solvent with $\chi<\tfrac12$ is a **good solvent** (coils swell, $A_2>0$), with $\chi>\tfrac12$ a **poor solvent**. For polystyrene, $\chi\approx0.35$ in toluene (good), 0.5 in cyclohexane at 34.5 °C (theta), about 0.9 in hexane (non-solvent).
- **Swelling of networks.** A crosslinked rubber cannot dissolve, but it swells until the mixing free energy is balanced by the elastic retraction of the network (Section 20.2). The Flory–Rehner equation that expresses this balance is the standard way to measure crosslink density (Chapter 21) and the basis of the fuel and oil compatibility tables for seals: a nitrile O-ring that swells by 5 % in hydraulic oil is acceptable, an EPDM ring that swells by 100 % is not.

### Solubility parameters

The interaction part of $\chi$ can be estimated from the **Hildebrand solubility parameter** $\delta=(E_{coh}/V)^{1/2}$, the square root of the cohesive energy density:

$$
\chi\approx0.34+\frac{V_1}{RT}\left(\delta_1-\delta_2\right)^2
$$

where $V_1$ is the molar volume of the solvent and 0.34 an empirical entropic contribution. "Like dissolves like" becomes quantitative: polymer and solvent should have $\delta$ values within about 2 MPa$^{1/2}$. Hansen split $\delta$ into dispersion, polar and hydrogen-bonding parts, which handles polar polymers and is used to formulate paints, inks and adhesives.

> **Status of the principle: Solubility-parameter estimate of χ**
> *Empirical.* The regular-solution form captures only dispersion-type interactions; the constant 0.34 is fitted, and the estimate is unreliable for polar or hydrogen-bonding systems and cannot predict negative $\chi$ (specific attractions).

| Material | $\delta$ (MPa$^{1/2}$, typical) |
|---|---|
| PTFE | 12.6 |
| n-Hexane | 14.9 |
| Polyethylene | 16.2–17.0 |
| Natural rubber, polyisoprene | 16.5–17.0 |
| Cyclohexane | 16.8 |
| Toluene | 18.2 |
| Polystyrene | 18.5–19.0 |
| PMMA | 18.6–19.5 |
| Acetone | 20.3 |
| PVC | 19.5–21.5 |
| Epoxy (cured) | 20–22 |
| Nylon-6,6 | about 28 |
| Water | 47.8 |

Natural rubber and hexane, at nearly equal $\delta$, explains why rubber seals swell badly in petrol, and why nitrile rubber (with polar acrylonitrile units, $\delta\approx19$–20) is used instead. Polyethylene has a suitable $\delta$ for many hydrocarbons, but its crystals are not dissolved until the solvent is above about 100 °C, because the free energy of melting must also be paid: crystallinity, not chemistry, is the source of its solvent resistance.

### Theta conditions

At the **theta temperature** $\theta$ (or in a theta solvent), $\chi=\tfrac12$, the second virial coefficient vanishes, and the excluded-volume swelling is exactly cancelled by segment–segment attraction. The chain then follows ideal random-walk statistics, and the Mark–Houwink exponent of Chapter 19 is exactly $a=0.5$. Theta conditions are therefore the experimental reference state in which unperturbed chain dimensions and $C_\infty$ are measured. They also mark the threshold of precipitation for infinitely long chains, which is why a polymer solution held just below its theta temperature separates by molar mass — the basis of fractionation.

---

## 20.4 Blends, miscibility and block-copolymer microphase separation

### Why most polymer pairs do not mix

Applying the Flory–Huggins expression to a blend of two polymers with $N_A$ and $N_B$ segments,

$$
\frac{\Delta G_{mix}}{kT}=\frac{\phi}{N_A}\ln\phi+\frac{1-\phi}{N_B}\ln(1-\phi)+\chi\phi(1-\phi)
$$

both entropy terms are divided by large numbers. The critical value of $\chi$ becomes

$$
\chi_c=\frac12\left(\frac{1}{\sqrt{N_A}}+\frac{1}{\sqrt{N_B}}\right)^2
$$

which for $N_A=N_B=1000$ is only 0.002. Almost any positive interaction parameter, even one too small to matter between small molecules, drives the blend to phase-separate. Most polymer pairs are therefore immiscible: polystyrene and polybutadiene, polyethylene and polypropylene, PET and polyethylene all separate into coarse, weakly bonded domains. This is a central obstacle in recycling mixed plastics (Chapter 21).

Miscible blends require $\chi\le0$, which needs a specific attraction between the two polymers: a hydrogen bond, a dipole–dipole interaction or a $\pi$-electron interaction. Commercially important miscible pairs include poly(phenylene oxide)/polystyrene (Noryl), PVC/nitrile rubber (for permanently flexible cable jackets), PMMA/poly(vinylidene fluoride) (weatherable films) and PC/polyester blends (partly miscible). Many miscible blends phase-separate on heating, showing a **lower critical solution temperature** (LCST), because the specific interactions that make $\chi$ negative weaken at high temperature.

**Worked example — polystyrene with PMMA, as a blend and as a block copolymer.** For polystyrene and PMMA, $\chi\approx0.028+3.9/T$, so at 150 °C (423 K), a typical processing temperature, $\chi\approx0.037$. A blend of two chains each of 1,000 segments has $\chi_c=0.002$; $\chi$ exceeds it by a factor of almost 20, and the blend separates into domains microns across, which scatter light: the mixture is opaque and brittle. Now join one PS chain and one PMMA chain of equal length end-to-end into a symmetric diblock copolymer. The blocks still want to separate, but they cannot move apart further than one chain length. Mean-field theory predicts an order–disorder transition at $(\chi N)_{ODT}\approx10.5$ for a symmetric diblock, where $N$ is the total number of segments. At 150 °C this requires $N\ge10.5/0.037\approx280$ segments, a total molar mass of only about 29,000 g/mol (taking roughly 104 g/mol per segment). Commercial PS-b-PMMA for directed self-assembly, with $M$ around 50,000–100,000 g/mol, is therefore well ordered and forms lamellae with a period of 25–40 nm, used to pattern features on semiconductor wafers.

### Compatibilization and toughened blends

Immiscible blends are not useless; they are the basis of toughened plastics, provided the interface is strong and the domain size is controlled. A **compatibilizer** — a block or graft copolymer whose segments are miscible with each phase — sits at the interface, lowers the interfacial tension, reduces the domain size and stitches the phases together. Maleic-anhydride-grafted polypropylene reacts with the amine ends of polyamide to form a graft copolymer in situ during extrusion (reactive compatibilization), making the tough PA/PP and PA/elastomer blends of car air-intake manifolds and ski-boot shells. ABS and HIPS achieve the same effect with grafted rubber particles (Chapter 19).

### Block-copolymer microphase separation

In a block copolymer the incompatible blocks segregate into domains whose size is set by the chain dimensions, typically 5–100 nm, and the joints between blocks are confined to the interfaces. The equilibrium morphology is chosen by a balance between interfacial energy (favouring few, large domains) and chain stretching (favouring small ones). It depends on two parameters: the segregation strength $\chi N$ and the volume fraction $f$ of one block. As $f$ moves from 0.5 toward 0, the interface curves around the minority block, and the morphology changes from **lamellae** ($f\approx0.35$–0.5) through a **bicontinuous gyroid** (a narrow window near $f\approx0.33$–0.37) to **hexagonally packed cylinders** ($f\approx0.17$–0.33) and **body-centred cubic spheres** ($f$ below about 0.17) (Figure 20.3). In the strong-segregation limit, the domain period scales as $d\propto aN^{2/3}\chi^{1/6}$, larger than the random-coil size because the chains are stretched away from the interface.

<!-- FIGURE 20.3 | figures/ch20/fig-20-3-block-copolymer-phase-diagram.png | plot | Mean-field phase diagram of a diblock copolymer, segregation strength χN versus volume fraction f, with sketches of the ordered morphologies. | Content: x-axis f_A from 0 to 1; y-axis χN from 0 to 50. Order–disorder boundary with minimum χN = 10.5 at f = 0.5 rising steeply toward f = 0 and 1. Regions labelled: disordered (below), spheres (S, bcc) near the edges, cylinders (C, hex), gyroid (G, narrow wedge), lamellae (L) in the middle; mirror-symmetric about f = 0.5. Small 3D sketches of each morphology beside the plot. Marker: "SBS thermoplastic elastomer, f_PS ≈ 0.2–0.3 → PS spheres/cylinders" and "PS-b-PMMA lithography, f ≈ 0.5 → lamellae, period 25–40 nm". -->

> **Status of the principle: Mean-field diblock phase diagram**
> *Approximate.* Self-consistent-field theory reproduces the observed sequence of morphologies and the strong-segregation scaling; near the order–disorder transition composition fluctuations, neglected in mean-field theory, shift the transition to higher $\chi N$ for short chains, and real systems also show kinetically trapped and non-equilibrium structures.

Microphase separation has three major engineering uses. In **thermoplastic elastomers** such as SBS, with 20–30 % polystyrene, glassy PS spheres or cylinders act as physical crosslinks in a rubbery polybutadiene matrix; above 100 °C they soften, and the material can be injection-moulded into shoe soles, grips and bitumen modifiers for road surfacing. In **nanolithography**, block copolymer films are aligned on chemically or topographically patterned substrates to multiply the density of lithographic features (directed self-assembly). In **drug delivery and medicine**, amphiphilic block copolymers (for example PEG-b-PLA) form micelles 20–100 nm across in water, carrying hydrophobic drugs in their cores (Chapter 31).

---

## 20.5 Crystallization: lamellae, chain folding, spherulites and crystallinity

### What can crystallize

A polymer can crystallize only if its chains are regular enough to pack into a lattice: linear, stereoregular, with few branches and without bulky random side groups. Polyethylene, isotactic PP, POM, PA66, PET, PEEK and PTFE crystallize; atactic PS, PMMA, PC and random copolymers with similar comonomer contents do not. Even crystallizable polymers never become fully crystalline: chains are too long and too entangled to disentangle completely in the time available, so the solid is **semicrystalline**, a composite of crystals and amorphous regions. Typical crystallinities are 40–80 % for polyethylene, 40–70 % for iPP, 30–50 % for PA66 and 0–40 % for PET, depending on cooling rate.

In the crystal, chains adopt their lowest-energy conformation and lie parallel. Polyethylene crystallizes in an orthorhombic cell ($a=0.741$ nm, $b=0.494$ nm, $c=0.255$ nm along the chain axis, two chains per cell) with the all-trans zig-zag along $c$, giving a crystal density of 1.00 g/cm³ against 0.855 g/cm³ for the amorphous melt-quenched phase. Isotactic PP packs as $3_1$ helices; PTFE as a 13₆ or 15₇ helix whose fluorine sheath gives the slippery surface.

### Lamellae and chain folding

In 1957 Keller, Till and Fischer independently grew single crystals of polyethylene from dilute solution and found thin platelets, about 10 nm thick and several micrometres wide, with the chain axis perpendicular to the plate. Since the chains are hundreds of nanometres long, they must fold back and forth at the surfaces of the platelet. These **lamellae**, 5–30 nm thick, are the basic crystalline unit of all semicrystalline polymers. In crystals grown from the melt the folding is less regular: some chains re-enter the same lamella in an adjacent position, others leave and wander through the amorphous layer to another lamella. Chains that bridge two lamellae are **tie molecules**, and entangled loops between lamellae act similarly. They carry load between crystals and control toughness, environmental stress-crack resistance and slow crack growth in pipes. The short branches of LLDPE and bimodal PE100 (Chapter 19) are used precisely to raise the number of tie molecules.

Why should crystals be so thin? The lamellar thickness $l$ is a kinetic, not an equilibrium, choice. A lamella of thickness $l$ has two fold surfaces with high surface energy $\sigma_e$ (about 0.09 J/m² for PE, much higher than the lateral surface energy), and its melting point is depressed below the equilibrium value $T_m^0$ for an infinitely thick crystal by the Gibbs–Thomson relation (Chapter 6):

$$
T_m=T_m^0\left(1-\frac{2\sigma_e}{\Delta h_v\,l}\right)
$$

where $\Delta h_v$ is the heat of fusion per unit volume. Crystallization at an undercooling $\Delta T=T_m^0-T_c$ produces lamellae that are slightly thicker than the minimum stable thickness at $T_c$, so $l\propto1/\Delta T$: fast cooling (large undercooling) gives thin lamellae with low melting points, slow cooling or annealing gives thicker, more perfect ones. The Lauritzen–Hoffman theory of secondary nucleation on the lamellar growth face formalizes this.

> **Status of the principle: Gibbs–Thomson relation for lamellar melting**
> *Derived.* Follows from the balance of bulk and fold-surface free energies (Chapter 6); quantitative use needs $\sigma_e$ and $T_m^0$, which are obtained from extrapolations of measured $T_m$ against $1/l$, and the relation ignores reorganization of lamellae during heating.

### Spherulites

When a semicrystalline polymer crystallizes from the melt without flow, the lamellae grow outward from a nucleus in all directions, splaying and branching, with amorphous material trapped between them. The resulting spherical aggregates, **spherulites**, are typically 1–100 µm across. Viewed between crossed polarizers they show a characteristic Maltese-cross extinction pattern, because the chain axis is tangential and the lamellar radii are optically birefringent. Spherulites grow at constant radial rate $G$ until they impinge, forming polygonal boundaries where low-molar-mass material and impurities collect — weak planes along which brittle fracture often runs. The overall crystallization follows Avrami (JMAK) kinetics (Chapter 9), with exponents of 2–4 depending on nucleation and growth geometry.

<!-- FIGURE 20.4 | figures/ch20/fig-20-4-semicrystalline-hierarchy.png | schematic | Structural hierarchy of a melt-crystallized semicrystalline polymer, from unit cell to spherulite. | Content: four linked panels left to right with scale bars. (1) Orthorhombic PE unit cell, a = 0.741 nm, b = 0.494 nm, c = 0.255 nm, zig-zag chains along c. (2) Chain-folded lamella, thickness l ≈ 10–20 nm, with adjacent re-entry folds, loose loops, cilia and a tie molecule crossing the amorphous layer (≈5 nm) to the next lamella; label "long period ≈ 20–30 nm". (3) Radiating, branching lamellar stack (fibrils) with amorphous material between. (4) Spherulite 50 µm across in crossed polarizers showing Maltese cross; neighbouring spherulites impinging along straight boundaries; one boundary labelled "weak plane: impurities, low-M chains". -->

Spherulite size is controlled by nucleation density. Adding **nucleating agents** (sodium benzoate, talc, organophosphates, sorbitol derivatives) raises the number of nuclei by orders of magnitude: spherulites become smaller than the wavelength of light, the part becomes clear, crystallization is faster (shorter moulding cycles) and stiffness and heat-distortion temperature rise. Clarified polypropylene food containers and syringe barrels — like those in the opening case — depend on sorbitol clarifiers. Flow during processing orients chains and produces different morphologies: **shish-kebab** structures (an extended-chain core with folded-chain lamellae overgrown on it) in injection-moulded skins and melt-spun fibres, and highly oriented fibrillar structures in drawn fibres, where gel-spun UHMWPE fibres (Dyneema, Spectra) reach moduli above 100 GPa because nearly all chains are extended and aligned.

### Degree of crystallinity and its measurement

The crystallinity of a sample can be obtained from several measurements, which agree only approximately because each sees a different boundary between "crystal" and "amorphous":

- **Density**, using the two-phase model. If $\rho_c$ and $\rho_a$ are the crystal and amorphous densities, the mass fraction crystallinity is $X_c=\rho_c(\rho-\rho_a)/[\rho(\rho_c-\rho_a)]$. A density-gradient column measures $\rho$ to four decimals.
- **Differential scanning calorimetry**, as the ratio of the measured heat of fusion to that of a 100 % crystalline polymer, $X_c=\Delta H_m/\Delta H_m^0$ (Chapter 42).
- **Wide-angle X-ray diffraction**, as the ratio of crystalline peak area to total scattering.
- **Spectroscopy** (FTIR, Raman, solid-state NMR) using bands specific to the crystalline conformation.

| Polymer | $\rho_c$ (g/cm³) | $\rho_a$ (g/cm³) | $\Delta H_m^0$ (J/g) | $T_m^0$ (°C) | Typical $X_c$ |
|---|---|---|---|---|---|
| Polyethylene | 1.00 | 0.855 | 293 | 141.5 | 40–80 % |
| Isotactic polypropylene | 0.94 | 0.85 | 207 | 186 | 40–70 % |
| PET | 1.46 | 1.33 | 140 | 280 | 0–40 % |
| Nylon-6,6 | 1.24 | 1.09 | 196 | 280 | 30–50 % |
| PEEK | 1.40 | 1.26 | 130 | 395 | 25–40 % |
| PTFE | 2.35 | 2.00 | 82 | 332 | 50–90 % |

**Worked example — crystallinity and lamellar thickness of an HDPE pipe resin.** A sample of HDPE pipe has density 0.950 g/cm³. With $\rho_c=1.00$ and $\rho_a=0.855$ g/cm³, the mass crystallinity is $X_c=1.00\times(0.950-0.855)/[0.950\times(1.00-0.855)]=0.690$, or 69 % (the volume fraction is $(0.950-0.855)/0.145=0.655$). A DSC run on the same material measures a melting enthalpy of 200 J/g; with $\Delta H_m^0=293$ J/g this gives 68 %, in good agreement. The DSC melting peak lies at about 129 °C. Using the Gibbs–Thomson relation with $T_m^0=414.6$ K (141.5 °C), $\sigma_e=0.090$ J/m² and $\Delta h_v=293$ J/g × 1.00 g/cm³ $=2.93\times10^8$ J/m³, a lamella 10 nm thick melts at $414.6\times(1-2\times0.090/(2.93\times10^8\times10^{-8}))=389.1$ K, or 116 °C; one 20 nm thick at 129 °C; one 50 nm thick at 136 °C. The peak at 129 °C therefore corresponds to lamellae about 20 nm thick, consistent with small-angle X-ray long periods of 25–30 nm (lamella plus amorphous layer) for slowly cooled HDPE. A pipe that is quenched from the extruder on its outer surface has thinner lamellae and a lower melting point at the skin than in the bulk, and the resulting gradient of crystallinity contributes to the residual stresses that pipe extruders try to minimize.

### Crystallinity and properties

Crystallinity raises stiffness, yield strength, density, chemical and solvent resistance, barrier performance and heat-distortion temperature, and lowers toughness, transparency and the rate of water or solvent uptake. Above Tg, the amorphous phase is rubbery, and the crystals act as stiff, physically crosslinked reinforcement: the modulus of polyethylene rises from about 0.2 GPa for LDPE to 1.2 GPa for HDPE, mostly through crystallinity. Below Tg, both phases are rigid, and crystallinity matters less for stiffness but more for chemical resistance. PET shows the extremes: quenched amorphous PET bottles are clear and have a Tg of 75 °C; slowly crystallized PET is opaque and dimensionally stable up to 200 °C, the basis of dual-ovenable food trays. Stretch-blow moulding (Chapter 21) induces small, oriented crystals that keep the bottle clear while improving CO₂ barrier and strength.

---

## 20.6 The glass transition

### Phenomenology

Cool an amorphous polymer melt and, at a temperature called the **glass-transition temperature** $T_g$, its properties change abruptly: the modulus rises from about 1 MPa (rubbery) to about 1–3 GPa (glassy) over a range of 10–20 K, and the slope of specific volume against temperature drops to roughly half its melt value (Figure 20.5). The heat capacity and thermal-expansion coefficient also step down. No latent heat is released and no structure appears in a diffraction pattern: the liquid simply stops rearranging on the time scale of the experiment. Measured $T_g$ depends on the cooling rate, rising by about 3 K for every tenfold increase in rate. The glass transition is therefore a kinetic phenomenon — the point where the molecular relaxation time exceeds the experimental time scale — not a true thermodynamic phase transition. It is the same phenomenon as in the oxide and metallic glasses of Chapters 9 and 17.

<!-- FIGURE 20.5 | figures/ch20/fig-20-5-glass-transition.png | plot | Specific volume versus temperature for an amorphous polymer cooled at two rates, and the WLF shift factor above Tg. | Content: left panel: x-axis temperature from 20 to 180 °C; y-axis specific volume 0.94 to 1.00 cm³/g (polystyrene-like). Melt line (expansion 5.5×10^-4 cm³ g^-1 K^-1) and two glass lines (2.0×10^-4) branching off at Tg = 100 °C (slow cooling, 1 K/min) and 106 °C (fast cooling, 100 K/min); shaded gap labelled "free volume frozen in"; small arrow labelled "physical aging" pointing down from the fast-cooled glass at 80 °C. Right panel: log10 aT versus T − Tg from 0 to 100 K using C1 = 17.44, C2 = 51.6 K; marked points at T − Tg = 10 (−2.83), 20 (−4.87), 30 (−6.41); dashed Arrhenius line for comparison. -->

### Free-volume theory and the WLF equation

The **free-volume** picture explains the transition. The volume of a liquid is the occupied volume of its molecules plus a **free volume** $V_f$ made of the gaps between them. Molecular motion requires a segment to find a nearby hole large enough to move into, so mobility rises steeply with the fractional free volume $f=V_f/V$. Doolittle found empirically that viscosity follows $\ln\eta=\ln A+B/f$. On cooling, $f$ decreases linearly, $f=f_g+\alpha_f(T-T_g)$, until the motions needed to shed further free volume become too slow; at $T_g$ the free volume is frozen in at a value $f_g$.

Writing the ratio of relaxation times (or viscosities) at $T$ and at a reference $T_g$, the **shift factor** $a_T$, from Doolittle's equation gives

$$
\log_{10}a_T=-\frac{C_1\,(T-T_g)}{C_2+T-T_g},\qquad C_1=\frac{B}{2.303f_g},\quad C_2=\frac{f_g}{\alpha_f}
$$

This is the **Williams–Landel–Ferry (WLF) equation** (1955). With "universal" constants $C_1=17.44$ and $C_2=51.6$ K it describes many amorphous polymers within a factor of a few between $T_g$ and $T_g+100$ K; for $B=1$ these correspond to $f_g\approx0.025$ and $\alpha_f\approx4.8\times10^{-4}$ K⁻¹, which says that about 2.5 % of the volume of a glass is free volume at $T_g$.

> **Status of the principle: WLF equation**
> *Empirical.* The form follows from Doolittle's free-volume relation, which is itself empirical; the constants $C_1$ and $C_2$ are fitted for each polymer (the "universal" values are averages). Valid from $T_g$ to about $T_g+100$ K; below $T_g$ the glass is out of equilibrium and relaxation is closer to Arrhenius, and far above $T_g$ Arrhenius behaviour also returns.

The WLF equation is the basis of **time–temperature superposition** (Chapter 14): viscoelastic data measured over a few decades of time at several temperatures can be shifted along the log-time axis by $\log a_T$ to build a master curve covering ten or more decades. Polymer engineers use it to predict 20-year creep of a polymer bracket from tests of days at higher temperature, and to understand why a polymer that is rubbery in a slow test can be glassy under impact.

**Worked example — how steeply mobility rises above Tg.** Take the universal constants. At $T_g+10$ K, $\log a_T=-17.44\times10/61.6=-2.83$, so molecular motions are $10^{2.83}\approx680$ times faster than at $T_g$. At $T_g+20$ K, $\log a_T=-17.44\times20/71.6=-4.87$, a factor of about 74,000; at $T_g+30$ K, $-6.41$, a factor of 2.6 million. Consider an injection-moulded polystyrene lens holder ($T_g=100$ °C). If the flow-induced orientation in the melt takes about an hour to relax at 100 °C, it relaxes at 120 °C in $3600\times1.34\times10^{-5}\approx0.05$ s — faster than the part cools through that range, so the orientation frozen into the part is set almost entirely by what happens in the last few degrees above $T_g$. Conversely, a PMMA aircraft canopy formed at 150 °C ($T_g+45$ K) relaxes in microseconds, but if it is held for years at 70 °C, 35 K below $T_g$, the glass continues to densify slowly — **physical aging** — becoming stiffer and more brittle, with lower creep compliance. Physical aging is why the creep data of glassy polymers must state the aging time before the test.

### Molecular factors controlling Tg

Since $T_g$ marks the onset of cooperative backbone motion, anything that hinders that motion raises it.

| Factor | Effect on Tg | Example |
|---|---|---|
| Backbone flexibility | Flexible links (–O–, –Si–O–) lower; rings in the backbone raise | PDMS −125 °C; PE −120 °C; PC 147 °C; polyimide above 350 °C |
| Bulky or stiff side groups | Raise by hindering rotation | PP −10 °C; PS 100 °C; poly(vinyl carbazole) 200 °C |
| Flexible side chains | Lower by internal plasticization | Poly(methyl acrylate) 10 °C; poly(butyl acrylate) −50 °C |
| Polarity and hydrogen bonds | Raise by strengthening interchain cohesion | PVC 82 °C vs PP −10 °C; PA66 50–60 °C dry, near 0 °C wet |
| Chain length | Raises up to a plateau (fewer free ends) | Flory–Fox: PS 67 °C at 3,000 g/mol, 90 °C at 10,000, 99 °C at 100,000 |
| Crosslinking | Raises | Epoxy Tg from 100 °C to above 200 °C with crosslink density |
| Plasticizers and absorbed solvent | Lower | PVC with 30–40 % plasticizer becomes rubbery at room temperature; moisture lowers PA66 and epoxy Tg |
| Copolymerization and miscible blending | Intermediate value | PPO/PS (Noryl) 50/50 has a single Tg near 150 °C |
| Tacticity | Moderate effect in some polymers | PMMA: syndiotactic about 125 °C, isotactic about 45 °C |

Two simple relations quantify the last effects. The **Flory–Fox equation** for molecular weight,

$$
T_g=T_{g,\infty}-\frac{K}{M_n}
$$

with $K\approx10^5$ K·g/mol for polystyrene, reflects the extra free volume carried by chain ends. The **Fox equation** for miscible blends, random copolymers and plasticized polymers,

$$
\frac{1}{T_g}=\frac{w_1}{T_{g1}}+\frac{w_2}{T_{g2}}
$$

(weight fractions, absolute temperatures) gives, for PPO ($T_g=215$ °C) blended 50/50 with PS ($T_g=100$ °C), $1/T_g=0.5/488.15+0.5/373.15$, so $T_g=423$ K = 150 °C — close to the measured value and the reason Noryl can be tuned between 100 and 200 °C by composition. A blend that shows a single, composition-dependent $T_g$ by DSC or DMA is the standard experimental test of miscibility; an immiscible blend shows the two separate $T_g$ values of its components.

> **Status of the principle: Flory–Fox and Fox equations**
> *Empirical.* Simple mixing rules with a free-volume rationale; adequate within about 10 K for weakly interacting systems, but they miss strong specific interactions (where the Gordon–Taylor or Kwei forms with fitted constants are used).

### Tg in design

The glass transition separates the service regimes of polymers. An **amorphous** thermoplastic is useful only below its $T_g$ (heat-distortion temperature is typically 10–20 K below $T_g$): PS cups soften in boiling water, PC survives it. An **elastomer** is useful only above its $T_g$: a seal compound with $T_g=-40$ °C becomes leathery and leaks in a Siberian winter, and the Challenger shuttle O-ring failure of 1986 involved a fluoroelastomer whose resilience was too low at the 2 °C launch temperature. A **semicrystalline** polymer can be used between $T_g$ and $T_m$ (PE, PP, POM, with $T_g$ below room temperature) or below $T_g$ (PEEK, PPS) for maximum stiffness. Near $T_g$ the mechanical loss factor $\tan\delta$ peaks, which is exploited in vibration-damping layers on car floors and in tyre treads, where a high loss near 0 °C at 10–100 Hz gives wet grip.

---

## 20.7 Liquid-crystalline polymers

### Rods that order

If the chain is not flexible but a stiff rod, a different kind of order becomes possible. Long, rigid rods in a concentrated solution or melt cannot all point randomly without overlapping: above a critical concentration, excluded-volume packing forces them to align along a common direction, the **director**, while their centres remain disordered as in a liquid. This **nematic** liquid-crystalline phase is the polymer analogue of the small-molecule liquid crystals in displays (Chapter 29). Onsager (1949) and Flory (1956) showed that rods with aspect ratio $x$ (length/diameter) form a nematic phase above a volume fraction of roughly $\phi^*\approx(8/x)(1-2/x)$, about 8 % for $x=100$: alignment is driven by packing entropy, not by attractive forces. The degree of alignment is measured by the **order parameter** $S=\langle\tfrac12(3\cos^2\theta-1)\rangle$, where $\theta$ is the angle between a molecule and the director; $S=0$ for an isotropic liquid and $S=1$ for perfect alignment, with typical nematic values of 0.5–0.9.

> **Status of the principle: Onsager–Flory rod criterion**
> *Approximate.* Mean-field excluded-volume theories for monodisperse rigid rods; they predict the right scaling with aspect ratio, but real chains are semiflexible and polydisperse, which shifts the transition.

### Lyotropic and thermotropic LCPs

**Main-chain** LCPs have mesogenic, rod-like units in the backbone; **side-chain** LCPs have mesogens attached through flexible spacers to a flexible backbone (used in optical and actuator applications, including liquid-crystal elastomers that contract reversibly on heating; Chapter 29).

- **Lyotropic** LCPs form liquid crystals in solution. Poly(p-phenylene terephthalamide) (PPTA; Kevlar, Twaron) cannot be melted below its decomposition temperature, but dissolves at about 20 % in concentrated sulfuric acid to give a nematic dope. Spinning this dope through an air gap into water (dry-jet wet spinning) aligns the domains along the fibre, giving fibres with modulus 70–130 GPa and strength about 3–3.6 GPa at a density of 1.44 g/cm³: specific strength five times that of steel wire. They are used in body armour, helmet shells, tyre cords, fibre-optic cable strength members and composite pressure vessels (Chapter 22). PBO (Zylon) and the gel-spun UHMWPE fibres mentioned earlier reach still higher specific stiffness.
- **Thermotropic** LCPs form liquid crystals in the melt. Aromatic copolyesters such as Vectra (hydroxybenzoic acid with hydroxynaphthoic acid) have a melting point lowered by the irregular copolymer sequence to 280–330 °C, and their melts are nematic. Under flow the rods align readily, so the melt viscosity is exceptionally low and the moulded part is highly oriented along the flow direction: very thin walls (0.2 mm) can be filled, the shrinkage and thermal expansion along the flow direction are almost zero, and the parts are stiff and chemically resistant. Thermotropic LCPs dominate fine-pitch electronic connectors and are used in minimally invasive surgical instruments and as low-loss, low-moisture substrates for high-frequency circuits.

The price of orientation is anisotropy: strength and stiffness across the flow direction can be a fifth of those along it, weld lines where two flow fronts meet are very weak, and fibres such as Kevlar are weak in compression because the aligned chains buckle into kink bands at about 0.4 GPa. Composite designers must therefore treat aramid fibres differently from carbon (Chapter 22).

<!-- FIGURE 20.6 | figures/ch20/fig-20-6-lcp-order.png | schematic | Isotropic, nematic and oriented-fibre states of a rigid-rod polymer, with the order parameter. | Content: three panels. (1) Isotropic solution: rods of aspect ratio about 100 at random orientations, φ < φ* ≈ 0.08, S = 0. (2) Nematic domain: rods roughly parallel to director n (arrow), S ≈ 0.7; several domains with different directors separated by disclinations. (3) After spinning: all domains aligned along the fibre axis, S > 0.9, labelled "PPTA fibre, E ≈ 70–130 GPa". Inset graph: S versus rod volume fraction, zero until φ* then jumping to about 0.8 (first-order transition). -->

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How do entangled chains flow, and why does melt viscosity scale as $M^{3.4}$? | Chapter 21 |
| How do polymer parts yield, craze and crack, and how do solvents cause stress cracking? | Chapter 21 |
| How is crosslink density measured by swelling, and how are elastomers vulcanized? | Chapter 21 |
| How do processing flows orient chains and set crystallinity in moulded parts, films and fibres? | Chapter 21 |
| What are the viscoelastic models and time–temperature superposition behind polymer creep? | Chapter 14 |
| How do the solution thermodynamics and Gibbs–Thomson effect used here follow from free energy? | Chapter 6 |
| How do nucleation and Avrami kinetics apply to crystallization in general? | Chapter 9 |
| How do aramid, carbon and glass fibres combine with polymer matrices in composites? | Chapter 22 |
| How do small-molecule liquid crystals, gels and self-assembled soft matter work? | Chapter 29 |
| How are DSC, DMA, X-ray scattering and polarized-light microscopy used to measure Tg and crystallinity? | Chapters 42 and 43 |
| How are polymer chains simulated with molecular dynamics and coarse-grained Monte Carlo? | Chapter 46 |
| How does physical and chemical aging change polymer properties in service? | Chapter 36 |

**Next:** Chapter 21 sets these chains in motion — in the melt, in the deforming solid and in the processing machine — and follows them through additives, degradation, vulcanization and recycling.
