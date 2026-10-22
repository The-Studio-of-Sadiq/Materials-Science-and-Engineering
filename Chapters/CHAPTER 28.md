# Chapter 28 — Optical and Photonic Materials

*Part VI · Physical and Functional Properties*

A defence contractor needs a window for the nose of a missile that must see in the visible and mid-infrared, survive rain erosion at Mach 3, and withstand a thermal shock of several hundred kelvin in a second. Glass is too weak and absorbs beyond 3 µm. Germanium transmits the infrared but is opaque to visible light and loses transparency when hot. Single-crystal sapphire is strong and transparent from the ultraviolet to 5 µm, but expensive to grow and machine into domes. The answer that eventually flew was a polycrystalline ceramic — spinel or aluminium oxynitride — sintered to full density so that not one pore in a million remained, with grains of the right size and a cubic crystal structure so that the grain boundaries would not scatter light. The same materials problem, without the missile, arises in a watch crystal, a smartphone camera cover, a high-pressure sodium lamp, a laser gain medium and a transparent armour window: what makes a solid transparent, and what makes most of them not?

This chapter explains how light interacts with matter and how structure sets the refractive index, dispersion, absorption, colour and scattering of materials; then turns to the materials that make light (phosphors, LEDs and lasers), guide it (optical fibres and waveguides), and control it (nonlinear, electro-optic, photonic-crystal and metamaterial structures). The *Materials Core (EEE)* book, Chapter 14, treats optoelectronic materials in more depth.

> **Why is window glass transparent while the sand it is made from is white?**
> **Why are gold and copper coloured, but silver and aluminium not?**
> **Why does a polycrystalline alumina tube transmit light diffusely, but a polycrystalline spinel window can be read through?**
> **Why do optical fibres carry signals for 100 km at 1.55 µm but only a few kilometres at 0.85 µm?**

| Concept | Engineering destination |
|---|---|
| Reflection, refraction, absorption, scattering | Windows, lenses, coatings, solar glazing, sensor covers |
| Refractive index, Sellmeier dispersion, birefringence | Lens design, achromats, polarizers, stress analysis by photoelasticity |
| Colour in metals, insulators, semiconductors, pigments | Paints, pigments, glass colourants, gemstones, architectural coatings |
| Transparency in ceramics and polymers | Transparent armour, IR domes, lamp envelopes, clear packaging, medical devices |
| Luminescence, phosphors, LEDs, lasers | Lighting, displays, medical scintillators, laser cutting and welding |
| Optical fibres and waveguides | Telecommunications, fibre-optic strain and temperature sensing, endoscopy |
| Nonlinear and electro-optic materials | Frequency conversion of lasers, optical modulators for data links |
| Photonic crystals, metamaterials, metasurfaces | Dielectric mirrors, VCSELs, structural colour, flat lenses, radiative cooling |

**Roadmap.** Light–matter interaction (28.1) → refractive index, its origin and Sellmeier dispersion (28.2) → colour (28.3) → transparency and opacity in ceramics and polymers (28.4) → luminescence, LEDs and lasers (28.5) → fibres and waveguides (28.6) → nonlinear and electro-optic materials (28.7) → photonic crystals and metamaterials (28.8).

---

## 28.1 Interaction of light with matter: refraction, dispersion, absorption, scattering

### Light as a field acting on bound and free charges

Light is an electromagnetic wave with an electric field oscillating at $10^{14}$–$10^{15}$ Hz in the visible (wavelength 400–700 nm, photon energy 1.8–3.1 eV). In a material, that field drives the same charges whose polarization was discussed in Chapter 25: bound electrons, ions and, in metals and doped semiconductors, free carriers. At optical frequencies only the electrons can follow (ions are too heavy above about $10^{13}$ Hz), so the optical properties are dominated by **electronic polarization** in insulators and **free-electron response** in metals.

When light meets a material, its energy is partitioned among reflection $R$, absorption $A$ and transmission $T$, with

$$
R+A+T=1
$$

for a slab (scattering counts as a loss from the transmitted beam). The two numbers that describe a homogeneous material are combined in the **complex refractive index**

$$
\tilde n=n+i\kappa,\qquad \tilde n^2=\varepsilon_r(\omega)
$$

where $n$ sets the phase velocity $c/n$ and $\kappa$, the **extinction coefficient**, sets the attenuation. The intensity decays as $I=I_0\exp(-\alpha x)$ (**Beer–Lambert law**) with absorption coefficient $\alpha=4\pi\kappa/\lambda$.

> **Status of the principle: Beer–Lambert law**
> *Approximate.* It assumes linear absorption by a homogeneous medium, with no scattering and intensity low enough that absorbers do not saturate. It fails at laser intensities (two-photon absorption, saturable absorption) and in turbid or scattering media.

### Refraction and reflection

At an interface between media of index $n_1$ and $n_2$, light bends according to **Snell's law**, $n_1\sin\theta_1=n_2\sin\theta_2$. Going from high to low index, beyond the critical angle $\theta_c=\arcsin(n_2/n_1)$ the light is totally internally reflected — the principle of the optical fibre (Section 28.6). Part of the light is always reflected. At normal incidence for a non-absorbing material the **Fresnel reflectance** is

$$
R=\left(\frac{n_2-n_1}{n_2+n_1}\right)^2
$$

so glass ($n=1.5$) reflects 4 % per surface, sapphire ($n=1.76$) 7.6 %, diamond ($n=2.42$) 17 %, and silicon ($n\approx3.5$ in the near infrared) 31 %. High reflection is part of diamond's brilliance and a major loss for solar cells and LEDs.

> **Status of the principle: Fresnel equations**
> *Fundamental.* They follow from Maxwell's equations with the boundary conditions on tangential fields. They assume flat, smooth interfaces; rough surfaces add diffuse scattering.

**Worked example — antireflection coatings.** A thin film of index $n_f$ and thickness $\lambda/(4n_f)$ makes the reflections from its top and bottom surfaces cancel by destructive interference. On glass ($n_s=1.52$) in air, the reflectance at the design wavelength becomes

$$
R=\left(\frac{n_s-n_f^2}{n_s+n_f^2}\right)^2
$$

which is zero for $n_f=\sqrt{n_s}=1.23$. No durable solid has an index so low, so the standard choice is MgF$_2$ ($n_f=1.38$): at 550 nm the film is $550/(4\times1.38)=99.6$ nm thick, and $R=[(1.52-1.904)/(1.52+1.904)]^2=1.26$ %, a third of the uncoated 4.3 %. For a silicon solar cell ($n_s\approx3.9$ at 600 nm), the ideal index is about 2.0 — exactly that of PECVD silicon nitride, which at 75 nm thickness reduces reflection at 600 nm to nearly zero and also passivates the surface (Chapter 26). This is why solar cells are dark blue: the coating is optimized near the peak of the solar spectrum and reflects some violet. Multilayer stacks broaden the low-reflection band for camera lenses and spectacles.

