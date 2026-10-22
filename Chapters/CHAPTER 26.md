# Chapter 26 — Semiconductor Materials

*Part VI · Physical and Functional Properties*

An electric-vehicle maker redesigns the traction inverter of its next car. The old inverter used silicon IGBTs; the new one uses silicon carbide MOSFETs. Nothing about the circuit topology changes, yet the inverter loses about half as much energy, the cooling plate shrinks, the battery can be a few kilowatt-hours smaller for the same range, and the system voltage rises from 400 V to 800 V so the charging cable can be thinner. Every one of those gains traces back to three numbers that belong to a crystal, not a circuit: a band gap three times that of silicon, a breakdown field nearly ten times higher, and a thermal conductivity three times higher. The cost traces back to materials too: SiC crystals must be grown from vapour at above 2000 °C, more slowly than silicon by two orders of magnitude, and every wafer carries defects that a silicon fab would reject. A semiconductor device is a materials system before it is a circuit element.

This chapter covers semiconductors as materials: where band gaps and effective masses come from, how carrier concentrations are set by temperature and doping, how carriers move and recombine, which material families exist and why, how junctions and heterostructures are built, and how crystal growth and doping put the required structure into the solid. Device physics and circuit design belong elsewhere; the *Materials Core (EEE)* book, Chapters 10–13, treats each topic at greater depth.

> **Why is silicon, a mediocre semiconductor in almost every single property, the basis of nearly all electronics?**
> **Why can a SiC or GaN transistor block 1200 V across a layer ten times thinner than silicon needs?**
> **Why do LEDs and lasers use GaAs, GaN and their alloys, but not silicon?**
> **Why does a few parts per billion of iron ruin a solar wafer?**

| Concept | Engineering destination |
|---|---|
| Bands, gaps, effective mass, density of states | Choosing a semiconductor for power, RF, light emission, detection or sensing |
| Intrinsic and extrinsic carrier statistics | Doping design; maximum operating temperature of devices and sensors |
| Mobility, drift, diffusion | Transistor speed, on-resistance, solar-cell collection |
| Recombination and lifetime | Solar-cell efficiency, LED efficiency, switching speed of power diodes |
| Material families | Silicon chips, SiC and GaN power converters, III–V lasers, oxide display backplanes, organic LEDs |
| Junctions, heterostructures, interfaces | Diodes, transistors, quantum-well lasers, high-electron-mobility transistors |
| Crystal growth and doping | Wafer cost and quality; yield; the processing chain of Chapter 41 |

**Roadmap.** Band structure essentials (26.1) → intrinsic and extrinsic carrier statistics (26.2) → mobility, drift, diffusion and recombination (26.3) → semiconductor families (26.4) → junctions, heterostructures and interfaces (26.5) → crystal growth and doping (26.6).

---

## 26.1 Band structure essentials

### From atomic levels to bands

When $N$ atoms come together to form a crystal, each atomic energy level splits into $N$ closely spaced levels because the electron wavefunctions overlap. For $N\sim10^{23}$ these form quasi-continuous **energy bands** separated by **gaps** where no electron states exist. In a periodic crystal the states are Bloch waves labelled by a wavevector $\mathbf k$, and the band structure $E(\mathbf k)$ is the dispersion relation of electrons in the crystal. The quantum mechanics is the business of the Engineering Physics book; what the materials engineer needs is its consequences.

Whether a solid conducts depends on how the bands are filled at 0 K:

- **Metals** have a partly filled band. Electrons at the top of the filled states (the Fermi energy) can accept infinitesimal energy from a field, so conduction is easy and the carrier density is fixed at about $10^{22}$–$10^{23}$ cm$^{-3}$ (Chapter 25).
- **Insulators and semiconductors** have a completely filled **valence band** and an empty **conduction band** separated by a **band gap** $E_g$. Conduction requires electrons to be promoted across the gap, leaving behind **holes** — vacancies in the valence band that behave as positive carriers.

The distinction between a semiconductor and an insulator is one of degree. With $E_g$ below about 3–4 eV, thermal excitation or doping can produce useful carrier densities; silicon (1.12 eV) is a semiconductor, diamond (5.5 eV) an insulator that can be doped into a wide-gap semiconductor, and SiO$_2$ (about 9 eV) an insulator. In covalent semiconductors the valence band derives from bonding sp$^3$ orbitals and the conduction band from antibonding orbitals, so the gap is a measure of bond strength: it decreases down a column of the periodic table (C 5.5, Si 1.12, Ge 0.66, grey Sn 0 eV) as bonds lengthen, and increases with ionicity in the sequence Ge (0.66) → GaAs (1.42) → ZnSe (2.7 eV), which share almost the same lattice constant.

### Direct and indirect gaps

The conduction-band minimum and valence-band maximum need not lie at the same $\mathbf k$ (Figure 26.1). In a **direct-gap** semiconductor (GaAs, InP, GaN, ZnO, most III–V and II–VI compounds) they do, and an electron can drop across the gap emitting a photon, because the photon carries negligible momentum. In an **indirect-gap** semiconductor (Si, Ge, SiC, diamond, AlAs) the minima are offset, and recombination needs a phonon to supply the momentum difference; radiative recombination is then about $10^4$–$10^6$ times slower, and other processes win. This single feature of the band structure decides which materials can be light emitters: GaAs and GaN make lasers and LEDs, silicon does not (Chapter 28). For absorption the difference is weaker but still important: silicon absorbs weakly near its gap and solar wafers must be 100–180 µm thick, while a direct-gap absorber such as CdTe or a halide perovskite absorbs the same light in about 1 µm (Chapter 32).

<!-- FIGURE 26.1 | figures/ch26/fig-26-1-direct-indirect-bands.png | band-diagram | Direct and indirect band gaps: in GaAs an electron can emit a photon directly; in Si the momentum mismatch requires a phonon. | Content: two side-by-side E–k panels, k from -pi/a to +pi/a (labels L, Gamma, X). Left GaAs: parabolic conduction-band minimum at Gamma 1.42 eV above valence-band maximum (heavy and light hole bands at Gamma); vertical arrow labelled photon hv = Eg. Right Si: valence-band maximum at Gamma, conduction-band minimum near X (0.85 of the way to X) at 1.12 eV; vertical arrow at Gamma labelled direct gap 3.4 eV; diagonal arrow from CB minimum to VB maximum labelled phonon + photon. Curvature of the GaAs CB minimum visibly sharper (m* = 0.067 m0) than the Si CB valleys (m* about 0.26 m0 conductivity mass). -->

