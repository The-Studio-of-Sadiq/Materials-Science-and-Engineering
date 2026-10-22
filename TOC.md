# Materials Science and Engineering — Master Syllabus

**Purpose:** The whole discipline in one book. Why materials have the structures they have, how thermodynamics and kinetics set those structures, how structure produces properties, how processing controls structure, and how materials are characterized, modelled, selected and kept in service.

Structure: 11 Parts · 59 Chapters. Sources: `Parts/PART N.md` (part openers) and `Chapters/CHAPTER N.md`.

The backbone is **structure → thermodynamics → kinetics → properties → materials classes → processing → characterization → computation and design**. Parts VI and VII treat electrical, dielectric, magnetic, superconducting, semiconductor and photonic materials at the depth an electrical and electronic engineer needs; every other part serves the whole discipline.

---

## Part I — Structure of Materials

### Chapter 1. The Materials Discipline
- Materials science and materials engineering; history of materials ages
- The structure–processing–property–performance tetrahedron
- Length and time scales from electrons to structures
- Material classes and their property ranges: metals, ceramics, glasses, polymers, composites, semiconductors, biomaterials
- Bonding as the origin of property classes (summary; chemistry in depth elsewhere)
- Isotropy, anisotropy, homogeneity
- Property charts and the logic of selection
- Materials and society: economics, criticality, sustainability

### Chapter 2. Crystal Structures and Non-Crystalline Solids
- Lattices, bases, unit cells; coordination and packing
- Metallic structures: FCC, BCC, HCP, stacking sequences
- Ionic and covalent structures: rock salt, CsCl, fluorite, zincblende, wurtzite, perovskite, spinel, corundum; Pauling's rules
- Silicate structures and polymorphism
- Directions, planes, Miller and Miller–Bravais indices; linear and planar densities
- Polycrystals, texture, grain size
- Amorphous solids and glasses; radial distribution functions
- Polymer chain packing and crystallinity (preview)
- Liquid crystals and quasicrystals (preview)

### Chapter 3. Symmetry and Space Groups
- Symmetry operations: rotation, reflection, inversion, rotoinversion, screw axes, glide planes
- The 32 point groups and 7 crystal systems
- The 14 Bravais lattices and why only these exist
- The 230 space groups; reading the International Tables
- Stereographic projection and pole figures
- Symmetry of real structures
- Superlattices, ordering, antiphase boundaries
- Quasicrystals and incommensurate structures

### Chapter 4. Reciprocal Space, Diffraction and Tensor Properties
- The reciprocal lattice and Brillouin zones
- Bragg's law, Laue condition, Ewald sphere
- Structure factor and systematic absences
- Intensities: atomic scattering factor, Debye–Waller factor, multiplicity, Lorentz–polarization
- Peak broadening: size and strain (Scherrer, Williamson–Hall)
- Neumann's principle
- Tensor properties: rank 2 (conductivity, permittivity, thermal expansion), rank 3 (piezoelectricity), rank 4 (elasticity)
- Why cubic crystals are isotropic in conduction but anisotropic in elasticity

### Chapter 5. Defects and Microstructure
- Point defects: vacancies, interstitials, substitutional solutes; equilibrium concentration
- Defects in ionic crystals: Schottky, Frenkel, Kröger–Vink notation, defect chemistry and non-stoichiometry
- Line defects: edge, screw and mixed dislocations, Burgers vector (introduction)
- Planar defects: grain boundaries (low- and high-angle, CSL), twin boundaries, stacking faults, phase boundaries (coherent, semicoherent, incoherent)
- Volume defects: pores, inclusions, precipitates
- Quantitative microstructure: stereology, grain size, volume fraction
- How defects control properties: an overview

## Part II — Thermodynamics and Kinetics

### Chapter 6. Thermodynamics of Materials
- Gibbs energy, chemical potential and equilibrium in condensed systems (recap)
- Solutions: ideal, regular and real; activity; Gibbs–Duhem
- Free-energy–composition curves and the common-tangent construction
- Miscibility gaps and spinodals
- Sublattice and compound-energy models; ordering
- Surfaces and interfaces: surface energy, Gibbs–Thomson effect, wetting
- Thermodynamics of point defects
- Ellingham diagrams for oxidation and reduction

