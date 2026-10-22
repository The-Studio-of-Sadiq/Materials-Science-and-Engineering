# Chapter 46 — Atomistic and Mesoscale Simulation

*Part X · Characterization, Computation and Design*

An aero-engine manufacturer is qualifying a new nickel-base superalloy for a turbine disc. A disc spends tens of thousands of hours between 600 and 750 °C under centrifugal stress; its life is set by creep, by fatigue cracks that start at grain boundaries and inclusions, and by the slow coarsening of the γ′ precipitates that give the alloy its strength. Testing alone would take a decade: creep tests of 10,000 h, fatigue campaigns at several temperatures, forging trials for every change of composition. Density-functional theory (Chapter 45) can compute the energy of a γ′ unit cell or of a single antiphase boundary, but a disc contains $10^{28}$ atoms, and its precipitates coarsen over years. No single calculation can span that gap. What engineers can do is build a chain: electronic-structure calculations feed interatomic potentials; potentials drive molecular dynamics of dislocations cutting precipitates; thermodynamic databases predict which phases form and in what fractions; phase-field models evolve the microstructure during heat treatment; dislocation dynamics and crystal plasticity turn that microstructure into a stress–strain response; and finite-element models of the whole disc use it. Each link has its own approximations and its own domain of validity. Choosing, linking and checking them is the subject of this chapter.

> **How do simulations reach from atoms to microstructures to components, when each method can span only a few orders of magnitude in length and time?**
> **What does each method assume, what does it deliver, and how are their results passed — and checked — from one scale to the next?**

| Concept | Engineering destination |
|---|---|
| Molecular dynamics | Dislocation–precipitate interactions, radiation cascades, thermal conductivity, polymer and glass structure |
| Interatomic potentials | Reliability of every MD and MC result; choice between speed and chemistry |
| Thermostats and barostats | Simulating at the temperature and pressure of service or processing |
| Metropolis Monte Carlo | Order–disorder in alloys, segregation to grain boundaries, polymer conformations |
| Kinetic Monte Carlo | Long-time diffusion, precipitation, radiation-damage annealing, thin-film growth |
| Phase-field modelling | Solidification microstructures, precipitate coarsening, grain growth, martensite, fracture |
| Discrete dislocation dynamics | Work hardening, size effects, fatigue structures |
| Crystal-plasticity FEM | Texture evolution in forming, grain-scale stress hot spots, fatigue initiation |
| CALPHAD | Phase diagrams of multicomponent alloys, heat-treatment windows, solidification paths |
| Multiscale modelling and ICME | Alloy and process design with fewer trials; certification of new materials |

**Roadmap.** The scale problem (46.1) → molecular dynamics: potentials, integrators, thermostats and barostats (46.2) → Monte Carlo, from Metropolis sampling to kinetic Monte Carlo (46.3) → phase-field modelling of microstructure (46.4) → discrete dislocation dynamics and crystal-plasticity finite elements (46.5) → CALPHAD and computational thermodynamics (46.6) → multiscale modelling and integrated computational materials engineering (46.7).

---

## 46.1 The scale problem

The phenomena that set the properties of engineering materials span about ten orders of magnitude in length and twenty in time. Atomic vibrations occur in $10^{-13}$ s over $10^{-10}$ m; a vacancy in copper at room temperature hops about once every few milliseconds; precipitates coarsen over hours at ageing temperatures and years in service; components are metres long and serve for decades. Figure 46.1 places the simulation methods on this map.

<!-- FIGURE 46.1 | figures/ch46/fig-46-1-length-time-scales.png | map | Length and time scales accessible to simulation methods, from electrons to components. | Content: log–log map, x-axis length 10^-10 to 10^0 m, y-axis time 10^-15 to 10^8 s. Overlapping translucent regions: DFT (0.1–2 nm, fs–10 ps), ab-initio MD within it, classical MD (1–100 nm, fs–1 μs), kinetic Monte Carlo (1 nm–1 μm, ps–hours), phase-field (10 nm–1 mm, μs–days), discrete dislocation dynamics (100 nm–50 μm, ns–ms at high strain rates), crystal-plasticity FEM (1 μm–10 mm, s–years), CALPHAD (equilibrium, no length/time; shown as vertical band labelled "thermodynamics: all scales"), continuum FEM (1 mm–10 m, s–decades). Diagonal arrow labelled "ICME: information passed upward, validation passed downward". -->

No method covers more than a few decades in each direction, for a simple reason: each must resolve the fastest and smallest relevant process in its own description. Molecular dynamics must follow atomic vibrations, so its time step is about a femtosecond; phase-field models must resolve a diffuse interface, so their grid spacing is a fraction of the interface width. Methods at larger scales gain reach by **coarse-graining**: they discard degrees of freedom (electrons, then individual atoms, then individual dislocations) and replace them with parameters — a potential, a rate, a mobility, a free-energy function, a hardening law — that must come from a finer-scale method or from experiment.

> **Status of the principle: Coarse-graining by scale separation**
> *Approximate.* A coarse model is valid when the discarded degrees of freedom equilibrate much faster, or act over much shorter distances, than the variables retained; it fails where scales overlap — for example in nanocrystals, where grain size approaches dislocation core size, or at shock strain rates, where loading is as fast as atomic relaxation.

---

## 46.2 Molecular dynamics

### The method

**Molecular dynamics (MD)** integrates Newton's equations of motion for a system of atoms interacting through a potential energy $U(\mathbf r_1,\dots,\mathbf r_N)$:

$$
m_i\frac{d^2\mathbf r_i}{dt^2}=\mathbf F_i=-\nabla_{\mathbf r_i}U
$$

