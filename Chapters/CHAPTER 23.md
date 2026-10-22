# Chapter 23 — Laminate Theory, Failure and Composite Manufacturing

*Part V · Polymers and Composites*

A carbon/epoxy panel comes out of the autoclave perfectly flat on one production line and curled like a potato crisp on another. Nothing is wrong with the prepreg, the cure cycle or the tool. On the second line an operator laid the plies in the order 0, 90, 0, 90 instead of 0, 90, 90, 0 — the same plies, the same angles, a different sequence. Elsewhere, a maintenance engineer taps an aircraft panel after a dropped tool and finds nothing visible; a later ultrasonic scan shows a cone of delaminations under the dent that has cut the panel's compressive strength by half. And a wind-turbine blade passes its static test only to crack along its trailing edge, where the skin laminate ends, at loads well below those that any single ply should have carried.

All three problems belong to the laminate, not to the ply. Chapter 22 described a single unidirectional layer. This chapter stacks layers into a structure, finds how the stacking sequence couples stretching, bending, shearing and twisting, predicts when and how laminates fail, follows the damage modes that have no counterpart in metals, and then turns to how composites are actually made — including the metal- and ceramic-matrix composites that carry the ideas into high-temperature service.

> **How does the stacking sequence of plies decide whether a laminate stretches, bends, twists or warps?**
> **How do laminates fail, why do delamination and impact damage matter so much, and how does the manufacturing route set the quality of the part?**

| Concept | Engineering destination |
|---|---|
| Classical laminate theory, ABD matrix | Stiffness of aircraft skins, car body panels, bicycle frames, pressure vessels |
| Symmetric and balanced layups | Warp-free panels, design rules in every aerospace layup |
| Failure criteria and progressive failure | Design allowables, first-ply and last-ply failure, margin of safety |
| Interlaminar stresses, delamination | Edges, holes, ply drops, bonded joints, blade trailing edges |
| Impact damage, compression after impact | Damage-tolerance certification of aircraft and pressure vessels |
| Sandwich structures | Aircraft floors, helicopter blades, boat hulls, wind blades, racing-car monocoques |
| Manufacturing processes | Choosing between hand lay-up, infusion, autoclave, RTM, winding, pultrusion and fibre placement |
| Metal- and ceramic-matrix composites | Brake discs, pistons, electronic baseplates, turbine shrouds, re-entry heat shields |

**Roadmap.** Stacking plies: classical laminate theory and the ABD matrix (23.1) → when plies fail: criteria and progressive failure (23.2) → stresses between plies: free edges and delamination (23.3) → impact damage and compression after impact (23.4) → sandwich structures (23.5) → how polymer composites are made (23.6) → metal- and ceramic-matrix composites (23.7).

---

## 23.1 Classical laminate theory

### Laminate notation

A laminate is described by its ply angles from top to bottom, measured from the structural $x$ axis. Square brackets enclose the sequence; a subscript $s$ means the listed half is mirrored about the mid-plane; a numerical subscript repeats a ply or group; $\pm$ means a $+\theta$ ply followed by a $-\theta$ ply. Thus $[0/\pm45/90]_s$ is the eight-ply sequence $0/45/-45/90/90/-45/45/0$, and $[0_2/90]_s$ is $0/0/90/90/0/0$. Plies of a typical carbon/epoxy prepreg are 0.125–0.25 mm thick; a wing skin may contain 40–150 of them.

### Kinematics: the Kirchhoff hypothesis

**Classical laminate theory** (CLT) treats the laminate as a thin plate and assumes, as in the classical theory of plates (Kirchhoff), that straight lines normal to the mid-plane remain straight and normal after deformation and do not change length. The plies are perfectly bonded, so displacements are continuous through the thickness. Then the in-plane strains at any height $z$ above the mid-plane are

$$
\boldsymbol\varepsilon(z)=\boldsymbol\varepsilon^0+z\,\boldsymbol\kappa
$$

where $\boldsymbol\varepsilon^0=(\varepsilon_x^0,\varepsilon_y^0,\gamma_{xy}^0)$ are the mid-plane strains and $\boldsymbol\kappa=(\kappa_x,\kappa_y,\kappa_{xy})$ the curvatures (bending and twisting). Strain varies linearly and continuously through the thickness. Stress does not: each ply $k$ has its own stiffness $[\bar Q]_k$ (Section 22.7), so stress jumps at every ply interface,

$$
\boldsymbol\sigma_k(z)=[\bar Q]_k\left(\boldsymbol\varepsilon^0+z\,\boldsymbol\kappa\right)
$$

### Force and moment resultants; the ABD matrix

Integrating stresses through the thickness $h$ gives force resultants $\mathbf N$ (force per unit width, N/mm) and moment resultants $\mathbf M$ (moment per unit width, N mm/mm):

$$
\mathbf N=\int_{-h/2}^{h/2}\boldsymbol\sigma\,dz,\qquad \mathbf M=\int_{-h/2}^{h/2}\boldsymbol\sigma\,z\,dz
$$

Substituting the ply stresses and summing over plies with interfaces at $z_{k-1}$ and $z_k$ gives the constitutive law of the laminate:

$$
\begin{pmatrix}\mathbf N\\ \mathbf M\end{pmatrix}=\begin{pmatrix}[A] & [B]\\ [B] & [D]\end{pmatrix}\begin{pmatrix}\boldsymbol\varepsilon^0\\ \boldsymbol\kappa\end{pmatrix}
$$

$$
A_{ij}=\sum_k(\bar Q_{ij})_k(z_k-z_{k-1}),\quad B_{ij}=\tfrac12\sum_k(\bar Q_{ij})_k(z_k^2-z_{k-1}^2),\quad D_{ij}=\tfrac13\sum_k(\bar Q_{ij})_k(z_k^3-z_{k-1}^3)
$$

$[A]$ is the **extensional stiffness**, $[D]$ the **bending stiffness**, and $[B]$ the **coupling stiffness** between them. The $6\times6$ **ABD matrix** is the central object of composite design: every finite-element shell element for composites computes it.

> **Status of the principle: Classical laminate theory**
> *Approximate.* Exact within linear elasticity for a thin plate under the Kirchhoff assumptions and perfect bonding; it ignores transverse shear deformation (important for thick laminates and sandwich panels, handled by first-order shear deformation theory) and cannot predict the interlaminar stresses at free edges (Section 23.3).

Figure 23.1 shows the geometry and resultants.