### Effective mass

Near a band minimum, $E(\mathbf k)$ is approximately parabolic, and an electron responds to forces as if it were a free particle with an **effective mass**

$$
\frac{1}{m^*}=\frac{1}{\hbar^2}\frac{d^2E}{dk^2}
$$

Sharp band curvature means a light carrier. The effective mass enters every transport and statistics formula below: lighter electrons are more mobile and give a lower density of states. Values span a wide range: $m_e^*=0.067m_0$ in GaAs, $0.041m_0$ in In$_{0.53}$Ga$_{0.47}$As, $0.26m_0$ (conductivity mass) in Si, $0.2$–$0.4m_0$ in SiC and GaN; holes are usually heavier ($0.3$–$0.8m_0$), which is why p-type material and p-channel devices are slower almost everywhere.

> **Status of the principle: Effective-mass approximation**
> *Approximate.* It replaces the band curvature near an extremum with a constant mass. It holds for carriers within a few $k_BT$ of a band edge and fails for hot carriers far up the band, where non-parabolicity and transfer to other valleys (the Gunn effect in GaAs) appear.

### Density of states and the Fermi–Dirac distribution

How many carriers occupy a band depends on how many states there are and on how likely each is to be filled. For a parabolic band in three dimensions the **density of states** per unit energy and volume is

$$
g_c(E)=\frac{1}{2\pi^2}\left(\frac{2m_e^*}{\hbar^2}\right)^{3/2}\sqrt{E-E_c}
$$

rising as the square root of energy above the band edge $E_c$ (a similar expression holds below the valence-band edge $E_v$). In quantum wells (two dimensions) the density of states becomes a staircase, and in quantum wires and dots it becomes spiky — the basis of the size effects of Chapter 30. Occupation follows the **Fermi–Dirac distribution**,

$$
f(E)=\frac{1}{1+\exp[(E-E_F)/k_BT]}
$$

where the **Fermi level** $E_F$ is the electrochemical potential of the electrons: the energy at which a state is half-filled. In thermal equilibrium $E_F$ is constant throughout a system of joined materials, which is the single principle that sets band bending at every junction in Section 26.5.

> **Status of the principle: Fermi–Dirac statistics and constant $E_F$ in equilibrium**
> *Fundamental.* It follows from the Pauli principle and equilibrium thermodynamics; a gradient of $E_F$ is what drives current, so in equilibrium it must vanish.

---

## 26.2 Intrinsic and extrinsic semiconductors; carrier statistics

### Intrinsic carriers

When the Fermi level lies more than a few $k_BT$ inside the gap, Fermi–Dirac statistics reduce to Boltzmann statistics and the electron and hole concentrations become

$$
n=N_c\exp\!\left(-\frac{E_c-E_F}{k_BT}\right),\qquad p=N_v\exp\!\left(-\frac{E_F-E_v}{k_BT}\right)
$$

where $N_c$ and $N_v$ are effective densities of states (of order $10^{19}$ cm$^{-3}$ at 300 K, scaling as $(m^*T)^{3/2}$). Their product is independent of the Fermi level, and therefore of doping:

$$
np=n_i^2=N_cN_v\exp\!\left(-\frac{E_g}{k_BT}\right)
$$

This is the **law of mass action** for carriers, an equilibrium constant for the reaction "bond ⇌ electron + hole". In a pure (intrinsic) crystal $n=p=n_i$, the **intrinsic carrier concentration**.

> **Status of the principle: Law of mass action $np=n_i^2$**
> *Derived.* It follows from Boltzmann statistics in equilibrium. It fails in degenerate material (doping above about $10^{19}$ cm$^{-3}$, where full Fermi–Dirac statistics and band-gap narrowing are needed) and whenever carriers are injected or generated out of equilibrium — in an illuminated solar cell or a forward-biased diode, $np\gg n_i^2$.

**Worked example — why silicon power electronics stops at about 150 °C.** For silicon take $N_c=2.86\times10^{19}$ and $N_v=3.10\times10^{19}$ cm$^{-3}$, $E_g=1.12$ eV and $k_BT=0.02585$ eV at 300 K. Then

$$
n_i=\sqrt{N_cN_v}\exp\!\left(-\frac{E_g}{2k_BT}\right)=(2.98\times10^{19})\exp(-21.66)=1.2\times10^{10}\ \mathrm{cm^{-3}}
$$

close to the accepted value of $1.0\times10^{10}$ cm$^{-3}$ (the difference reflects uncertainty in $N_c$ and $N_v$). The exponential makes $n_i$ climb steeply with temperature. Allowing for the $T^{3/2}$ factor and the slight narrowing of the gap with temperature (1.09 eV at 150 °C, 1.04 eV at 300 °C), $n_i$ reaches $1.6\times10^{13}$ cm$^{-3}$ at 150 °C and $2\times10^{15}$ cm$^{-3}$ at 300 °C. A 1200 V silicon device has a drift layer doped to only about $10^{14}$ cm$^{-3}$ (Section 26.4), so above about 200 °C intrinsic carriers outnumber the dopant electrons, leakage current soars and the junction can no longer block. For 4H-SiC ($E_g=3.26$ eV, $N_c=1.7\times10^{19}$, $N_v=2.5\times10^{19}$ cm$^{-3}$) the same formula gives $n_i\approx10^{-8}$ cm$^{-3}$ at 300 K and still only about $10^{5}$ cm$^{-3}$ at 300 °C. The band gap sets the maximum junction temperature, which is why wide-gap materials are used in down-hole oil and geothermal sensors, aero-engine electronics and Venus-lander circuits, as well as in power converters.

### Donors, acceptors and the hydrogen model

Substituting a group-V atom (P, As, Sb) for silicon leaves one valence electron that is not needed for bonding. It is bound to the donor ion like the electron of a hydrogen atom, but in a medium of permittivity $\varepsilon_r$ and with mass $m^*$, so its binding energy is

