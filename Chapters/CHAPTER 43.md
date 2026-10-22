# Chapter 43 — Large-Facility and Nanoscale Characterization

*Part X · Characterization, Computation and Design*

The steel walls of a nuclear reactor pressure vessel, 200 mm thick, slowly lose toughness under neutron irradiation: their ductile-to-brittle transition temperature can rise by 100 °C or more over decades, and plant life depends on predicting how much. Optical and scanning electron microscopes see nothing different in irradiated specimens, and conventional TEM sees only faint "black dots". The cause turned out to be clusters of copper, nickel, manganese and silicon atoms only 2–4 nm across, at number densities of $10^{23}$–$10^{24}$ m$^{-3}$, which obstruct dislocations (Chapter 33). They were measured by small-angle neutron scattering, which counts and sizes them in a cubic-millimetre volume, and by atom-probe tomography, which places each atom of a cluster in three dimensions. The same story repeats across the discipline. The oxidation state of nickel in a working battery cathode, the residual stress 30 mm inside a railway wheel, the hydrogen in a zirconium fuel cladding, the boron at a single grain boundary in a turbine-disc alloy and the structure of a protein adsorbed on an implant all lie beyond the laboratory toolkit of Chapter 42. They need either a source far brighter or more penetrating than a laboratory tube, or an instrument that resolves single atoms.

> **What do synchrotron X-rays and neutrons offer that laboratory sources cannot?**
> **How do X-ray absorption, small-angle scattering, total scattering and tomography reveal local structure, nanostructure and internal defects?**
> **How do atom probes and aberration-corrected microscopes locate individual atoms and measure local chemistry?**
> **How are beam-sensitive soft and biological materials imaged without destroying them?**

| Concept | Engineering destination |
|---|---|
| Synchrotron brilliance and tunability | Feasibility of fast, small-beam, element-specific experiments |
| XANES and EXAFS | Oxidation states in battery cathodes and catalysts, local structure of dopants and glasses |
| SAXS | Precipitates in aluminium alloys, porosity, polymer lamellae, nanoparticles |
| High-resolution diffraction and PDF analysis | Phase transformations, strain in bulk parts, structure of amorphous and nanocrystalline materials |
| X-ray tomography | Porosity in castings and AM parts, damage in composites, concrete, bone, batteries |
| Neutron scattering | Light elements, magnetic structures, deep residual stress, phonons and diffusion |
| Atom-probe tomography | Solute clusters, segregation, precipitate chemistry in 3D at near-atomic resolution |
| Aberration-corrected STEM, EELS, 4D-STEM | Interface structure, light-element imaging, local bonding, strain and orientation maps |
| Cryo-EM | Polymers, hydrogels, proteins on biomaterials, lithium metal and SEI in batteries |

**Roadmap.** Why go to a facility (43.1) → synchrotron methods: absorption spectroscopy, small-angle scattering, diffraction and PDF, tomography (43.2–43.5) → neutrons (43.6) → atom-probe tomography (43.7) → aberration-corrected STEM (43.8) → cryo-EM (43.9) → choosing a method (43.10).

---

## 43.1 Why go to a facility

### Synchrotron light

A laboratory X-ray tube produces photons by electrons hitting an anode: a few characteristic wavelengths, emitted in all directions, with most of the power turned into heat. A **synchrotron** stores electrons of a few GeV in a ring hundreds of metres to over a kilometre in circumference; wherever magnets bend their path, they radiate. Because the electrons are ultra-relativistic, the radiation is compressed into a narrow forward cone of half-angle about $1/\gamma$, where $\gamma=E/m_ec^2$. For a 6 GeV ring, $\gamma=6000/0.511=11\,700$, so the cone is about 85 µrad wide.

**Bending magnets** give a broad, continuous spectrum characterized by the critical energy $E_c(\mathrm{keV})=0.665\,E^2(\mathrm{GeV})\,B(\mathrm{T})$: 19 keV for 6 GeV electrons in a 0.8 T field. **Undulators**, periodic arrays of magnets with period $\lambda_u$, make the electrons wiggle so that radiation from successive periods interferes, concentrating flux into narrow harmonics:

$$
\lambda_1=\frac{\lambda_u}{2\gamma^2}\left(1+\frac{K^2}{2}\right)
$$

with $K$ the deflection parameter (proportional to field and period).

> **Status of the principle: Undulator equation**
> *Derived.* Follows from the relativistic Doppler compression of the electron's oscillation as seen on-axis, plus constructive interference between periods; it gives the on-axis fundamental and ignores the finite emittance and energy spread of the electron beam, which broaden the harmonics.

**Worked example — tuning an undulator.** For $\lambda_u=20$ mm, $K=1.5$ and a 6 GeV ring, $\lambda_1=0.020/(2\times11\,742^2)\times(1+1.125)=1.54\times10^{-10}$ m, i.e. 0.154 nm or 8.0 keV, the energy of Cu K$\alpha$. Opening the magnet gap reduces $K$ and moves the harmonic to higher energy, so the same device scans across an absorption edge. This continuous tunability, impossible with a tube, underlies every spectroscopy in Section 43.2.

The figure of merit for most experiments is **brilliance**: photons per second per unit source area per unit solid angle per 0.1 % bandwidth. A rotating-anode tube gives roughly $10^{9}$–$10^{10}$ in these units; third-generation undulators about $10^{20}$; fourth-generation rings built since 2016 with multi-bend achromat lattices (MAX IV, ESRF-EBS, APS-U and others) reach about $10^{22}$, because their electron beams are smaller and less divergent (Figure 43.1). X-ray free-electron lasers add femtosecond pulses for following processes such as laser melting or shock compression on their own timescale. Brilliance buys three things: **small beams** (100 nm to 1 µm spots that still carry enormous flux), **speed** (a diffraction pattern in a millisecond, a tomogram in a second, hence in-situ and operando studies, Chapter 44), and **high energies** (50–150 keV photons that pass through centimetres of steel).