The result is a trajectory — positions and velocities of every atom at every step — from which thermodynamic averages (energy, pressure, heat capacity), structure (radial distribution functions, defect configurations) and transport properties (diffusion coefficients from mean-square displacement, thermal conductivity from heat-flux correlations, viscosity) are computed by statistical mechanics. Periodic boundary conditions remove free surfaces; systems from a few thousand to billions of atoms are simulated on modern supercomputers, with $10^5$–$10^7$ atoms routine for materials problems.

Everything rests on the potential. If $U$ comes from DFT at each step (**ab-initio MD**), the method inherits DFT's accuracy and cost — a few hundred atoms for tens of picoseconds. **Classical MD** uses an analytic or fitted potential, roughly $10^3$–$10^6$ times cheaper, and reaches millions of atoms and nanoseconds to microseconds.

### Interatomic potentials

The potential must reproduce the parts of the DFT potential-energy surface (Chapter 45) relevant to the problem. Four families illustrate the range.

**Lennard-Jones (LJ).** A pair potential for closed-shell atoms:

$$
U_{LJ}(r)=4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12}-\left(\frac{\sigma}{r}\right)^{6}\right]
$$

The $r^{-6}$ term is the van der Waals (dispersion) attraction; the $r^{-12}$ term is a convenient, not physical, model of Pauli repulsion. For argon $\varepsilon/k_B=119.8$ K ($\varepsilon=0.0103$ eV) and $\sigma=3.405$ Å, so the minimum lies at $r_{min}=2^{1/6}\sigma=3.82$ Å. LJ is excellent for noble gases and a building block for non-bonded interactions in polymer force fields; for metals and covalent solids it fails badly. Any pair potential predicts the Cauchy relation $C_{12}=C_{44}$ for cubic crystals and a vacancy formation energy equal to the cohesive energy, whereas real metals have $C_{12}\ne C_{44}$ and vacancy energies a third of the cohesive energy.

**Embedded-atom method (EAM).** For metals the energy of an atom depends on how many neighbours share its electron gas. The EAM writes

$$
U=\sum_i F_i\!\left(\bar\rho_i\right)+\frac12\sum_{i\ne j}\phi_{ij}(r_{ij}),\qquad \bar\rho_i=\sum_{j\ne i}f_j(r_{ij})
$$

where $\bar\rho_i$ is the electron density at atom $i$ contributed by its neighbours, $F_i$ is the energy of embedding the atom in that density, and $\phi$ is a pair repulsion. Because $F$ is concave, the energy per bond decreases as coordination rises — correctly giving low vacancy and surface energies relative to cohesion. EAM and its angular extension MEAM are the workhorses for FCC and many BCC metals and alloys: Cu, Al, Ni, Ni–Al, Fe, Fe–Cr. Their cost is only a few times that of a pair potential.

**Tersoff and bond-order potentials.** Covalent solids have directional bonds whose strength depends on the number and angles of neighbours. The **Tersoff** potential,

$$
U=\frac12\sum_{i\ne j}f_c(r_{ij})\left[A\,e^{-\lambda_1r_{ij}}-b_{ij}\,B\,e^{-\lambda_2r_{ij}}\right]
$$

multiplies the attractive term by a **bond order** $b_{ij}$ that decreases as atom $i$ acquires more neighbours, weighted by bond angles. It stabilizes the diamond structure of Si, C and Ge and describes SiC; the related REBO and AIREBO potentials are standard for graphene, nanotubes and hydrocarbons.

**Reactive force fields (ReaxFF).** To model bond breaking and formation in mixed chemistry — combustion, oxidation, corrosion, polymer pyrolysis, battery electrolyte decomposition — ReaxFF computes bond orders continuously from distances and equilibrates atomic charges at every step. It is about 10–100 times more expensive than EAM and requires parameter sets fitted carefully to quantum-chemical data for each chemistry; a set built for hydrocarbon combustion is not valid for silica glass.

Machine-learned potentials (GAP, NequIP, MACE), which fit the DFT surface flexibly with near-DFT accuracy at a fraction of its cost, are the newest family; Chapter 47 covers them.

Table 46.1 summarizes the trade-offs.

| Potential | Typical materials | Relative cost per atom-step | Captures | Misses |
|---|---|---|---|---|
| Lennard-Jones | Noble gases, non-bonded parts of polymers | 1 | Dispersion, packing | Metallic, covalent and ionic bonding |
| Buckingham + Coulomb | Ionic oxides, silicates | 2–10 (long-range sums) | Ionic structure, defects in oxides | Charge transfer, covalency |
| EAM / MEAM | Metals and alloys | 2–5 | Many-body metallic cohesion, defects, dislocations | Directional bonding, magnetism (except special forms) |
| Tersoff / REBO | Si, C, SiC, hydrocarbons | 5–10 | Directional covalent bonds | Long-range dispersion, charge |
| ReaxFF | Reactive mixed chemistry | 100–500 | Bond breaking and formation, charge equilibration | Accuracy outside training chemistry |
| Machine-learned (GAP, NequIP, MACE) | Any, given training data | 100–$10^4$ | Near-DFT accuracy | Configurations far from training set |

> **Status of the principle: Classical interatomic potentials**
> *Empirical.* Functional forms are physically motivated but their parameters are fitted to experimental or DFT data; a potential is reliable only for structures, temperatures and deformation modes similar to its fitting set, and transferability must be checked for each new use.

### Integrators

The equations of motion are integrated in small time steps $\Delta t$. The standard algorithm, **velocity Verlet**, is

$$
\mathbf r(t+\Delta t)=\mathbf r(t)+\mathbf v(t)\Delta t+\frac{\mathbf F(t)}{2m}\Delta t^2
$$