*Boundary:* the laws of thermodynamics and reaction thermodynamics belong to Advanced Chemistry; this chapter applies them to solids and solutions.

### Chapter 7. Phase Diagrams
- Gibbs phase rule
- Unary diagrams (water, iron, carbon, silica)
- Binary isomorphous, eutectic, peritectic, monotectic, eutectoid, intermediate compounds
- Lever rule; microstructure development on cooling
- The Fe–C (Fe–Fe₃C) diagram
- Ceramic phase diagrams (Al₂O₃–SiO₂, ZrO₂–Y₂O₃, MgO–Al₂O₃)
- Ternary diagrams: Gibbs triangle, isothermal and vertical sections, liquidus projections
- CALPHAD: computed phase diagrams
- Reading real diagrams for alloy and process design

### Chapter 8. Diffusion in Solids
- Fick's laws and their solutions: thin film, error function, separation of variables
- Atomic mechanisms: vacancy, interstitial, interstitialcy
- Random walk and the Arrhenius law derived
- Self-diffusion, interdiffusion, Kirkendall effect, Darken equations
- Short-circuit paths: grain boundaries, dislocations, surfaces (Harrison A/B/C)
- Diffusion in ionic solids: Nernst–Einstein, defect-controlled diffusion
- Diffusion in polymers and glasses
- Uphill diffusion and chemical-potential gradients
- Engineering applications: carburizing, doping, homogenization

### Chapter 9. Nucleation, Growth and Solidification
- Driving force for transformation
- Homogeneous nucleation: critical radius, barrier, rate
- Heterogeneous nucleation: wetting angle, inoculation
- Interface-controlled and diffusion-controlled growth
- Overall transformation kinetics: JMAK equation, TTT construction
- Solidification: constitutional supercooling, planar/cellular/dendritic growth
- Segregation: Scheil equation, zone refining
- Eutectic and peritectic solidification; casting microstructures
- Rapid solidification and metallic glasses

### Chapter 10. Phase Transformations in Solids
- Classification: diffusional, diffusionless, displacive, order–disorder
- Precipitation: GP zones, coherency, precipitation sequences (Al–Cu), age hardening
- Coarsening: Ostwald ripening, LSW theory
- Spinodal decomposition: Cahn–Hilliard picture
- Pearlite and bainite in steels
- Martensitic transformations: crystallography, habit planes, shape memory
- Recovery, recrystallization and grain growth; Zener pinning; abnormal grain growth
- Massive and discontinuous transformations
- Transformation diagrams (TTT, CCT) in practice

## Part III — Mechanical Behaviour

### Chapter 11. Elasticity and Mechanical Testing
- Stress, strain and their tensors
- Linear elasticity: Hooke's law, elastic constants, anisotropic elasticity
- Origins of elastic moduli in bonding
- Rubber and entropic elasticity (preview)
- The tensile test: yield, UTS, ductility, true stress–strain
- Hardness tests (Brinell, Vickers, Rockwell, nanoindentation)
- Impact and toughness testing
- Bend, compression and shear testing
- Statistical nature of strength

### Chapter 12. Dislocation Theory
- Theoretical shear strength versus real strength
- Stress and strain fields of edge and screw dislocations; line energy and line tension
- Forces on dislocations: Peach–Koehler; glide and climb
- Interactions: junctions, jogs, kinks, forest hardening
- Multiplication: Frank–Read and other sources
- Partial dislocations, stacking faults, stacking-fault energy
- Dislocations in FCC, BCC (Peierls stress), HCP and ceramics
- Observing dislocations

### Chapter 13. Plasticity and Strengthening Mechanisms
- Slip systems; Schmid's law; critical resolved shear stress
- Single-crystal stress–strain curves: stages I–III
- Polycrystal plasticity: Taylor factor, von Mises criterion
- Yield criteria: Tresca, von Mises
- Work hardening: Taylor equation
- Solid-solution strengthening
- Grain-boundary strengthening: Hall–Petch from pile-ups
- Precipitate strengthening: cutting versus Orowan bypass
- Twinning; superplasticity
- Combining mechanisms in real alloys