<!-- FIGURE 23.1 | figures/ch23/fig-23-1-laminate-geometry.png | schematic | Laminate geometry in classical laminate theory: ply numbering and z-coordinates, linear strain and piecewise-constant stress through the thickness, and the force and moment resultants. | Content: left: exploded stack of eight plies [0/±45/90]_s, each with fibre lines at its angle, z-axis pointing down through the stack, mid-plane dashed, interface coordinates z_0 = −h/2 … z_8 = +h/2 labelled. Centre: through-thickness plot of strain ε_x(z) under combined stretching and bending (straight inclined line). Right: through-thickness plot of σ_x(z) for the same deformation, jumping at each ply interface (large in 0° plies, small in 90° plies, intermediate in ±45°). Bottom: small plate element with N_x, N_y, N_xy arrows on edges and M_x, M_y, M_xy double-headed moment arrows, units N/mm and N mm/mm. -->

### Coupling and how to avoid it

The terms of $[A]$, $[B]$ and $[D]$ that would be zero for an isotropic plate describe coupling between deformation modes:

- $A_{16}$, $A_{26}$: **extension–shear** coupling. A tensile $N_x$ produces shear strain $\gamma_{xy}^0$.
- $B_{ij}$: **extension–bending** coupling. In-plane loads, including thermal loads, produce bending and twisting.
- $D_{16}$, $D_{26}$: **bend–twist** coupling. A bending moment produces twist.

Three layup rules control them:

- A **symmetric** laminate (ply angles and materials mirrored about the mid-plane) has $[B]=0$. Every term in the $B$ sum from a ply above the mid-plane is cancelled by its mirror image below. This is why the operator who laid $0/90/0/90$ instead of $0/90/90/0$ got a curled panel: that sequence is unsymmetric, and the thermal contraction on cool-down from cure bent it.
- A **balanced** laminate (every $+\theta$ ply has a $-\theta$ ply of the same material and thickness, anywhere in the stack) has $A_{16}=A_{26}=0$, because $\bar Q_{16}$ and $\bar Q_{26}$ are odd functions of $\theta$.
- $D_{16}$ and $D_{26}$ vanish only if each $+\theta$ ply has a $-\theta$ ply at the same distance from the mid-plane on the same side, which is impossible in a symmetric laminate. They can be made small by interleaving many $\pm\theta$ pairs, or eliminated by antisymmetric layups that sacrifice $B=0$. Most aerospace laminates are symmetric and balanced and accept small bend–twist terms.

A laminate with equal stiffness in every in-plane direction — **quasi-isotropic** — results from $N\ge3$ ply angles spaced $180°/N$ apart in equal proportions, for example $[0/\pm60]_s$ or $[0/\pm45/90]_s$. Its $[A]$ is isotropic; its $[D]$ is not, because the outer plies dominate bending.

> **Status of the principle: Symmetric and balanced layup rules**
> *Derived.* Direct consequences of the definitions of $[A]$ and $[B]$ and the parity of the transformed stiffnesses; they hold exactly within CLT and are the reason aerospace design manuals require symmetric, balanced laminates unless coupling is wanted.

Figure 23.2 shows what the coupling terms do to a flat plate.

<!-- FIGURE 23.2 | figures/ch23/fig-23-2-laminate-coupling.png | schematic | Coupling effects in laminates: extension–shear in an unbalanced laminate, extension–bending and thermal warping of an unsymmetric laminate, and bend–twist coupling. | Content: three columns. (a) Unbalanced [30]_4 coupon under tension N_x: original rectangle (dashed) and deformed parallelogram showing shear, label "A_16 ≠ 0". (b) Unsymmetric [0/90]_T plate after cooling 150 K from cure: saddle/cylindrical curvature with radius ≈ 98 mm for 0.25 mm total thickness, label "B ≠ 0: thermal warping"; beside it a flat [0/90]_s plate, label "symmetric: B = 0". (c) Cantilever [+30/−30/+30/−30]-type strip under tip bending load showing tip twist, label "D_16 ≠ 0: bend–twist coupling (aeroelastic tailoring)". -->

**Worked example — ABD matrices of three carbon/epoxy laminates.** Use T300/epoxy plies (Table 22.3: $Q_{11}=181.8$, $Q_{22}=10.35$, $Q_{12}=2.90$, $Q_{66}=7.17$ GPa) of thickness 0.125 mm.

*Cross-ply $[0/90]_s$*, $h=0.5$ mm. Each orientation occupies 0.25 mm, so $A_{11}=A_{22}=0.25\times(181.8+10.35)=48.0\times10^3$ N/mm, $A_{12}=0.5\times2.90=1.45\times10^3$ N/mm, $A_{66}=0.5\times7.17=3.59\times10^3$ N/mm, and $A_{16}=A_{26}=0$, $[B]=0$. Inverting $[A]$ gives the effective in-plane moduli $E_x=1/(h\,a_{11})$ etc. (with $a=A^{-1}$): $E_x=E_y=96.0$ GPa, $G_{xy}=7.17$ GPa and $\nu_{xy}=0.030$. The cross-ply is stiff along both axes but no stiffer in shear than a single ply. The bending stiffnesses are very different: $D_{11}=1671$ N mm but $D_{22}=331$ N mm, because the 0° plies are on the outside.

*Quasi-isotropic $[0/\pm45/90]_s$*, $h=1.0$ mm. The calculation gives $A_{11}=A_{22}=76.4\times10^3$, $A_{12}=22.6\times10^3$, $A_{66}=26.9\times10^3$ N/mm, hence $E_x=E_y=69.7$ GPa, $G_{xy}=26.9$ GPa and $\nu_{xy}=0.296$. Check: $E/[2(1+\nu)]=69.7/2.592=26.9$ GPa, as for an isotropic material. A quasi-isotropic CFRP laminate is as stiff as aluminium (70 GPa) at 58 % of its density (1.60 against 2.70 g/cm³). But its bending stiffnesses are $D_{11}=10{,}690$, $D_{22}=2{,}653$ and $D_{16}=D_{26}=670$ N mm — the outer 0° plies dominate, and the bend–twist terms are 6 % of $D_{11}$.

*Unsymmetric $[0/90]_T$*, $h=0.25$ mm. Now $B_{11}=-1340$ N and $B_{22}=+1340$ N: stretching causes bending. Cooling from a stress-free temperature 150 K above room temperature (with $\alpha_1=0.02$ and $\alpha_2=22.5$ ppm/K) produces thermal force and moment resultants; solving the full ABD system gives curvatures $\kappa_x=-0.0102$ and $\kappa_y=+0.0102$ mm⁻¹: a radius of curvature of 98 mm, and a 100 mm wide panel deflects about 13 mm at mid-span. In practice such thin unsymmetric plates snap into one of two cylindrical shapes rather than a saddle — they are **bistable**, a property exploited in morphing structures.

### Thermal and hygral loads in laminates

