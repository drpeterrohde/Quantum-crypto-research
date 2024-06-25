#import "@preview/charged-ieee:0.1.0": ieee

#show: ieee.with(
  title: [A typesetting system to untangle the scientific writing process],
  abstract: [
    The process of scientific writing is often tangled up with the intricacies of typesetting, leading to frustration and wasted time for researchers. In this paper, we introduce Typst, a new typesetting system designed specifically for scientific writing. Typst untangles the typesetting process, allowing researchers to compose papers faster. In a series of experiments we demonstrate that Typst offers several advantages, including faster document creation, simplified syntax, and increased ease-of-use.
  ],
  authors: (
    (
      name: "Martin Haug",
      department: [Co-Founder],
      organization: [Typst GmbH],
      location: [Berlin, Germany],
      email: "haug@typst.app"
    ),
    (
      name: "Laurenz Mädje",
      department: [Co-Founder],
      organization: [Typst GmbH],
      location: [Berlin, Germany],
      email: "maedje@typst.app"
    ),
  ),
  index-terms: ("Scientific writing", "Typesetting", "Document creation", "Syntax"),
)

= Links & chats
<links-chats>
- One way functions and P vs NP:
  #link("https://en.wikipedia.org/wiki/One-way_function");: \"The
  existence of such one-way functions is still an open conjecture. Their
  existence would prove that the complexity classes P and NP are not
  equal,\" \
  \* one-way permutation. \
  \* Trapdoor function. \

- GapP, NP, binary optimisation problems:
  #link("https://chatgpt.com/share/2e9f8c0f-fa1d-4d97-9af0-c195ad3cd22c")

- Homomorphism between $B_n$ and $S_n$:
  #link("https://chatgpt.com/share/c0390897-77f1-403e-bce9-ca2bf5c9fccc")

- Even Hamming weight for
  \$H(x{{\\hspace{1pt}}{\\mathbin{\\mathpalette\\make\@small{\\mathbin\\oplus}}}}{\\hspace{1pt}}y)\\in 2\\mathbb{Z}\$
  if $H (x) = H (y)$. Hence also for $y = pi circle.stroked.tiny x$
  where $pi in S_n$.

- Word problem for the braid group $B_n$ is poly-time solvable:
  #link("https://chatgpt.com/c/f8827503-7af9-4b81-b3dd-a79f1891746e")

- Wreath product #link("https://en.wikipedia.org/wiki/Wreath_product")

- Braid permutations $pi : B_n arrow.r S_n$, for $beta in B_n$ we have
  $pi (beta)$:
  #link("https://chatgpt.com/share/6c61f5ef-a33d-4c76-8f1f-0d8bdf1bb4aa")

- Inverting braids $[x / x]_pi^(pi^(‾)) arrow.r x$ is equivalent to the
  Conjugacy Problem for Permutations (CPP), known to be NP-complete. For
  braid codes complexity is maximised for the balanced pre-image space,
  $upright(w t) (x) = n \/ 2$.

= Overview
<overview>
The goal is to create information-theoretically secure asymmetric PQC
primitives where the only hardness assumption is the hardness of
brute-force, reducing all arguments to entropic ones.

There are multiple primitives we will combine together.

The purpose of differential encoding is create differential pairs
encoded against a secret, where the differential term is public and
cannot reveal the secret itself.

Combining differential encoding with random codewords we have a
codespace where all codewords are unique (statistical security
assumption) and errors on differentials are always detectable (but not
correctable).

Permutation codes and their respective algebra are used to create
asymmetric primitives from random codewords. This closely relates to and
is inspired by hash algebra. Here the central concept is that any
permutation on the bits in codewords creates a distinct codeword
(statistical security assumption). The asymmetric objects introduced
here are defines under the algebra of the symmetric group and their
inversion assuming random codewords is only via brute force as the
objects are provably non-invertible.

The security of asymmetric objects relates to their pre-image space
which decomposes into collisional and non-collisional partitions. The
former is insecure (ambiguous secrets) while the latter is secure.
Quantifying the size of these respective spaces affords provable
statements on statistical security alone.

The schemes resulting from this are compositional under binary XOR
algebra.

= Braid code summary
<braid-code-summary>
Asymmetric encryption ($A arrow.r B : m$):
$ mono(s i g)_A : thin & [frac(h (m xor p), m)]_pi^(pi^(‾)) ,\
mono(k e y)_B : thin & [s / p]_pi^(pi^(‾)) ,\
mono(d e c)_B : thin & [frac(h (m xor p), m)]_pi^(pi^(‾)) xor [s / p]_pi^(pi^(‾)) = [frac(h (m xor p) xor s, m xor p)]_pi^(pi^(‾)) , $
where knowledge of ${ s , p , h (m) , pi }$ affords the decryption
stage.