### Chapter 14. Creep, Viscoelasticity and Fracture
- Creep mechanisms: Nabarro–Herring, Coble, dislocation creep, grain-boundary sliding
- Power-law creep; Larson–Miller parameter
- Deformation-mechanism maps
- Viscoelasticity: Maxwell, Kelvin–Voigt, standard linear solid, relaxation spectra, time–temperature superposition
- Linear-elastic fracture mechanics: Griffith, Irwin, crack-tip fields, K and G
- Elastic–plastic fracture: J-integral, CTOD
- Ductile–brittle transition
- Fatigue: S–N, strain–life, Paris law, crack closure
- Toughening of ceramics: transformation toughening, bridging, R-curves
- Weibull statistics

## Part IV — Metals, Ceramics and Construction Materials

### Chapter 15. Physical Metallurgy of Steels and Cast Irons
- Iron and its allotropes; the Fe–C diagram revisited
- Plain-carbon steels: microstructure versus carbon content
- Heat treatment: annealing, normalizing, quenching, tempering
- Hardenability: Jominy test, alloying effects, CCT diagrams
- Alloy steels: HSLA, tool steels, maraging
- Stainless steels: ferritic, austenitic, martensitic, duplex; Schaeffler diagram
- Advanced high-strength steels: dual-phase, TRIP, TWIP
- Cast irons: grey, ductile, white, malleable
- Surface hardening: carburizing, nitriding, induction

### Chapter 16. Non-Ferrous Alloys
- Aluminium alloys: wrought and cast series, tempers, age hardening
- Copper alloys: brasses, bronzes, high-conductivity alloys
- Titanium alloys: α, α+β, β; processing and applications
- Nickel-base superalloys: γ/γ′, single crystals, coatings
- Magnesium and zinc alloys
- Refractory and precious metals
- Intermetallics and high-entropy alloys
- Selecting non-ferrous alloys

### Chapter 17. Ceramics and Glasses
- Structure and bonding of engineering ceramics
- Traditional versus technical ceramics: alumina, zirconia, SiC, Si₃N₄
- Ceramic powder processing: synthesis, forming, sintering (solid-state and liquid-phase)
- Mechanical behaviour of ceramics: flaws, Weibull, toughening (recap of Ch 14)
- Glass formation: Zachariasen rules, network formers and modifiers
- Glass properties: viscosity–temperature (VFT), annealing, tempering, chemical strengthening
- Glass-ceramics
- Refractories
- Functional ceramics (pointer to Part VI)

### Chapter 18. Cement, Concrete and Construction Materials
- Portland cement: clinker phases, hydration chemistry, C–S–H
- Concrete: mix design, water–cement ratio, strength development, curing
- Durability: carbonation, chloride attack, alkali–silica reaction, freeze–thaw
- Reinforced and prestressed concrete as a composite
- Structural steels and their specifications
- Timber: wood structure, anisotropy, moisture, engineered wood
- Asphalt and bituminous materials
- Masonry, brick and stone
- Low-carbon cements and construction sustainability

## Part V — Polymers and Composites

### Chapter 19. Polymer Synthesis and Molecular Structure
- Monomers, repeat units, nomenclature
- Step-growth polymerization; Carothers equation
- Chain-growth: free-radical, ionic, coordination (Ziegler–Natta, metallocene), ring-opening
- Molecular weight: averages, dispersity, measurement
- Copolymers: random, alternating, block, graft
- Tacticity, branching, crosslinking, networks
- Commodity, engineering and high-performance polymers

### Chapter 20. Polymer Physics and Morphology
- Chain conformations: freely jointed chain, Kuhn length, end-to-end distance
- Rubber elasticity derived from entropy
- Polymer solutions: Flory–Huggins theory, theta conditions
- Blends and miscibility; block-copolymer microphase separation
- Crystallization: lamellae, chain folding, spherulites, degree of crystallinity
- The glass transition: free-volume theory, WLF equation, molecular factors controlling Tg
- Liquid-crystalline polymers

### Chapter 21. Polymer Rheology, Mechanics and Processing
- Melt rheology: shear thinning, entanglement, reptation, the M^3.4 law
- Viscoelastic mechanical behaviour in practice
- Yielding, crazing, environmental stress cracking
- Processing: extrusion, injection moulding, blow moulding, thermoforming, fibre spinning, film blowing
- Additives: plasticizers, fillers, stabilizers, flame retardants
- Degradation: UV, thermo-oxidative, hydrolytic
- Elastomers and their vulcanization
- Recycling and biodegradable polymers

