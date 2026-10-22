# Chapter 3 — Symmetry and Space Groups

*Part I · Structure of Materials*

Every medical ultrasound probe, every car parking sensor and every sonar array contains a piezoelectric ceramic, almost always lead zirconate titanate (PZT). Above its Curie temperature of about 350 °C, PZT is a cubic perovskite and is not piezoelectric at all. A cubic crystal has a centre of symmetry, and a centrosymmetric crystal cannot produce an electric polarization when it is squeezed: any polarization would have to point in some direction, and inversion would turn it into its opposite without changing the crystal. Only when PZT cools through its Curie point and the titanium and zirconium ions shift off-centre, lowering the symmetry to tetragonal or rhombohedral, does piezoelectricity become possible. Even then a freshly sintered ceramic shows almost none: each grain splits into domains whose polarizations point along the six (tetragonal) or eight (rhombohedral) symmetry-equivalent directions, and they cancel. The manufacturer must *pole* the part by applying a strong field at elevated temperature to align the domains. Whether a material can be piezoelectric, how many domain orientations it forms and how it must be processed all follow from symmetry alone, before any property has been measured.

Symmetry is the most economical description of a crystal: instead of listing every atom, one lists a few atoms and the operations that generate the rest. It is also a powerful constraint on properties, a guide to phase transformations and the key to reading the crystallographic databases that every materials engineer eventually uses. This chapter develops the theory at the level an engineer needs.

> **Which symmetry operations can a crystal have, and why are only certain lattices, point groups and space groups possible?**
> **How do symmetry and its breaking explain piezoelectricity, domains, ordering, texture and the existence of quasicrystals?**

| Concept | Engineering destination |
|---|---|
| Symmetry operations, including screw axes and glide planes | Reading structure files; predicting diffraction absences (Chapter 4) |
| 32 point groups and 7 crystal systems | Which tensor properties exist: piezo-, pyro- and ferroelectricity (Chapters 4, 25) |
| 14 Bravais lattices | Choosing cells; recognizing equivalent descriptions; lattice-based calculations (Chapters 4, 45) |
| 230 space groups; International Tables | Atomic positions, Wyckoff sites, databases and simulation inputs (Chapters 45–47) |
| Stereographic projection and pole figures | Texture control in sheet, wire, cladding and additively manufactured parts (Chapters 38, 40, 42) |
| Symmetry of real structures; symmetry breaking | Domains in ferroelectrics, variants in martensite and shape-memory alloys (Chapters 10, 29) |
| Superlattices, ordering, antiphase boundaries | Superalloys, intermetallics, magnetic alloys (Chapters 12, 16) |
| Quasicrystals and incommensurate structures | Coatings, modulated martensites, the modern definition of a crystal |

**Roadmap.** Symmetry operations (3.1) → the point groups and crystal systems they allow (3.2) → the fourteen Bravais lattices (3.3) → space groups and the International Tables (3.4) → stereographic projection and pole figures (3.5) → symmetry of real structures and its breaking (3.6) → ordering and antiphase boundaries (3.7) → quasicrystals and incommensurate structures (3.8).

---

## 3.1 Symmetry operations

### What a symmetry operation is

A **symmetry operation** is a rigid motion (one that preserves all distances) that carries an object into a position indistinguishable from the original. The set of points, lines or planes left fixed by the operation is its **symmetry element**. For a finite object such as a molecule, or for the arrangement of atoms around one point of a crystal, the operations leave at least one point fixed; for an infinite crystal they may also include translations.

Every rigid motion can be written as $\mathbf x'=\mathbf W\mathbf x+\mathbf w$, where $\mathbf W$ is a $3\times3$ orthogonal matrix (a rotation or a rotation combined with inversion) and $\mathbf w$ a translation. Crystallographers write the operations in the compact notation of the International Tables: the operation $(x,y,z)\to(-y,x,z)$ is a fourfold rotation about $z$; $(x,y,z)\to(-x,-y,-z)$ is inversion.

### Point operations

Operations that leave at least one point fixed are:

- **Rotation** by $360^\circ/n$ about an axis, an $n$-fold axis written $n$ (Hermann–Mauguin notation) or $C_n$ (Schoenflies). Applying it $n$ times returns the object to its starting position.
- **Reflection** in a mirror plane, written $m$ (Schoenflies $\sigma$). It turns a right hand into a left hand.
- **Inversion** through a centre, written $\bar1$ (Schoenflies $i$): $\mathbf x\to-\mathbf x$. A crystal with this element is **centrosymmetric**.
- **Rotoinversion**, rotation by $360^\circ/n$ followed by inversion, written $\bar n$. $\bar1$ is inversion itself; $\bar2$ is identical to a mirror perpendicular to the axis; $\bar3$ equals a threefold axis plus a centre; $\bar4$ is a genuinely new operation, present in the tetrahedral sites of zincblende; $\bar6$ equals a threefold axis with a perpendicular mirror. (Schoenflies notation uses the equivalent *rotoreflections* $S_n$ instead.)

Rotations are **proper** operations (determinant of $\mathbf W$ equal to $+1$): they can be performed physically on a real object. Reflections, inversion and rotoinversions are **improper** (determinant $-1$): they convert an object into its mirror image. A crystal whose symmetry contains only proper operations can exist in left- and right-handed forms; quartz is the classic example, and the two hands rotate polarized light in opposite senses.

### Operations with translation: screw axes and glide planes

Figure 3.1 summarizes these operations. An infinite crystal can also be invariant under operations combining a point operation with a translation that is a *fraction* of a lattice vector.

- A **screw axis** $n_p$ combines a rotation of $360^\circ/n$ with a translation of $p/n$ of the lattice repeat along the axis. A $2_1$ axis rotates by 180° and translates by half a repeat; $3_1$ and $3_2$ rotate by 120° and translate by one-third and two-thirds, giving right- and left-handed helices; $6_3$ rotates by 60° and translates by half the $c$ repeat, which is exactly how the A and B layers of HCP are related. The polymer chains of Chapter 2 are built on screw axes: the planar zigzag of polyethylene has a $2_1$ axis, and isotactic polypropylene a threefold helix.
- A **glide plane** combines reflection with a translation of half a lattice vector parallel to the plane: an $a$, $b$ or $c$ glide translates along that axis, an $n$ glide along a face diagonal and a $d$ ("diamond") glide by a quarter of a face diagonal.

Screw axes and glide planes are invisible in the external shape of a crystal and in its macroscopic properties, because over macroscopic distances the fractional translation is negligible; a $2_1$ axis and a $2$ axis produce the same symmetry of a property tensor. But they are clearly visible in diffraction, where they cause certain reflections to vanish (*systematic absences*, Chapter 4), which is how they are detected.