### Dispersion

The refractive index depends on wavelength — **dispersion** — because the material's response depends on how close the light frequency is to its electronic and ionic resonances (Section 28.2). In the transparent range of glasses, $n$ falls slowly with increasing wavelength (normal dispersion), so blue light is refracted more than red: the origin of prismatic colour, of chromatic aberration in lenses, and of the spreading of short pulses in fibres.

### Absorption

Absorption occurs wherever photons can be taken up by an excitation of the material:

- **Electronic transitions across a band gap** in semiconductors and insulators — strong absorption ($\alpha\sim10^4$–$10^6$ cm$^{-1}$) for photon energies above $E_g$. This sets the ultraviolet edge of glasses and ceramics and the colour of semiconductors.
- **Transitions within partly filled d or f shells** of transition-metal and rare-earth ions — weak, narrow or broad bands that give colour to gemstones and glasses (Section 28.3).
- **Free-carrier absorption** in metals and doped semiconductors.
- **Lattice vibrations (phonons)** — multi-phonon absorption sets the infrared edge of transparency. Light atoms with strong bonds (Si–O, Al–O) vibrate at high frequency, so oxides become opaque at 3–6 µm; heavy atoms with weak bonds (Zn–Se, Ge, chalcogenides, alkali halides) vibrate slowly, so they transmit to 10–20 µm. This is why thermal-imaging lenses are made of germanium, ZnSe or chalcogenide glass, not silica.

Each material is therefore transparent only within a **window** between its electronic absorption edge in the ultraviolet and its phonon edge in the infrared (Figure 28.1).

<!-- FIGURE 28.1 | figures/ch28/fig-28-1-transmission-windows.png | map | Transparency windows of optical materials: each is bounded by electronic absorption at short wavelengths and lattice absorption at long wavelengths. | Content: horizontal log axis wavelength 0.1 to 30 um; visible band 0.4–0.7 um shaded in spectrum colours; atmospheric windows 3–5 and 8–12 um shaded grey. Horizontal bars: LiF 0.11–7, CaF2 0.13–10, MgF2 0.12–7, fused silica 0.16–3.5 (with OH dip at 2.7), BK7 glass 0.33–2.5, sapphire 0.17–5.5, MgAl2O4 spinel 0.2–5.5, AlON 0.22–5, YAG 0.21–5.5, diamond 0.23–50 (with weak multiphonon band 2.5–6), ZnS multispectral 0.37–12, ZnSe 0.5–20, Si 1.2–7, Ge 2–14, GaAs 0.9–15, chalcogenide glass (As2S3) 0.6–11, PMMA 0.38–1.6, polycarbonate 0.4–1.6. Label which bound is set by band gap and which by phonons. -->

### Scattering

Light is scattered wherever the refractive index changes over a distance comparable to or smaller than the wavelength: pores, inclusions, second phases, grain boundaries in birefringent crystals, density and composition fluctuations in glass, and crystalline regions in polymers. For particles much smaller than the wavelength, **Rayleigh scattering** scales as $\lambda^{-4}$ and with the square of the particle volume and of the index contrast — why the sky is blue, why fine smoke looks blue against a dark background, and why the attenuation of optical fibres falls steeply with wavelength. For particles comparable to the wavelength, **Mie scattering** is strong and almost wavelength-independent, so clouds, milk, paper, snow and white paint look white. Scattering, not absorption, makes most solids opaque: crushed glass and sand, white marble, porous alumina and polyethylene are made of transparent constituents and are opaque only because they contain many interfaces.

---

## 28.2 Refractive index and its origin; Sellmeier

### The Lorentz oscillator

Model each bound electron as a charge on a spring with natural frequency $\omega_0$ and weak damping, driven by the optical field. Below resonance it follows the field in phase and adds to the polarization, so $n>1$; approaching resonance the response grows; above resonance it lags and reduces the polarization. Summing over oscillators with strengths $f_j$ gives

$$
n^2(\omega)-1=\frac{Ne^2}{\varepsilon_0m}\sum_j\frac{f_j}{\omega_j^2-\omega^2}
$$

away from the resonances. Two structural conclusions follow. First, the index grows with the **density of polarizable electrons** $N$ and with their polarizability; for a dense medium, the local-field correction gives the **Lorentz–Lorenz relation**, the optical form of the Clausius–Mossotti equation of Chapter 25:

$$
\frac{n^2-1}{n^2+2}=\frac{N\alpha_e}{3\varepsilon_0}
$$

Second, the index is higher in materials whose resonances lie at lower frequency, that is, with smaller band gaps. Empirically $n$ rises as $E_g$ falls: fluorides ($E_g>10$ eV, $n\approx1.4$), silica (9 eV, 1.46), alumina (8.8 eV, 1.76), ZnS (3.6 eV, 2.37), TiO$_2$ (3.0 eV, 2.6–2.9), silicon (1.1 eV, 3.5), germanium (0.66 eV, 4.0).

> **Status of the principle: Lorentz–Lorenz relation**
> *Approximate.* It assumes isotropic, non-interacting polarizable units in a Lorentz local field. It predicts well how the index of a glass or polymer changes with density (useful for estimating porosity and stress-induced index changes), but not absolute values in strongly covalent or anisotropic solids.

| Material | $n_d$ (589 nm) | Abbe number $V_d$ | Notes |
|---|---|---|---|
| Aerogel (silica) | 1.01–1.05 | — | Mostly air; Cherenkov detectors, insulation |
| MgF$_2$ | 1.38 | 106 | Antireflection coatings, UV optics |
| CaF$_2$ | 1.434 | 95 | Low-dispersion lens elements, UV lithography |
| Fused silica | 1.458 | 68 | Fibres, UV optics, lithography lenses |
| PMMA | 1.49 | 57 | Lenses, light guides, POF |
| N-BK7 crown glass | 1.517 | 64 | General-purpose optical glass |
| Soda-lime window glass | 1.52 | 59 | Windows, containers |
| Polycarbonate | 1.586 | 30 | Spectacle and safety lenses |
| SF11 dense flint glass | 1.785 | 26 | High-index, high-dispersion lens elements |
| Sapphire (Al$_2$O$_3$, ordinary ray) | 1.768 | 72 | Windows, watch crystals, LED substrates |
| MgAl$_2$O$_4$ spinel | 1.72 | 60 | Transparent armour, IR domes |
| Y$_3$Al$_5$O$_{12}$ (YAG) | 1.83 | 53 | Laser hosts, phosphors |
| Cubic zirconia (Y-stabilized) | 2.15–2.18 | 33 | Gem simulant, high-index optics |
| Diamond | 2.417 | 55 | Windows, heat spreaders, gems |
| TiO$_2$ rutile (ordinary / extraordinary) | 2.61 / 2.90 | ≈10 | White pigment, high-index coatings |
| Si (at 1.55 µm) | 3.48 | — | Silicon photonics, IR optics |
| Ge (at 10 µm) | 4.00 | — | Thermal-imaging lenses |