### Chapter 22. Composite Micromechanics and Lamina Behaviour
- Why composites: classes and architectures
- Fibres (glass, carbon, aramid, natural) and matrices (polymer, metal, ceramic)
- Rule of mixtures; Halpin–Tsai
- Particulate composites; Eshelby inclusions (qualitative)
- Short-fibre composites: shear-lag, critical length
- The orthotropic lamina: stiffness and compliance, reduced stiffness Q
- Off-axis lamina: transformation, Q-bar
- Thermal and hygral expansion of laminae

### Chapter 23. Laminate Theory, Failure and Composite Manufacturing
- Classical laminate theory: ABD matrix, coupling, symmetric and balanced layups
- Failure criteria: maximum stress, Tsai–Hill, Tsai–Wu, Puck; progressive ply failure
- Interlaminar stresses, free-edge effects, delamination
- Impact damage and compression after impact
- Sandwich structures
- Manufacturing: hand layup, prepreg/autoclave, RTM, filament winding, pultrusion, automated fibre placement
- Metal- and ceramic-matrix composites

## Part VI — Thermal, Electrical, Dielectric and Magnetic Materials

### Chapter 24. Thermal Properties
- Phonons and heat capacity (Einstein, Debye)
- Thermal expansion and the anharmonic potential
- Thermal conductivity: phonon and electron contributions
- Thermal diffusivity and transient heat flow
- Thermal stresses and thermal shock
- Thermal barrier coatings and insulation
- Materials for thermal management

### Chapter 25. Electrical Conduction in Materials
- Conductivity and resistivity
- Mobility and scattering as material properties
- Temperature coefficients of resistance
- Conductivity in metals and alloys
- Contact resistance
- Thin-film conductors
- Conductive composites
- Electrical conductivity versus thermal conductivity
- Material selection for wires, contacts, interconnects, and electrodes
- Ionic conduction and solid electrolytes

### Chapter 26. Dielectric and Insulating Materials
- Permittivity and dielectric polarization
- Dielectric loss and loss tangent
- Frequency and temperature dependence
- Dielectric strength
- Electrical breakdown mechanisms
- Volume and surface resistivity
- Tracking and partial discharge
- Moisture and contamination effects
- Polymer, ceramic, and composite insulators
- Insulation aging and degradation

### Chapter 27. Functional Dielectric Materials
- Ferroelectric materials
- Piezoelectric materials
- Pyroelectric materials
- Electrostrictive materials
- High-permittivity dielectrics
- Dielectric resonators
- Electro-optic materials
- Applications in capacitors, actuators, sensors, and RF systems

### Chapter 28. Magnetic Material Behaviour
- Magnetic susceptibility and permeability
- Diamagnetic and paramagnetic materials
- Ferromagnetism and ferrimagnetism
- Antiferromagnetism
- Magnetic domains
- Domain-wall motion
- Hysteresis
- Remanence and coercivity
- Saturation magnetization
- Temperature dependence of magnetic behavior

### Chapter 29. Soft and Hard Magnetic Materials
- Soft magnetic materials
- Hard magnetic materials
- Electrical steels
- Ferrites
- Amorphous and nanocrystalline magnetic alloys
- Permanent-magnet materials
- Magnetic losses
- Eddy-current suppression
- Magnetic shielding materials
- Material selection for transformers, motors, inductors, and sensors

### Chapter 30. Superconducting Materials
- Superconducting properties
- Critical temperature, field, and current
- Type I and Type II superconductors
- High-temperature superconductors
- Flux pinning
- Superconducting wires and tapes
- Material processing constraints
- Applications in magnets, power systems, and sensing

## Part VII — Semiconductor and Photonic Materials

### Chapter 31. Solid-State Foundations for Materials Engineering
- Electronic states in solids
- Energy-band formation
- Valence and conduction bands
- Band gaps
- Density of states
- Fermi level
- Effective mass
- Temperature dependence of carrier populations
- Direct and indirect band gaps

*Boundary:* material-level explanation only. Detailed quantum mechanics belongs in Engineering Physics; device operation belongs in Electronics & Computing.