$$
E_d\approx13.6\ \mathrm{eV}\times\frac{m^*/m_0}{\varepsilon_r^2}
$$

For silicon ($m^*=0.26m_0$, $\varepsilon_r=11.7$) this gives 26 meV; measured values are 39–54 meV for Sb, P and As. Since $k_BT=26$ meV at room temperature, almost every donor is ionized and contributes one free electron: silicon doped with $10^{16}$ P cm$^{-3}$ has $n\approx10^{16}$ cm$^{-3}$ — a million times its intrinsic value — and $p=n_i^2/n\approx10^4$ cm$^{-3}$. Group-III **acceptors** (B, Al, Ga) accept an electron from the valence band and create a hole in the same way. Shallow dopants exist in silicon because its permittivity is high and its effective mass small; in wide-gap materials the hydrogen model predicts deeper levels (Mg acceptors in GaN lie about 0.17–0.2 eV above the valence band, so only a few per cent ionize at room temperature), which is why p-type GaN is hard and why some oxides can only be doped n-type.

Impurities with levels near mid-gap — Au, Fe, Cu, Ni in silicon, or native defects such as vacancies — are **deep levels**. They do not usefully dope; they trap carriers and catalyse recombination (Section 26.3).

### Three temperature regimes

In an n-type sample with donor density $N_d$ the electron concentration passes through three regimes (Figure 26.2):

- **Freeze-out** at low temperature, where electrons fall back onto donors; $n$ rises exponentially with $T$ with an activation energy of about $E_d/2$.
- **Extrinsic (saturation)** range, $n\approx N_d$, flat over hundreds of kelvin. Devices are designed to work here.
- **Intrinsic** range, where $n_i$ exceeds $N_d$ and $n$ rises again with an activation energy $E_g/2$.

The position of the Fermi level follows: in the extrinsic range $E_c-E_F=k_BT\ln(N_c/N_d)$, which for $N_d=10^{16}$ cm$^{-3}$ in silicon is 0.21 eV. When both donors and acceptors are present, they **compensate**: the net carrier density is $\lvert N_d-N_a\rvert$, but both species still scatter carriers, so compensated material has low mobility. Upgraded metallurgical silicon for solar cells, which contains both boron and phosphorus, suffers exactly this.

<!-- FIGURE 26.2 | figures/ch26/fig-26-2-carrier-vs-temperature.png | plot | Electron concentration in n-type silicon against temperature: freeze-out, extrinsic and intrinsic regimes, with the intrinsic concentration of four semiconductors. | Content: x-axis 1000/T from 1 to 20 K^-1 (top axis temperature in C, from 700 down to -220); y-axis log10 n from 1e8 to 1e18 cm^-3. Bold curve: Si with Nd = 1e15 cm^-3 — freeze-out slope at the right (below about 100 K), flat plateau at 1e15 between about 150 and 500 K, intrinsic rise at the left. Thin dashed lines: n_i(T) for Ge (2e13 at 300 K), Si (1e10 at 300 K), GaAs (2e6 at 300 K), 4H-SiC (about 1e-8 at 300 K, entering the plot only above about 500 C). Horizontal dotted line at Nd. Shade the useful device window for Si. -->

---

## 26.3 Mobility, drift, diffusion and recombination

### Drift and mobility

In a field, carriers drift with velocity $v=\mu E$, so the conductivity of a semiconductor is

$$
\sigma=q(n\mu_n+p\mu_p)
$$

With both $n$ and $\mu$ variables, semiconductors are the materials where conductivity is designed rather than accepted. Mobility $\mu=q\tau/m^*$ is limited by two main scattering mechanisms: **lattice (phonon) scattering**, which grows with temperature ($\mu_L\propto T^{-3/2}$ in an ideal case; closer to $T^{-2.2}$ for electrons in Si), and **ionized-impurity scattering** from the dopants themselves, which grows with doping and decreases with temperature as faster carriers are deflected less. Matthiessen's rule (Chapter 25) combines them, $1/\mu=1/\mu_L+1/\mu_I$. The empirical mobility–doping curves of Figure 26.3 are the semiconductor designer's working data: silicon electron mobility falls from 1400 cm²/(V s) in pure material to about 1200 at $10^{16}$ cm$^{-3}$ and below 100 at $10^{19}$ cm$^{-3}$.

At high fields the drift velocity stops rising with field and **saturates** near $10^7$ cm/s in Si, because carriers lose energy to optical phonons as fast as they gain it. Saturation velocity, not low-field mobility, limits short-channel transistors. GaN's saturation velocity (about $2.5\times10^7$ cm/s) and GaAs's velocity overshoot are why those materials serve microwave amplifiers.

<!-- FIGURE 26.3 | figures/ch26/fig-26-3-mobility-vs-doping.png | plot | Carrier mobility falls with doping as ionized-impurity scattering adds to lattice scattering. | Content: x-axis total dopant concentration 1e13 to 1e20 cm^-3 (log); y-axis mobility 10 to 10000 cm^2/(V s) (log). Curves at 300 K (Caughey–Thomas form): Si electrons (1417 at low doping, about 1200 at 1e16, 260 at 1e18, about 90 at 1e19); Si holes (470, 410 at 1e16, 150 at 1e18, 60 at 1e19); GaAs electrons (8500 at low doping, about 6000 at 1e16, 2400 at 1e18); 4H-SiC electrons (about 950 at low doping, 400 at 1e18). Annotate the lattice-limited plateau and the impurity-limited roll-off. -->

### Diffusion and the Einstein relation