*Table 28.1 — Refractive index and dispersion of optical materials at room temperature (typical).*

### Sellmeier dispersion

For practical design the Lorentz form is written with resonances at wavelengths $\lambda_j$ and fitted strengths $B_j$, the **Sellmeier equation**:

$$
n^2(\lambda)=1+\sum_{j=1}^{3}\frac{B_j\lambda^2}{\lambda^2-C_j},\qquad C_j=\lambda_j^2
$$

Two terms usually describe ultraviolet electronic resonances and one an infrared lattice resonance; between them, the index falls smoothly with wavelength (Figure 28.2). Glass catalogues list $B_j$ and $C_j$ for every glass, and lens-design software uses nothing else. A compact measure of dispersion in the visible is the **Abbe number**

$$
V_d=\frac{n_d-1}{n_F-n_C}
$$

using the helium d (587.6 nm), hydrogen F (486.1 nm) and C (656.3 nm) lines. Crown glasses ($V_d>50$) disperse little; flint glasses, whose lead or titanium oxides add low-lying resonances, have high index and high dispersion ($V_d<50$). An achromatic doublet pairs a crown and a flint so that their dispersions cancel.

> **Status of the principle: Sellmeier equation**
> *Empirical.* It is the Lorentz oscillator form with fitted resonance positions and strengths. Within a material's transparency window it reproduces the index to $10^{-5}$ or better; it fails near absorption bands, where damping must be included.

**Worked example — dispersion of fused silica.** Malitson's Sellmeier coefficients for fused silica are $B=(0.6961663,\ 0.4079426,\ 0.8974794)$ and resonance wavelengths $\lambda_j=(0.0684043,\ 0.1162414,\ 9.896161)$ µm. At $\lambda=0.5893$ µm,

$$
n^2=1+\frac{0.69617(0.34728)}{0.34728-0.00468}+\frac{0.40794(0.34728)}{0.34728-0.01351}+\frac{0.89748(0.34728)}{0.34728-97.934}=2.12694
$$

so $n=1.4584$. The same equation gives $n_F=1.4631$ and $n_C=1.4564$, hence $V_d=(1.4584-1)/(1.4631-1.4564)=67.8$, a low-dispersion glass. In the infrared, $n=1.4468$ at 1.31 µm and $1.4440$ at 1.55 µm. The second derivative of $n(\lambda)$ sets the **material dispersion** that spreads short pulses in a fibre: it passes through zero near 1.27 µm, where the ultraviolet and infrared resonances balance, and at 1.55 µm amounts to about 22 ps per nanometre of source linewidth per kilometre. Silica's two resonances, one electronic and one Si–O vibrational, thus set the two telecom windows of Section 28.6.

<!-- FIGURE 28.2 | figures/ch28/fig-28-2-sellmeier-dispersion.png | plot | Refractive index against wavelength for optical materials: normal dispersion between ultraviolet and infrared resonances. | Content: x-axis wavelength 0.2 to 5 um (log); y-axis refractive index 1.35 to 2.5. Curves from Sellmeier fits: CaF2 (1.434 at 0.589), fused silica (1.458 at 0.589, 1.444 at 1.55, rising steeply below 0.25 um), N-BK7 (1.517, ending near 2.5 um), sapphire ordinary ray (1.768), YAG (1.83), diamond (2.417 at 0.589, about 2.38 at 2 um). Mark the d, F, C lines with vertical ticks; inset: fused silica material dispersion D from 1.0 to 1.7 um crossing zero at 1.27 um and about +22 ps/(nm km) at 1.55 um. -->

### Birefringence

In non-cubic crystals the index depends on the polarization and direction of light, the optical counterpart of the tensor properties of Chapter 4. Uniaxial crystals have an ordinary index $n_o$ and an extraordinary index $n_e$; their difference, the **birefringence**, ranges from $-0.008$ in sapphire and $+0.009$ in quartz to $-0.17$ in calcite and $+0.29$ in rutile. Birefringent crystals make wave plates and polarizers, and birefringence enables phase matching in nonlinear optics (Section 28.7). Isotropic materials become birefringent under stress or orientation: **photoelasticity**, the stress-induced birefringence of glass and polymers, reveals residual stress in tempered glass, frozen-in moulding stresses in polycarbonate lenses and polymer parts, and stress fields in transparent models of engineering components. Oriented polymer films (stretched PET, PVA polarizer films) are birefringent by chain alignment.

---

## 28.3 Colour in metals, insulators, semiconductors and pigments

Colour is what remains of white light after the material has absorbed, reflected or scattered parts of the spectrum. Its origin differs in each class of material, and in each case it can be traced to an electronic structure.

### Metals

Free electrons in a metal respond to fields below the **plasma frequency**

$$
\omega_p=\sqrt{\frac{ne^2}{\varepsilon_0m^*}}
$$

by screening them: below $\omega_p$ the permittivity is negative, light cannot propagate, and the metal reflects almost everything. For aluminium ($n=1.8\times10^{29}$ m$^{-3}$) the free-electron plasma wavelength is about 80 nm, deep in the ultraviolet, so aluminium reflects about 90 % across the whole visible and is the standard mirror coating for telescopes and the reflective layer of food packaging. Silver is the best visible reflector (95–99 %), though its d electrons pull its effective plasma edge to about 320 nm. In **copper and gold**, transitions from filled d bands to the Fermi level begin at about 2.1 eV (590 nm) and 2.4 eV (520 nm) respectively, so blue and green light are absorbed while red and yellow are reflected (Figure 28.3). Alloying shifts these edges: brass is yellower than copper, and gold alloys with silver and copper range from green-yellow to red. Titanium nitride, with a plasma edge in the visible, is gold-coloured and is used as a hard decorative coating on tools and fittings (Chapter 37).