### Chapter 32. Semiconductor Material Properties
- Intrinsic and extrinsic semiconductors
- Donors and acceptors
- Doping profiles
- Carrier concentration
- Carrier mobility
- Drift and diffusion
- Recombination and generation
- Minority-carrier lifetime
- Temperature dependence
- High-field transport
- Defects and impurities in semiconductors

### Chapter 33. Semiconductor Material Families
- Silicon and germanium
- III–V compound semiconductors
- Gallium arsenide and indium phosphide
- Silicon carbide
- Gallium nitride
- Other wide-bandgap semiconductors
- Amorphous silicon
- Organic semiconductors
- Two-dimensional materials
- Material comparison for power, RF, sensing, and optoelectronics

### Chapter 34. Semiconductor Interfaces and Thin Films
- Semiconductor heterostructures
- Band alignment
- Heterojunction interfaces
- Surface states
- Interface traps
- Thin-film properties
- Film stress and defects
- Grain boundaries in thin films
- Contact interfaces
- Material properties of gate dielectrics
- Interface reliability

### Chapter 35. Electronic and Optoelectronic Materials
- Light absorption and emission in materials
- Photoconductive materials
- Luminescent materials
- LED and laser semiconductor materials
- Photodetector materials
- Solar-cell absorber materials
- Optical and photonic materials
- Material properties for high-frequency electronics
- Sensor materials

*Boundary:* the materials mechanisms behind these devices belong here; circuit configurations and detailed device operation belong in Electronics & Computing.

### Chapter 36. Optical and Photonic Materials
- Interaction of light with matter: refraction, dispersion, absorption, scattering
- Refractive index and its origin; Sellmeier
- Colour in metals, insulators, semiconductors and pigments
- Transparency and opacity in ceramics and polymers
- Luminescence and phosphors; LEDs and lasers as material systems
- Optical fibres and waveguides
- Nonlinear and electro-optic materials
- Photonic crystals and metamaterials

## Part VIII — Advanced and Emerging Materials

### Chapter 37. Smart and Soft Materials
- Shape-memory alloys: martensite, superelasticity, NiTi
- Magnetostrictive and magnetic shape-memory materials
- Piezoelectric actuators and sensors (recap)
- Electroactive polymers
- Colloids and their stability (DLVO)
- Gels and hydrogels
- Liquid crystals: phases, order parameter, displays
- Self-assembly and soft-matter design

### Chapter 38. Nanomaterials and Two-Dimensional Materials
- Size effects: surface-to-volume, melting-point depression, quantum confinement
- Nanoparticles, nanowires, nanotubes, quantum dots
- Graphene and other 2D materials
- Nanocrystalline metals: strength, the inverse Hall–Petch regime
- Nanocomposites
- Synthesis: top-down and bottom-up
- Characterization and safety of nanomaterials

### Chapter 39. Biomaterials
- The host response: biocompatibility, protein adsorption, inflammation, foreign-body response
- Metallic biomaterials: Ti alloys, CoCr, stainless steel, corrosion in the body
- Ceramic biomaterials: alumina, zirconia, hydroxyapatite, bioactive glass
- Polymeric biomaterials; biodegradable polymers (PLA, PGA, PCL)
- Hydrogels, tissue scaffolds, tissue engineering
- Implants: hips, knees, dental, cardiovascular stents
- Drug delivery systems
- Sterilization, testing and regulation

### Chapter 40. Materials for Energy
- Photovoltaic absorbers
- Battery materials: intercalation electrodes, electrolytes, solid-state
- Fuel-cell and electrolyser materials
- Hydrogen storage materials and hydrogen embrittlement
- Thermoelectric materials
- Supercapacitor materials
- Nuclear fuels and cladding (pointer to Ch 41)
- Critical raw materials and scalability

### Chapter 41. Materials for Extreme Environments
- High-temperature materials: superalloys, refractory alloys, ceramics, CMCs, thermal barrier coatings
- High-temperature oxidation and hot corrosion (pointer to Ch 42)
- Radiation damage: displacement cascades, dpa, swelling, embrittlement, helium
- Nuclear materials: fuels, cladding, structural steels, fusion first-wall
- Aerospace materials: lightweighting, fatigue-critical design
- Cryogenic materials: ductile–brittle behaviour, Invar, insulation
- Hypersonic and space environments