<!-- FIGURE 43.1 | figures/ch43/fig-43-1-source-brilliance.png | plot | Spectral brilliance of X-ray sources versus photon energy. | Content: log-log plot; x-axis photon energy 0.1 to 200 keV; y-axis brilliance in photons/s/mm^2/mrad^2/0.1% bandwidth from 1e6 to 1e24. Curves/bands: laboratory sealed tube and rotating anode (continuous bremsstrahlung ~1e7-1e8 with characteristic-line spikes to ~1e9-1e10 at Cu Kα 8.05 keV and Mo Kα 17.5 keV); bending magnet of 3rd-generation ring (broad hump ~1e15-1e16, critical energy marked ~19 keV); wiggler (~1e17-1e18 extending to 100 keV); 3rd-generation undulator (comb of harmonics, envelope ~1e19-1e21 from 1 to 30 keV); 4th-generation (MBA) undulator (~1e21-1e22.5). Annotations of energy uses: 'soft X-ray: XPS, C/N/O edges' below 2 keV, '3d-metal K edges 5-9 keV', 'high-energy diffraction in steel 60-150 keV'. -->

### Neutron sources

Neutrons are produced either by fission in a **research reactor** (a continuous beam, moderated to thermal energies of about 25 meV) or by **spallation**, in which pulses of GeV protons strike a heavy-metal target (ISIS, SNS, J-PARC, ESS). Spallation sources are pulsed, so neutron energy is measured by time of flight over a known path, and a whole spectrum is used at once. Even the brightest neutron sources deliver orders of magnitude fewer particles per second onto a sample than a synchrotron, so neutron experiments use larger samples (cubic millimetres to centimetres) and longer counting times. Their advantages lie elsewhere (Section 43.6).

Access to both kinds of facility is by competitive proposal, reviewed for scientific merit, with beamtime typically free for open publication and charged for proprietary industrial work. Industrial users from aerospace, automotive, energy and pharmaceutical companies use dedicated industrial liaison teams; residual-stress mapping of welds and tomography of castings are among the most common industrial measurements.

---

## 43.2 X-ray absorption spectroscopy

As photon energy rises through the binding energy of a core level, the absorption coefficient $\mu(E)$ of that element jumps: the **absorption edge** (K edges at 6.54 keV for Mn, 7.71 keV for Co, 8.33 keV for Ni, 11.56 keV for the Pt L$_3$ edge). Tuning a monochromatic synchrotron beam across an edge and measuring transmission ($\mu x=\ln I_0/I$) or the fluorescence that follows absorption gives an **X-ray absorption spectrum** of one element at a time, even at concentrations of 0.01–1 % in a complex matrix, in crystals, glasses, liquids and working devices. The spectrum has two regions (Figure 43.2).

### XANES

The **X-ray absorption near-edge structure** (XANES), within about 50 eV of the edge, reflects transitions into empty states and is a fingerprint of **oxidation state and coordination**. The edge shifts to higher energy as the absorbing atom becomes more oxidized, typically by about 1–3 eV per unit change in oxidation state for 3d metals, because the core electron is more tightly bound. Comparing with reference compounds measured on the same beamline gives the average oxidation state. Engineering uses: following Ni$^{2+}$ → Ni$^{4+}$ oxidation in a layered NMC cathode during charge, and identifying which transition metal compensates the charge; Ce$^{3+}$/Ce$^{4+}$ in automotive three-way catalysts; the speciation of chromium (harmless Cr$^{3+}$ versus toxic Cr$^{6+}$) in corrosion products, slags and contaminated soils; uranium oxidation state in nuclear-waste glass.

### EXAFS

At higher energies, the outgoing photoelectron wave scatters off neighbouring atoms and interferes with itself, modulating the absorption. This **extended X-ray absorption fine structure** (EXAFS), $\chi(k)$, is analysed as a function of photoelectron wavenumber

$$
k=\frac{\sqrt{2m_e(E-E_0)}}{\hbar}=0.5123\sqrt{E-E_0\ [\mathrm{eV}]}\ \ \mathrm{\AA^{-1}}
$$

and is described by the EXAFS equation

$$
\chi(k)=\sum_j\frac{N_jS_0^2\,f_j(k)}{kR_j^2}\,e^{-2k^2\sigma_j^2}\,e^{-2R_j/\lambda(k)}\sin\!\left[2kR_j+\delta_j(k)\right]
$$

where shell $j$ contains $N_j$ atoms at distance $R_j$ with mean-square disorder $\sigma_j^2$, $f_j$ and $\delta_j$ are scattering amplitude and phase (calculated by codes such as FEFF), $\lambda$ is the photoelectron mean free path and $S_0^2$ an amplitude reduction factor. Fourier transforming $\chi(k)$ gives a pseudo-radial distribution around the absorbing element; fitting gives bond lengths to about 0.01–0.02 Å and coordination numbers to 10–20 %.

> **Status of the principle: EXAFS equation**
> *Approximate.* Single-scattering, plane-wave-corrected theory with harmonic disorder; multiple scattering, anharmonic vibrations at high temperature and the strong correlation between $N$, $S_0^2$ and $\sigma^2$ limit accuracy, and the region close to the edge (XANES) cannot be fitted this way.

**Worked example — what range of $k$ resolves two shells?** Data collected to $E-E_0=600$ eV reach $k_{max}=0.5123\sqrt{600}=12.5$ Å$^{-1}$; the low-$k$ region below about 3 Å$^{-1}$ is excluded. The usable range $\Delta k=9.5$ Å$^{-1}$ resolves neighbour shells separated by more than $\Delta R\approx\pi/(2\Delta k)=0.17$ Å. Two oxygen shells at 1.90 and 2.10 Å around a Jahn–Teller-distorted Mn$^{3+}$ ion in a cathode can thus just be separated; at 50 eV above the edge ($k=3.6$ Å$^{-1}$) the spectrum is still XANES and carries no such information. Dilute or heavily absorbing samples measured in fluorescence reach lower $k_{max}$ in practical counting times, which is why EXAFS on trace elements gives fewer, less certain shells.