Doped oxides with fewer free carriers have plasma edges in the infrared. Tin-doped indium oxide with $10^{21}$ carriers/cm³ and an effective mass of $0.35m_0$ reflects beyond about 1.2 µm but transmits visible light — the basis of transparent electrodes and of the low-emissivity coatings on energy-saving windows, which reflect thermal infrared back into a building while letting daylight through.

<!-- FIGURE 28.3 | figures/ch28/fig-28-3-metal-reflectance.png | plot | Reflectance of metals: free electrons reflect below the plasma frequency, and interband absorption gives copper and gold their colour. | Content: x-axis wavelength 200 to 2000 nm; y-axis normal-incidence reflectance 0 to 100 %. Curves for evaporated films: Ag (rising steeply from 320 nm to 95 % at 450 nm, 98–99 % beyond), Al (90–92 % across 200–2000 nm with dip to about 86 % at 830 nm), Au (about 35–40 % below 500 nm, steep rise 500–600 nm, above 95 % beyond 700 nm), Cu (about 40–50 % below 550 nm, steep rise near 580 nm, 95 % beyond 700 nm). Visible band shaded in spectrum colours; annotate d-band absorption edges for Cu and Au. -->

### Insulators: ions, defects and charge transfer

Pure wide-gap insulators (silica, alumina, MgO, diamond) are colourless. Their colour comes from small concentrations of impurities and defects:

- **Transition-metal ions.** The partly filled d shell of an ion such as Cr$^{3+}$ is split by the electric field of its neighbouring anions (the **crystal field**), giving absorption bands in the visible whose positions depend on the host. The same Cr$^{3+}$ ion makes ruby red in Al$_2$O$_3$ (strong crystal field, absorbing green and violet) and emerald green in beryl (weaker field). Glass colourants work the same way: Co$^{2+}$ gives cobalt blue, Fe$^{2+}$ the green of ordinary bottle and window glass, Cr$^{3+}$ green, Mn$^{3+}$ purple. Removing iron to below 0.01 % produces the "low-iron" glass used for solar-panel covers and display glass.
- **Charge transfer.** An electron jumping between ions — Fe$^{2+}$ to Ti$^{4+}$ in blue sapphire, or from O$^{2-}$ to Fe$^{3+}$ in hematite (Fe$_2$O$_3$, the red of rust and red ochre) — produces strong, broad absorption.
- **Colour centres.** Point defects that trap electrons or holes, such as F-centres (an electron in an anion vacancy, Chapter 5), colour alkali halides and darken glasses exposed to radiation; deliberately created nitrogen–vacancy centres in diamond are now quantum sensors.

### Semiconductors

A semiconductor absorbs all photons with energy above its band gap and transmits those below (Section 28.1), so its colour is set by $E_g$. Converting energy to wavelength with $\lambda(\mathrm{nm})=1239.8/E(\mathrm{eV})$:

| Material | $E_g$ (eV) | Absorption edge (nm) | Appearance |
|---|---|---|---|
| Diamond | 5.47 | 227 | Colourless (absorbs only UV) |
| GaN, ZnO | 3.4 | 365 | Colourless; transparent |
| TiO$_2$ (rutile) | 3.0 | 413 | White powder; very slightly yellow crystal |
| CdS | 2.42 | 512 | Yellow (cadmium yellow) |
| GaP | 2.26 | 549 | Orange |
| HgS (vermilion) | 2.0 | 620 | Red |
| CdSe | 1.74 | 713 | Black-red |
| Si | 1.12 | 1107 | Opaque, metallic grey (all visible absorbed; reflection gives lustre) |

*Table 28.2 — Band gap and colour of semiconductors (typical).*

Materials whose edge lies in the visible absorb the blue end and look yellow, orange or red; those whose edge lies below 1.8 eV absorb everything and look black or metallic. Alloying tunes the edge continuously, as in the Cd(S,Se) pigments and the GaAsP and AlGaInP red and amber LEDs.

### Pigments, dyes and scattering colour

A **pigment** is an insoluble powder dispersed in a binder; a **dye** is a dissolved molecule. Inorganic pigments use the mechanisms above — Fe$_2$O$_3$ red, Cr$_2$O$_3$ green, cobalt aluminate blue, CdS yellow (now restricted for toxicity), bismuth vanadate yellow. Organic dyes and pigments owe their colour to conjugated π-electron systems whose HOMO–LUMO gap lies in the visible; longer conjugation shifts absorption to longer wavelength. **White** pigments rely on scattering, not absorption: rutile TiO$_2$, with the highest index of any common white material (about 2.7 against about 1.5 for a polymer binder), scatters visible light most strongly when its particles are about 0.2–0.3 µm — half the wavelength of visible light. Some 7 million tonnes are made each year for paints, plastics, paper and sunscreens, and the pigment's band gap at 3.0 eV also makes it a UV absorber and, unless its surface is coated, a photocatalyst that degrades the surrounding binder (Chapter 36). Colour that arises from interference and diffraction in periodic structures — **structural colour** — is discussed in Section 28.8.

---

## 28.4 Transparency and opacity in ceramics and polymers

### What scatters light in a polycrystal

A dense, single-phase solid whose constituents absorb nothing in the visible should be transparent. Most ceramics and many polymers are not, because they scatter. Three microstructural sources dominate:

1. **Porosity.** A pore in a ceramic is an index contrast of 0.5–1.5, the largest possible, and pores of 0.1–1 µm scatter strongly. Transparency requires porosity below about 0.01–0.05 %. Achieving it is a sintering problem (Chapter 38): fine, pure, agglomerate-free powders; sintering aids (MgO in alumina, LiF in spinel) that keep pores attached to grain boundaries so they can be eliminated; and **hot isostatic pressing** to close the last pores.
2. **Birefringent grains.** In a non-cubic ceramic such as alumina, each grain has a different orientation and therefore a slightly different index for a given ray; every grain boundary is a weak scatterer. Cubic ceramics — spinel (MgAl$_2$O$_4$), YAG, AlON, Y$_2$O$_3$, MgO — have no birefringence and can be made fully transparent at any grain size.
3. **Second phases and inclusions**, including impurity-rich grain-boundary films.

For birefringent ceramics the scattering depends on the ratio of grain size to wavelength. In the regime where grains are smaller than the wavelength, Apetz and Bruls showed that the **real in-line transmission** — the fraction of light passing straight through, which determines whether an image can be seen — is approximately

$$
T_{\mathrm{RIT}}=(1-R_s)\exp\!\left(-\frac{3\pi^2\Delta n^2\,r\,d}{\lambda_0^2}\right)
$$