Each ply wants its free thermal strain $\boldsymbol\alpha_k\Delta T$ (Section 22.8), but the plies are bonded. CLT handles this by defining thermal resultants

$$
\mathbf N^T=\sum_k[\bar Q]_k\boldsymbol\alpha_k\Delta T\,(z_k-z_{k-1}),\qquad \mathbf M^T=\tfrac12\sum_k[\bar Q]_k\boldsymbol\alpha_k\Delta T\,(z_k^2-z_{k-1}^2)
$$

which are added to the mechanical loads. The laminate deforms to a compromise strain, and each ply is left with a **residual stress** $[\bar Q]_k(\boldsymbol\varepsilon^0+z\boldsymbol\kappa-\boldsymbol\alpha_k\Delta T)$. Moisture enters identically, with $\boldsymbol\beta\Delta M$ in place of $\boldsymbol\alpha\Delta T$. The laminate CTE follows from the same equations with $\mathbf N=\mathbf 0$: for T300/epoxy both $[0/90]_s$ and $[0/\pm45/90]_s$ have $\alpha_x=\alpha_y=1.5$ ppm/K, while a 0°-dominated $[0/\pm30/0]_s$ has $\alpha_x=-1.0$ ppm/K along its axis — the basis of near-zero-expansion structures for satellites and optical instruments.

---

## 23.2 Failure criteria and progressive ply failure

### Why composite failure is hard

A metal yields by one mechanism, and an isotropic criterion (Tresca or von Mises, Chapter 13) handles any combination of stresses. A ply has at least five strengths ($X_t$, $X_c$, $Y_t$, $Y_c$, $S$) that differ by factors of up to 40, and several physically distinct failure modes: fibre fracture in tension, fibre kinking in compression, matrix cracking in transverse tension, shear failure, and matrix crushing in transverse compression. A laminate fails progressively: one ply cracks, its load is redistributed, another fails, and so on. Failure criteria are applied **ply by ply**, in material axes, to the stresses from CLT.

### Maximum stress and maximum strain

The simplest criterion compares each stress component with its strength separately: failure when any of

$$
\frac{\sigma_1}{X_t\ \mathrm{or}\ X_c},\qquad \frac{\sigma_2}{Y_t\ \mathrm{or}\ Y_c},\qquad \frac{\lvert\tau_{12}\rvert}{S}
$$

reaches 1. The **maximum stress** criterion identifies the failure mode directly, which is its great advantage, but ignores interaction: a ply under combined transverse tension and shear fails earlier than either alone. The **maximum strain** criterion does the same with strains and differs slightly through Poisson effects; it is widely used in aerospace practice, where allowable strains (for example 3,000–4,000 microstrain in compression after impact, Section 23.4) are the design currency.

### Tsai–Hill

**Tsai–Hill** adapts Hill's anisotropic yield criterion (Chapter 13) to a transversely isotropic ply under plane stress:

$$
\frac{\sigma_1^2}{X^2}-\frac{\sigma_1\sigma_2}{X^2}+\frac{\sigma_2^2}{Y^2}+\frac{\tau_{12}^2}{S^2}=1
$$

with $X$ and $Y$ chosen as tensile or compressive according to the sign of the stress. It is a single smooth function, gives good predictions for off-axis strength, but cannot say which mode failed and treats unlike mechanisms (fibre fracture, matrix cracking) as if they interacted like components of one yield process. For a T300/epoxy ply loaded uniaxially at an angle $\theta$, substituting $\sigma_1=\sigma c^2$, $\sigma_2=\sigma s^2$, $\tau_{12}=-\sigma sc$ gives strengths of 1,500 MPa at 0°, 690 at 5°, 245 at 15°, 112 at 30°, 69 at 45° and 40 MPa at 90°: the ply loses 84 % of its strength at only 15° off-axis.

### Tsai–Wu

**Tsai–Wu** writes a general quadratic polynomial in stress, the most general form invariant under coordinate rotation:

$$
F_1\sigma_1+F_2\sigma_2+F_{11}\sigma_1^2+F_{22}\sigma_2^2+F_{66}\tau_{12}^2+2F_{12}\sigma_1\sigma_2=1
$$

with $F_1=1/X_t-1/X_c$, $F_{11}=1/(X_tX_c)$, $F_2=1/Y_t-1/Y_c$, $F_{22}=1/(Y_tY_c)$, $F_{66}=1/S^2$. The linear terms capture the different tensile and compressive strengths. The interaction coefficient $F_{12}$ should come from a biaxial test, which is difficult; in practice $F_{12}=-\tfrac12\sqrt{F_{11}F_{22}}$ is used, which makes the failure surface an ellipsoid resembling von Mises. The **strength ratio** $R$, the factor by which the applied stresses must be multiplied to reach failure, is the positive root of $aR^2+bR-1=0$, where $a$ collects the quadratic and $b$ the linear terms.

> **Status of the principle: Tsai–Hill and Tsai–Wu criteria**
> *Empirical.* Phenomenological surfaces fitted to uniaxial (and occasionally biaxial) strengths, with no reference to failure mechanism; they work well in tension-dominated regimes and for off-axis plies but can be non-conservative under biaxial compression and give spurious interaction between fibre and matrix modes. The World-Wide Failure Exercise (1996–2012) found none of the classical criteria reliable in every case.

### Puck: mechanism-based criteria

The **Puck** criterion, the best performer in the World-Wide Failure Exercise and the basis of VDI 2014 guidelines, separates the mechanisms. **Fibre fracture** is checked with a fibre-direction criterion (essentially maximum stress or strain in $\sigma_1$, corrected for transverse stresses). **Inter-fibre fracture** (matrix cracking) is treated as Mohr–Coulomb-type fracture on an inclined **action plane** parallel to the fibres: the criterion searches the angle of that plane, and the normal and shear stresses on it decide failure. Transverse compression raises the shear strength on the plane (friction) instead of lowering it, and fracture is classified into **modes A, B and C**. Mode C, with fracture planes inclined at about 50° under high transverse compression, produces wedge-shaped fragments that can split adjacent plies, and is flagged as particularly dangerous. **LaRC** criteria (NASA) extend the same physical approach to fibre kinking. Mechanism-based criteria are more work to implement but tell the designer what will fail, which is what damage-tolerance and progressive-failure analysis need.

Figure 23.3 compares the envelopes.