EXAFS needs no long-range order, so it gives the local structure of glasses, amorphous alloys, solutes in solid solution (does a dopant sit on a substitutional site?), nanoparticle catalysts and ions in solution.

<!-- FIGURE 43.2 | figures/ch43/fig-43-2-xanes-exafs.png | plot | X-ray absorption spectrum at the Ni K edge showing the XANES and EXAFS regions, with the k-weighted EXAFS and its Fourier transform. | Content: main panel: normalized absorption μ(E) vs photon energy 8250 to 8950 eV; edge at E0 = 8333 eV; two XANES curves offset by ~2.5 eV labelled 'Ni2+ (discharged)' and 'Ni4+ (charged)', with edge shift arrow; shaded 'XANES' window (E0-20 to E0+50 eV) and 'EXAFS' region beyond with oscillations decaying; top axis k = 0.5123 sqrt(E-E0) marked at 3, 6, 9, 12.5 Å^-1 (12.5 at E0+600 eV). Inset 1: k^2 χ(k) from 3 to 12.5 Å^-1. Inset 2: magnitude of Fourier transform vs R (uncorrected for phase shift) 0 to 6 Å with peaks labelled 'Ni-O' (~1.5 Å apparent) and 'Ni-M' (~2.5 Å apparent). -->

---

## 43.3 Small-angle X-ray scattering

Bragg's law relates large scattering angles to atomic spacings; structures of 1–100 nm scatter at angles below a few degrees. Small-angle scattering is described by the scattering vector magnitude

$$
q=\frac{4\pi\sin\theta}{\lambda}
$$

(with $2\theta$ the scattering angle), and a feature of size $D$ scatters near $q\approx2\pi/D$. With $\lambda=0.10$ nm (12.4 keV), $2\theta=0.5^\circ$ corresponds to $q=0.55$ nm$^{-1}$. **SAXS** measures the intensity $I(q)$ from **contrast in electron density** $\Delta\rho$ between particles and matrix, averaged over a beam-sized volume containing millions of features: statistically robust, unlike counting particles in TEM.

At small $q$, a dilute system of particles of radius of gyration $R_g$ follows the **Guinier law**

$$
I(q)=I(0)\exp\!\left(-\frac{q^2R_g^2}{3}\right)
$$

so a plot of $\ln I$ against $q^2$ has slope $-R_g^2/3$. At large $q$, sharp interfaces give the **Porod law** $I\propto q^{-4}$, with a prefactor proportional to the interface area per unit volume. The integrated intensity (the invariant) gives the volume fraction if the contrast is known (Figure 43.3).

> **Status of the principle: Guinier and Porod laws**
> *Approximate.* Guinier holds for dilute, non-interacting particles at $qR_g\lesssim1.3$; Porod for sharp, smooth interfaces at $qR_g\gg1$. Size distributions, concentrated systems (interparticle interference) and diffuse interfaces need full model fitting.

**Worked example — precipitate size in an aged aluminium alloy.** A 7xxx alloy aged at 120 °C gives a Guinier plot with slope $-3.0$ nm$^2$, so $R_g^2=9.0$ nm$^2$ and $R_g=3.0$ nm. For spheres, $R_g=\sqrt{3/5}\,R$, so $R=3.0/0.775=3.9$ nm: η′-type precipitates about 8 nm across, the size range that gives peak strength (Chapter 16). The Guinier fit is valid only for $q<1.3/R_g=0.43$ nm$^{-1}$, which sets the angular range that must be measured. Repeating the measurement every few seconds during a heat treatment at a synchrotron follows nucleation, growth and coarsening directly.

<!-- FIGURE 43.3 | figures/ch43/fig-43-3-saxs-guinier-porod.png | plot | SAXS intensity from precipitates in an aged Al–Zn–Mg alloy, with Guinier and Porod regimes. | Content: main panel log-log I(q) (arbitrary units, 1e-2 to 1e4) vs q from 0.05 to 5 nm^-1 for spheres of R = 3.9 nm (Rg = 3.0 nm) with ~15 % size dispersion; flat Guinier plateau below ~0.2 nm^-1, knee near 0.4 nm^-1, q^-4 Porod slope above ~1 nm^-1 (dashed guide 'slope -4'). Vertical dashed line at q = 1.3/Rg = 0.43 nm^-1 labelled 'Guinier limit'. Inset: ln I vs q^2 from 0 to 0.2 nm^-2, straight line with slope -3.0 nm^2 labelled 'Rg = 3.0 nm'. Top axis: real-space size 2π/q in nm. -->

Beyond metals, SAXS measures the lamellar long period of semicrystalline polymers (10–30 nm), microphase separation in block copolymers, pore sizes in catalysts, aerogels and cement gels, nanoparticle size distributions, and the hierarchical collagen–mineral structure of bone. **Grazing-incidence SAXS** probes nanostructure in thin films, for example the self-assembly of block-copolymer templates for lithography or the crystallization of perovskite solar absorbers. **Anomalous SAXS**, tuned near an absorption edge, makes one element's contribution visible.

---

## 43.4 High-resolution diffraction and pair-distribution-function analysis

### Synchrotron powder diffraction

A collimated synchrotron beam with an analyser crystal gives peak widths limited by the sample itself, a resolution $\Delta d/d$ of about $10^{-4}$, an order of magnitude better than a laboratory diffractometer. Subtle symmetry lowering (the monoclinic distortion of a ferroelectric, superstructure peaks of ordered phases), small phase fractions down to about 0.1 wt% and precise lattice parameters become measurable.