<!-- FIGURE 3.1 | figures/ch03/fig-3-1-symmetry-operations.png | schematic | The crystallographic symmetry operations acting on a motif: rotation, reflection, inversion, rotoinversion, screw axis and glide plane. | Content: six panels, each using a small asymmetric motif (a comma or a "right hand" shape) with "+"/"−" height labels and open/filled shading for mirror images, in the style of International Tables stereograms. (a) 4-fold rotation: four equivalent commas around an axis, graphic symbol ■. (b) mirror m: pair of mirror-image commas across a plane. (c) inversion 1-bar: comma at +z and its inverted, mirror-image partner at −z through a centre. (d) 4-bar rotoinversion: four commas alternating +/− and right/left handed, symbol ■ with inscribed ellipse. (e) screw axis 2_1 along c: helix of two commas, rotated 180° and raised by c/2; contrast with a plain 2 axis. (f) c-glide: comma reflected across a plane and translated by c/2. Each panel labelled with Hermann–Mauguin and Schoenflies symbols (4/C4, m/σ, 1-bar/i, 4-bar/S4, 2_1, c). -->

### Groups

The symmetry operations of an object always form a **group** in the mathematical sense: the combination of any two is again a symmetry operation, there is an identity (do nothing), each operation has an inverse, and combination is associative. Group theory is what makes symmetry so economical: a few **generators** produce all the operations, and the number of operations, the **order** of the group, is a key quantity. The point group of a cube, for example, has order 48 and can be generated from a fourfold axis, a threefold axis and inversion.

---

## 3.2 The 32 point groups and the 7 crystal systems

### The crystallographic restriction

A lattice can have only certain rotational symmetries. Suppose a lattice has an $n$-fold axis. In a basis of lattice vectors, the matrix of the rotation must have integer entries, because it maps lattice points onto lattice points. The trace of a matrix does not depend on the basis, and in a Cartesian basis the trace of a rotation by $\phi$ is $1+2\cos\phi$. Hence

$$
1+2\cos\frac{2\pi}{n}\in\mathbb Z\quad\Longrightarrow\quad 2\cos\frac{2\pi}{n}\in\{-2,-1,0,1,2\}
$$

which allows only $n=1,2,3,4,6$ (traces $3,-1,0,1,2$). For $n=5$ the trace would be $1+2\cos72^\circ=1.618$, the golden ratio; for $n=7$, 2.247; for $n=8$, 2.414. None is an integer.

> **Status of the principle: crystallographic restriction theorem**
> *Derived.* It follows rigorously from the requirement that a rotation map a three-dimensional lattice onto itself; it forbids five-, seven- and higher-fold axes in any periodic crystal, but not in quasicrystals, which are ordered without being periodic (Section 3.8).

A geometric picture makes the same point (Figure 3.2): squares, equilateral triangles and hexagons tile the plane, but regular pentagons leave gaps.

### The 32 crystallographic point groups

The **point group** of a crystal is the set of point operations (rotations, mirrors, inversion, rotoinversions) that leave the crystal's *pattern of directions* unchanged; it is obtained from the full symmetry by discarding all translations, so screw axes count as plain rotations and glides as plain mirrors. Combining the allowed axes 1, 2, 3, 4, 6 and their rotoinversions in every self-consistent way gives exactly **32 crystallographic point groups** (also called crystal classes). They are the possible symmetries of crystal shapes and of crystal properties.

The point groups are sorted into seven **crystal systems** according to their characteristic symmetry, the minimum symmetry that a crystal of that system must have:

| Crystal system | Characteristic symmetry | Lattice parameters (conventional cell) | Point groups (Hermann–Mauguin) | Number | Engineering examples |
|---|---|---|---|---|---|
| Triclinic | None, or only $\bar1$ | $a\ne b\ne c$; $\alpha\ne\beta\ne\gamma$ | $1$, $\bar1$ | 2 | Plagioclase feldspar, CuSO$_4\cdot$5H$_2$O |
| Monoclinic | One 2-fold axis or mirror | $a\ne b\ne c$; $\alpha=\gamma=90^\circ\ne\beta$ | $2$, $m$, $2/m$ | 3 | Monoclinic ZrO$_2$, gypsum, many molecular crystals |
| Orthorhombic | Three perpendicular 2-fold axes or mirrors | $a\ne b\ne c$; all $90^\circ$ | $222$, $mm2$, $mmm$ | 3 | Polyethylene, cementite Fe$_3$C, olivine, YBa$_2$Cu$_3$O$_7$ |
| Tetragonal | One 4-fold axis | $a=b\ne c$; all $90^\circ$ | $4$, $\bar4$, $4/m$, $422$, $4mm$, $\bar42m$, $4/mmm$ | 7 | β-Sn, rutile TiO$_2$, tetragonal BaTiO$_3$ and ZrO$_2$, martensite |
| Trigonal | One 3-fold axis | $a=b=c$, $\alpha=\beta=\gamma\ne90^\circ$ (rhombohedral) or hexagonal axes | $3$, $\bar3$, $32$, $3m$, $\bar3m$ | 5 | α-quartz, sapphire, calcite, LiNbO$_3$, Bi$_2$Te$_3$ |
| Hexagonal | One 6-fold axis | $a=b\ne c$; $\alpha=\beta=90^\circ$, $\gamma=120^\circ$ | $6$, $\bar6$, $6/m$, $622$, $6mm$, $\bar6m2$, $6/mmm$ | 7 | Mg, Ti, Zn, ice, graphite, ZnO, GaN, hydroxyapatite |
| Cubic | Four 3-fold axes (body diagonals) | $a=b=c$; all $90^\circ$ | $23$, $m\bar3$, $432$, $\bar43m$, $m\bar3m$ | 5 | Cu, Fe, Al, Si, NaCl, GaAs, spinels, garnets |

The equalities of lattice parameters are consequences of the symmetry, not its definition. A crystal with a fourfold axis must have $a=b$; but a crystal whose $a$ and $b$ happen to be equal to within measurement error is not tetragonal unless it has the fourfold axis.

<!-- FIGURE 3.2 | figures/ch03/fig-3-2-restriction-bravais.png | crystal | Why only 1-, 2-, 3-, 4- and 6-fold axes are compatible with a lattice, and the 14 Bravais lattices. | Content: top strip: plane tilings by regular polygons — triangles, squares and hexagons fill the plane; pentagons leave rhombic gaps (shaded red) and octagons leave square gaps; label "trace 1 + 2cos(2π/n) must be an integer: n = 1, 2, 3, 4, 6". Main panel: the 14 Bravais lattices as conventional cells, grouped by crystal system in rows: triclinic P; monoclinic P, C; orthorhombic P, C, I, F; tetragonal P, I; hexagonal P (with primitive cell outlined in the hexagonal prism); rhombohedral R (drawn both as rhombohedron and in hexagonal setting with the extra points at (2/3,1/3,1/3) and (1/3,2/3,2/3)); cubic P, I, F. Lattice points as spheres, centring points in a second colour. Inset: "C-centred tetragonal = smaller primitive tetragonal" with the a/√2 cell drawn inside the C cell. -->