<!-- FIGURE 23.3 | figures/ch23/fig-23-3-failure-envelopes.png | plot | Failure envelopes of a T300/epoxy ply in the σ1–σ2 plane (τ12 = 0) and off-axis uniaxial strength versus angle, for the maximum stress, Tsai–Hill and Tsai–Wu criteria. | Content: left panel: x-axis σ1 −1800 to +1800 MPa, y-axis σ2 −300 to +100 MPa (note very different scales). Strengths X_t = X_c = 1500, Y_t = 40, Y_c = 246 MPa. Maximum-stress rectangle; Tsai–Hill piecewise ellipse; Tsai–Wu ellipse (F12 = −½√(F11F22)), shifted towards compression in σ2. Label quadrants. Right panel: x-axis θ 0–90°, y-axis strength 10–2000 MPa on log scale: Tsai–Hill (1500 at 0°, 690 at 5°, 370 at 10°, 245 at 15°, 112 at 30°, 69 at 45°, 50.5 at 60°, 40 at 90°) and maximum stress (1500, 783, 398, 272, 157, 80, 53, 40) with regions labelled "fibre", "shear", "transverse" for the max-stress mode. -->

### First-ply failure, last-ply failure and residual stress

In a laminate the first ply to fail rarely ends the laminate's life. **First-ply failure** (FPF) is usually transverse matrix cracking in the plies most nearly perpendicular to the load. The cracks multiply, the cracked plies lose transverse and shear stiffness, and their load is shed to neighbours. **Last-ply failure** (LPF) is fibre fracture in the load-aligned plies. Progressive failure analysis follows this sequence by **ply discount**: when a ply fails in a matrix mode its $E_2$ and $G_{12}$ are reduced (to zero or to a small fraction), the ABD matrix is recomputed and the load increased again. Continuum damage mechanics replaces the sudden discount with gradual stiffness degradation driven by damage variables, and is the basis of modern finite-element progressive damage models.

**Worked example — First- and last-ply failure of a cross-ply.** A T300/epoxy $[0/90]_s$ laminate ($h=0.5$ mm) carries a tensile load $N_x$. Under $N_x=1$ N/mm (average stress 2 MPa), CLT gives ply stresses of $\sigma_1=3.786$, $\sigma_2=0.054$ MPa in the 0° plies and $\sigma_1=-0.054$, $\sigma_2=0.214$ MPa in the 90° plies.

*Without residual stress.* The 90° plies crack in transverse tension when $0.214N_x=Y_t=40$ MPa, so $N_x=187$ N/mm, an average laminate stress of 374 MPa (Tsai–Wu gives 373 MPa). The 0° plies reach $X_t$ at $N_x=1500/3.786=396$ N/mm (792 MPa).

*With cure residual stress.* The laminate was cured at 177 °C; take the stress-free temperature as 150 K above room temperature. Cooling leaves every ply with $\sigma_1=-31.9$ MPa and $\sigma_2=+31.9$ MPa: the plies want to shrink across their fibres by $22.5\times150=3{,}375$ microstrain but are held by their neighbours' fibres. The residual transverse stress alone uses 80 % of $Y_t$. The 90° plies now crack when $31.9+0.214N_x=40$, at $N_x=37.9$ N/mm — an average stress of only 76 MPa (Tsai–Wu: 73 MPa), a fifth of the value without residual stress.

*After first-ply failure.* The 90° plies are discounted; the laminate modulus drops only slightly (from 96 to about 91 GPa), because the 90° plies contributed little along $x$. The laminate keeps carrying load until the 0° plies break at a fibre strain of about $1500/181{,}000=0.83$ %, an average stress of roughly 750–790 MPa. So the laminate's first-ply failure is at about a tenth of its ultimate strength.

Two lessons follow. First, residual cure stresses are not a correction but often the largest single term in matrix-cracking predictions; that is why aerospace resins were toughened in the 1980s and why thin plies, which resist transverse cracking better than thick ones (the **in-situ strength** effect, which can raise effective $Y_t$ by 50–100 % in plies 0.1 mm thick), are favoured. Second, matrix cracks are not structurally fatal in tension, but they open paths for moisture and fuel, lower compressive and shear stiffness, and initiate delaminations; pressure vessels and fuel tanks are therefore often designed to first-ply failure, primary structure to ultimate. Figure 23.4 shows the load–strain record.

<!-- FIGURE 23.4 | figures/ch23/fig-23-4-progressive-failure.png | plot | Progressive failure of a T300/epoxy [0/90]s laminate in tension, with and without cure residual stress. | Content: x-axis laminate strain ε_x 0–0.9 %; y-axis average laminate stress 0–850 MPa. Curve: linear slope 96 GPa; first-ply failure marked at 76 MPa (ε ≈ 0.08 %) for the laminate with residual stress (ΔT = −150 K), and alternative FPF marker at 374 MPa (ε ≈ 0.39 %) for the hypothetical stress-free laminate; after FPF a slightly reduced slope ≈ 91 GPa; final failure (last-ply failure, 0° fibre fracture) at about 760 MPa and ε ≈ 0.83 %. Small inset: edge view of the laminate showing transverse cracks multiplying in the inner 90° plies with increasing load (crack spacing decreasing), label "matrix crack saturation". -->

---

## 23.3 Interlaminar stresses, free edges and delamination

### What CLT cannot see

CLT assumes plane stress in each ply: $\sigma_z=\tau_{xz}=\tau_{yz}=0$. At a **free edge** — the side of a coupon, the bore of a hole, a cut-out, a ply drop, the end of a bonded doubler — this cannot hold. Consider a $[\pm45]_s$ coupon in tension. CLT says each ply carries an in-plane shear stress $\tau_{xy}$ of opposite sign in the $+45$ and $-45$ plies. At the free edge $y=\pm b$, that shear must vanish (the edge is traction-free). The only way for the ply to shed it is to transfer it, through **interlaminar shear stress** $\tau_{xz}$, to the neighbouring ply over a **boundary layer** about one laminate thickness wide. Pipes and Pagano (1970) showed by finite differences that this interlaminar stress is singular at the edge of the interface in the elastic solution.

The same logic applies to Poisson mismatch. In a $[0/90]_s$ laminate in tension the 0° plies want to contract across their width far more ($\nu_{12}=0.28$) than the 90° plies ($\nu_{21}=0.016$). In the interior they are forced to a common strain; at the free edge the forces that enforce it must be transmitted by interlaminar stresses, and they also produce a moment that gives an **interlaminar normal stress** $\sigma_z$ — peeling stress — at the mid-plane.

> **Status of the principle: Free-edge interlaminar stresses**
> *Derived.* A consequence of three-dimensional elasticity at a traction-free boundary of a laminate with ply-to-ply mismatch in Poisson's ratio or in shear coupling; the elastic solution is singular at the interface corner, so design uses averaged stresses over a characteristic distance or fracture mechanics rather than point values.

### Stacking sequence controls the sign of $\sigma_z$