## Part IX — Corrosion, Degradation and Surfaces

### Chapter 42. Thermodynamics and Kinetics of Corrosion
- The electrochemical corrosion cell
- Pourbaix diagrams for Fe, Al, Cu, Zn, Ti
- Mixed-potential theory; Evans diagrams
- Butler–Volmer and Tafel kinetics
- Corrosion rate from current; Faraday's law
- Passivity and passive-film breakdown
- High-temperature oxidation: Wagner theory, parabolic law, Pilling–Bedworth ratio

*Boundary:* electrochemistry fundamentals belong to Advanced Chemistry.

### Chapter 43. Forms of Corrosion and Protection
- Uniform, galvanic, pitting, crevice, intergranular corrosion
- Stress-corrosion cracking, hydrogen embrittlement, corrosion fatigue
- Microbially influenced corrosion; selective leaching; erosion–corrosion; cavitation
- Protection: material selection, coatings, galvanizing, inhibitors
- Cathodic protection: sacrificial and impressed current; sizing
- Anodic protection; design rules
- Testing: salt spray, polarization, EIS

### Chapter 44. Degradation and Failure Analysis
- Degradation mechanisms across classes: metals, ceramics, polymers, composites, concrete
- Polymer aging and weathering
- Wear-out mechanisms and life prediction
- Failure analysis: methodology, fractography, root cause
- Case studies across industries
- Reliability statistics: Weibull, bathtub curve
- Wear-out of electronic materials: Norris–Landzberg, electromigration (Black's equation, Blech length), dielectric breakdown and TDDB, semiconductor defect generation, moisture ingress, contact degradation
- Accelerated aging tests: HAST, THB, temperature cycling, HTOL

### Chapter 45. Surfaces, Interfaces and Tribology
- Surface structure and surface energy
- Adsorption and surface chemistry
- Adhesion and wetting
- Contact mechanics: Hertz, real contact area
- Friction: Amontons' laws and their origins
- Wear mechanisms: adhesive, abrasive, fatigue, corrosive
- Lubrication regimes: Stribeck curve
- Surface engineering: coatings, hardening, texturing

## Part X — Processing and Manufacturing

### Chapter 46. Casting, Forming and Powder Processing
- Casting processes and casting design; defects
- Deformation processing: rolling, forging, extrusion, drawing, sheet forming
- Hot, warm and cold working; formability and forming limit diagrams
- Thermomechanical processing and texture control
- Powder metallurgy: production, compaction, sintering, HIP, MIM
- Processing of ceramics and glasses (pointer to Ch 17)

### Chapter 47. Joining: Welding, Brazing and Adhesive Bonding
- Fusion welding processes: arc, laser, electron beam
- Welding metallurgy: fusion zone, heat-affected zone, residual stress
- Weldability: carbon equivalent, hot and cold cracking
- Solid-state welding: friction stir, diffusion bonding
- Brazing and soldering
- Adhesive bonding: surface preparation, joint design
- Mechanical fastening and joining dissimilar materials

### Chapter 48. Additive Manufacturing
- Process families: powder-bed fusion, directed energy deposition, binder jetting, material extrusion, vat photopolymerization
- Melt-pool physics and solidification in AM
- Microstructure and defects: porosity, lack of fusion, residual stress, anisotropy
- Post-processing: HIP, heat treatment, machining
- Polymer and ceramic AM
- Design for AM; qualification and certification

### Chapter 49. Thin Films and Coatings
- Vacuum and plasma basics
- PVD, CVD, ALD, electroplating, sol–gel
- Thin-film growth modes and structure-zone models
- Film stress and adhesion
- Electroless plating, anodizing, conversion coatings
- Crystal growth and semiconductor processing (pointer to Ch 50)
- Thermal spray and hard coatings

### Chapter 50. Electronic Materials Manufacturing
- Single-crystal growth
- Wafer preparation
- Thin-film deposition
- Oxidation and diffusion
- Doping and implantation principles
- Photolithography overview
- Etching
- Metallization
- Dielectric deposition
- Packaging and encapsulation materials
- Process-induced defects

*Boundary:* how manufacturing changes material structure and properties. Detailed fabrication flows and IC process integration remain in Electronics & Computing.

### Chapter 51. Joining, Packaging, and Interconnect Materials
- Solder materials
- Bonding wires
- Flip-chip interconnects
- Conductive adhesives
- Substrate materials
- Printed circuit board laminates
- Encapsulation materials
- Thermal interface materials
- Coefficient-of-thermal-expansion mismatch
- Package stress and failure mechanisms

## Part XI — Characterization, Computation and Design

### Chapter 52. Materials Characterization: The Laboratory Toolkit
- Optical microscopy and metallography
- SEM, EDS, EBSD; TEM and diffraction
- X-ray diffraction in practice
- Surface analysis: XPS, AES, SIMS
- Spectroscopy: Raman, FTIR, UV–Vis
- Thermal analysis: DSC, TGA, TMA, DMA
- Mechanical and electrical testing
- Measurement uncertainty

### Chapter 53. Large-Facility and Nanoscale Characterization
- Synchrotron X-rays: XAS (XANES, EXAFS), SAXS, high-resolution diffraction, PDF analysis, tomography
- Neutron scattering: contrast with X-rays, magnetic structures, light elements, residual stress, inelastic scattering
- Atom-probe tomography
- Aberration-corrected STEM: HAADF, EELS, 4D-STEM
- Cryo-EM for soft materials

### Chapter 54. In-Situ, Operando and Correlative Methods
- In-situ heating, straining and biasing in TEM and SEM
- Operando battery and catalyst studies
- Positron annihilation spectroscopy
- Mössbauer and solid-state NMR
- Micropillar compression and in-situ nanoindentation
- Correlative multimodal workflows
- Big data and automated analysis

### Chapter 55. Electronic-Structure Methods
- Born–Oppenheimer approximation; Hartree–Fock; why DFT
- Kohn–Sham equations; exchange–correlation functionals: LDA, GGA, hybrids, DFT+U
- Basis sets: plane waves, pseudopotentials, PAW
- k-point sampling and convergence
- What DFT predicts well and badly
- Practical workflows: codes, inputs, outputs, validation

*Boundary:* quantum-mechanical foundations belong to Engineering Physics.

### Chapter 56. Atomistic and Mesoscale Simulation
- Molecular dynamics: interatomic potentials (LJ, EAM, Tersoff, ReaxFF), integrators, thermostats, barostats
- Monte Carlo: Metropolis; kinetic Monte Carlo
- Phase-field modelling
- Discrete dislocation dynamics; crystal plasticity FEM
- CALPHAD and computational thermodynamics
- Multiscale modelling and ICME

### Chapter 57. Materials Informatics
- Materials databases: Materials Project, AFLOW, OQMD, ICSD
- Descriptors and features
- Machine-learning property prediction; graph neural networks
- Machine-learned interatomic potentials (GAP, NequIP, MACE)
- High-throughput screening; active learning; autonomous labs
- Inverse design
- Uncertainty and the limits of data-driven discovery

### Chapter 58. Materials Selection and Design
- Design process and material requirements
- Regulatory compatibility: RoHS, REACH, conflict minerals
- Performance indices derived
- Ashby charts and selection
- Multi-objective selection: Pareto fronts, penalty functions
- Shape factors
- Process selection and cost modelling
- Selection case studies across engineering fields

### Chapter 59. Sustainability, Lifecycle and the Circular Economy
- Materials flows and the materials footprint of society
- Embodied energy and carbon
- Lifecycle assessment
- Critical and conflict materials
- Design for recycling, reuse and remanufacture
- Recycling metallurgy, polymer recycling, construction-waste recovery
- Green materials and the circular economy
- The future of the discipline

---

## Relation to the other books

| Topic | Where it lives |
|---|---|
| Laws of thermodynamics, bonding, reaction chemistry, electrochemistry fundamentals | Advanced Chemistry |
| Quantum mechanics and solid-state physics foundations | Engineering Physics |
| Mathematics (tensors, PDEs, statistics) | The Mathematics Universe |
| Semiconductor device and circuit operation | Electronics & Computing |
| Power-system, machine and battery-system sizing | Electrical Energy & Machines |
| All of materials science and engineering | **This book** |