### Laue classes and the properties symmetry allows

Point groups decide which physical properties a crystal can have, through **Neumann's principle**: the symmetry of any physical property must include the symmetry of the crystal's point group (developed with tensors in Chapter 4).

> **Status of the principle: Neumann's principle**
> *Fundamental.* A property cannot change when the crystal is carried into an indistinguishable configuration, so every symmetry operation of the point group must leave every property tensor unchanged.

Three consequences sort the 32 point groups.

- **Eleven point groups are centrosymmetric** ($\bar1$, $2/m$, $mmm$, $4/m$, $4/mmm$, $\bar3$, $\bar3m$, $6/m$, $6/mmm$, $m\bar3$, $m\bar3m$). These are the **Laue classes**: because diffraction intensities normally add a centre of symmetry, a diffraction pattern reveals only the Laue class of a crystal, not its full point group.
- **The other 21 lack a centre of symmetry**, and 20 of them (all except $432$) allow **piezoelectricity**, the polarization produced by stress. Quartz ($32$), GaN and ZnO ($6mm$), GaAs ($\bar43m$) and poled PZT ($4mm$ or $3m$) are piezoelectric; silicon, iron and alumina ($m\bar3m$, $m\bar3m$, $\bar3m$) are not.
- **Ten of the 20 are polar** ($1$, $2$, $m$, $mm2$, $4$, $4mm$, $3$, $3m$, $6$, $6mm$): they have a direction that no symmetry operation reverses, so they can carry a spontaneous polarization. These crystals are **pyroelectric**: their polarization changes with temperature, the basis of infrared detectors. If the spontaneous polarization can be switched by a field, the crystal is **ferroelectric** (BaTiO$_3$, PZT, LiNbO$_3$; Chapter 25).

| Property | Symmetry requirement | Number of point groups | Examples |
|---|---|---|---|
| Enantiomorphism (left- and right-handed forms) | No improper operations | 11 | Quartz, sugar crystals |
| Piezoelectricity | No centre of symmetry (and not $432$) | 20 | Quartz, AlN, ZnO, PZT, PVDF (β-phase) |
| Pyroelectricity, ferroelectricity | Polar point group | 10 | Tourmaline, LiTaO$_3$, BaTiO$_3$, PZT |
| Isotropic second-rank tensors (conductivity, expansion) | Cubic | 5 | Cu, Fe, Si, MgO |
| Uniaxial second-rank tensors | Tetragonal, trigonal, hexagonal | 19 | Sapphire, Zn, Ti, GaN, graphite |

The opening problem now has its formal answer. Cubic PZT has point group $m\bar3m$, centrosymmetric, so its piezoelectric tensor must vanish. Tetragonal PZT has point group $4mm$, polar, so it can be piezoelectric and ferroelectric.

---

## 3.3 The 14 Bravais lattices and why only these exist

### Lattice systems and centring

A lattice is itself an object with symmetry, and its point symmetry must be one of the *holohedral* (maximal) point groups of the seven systems: $\bar1$, $2/m$, $mmm$, $4/mmm$, $\bar3m$, $6/mmm$ and $m\bar3m$. Taking the simplest (primitive, P) lattice of each system gives seven lattices. Others arise by **centring**: adding lattice points at the centre of the cell (body-centred, I), at the centres of all faces (F) or at the centres of one pair of faces (A, B or C). The trigonal system has its own rhombohedral lattice (R), equivalent to a hexagonal cell with two extra points inside.

A centred cell is a new Bravais lattice only if two conditions hold: the centred arrangement must keep the full symmetry of its system, and it must not be describable by a smaller cell of the same system. Applying these tests to every possible centring of every system leaves exactly **14 Bravais lattices** (Figure 3.2):

| System | Bravais lattices | Lattice points per conventional cell |
|---|---|---|
| Triclinic | P | 1 |
| Monoclinic | P, C | 1, 2 |
| Orthorhombic | P, C, I, F | 1, 2, 2, 4 |
| Tetragonal | P, I | 1, 2 |
| Trigonal (rhombohedral) | R | 1 (3 in hexagonal setting) |
| Hexagonal | P | 1 |
| Cubic | P, I, F | 1, 2, 4 |

> **Status of the principle: the 14 Bravais lattices**
> *Derived.* They follow from enumerating the centrings compatible with the seven lattice point symmetries and removing duplicates (Bravais, 1848); the list is complete for three-dimensional periodic lattices.

### Why the others are missing

Each missing combination fails one of the tests.

- **C-centred cubic** would put extra points on only one pair of faces, destroying the threefold axes along the body diagonals; the result would no longer be cubic, but tetragonal.
- **C-centred tetragonal** is identical to a smaller primitive tetragonal lattice. In a C-centred tetragonal cell of side $a$, the face-centre point and the corners together form a square net of side $a/\sqrt2$ rotated by 45°; the new cell has the same $c$, edge $a/\sqrt2$, half the volume and only corner points.
- **F-centred tetragonal** is similarly identical to an I-centred tetragonal cell with edge $a/\sqrt2$.
- **Body-centred or face-centred hexagonal** would break the sixfold symmetry, and **base-centred hexagonal** reduces to a smaller primitive cell.

**Worked example — Two descriptions of one lattice.** A tetragonal crystal is reported with a C-centred cell $a=b=0.600$ nm, $c=0.400$ nm. Its conventional cell contains $8\times\tfrac18+2\times\tfrac12=2$ lattice points in volume $a^2c=0.1440\ \mathrm{nm^3}$, i.e. $0.0720\ \mathrm{nm^3}$ per point. The primitive tetragonal cell spanned by $\tfrac12(\mathbf a+\mathbf b)$, $\tfrac12(\mathbf a-\mathbf b)$ and $\mathbf c$ has edges $0.600/\sqrt2=0.4243$ nm, perpendicular to each other, and $c=0.400$ nm, so its volume is $0.4243^2\times0.400=0.0720\ \mathrm{nm^3}$ with one lattice point: the same lattice, described by a cell of half the size, and still tetragonal. The reverse effect occurs in FCC metals. The primitive cell of copper is a rhombohedron with edge $a/\sqrt2=0.2556$ nm and interaxial angles of 60°, volume $a^3/4=0.01181\ \mathrm{nm^3}$; it is perfectly valid but hides the cubic symmetry, which is why the four-point conventional cube is used. Neither description is "the" lattice; one is chosen for convenience and the conventions of the International Tables fix the choice so that databases agree.

### Lattice systems, crystal systems and crystal families