The interlaminar normal stress depends on the stacking sequence, not just on the plies present. For a laminate containing ±θ and 90° plies loaded in tension, the outer ±θ plies want to contract across the width far more than the 90° plies (a ±30° carbon/epoxy pair has an effective Poisson's ratio above 1). In the sequence $[\pm\theta/90]_s$ the resulting edge moment produces tensile $\sigma_z$ at the mid-plane; moving the 90° plies outside, $[90/\pm\theta]_s$, reverses it to compression. Tensile peel stress opens delaminations; compressive stress suppresses them. The two layups are identical in CLT, yet the first delaminates at much lower load — so reliably that the standard edge-delamination test uses a $[\pm30/\pm30/90/\bar{90}]_s$ coupon precisely to make the mid-plane delaminate under tension. Design rules follow: avoid grouping many plies of the same angle (which raises interlaminar stresses and lowers in-situ strength), avoid blocks of 90° plies at the mid-plane beneath ±θ plies in tension-loaded laminates, terminate dropped plies gradually (ply-drop ratios of 1:20 or more), and protect free edges with edge caps, stitching or tapering.

### Delamination as a fracture problem

**Delamination** — separation between plies — is the most characteristic damage mode of laminated composites, because the interlaminar region is pure matrix with no fibres crossing it. It is treated by fracture mechanics (Chapter 14) with the energy release rate $G$ partitioned into **mode I** (opening), **mode II** (in-plane shear) and **mode III** (tearing). Interlaminar toughness is measured with standard tests: the double-cantilever beam (DCB) for $G_{Ic}$, the end-notched flexure (ENF) for $G_{IIc}$ and the mixed-mode bending (MMB) test for combinations.

**Table 23.1 — Interlaminar fracture toughness of carbon-fibre laminates (typical values).**

| Matrix | $G_{Ic}$ (kJ/m²) | $G_{IIc}$ (kJ/m²) | Typical use |
|---|---|---|---|
| Untoughened epoxy (1970s, e.g. 5208 type) | 0.08–0.2 | 0.3–0.6 | Early military aircraft |
| Toughened epoxy (thermoplastic-modified, interleaved) | 0.3–0.6 | 1.0–2.5 | 787/A350 primary structure |
| Bismaleimide | 0.15–0.4 | 0.5–1.2 | High-temperature fighter structure |
| PEEK/PEKK (thermoplastic) | 1.2–2.0 | 1.5–2.5 | Brackets, clips, welded structures |

Mode II toughness is several times mode I, which is why delaminations grow most easily under peel and why bonded and co-cured joints are designed to minimize peel stress. Numerically, delamination growth is predicted with the **virtual crack closure technique** (VCCT) or with **cohesive-zone elements** placed between plies, whose traction–separation law is calibrated so that its area equals $G_c$. Through-thickness reinforcement — stitching, tufting, z-pins, and 3D weaving — raises $G_{Ic}$ several-fold by bridging the crack, at some cost in in-plane properties.

<!-- FIGURE 23.5 | figures/ch23/fig-23-5-free-edge-and-impact.png | schematic | Interlaminar stresses near a laminate free edge, and the internal damage under a low-velocity impact. | Content: left: cut-away of a [±45]_s coupon in tension: in-plane shear τ_xy of each ply constant across the width in the interior and dropping to zero at the free edge over a boundary layer of width ≈ h; interlaminar shear τ_xz rising sharply at the +45/−45 interface near the edge (plotted against y/b from 0 to 1). Below: mid-plane σ_z versus y/b near the edge for [±30/90]_s (tensile at the edge, labelled "delamination-prone") versus [90/±30]_s (compressive). Right: cross-section through an impacted quasi-isotropic laminate, 4–6 mm thick: small surface dent at top (≈0.3 mm, "barely visible"), conical array of delaminations widening towards the back face (each interface delamination shaped like a peanut aligned with the ply below), matrix cracks linking them, back-face fibre splitting. Inset C-scan plan view of the projected delamination area (≈ 25–40 mm across) much larger than the dent. -->

---

## 23.4 Impact damage and compression after impact

### Barely visible impact damage

A metal panel hit by a dropped tool dents and the dent is visible. A carbon/epoxy panel hit with the same energy may show almost nothing on the surface, while inside, a cone of delaminations has formed (Figure 23.5). The mechanism: the contact load bends the laminate locally, shear and bending stresses crack the matrix in the plies, the matrix cracks reach ply interfaces where bending-stiffness mismatch between differently oriented plies drives delaminations, and the delaminations spread outward, each shaped by the orientation of the ply beneath it. The back face may split.

Certification rules define **barely visible impact damage** (BVID), typically a dent 0.25–0.5 mm deep detectable in a general visual inspection, or the damage from an impact energy cutoff (often 35–50 J for aircraft structure, or about 6.7 J per mm of thickness in standard coupon tests). Structure containing BVID must carry ultimate load for the life of the aircraft, because it may never be found. Larger, visible damage must be found and repaired within an inspection interval.

### Compression after impact

Delaminations barely reduce tensile strength, but they are devastating in compression. A delaminated region splits the laminate into thin sublaminates that buckle locally at loads far below the buckling load of the intact plate; the buckled sublaminates drive the delaminations to grow, and the laminate fails. The standard measure is the **compression-after-impact** (CAI) strength from ASTM D7137 or equivalent, on a 150 × 100 mm plate impacted at a specified energy.

**Table 23.2 — Compression after impact of carbon-fibre quasi-isotropic laminates (typical, about 30 J impact on 4–5 mm plate).**

| System | Undamaged compressive strength (MPa) | CAI strength (MPa) | Retention |
|---|---|---|---|
| Untoughened epoxy | 500–600 | 130–180 | 25–35 % |
| Toughened epoxy (current aerospace) | 550–700 | 250–320 | 40–55 % |
| Thermoplastic (PEEK-type) | 550–650 | 280–350 | 50–60 % |

These numbers explain why compression after impact, not static strength, usually sets the design allowables of composite aircraft structure: allowable strains of about 3,000–4,000 microstrain, against a fibre failure strain of 15,000. The improvements came from the matrix and interleaf, not the fibre: toughened resins and interleaved thermoplastic particles raise $G_{IIc}$ and shrink the delaminated area. Damage resistance (how little damage forms) and damage tolerance (how much strength remains) are separate properties; sandwich panels, thin skins and helicopter blades are typically impact-limited, and armour applications exploit the very energy absorption by delamination that aircraft designers try to avoid.

> **Status of the principle: Compression-after-impact allowables**
> *Empirical.* Allowable strains and CAI strengths are established by standard coupon and element tests for each material and layup; analytical models (sublaminate buckling, soft-inclusion models) explain the trends but are not yet trusted for certification without test data.

---

## 23.5 Sandwich structures

### Why separate the faces

Bending stiffness of a plate scales with the cube of its thickness. A **sandwich panel** exploits this by separating two thin, stiff **face sheets** with a thick, light **core**, exactly as the flanges of an I-beam are separated by its web. The faces carry bending as tension and compression; the core carries transverse shear and keeps the faces apart and stable. Cores are honeycombs (aluminium, Nomex aramid paper, thermoplastic), closed-cell foams (PVC, PET, PMI, polyurethane), and end-grain balsa. Applications include aircraft floors, flaps and control surfaces, helicopter rotor blades, boat hulls and decks, wind-turbine blade shells, racing-car monocoques, train and bus panels, and building cladding.

For a sandwich beam of unit width with identical faces of thickness $t_f$ and modulus $E_f$, core thickness $c$, and distance between face centroids $d=c+t_f$, the flexural rigidity per unit width is dominated by the faces:

$$
D\approx\frac{E_ft_fd^2}{2}
$$

and the transverse shear stiffness by the core:

$$
S\approx\frac{G_cd^2}{c}
$$

The deflection of a simply supported beam under a central load $P$ (per unit width) over span $L$ has a bending and a shear part, $w=PL^3/(48D)+PL/(4S)$. The shear term is negligible in solid beams but can dominate in short, thick sandwich beams with soft cores.

> **Status of the principle: Sandwich beam theory**
> *Approximate.* Assumes thin faces carrying only membrane stress, a core carrying only transverse shear, and no core compression; it is accurate for $c/t_f\gtrsim5$ and stiff cores, and is extended by high-order sandwich theories when cores are very soft or loads are concentrated.

**Worked example — Sandwich versus solid plate of equal mass.** Faces are quasi-isotropic CFRP ($E_f=70$ GPa, $\rho=1600$ kg/m³), 1.0 mm thick each; the core is aluminium honeycomb 20 mm thick, density 50 kg/m³, with ribbon-direction shear modulus $G_c=310$ MPa.

Mass per area: $2\times0.001\times1600+0.020\times50=3.2+1.0=4.2$ kg/m².

Sandwich rigidity, with $d=21$ mm: $D=70{,}000\times1.0\times21^2/2=1.54\times10^7$ N mm per mm width.

A solid quasi-isotropic CFRP plate of the same mass is $4.2/1600=2.63$ mm thick, with $D=Et^3/12=70{,}000\times2.63^3/12=1.06\times10^5$ N mm per mm. The sandwich is **146 times stiffer** in bending at the same weight.

Deflection of a 1 m span under $P=1$ N/mm: bending $10^9/(48\times1.54\times10^7)=1.35$ mm; core shear $S=310\times21^2/20=6{,}836$ N/mm, so shear deflection $1000/(4\times6836)=0.037$ mm. The solid plate would deflect 197 mm. At a 0.3 m span the shear part rises to 23 % of the total.

Strength: the face stress is $M/(t_fd)=PL/(4t_fd)=11.9$ MPa per N/mm of load, and the core shear stress is $P/(2d)=0.024$ MPa per N/mm. Against a face compressive allowable of 500 MPa and a core shear strength of about 2.2 MPa, the panel fails by face failure at $P\approx42$ N/mm before the core shears at 92 N/mm.

### Sandwich failure modes

A sandwich can fail in more ways than a solid beam: **face yielding or fracture**; **core shear failure**; **face wrinkling**, a short-wavelength local buckling of the compressed face on its elastic core, approximately at

$$
\sigma_{\mathrm{wr}}\approx0.5\,(E_fE_cG_c)^{1/3}
$$

(about 280 MPa for CFRP faces on an 80 kg/m³ PVC foam with $E_c=97$ MPa and $G_c=27$ MPa — below the face strength, so foam-cored panels are often wrinkling-limited); **intracell dimpling** of thin faces over large honeycomb cells; **core crushing** under local loads; and **face–core debonding**, which is a delamination problem with the added hazard of water ingress into honeycomb. Inserts, edge closures and ply ramps are where most sandwich structures fail in practice. Figure 23.6 summarizes the construction and the modes.

<!-- FIGURE 23.6 | figures/ch23/fig-23-6-sandwich-failure-modes.png | schematic | A sandwich beam in three-point bending and its failure modes. | Content: top: sandwich beam, faces t_f = 1 mm CFRP, core c = 20 mm honeycomb, span L, central load P; through-thickness distributions of bending normal stress (concentrated in faces, near zero in core) and shear stress (nearly uniform in core). Annotate D ≈ E_f t_f d²/2 and S ≈ G_c d²/c. Bottom row of six small sketches: face fracture (tension face), face wrinkling (short-wave buckles of the compression face into the core), intracell dimpling (face buckling into honeycomb cells), core shear failure (45° cracks in core), core indentation under the load, face–core debond. Small bar inset: equal-mass bending stiffness, sandwich 146 × solid 2.63 mm plate. -->

---

## 23.6 Manufacturing polymer-matrix composites

### What processing must achieve

Every composite process must do four things: place fibres in the right orientation, impregnate them fully with matrix, consolidate the stack to the target fibre volume fraction with minimal voids, and cure or solidify the matrix. Each process strikes a different balance between part size, quality, rate and cost. The processing defects that matter most are **voids** (each 1 % of porosity costs about 5–10 % of interlaminar shear strength), **fibre waviness and wrinkles** (which cut compressive strength, Section 22.3), **resin-rich and resin-starved regions**, **incomplete cure**, **residual stress and distortion** (spring-in of angled parts, typically 0.5–2° for carbon/epoxy), and **dry spots** in liquid-moulded parts.

### Open-mould processes

**Hand lay-up and spray-up** are the oldest: dry fabric or chopped glass is placed on a single-sided mould and wetted out with polyester or vinyl ester by roller or spray gun, and cured at room temperature. Tooling is cheap and part size is unlimited (boat hulls, swimming pools, tanks), but $V_f$ is only 0.20–0.40, quality depends on the operator, and styrene emissions are a health and environmental concern. **Vacuum bagging** consolidates a wet lay-up under atmospheric pressure, and **vacuum infusion** (VARTM) draws resin through a dry preform under a bag — the standard process for wind-turbine blades, boat hulls and bridge decks, achieving $V_f$ of 0.50–0.58 with low emissions.

### Prepreg and autoclave

**Prepreg** is fibre pre-impregnated with partially reacted (B-staged) resin, supplied as tape or fabric on rolls and stored frozen. Plies are cut, laid up on a tool, bagged and cured in an **autoclave** — a heated pressure vessel — typically at 120–180 °C and 0.6–0.7 MPa for 2–6 hours. The pressure collapses voids and suppresses volatile nucleation; the result is $V_f$ of 0.55–0.65 and porosity below 1 %, the reference quality for primary aircraft structure. The costs are high: autoclaves for wing skins exceed 30 m in length, frozen-storage and out-time limits apply, and cycle times are long. **Out-of-autoclave** prepregs, designed with dry channels for air evacuation, achieve near-autoclave quality under vacuum alone.

### Liquid moulding: RTM

**Resin transfer moulding** (RTM) injects resin into a dry fibre preform held in a closed, matched mould. Flow through the preform follows **Darcy's law**,

$$
\mathbf u=-\frac{K}{\mu}\nabla p
$$

with $\mathbf u$ the superficial velocity, $K$ the preform permeability (typically $10^{-11}$–$10^{-9}$ m²), $\mu$ the resin viscosity and $p$ the pressure. For one-dimensional filling from a line gate at constant injection pressure $\Delta p$, a flow front advances as $\sqrt t$ and the fill time for a length $L$ is

$$
t_{\mathrm{fill}}=\frac{\phi\mu L^2}{2K\Delta p}
$$

where $\phi=1-V_f$ is the preform porosity.

> **Status of the principle: Darcy's law for preform impregnation**
> *Empirical.* A linear relation between flow rate and pressure gradient for slow viscous flow through porous media, confirmed for fibre preforms at the low Reynolds numbers of moulding; the permeability is anisotropic, depends strongly on $V_f$ (Kozeny–Carman) and on preform shearing, and capillary and dual-scale (intra-tow) flow cause deviations that produce voids.

**Worked example — How long does a mould take to fill?** An RTM panel 1 m long with $V_f=0.5$ ($\phi=0.5$), preform permeability $K=1\times10^{-10}$ m², resin viscosity 0.1 Pa s and injection pressure 0.5 MPa: $t=0.5\times0.1\times1^2/(2\times10^{-10}\times5\times10^5)=500$ s, about 8 minutes. The same preform infused under vacuum ($\Delta p=0.1$ MPa) with a resin of 0.2 Pa s and a more permeable flow medium ($K=2\times10^{-10}$ m²) takes 2,500 s; a 3 m flow length takes $9\times$ longer, 22,500 s or more than 6 hours — longer than the pot life of many resins. The $L^2$ scaling is why large infusions use distribution media and multiple gates, and why fast-curing automotive RTM uses high pressure (5–15 MPa) and very low viscosity resins to fill in under a minute.

### Continuous processes: filament winding and pultrusion

**Filament winding** draws resin-wet fibre tows onto a rotating mandrel along programmed paths, producing pipes, drive shafts, rocket-motor cases and pressure vessels — including Type IV hydrogen tanks for fuel-cell vehicles, which wind carbon fibre over a polymer liner to 70 MPa. For a closed cylinder under internal pressure, the hoop stress is twice the axial stress; fibres alone carry both if wound at the **netting angle** $\theta$ satisfying $\tan^2\theta=2$, that is $\theta=54.7°$ from the axis. Real vessels combine near-hoop and helical layers to the same effect.

**Pultrusion** pulls continuous fibres through a resin bath and a heated die, curing a constant-section profile continuously at 0.2–3 m/min: ladder rails, bridge decks, rebar, wind-blade spar caps, window frames. It achieves the highest $V_f$ (up to 0.70) and the lowest cost per kilogram of continuous-fibre composite, but the fibres are mostly axial and the section must be constant.

### Automated fibre placement and tape laying

**Automated tape laying** (ATL) and **automated fibre placement** (AFP) use robotic heads to lay prepreg tape (75–300 mm wide for ATL) or bundles of narrow tows (3–13 mm, up to 32 tows) onto a tool, cutting and restarting each tow individually. AFP can steer tows along curved paths and follow doubly curved surfaces, enabling **variable-stiffness** laminates. Deposition rates of 20–100 kg/h made the composite fuselages and wings of current airliners possible. Defects specific to AFP — gaps, overlaps, twisted tows and wrinkles at steered paths — are monitored in-line. With thermoplastic tows and laser heating, AFP can consolidate in situ without an autoclave.

**Table 23.3 — Polymer-composite manufacturing processes (typical values).**

| Process | Fibre form | $V_f$ | Void content (%) | Cycle time | Typical products |
|---|---|---|---|---|---|
| Hand lay-up / spray-up | Mat, woven fabric, chopped | 0.20–0.40 | 2–5 | hours | Boat hulls, tanks, pools |
| Vacuum infusion | Fabrics, non-crimp fabrics | 0.50–0.58 | 1–2 | hours | Wind blades, yachts, bridge decks |
| Prepreg / autoclave | UD tape, fabric prepreg | 0.55–0.65 | <1 | 4–12 h | Aircraft wings and fuselages, F1 chassis |
| RTM / HP-RTM | Dry preform | 0.45–0.60 | 0.5–2 | 1–60 min | Car structural parts, aero brackets, fan blades |
| Compression moulding (SMC) | Chopped (25 mm) | 0.20–0.35 | 1–3 | 1–3 min | Truck cabs, car panels, enclosures |
| Filament winding | Continuous tow | 0.55–0.70 | 1–3 | min–h | Pipes, pressure vessels, shafts |
| Pultrusion | Continuous roving, mat | 0.55–0.70 | 1–2 | continuous | Profiles, rebar, spar caps |
| AFP / ATL | Prepreg tow or tape | 0.55–0.65 | <1 (after cure) | hours | Fuselage barrels, wing skins |
| Injection moulding (short fibre) | Chopped in pellets | 0.10–0.25 | <1 | 20–90 s | Housings, intake manifolds, brackets |

> **Boundary.** Polymer flow, cure kinetics and the rheology of thermoset and thermoplastic matrices are developed in Chapters 19 and 21; here only the composite-specific steps are treated. Recycling of composites is taken up in Chapter 49.

---

## 23.7 Metal- and ceramic-matrix composites

### Metal-matrix composites

MMCs combine a metallic matrix — mostly aluminium, also magnesium, titanium and copper — with ceramic particles, whiskers or fibres. The goals are higher stiffness, wear resistance, elevated-temperature strength and lower thermal expansion than the alloy alone, while keeping metallic toughness, conductivity and transverse properties that PMCs lack. Matrix-dominated properties (transverse strength, shear, temperature capability) are far better than in PMCs; the price is processing difficulty and lower ductility.

Processing routes are:

- **Stir casting**: SiC or Al₂O₃ particles stirred into molten aluminium and cast. Cheap, but limited to about 20–25 vol% and prone to clustering and reaction ($4\mathrm{Al}+3\mathrm{SiC}\rightarrow\mathrm{Al_4C_3}+3\mathrm{Si}$, a brittle, moisture-sensitive carbide; adding Si to the melt suppresses it).
- **Powder metallurgy**: blending alloy and ceramic powders, compacting, and extruding or forging (Chapter 38). Better distribution, up to about 40 vol%.
- **Squeeze casting and pressure infiltration** of a porous ceramic preform with molten metal, reaching 50–70 vol% — the route for AlSiC electronic baseplates.
- **Diffusion bonding** of foil–fibre–foil stacks for continuous-fibre titanium MMCs (SiC monofilament in Ti), used in a few aero-engine components.

**Table 23.4 — Representative metal- and ceramic-matrix composites (typical values).**

| Material | Reinforcement | Density (g/cm³) | $E$ (GPa) | Strength (MPa) | CTE (ppm/K) | Application |
|---|---|---|---|---|---|---|
| Al 6061 (reference) | — | 2.70 | 69 | 310 | 23 | — |
| 6061/SiC/20p | 20 % SiC particles | 2.80 | 100–105 | 400–500 | 15–16 | Bicycle frames, brake rotors, pistons |
| AlSiC (infiltrated) | 63–70 % SiC | 2.95–3.0 | 190–220 | 250–350 (flexure) | 7–8 | Power-electronics baseplates |
| Ti/SiC (continuous fibre) | 35 % SiC monofilament | 3.9 | 210 (axial) | 1,500–1,800 (axial) | ~6 | Aero-engine shafts, rings (niche) |
| WC–Co (cemented carbide) | 85–94 % WC | 14–15 | 550–650 | 2,000–4,000 (TRS) | 5–6 | Cutting tools, mining bits |
| C/C | Carbon fibre | 1.6–1.9 | 30–100 | 100–300 | ~1 | Aircraft and F1 brakes, re-entry nose caps |
| C/SiC | Carbon fibre | 1.9–2.4 | 60–100 | 200–350 | 2–3 | Car brake discs, thrust nozzles |
| SiC/SiC | SiC fibre, BN interphase | 2.5–2.8 | 200–280 | 250–350 | 4–5 | Turbine shrouds, combustor liners |
| Oxide/oxide | Nextel 610/720 | 2.6–2.9 | 70–120 | 150–350 | 6–8 | Exhaust mixers, combustor liners |

### Ceramic-matrix composites: toughness by design

In a PMC the fibres are there to add stiffness and strength to a weak matrix. In a CMC the matrix is already stiff and strong; the fibres are there to stop it failing catastrophically. A monolithic SiC ceramic has a fracture toughness of 3–4 MPa m$^{1/2}$ and fails from its largest flaw (Chapter 14). A SiC/SiC composite fails gradually, with a non-linear stress–strain curve and a "toughness" equivalent to 20–30 MPa m$^{1/2}$.

The key is a deliberately **weak interface**. Fibres are coated with a thin interphase — pyrolytic carbon or boron nitride, 0.1–1 μm thick — with a layered structure that cleaves easily. When a matrix crack reaches a fibre, the crack deflects along the interphase instead of cutting the fibre (the He–Hutchinson criterion: deflection occurs if the interface toughness is below about a quarter of the fibre toughness). The intact fibres then **bridge** the crack, and as they break at scattered locations, they **pull out** against interfacial friction, absorbing energy. Under tension the matrix cracks first at the **matrix cracking stress** (predicted by Aveston–Cooper–Kelly theory), then more cracks form until they saturate, and the fibres carry the load until they fail — a pseudo-ductile response. This is the same physics as fibre bridging and R-curve toughening in Chapter 14, made into the main mechanism.

Processing routes are **chemical vapour infiltration** (CVI), which deposits SiC within a fibre preform from methyltrichlorosilane gas over weeks, leaving 10–15 % porosity; **polymer infiltration and pyrolysis** (PIP), which repeatedly impregnates and pyrolyses a preceramic polymer; and **melt infiltration** (MI), which infiltrates a carbon-containing preform with molten silicon to react to SiC, giving near-full density but residual free silicon that limits service to about 1,350 °C. **C/C composites**, made by CVI of carbon or by repeated pitch impregnation, combine low density, high thermal conductivity and strength retention to over 2,000 °C in inert atmospheres, which makes them the material of aircraft and Formula 1 brakes and of re-entry nose caps — but they oxidize in air above about 450 °C and need protective coatings. C/SiC brakes now appear on high-performance cars.

SiC/SiC CMCs entered commercial aero-engine service in the 2010s as high-pressure turbine shrouds, with a third of the density of the nickel superalloys they replace and capability about 150–200 K higher, cutting cooling air requirements (Chapter 33). Their limiting issues are oxidation of the interphase through matrix cracks at intermediate temperatures, recession of SiC by water vapour (mitigated by environmental barrier coatings) and cost.

> **Status of the principle: Weak-interface toughening of CMCs**
> *Approximate.* The crack-deflection criterion and the Aveston–Cooper–Kelly matrix-cracking stress follow from fracture mechanics and shear-lag analysis under idealized assumptions (uniform fibre spacing, constant frictional sliding stress, single fibre strength); they predict the trends that guide interphase design, while quantitative design relies on measured stress–strain behaviour.

---

## What remains open

| Open question | Where it is answered |
|---|---|
| How are ply properties obtained from fibre and matrix, and how do they transform with angle? | Chapter 22 (micromechanics, $Q$ and $\bar Q$) |
| What fracture-mechanics concepts ($G$, $K$, R-curves, Weibull) underlie delamination and CMC toughening? | Chapter 14 (fracture, toughening, statistics) |
| How do composites behave under cyclic loading and long-term environmental exposure? | Chapter 14 (fatigue), Chapter 36 (degradation and failure analysis) |
| How are composite structures joined to each other and to metals? | Chapter 39 (adhesive bonding, mechanical fastening, dissimilar joints) |
| How are CMCs and C/C used in turbines, hypersonic vehicles and re-entry? | Chapter 33 (extreme environments) |
| How do moisture, temperature and expansion mismatch interact in thermal design? | Chapter 24 (thermal properties, thermal stress) |
| How are internal defects (voids, delaminations) detected? | Chapter 42 (laboratory characterization), Chapter 43 (tomography) |
| How are composite laminates modelled in multiscale simulations? | Chapter 46 (multiscale modelling and ICME) |
| How are composites chosen against metals for weight-critical parts? | Chapter 48 (materials selection) |
| How can thermoset composites be recycled at end of life? | Chapter 49 (recycling, circular economy) |

**Next:** Chapter 24 opens Part VI with the thermal properties of materials — how solids store, conduct and expand with heat, and how temperature changes turn into stress.