High photon energies also bring **penetration**. In iron, the mass attenuation coefficient is about 302 cm$^2$/g at 8 keV but only 0.37 cm$^2$/g at 100 keV. With $\rho=7.87$ g/cm$^3$, the 1/e depth rises from 4.2 µm to 3.4 mm, and a 10 mm steel plate transmits $\exp(-2.93)=5$ % of the beam. At such energies Bragg angles are small (a few degrees), so a two-dimensional detector records whole Debye–Scherrer rings in transmission. Ring distortion maps strain in every direction within the plate, and moving the specimen maps **residual stress through the thickness** of welds, shot-peened parts and additively manufactured components with gauge volumes far smaller than neutrons achieve (but with a limited thickness range and elongated gauge volumes along the beam).

### Total scattering and the pair distribution function

Bragg peaks contain the average periodic structure; diffuse scattering between them contains the deviations from it. **Total scattering** measures both and Fourier-transforms the normalized structure function $S(Q)$ into the **pair distribution function**

$$
G(r)=\frac{2}{\pi}\int_0^{Q_{max}}Q\,[S(Q)-1]\sin(Qr)\,dQ=4\pi r\,[\rho(r)-\rho_0]
$$

which gives the probability of finding atom pairs at separation $r$, weighted by scattering power, with $\rho_0$ the average number density. Its peaks are interatomic distances; their areas give coordination numbers. This is the radial distribution function of Chapter 2, measured. It works equally on crystals, nanocrystals, glasses and liquids.

> **Status of the principle: Pair distribution function from total scattering**
> *Derived.* An exact Fourier relation between the structure factor and the pair correlation for an isotropic sample; in practice its accuracy is limited by truncation at $Q_{max}$, by corrections for Compton and multiple scattering, and by the need to model what the one-dimensional, orientationally averaged function cannot uniquely determine.

**Worked example — why PDF needs short wavelengths.** Real-space resolution is set by $Q_{max}$; features closer than roughly $2\pi/Q_{max}$ blur, and termination ripples appear. Cu K$\alpha$ can at best reach $Q_{max}=4\pi/1.5406=8.2$ Å$^{-1}$ (at 2θ = 180°), too low to resolve the 1.6 Å Si–O bond in silica from neighbouring correlations. Mo K$\alpha$ reaches 17.7 Å$^{-1}$ and Ag K$\alpha$ 22.5 Å$^{-1}$. A 60 keV synchrotron beam ($\lambda=0.2066$ Å) reaches $4\pi\sin20^\circ/0.2066=20.8$ Å$^{-1}$ at a modest $2\theta=40^\circ$ on a flat-panel detector, and 30.4 Å$^{-1}$ at $2\theta=60^\circ$, in a second of exposure. That speed allows PDFs to be followed during the crystallization of a metallic glass, the formation of nanoparticles in solution, or the lithiation of an electrode whose products are too disordered for Bragg analysis.

---

## 43.5 X-ray tomography

**Computed tomography (CT)** records radiographs at many angles and reconstructs the three-dimensional distribution of the attenuation coefficient. The contrast comes from Beer–Lambert attenuation, $I=I_0\exp(-\int\mu\,dx)$, so pores (zero attenuation), heavy inclusions, cracks and phases of different density or composition appear in grey levels. Synchrotron beams add **phase contrast**: their spatial coherence lets edges between materials of similar attenuation (carbon fibres in epoxy, soft tissue, polymer blends) appear through refraction fringes, and phase retrieval converts them into quantitative maps.

> **Status of the principle: Absorption-contrast tomography**
> *Approximate.* Reconstruction assumes straight rays and monochromatic Beer–Lambert attenuation; laboratory polychromatic beams harden (low energies are absorbed first), producing cupping artefacts and streaks near dense features, which must be corrected or avoided by filtering.

**Worked example — field of view against resolution.** A detector 2048 pixels wide with an effective pixel size of 0.65 µm images a field of view of $2048\times0.65=1.33$ mm. A good reconstruction needs about $\pi/2\times2048\approx3200$ projections, and the 16-bit volume occupies $2048^3\times2=17$ GB. Seeing pores of 2 µm in a 10 mm additively manufactured part is impossible in one scan: either a 1.3 mm sub-volume is cut out or scanned locally (interior tomography), or the voxel size is relaxed to about 5 µm to cover the whole part. This trade-off decides every tomography experiment.

Engineering uses span the discipline: porosity, lack-of-fusion defects and unmelted powder in AM parts (Chapter 40) and castings (Chapter 38); fibre orientation, voids and damage accumulation in composites under load (Chapter 23); crack networks, aggregate distribution and steel-fibre orientation in concrete; trabecular bone and its integration with porous implants; particle cracking and lithium plating in batteries; corrosion pits in aluminium aircraft alloys. Fourth-generation sources acquire tomograms in under a second, fast enough to follow solidification, foaming or crack growth in four dimensions. **Diffraction-contrast tomography** reconstructs grain shapes and orientations in 3D in polycrystals, a non-destructive counterpart to serial-sectioning EBSD. Laboratory micro-CT and nano-CT (to about 50 nm voxels with X-ray optics) now perform many of these measurements in-house, with longer scan times.

---

## 43.6 Neutron scattering

### What makes neutrons different

Neutrons are uncharged and interact with nuclei through the short-range nuclear force, and with unpaired electrons through their magnetic moment. Four consequences follow.

**Contrast does not follow atomic number.** X-rays scatter from electrons, with amplitude proportional to $Z$ (about $2.82Z$ fm at small angles), so hydrogen and lithium are nearly invisible next to iron or lead. The nuclear **coherent scattering length** $b$ varies irregularly from element to element and even between isotopes:

| Nucleus | H | D | Li (nat.) | C | O | Al | Ti | V | Fe | Ni | Zr |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $b$ (fm) | −3.74 | 6.67 | −1.90 | 6.65 | 5.80 | 3.45 | −3.44 | −0.38 | 9.45 | 10.3 | 7.16 |
| X-ray $f(0)=2.82Z$ (fm) | 2.8 | 2.8 | 8.5 | 16.9 | 22.5 | 36.6 | 62.0 | 64.8 | 73.3 | 78.9 | 112.7 |