Digital signature for $m$:
$ mono(v e r)_A : thin & [frac(m, h (m))]_pi^(pi^(‾)) ,\
mono(s i g)_A : thin & h (m_pi) ,\
mono(k e y)_B : thin & [s / p]_pi^(pi^(‾)) ,\
mono(d e c)_B : thin & [frac(m, h (m))]_pi^(pi^(‾)) xor [s / p]_pi^(pi^(‾)) = [frac(m xor s, h (m) xor p)]_pi^(pi^(‾)) . $

= Entropy algebra
<entropy-algebra>
Taking the abelian group of arbitrary length bit-strings under bit-wise
XOR#footnote[Elementary abelian 2-group.];,
$ G_(upright(b i n)) & tilde.op (bb(Z)_2^n , xor) tilde.op ({ 0 , 1 }^n , xor) , $
we consider subgroups generated by finite alphabets of $k$ randomly
sampled letters, $ Sigma & in cal(X) (bb(Z)_2^n) ,\
G_Sigma & = angle.l Sigma angle.r ,\
G_Sigma & subset.eq G_(upright(b i n)) , $ where individual generators
compose under $(bb(Z)_2 , xor)$, $ g_i xor g_i = e tilde.op bold(0) , $
and the identity element is the zero vector. Entropy groups have group
generators representing independent random variables,
$ G_E & = angle.l cal(X)_(i in { 1 , k }) angle.r tilde.op bb(Z)_2^k ,\
lr(|G_(upright(E))|) & = 2^k , $ where group elements comprise all
binary combinations of group generators.

Independent maximum entropy letters, $ H (cal(X)) = 1 , $ exhibit no
mutual information, $ I (cal(X)_i , cal(X)_j) = delta_(i , j) , $ and
are statistically orthogonal, thereby constituting distinct letters in
the algebra. Zero-entropy letters reduce to constants,
$ H (cal(X) arrow.r c) = 0 . $

Information theoretically, for maximum entropy random variables the
entropy group generators are distinct, \$\$\\begin{aligned}
    G\_\\mathrm{ent} &= \\langle \\mathcal{X}\_i,\\mathcal{X}\_j\\rangle,\\nonumber\\\\
    &= \\{e,\\mathcal{X}\_i,\\mathcal{X}\_j, \\mathcal{X}\_i{{\\hspace{1pt}}{\\mathbin{\\mathpalette\\make\@small{\\mathbin\\oplus}}}}{\\hspace{1pt}}\\mathcal{X}\_j\\} \\nonumber\\\\
    &= \\langle \\mathcal{X}\_i\\rangle \\times \\langle \\mathcal{X}\_j\\rangle \\nonumber\\\\
    &\\sim \\mathbb{Z}\_2 \\times \\mathbb{Z}\_2.
\\end{aligned}\$\$ Zero-entropy random variables have no
information-theoretic content, reducing the action of the entropy group
to the trivial group, $ phi.alt : & thin cal(X) arrow.r e ,\
tilde(G)_(upright(E)) & = { e } tilde.op bold(1) . $ defining a group
homomorphism mapping entropic code groups to non-entropic ones,
$  & phi.alt : G_(upright(C)) arrow.r tilde(G)_(upright(C)) ,\
 & upright(k e r) (tilde(G)_(upright(C))) = G_(upright(E)) ,\
 & tilde(G)_(upright(C)) = G_(upright(C)) thin \/ thin upright(k e r) (phi.alt) = G_(upright(C)) \/ G_(upright(E)) . $

Code groups may contain both entropic ($cal(X)$) and non-entropic
generators ($x$) and group elements in general comprise letters from
both
(\$\\mathcal{X}{{\\hspace{1pt}}{\\mathbin{\\mathpalette\\make\@small{\\mathbin\\oplus}}}}{\\hspace{1pt}}x\$).
Non-entropic group elements comprising only non-entropic generators
expose the group generators comprising the group element ($x$), whereas
entropic elements
(\$\\mathcal{X}{{\\hspace{1pt}}{\\mathbin{\\mathpalette\\make\@small{\\mathbin\\oplus}}}}{\\hspace{1pt}}x\$)
do not. The entropic and non-entropic subgroups partition a group into a
direct product (sum under $xor$) decomposition,
$ G = G_(cal(X)) times tilde(G)_(cal(X)) , $ where the entropic subgroup
$G_(cal(X))$ is protected while the non-entropic group is exposed.

Different parties in a multi-party communications protocol in general
possess different generating sets defining their subjective code groups.
In the context of an encryption protocol the goal is for communicating
parties to establish private code groups exposing encrypted data, while
ensuring the public code group exposes only entropic objects.

== Symmetric encryption
<symmetric-encryption>
Consider an entropy code group comprising two random variables
($cal(X)_i , cal(X)_j$), secrets ($s , p$), and message $m$, defining
the group generators,
$ G_(upright(C)) & = angle.l s , p , m , cal(X)_i , cal(X)_j angle.r tilde.op bb(Z)_2^5 . $
with $lr(|G_(upright(C))|) = 2^5$ code words.