Two subtleties often confuse. First, the classification of *lattices* and of *point groups* differ in the trigonal/hexagonal case: a crystal of the trigonal system may have either a rhombohedral (R) lattice (sapphire, calcite) or a hexagonal (P) lattice (quartz). Strictly, there are seven crystal systems, seven lattice systems and six crystal families. Second, the lattice can have higher symmetry than the crystal: tetragonal BaTiO$_3$ has a lattice that is very nearly cubic ($c/a=1.011$), but its point group, which includes the displaced atoms, is unmistakably tetragonal.

---

## 3.4 The 230 space groups; reading the International Tables

### From point groups to space groups

Combining the 32 point groups with the 14 Bravais lattices, and with all the ways of replacing rotations by screw axes and mirrors by glides, gives exactly **230 space groups** (enumerated independently by Fedorov and Schoenflies in 1891). Every periodic crystal belongs to one of them.

| Crystal system | Number of space groups | Space-group numbers |
|---|---|---|
| Triclinic | 2 | 1–2 |
| Monoclinic | 13 | 3–15 |
| Orthorhombic | 59 | 16–74 |
| Tetragonal | 68 | 75–142 |
| Trigonal | 25 | 143–167 |
| Hexagonal | 27 | 168–194 |
| Cubic | 36 | 195–230 |

Seventy-three of these are **symmorphic**, containing no screw axes or glides (for example $Pm\bar3m$, $Fm\bar3m$); the other 157 contain at least one. Eleven pairs differ only in handedness (such as $P3_121$ and $P3_221$, the two hands of α-quartz).

> **Status of the principle: the 230 space groups**
> *Derived.* They are the complete set of symmetry groups of three-dimensional periodic patterns, obtained by group-theoretical enumeration; the count assumes perfect periodicity and is exceeded by magnetic (1651 Shubnikov groups) and modulated (superspace) structures.

### The space-group symbol

The **Hermann–Mauguin symbol** begins with the lattice letter (P, A, B, C, I, F, R) and then lists the symmetry along characteristic directions, which depend on the system: for cubic, the cube axis, the body diagonal and the face diagonal; for tetragonal, $c$, $a$ and $[110]$; for hexagonal, $c$, $a$ and $[1\bar10]$; for orthorhombic, $a$, $b$ and $c$. Thus:

- $Fm\bar3m$ (No. 225): F-centred cubic, mirrors perpendicular to the cube axes, $\bar3$ along the body diagonals, mirrors perpendicular to the face diagonals. Copper, aluminium, nickel, NaCl, MgO, CaF$_2$, UO$_2$.
- $Im\bar3m$ (No. 229): the same point group on a body-centred lattice. α-Fe, W, Mo, Cr.
- $P6_3/mmc$ (No. 194): hexagonal, a $6_3$ screw axis along $c$ with a perpendicular mirror, mirrors and $c$-glides parallel to $c$. Mg, Ti, Zn, Co; graphite.
- $Fd\bar3m$ (No. 227): cubic with diamond glides. Diamond, Si, Ge, and spinels such as MgAl$_2$O$_4$.
- $F\bar43m$ (No. 216): zincblende GaAs and cubic SiC, which lack the centre of diamond.
- $P6_3mc$ (No. 186): wurtzite GaN, ZnO, AlN, polar.
- $Pm\bar3m$ (No. 221): cubic perovskite (BaTiO$_3$ above its Curie point), CsCl, and ordered alloys such as Cu$_3$Au, Ni$_3$Al and NiAl.
- $P4mm$ (No. 99): tetragonal BaTiO$_3$. $R\bar3c$ (No. 167): corundum. $Pnma$ (No. 62): cementite, many orthorhombic perovskites, polyethylene. $P2_1/c$ (No. 14): monoclinic ZrO$_2$, and the most common space group of all for molecular crystals.

### Reading a page of the International Tables

The *International Tables for Crystallography, Volume A* devotes a page or two to each space group. The entries an engineer needs are:

- **Symbols and number**: short and full Hermann–Mauguin symbols, Schoenflies symbol, number, point group and crystal system.
- **Diagrams**: the positions of the symmetry elements in the cell, and a stereogram-like diagram of the equivalent positions generated from one general point.
- **Origin choice**: some groups have two standard origins (for example, origin choice 1 of $Fd\bar3m$ at a site of $\bar43m$ symmetry, origin choice 2 at a centre of inversion). Structure files must say which is used, or atoms land in the wrong places.
- **Symmetry operations**, as coordinate triplets such as $(-y, x-y, z+\tfrac12)$.
- **Wyckoff positions**: the list of positions, each given a **multiplicity** (how many equivalent points it generates in the conventional cell), a **Wyckoff letter**, a **site symmetry** (the point symmetry of that position) and its coordinates. The *general position* has site symmetry 1 and the largest multiplicity, equal to the order of the point group times the number of lattice points per cell; *special positions* lie on symmetry elements, have higher site symmetry and lower multiplicity, and some have fixed coordinates while others have free parameters such as $(x,x,x)$.
- **Reflection conditions**: the systematic absences produced by centring, screw axes and glides (Chapter 4).
- **Maximal subgroups and minimal supergroups**: the symmetry relations used to analyse phase transitions (Section 3.6).

A crystal structure is then completely specified (Figure 3.3) by its space group, its lattice parameters and the Wyckoff positions (with any free parameters) of the atoms in the **asymmetric unit**. This is exactly the content of a crystallographic information file (CIF) in databases such as the ICSD, and of the input to electronic-structure and molecular-dynamics codes (Chapters 45–47).

<!-- FIGURE 3.3 | figures/ch03/fig-3-3-wyckoff-positions.png | crystal | Building structures from Wyckoff positions: rock salt, fluorite and spinel in space groups Fm-3m and Fd-3m. | Content: three panels. (a) Fm-3m cell with Wyckoff sites colour-coded: 4a (0,0,0) red, 4b (½,½,½) blue, 8c (¼,¼,¼) green, one 24e (x,0,0) site grey; table beside: letter, multiplicity, site symmetry (4a m-3m, 4b m-3m, 8c -43m, 24d m.mm, 24e 4m.m, 192l 1). (b) "Choose sites": NaCl = Na 4a + Cl 4b; CaF2 = Ca 4a + F 8c; Cu = Cu 4a; each drawn as a small cell. (c) Spinel MgAl2O4 in Fd-3m (origin choice 2): Mg 8a, Al 16d, O 32e (x,x,x) with x ≈ 0.26; one-eighth of the cell shown with tetrahedral Mg and octahedral Al; count 8 + 16 + 32 = 56 atoms. -->

**Worked example — Building three structures from the tables.** *Rock salt.* $Fm\bar3m$ has point group order 48 and 4 lattice points per cell, so its general position $192l$ has multiplicity $48\times4=192$. The special positions $4a$ at $(0,0,0)$ and $4b$ at $(\tfrac12,\tfrac12,\tfrac12)$ each have site symmetry $m\bar3m$ and multiplicity 4: the four points are the origin plus the F-centring translations $(0,\tfrac12,\tfrac12)$, $(\tfrac12,0,\tfrac12)$, $(\tfrac12,\tfrac12,0)$. Placing Na at $4a$ and Cl at $4b$ gives the whole structure: 4 Na and 4 Cl per cell, each ion octahedrally surrounded by six of the other. With $a=0.5640$ nm,