where $\Delta n$ is the effective birefringence, $r$ the grain radius, $d$ the thickness and $R_s$ the reflection loss from both surfaces.

> **Status of the principle: Apetz–Bruls in-line transmission**
> *Approximate.* It treats grains as independent Rayleigh–Gans scatterers smaller than the wavelength, with random orientation and no porosity. It captures the strong dependence on grain size; residual porosity of even 0.01 % adds scattering that it omits.

**Worked example — fine-grained transparent alumina.** Take a 0.8 mm alumina disc ($n=1.76$, $\Delta n=0.008$) at $\lambda_0=640$ nm. Each surface reflects $[(1.76-1)/(1.76+1)]^2=7.6$ %, and with multiple reflections the two surfaces lose $R_s=2R/(1+R)=14$ %. For grains 0.3 µm in diameter ($r=0.15$ µm), the exponent is

$$
\frac{3\pi^2(0.008)^2(0.15\times10^{-6})(0.8\times10^{-3})}{(640\times10^{-9})^2}=0.555
$$

so $T_{\mathrm{RIT}}=0.86\,e^{-0.555}=0.49$ — half the light passes straight through, close to measured values of 50–60 %. With 1 µm grains the exponent becomes 1.85 and $T_{\mathrm{RIT}}=13.5$ %; with 2 µm grains, 2 %; with the 20 µm grains of conventional alumina, essentially zero. Conventional alumina can still have a high *total* transmission (over 90 % in high-pressure sodium lamp tubes, where only diffuse light is needed) but cannot be seen through. The design rules are therefore: choose a cubic ceramic (spinel, AlON, YAG) when image quality matters at any thickness, or make alumina's grains far smaller than the wavelength, which requires sintering at low temperature with pressure to stop grain growth (Figure 28.4).

<!-- FIGURE 28.4 | figures/ch28/fig-28-4-transparent-ceramic-grain-size.png | plot | Real in-line transmission of polycrystalline ceramics: birefringent alumina becomes transparent only when grains are far smaller than the wavelength, while cubic spinel is limited only by reflection and porosity. | Content: x-axis mean grain size 0.1 to 100 um (log); y-axis real in-line transmission 0 to 90 % at 640 nm, 0.8 mm thickness. Curve: Al2O3 from the Apetz–Bruls equation (Delta n 0.008): 49 % at 0.3 um, 13.5 % at 1 um, 2 % at 2 um, near zero above 5 um; horizontal dashed line at 86 % = 1 - Rs for alumina. Spinel (n 1.72) horizontal band near 84–86 % independent of grain size; second spinel curve for 0.05 % porosity with 0.2 um pores falling to about 30 %. Inset photos-style icons: text read through 0.3 um alumina (clear) and 20 um alumina (translucent). -->

Transparent polycrystalline ceramics serve as armour windows for vehicles and aircraft (spinel and AlON, three to four times as weight-efficient as laminated glass), infrared domes and windows (spinel, ZnS, sapphire), laser gain media (Nd:YAG and Yb:YAG ceramics, which can be made larger and more heavily doped than single crystals), scintillators for medical CT, and envelopes for metal-halide lamps.

**Glass-ceramics** exploit the same physics from the other side. Controlled nucleation (Chapter 9) crystallizes a glass into a dense array of crystals tens of nanometres across, too small to scatter. If the crystal is a near-zero-expansion phase such as β-quartz solid solution, the result — the material of induction-hob cooktops and of telescope mirror blanks such as Zerodur — is transparent, strong and immune to thermal shock.

### Polymers

Amorphous polymers (PMMA, polycarbonate, polystyrene, cyclic olefin copolymers) are intrinsically transparent, with in-line transmission of 89–92 %, limited by surface reflection. They replace glass in vehicle lamps, glazing, lenses, medical devices and optical discs. **Semicrystalline** polymers (polyethylene, polypropylene, nylon, PTFE) are usually translucent or opaque, because crystalline lamellae and spherulites (Chapter 20), with an index higher than the amorphous regions by 0.02–0.05, form scattering structures several micrometres across. Three routes restore clarity: suppress crystallinity (quenching thin PET film, or copolymerization); make the crystals small, by adding **nucleating clarifiers** to polypropylene so that thousands of times more spherulites form, each too small to scatter (clarified PP food containers and syringes); or orient the crystals by stretching, as in biaxially oriented PET bottles and BOPP film. In fibre-reinforced polymers, a resin whose index matches that of the glass fibres can produce translucent panels. **Haze** — the fraction of transmitted light scattered by more than 2.5° — is the standard quality measure for films and sheets, along with yellowing from UV degradation, which absorbs the blue end of the spectrum (Chapter 36).

---

## 28.5 Luminescence and phosphors; LEDs and lasers as material systems

### Luminescence

**Luminescence** is the emission of light by a material after it has been excited by something other than heat: photons (photoluminescence), electrons (cathodoluminescence), an electric current (electroluminescence), X-rays or gamma rays (scintillation), or a chemical reaction. Because some energy is lost to lattice vibrations before emission, the emitted light has a longer wavelength than the exciting light — the **Stokes shift**. Emission that stops within microseconds of excitation is fluorescence; long-lived emission (milliseconds to hours) is phosphorescence.

Most practical luminescent materials are **phosphors**: a host crystal (oxide, nitride, sulfide, fluoride) doped with an activator ion whose energy levels produce the emission. Rare-earth ions dominate. **Eu$^{3+}$** and **Tb$^{3+}$** emit narrow lines (red at 611 nm and green at 545 nm) from shielded 4f levels, almost independent of the host. **Ce$^{3+}$** and **Eu$^{2+}$** emit broad bands from 5d→4f transitions whose energy depends strongly on the host's crystal field and covalency: the same Ce$^{3+}$ emits in the ultraviolet in a fluoride but yellow in Y$_3$Al$_5$O$_{12}$ (YAG:Ce), and Eu$^{2+}$ emits red in nitride hosts such as CaAlSiN$_3$. Phosphor design is crystal chemistry: choosing the site symmetry, bond covalency and stiffness of the host to place emission at the wanted wavelength and to suppress thermal quenching. Persistent phosphors such as SrAl$_2$O$_4$:Eu,Dy store energy in traps and glow for hours in emergency signage. **Scintillators** convert ionizing radiation to visible light for medical imaging and security scanning: lutetium–yttrium oxyorthosilicate (LYSO:Ce, about 30 000 photons per MeV with a 40 ns decay) in PET scanners, CsI:Tl in X-ray detectors, and transparent ceramic garnets and oxysulfides in CT.

### LEDs