$$
\mathbf v(t+\Delta t)=\mathbf v(t)+\frac{\mathbf F(t)+\mathbf F(t+\Delta t)}{2m}\Delta t
$$

It is time-reversible and **symplectic** — it preserves phase-space volume — so although individual trajectories diverge from the exact ones (MD is chaotic), the total energy does not drift systematically over millions of steps. Higher-order integrators conserve energy better over a single step but drift over long runs and are rarely used.

The time step must resolve the fastest motion. A rule of thumb is $\Delta t$ about one-twentieth to one-fiftieth of the shortest vibrational period: 1–5 fs for metals, about 1 fs for oxides, 0.5–1 fs for systems containing hydrogen (whose bonds vibrate at about 90 THz), unless those bonds are constrained.

### Ensembles, thermostats and barostats

Plain MD conserves energy and samples the microcanonical (**NVE**) ensemble. Experiments are done at fixed temperature and pressure, so most simulations sample the canonical (**NVT**) or isothermal–isobaric (**NPT**) ensemble by coupling the system to a thermostat and a barostat.

- **Velocity rescaling and the Berendsen thermostat** scale velocities towards the target temperature with a time constant $\tau_T$. They are robust for equilibration but do not generate the correct canonical distribution of fluctuations.
- **Nosé–Hoover** thermostats add a friction variable $\zeta$ with its own equation of motion,

$$
\dot{\mathbf v}_i=\frac{\mathbf F_i}{m_i}-\zeta\,\mathbf v_i,\qquad \dot\zeta=\frac{1}{Q}\left(\sum_i m_iv_i^2-3Nk_BT\right)
$$

where $Q$ is a fictitious thermal mass. The extended system samples the canonical ensemble exactly (for ergodic systems; Nosé–Hoover chains fix the cases where a single thermostat is not ergodic).
- **Langevin** thermostats add friction and random forces to each atom; they are canonical and stable, and model coupling to an electron bath in metals, but they perturb dynamics and hence transport coefficients.
- **Barostats** (Berendsen, Nosé–Hoover/MTK, Parrinello–Rahman) let the cell volume — and, in Parrinello–Rahman, its shape — fluctuate in response to the difference between the instantaneous and target stress tensors. Variable cell shape is essential for simulating phase transformations (martensitic, pressure-induced) and for applying uniaxial stress.

The choice matters: transport properties (diffusion, viscosity, thermal conductivity) should be computed in NVE or with weakly coupled deterministic thermostats after equilibration, never with strong Langevin damping.

### What MD has delivered, and its limits

Classical MD gave the first atomic-scale pictures of displacement cascades in irradiated metals (hundreds of displaced atoms in a few picoseconds, most recombining within 10 ps), of dislocation cores and their dissociation, of dislocation cutting of γ′ precipitates, of grain-boundary sliding in nanocrystals, of crack-tip emission versus cleavage, of glass formation and of polymer chain entanglement. Its limits are equally clear:

- **Time.** Nanoseconds to microseconds. Thermally activated processes with barriers above about 0.5 eV happen too rarely at moderate temperatures to be seen.
- **Strain rate.** Deforming a simulation cell by even a few percent within a nanosecond implies strain rates of $10^7$–$10^{9}\ \mathrm{s^{-1}}$, versus $10^{-3}\ \mathrm{s^{-1}}$ in a tensile test. Flow stresses from MD are therefore upper bounds dominated by athermal processes.
- **Size.** $10^7$ atoms of copper is a cube about 50 nm on a side — one small grain, a few dislocations.

**Worked example — the cost and reach of an MD simulation of copper.** The highest phonon frequency of copper is about 7 THz, a period of $1/7\times10^{12}=0.14$ ps. A time step of 2 fs gives 70 steps per shortest period, adequate for velocity Verlet. One nanosecond needs $10^{-9}/2\times10^{-15}=5\times10^{5}$ steps. A $10^6$-atom cell (a cube about 23 nm on a side) with an EAM potential costing about $2\times10^{-6}$ core-seconds per atom per step needs

$$
10^{6}\times5\times10^{5}\times2\times10^{-6}\ \mathrm{s}=10^{6}\ \mathrm{core\text{-}s}\approx278\ \mathrm{core\text{-}hours}
$$

— a few hours on a 100-core cluster node. To strain the cell by 1 % in 100 ps imposes $\dot\varepsilon=0.01/10^{-10}\ \mathrm{s}=10^{8}\ \mathrm{s^{-1}}$, eleven orders of magnitude faster than a quasi-static tensile test at $10^{-3}\ \mathrm{s^{-1}}$. Reaching 10 % strain at the laboratory rate would take 100 s of simulated time, or $5\times10^{16}$ steps — about $10^{11}$ times the run just costed. MD is therefore a tool for mechanisms, for high-rate events (shock, ballistic impact, laser ablation, radiation cascades) and for computing parameters such as dislocation mobilities and grain-boundary energies that slower methods use, not for simulating a tensile test directly.

---

## 46.3 Monte Carlo methods

### Metropolis Monte Carlo

Many questions are about equilibrium — which atomic arrangement a solid solution adopts at 600 °C, how much solute sits at a grain boundary, what conformations a polymer chain takes in a melt — and do not need the dynamics. **Monte Carlo (MC)** methods generate configurations with the correct Boltzmann probabilities directly, by random moves. The **Metropolis algorithm** (1953) proposes a random change (swap two atoms of different species, displace an atom, flip a spin, rotate a chain segment), computes the energy change $\Delta E$, and accepts the move with probability

$$
P_{acc}=\min\left[1,\exp\left(-\frac{\Delta E}{k_BT}\right)\right]
$$