> **Status of the principle: Neutron scattering lengths**
> *Empirical.* Scattering lengths depend on nuclear structure and resonances and are not predictable from simple theory; they are measured and tabulated for every element and isotope.

Light elements are therefore seen clearly: oxygen in oxide superconductors and fuel-cell electrolytes, lithium in battery materials, hydrogen in hydrides and metals, carbon and nitrogen in steels. Neighbouring elements (Fe and Mn, Ni and Co) that X-rays barely distinguish have very different $b$. The opposite signs of $b$ for H and D are the basis of **contrast variation**: deuterating one block of a copolymer or one component of a blend makes it visible in small-angle neutron scattering (SANS), and adjusting the H/D ratio of a solvent can make one component invisible ("contrast matching"). Vanadium, with $b\approx0$, is used for sample cans that do not diffract. Hydrogen's large *incoherent* cross-section (about 80 barn) gives a high background in diffraction but makes it the ideal target for vibrational and diffusion spectroscopy (below) and for neutron imaging.

**Penetration.** Most engineering metals absorb neutrons weakly; the 1/e attenuation length of thermal neutrons is roughly 8 mm in iron and nearly 10 cm in aluminium (with exceptions such as boron, cadmium and gadolinium, which are strong absorbers). Neutrons therefore probe the interior of real components (Figure 43.4).

<!-- FIGURE 43.4 | figures/ch43/fig-43-4-xray-neutron-contrast.png | plot | Scattering power of elements for X-rays and neutrons, showing why neutrons see light elements and distinguish neighbours. | Content: x-axis atomic number Z from 1 to 82 with element symbols at selected points (H, Li, C, O, Al, Ti, V, Fe, Ni, Cu, Zr, Pb). Left y-axis scattering amplitude in fm from -5 to 120. X-ray f(0) = 2.82 Z fm drawn as a rising straight line (H 2.8, Fe 73.3, Pb 231 shown off-scale arrow). Neutron coherent scattering lengths as points with stems: H -3.74, D 6.67 (plotted at Z=1 with a separate marker), Li -1.90, C 6.65, O 5.80, Al 3.45, Ti -3.44, V -0.38, Fe 9.45, Ni 10.3, Cu 7.72, Zr 7.16, Pb 9.41; zero line emphasised; negative values shaded. Callout boxes: 'H and D: opposite sign → contrast variation', 'V ≈ 0: sample cans'. -->

**Magnetism.** The neutron's magnetic moment scatters from ordered electron spins, so **magnetic structures** appear directly in diffraction. The historic example is MnO: below its Néel temperature of 118 K, extra peaks appear that index on a cell of twice the chemical lattice parameter (0.889 nm instead of 0.4445 nm), proving antiparallel ordering of Mn moments, the first direct observation of antiferromagnetism. Today neutron diffraction determines spin arrangements in permanent-magnet compounds, multiferroics and magnetocaloric alloys (Chapter 27), and polarized SANS measures magnetic nanostructure in electrical steels and nanocrystalline soft magnets.

**Energies matched to atomic motions.** A thermal neutron of wavelength 1.8 Å has energy $E=81.81/\lambda^2$ meV $=25$ meV and speed 2200 m/s. Its wavelength matches interatomic spacings and its energy matches phonons, so a single scattering event can exchange a measurable fraction of the neutron's energy with the sample. X-ray photons of 1.8 Å carry 6.9 keV, and a 25 meV change is a part in $3\times10^5$.

### Residual stress deep inside components

Neutron diffraction measures lattice strain in a **gauge volume** defined by slits on the incident and diffracted beams (typically 1–4 mm on a side), at depths of several centimetres in steel and over 10 cm in aluminium. Strain follows from the shift of a peak, $\varepsilon=(d-d_0)/d_0=-\cot\theta\,\Delta\theta$; with $2\theta=90^\circ$ a cubic gauge volume is obtained, and a strain of $10^{-4}$ shifts the peak by only 0.006°. Measuring three orthogonal directions gives the triaxial stress through Hooke's law (Chapter 11):

$$
\sigma_{x}=\frac{E}{(1+\nu)(1-2\nu)}\left[(1-\nu)\varepsilon_x+\nu(\varepsilon_y+\varepsilon_z)\right]
$$

and cyclically for $y$ and $z$.

> **Status of the principle: Stress from diffraction strains**
> *Derived.* Isotropic linear elasticity applied to measured lattice strains; requires the principal directions to be known (or six strains measured), plane-specific diffraction elastic constants for textured or anisotropic materials, and a reliable stress-free reference $d_0$ measured on a small cube or comb cut from the same material, because composition changes across a weld shift $d_0$ itself.

**Worked example — residual stress in a butt weld.** At the mid-thickness of a 25 mm ferritic-steel butt weld, Fe(211) strains measured with $\lambda=0.165$ nm ($2\theta\approx90^\circ$) relative to a stress-free comb are $\varepsilon_x=1.2\times10^{-3}$ (longitudinal), $\varepsilon_y=0.5\times10^{-3}$ (transverse) and $\varepsilon_z=-0.2\times10^{-3}$ (normal). With $E=210$ GPa and $\nu=0.3$, $E/[(1+\nu)(1-2\nu)]=404$ GPa, and

$$
\sigma_x=404\times[0.7\times1.2+0.3\times0.3]\times10^{-3}\ \mathrm{GPa}=376\ \mathrm{MPa}
$$

with $\sigma_y=262$ MPa and $\sigma_z=149$ MPa. A longitudinal stress near the yield strength of the parent plate is typical of an as-welded joint and is exactly what fracture assessments such as BS 7910 and R6 must assume unless a post-weld heat treatment has relaxed it. Note that $\sigma_z$ is far from zero: inside a thick section the stress state is triaxial, which the surface-only $\sin^2\psi$ method (Chapter 42) cannot reveal. With a typical strain uncertainty of $50\times10^{-6}$, stresses are known to about ±10–15 MPa. Neutron strain scanning is routinely applied to rail welds and wheels, turbine discs, pressure-vessel nozzles, aircraft wing-skin friction-stir welds and additively manufactured parts.