A **light-emitting diode** is a p–n junction (Chapter 26) in a direct-gap semiconductor. Forward bias injects electrons and holes into a thin active region, where they recombine radiatively and emit photons of energy close to the band gap. Each element of the device is a materials choice:

- **The active layer** sets the colour. InGaN quantum wells in GaN emit violet to green (405–530 nm) as indium content rises; AlGaInP lattice-matched to GaAs emits red to amber (590–650 nm); AlGaN reaches the ultraviolet (to 210 nm) for disinfection. Between them lies the "green gap", where neither system is efficient: high-indium InGaN suffers strain, phase separation and strong polarization fields, and AlGaInP becomes indirect.
- **Heterostructure barriers** confine carriers in the wells (Chapter 26), raising the radiative rate.
- **Defects** compete through non-radiative SRH recombination. That GaN LEDs work at dislocation densities of $10^8$ cm$^{-2}$ is due to carrier localization in indium-rich regions.
- **Light extraction** is limited by total internal reflection. In a semiconductor with $n=2.5$, the critical angle is $\theta_c=\arcsin(1/2.5)=23.6$°, and only the fraction $(1-\cos\theta_c)/2=4.2$ % of isotropically emitted light can escape through the top surface. Roughened or patterned surfaces, patterned sapphire substrates, and encapsulation in high-index silicones raise extraction to 80 % or more.

**White LEDs** combine a blue InGaN chip (about 450 nm) with a YAG:Ce phosphor that absorbs part of the blue and emits broadband yellow; adding a red nitride phosphor raises colour rendering for warm-white lighting (Figure 28.5). Today's best white LEDs exceed 200 lumens per watt, more than ten times an incandescent lamp, and solid-state lighting has cut global lighting electricity substantially. The phosphor's thermal quenching, the degradation of silicone encapsulants and the efficiency **droop** at high current (partly Auger recombination) are the materials limits on lifetime and brightness.

<!-- FIGURE 28.5 | figures/ch28/fig-28-5-white-led-spectrum.png | plot | A phosphor-converted white LED: a blue InGaN chip plus yellow (and optionally red) phosphor emission. | Content: left panel schematic cross-section: sapphire or patterned substrate, n-GaN, InGaN/GaN multiple quantum wells, p-GaN, contacts; phosphor-in-silicone layer on top; arrows for blue photons partly converted to yellow. Right panel: x-axis wavelength 380 to 780 nm; y-axis relative spectral power 0 to 1. Narrow blue peak at 450 nm (FWHM about 20 nm); broad YAG:Ce band peaking near 555 nm (FWHM about 110 nm); optional dashed red nitride phosphor band peaking near 630 nm for warm white. Overlay the photopic eye-sensitivity curve V(lambda) peaking at 555 nm as a thin grey line. -->

### Lasers

A laser amplifies light by **stimulated emission** in a medium with a **population inversion** — more atoms in the upper level of a transition than in the lower — inside an optical resonator. The gain medium is a materials system in which the host and the dopant are chosen together:

| Laser | Gain material | Wavelength | Uses |
|---|---|---|---|
| Nd:YAG | Nd$^{3+}$ in Y$_3$Al$_5$O$_{12}$ crystal or ceramic | 1064 nm | Marking, drilling, medical, range-finding |
| Yb fibre | Yb$^{3+}$ in silica fibre core | 1030–1080 nm | Industrial cutting and welding (to tens of kW), additive manufacturing |
| Er fibre amplifier | Er$^{3+}$ in silica fibre | 1530–1565 nm | Telecommunications amplification |
| Ti:sapphire | Ti$^{3+}$ in Al$_2$O$_3$ | 650–1100 nm (tunable) | Ultrafast pulses, research |
| CO$_2$ | Gas molecule | 10.6 µm | Cutting non-metals, older metal cutting |
| Semiconductor diode | InGaAs, AlGaAs, InGaN quantum wells | 375 nm–2 µm | Pumps for solid-state lasers, data links, Blu-ray, lidar |

*Table 28.3 — Representative laser materials.*

In solid-state lasers the host must be transparent, optically homogeneous, thermally conductive (to remove waste heat without thermal lensing or fracture) and able to accept the dopant ion on a suitable site; YAG and sapphire excel because they are hard, conductive and isotropic or well-characterized. In fibre lasers, the long thin geometry dissipates heat so well that a single fibre delivers kilowatts, which is why Yb fibre lasers now dominate laser welding, cutting and powder-bed fusion (Chapters 39–40). Diode lasers add a resonator to the LED structure: cleaved crystal facets serve as mirrors, and a double heterostructure confines both carriers (lower gap) and light (higher index) in the active layer. At high power, facets fail by catastrophic optical damage, a materials-degradation problem solved by facet passivation and non-absorbing mirror regions.

---

## 28.6 Optical fibres and waveguides

### Guiding by total internal reflection

An optical fibre has a **core** of slightly higher index than its **cladding**; light launched within the acceptance cone is totally reflected at the boundary and guided. The **numerical aperture**

$$
\mathrm{NA}=\sqrt{n_1^2-n_2^2}=\sin\theta_{\max}
$$

measures the acceptance cone. When the core is small enough, only one guided mode propagates; the condition is that the normalized frequency

$$
V=\frac{2\pi a}{\lambda}\,\mathrm{NA}<2.405
$$

where $a$ is the core radius. Single-mode fibres avoid the spreading of pulses between modes and carry the world's long-distance and data-centre traffic; multimode fibres (core 50–62.5 µm) serve short links and are easier to couple to cheap sources.

> **Status of the principle: Single-mode condition $V<2.405$**
> *Derived.* It follows from solving Maxwell's equations for a step-index cylindrical guide in the weakly guiding approximation ($n_1-n_2\ll n_1$); 2.405 is the first zero of the Bessel function $J_0$.

**Worked example — designing a single-mode fibre.** A germania-doped core of $n_1=1.4500$ in a silica cladding of $n_2=1.4447$ gives

$$
\mathrm{NA}=\sqrt{1.4500^2-1.4447^2}=0.124
$$

an acceptance half-angle of 7.1°. For single-mode operation at 1.31 µm, $a<2.405\lambda/(2\pi\,\mathrm{NA})=2.405(1.31)/(2\pi\times0.124)=4.05$ µm. A core radius of 4.1 µm gives $V=2.44$ at 1.31 µm (just multimode) and $V=2.06$ at 1.55 µm — so standard telecom fibre, with a core diameter of about 8–9 µm, is single-mode at 1.55 µm and only marginally above cutoff at 1.31 µm. The index step of 0.0053 is produced by about 4 mol% GeO$_2$ in the core, deposited by **modified chemical vapour deposition** (MCVD) or outside vapour deposition: SiCl$_4$ and GeCl$_4$ are oxidized to soot inside or around a silica tube, sintered to a transparent preform, and drawn to a 125 µm fibre at about 2000 °C. The vapour route is essential because the chlorides can be distilled to a purity that no melted glass could reach.