Downhill moves are always accepted; uphill moves are accepted with the Boltzmann factor. Repeating this generates a Markov chain whose configurations, after equilibration, are distributed according to the canonical ensemble, because the acceptance rule satisfies **detailed balance**.

> **Status of the principle: Metropolis sampling**
> *Derived.* Detailed balance plus ergodicity guarantee convergence to the Boltzmann distribution; the guarantee is asymptotic, and in practice sampling can be trapped in metastable states when barriers between configurations are large compared with $k_BT$.

For example, an uphill swap costing $\Delta E=0.1$ eV is accepted with probability $\exp(-0.1/0.02585)=0.021$ at 300 K but $\exp(-0.1/0.0776)=0.28$ at 900 K. This is why MC simulations of ordering in alloys are run by slowly cooling ("simulated annealing"), and why the same idea is used as a general optimization method.

MC moves need not be physical, which is its power: atoms may swap across the whole cell in one step, something that takes diffusion years. Combined with a **cluster expansion** — an Ising-like model of alloy energy as a sum of pair, triplet and higher-order interactions fitted to DFT energies of dozens of ordered structures — Metropolis MC predicts order–disorder transition temperatures, short-range order, and solubility limits in alloys such as Ni–Al, Cu–Au and high-entropy alloys. **Hybrid MD/MC** (swaps interleaved with MD steps) predicts equilibrium segregation of solutes to grain boundaries and dislocations, which governs temper embrittlement of steels and the thermal stability of nanocrystalline alloys. **Grand-canonical MC**, in which particles are inserted and removed at fixed chemical potential, computes gas adsorption in zeolites and metal–organic frameworks for carbon capture and hydrogen storage.

### Kinetic Monte Carlo

Metropolis MC has no physical time. **Kinetic Monte Carlo (kMC)** restores it for systems that evolve by discrete, thermally activated events — atom–vacancy exchanges, adatom hops on a growing film, emission of a solute from a cluster. Each possible event $i$ has a rate from transition-state theory,

$$
r_i=\nu_i\exp\left(-\frac{E_{a,i}}{k_BT}\right)
$$

with attempt frequency $\nu_i\approx10^{12}$–$10^{13}\ \mathrm{s^{-1}}$ and activation energy $E_{a,i}$ (from DFT nudged-elastic-band calculations, Chapter 45, or a fitted model). The **residence-time** (Bortz–Kalos–Lebowitz, or Gillespie) algorithm proceeds as follows (Figure 46.2):

1. List all possible events and their rates; the total rate is $R=\sum_i r_i$.
2. Choose event $j$ with probability $r_j/R$ using a uniform random number.
3. Execute it, and advance the clock by $\Delta t=-\ln u/R$, where $u$ is a second uniform random number in (0, 1].
4. Update the event list and repeat.

Each step is an event; the simulation never wastes time on the vibrations between events. That is the source of kMC's enormous reach in time.

> **Status of the principle: Kinetic Monte Carlo**
> *Approximate.* Exact for a Markov process whose event list and rates are complete and correct; its accuracy rests on transition-state theory (harmonic rates, no correlated multiple jumps) and on the completeness of the event catalogue — an event that is not listed can never happen.

<!-- FIGURE 46.2 | figures/ch46/fig-46-2-kmc-residence-time.png | schematic | Kinetic Monte Carlo: a vacancy among possible jumps on an energy landscape, and the residence-time event selection. | Content: (a) 2D square lattice patch with a vacancy (open circle), four neighbouring atoms with arrows for possible exchanges; below it an energy-vs-reaction-coordinate profile with minima (lattice sites) and saddle points of height Ea = 0.70 eV; attempt frequency ν = 10^13 s^-1 annotated. (b) Horizontal bar of total length R split into segments r1, r2, r3, r4 (unequal, e.g. a solute-neighbour jump with lower barrier is longer); random number u1·R arrow selecting segment r2; side formula Δt = −ln(u2)/R. (c) Small inset table: T = 300, 600, 900 K with Δt ≈ 4.8 ms, 6.3 ns, 69 ps. -->

**Worked example — why kinetic Monte Carlo is needed for vacancy diffusion.** In copper, a vacancy exchanges with one of its 12 nearest neighbours with migration energy $E_m\approx0.70$ eV and $\nu\approx10^{13}\ \mathrm{s^{-1}}$. The rate per neighbour at 300 K is

$$
r=10^{13}\exp\left(-\frac{0.70}{8.617\times10^{-5}\times300}\right)=17.4\ \mathrm{s^{-1}}
$$

so the total rate is $R=12\times17.4=209\ \mathrm{s^{-1}}$ and the mean residence time between hops is $1/R=4.8$ ms. An MD simulation with 2 fs steps would need $4.8\times10^{-3}/2\times10^{-15}=2.4\times10^{12}$ steps to see one hop — impossible. In kMC each hop is one step. At 600 K the rate rises to $R=1.58\times10^{8}\ \mathrm{s^{-1}}$ ($\Delta t=6.3$ ns) and at 900 K to $1.44\times10^{10}\ \mathrm{s^{-1}}$ ($\Delta t=69$ ps), where MD and kMC begin to overlap and can be cross-checked. The vacancy diffusivity at 900 K is $D_v=Ra^2/6$ with jump distance $a=0.256$ nm, giving $1.44\times10^{10}\times(0.256\times10^{-9})^2/6=1.6\times10^{-10}\ \mathrm{m^2\,s^{-1}}$. Multiplying by the vacancy fraction (Chapter 8) gives the self-diffusion coefficient that sets creep and sintering rates.