$$
\rho=\frac{4\times58.44}{(5.640\times10^{-8})^3\times6.022\times10^{23}}=2.16\ \mathrm{g\,cm^{-3}}
$$

Changing only the anion site to $8c$ at $(\tfrac14,\tfrac14,\tfrac14)$ (site symmetry $\bar43m$) gives fluorite: 4 Ca + 8 F, the CaF$_2$ stoichiometry, every F tetrahedrally coordinated. One line of a table distinguishes table salt from nuclear fuel (UO$_2$).

*Silicon.* In $Fd\bar3m$ (origin choice 1) silicon occupies $8a$, whose two representative points $(0,0,0)$ and $(\tfrac14,\tfrac14,\tfrac14)$ plus F-centring give the 8 atoms of the diamond cell, each on a site of symmetry $\bar43m$, the tetrahedral symmetry of the $sp^3$ bond. 

*Corundum.* In $R\bar3c$ (hexagonal setting, 3 lattice points per cell) Al occupies $12c$ at $(0,0,z)$ with $z\approx0.352$ and O occupies $18e$ at $(x,0,\tfrac14)$ with $x\approx0.306$. The cell therefore holds $12+18=30$ atoms, six Al$_2$O$_3$ formula units, and two free parameters describe the slight buckling of the oxygen layers and displacement of the Al ions from ideal octahedral sites. These two numbers, refined by diffraction, are all that distinguishes real sapphire from an idealized close-packed model.

---

## 3.5 Stereographic projection and pole figures

### Projecting directions onto a plane

Crystallography constantly needs angles between directions and planes in three dimensions: between slip planes and a loading axis, between a wafer surface and an etch facet, between grain orientations and a sheet's rolling direction. The **stereographic projection** maps directions onto a flat diagram while preserving angles.

Imagine the crystal at the centre of a **reference sphere** of radius $R$. Each plane is represented by its normal, extended until it meets the sphere at a **pole**. Each pole in the northern hemisphere is joined by a straight line to the south pole of the sphere, and the point where that line crosses the equatorial plane is the projection. A pole at angle $\phi$ from the north pole (the projection axis) lands at distance

$$
r=R\tan\frac{\phi}{2}
$$

from the centre. Poles at the north pole plot at the centre, poles on the equator ($\phi=90^\circ$) on the **primitive circle** of radius $R$. Planes containing the projection axis plot as straight lines through the centre; all other planes plot as arcs of circles (great circles). Small circles of constant angle about any pole also project as circles: the projection is *conformal*, which is why it is used instead of simpler projections. Angles are measured with a **Wulff net**, a stereographic grid of great and small circles.

> **Status of the principle: stereographic projection**
> *Derived.* Pure spherical geometry: the mapping $r=R\tan(\phi/2)$ preserves angles locally and maps circles on the sphere to circles in the plane, but it does not preserve areas, which is why texture intensities are normalized on the sphere, not on the diagram.

### The standard projection of a cubic crystal

A **standard projection** shows the poles of the low-index planes of a crystal with one chosen pole at the centre (Figure 3.4). For a cubic crystal viewed down $[001]$:

- the $\{100\}$ poles lie at the centre and at four points on the primitive circle;
- the $\{110\}$ poles lie at $45^\circ$ from the centre ($r=R\tan22.5^\circ=0.414R$) and on the primitive circle;
- the $\{111\}$ poles lie at $54.74^\circ$ ($r=R\tan27.37^\circ=0.518R$), at azimuths of $45^\circ$, $135^\circ$, $225^\circ$ and $315^\circ$;
- $\{112\}$ poles at $35.26^\circ$ ($r=0.318R$) and $\{012\}$ at $26.57^\circ$ ($r=0.236R$).

The cubic symmetry divides the projection into 48 identical spherical triangles. One of them, bounded by $001$, $011$ and $111$, the **standard stereographic triangle**, contains every distinct orientation of a direction in a cubic crystal, and is used to plot loading axes in single-crystal experiments (Chapter 13) and in inverse pole figures.

<!-- FIGURE 3.4 | figures/ch03/fig-3-4-stereographic-pole-figures.png | plot | The stereographic projection of a cubic crystal and the {111} pole figures of rolled and recrystallized FCC sheet. | Content: (a) Construction: reference sphere with crystal at centre, pole P at angle φ from north pole N, line from P to south pole S crossing equatorial plane at P′, label r = R tan(φ/2). (b) Standard (001) projection of a cubic crystal on the primitive circle: poles 001 (centre), 100, 010, -100, 0-10 on rim; 011-type at r = 0.414R and on rim; 111-type at r = 0.518R at 45° azimuths; 112-type at 0.318R; 012-type at 0.236R; great circles for {100} and {110} zones drawn; one standard triangle 001–011–111 shaded. (c) {111} pole figure (RD up, TD right, ND at centre) for ideal cube texture {001}<100>: four peaks at r = 0.518R on the 45° diagonals, contour levels 1, 2, 4, 8, 16 MRD. (d) {111} pole figure for cold-rolled copper (typical β-fibre: copper {112}<111>, S {123}<634>, brass {110}<112> components), maximum about 8 MRD, with ideal component positions marked by symbols. -->

**Worked example — Locating texture components on a pole figure.** An aluminium sheet recrystallized after rolling has the **cube texture** $\{001\}\langle100\rangle$: most grains have a cube face in the sheet plane and a cube edge along the rolling direction (RD). A $\{111\}$ pole figure is plotted with the sheet normal (ND) at the centre, RD at the top and the transverse direction (TD) at the right. Where do the peaks appear?

In each cube-oriented grain, $[001]$ is parallel to ND and $[100]$ to RD. The four $\langle111\rangle$ poles in the upper hemisphere, $[111]$, $[\bar111]$, $[1\bar11]$ and $[\bar1\bar11]$, all make $54.74^\circ$ with $[001]$, so they lie at

$$
r=R\tan\frac{54.74^\circ}{2}=R\tan27.37^\circ=0.518R
$$

from the centre. Their projections on the sheet plane point along $[110]$, $[\bar110]$, $[1\bar10]$ and $[\bar1\bar10]$, that is, at 45° between RD and TD. The pole figure therefore shows four sharp peaks at about half the radius, on the diagonals. If instead the texture were the Goss component $\{110\}\langle001\rangle$ of electrical steel, with $[110]$ along ND and $[001]$ along RD, the $\langle111\rangle$ poles would lie at $35.26^\circ$ from ND ($r=0.318R$) in the TD–ND plane and at $90^\circ$ (on the rim) along TD: a quite different, immediately recognizable pattern. Reading which ideal orientations a measured pole figure contains is the first step in controlling texture.