Carriers also move down concentration gradients, giving diffusion currents $J_n=qD_n\,dn/dx$ (Fick's first law, Chapter 8). Drift and diffusion are two faces of the same random motion, and their coefficients are linked by the **Einstein relation**

$$
\frac{D}{\mu}=\frac{k_BT}{q}
$$

which is 25.9 mV at 300 K. It is the semiconductor form of the Nernst–Einstein relation of Chapter 25.

> **Status of the principle: Einstein relation $D/\mu=k_BT/q$**
> *Derived.* It follows from requiring zero net current in equilibrium with Boltzmann statistics. It is modified in degenerate material and for hot carriers far from equilibrium.

### Generation, recombination and lifetime

Excess carriers created by light or injection decay back to equilibrium by **recombination**, with a characteristic **minority-carrier lifetime** $\tau$. Three routes exist:

- **Radiative recombination** — an electron drops across the gap and emits a photon. Fast in direct-gap materials (nanoseconds at high injection in GaAs), negligible in indirect-gap Si. It is the useful process in LEDs and lasers.
- **Shockley–Read–Hall (SRH) recombination** — via a deep trap level, which captures an electron and then a hole. Its rate is proportional to the trap density, and traps near mid-gap are the most effective. This is the dominant loss in silicon and in defective wide-gap crystals, and the reason transition metals are so damaging: interstitial iron at $10^{12}$ cm$^{-3}$ — about 20 parts per trillion — reduces the lifetime of p-type silicon to a few microseconds.
- **Auger recombination** — the energy goes to a third carrier rather than a photon. It scales as the cube of carrier density and dominates in heavily doped regions and in LEDs at high current (one cause of efficiency droop in GaN LEDs).

The **diffusion length** $L=\sqrt{D\tau}$ is the average distance a minority carrier travels before recombining. It is the materials parameter that decides whether a solar cell collects the carriers generated deep in its absorber.

**Worked example — the solar wafer and its lifetime.** An n-type Czochralski silicon wafer, doped $10^{16}$ cm$^{-3}$, has hole (minority) mobility $\mu_p\approx450$ cm²/(V s). The Einstein relation gives $D_p=0.02585\times450=11.6$ cm²/s. With a lifetime of 10 µs (a moderately contaminated wafer):

$$
L_p=\sqrt{D_p\tau}=\sqrt{11.6\times10\times10^{-6}}=1.08\times10^{-2}\ \mathrm{cm}=108\ \mu\mathrm m
$$

which is shorter than the 160 µm wafer, so carriers generated at the back by long-wavelength light recombine before reaching the junction. A high-quality n-type wafer with $\tau=1$ ms has $L_p=1.08$ mm, more than six times the wafer thickness, and nearly every carrier is collected. The difference — achieved by gettering iron to the surface, passivating the surfaces with Al$_2$O$_3$ or SiN$_x$, and choosing n-type material, which is less sensitive to iron and free of the boron–oxygen defect that degrades p-type cells — is a large part of why commercial cell efficiency rose from 17 % to over 24 % in a decade.

---

## 26.4 Semiconductor families: Si, Ge, III–V, SiC, GaN, oxides, organics

### A comparison

| Material | $E_g$ (eV), type | $\mu_n$ (cm²/(V s)) | $\varepsilon_r$ | $E_{\mathrm{crit}}$ (MV/cm) | $k$ (W/(m K)) | Main uses |
|---|---|---|---|---|---|---|
| Si | 1.12, indirect | 1400 | 11.7 | 0.3 | 150 | Logic, memory, sensors, PV, power to 1.7 kV |
| Ge | 0.66, indirect | 3900 | 16.0 | 0.1 | 60 | IR optics and detectors, SiGe channels |
| GaAs | 1.42, direct | 8500 | 12.9 | 0.4 | 46–55 | RF front ends, lasers, space PV |
| InP | 1.34, direct | 5400 | 12.5 | 0.5 | 68 | Telecom lasers and detectors, high-speed electronics |
| In$_{0.53}$Ga$_{0.47}$As | 0.74, direct | 12 000 | 13.9 | 0.2 | 5 | 1.55 µm detectors, HEMT channels |
| 4H-SiC | 3.26, indirect | 950 | 9.7 | 2.5–3 | 370–490 | Power devices 650 V–10 kV, harsh-environment sensors |
| GaN | 3.4, direct | 1000 (2000 in 2DEG) | 9.0 | 3.3 | 130–230 | Blue/white LEDs, lasers, RF and fast power switches |
| β-Ga$_2$O$_3$ | 4.8, (indirect) | 200 | 10 | 8 (theory) | 11–27 | Developmental ultra-high-voltage power |
| Diamond | 5.5, indirect | 2000 | 5.7 | 10 | 2000 | Heat spreaders, radiation detectors |
| ZnO | 3.37, direct | 200 | 8.7 | — | 50 | Varistors, transparent electrodes, UV sensors |
| a-IGZO (amorphous oxide) | 3.0–3.5 | 10–20 | 10–16 | — | 1–2 | Display backplane transistors |
| a-Si:H | 1.7 (mobility gap) | ≈1 | 11 | — | 1–2 | Large-area displays, detectors (largely superseded) |
| Organic (small molecule / polymer) | 1.5–3 (HOMO–LUMO) | $10^{-3}$–10 | 3–4 | — | 0.2 | OLED displays, flexible electronics, OPV |

*Table 26.1 — Properties of semiconductor families at 300 K (typical values; mobility for low-doped material, field-effect mobility for amorphous and organic films).*

### Silicon and germanium

Silicon's dominance is not due to any outstanding electronic property: its mobility is modest, its gap indirect, its breakdown field low. It wins on materials and processing grounds. Silicon is the second most abundant element in the crust; it can be purified to eleven nines and grown as dislocation-free crystals 300 mm in diameter (Section 26.6); and above all it forms a native oxide, SiO$_2$, that is an excellent insulator with an interface that can be passivated to fewer than $10^{10}$ defect states per cm² — a property no other semiconductor matches. Silicon is also mechanically strong (it is the structural material of MEMS accelerometers and pressure sensors, with a yield strength above 1 GPa in small structures) and a good thermal conductor. Germanium, with higher mobility and a smaller gap, was the first transistor material but lost because its oxide is water-soluble and its $n_i$ is too high for hot devices. It survives in infrared optics and detectors, gamma-ray spectrometers, and as SiGe alloys that strain silicon channels and form fast heterojunction bipolar transistors.

### III–V compounds and alloys

Compounds of group-III (Al, Ga, In) and group-V (N, P, As, Sb) elements crystallize in the zincblende structure (wurtzite for nitrides; Chapter 2) and are mostly direct-gap. Their decisive advantage is that they form continuous solid solutions whose lattice constant and band gap can be tuned by composition. The lattice constant follows **Vegard's law** (linear interpolation), and the band gap follows a quadratic with a **bowing parameter** $b$:

$$
a(x)=xa_{AC}+(1-x)a_{BC},\qquad E_g(x)=xE_{AC}+(1-x)E_{BC}-b\,x(1-x)
$$

Figure 26.4, the band-gap–lattice-constant map, is the design chart for heterostructures: materials connected by a line can be alloyed; materials on the same vertical line can be grown on each other without strain.

> **Status of the principle: Vegard's law and band-gap bowing**
> *Empirical.* Vegard's law holds to within about 0.5 % for most III–V alloys; the band gap needs a fitted bowing parameter, which is large (several eV) for highly mismatched alloys such as GaAsN and InGaN, where the linear picture fails badly.

**Worked example — designing a 1.55 µm detector alloy.** Telecom fibres have their lowest loss near 1.55 µm (Chapter 28), and InP is the substrate of choice. Which In$_x$Ga$_{1-x}$As composition is lattice-matched to InP? With $a_{\mathrm{GaAs}}=5.6533$ Å, $a_{\mathrm{InAs}}=6.0584$ Å and $a_{\mathrm{InP}}=5.8687$ Å, Vegard's law gives

$$
x=\frac{5.8687-5.6533}{6.0584-5.6533}=0.532
$$

the familiar In$_{0.53}$Ga$_{0.47}$As. With $E_{\mathrm{InAs}}=0.354$ eV, $E_{\mathrm{GaAs}}=1.424$ eV and $b=0.477$ eV,

$$
E_g=0.532(0.354)+0.468(1.424)-0.477(0.532)(0.468)=0.736\ \mathrm{eV}
$$

corresponding to an absorption edge at $1.2398/0.736=1.68$ µm. The alloy absorbs strongly across the 1.3 and 1.55 µm telecom bands and remains transparent beyond 1.7 µm: one composition simultaneously solves the lattice-matching problem (no misfit dislocations) and the optical problem. Lasers for the same band use quaternary InGaAsP or InGaAlAs, where the extra degree of freedom lets the gap be tuned while staying lattice-matched.

<!-- FIGURE 26.4 | figures/ch26/fig-26-4-bandgap-vs-lattice-constant.png | map | Band gap against lattice constant for the principal semiconductors: the design chart for alloys and heterostructures. | Content: x-axis lattice constant 3.0 to 6.6 angstrom (for wurtzite nitrides and SiC use the a-parameter, plotted in a separate left cluster 3.0–3.6); y-axis band gap 0 to 6.5 eV, right axis corresponding wavelength in um (0.2 to 10). Points: AlN (3.11, 6.0), GaN (3.19, 3.4), InN (3.54, 0.7), 4H-SiC (3.07, 3.26), diamond (3.57, 5.5), Si (5.431, 1.12), Ge (5.658, 0.66), GaP (5.451, 2.26), AlAs (5.661, 2.16), GaAs (5.653, 1.42), InP (5.869, 1.34), InAs (6.058, 0.35), GaSb (6.096, 0.73), AlSb (6.136, 1.6), InSb (6.479, 0.17), ZnSe (5.668, 2.7), CdTe (6.48, 1.5). Solid lines for direct-gap alloys, dashed for indirect segments; bowed curves for InGaAs, AlGaAs (nearly vertical), InGaN. Vertical dashed line at InP with In0.53Ga0.47As marked at 0.74 eV. Visible band 1.65–3.1 eV shaded in spectrum colours. -->

GaAs and AlGaAs (nearly lattice-matched across the whole range) make red and infrared lasers, the high-efficiency multi-junction solar cells that power satellites, and the RF front-end amplifiers of mobile phones. InP-based alloys own optical communication. Antimonides and InSb cover the mid-infrared for thermal imaging and gas sensing.

### Silicon carbide

SiC is a covalent compound that exists in more than 200 **polytypes** — the same Si–C layers stacked in different sequences (Chapter 2) — of which 4H-SiC is the electronic grade, chosen for its high, nearly isotropic electron mobility. It combines a 3.26 eV gap, a critical field of 2.5–3 MV/cm, a thermal conductivity above that of copper, and a native SiO$_2$ (though with a worse interface than silicon's, which limits MOSFET channel mobility). Its difficulties are crystal growth (Section 26.6) and the extreme hardness that makes wafering slow. It is also a structural ceramic: the same compound is used as abrasive, armour, kiln furniture, and as the matrix and fibre of SiC/SiC composites in jet-engine hot sections (Chapter 33).

### Gallium nitride and the nitrides

GaN and its alloys with InN and AlN cover band gaps from 0.7 eV to 6.0 eV — infrared to deep ultraviolet — in one material system. InGaN quantum wells emit the blue light of every white LED (a blue chip plus a yellow phosphor, Chapter 28) and the violet light of Blu-ray lasers. In electronics, GaN's high critical field and the very high sheet density of electrons that forms spontaneously at an AlGaN/GaN interface (Section 26.5) make high-electron-mobility transistors (HEMTs) for radar, 5G base stations and compact chargers. Remarkably, GaN devices work despite dislocation densities of $10^8$–$10^9$ cm$^{-2}$, because GaN is grown on sapphire, SiC or silicon with large lattice mismatch; in GaAs such densities would kill a laser in minutes. Indium-rich clusters that localize carriers away from dislocations are part of the explanation.

### Oxide semiconductors

Most oxides are insulators, but several are wide-gap semiconductors with useful niches. ZnO, n-type through native defects and hydrogen, is the basis of the varistors that protect power lines and electronics from surges (its grain boundaries form back-to-back barriers, a microstructural device). In$_2$O$_3$:Sn (ITO), SnO$_2$:F and Al-doped ZnO are degenerately doped **transparent conducting oxides**, combining a gap above 3 eV with conductivity near $10^4$ S/cm, essential for displays, touch screens and solar cells. **Amorphous oxide semiconductors** such as InGaZnO$_4$ (IGZO) keep mobilities of 10–20 cm²/(V s) without crystallinity, because conduction runs through overlapping, spherically symmetric metal s orbitals that are insensitive to bond-angle disorder — unlike the directional sp$^3$ bonds of amorphous silicon, whose mobility collapses to about 1. IGZO thin-film transistors drive large OLED and LCD panels. β-Ga$_2$O$_3$, with a 4.8 eV gap and melt-grown substrates, is the leading candidate for the next generation of power devices, though it cannot be doped p-type and conducts heat poorly.

### Organic semiconductors

Conjugated molecules and polymers (pentacene, rubrene, P3HT, polyfluorenes, fullerene derivatives) are semiconductors because their delocalized π electrons form a highest occupied and a lowest unoccupied molecular orbital (HOMO and LUMO) separated by 1.5–3 eV. In the solid, molecules are held by weak van der Waals forces, so carriers hop between molecules and mobilities are low ($10^{-3}$–10 cm²/(V s)) and strongly dependent on molecular packing, crystallinity and film processing — a polymer-morphology problem of the kind in Chapter 20. Light absorption creates tightly bound excitons rather than free carriers because the permittivity is low (about 3). Organic semiconductors cannot compete with silicon on speed, but they can be printed, deposited at low temperature on plastic, and tuned by chemistry. OLED displays in phones and televisions are the large commercial success; organic photovoltaics, sensors and flexible circuits are smaller. Halide perovskites, a newer solution-processed family with remarkable defect tolerance, are treated as photovoltaic absorbers in Chapter 32, and two-dimensional semiconductors such as MoS$_2$ in Chapter 30.

**Worked example — why SiC and GaN power devices are small.** A unipolar power device blocks voltage across a lightly doped **drift layer**. For a 1200 V device with a triangular field profile peaking at the critical field $E_c$, the minimum layer thickness is $W=2V/E_c$ and the maximum doping $N=\varepsilon_r\varepsilon_0E_c^2/(2qV)$. For silicon ($E_c=0.3$ MV/cm, $\varepsilon_r=11.7$):

$$
W=\frac{2(1200)}{3\times10^7\ \mathrm{V/m}}=80\ \mu\mathrm m,\qquad N=\frac{11.7(8.854\times10^{-12})(3\times10^7)^2}{2(1.602\times10^{-19})(1200)}=2.4\times10^{20}\ \mathrm{m^{-3}}=2.4\times10^{14}\ \mathrm{cm^{-3}}
$$

For 4H-SiC ($E_c=2.5$ MV/cm, $\varepsilon_r=9.7$): $W=9.6$ µm and $N=1.4\times10^{16}$ cm$^{-3}$. The drift-layer resistance per unit area, $R_{\mathrm{on}}=W/(q\mu N)$, is therefore

$$
R_{\mathrm{on,Si}}=\frac{80\times10^{-4}\ \mathrm{cm}}{(1.602\times10^{-19})(1350)(2.4\times10^{14})}=153\ \mathrm{m\Omega\,cm^2},\qquad R_{\mathrm{on,SiC}}=0.45\ \mathrm{m\Omega\,cm^2}
$$

(with $\mu=950$ cm²/(V s) for SiC) — a factor of about 340. Because $R_{\mathrm{on}}\propto V^2/(\varepsilon_r\mu E_c^3)$, the critical field enters as its cube, and that single materials property drives the whole trend. In practice silicon uses bipolar IGBTs to flood the drift layer with carriers and reduce this penalty, at the cost of slower switching. The SiC device conducts the same current through a chip a few hundredths the area, with less capacitance and faster switching — the opening example's inverter gains, derived from a breakdown field. The quantity $\varepsilon_r\mu E_c^3$ is Baliga's figure of merit, a performance index in exactly the sense of Chapter 48.

---

## 26.5 Junctions, heterostructures and interfaces as material problems

### The p–n junction

When p-type and n-type regions of the same crystal meet, electrons diffuse into the p side and holes into the n side, leaving behind a **depletion region** of ionized dopants whose field opposes further diffusion. Equilibrium is reached when the Fermi level is constant across the junction; the bands then bend by the **built-in potential**

$$
V_{bi}=\frac{k_BT}{q}\ln\frac{N_aN_d}{n_i^2}
$$

For silicon with $N_a=10^{17}$ and $N_d=10^{16}$ cm$^{-3}$, $V_{bi}=0.0259\ln(10^{33}/10^{20})=0.77$ V, and the depletion width $W=\sqrt{2\varepsilon V_{bi}(1/N_a+1/N_d)/q}$ is 0.33 µm. Under forward bias the barrier drops and current rises exponentially; under reverse bias only a small leakage flows, set by $n_i^2$ and by generation at defects — which is why leakage, like the high-temperature limit of Section 26.2, is ultimately a band-gap and crystal-quality property. Every solar cell, LED, photodiode and bipolar transistor is a junction.

### Metal–semiconductor contacts

A metal on a semiconductor forms either a rectifying **Schottky barrier** or an ohmic contact. The simple Schottky–Mott rule predicts a barrier equal to the metal work function minus the semiconductor's electron affinity, but in practice interface states **pin** the Fermi level, so barriers on silicon and GaAs depend only weakly on the metal. Ohmic contacts are therefore made not by choosing a metal of the right work function but by doping the semiconductor so heavily ($>10^{19}$ cm$^{-3}$) that the barrier becomes thin enough for electrons to tunnel, and by reacting metal with semiconductor to form silicides (TiSi$_2$, NiSi) or alloyed contacts (Ti/Al on GaN, Ni on SiC annealed at about 1000 °C). Contact formation is interfacial metallurgy: reaction kinetics, phase formation and thermal stability decide whether a contact survives.

### Heterostructures and band alignment

A **heterojunction** joins two different semiconductors. Their gaps differ, so at the interface the band edges must step, and the steps $\Delta E_c$ and $\Delta E_v$ share the gap difference according to the **band alignment** (Figure 26.5). In a **type I** (straddling) alignment, such as GaAs in AlGaAs, the narrow-gap material is a well for both electrons and holes; this confines carriers in quantum-well lasers and LEDs. In a **type II** (staggered) alignment, electrons and holes collect on opposite sides, used in some infrared detectors. **Type III** (broken gap), as in InAs/GaSb, lets electrons tunnel from one valence band into the other's conduction band. Alignments are estimated from electron affinities (Anderson's rule, often wrong by 0.1–0.3 eV because of interface dipoles) and measured by photoemission.

Heterostructures created modern optoelectronics: confining carriers and light in a thin, narrow-gap layer between wider-gap, lower-index cladding is what made continuous room-temperature semiconductor lasers possible. They also enable **modulation doping**: donors placed in the wide-gap layer release electrons that fall into the adjacent narrow-gap layer, where they move without impurity scattering in a **two-dimensional electron gas** (2DEG).

In AlGaN/GaN, no doping is needed. Wurtzite nitrides are polar (pyroelectric, Chapter 25), and AlGaN grown on GaN is also strained and therefore piezoelectrically polarized. The discontinuity in total polarization at the interface leaves a fixed sheet charge of about $10^{13}$ cm$^{-2}$, which attracts an equal sheet density of electrons — a 2DEG with mobility near 2000 cm²/(V s). The GaN HEMT is a device whose channel is created by crystal symmetry.

<!-- FIGURE 26.5 | figures/ch26/fig-26-5-junction-band-diagrams.png | band-diagram | Band diagrams of a silicon p–n junction in equilibrium and of an AlGaN/GaN heterojunction with its polarization-induced two-dimensional electron gas. | Content: left panel: Si p–n junction, Na = 1e17, Nd = 1e16 cm^-3, x from -0.5 to +0.5 um; Ec and Ev bending by qVbi = 0.77 eV across a depletion region 0.33 um wide (mostly on the n side), flat EF dashed line across; label Eg = 1.12 eV, depletion region, + and - fixed charges. Right panel: Al0.25Ga0.75N (25 nm, Eg 3.96 eV) on GaN (Eg 3.4 eV); conduction-band offset about 0.4 eV, triangular well at the interface dipping below EF, shaded 2DEG labelled ns about 1e13 cm^-2; arrows showing spontaneous and piezoelectric polarization in each layer; surface at left with gate metal. -->

### Lattice mismatch, strain and critical thickness

A heterostructure is only as good as its interface, and the first materials problem is the **lattice mismatch** $f=(a_{\mathrm{film}}-a_{\mathrm{sub}})/a_{\mathrm{sub}}$. A thin mismatched layer can grow coherently, elastically strained to the substrate's in-plane lattice parameter. Its strain energy grows with thickness, and beyond a **critical thickness** $h_c$ it becomes favourable to introduce misfit dislocations at the interface (the Matthews–Blakeslee criterion, from the dislocation theory of Chapter 12). For Si$_{0.8}$Ge$_{0.2}$ on Si ($f=0.84\,\%$) $h_c$ is of order 10–20 nm at equilibrium, larger in metastable low-temperature growth. Threading segments of these dislocations pass through active layers and act as recombination centres and leakage paths. Strain is not only a problem: biaxial tension in silicon channels raises electron mobility and was introduced deliberately into every high-performance logic chip from the 90 nm node, and compressive strain in InGaAs quantum wells improves lasers.

When no lattice-matched substrate exists, as for GaN, growth on sapphire (16 % mismatch after the 30° in-plane rotation of the epitaxial relationship), SiC (3.5 %) or Si(111) (about 17 %, with a large thermal-expansion mismatch that cracks thick layers on cooling) relies on nucleation layers, buffer superlattices and dislocation filtering. These are materials-science solutions to device problems.

### The Si/SiO$_2$ interface and high-$\kappa$ dielectrics

The MOS transistor depends on the quality of a semiconductor–insulator interface. Thermally grown SiO$_2$ on silicon, annealed in hydrogen, has an interface-trap density of about $10^{10}$ cm$^{-2}$ eV$^{-1}$ — one electrically active defect per $10^5$ surface atoms — because the amorphous oxide can accommodate the bond geometry of the crystal and hydrogen saturates the few remaining dangling bonds. When gate oxides thinned below about 1.5 nm, tunnelling leakage forced a change to **high-$\kappa$** dielectrics (HfO$_2$, $\varepsilon_r\approx20$–25), which give the same capacitance with a physically thicker layer; a sub-nanometre SiO$_2$ interlayer is kept to preserve the interface. SiC and GaN have worse oxide interfaces ($10^{11}$–$10^{12}$ cm$^{-2}$ eV$^{-1}$), which lowers channel mobility and causes threshold-voltage drift, an active area of interface materials science.

---

## 26.6 Crystal growth and doping as materials processing

### Purity and perfection

Semiconductor devices need crystals of a perfection demanded nowhere else in engineering: electrically active impurities below $10^{12}$–$10^{13}$ cm$^{-3}$ (sub-ppb), and, for silicon, no dislocations at all. Purification starts with chemistry: metallurgical-grade silicon (98–99 %) from carbothermic reduction of quartz is converted to trichlorosilane, distilled, and decomposed onto hot silicon rods (the Siemens process) to give polysilicon of 9–11 nines. The solidification science of Chapter 9 then turns it into single crystals.

### Czochralski growth and segregation

In the **Czochralski** (Cz) process, a seed crystal is dipped into molten silicon (1414 °C) in a silica crucible and slowly pulled and rotated, growing an ingot up to 300 mm in diameter and 2 m long. Two materials-science ideas make it work. First, dislocations are eliminated by **Dash necking**: the crystal is first pulled to a thin neck of about 3 mm, which dislocations grow out of, after which the crystal stays dislocation-free because there are no sources to regenerate them. Second, dopants and impurities **segregate** between melt and solid. With an equilibrium distribution coefficient $k=C_s/C_l$ and complete mixing in the melt, the dopant concentration in the solid follows the **Scheil equation** of Chapter 9:

$$
C_s=kC_0(1-f_s)^{k-1}
$$

where $f_s$ is the fraction solidified.

> **Status of the principle: Scheil equation**
> *Approximate.* It assumes complete mixing in the liquid, no diffusion in the solid and local equilibrium at the interface. It describes Cz growth well when the melt is stirred by rotation and convection; an effective $k$ (closer to 1 at high growth rate) corrects for incomplete mixing in the boundary layer.

**Worked example — the resistivity profile along a Cz ingot.** Boron in silicon has $k=0.8$; phosphorus has $k=0.35$. For boron, the first solid ($f_s=0$) has $0.8C_0$, the middle of the ingot ($f_s=0.5$) has $0.8(0.5)^{-0.2}C_0=0.92C_0$, and at $f_s=0.9$ the concentration reaches $0.8(0.1)^{-0.2}C_0=1.27C_0$. Since resistivity is roughly inversely proportional to doping, the resistivity varies by a factor of $1.27/0.8=1.6$ along 90 % of the ingot — tolerable for most uses. For phosphorus, the same points give $0.35C_0$, $0.55C_0$ and $1.56C_0$: a factor of 4.5. n-type Cz ingots therefore have a wide resistivity spread, which matters for high-efficiency n-type solar wafers and for power devices. Figure 26.6 shows these profiles. Remedies are continuous Cz (topping up the melt), co-doping, or **neutron transmutation doping** of float-zone silicon, in which reactor neutrons convert $^{30}$Si to $^{31}$P uniformly through the whole crystal — doping by nuclear reaction rather than solidification.

<!-- FIGURE 26.6 | figures/ch26/fig-26-6-czochralski-scheil.png | plot | Czochralski growth and the dopant profile it produces: segregation makes concentration rise along the ingot, much more strongly for phosphorus than for boron. | Content: left panel schematic of a Cz puller: rotating seed and neck (about 3 mm), shoulder, cylindrical ingot, meniscus, silica crucible in graphite susceptor, heaters, argon flow; labels 1414 C melt, pull rate about 1 mm/min. Right panel: x-axis fraction solidified 0 to 1; y-axis Cs/C0 from 0 to 3. Scheil curves for k = 0.8 (B: 0.80, 0.92 at 0.5, 1.27 at 0.9), k = 0.35 (P: 0.35, 0.55, 1.56), k = 0.023 (Sb, rising from 0.023), and k = 8e-6 (Fe, flat near zero until near the end, inset log scale) showing segregation-based purification. Horizontal line at 1. -->

Cz silicon dissolves oxygen from the crucible at about $10^{18}$ cm$^{-3}$. That oxygen is both a nuisance (thermal donors, boron–oxygen light-induced degradation in solar cells) and a resource: controlled precipitation of SiO$_2$ in the wafer interior creates **internal gettering** sites that trap iron and copper away from the device layer, and dissolved oxygen pins dislocations and strengthens wafers against slip during processing. When the lowest oxygen and highest resistivity are needed (power devices, detectors), the crucible-free **float-zone** process passes a molten zone along a polycrystalline rod held by surface tension. Solar silicon is also cast by **directional solidification** into large multicrystalline blocks, cheaper but containing grain boundaries and dislocations that limit lifetime — the subject of the lifetime example in Section 26.3.

Compound semiconductors are harder. GaAs and InP decompose before melting at atmospheric pressure, so they are grown by liquid-encapsulated Czochralski under a B$_2$O$_3$ layer and high pressure, or by vertical gradient freeze, with dislocation densities of $10^2$–$10^4$ cm$^{-2}$. SiC sublimes rather than melts, and is grown by **physical vapour transport** at 2200–2500 °C at a few hundred micrometres per hour, compared with millimetres per minute for Cz silicon; screw-dislocation "micropipes" have been eliminated, but basal-plane dislocations that convert to stacking faults under forward current remain a reliability issue. GaN substrates are grown by hydride vapour-phase epitaxy or ammonothermally and remain expensive, so most GaN is grown on foreign substrates.

### Epitaxy

Device layers are grown on substrates by **epitaxy**, the deposition of a crystalline film that continues the substrate lattice. Chemical vapour deposition grows silicon and SiC epilayers with precisely controlled doping; **metal-organic CVD** (MOCVD), using trimethylgallium, ammonia and arsine, grows almost all III–V and nitride LEDs and lasers on wafers up to 200 mm; **molecular-beam epitaxy** (MBE) in ultra-high vacuum gives atomic-layer control for research and high-frequency devices. Growth modes, strain relaxation and defect formation are treated in Chapter 41.

### Doping by diffusion and ion implantation

Dopants are introduced locally by **diffusion** from a surface source at 900–1100 °C, with profiles given by the error-function and Gaussian solutions of Fick's second law (Chapter 8), or by **ion implantation**, in which dopant ions accelerated to keV–MeV energies penetrate to a depth set by their range. Implantation gives precise dose and depth control but displaces many lattice atoms per ion, amorphizing the surface at high dose; an **activation anneal** must recrystallize the damage and move dopants onto substitutional sites, while diffusion during the anneal smears the profile. Modern silicon processing uses millisecond flash and laser anneals to activate without diffusing. In SiC, dopant diffusion is negligible even at 1700 °C, so all selective doping is by hot implantation followed by anneals at 1600–1800 °C under a carbon cap to stop silicon evaporating; in GaN, activating implanted Mg acceptors is still one of the material's hardest problems. Doping is solid-state kinetics applied with nanometre precision.

> **Boundary.** Band theory and carrier statistics are recapped here; their quantum-mechanical derivation belongs to the Engineering Physics book. Device operation and the full processing sequence (lithography, etching, metallization) are developed in the *Materials Core (EEE)* book, Chapters 10–13 and 20–22, and summarized in Chapter 41.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How do band gaps and recombination produce colour, luminescence, LEDs and lasers? | Chapter 28 |
| How do quantum confinement and two-dimensional materials change band structure? | Chapter 30 |
| How are semiconductors used as photovoltaic and thermoelectric materials, and why do halide perovskites tolerate defects? | Chapter 32 |
| How do radiation and high temperature degrade semiconductor devices? | Chapter 33 |
| How do electromigration, interface traps and dielectric wear-out cause device failures? | Chapter 36 |
| How are films deposited and epitaxial layers grown; how are oxidation, implantation, lithography and etching done? | Chapter 41 |
| How are carrier density, mobility, lifetime and band gap measured (Hall effect, photoluminescence, DLTS)? | Chapters 42 and 43 |
| How are band structures and defect levels calculated from first principles? | Chapter 45 |
| How is a semiconductor chosen for a given power, frequency or optical application? | Chapter 48 |

**Next:** Chapter 27 turns from electrons as charge carriers to electrons as magnetic moments, and asks how exchange, domains and microstructure make the soft and hard magnets of motors, transformers and generators.