### Loss: the materials limits

Fibre attenuation is quoted in decibels per kilometre; a loss of $\alpha$ dB/km over length $L$ leaves a fraction $10^{-\alpha L/10}$ of the power. Silica fibre loss has three materials origins (Figure 28.6):

- **Rayleigh scattering** from frozen-in density and composition fluctuations of the glass, proportional to $\lambda^{-4}$ and to the fictive temperature at which the glass structure froze (Chapter 17). It dominates in the near infrared.
- **Infrared absorption** by Si–O vibrational overtones, rising steeply beyond 1.6 µm.
- **Impurity absorption**, above all by OH groups (overtone at 1.38 µm) and transition metals. A transition-metal content of 1 ppb or an OH content below 1 ppm is required, achieved through vapour-phase chemistry and dehydration with chlorine.

Between Rayleigh scattering and infrared absorption lies a minimum near 1.55 µm, about 0.17–0.2 dB/km in standard fibre and 0.14 dB/km in pure-silica-core fibres — so 100 km of fibre transmits about 1 % of the input, recoverable with an erbium-doped fibre amplifier. At 0.85 µm, Rayleigh scattering is $(1550/850)^4=11$ times stronger, giving losses of about 2 dB/km, and the same 100 km would transmit $10^{-20}$ of the light. This is the answer to the fourth opening question.

<!-- FIGURE 28.6 | figures/ch28/fig-28-6-fibre-attenuation.png | plot | Attenuation of silica optical fibre: Rayleigh scattering and infrared absorption bound a low-loss window at 1.3–1.6 um. | Content: x-axis wavelength 0.7 to 1.8 um; y-axis attenuation 0.1 to 10 dB/km (log). Curves: total measured loss of standard single-mode fibre (about 2.2 at 0.85, 0.33 at 1.31, 0.19 at 1.55 um, low-water-peak version without the OH peak; older fibre with OH peak about 1 dB/km at 1.38 um as a dashed variant); Rayleigh scattering component A/lambda^4 with A about 0.85 dB km^-1 um^4; infrared absorption tail rising from 1.6 um; UV absorption tail at short wavelength. Shade telecom bands O (1260–1360), C (1530–1565), L (1565–1625). Mark 0.14 dB/km record pure-silica-core fibre at 1.56 um. -->

### Other fibres and waveguides

**Polymer optical fibre** (PMMA core, fluoropolymer cladding) has high loss (about 150–200 dB/km at 650 nm, from C–H vibrational overtones) but large cores, flexibility and cheap connectors, and serves in-vehicle networks, lighting and short links. **Fluoride and chalcogenide glass fibres** transmit the mid-infrared for spectroscopy and laser delivery. **Fibre sensors** turn the fibre itself into a strain gauge or thermometer: fibre Bragg gratings, written by ultraviolet light into a germanosilicate core, reflect a narrow band whose wavelength shifts with strain (about 1.2 pm per microstrain at 1.55 µm) and temperature, and are embedded in bridges, wind-turbine blades, composite aircraft structures, pipelines and oil wells, where they are immune to electromagnetic interference. Distributed sensing reads Rayleigh, Raman or Brillouin backscatter along tens of kilometres of fibre to locate leaks, fires or ground movement.

On chips, **integrated waveguides** guide light through a high-index core patterned on a low-index substrate: silicon on SiO$_2$ (silicon photonics, an index contrast of 3.48/1.44 that allows bends of a few micrometres), silicon nitride (lower loss, visible-to-infrared), and thin-film lithium niobate for modulators (Section 28.7). Silicon photonic transceivers carry the optical links of data centres.

---

## 28.7 Nonlinear and electro-optic materials

### Nonlinear optics

At low intensity, polarization is proportional to the optical field. At laser intensities, the field approaches the inner-atomic fields that bind electrons, and higher-order terms appear:

$$
P=\varepsilon_0\left(\chi^{(1)}E+\chi^{(2)}E^2+\chi^{(3)}E^3+\dots\right)
$$

The **second-order** susceptibility $\chi^{(2)}$ mixes frequencies: two photons at $\omega$ combine to one at $2\omega$ (**second-harmonic generation**), as in the green laser pointer, where 1064 nm light from Nd:YVO$_4$ is doubled to 532 nm in a KTP crystal. Sum- and difference-frequency generation and optical parametric oscillation extend the same idea to tunable sources. Symmetry decides which materials qualify: $\chi^{(2)}$ is a third-rank tensor like the piezoelectric coefficient, and vanishes in any centrosymmetric material (Chapter 25). Glass, silicon and cubic centrosymmetric crystals have no bulk second-order response; the useful crystals are non-centrosymmetric — LiNbO$_3$ ($d_{33}\approx25$ pm/V), KTiOPO$_4$ (KTP, about 15), β-BaB$_2$O$_4$ (BBO, about 2, transparent into the deep ultraviolet), LiB$_3$O$_5$ (LBO, about 1, with a high damage threshold).

Efficient conversion requires **phase matching**: the fundamental and harmonic must travel at the same phase velocity, which dispersion prevents. Birefringent crystals solve this by using different polarizations whose indices cross at a particular angle. A materials-processing alternative is **quasi-phase matching**: the ferroelectric domains of LiNbO$_3$ are periodically reversed by applying a high field through patterned electrodes (periodically poled lithium niobate, PPLN), so the sign of $\chi^{(2)}$ flips every coherence length — domain engineering of the kind described in Chapter 25, used here for light.

The **third-order** susceptibility $\chi^{(3)}$ exists in all materials, including glass. It makes the refractive index depend on intensity, $n=n_0+n_2I$ (the **optical Kerr effect**); for silica $n_2\approx2.6\times10^{-20}$ m²/W, small but significant over the long lengths and small cores of fibres, where it causes self-phase modulation and four-wave mixing that limit high-capacity links and also generate supercontinuum light sources.

> **Status of the principle: Power-series expansion of the polarization**
> *Approximate.* It holds when the optical field is much smaller than the atomic fields, so successive terms shrink rapidly. It breaks down at intensities near the damage threshold, where multiphoton ionization and plasma formation occur — the regime exploited in femtosecond laser machining.

### Electro-optic materials