### Pole figures and texture

A **pole figure** is a stereographic (or equal-area) map, in the *sample* reference frame (RD, TD, ND for sheet), of the density of poles of one family of crystal planes, summed over all grains. It is measured by X-ray or neutron diffraction, tilting and rotating the sample with the detector fixed on one Bragg reflection, or calculated from orientation maps obtained by electron backscatter diffraction (Chapter 42). Intensities are expressed in **multiples of a random distribution** (MRD): 1 everywhere for a random polycrystal, peaks of 5–20 for strongly textured sheet.

Because one pole figure shows only one family of planes, the full description of texture is the **orientation distribution function** (ODF), the probability density of grain orientations expressed in three Euler angles, computed from several pole figures. Its complement, the **inverse pole figure**, plots the density of crystal directions parallel to one sample axis inside the standard triangle; it is the natural display for wires, fibres, thin films and additively manufactured parts, whose textures are fibres about one axis.

Texture is not an academic curiosity. In deep-drawing steel the γ-fibre ($\{111\}\parallel$ ND) raises the plastic strain ratio $r$ (the ratio of width to thickness strain in a tensile test) above 1.5, so the sheet resists thinning. In aluminium can stock the balance of rolling and cube components sets the height of ears on the drawn cup. In titanium and zirconium alloys, basal textures control anisotropy of strength and hydride orientation. In additively manufactured nickel alloys, the $\langle100\rangle$ fibre along the build direction lowers the modulus along that direction by about a third compared with a random polycrystal. Chapters 13, 38 and 40 develop how processing produces these textures.

---

## 3.6 Symmetry of real structures

### Symmetry and properties

Section 3.2 showed that symmetry determines which properties can exist. It also determines how many independent numbers are needed to describe them: a cubic crystal needs one thermal conductivity and three elastic constants, a hexagonal crystal two conductivities and five elastic constants, a triclinic crystal six and twenty-one (Chapter 4). The effective symmetry of a polycrystal is set by its texture: a random polycrystal is isotropic whatever the crystal symmetry; a rolled sheet usually has orthorhombic sample symmetry ($mmm$, with mirrors perpendicular to RD, TD and ND); a fibre-textured wire has cylindrical symmetry about its axis. **Curie's principle** generalizes the idea to effects: the symmetry of an effect (such as the strain of a crystal under a field) contains the common symmetry elements of the cause and of the medium.

> **Status of the principle: Curie's principle**
> *Fundamental.* An effect cannot be less symmetric than the combination of its causes and the medium; asymmetry in an effect must therefore come from the cause, the medium or a spontaneous symmetry breaking (as in a phase transition).

### Symmetry breaking at phase transitions

Many important transformations lower the symmetry of a crystal: the cubic-to-tetragonal ferroelectric transition of BaTiO$_3$ and PZT, the tetragonal-to-monoclinic transformation of zirconia, the cubic-to-tetragonal Bain distortion in steel martensite, the cubic (B2) to monoclinic martensite of NiTi shape-memory alloys, the disorder–order transitions of Section 3.7. In each case the low-symmetry phase has a space group that is a **subgroup** of the parent's, and the International Tables list the maximal subgroups that guide such analyses.

When symmetry is lost, the lost operations relate several equally good orientations of the new phase. A transformation from a parent point group of order $|G|$ to a product of order $|H|$ creates

$$
N=\frac{|G|}{|H|}
$$

**orientation variants** (or domain states), which form side by side in different regions of the parent crystal. They are separated by **domain walls** or **twin boundaries**. A second, translational kind of variant appears when the lattice repeat increases, as in ordering (Section 3.7), producing antiphase domains.