Applications of kMC include precipitation of copper clusters in irradiated reactor-pressure-vessel steels over decades of service, the annealing of radiation damage (object kMC, which tracks defect clusters rather than lattice sites), the morphology of thin films grown by vapour deposition (island versus layer growth, Chapter 41), and surface reactions on catalysts with rates computed by DFT.

---

## 46.4 Phase-field modelling

### The diffuse-interface idea

Microstructures — dendrites, precipitates, grains, martensite plates, domains — are defined by interfaces that move. Tracking sharp interfaces explicitly is awkward when they merge, split or meet at triple junctions. The **phase-field method** replaces each sharp interface by a smooth transition of one or more continuous fields across a finite width $\delta$. A **non-conserved order parameter** $\phi$ distinguishes phases or grains (for example $\phi=1$ in solid, $0$ in liquid), and a **conserved field** $c$ represents composition. Interfaces are simply where the fields change; topology changes happen automatically.

The model is built from a free-energy functional of Ginzburg–Landau type:

$$
F=\int_V\left[f(\phi,c,T)+\frac{\kappa_\phi}{2}\lvert\nabla\phi\rvert^2+\frac{\kappa_c}{2}\lvert\nabla c\rvert^2+f_{el}\right]dV
$$

The bulk term $f$ is a double-well (or multi-well) function whose minima are the phases; for quantitative work it is taken from CALPHAD databases (Section 46.6). The gradient terms penalize sharp changes and, together with the barrier height of $f$, set the interface energy $\gamma$ and width $\delta$. The elastic term $f_{el}$ adds misfit and applied stresses.

### Evolution equations

Non-conserved fields relax down the gradient of free energy (the **Allen–Cahn** or time-dependent Ginzburg–Landau equation); conserved fields evolve by diffusion driven by gradients of the chemical potential (the **Cahn–Hilliard** equation):

$$
\frac{\partial\phi}{\partial t}=-L\,\frac{\delta F}{\delta\phi},\qquad \frac{\partial c}{\partial t}=\nabla\cdot\left(M\,\nabla\frac{\delta F}{\delta c}\right)
$$

with interface mobility $L$ and atomic mobility $M$, related to the diffusion coefficient (Chapter 8). Noise terms can be added to model nucleation, although nucleation is usually inserted explicitly using classical nucleation theory (Chapter 9).

> **Status of the principle: Phase-field evolution equations**
> *Derived.* They follow from linear irreversible thermodynamics as the simplest dissipative dynamics that lower the free energy (non-conserved) or conserve mass while lowering it (conserved); quantitative accuracy depends on the input free energies and mobilities and on a thin-interface analysis linking the diffuse model to sharp-interface physics.

### The interface-width problem

Physical interfaces in metals are about 1 nm wide; dendrites are tens of micrometres across. Resolving a 1 nm interface with about five grid points over a 100 μm domain in three dimensions would need $(10^{5}\times5)^3\approx10^{17}$ grid points. Practical models therefore use artificially wide interfaces (0.1–1 μm) and rely on **thin-interface asymptotics** (Karma–Rappel, 1996, and later anti-trapping corrections), which choose the model parameters so that the interface still moves with the correct sharp-interface kinetics despite its exaggerated width. Adaptive mesh refinement and GPU computing extend reach further.

<!-- FIGURE 46.3 | figures/ch46/fig-46-3-phase-field.png | plot | Phase-field description of a moving interface and a simulated solidification dendrite. | Content: (a) order parameter φ vs distance x across an interface (−5δ to +5δ): tanh profile φ = ½[1 − tanh(x/δ)], with δ marked and labels "solid φ = 1" and "liquid φ = 0"; overlaid composition c(x) with solute pile-up ahead of the interface (partition coefficient k = 0.2). (b) 2D false-colour map of a growing dendrite in an undercooled Al–Cu melt, 200 μm × 200 μm field, fourfold anisotropy, primary arm and secondary arms; colour = solute concentration 2–8 wt% Cu, interdendritic enrichment visible; scale bar 50 μm. -->

### Applications across engineering

- **Solidification** (Figure 46.3): dendrite tip radius and velocity, primary and secondary arm spacings and microsegregation in castings and welds (Chapters 9, 38 and 39), and the columnar-to-equiaxed transition in additive manufacturing (Chapter 40).
- **Precipitation and coarsening**: the shape and arrangement of coherent γ′ cuboids in nickel superalloys, which align into rafts under stress at high temperature, and θ′ plates in aluminium alloys, both controlled by elastic misfit energy.
- **Spinodal decomposition**: the interconnected microstructures of Fe–Cr in duplex stainless steels aged at 300–500 °C ("475 °C embrittlement") and of phase-separating glasses and polymer blends.
- **Grain growth and recrystallization**, with many order parameters, one per grain orientation.
- **Martensite and ferroelectric domains**, where the order parameter is a strain or polarization.
- **Fracture**: phase-field fracture models represent a crack as a damage field, letting cracks nucleate, branch and merge without explicit tracking — now used for concrete, rock, composites and battery-electrode particles.
- **Electrochemistry**: lithium dendrite growth and phase separation in LiFePO₄ particles (Chapter 32), corrosion pit growth (Chapter 35).

---

## 46.5 Discrete dislocation dynamics and crystal-plasticity FEM

### Discrete dislocation dynamics

Plastic deformation of crystals is the collective motion of dislocations (Chapters 12 and 13). MD can follow a few dislocations for nanoseconds; a deformed grain contains $10^{12}$–$10^{15}$ m of dislocation line per cubic metre. **Discrete dislocation dynamics (DDD)** treats dislocations as elastic line defects in a continuum, discretized into segments, and computes their motion from the forces acting on them:

1. The stress at each segment from the applied load and from every other segment is computed from linear elasticity (Chapter 12).
2. The force per unit length follows from the **Peach–Koehler** formula $\mathbf f=(\boldsymbol\sigma\cdot\mathbf b)\times\boldsymbol\xi$, with Burgers vector $\mathbf b$ and line direction $\boldsymbol\xi$.
3. A **mobility law**, typically $v=f/B$ for FCC metals with drag coefficient $B\approx10^{-5}$–$10^{-4}\ \mathrm{Pa\,s}$ (from MD), or thermally activated kink-pair motion for BCC screw dislocations, gives segment velocities.
4. **Local rules**, again calibrated on MD, handle core-scale events: junction formation and annihilation, cross-slip, nucleation at sources.

DDD simulations of cubes 5–20 μm on a side reach plastic strains of a few percent and reproduce the formation of dislocation networks and the size effects of micropillars (Chapter 44). They have tested the **Taylor relation** between flow stress and dislocation density,

$$
\tau=\alpha\,\mu\,b\sqrt{\rho}
$$

finding $\alpha\approx0.2$–$0.4$ in FCC metals and explaining it through junction strength, and they have explored fatigue persistent slip bands and dislocation–precipitate interactions. The main limitations are cost — the long-range interactions scale poorly with the number of segments — and reach: strains above a few percent and strain rates below about $10^{2}\ \mathrm{s^{-1}}$ are difficult.

> **Status of the principle: Taylor hardening relation**
> *Empirical.* The $\sqrt\rho$ dependence is supported by theory and simulation of forest hardening; the coefficient $\alpha$ is fitted and varies with dislocation arrangement, crystal structure and strain rate.

**Worked example — linking dislocation density to flow stress in copper.** For copper, $\mu=48$ GPa, $b=0.256$ nm and $\alpha=0.3$. At an annealed density of $\rho=10^{12}\ \mathrm{m^{-2}}$,

$$
\tau=0.3\times48\times10^{9}\times0.256\times10^{-9}\times\sqrt{10^{12}}=3.7\ \mathrm{MPa}
$$

and the polycrystal flow stress, using the Taylor factor $M=3.06$ for an untextured FCC aggregate, is $\sigma=M\tau=11$ MPa. After moderate cold work ($\rho=10^{14}\ \mathrm{m^{-2}}$), $\tau=37$ MPa and $\sigma=113$ MPa; after heavy cold work ($\rho=10^{15}\ \mathrm{m^{-2}}$), $\tau=117$ MPa and $\sigma=357$ MPa. These match the measured range for copper from fully annealed to hard-drawn wire, and show the sort of constitutive input — a hardening law tied to a physical state variable — that DDD supplies to crystal-plasticity models.

### Crystal-plasticity finite elements

At the scale of a polycrystal, individual dislocations are replaced by **slip rates** on each slip system. **Crystal-plasticity finite-element (CPFEM)** models mesh a representative volume of grains — taken from EBSD maps or synthetic microstructures — and in each integration point solve:

- **Kinematics**: the deformation gradient is decomposed into elastic and plastic parts, $\mathbf F=\mathbf F_e\mathbf F_p$, with the plastic part produced by slip on systems $\alpha$ (12 for FCC $\{111\}\langle110\rangle$, up to 48 for BCC, basal, prismatic and pyramidal for HCP).
- **Flow rule**: for example the phenomenological power law

$$
\dot\gamma^{\alpha}=\dot\gamma_0\left\lvert\frac{\tau^{\alpha}}{\tau_c^{\alpha}}\right\rvert^{1/m}\mathrm{sgn}\left(\tau^{\alpha}\right)
$$