A DC or low-frequency field can also change the refractive index. In non-centrosymmetric crystals the change is linear in field — the **Pockels effect**:

$$
\Delta n=-\tfrac12n^3rE
$$

where $r$ is the electro-optic coefficient (pm/V). In centrosymmetric materials only the quadratic **Kerr electro-optic effect** remains. The index change shifts the phase of light travelling through the material; placed in one or both arms of a Mach–Zehnder interferometer, it switches light on and off. The voltage needed to shift the phase by $\pi$ is the **half-wave voltage**

$$
V_\pi=\frac{\lambda g}{n^3r\Gamma L}
$$

for electrodes with gap $g$, length $L$ and overlap factor $\Gamma$ between the electric and optical fields.

**Worked example — a lithium niobate modulator.** For light at 1.55 µm polarized along the c-axis of LiNbO$_3$ ($n_e=2.138$, $r_{33}=30.8$ pm/V), with an electrode gap of 15 µm, a length of 2 cm and an overlap of 0.5:

$$
V_\pi=\frac{(1.55\times10^{-6})(15\times10^{-6})}{(2.138)^3(30.8\times10^{-12})(0.5)(0.02)}=7.7\ \mathrm V
$$

Driving both arms in push-pull halves this to about 3.9 V, typical of the bulk-crystal modulators that carried long-haul telecom traffic for decades. Because $V_\pi\propto g/L$, a lower voltage requires either longer devices or narrower gaps; thin-film lithium niobate on insulator, which confines light in a waveguide less than a micrometre across, allows gaps of a few micrometres and modulators driven directly by CMOS-level voltages at over 100 GHz. Alternatives include electro-optic polymers ($r_{33}$ above 100 pm/V, but with long-term stability concerns), BaTiO$_3$ films on silicon ($r$ of several hundred pm/V), and silicon itself, which has no Pockels effect and modulates instead by changing carrier density (the free-carrier plasma effect). Liquid crystals, whose large birefringence is reoriented by modest fields, make the slow but cheap electro-optic devices of displays (Chapter 29).

---

## 28.8 Photonic crystals and metamaterials

### Photonic crystals

A material whose refractive index varies periodically on the scale of the wavelength scatters light coherently, just as a crystal lattice diffracts X-rays (Chapter 4). Waves reflected from successive periods add in phase at the Bragg condition, and over a range of frequencies light cannot propagate at all: a **photonic band gap**, the optical analogue of the electronic band gap of Chapter 26.

The one-dimensional case is the **distributed Bragg reflector** (DBR): alternating quarter-wave layers of high and low index. For TiO$_2$ ($n_H=2.3$) and SiO$_2$ ($n_L=1.45$) on glass, designed for 1064 nm, the layers are 116 nm and 183 nm thick; ten pairs reflect 99.99 % at the design wavelength, over a stop band about 29 % of the centre frequency wide. Such dielectric mirrors absorb far less than metal mirrors and are used in high-power laser optics, in the cavity mirrors of **vertical-cavity surface-emitting lasers** (VCSELs) — epitaxial GaAs/AlGaAs DBRs grown directly on the laser, used for face recognition in phones and short optical links — and in the heat-reflecting coatings of halogen lamps and solar-control glazing.

Two- and three-dimensional photonic crystals confine light more completely. **Photonic-crystal fibres**, drawn from stacks of silica capillaries, guide light by a periodic array of air holes; hollow-core versions guide light in air, with lower nonlinearity and latency than solid fibres. Three-dimensional photonic crystals can be made by self-assembly of monodisperse colloidal spheres (synthetic opals, Chapter 29), by lithography, or by direct laser writing. Nature uses them extensively: the iridescence of opal gemstones (ordered silica spheres), butterfly wings, beetle shells and peacock feathers is **structural colour**, which does not fade because no dye is involved, and is being developed for paints and inks without pigments.

### Metamaterials and metasurfaces

A **metamaterial** is an artificial structure whose unit cells are smaller than the wavelength, so that light sees an effective homogeneous medium — but one whose permittivity and permeability are set by the geometry of the cells rather than by their atoms. Arrays of split-ring resonators and wires can give a negative effective permeability and permittivity together, and therefore a **negative refractive index**, demonstrated at microwave frequencies in 2000. Proposed applications include sub-wavelength "superlenses" and electromagnetic cloaks; both work only over narrow bands and are limited by the losses of metallic resonators, especially at optical frequencies.

More practical are **metasurfaces**: single layers of sub-wavelength nanostructures (TiO$_2$ or amorphous silicon pillars, gold antennas) that impose a designed phase shift on transmitted light at each point. A metasurface can act as a flat lens, polarizer, hologram or beam deflector a fraction of a micrometre thick, and metalenses are entering phone cameras and sensors. **Plasmonics** uses the collective electron oscillations of metal nanoparticles: gold nanoparticles of 20–50 nm absorb green light, giving the red of medieval stained glass, and are used in lateral-flow medical tests and as photothermal agents in cancer therapy (Chapter 31). Engineered emitters also manage heat: **radiative-cooling** films combine high solar reflectance with strong thermal emission in the 8–13 µm atmospheric window, cooling buildings below ambient temperature in direct sunlight without power — a photonic material for energy efficiency.

> **Boundary.** Maxwell's equations, quantum theory of absorption and emission, and laser physics belong to the Engineering Physics book; optoelectronic devices (photodetectors, solar cells, modulators) are treated in the *Materials Core (EEE)* book, Chapter 14.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How does the electronic polarization of Section 28.2 relate to dielectric behaviour at lower frequencies, and why is $\chi^{(2)}$ governed by the same symmetry as piezoelectricity? | Chapter 25 |
| How do band structure, doping and heterostructures make LED and laser active layers? | Chapter 26 |
| How do liquid crystals switch light in displays, and how do colloids self-assemble into photonic structures? | Chapter 29 |
| How does quantum confinement tune the colour of quantum dots, and what are 2D optical materials? | Chapter 30 |
| How are photovoltaic absorbers chosen, and how do coatings and textures trap light in solar cells? | Chapter 32 |
| How do UV light and weathering yellow polymers and degrade pigments? | Chapter 36 |
| How are lasers used in welding, cutting and additive manufacturing? | Chapters 39 and 40 |
| How are optical coatings and thin films deposited? | Chapter 41 |
| How are optical constants, luminescence and Raman spectra measured? | Chapters 42 and 43 |
| How are optical materials and glasses selected for a given application and cost? | Chapter 48 |

**Next:** Chapter 29 opens Part VII with smart and soft materials — shape-memory alloys, electroactive polymers, gels, colloids and liquid crystals — whose properties change on command.