### Inelastic and quasielastic scattering

Measuring the energy the neutron gains or loses maps **phonon dispersion curves** (triple-axis spectrometers on single crystals), which test interatomic potentials and DFT calculations (Chapters 45 and 46), and **magnon** dispersions in magnets. Vibrational spectroscopy with neutrons has no optical selection rules and is dominated by hydrogen, so it identifies hydrogen bonding sites in metal hydrides, zeolites and polymers. **Quasielastic scattering**, a small broadening of the elastic line, measures the jump frequencies and geometry of diffusing atoms: hydrogen in metals, lithium and sodium in solid electrolytes, water in cement and clays, and chain dynamics in polymers. **Neutron imaging** (radiography and tomography) sees hydrogen-rich materials inside metals: water distribution in an operating fuel cell, hydride blisters in zirconium cladding, oil inside engine parts, adhesive inside a bonded joint.

---

## 43.7 Atom-probe tomography

**Atom-probe tomography (APT)** removes atoms one at a time from a needle-shaped specimen and identifies each by time-of-flight mass spectrometry, then reconstructs their original positions in three dimensions. It is the only technique that combines near-atomic spatial resolution with chemical identification of every atom, including light elements, at the parts-per-million level.

### Field evaporation and mass spectrometry

A specimen with a tip radius $R$ of 20–100 nm, prepared by electropolishing or focused-ion-beam milling, is cooled to 20–80 K in ultra-high vacuum and held at a standing voltage $V$ of a few kilovolts. The field at the apex is

$$
F=\frac{V}{k_fR}
$$

with $k_f$ a geometric factor of about 3–8. Superimposed voltage pulses (for metals) or laser pulses (for semiconductors, oxides and other poor conductors) raise the field or temperature just enough to **field-evaporate** surface atoms as ions, one pulse in about a hundred producing an event. Evaporation fields are about 19 V/nm for aluminium, 33 V/nm for iron and 57 V/nm for tungsten.

**Worked example — voltage and flight time.** For iron with $k_f=5$ and $R=50$ nm, $V=F\,k_fR=33\times10^9\times5\times50\times10^{-9}=8.3$ kV. As atoms are removed the tip blunts and the voltage is raised automatically, typically to 10–15 kV before the specimen fractures or the run ends. An ion of charge $ne$ accelerated through $V$ reaches speed $v=\sqrt{2neV/m}$, so for a flight path $L$ the mass-to-charge ratio follows from the flight time:

$$
\frac{m}{n}=\frac{2eV\,t^2}{L^2}
$$

A $^{56}$Fe$^{2+}$ ion ($m/n=28$ Da) at 6 kV over 0.10 m arrives after $t=L\sqrt{m/(2neV)}=491$ ns; a timing precision of about 0.1 ns, plus correction for the energy spread of voltage-pulsed ions, gives the mass resolution needed to separate isotopes and overlapping peaks. A typical run collects $10^7$–$10^8$ ions: a 50 × 50 × 200 nm$^3$ volume of steel contains $4.2\times10^7$ atoms, of which about half are detected at a detection efficiency of 50 %.

### Reconstruction and its limits

The detector records the hit position and sequence of each ion. A projection model with an assumed tip shape converts hit positions to lateral coordinates and the cumulative evaporated volume to depth. Depth resolution is excellent (0.1–0.2 nm; atomic planes are often visible), lateral resolution 0.3–0.5 nm. The reconstruction is a model, however: phases with different evaporation fields make the tip surface uneven, producing **local magnification** that distorts precipitates and smears interfaces; trajectory overlaps degrade positions near poles; molecular ions and overlapping mass peaks (for example $^{14}$N$^+$ and $^{28}$Si$^{2+}$, both at 14 Da) complicate composition; detection efficiency below 100 % and specimen fracture limit volumes and statistics.

> **Status of the principle: APT point-projection reconstruction**
> *Approximate.* Assumes a hemispherical tip of known radius evolving smoothly and a fixed image-compression factor; it is calibrated against known lattice spacings or correlative TEM, and fails near phases with strongly different evaporation fields.

### What APT reveals

Analysis tools identify **clusters** (by maximum separation between solute atoms), plot **proximity histograms** of concentration against distance from an interface, and quantify segregation at boundaries in atoms per nm$^2$. Applications span the discipline (Figure 43.5): the Cu–Ni–Mn–Si clusters of irradiated pressure-vessel steels of the opening (a cluster of 1.5 nm radius in iron contains about 1200 atoms); carbon partitioning between martensite and retained austenite in quenched-and-partitioned and bainitic steels (Chapter 15); boron and carbon segregation to grain boundaries in nickel superalloys; nanometre Al$_3$(Sc,Zr) precipitates in aluminium alloys; deuterium trapped at carbides in hydrogen-embrittlement studies of steels; dopant distributions in transistors and III–N quantum wells; and the chemistry of tooth enamel and bone mineral.

<!-- FIGURE 43.5 | figures/ch43/fig-43-5-apt-reconstruction.png | schematic | Atom-probe tomography: instrument principle and a reconstruction of solute clusters in irradiated pressure-vessel steel with a proximity histogram. | Content: left: schematic of needle specimen (apex radius 50 nm) at standing voltage ~8 kV with pulsing, ion trajectories (Fe2+ shown) flying 0.1 m to a position-sensitive detector; labels 'time of flight → m/n', 'hit position → x,y', 'sequence → z'. Middle: reconstructed box 50 x 50 x 200 nm with Fe atoms omitted, Cu atoms (orange), Ni (green), Mn (purple), Si (grey) showing ~20 clusters of 1-2 nm radius; scale bar 20 nm. Right: proximity histogram, concentration (at.%) vs distance from cluster interface (-2 to +2 nm): Cu rising from ~0.05 at.% in matrix to ~30 at.% in core, Ni to ~20 at.%, Mn ~10 at.%, Si ~8 at.%; Fe complementary. -->