where $\tau^{\alpha}$ is the resolved shear stress (Schmid's law, Chapter 13), $\tau_c^{\alpha}$ the critical resolved shear stress and $m$ a rate sensitivity (0.01–0.05 at room temperature).
- **Hardening**: evolution of $\tau_c^{\alpha}$ with slip on all systems, through a hardening matrix, or of dislocation densities per system linked by the Taylor relation (physically based models).

Figure 46.4 shows a typical result: stress concentrates in grains whose orientation makes them elastically and plastically hard. CPFEM predicts texture evolution in rolling and deep drawing (and hence earing of aluminium beverage-can stock), the anisotropy of HCP magnesium and titanium sheet, the stress and strain hot spots at grain boundaries where fatigue cracks initiate in turbine-disc alloys, and the response of additively manufactured parts with columnar grains. Spectral (FFT-based) solvers handle periodic microstructures with millions of voxels quickly. Inputs — critical resolved shear stresses of each slip system and hardening parameters — come from single-crystal tests, micropillar compression (Chapter 44) and DDD.

<!-- FIGURE 46.4 | figures/ch46/fig-46-4-cpfem-polycrystal.png | schematic | Crystal-plasticity finite-element simulation of a polycrystal under uniaxial tension. | Content: (a) 3D representative volume of ~100 grains coloured by inverse-pole-figure orientation (as from EBSD), with load arrows along x. (b) Same volume after 5 % applied strain coloured by von Mises equivalent stress 150–450 MPa (Ti-6Al-4V-like), hot spots at selected grain boundaries and triple junctions highlighted; grains with c-axis near load axis labelled "hard", others "soft". (c) Small plot: macroscopic stress–strain curve 0–5 % from the simulation vs experiment points. -->

> **Status of the principle: Crystal-plasticity constitutive laws**
> *Empirical.* Kinematics are exact continuum mechanics, but flow and hardening laws are phenomenological or physically motivated fits; their parameters must be calibrated and the model validated against measured stress–strain curves, textures or local strain maps (digital image correlation).

---

## 46.6 CALPHAD and computational thermodynamics

### The method

Engineering alloys contain many elements: a nickel superalloy has 8–12, a tool steel 6–10, a solder 3–5. Their phase diagrams cannot be measured exhaustively. The **CALPHAD** (CALculation of PHAse Diagrams) method models the Gibbs energy of every phase as a function of temperature, pressure and composition, fits the model parameters to experimental data (phase equilibria, enthalpies, heat capacities, activities) and DFT energies for the binary and ternary subsystems, and then predicts equilibria in multicomponent systems by minimizing total Gibbs energy (Chapter 7).

For a substitutional solution phase,

$$
G_m=\sum_i x_i\,{}^{0}G_i+RT\sum_ix_i\ln x_i+{}^{ex}G_m
$$

where ${}^{0}G_i$ are the Gibbs energies of the pure components in that structure (the "lattice stabilities", tabulated as polynomials in $T$), the second term is ideal mixing, and the excess term is expanded as a **Redlich–Kister polynomial**:

$$
{}^{ex}G_m=\sum_i\sum_{j>i}x_ix_j\sum_{\nu}L_{ij}^{(\nu)}\left(x_i-x_j\right)^{\nu}+\dots
$$

with interaction parameters $L^{(\nu)}=a+bT+\dots$, plus ternary terms. Ordered phases, interstitial solutions and intermetallics use the **compound-energy formalism**, with sublattices (for example $(\mathrm{Fe,Cr,Ni})_1(\mathrm{C,N,Va})_3$ for austenite with carbon and nitrogen on octahedral interstitial sites). Magnetic contributions are added for iron, nickel and cobalt.

> **Status of the principle: CALPHAD Gibbs-energy models**
> *Empirical.* The minimization of Gibbs energy is fundamental thermodynamics, but the model parameters are fitted to data; extrapolation to multicomponent compositions is reliable when binary and ternary descriptions are sound, and least reliable for phases or composition regions without experimental or DFT input.

**Worked example — a miscibility gap from the regular-solution model.** The simplest excess model, $^{ex}G_m=\Omega x(1-x)$ (a single temperature-independent $L^{(0)}=\Omega$), describes a binary solution with a miscibility gap when $\Omega>0$. The critical temperature is where the curvature of $G_m$ vanishes at $x=0.5$: $T_c=\Omega/2R$. For $\Omega=20$ kJ/mol, $T_c=20{,}000/(2\times8.314)=1{,}203$ K. At 1,000 K, the Gibbs energy of mixing at $x=0.5$ is

$$
\Delta G_{mix}=20{,}000\times0.25+8.314\times1000\times(0.5\ln0.5+0.5\ln0.5)=5{,}000-5{,}763=-763\ \mathrm{J\,mol^{-1}}
$$

negative, yet the solution is not stable: the curve has two minima, and the common-tangent construction gives the equilibrium compositions (the **binodal**) from $\ln[x/(1-x)]=\Omega(2x-1)/RT$, which yields $x=0.169$ and $0.831$. The **spinodal**, where $\partial^2G/\partial x^2=0$, lies at $x(1-x)=RT/2\Omega=0.208$, giving $x=0.295$ and $0.705$. Alloys between 0.295 and 0.705 decompose spontaneously by spinodal decomposition; those between the binodal and spinodal need nucleation (Chapters 7, 9 and 10). A real CALPHAD assessment has many such parameters, temperature-dependent and asymmetric, but the logic is the same: a Gibbs-energy model for each phase, minimized to give phase fractions and compositions (Figure 46.5).

<!-- FIGURE 46.5 | figures/ch46/fig-46-5-regular-solution.png | plot | Regular-solution model with Ω = 20 kJ/mol: Gibbs energy of mixing curves and the resulting miscibility gap. | Content: (a) ΔG_mix (J/mol, −2,500 to +500) vs x from 0 to 1 at T = 800, 1,000, 1,203 and 1,400 K; at 1,000 K common tangent touching at x = 0.169 and 0.831, inflection points at 0.295 and 0.705 marked. (b) Temperature 600–1,300 K vs x: binodal (solid) and spinodal (dashed) curves meeting at Tc = 1,203 K, x = 0.5; horizontal tie-line at 1,000 K from 0.169 to 0.831; regions labelled "single phase", "nucleation and growth", "spinodal decomposition". -->

### Tools and uses

Commercial and open software (Thermo-Calc, FactSage, Pandat, OpenCalphad, pycalphad) with assessed databases for steels, nickel, aluminium, titanium and magnesium alloys, solders, oxides and slags is now part of routine industrial alloy and process development. Typical outputs:

- equilibrium phase fractions and compositions versus temperature (for example the γ′ solvus of a superalloy, which sets the solution-treatment window);
- **Scheil–Gulliver** solidification paths, assuming no diffusion in the solid and complete mixing in the liquid, which predict microsegregation, freezing range and hot-cracking susceptibility of castings and welds;
- driving forces for nucleation of unwanted phases (σ and Laves phases in superalloys and stainless steels; Chapter 16);
- slag and oxide equilibria in steelmaking, glass and refractory design.

CALPHAD extends to kinetics through **mobility databases**: DICTRA-type models solve diffusion with CALPHAD thermodynamics to predict carburizing profiles, interdiffusion in coatings and homogenization times; **precipitation models** (Kampmann–Wagner numerical approaches) combine classical nucleation, growth and coarsening with CALPHAD driving forces to predict precipitate size distributions during ageing — the γ′ distribution of the opening problem — and supply free energies to phase-field models.

---

## 46.7 Multiscale modelling and ICME

### Linking scales

The methods of this chapter and of Chapter 45 form a chain in which each passes parameters upward:

| From | To | Information passed |
|---|---|---|
| DFT | Interatomic potentials, cluster expansions | Energies and forces of many configurations |
| DFT | kMC, CALPHAD | Migration barriers, formation energies of end-members and metastable phases |
| MD | DDD | Dislocation mobilities, junction strengths, cross-slip rates |
| MD, kMC | Phase field | Interface energies and mobilities, diffusion coefficients |
| CALPHAD | Phase field, precipitation models | Free energies, mobilities, driving forces |
| DDD, micropillar tests | Crystal plasticity | Hardening laws, critical resolved shear stresses |
| Phase field, precipitation models | Crystal plasticity | Precipitate size and fraction, grain structure |
| Crystal plasticity | Component FEM | Homogenized anisotropic constitutive laws, fatigue indicators |

This is **hierarchical** (sequential) multiscale modelling: each method runs separately and hands over parameters. **Concurrent** multiscale methods run two descriptions simultaneously in one simulation — the quasicontinuum method treats atoms explicitly near a crack tip and as a coarse finite-element continuum elsewhere; QM/MM embeds a DFT region in a classical MD region to model bond breaking at a crack tip or a catalytic site. Concurrent coupling is powerful but must avoid spurious forces and wave reflections at the handshake region.

### Integrated computational materials engineering

**Integrated computational materials engineering (ICME)** applies this chain to product development. The idea, given impetus by a 2008 US National Academies report and by the 2011 Materials Genome Initiative, is to treat the material as a designed variable alongside geometry, linking process models, microstructure models and property models so that alloy composition, processing and component design are optimized together (Figure 46.6). Demonstrated examples include:

- **Cast aluminium engine blocks and heads.** An automotive ICME programme coupled casting simulation, CALPHAD-based solidification and precipitation models and property models to predict local yield strength and fatigue life across a cast cylinder head, shortening development cycles and cutting prototype iterations.
- **Computationally designed steels.** Ultra-high-strength, corrosion-resistant landing-gear steels were designed with CALPHAD and precipitation models to replace cadmium-plated 300M steel, and reached aerospace qualification in a fraction of the traditional time.
- **Nickel superalloy discs.** Models of forging, heat treatment, γ′ precipitation and grain size predict location-specific properties within a turbine disc, used in its life assessment.
- **Additive manufacturing.** Thermal models of the melt pool feed solidification and phase-field models to predict grain structure and residual stress, which feed crystal-plasticity and fatigue models (Chapter 40).

<!-- FIGURE 46.6 | figures/ch46/fig-46-6-icme-chain.png | flowchart | An ICME chain for a precipitation-strengthened turbine disc: process → microstructure → properties → performance, with the simulation method at each link. | Content: four column headers "Process", "Microstructure", "Properties", "Performance". Boxes: Process: "forging FEM (T, strain, strain rate)", "heat-treatment thermal model"; Microstructure: "CALPHAD + precipitation model: γ′ size and fraction", "phase-field / grain-growth: grain size"; Properties: "crystal plasticity + DDD-informed hardening: yield, flow", "fatigue indicator from grain-scale hot spots"; Performance: "disc FEM: creep, LCF life, burst margin". Arrows left to right; dotted arrows back from Performance to Process labelled "design optimization". Lower band: "DFT → potentials → MD inputs" feeding CALPHAD and DDD boxes; side band "validation: experiments at each link (DSC, SEM, micropillar, creep tests)". -->

### Verification, validation and uncertainty

A chain of models compounds uncertainties. ICME practice therefore distinguishes:

- **Verification**: is the model solved correctly (convergence, code testing)?
- **Validation**: does the model represent reality for the intended use (comparison with experiments designed for the purpose, at each link and at the end of the chain)?
- **Uncertainty quantification**: how do uncertainties in inputs (potential parameters, CALPHAD assessments, mobility values) propagate to outputs (yield strength, life)? Monte Carlo sampling of inputs, sensitivity analysis and surrogate models (Chapter 47) make this tractable.

A useful discipline is to state, for every predicted property, which link limits its accuracy. In a precipitation-strengthened alloy, the strength prediction is often limited not by the dislocation model but by the precipitate size distribution, which depends on interfacial energy — a parameter that is hard to measure, uncertain by a factor of two in DFT and MD, and enters nucleation rates exponentially. Identifying such bottlenecks directs experimental effort to where it matters most.

> **Status of the principle: Integrated computational materials engineering**
> *Approximate.* ICME predictions are as reliable as the weakest validated link in the chain; they are most effective for interpolation within well-characterized alloy families and processes, and require experimental calibration and validation when extrapolated to new chemistries or processing routes.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are the energies, forces and barriers that parameterize these models computed from electrons? | Chapter 45 |
| How do machine-learned potentials and surrogate models extend the reach and accuracy of MD, kMC and ICME? | Chapter 47 |
| How are simulated properties used to select materials and processes in design? | Chapter 48 |
| What thermodynamic principles and phase diagrams do CALPHAD models encode? | Chapters 6 and 7 |
| What diffusion, nucleation and transformation theories underlie kMC, phase-field and precipitation models? | Chapters 8, 9 and 10 |
| What dislocation physics and strengthening mechanisms do DDD and crystal plasticity represent? | Chapters 12 and 13 |
| How are simulated microstructures and stress–strain curves validated by in-situ experiments and micropillars? | Chapter 44 |
| How do superalloys, steels and aluminium alloys benefit from computational design? | Chapters 15, 16 and 33 |
| How are solidification and process simulations used in casting, welding and additive manufacturing? | Chapters 38, 39 and 40 |

**Next:** Chapter 47 asks how the vast data generated by experiments and by the simulations of Chapters 45 and 46 can be organized into databases and used by machine learning to predict properties, build better potentials and design materials directly.