> **Status of the principle: number of orientation variants $|G|/|H|$**
> *Derived.* A consequence of group theory (Lagrange's theorem): the parent operations not retained in the product generate distinct but energetically equivalent orientations; it counts the possible variants, not which ones form, which depends on stress, field and nucleation.

**Worked example — Domains in ferroelectrics and variants in martensite.** Cubic BaTiO$_3$ has point group $m\bar3m$ of order 48. Tetragonal BaTiO$_3$ has point group $4mm$ of order 8. Hence

$$
N=\frac{48}{8}=6
$$

ferroelectric domain states, with polarization along $[100]$, $[\bar100]$, $[010]$, $[0\bar10]$, $[001]$ or $[00\bar1]$. The rhombohedral phase ($3m$, order 6) has $48/6=8$ states, polarized along the eight body diagonals; the orthorhombic phase ($mm2$, order 4) has 12. PZT near its morphotropic phase boundary, where tetragonal and rhombohedral phases coexist, offers $6+8=14$ possible polarization directions, which helps explain why compositions near that boundary pole most completely and give the highest piezoelectric coefficients (Chapter 25).

The same arithmetic counts martensite variants. If the cubic-to-tetragonal transformation of steel kept only the tetragonal holohedry $4/mmm$ (order 16), there would be $48/16=3$ Bain variants, one for each cube axis that becomes the $c$ axis. The cubic-to-monoclinic transformation of NiTi gives $48/4=12$ lattice-correspondence variants (24 habit-plane variants when the two twin solutions per correspondence are counted). The rich variety of variants is what lets shape-memory alloys accommodate the transformation strain by arranging variants into self-accommodating groups, and then reorient them under stress (Chapters 10 and 29).

---

## 3.7 Superlattices, ordering and antiphase boundaries

### Disorder and order in alloys

In a random substitutional solid solution, each lattice site is occupied by A or B atoms at random, with probabilities equal to the composition. Such an alloy has the symmetry of the simple metallic structure. Below a critical temperature, many alloys with an attraction between unlike atoms **order**: A and B atoms segregate onto distinct sublattices. Because the sites are no longer all equivalent, the lattice repeat or the centring changes, and the ordered structure is called a **superlattice** (or superstructure).

| Ordered structure | Parent | Example alloys | Ordering temperature (typical) |
|---|---|---|---|
| L1$_2$ (Cu$_3$Au type), $Pm\bar3m$ | FCC | Cu$_3$Au, Ni$_3$Al (γ′ in superalloys), Ni$_3$Fe, Al$_3$Sc, Al$_3$Li | 390 °C (Cu$_3$Au); Ni$_3$Al ordered to its melting point |
| L1$_0$ (CuAu type), $P4/mmm$ | FCC | CuAu, FePt, CoPt, TiAl (γ-TiAl turbine blades) | FePt about 1300 °C |
| B2 (CsCl type), $Pm\bar3m$ | BCC | CuZn (β-brass), NiAl, FeAl, FeCo, NiTi austenite | 460 °C (CuZn); NiAl ordered to melting |
| D0$_3$ (Fe$_3$Al type), $Fm\bar3m$ | BCC | Fe$_3$Al, Fe$_3$Si | about 550 °C |

In L1$_2$ Cu$_3$Au, Au occupies the cube corners and Cu the face centres. The F-centring of the disordered FCC lattice is lost, and the lattice becomes simple cubic with a four-atom basis. In B2 CuZn, Cu sits at the corners and Zn at the body centre; the I-centring of BCC is lost. The degree of ordering is measured by the **long-range order parameter**

$$
S=\frac{p_A-x_A}{1-x_A}
$$

where $p_A$ is the probability that a site of the A sublattice is occupied by an A atom and $x_A$ the overall atom fraction of A; $S=1$ for perfect order and $S=0$ for a random alloy. The thermodynamics of ordering, and why $S$ falls continuously to zero in some alloys (B2) but discontinuously in others (L1$_2$), are developed in Chapter 6.

Ordering matters for properties. Ordered Ni$_3$Al precipitates are what make nickel superalloys strong at high temperature (Chapter 16); L1$_0$ FePt has enormous magnetocrystalline anisotropy, used in high-density magnetic recording; ordering in FeCo and Ni$_3$Fe (permalloy) changes magnetic softness; ordering usually raises electrical resistivity less and strength more than disorder would suggest.

### Detecting order: superlattice reflections

When the centring is lost, reflections forbidden for the disordered lattice reappear weakly: the **superlattice reflections**. Their amplitude is proportional to $S$ times the difference in scattering power of the two atoms, while the fundamental reflections depend on the average (Chapter 4 derives this from the structure factor).

**Worked example — Why X-rays see order in Cu$_3$Au but hardly in β-brass.** For L1$_2$ Cu$_3$Au, approximate the X-ray atomic scattering factors at low angle by the atomic numbers: $f_{\mathrm{Au}}\approx79$, $f_{\mathrm{Cu}}\approx29$. The fundamental reflections (all indices odd or all even, as in FCC) have structure-factor amplitude $f_{\mathrm{Au}}+3f_{\mathrm{Cu}}=166$; the superlattice reflections (mixed indices, such as 100 and 110) have $S(f_{\mathrm{Au}}-f_{\mathrm{Cu}})=50S$. The intensity ratio is

$$
\frac{I_{\mathrm{super}}}{I_{\mathrm{fund}}}=\left(\frac{50S}{166}\right)^2=0.091\,S^2
$$

so a fully ordered alloy shows superlattice peaks about 9 % as strong as the fundamentals (before angle-dependent corrections), easily measured; at $S=0.5$ they fall to 2.3 %. For B2 CuZn, $f_{\mathrm{Cu}}\approx29$ and $f_{\mathrm{Zn}}\approx30$ differ by one electron, and the ratio is $(1/59)^2=2.9\times10^{-4}$: the order is practically invisible to X-rays. Neutrons, which scatter from nuclei with lengths unrelated to atomic number ($b_{\mathrm{Cu}}=7.72$ fm, $b_{\mathrm{Zn}}=5.68$ fm), give a ratio of $\left(\frac{2.04}{13.40}\right)^2=0.023$, eighty times better, which is why the ordering of β-brass was first measured by neutron diffraction (Chapter 43). For Ni$_3$Al with X-rays, $(28-13)/(13+3\times28)=0.155$, a ratio of 0.024: the γ′ superlattice reflections are weak but routine.

### Antiphase boundaries

Ordering nucleates independently in different regions of a crystal. Because the A atoms can choose any one of the equivalent sublattices, neighbouring ordered regions may be perfectly aligned crystallographically yet out of step in their A–B sequence. Where they meet, an **antiphase boundary** (APB) forms: a surface across which A atoms face A atoms and B face B, with a displacement between the domains equal to a vector of the disordered lattice that is not a vector of the ordered one ($\tfrac12\langle110\rangle$ in L1$_2$, $\tfrac12\langle111\rangle$ in B2). An ordered alloy that nucleated from many points becomes a mosaic of **antiphase domains**; their number of distinct translational variants equals the ratio of the volume of the ordered primitive cell to that of the disordered one: 4 for L1$_2$, 2 for B2.

APBs cost energy, because they create wrong A–A and B–B bonds; typical APB energies are 0.1–0.3 J m$^{-2}$ for Ni$_3$Al on $\{111\}$. They are also created whenever a dislocation of the disordered lattice passes through an ordered crystal: its Burgers vector shifts the sublattices. A single such dislocation would leave a sheet of APB behind it, so dislocations in ordered alloys (Figure 3.5) travel in pairs, **superdislocations**, the second restoring order behind the first. This is the central mechanism of precipitation strengthening by γ′ and of the anomalous rise in strength of Ni$_3$Al with temperature (Chapters 12, 13 and 16).

<!-- FIGURE 3.5 | figures/ch03/fig-3-5-ordering-apb.png | crystal | Order–disorder in alloys: the L1₂ and B2 superlattices, an antiphase boundary, and superlattice reflections in diffraction. | Content: (a) disordered FCC cell with all sites half-shaded (mixed Cu/Au) beside ordered L1₂ Cu3Au cell (Au corners gold, Cu face centres copper colour). (b) disordered BCC beside ordered B2 CuZn (Cu corners, Zn body centre). (c) 2D square-lattice section of an ordered AB alloy with two antiphase domains; boundary drawn where A–A and B–B nearest-neighbour pairs occur, highlighted in red; displacement vector ½<110> arrow; label "APB energy ≈ 0.1–0.3 J/m² (Ni3Al)". (d) schematic powder diffraction patterns, 2θ from 20° to 80° (Cu Kα) for Cu3Au, a = 0.375 nm: disordered (only 111, 200, 220, 311, 222 peaks) and ordered (additional weak 100, 110, 210, 211 superlattice peaks at about 9 % relative intensity), with "S = 1" and "S = 0" labels. -->

### Artificial superlattices

The word superlattice is also used for **artificial multilayers**: periodic stacks of two materials deposited layer by layer, such as GaAs/AlAs in quantum-cascade lasers, Co/Pt and Fe/Cr in magnetic devices (the Fe/Cr multilayers in which giant magnetoresistance was discovered), and TiN/NbN or TiN/AlN hard coatings, whose hardness peaks at bilayer periods of a few nanometres because dislocations cannot cross the many coherent interfaces. They impose a new, longer period on the parent lattice exactly as chemical ordering does, and they too produce satellite reflections around the fundamental Bragg peaks.

---

## 3.8 Quasicrystals and incommensurate structures

### Quasicrystals

Section 3.2 proved that a periodic crystal cannot have fivefold symmetry, yet Shechtman's Al–Mn alloys gave sharp diffraction spots with icosahedral symmetry (Chapter 2). The resolution is that sharp diffraction requires *long-range order*, not periodicity. A quasicrystal is **quasiperiodic**: its structure can be generated as a three-dimensional slice through a periodic lattice in six-dimensional space (for icosahedral quasicrystals) or five dimensions (for decagonal ones, which are periodic in one direction and quasiperiodic in the plane perpendicular to it). Because the slice is at an irrational angle to the higher-dimensional lattice, the pattern never repeats, but every local configuration recurs infinitely often.

The two-dimensional model is the **Penrose tiling** (Figure 3.6a), made from a "fat" rhombus (angles 72° and 108°) and a "thin" rhombus (36° and 144°) assembled under matching rules. Its local fivefold symmetry and its scaling properties involve the golden ratio:

$$
\tau=\frac{1+\sqrt5}{2}=1.6180\ldots,\qquad \tau^2=\tau+1
$$

The ratio of fat to thin tiles tends to $\tau$, and the pattern is self-similar under scaling by $\tau$. The one-dimensional analogue, the Fibonacci chain of long (L) and short (S) segments generated by repeatedly replacing L → LS and S → L, makes the point most simply: the numbers of L and S segments are successive Fibonacci numbers, their ratio converges to $\tau$ (after 15 generations it is 1.618034, against $\tau=1.618034$), and the chain is ordered but never periodic. Diffraction from such structures gives sharp peaks indexed by six integers (icosahedral) instead of three, with intensities forming self-similar patterns related by powers of $\tau$.

Hundreds of stable quasicrystals are now known, in Al–Cu–Fe, Al–Pd–Mn, Zn–Mg–RE, Ti–Zr–Ni and other systems; a natural one was found in a meteorite. Their properties reflect their unusual structure: high hardness, low friction and surface energy (hence non-stick and wear-resistant coatings), low thermal and electrical conductivity for metallic alloys, and brittleness at room temperature. Closely related **approximants** are periodic crystals with very large cells whose local structure mimics the quasicrystal; they bridge the two descriptions.

<!-- FIGURE 3.6 | figures/ch03/fig-3-6-quasicrystal-modulated.png | schematic | Order without periodicity: a Penrose tiling and its tenfold diffraction pattern, the Fibonacci chain, and an incommensurately modulated structure with its satellite reflections. | Content: (a) Penrose rhombus tiling patch (~150 tiles), fat rhombi (72°/108°) light blue, thin rhombi (36°/144°) dark blue, a local fivefold star highlighted; label "fat/thin → τ = 1.618". (b) Calculated diffraction pattern of the tiling: sharp spots with tenfold symmetry, intensities as dot sizes, rings of spots whose radii scale by τ. (c) 1D Fibonacci chain L S L L S L S L L S L L S ... generated by L → LS, S → L, with its construction as a cut through a 2D square lattice at slope 1/τ (strip-projection sketch). (d) 1D chain of atoms with a sinusoidal displacement modulation of wavelength 3.7a (incommensurate), and its diffraction: main reflections at integer h with first- and second-order satellites at h ± q, q = 0.27 a*. -->

### Incommensurate and modulated structures

A second family of ordered but non-periodic solids are **incommensurately modulated structures**. Start from an ordinary crystal (the *basic structure*) and impose a periodic distortion, a displacement of atoms, a variation in site occupancy or a rotation of magnetic moments, whose wavelength is not a rational multiple of the lattice repeat. The modulation wave vector is written

$$
\mathbf q=\alpha\,\mathbf a^*+\beta\,\mathbf b^*+\gamma\,\mathbf c^*
$$

with at least one of $\alpha$, $\beta$, $\gamma$ irrational, where $\mathbf a^*$, $\mathbf b^*$, $\mathbf c^*$ are reciprocal-lattice vectors (Chapter 4). The diffraction pattern then shows the main Bragg reflections of the basic structure surrounded by **satellite reflections** (Figure 3.6d) at $\pm\mathbf q$, $\pm2\mathbf q$, …, all sharp. Such structures are described by **superspace groups** in $(3+d)$ dimensions, where $d$ is the number of independent modulation vectors.

Engineering and scientific examples include:

- **Modulated martensites** in Ni–Mn–Ga magnetic shape-memory alloys (the "5M" and "7M" structures), whose modulation makes twin boundaries so mobile that a magnetic field produces strains of several per cent (Chapter 29);
- the narrow **incommensurate phase of quartz**, about 1.4 K wide, between the α and β forms near 573 °C;
- **charge-density waves** in layered compounds such as NbSe$_2$ and TaS$_2$, and **spin-density waves** and helical magnetic structures in chromium and rare-earth metals;
- **composite (misfit) crystals** in which two interpenetrating substructures have incommensurate repeats along a common direction, as in the misfit-layer sulphides and in the host–guest high-pressure phases of barium and bismuth.

When the modulation locks into a rational value, the structure becomes an ordinary but larger-celled superstructure, a **commensurate** phase; many systems pass through incommensurate phases on the way between two commensurate ones as temperature changes.

> **Status of the principle: the crystal as a solid with essentially discrete diffraction**
> *Empirical.* The 1992 IUCr definition was adopted because experiment found sharp diffraction from quasicrystals and modulated phases; it replaces periodicity, which remains the special case covered by the 230 space groups, with long-range order detectable by diffraction.

Quasicrystals and modulated phases show that the classical crystallography of Sections 3.1–3.4 is the most important special case of a more general idea of order. For the engineer, the classical case covers almost every structural material; the generalization matters for coatings, shape-memory alloys, some magnetic and electronic materials, and the interpretation of unexpected diffraction spots.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are reciprocal lattices, structure factors and systematic absences derived from symmetry, and how are superlattice intensities calculated exactly? | Chapter 4 |
| How do point-group symmetries reduce the number of independent components of conductivity, piezoelectric and elastic tensors? | Chapter 4 |
| How are domain walls, twin boundaries and antiphase boundaries classified among planar defects? | Chapter 5 |
| What thermodynamics controls order–disorder transitions, and why are some continuous and some discontinuous? | Chapter 6 |
| How do martensite variants form and accommodate transformation strain? | Chapter 10 |
| How do superdislocations and APB energy strengthen γ′ and other ordered intermetallics? | Chapters 12, 13 and 16 |
| How do texture and the plastic strain ratio govern formability? | Chapters 13 and 38 |
| How do ferroelectric domains, poling and the morphotropic phase boundary set piezoelectric performance? | Chapter 25 |
| How are shape-memory and magnetic shape-memory alloys designed? | Chapter 29 |
| How are pole figures, ODFs and orientation maps measured in practice? | Chapter 42 |
| How do neutrons and synchrotron X-rays reveal ordering, modulations and light atoms? | Chapter 43 |
| How do electronic-structure and database tools use space groups and Wyckoff positions? | Chapters 45 and 47 |

**Next:** Chapter 4 turns from real space to reciprocal space: the reciprocal lattice, Bragg's law and the Ewald sphere, structure factors and intensities, peak broadening, and the tensor description of properties that symmetry constrains.