---

## 43.8 Aberration-corrected STEM: HAADF, EELS and 4D-STEM

### Correcting the lens

Magnetic electron lenses have unavoidable spherical aberration (Scherzer's theorem for round lenses), which limited TEM resolution to 0.15–0.2 nm for decades despite electron wavelengths of 2–3 pm. Multipole **aberration correctors**, practical since about 2000, cancel it. The probe can then use a larger convergence semi-angle $\alpha$, and its diffraction-limited size $d\approx0.61\lambda/\alpha$ shrinks.

**Worked example — probe size.** At 300 kV ($\lambda=1.97$ pm) with a corrected convergence angle of 30 mrad, $d\approx0.61\times1.97/0.030=40$ pm. An uncorrected 200 kV instrument ($\lambda=2.51$ pm) is restricted to about 10 mrad by aberrations, giving 153 pm. The corrected probe is smaller than the separation of atomic columns in any crystal viewed along a low-index zone (for silicon along ⟨110⟩, the "dumbbell" columns are 136 pm apart), so individual columns are scanned one at a time. Practical resolution of 50–70 pm also depends on stability, source size and specimen quality.

### HAADF, ABF and EELS

In **scanning TEM (STEM)** the probe is rastered across a thin specimen and different detectors collect different signals at each position (Figure 43.6). A **high-angle annular dark-field (HAADF)** detector collects electrons scattered beyond about 60–80 mrad, mostly by Rutherford-like scattering near nuclei; intensity scales roughly as $Z^{1.6\text{–}2}$, so heavy columns are bright and contrast is directly interpretable as **Z-contrast**. Single dopant atoms (Pt on a ceria catalyst support, Hf in a silicon channel, rare-earth atoms segregated to grain boundaries in silicon nitride) can be seen. **Annular bright-field (ABF)** imaging, from a ring inside the bright-field disc, shows light columns such as oxygen, nitrogen, lithium and even hydrogen alongside heavy ones, essential for oxide interfaces and battery cathodes.

> **Status of the principle: HAADF Z-contrast**
> *Empirical.* The exponent of $Z$ depends on detector angles, accelerating voltage and thickness, and channelling along columns makes intensity non-linear in thickness; quantitative work compares with image simulations.

**Electron energy-loss spectroscopy (EELS)** analyses the energy lost by transmitted electrons. **Core-loss edges** identify elements, with particular sensitivity to light elements (B, C, N, O) where EDS is weak. Their fine structure (**ELNES**) carries bonding and oxidation state: the L$_3$/L$_2$ intensity ratio of Mn or Fe, the C K-edge shape distinguishing sp$^2$ graphite-like from sp$^3$ diamond-like bonding in DLC coatings (Chapter 41). Mapping across an interface column by column shows, for example, Ti$^{3+}$ in the first unit cells of an oxide heterostructure or oxygen vacancies at a grain boundary in an electrolyte. **Low-loss** EELS measures plasmons, band gaps and specimen thickness through the log-ratio relation $t=\lambda_{in}\ln(I_t/I_0)$; if the total intensity is 1.5 times the zero-loss intensity and the inelastic mean free path is about 110 nm, $t=110\times\ln1.5=45$ nm. Monochromated instruments with energy resolution below 10 meV detect vibrational modes and phonons from nanometre regions.

> **Status of the principle: EELS log-ratio thickness**
> *Approximate.* Assumes Poisson statistics of independent inelastic events and a known mean free path, which depends on composition, voltage and collection angle and is itself uncertain by 10–20 %.

### 4D-STEM

Fast **pixelated detectors** record the entire diffraction pattern (two dimensions) at every probe position (two more), giving a four-dimensional data set. From it, virtual detectors of any shape can be applied after the experiment, and many quantities can be mapped:

- **Strain maps** from the positions of diffracted discs, to about $10^{-4}$, across transistors, precipitates and dislocation cores.
- **Orientation and phase maps** of nanocrystalline metals, beam-sensitive polymers and pharmaceutical crystals, at nanometre steps (like EBSD with a hundred times finer resolution).
- **Electric and magnetic fields** from the deflection of the central disc (differential phase contrast), showing p–n junctions, ferroelectric polarization and magnetic skyrmions.
- **Electron ptychography**, which computationally solves for the specimen potential from overlapping diffraction patterns and has reached resolutions below 0.05 nm, limited by thermal vibration of the atoms themselves, at lower doses than conventional imaging.

**Worked example — the data problem.** A 512 × 512 scan with a 256 × 256-pixel pattern stored at 2 bytes per pixel is $512^2\times256^2\times2=34$ GB. At 1 ms per pattern it takes 262 s, during which drift and beam damage accumulate; detectors running at 10 kHz or faster cut this to 26 s. Data volumes of this size have turned microscopy into a computational field, with automated analysis and machine-learning classification (Chapters 44 and 47).

<!-- FIGURE 43.6 | figures/ch43/fig-43-6-stem-detectors.png | schematic | Detector geometry in an aberration-corrected STEM: HAADF, ABF, EELS and pixelated 4D-STEM detection. | Content: vertical ray diagram: electron source, aberration corrector (hexapole/octupole block labelled 'Cs corrector'), probe-forming lens giving convergent probe (semi-angle 30 mrad, probe size ~40 pm at 300 kV) on a thin crystal with atomic columns. Below specimen: concentric annular detectors labelled by collection angles: ABF (11-22 mrad), ADF (40-80 mrad) and HAADF (> 80 mrad); central hole passing electrons into an EELS spectrometer (magnetic prism, energy-loss spectrum sketch with zero-loss peak, plasmon, and a core-loss edge labelled 'O K 532 eV'). Alternative inset: pixelated camera recording full convergent-beam pattern at each probe position (x, y, kx, ky = '4D'). Side panel: simulated HAADF image of Si <110> dumbbells 136 pm apart and SrTiO3 <100> with bright Sr and Ti columns and O visible only in the ABF image. -->

---

## 43.9 Cryo-EM for soft materials

Polymers, hydrogels, proteins, organic electronics, metal–organic frameworks and lithium metal are damaged by the electron beam far faster than metals or ceramics: radiolysis breaks bonds, mass is lost, and crystallinity disappears after doses a hundred to a thousand times smaller than a metal tolerates. Hydrated specimens cannot even enter the vacuum unless their water is immobilized. **Cryo-electron microscopy (cryo-EM)** addresses both problems.

**Vitrification.** A thin film of the aqueous specimen (a protein solution, a micelle dispersion, a hydrogel) is blotted on a grid and plunged into liquid ethane, cooling at $10^5$ K/s or more, fast enough that water solidifies as amorphous (vitreous) ice instead of crystalline ice, whose crystals would destroy the structure and diffract strongly. The specimen is kept below about −140 °C during imaging. Vitrification preserves self-assembled structures exactly as they were in solution: block-copolymer micelles and vesicles, lipid nanoparticles for drug and mRNA delivery, the fibril network of a hydrogel scaffold, the adsorbed protein layer on an implant surface.

**Low-dose imaging and averaging.** Total doses are limited to roughly 20–60 electrons per Å$^2$ (40 e/Å$^2$ is about 640 C/m$^2$). Each image is therefore extremely noisy. Direct electron detectors, which count individual electrons with high efficiency at hundreds of frames per second, allow motion correction of the specimen drift within an exposure. In **single-particle analysis** tens to hundreds of thousands of images of identical molecules in random orientations are classified, aligned and averaged into a three-dimensional reconstruction; resolutions better than 2 Å are now achieved for proteins, which won the 2017 Nobel Prize in Chemistry. For materials engineering this means the structure of enzymes used in biocatalytic processing, of protein–surface complexes relevant to biomaterials (Chapter 31), and of viral capsids and protein cages used as nanoscale templates. **Cryo-electron tomography** reconstructs unique, non-repeating objects (a polymer–nanoparticle composite, a bacterial biofilm on a catheter) from tilt series, and **cryo-FIB** milling cuts thin lamellae from frozen bulk specimens.

**Batteries and beam-sensitive solids.** Cryo-EM moved into hard materials science around 2017 when it was used to image lithium metal dendrites and their solid–electrolyte interphase (SEI) at atomic resolution, structures that melt or decompose within seconds under a room-temperature beam. Cryogenic conditions slow radiolytic damage and mass loss, typically by a factor of a few, and stop reactions with residual gas. Similar protocols now image MOFs, perovskite solar absorbers, organic semiconductors and the hydration products of cement.

> **Boundary.** The image-formation and reconstruction mathematics of cryo-EM (contrast transfer function, Fourier-slice theorem, maximum-likelihood classification) belong to Engineering Physics and The Mathematics Universe; here only what the methods deliver and when they are needed is described.

---

## 43.10 Choosing among the advanced methods

Large-facility and atomic-resolution methods are expensive in time, preparation and access, so they are used when a question cannot be answered otherwise and are paired with the laboratory toolkit of Chapter 42 to establish representativeness.

| Question | First-choice method | Probe volume | Complementary method |
|---|---|---|---|
| Oxidation state of a dilute element, in a working device | XANES | mm$^3$ (µm with a microbeam) | XPS (surface), EELS (nm) |
| Local structure without long-range order | EXAFS, PDF | mm$^3$ | Neutron total scattering, ELNES |
| Size and fraction of 1–100 nm features in bulk | SAXS, SANS | mm$^3$ | TEM, APT (local) |
| Composition of nm clusters or a grain boundary in 3D | APT | $10^{-22}$–$10^{-21}$ m$^3$ ($10^5$–$10^6$ nm$^3$) | STEM-EDS/EELS |
| Atomic structure of an interface | Aberration-corrected STEM (HAADF, ABF) | nm$^3$ slice | DFT (Chapter 45) |
| Residual stress deep inside a part | Neutron diffraction, high-energy synchrotron XRD | mm$^3$ gauge | Contour method, hole drilling |
| Internal porosity and damage in 3D | X-ray tomography | mm$^3$–cm$^3$ | Serial sectioning |
| Hydrogen, lithium, oxygen positions; magnetic order | Neutron diffraction | mm$^3$–cm$^3$ | ABF-STEM, APT for H/D |
| Structure of soft or hydrated assemblies | Cryo-EM, SAXS/SANS | nm (EM), mm$^3$ (scattering) | Rheology, DSC |

Two practical lessons recur. First, local and averaging methods answer different questions and are most powerful together: SANS gives the number density and mean size of the irradiation clusters in a pressure vessel, APT their composition, and TEM their interaction with dislocations; none alone predicts the embrittlement. Second, the most informative experiments increasingly follow a material while it is being processed, loaded or operated, which is the subject of the next chapter.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are these methods applied while a sample is heated, strained, charged or reacting? | Chapter 44 (in-situ and operando studies) |
| How do positron annihilation, Mössbauer and solid-state NMR complement them for vacancies, iron chemistry and local environments? | Chapter 44 |
| How are EXAFS, EELS and phonon spectra calculated to interpret measurements? | Chapter 45 (DFT) |
| How are APT and SANS cluster data used to parametrize kinetic Monte Carlo and cluster-dynamics models? | Chapter 46 |
| How are terabyte data sets from 4D-STEM, tomography and beamlines analysed automatically? | Chapters 44 and 47 |
| Where do Bragg diffraction, structure factors and reciprocal space come from? | Chapter 4 (back reference) |
| How do irradiation clusters embrittle steels, and how is this used in plant-life assessment? | Chapter 33 (back reference) |

**Next:** Chapter 44 puts the specimen inside the instrument while it is heated, strained, biased or electrochemically cycled, and shows how in-situ, operando and correlative methods connect what is seen to how a material behaves.
