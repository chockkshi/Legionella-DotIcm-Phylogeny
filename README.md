# Legionella-DotIcm-Phylogeny

Mini comparative-genomics project exploring the conservation of the Dot/Icm type IVB secretion system across the *Legionella* genus.

## Question

Is the Dot/Icm secretion system (the molecular “syringe” *Legionella* uses to survive inside host cells) conserved across the genus, and is it shared with related intracellular bacteria?

## Data

11 RefSeq proteomes downloaded from NCBI Datasets (accessions listed in `genomes.tsv`):

- 8 *Legionella* species: *L. pneumophila*, *L. longbeachae*, *L. micdadei*, *L. oakridgensis*, *L. feeleii*, *L. jordanis*, *L. bozemanii*, *L. anisa*
- *Coxiella burnetii* (close relative)
- *Francisella tularensis* (more distant relative)
- *Escherichia coli* K-12 (outgroup)

## Methods

- **Species tree**: Single-copy marker gene *rpoB* extracted from each proteome and analysed with the NGPhylogeny.fr One-Click workflow (PhyML). Tree rooted on *E. coli* and visualised in iTOL.
- **Gene content analysis**: 11 core Dot/Icm proteins from *L. pneumophila* used as BLASTP queries. A gene was scored **present** when the best hit (selected by bitscore) showed ≥30% identity and ≥50% query coverage.
- **Validation**: Reciprocal best-hit test applied to borderline DotB hits in *E. coli* and *Francisella*.

## Key Results

- All 8 *Legionella* species possess the complete set of 11 Dot/Icm genes.
- *Coxiella burnetii* retains 8 of the 11 genes (dotA, icmL and icmX fell below the detection threshold).
- *Francisella tularensis* and *E. coli* lack a true Dot/Icm system (initial DotB-like hits failed the reciprocal best-hit test and were scored absent).

**Biological interpretation**: The Dot/Icm system appears to be an ancestral and conserved feature of the *Legionella–Coxiella* lineage.

## Figure

![Tree and Dot/Icm presence-absence](05_Figures/saWBFADVxtrJt6uAvbljkw.pdf)

*rpoB protein tree of 11 bacteria (rooted on E. coli) with presence (filled) or absence (empty) of 11 Dot/Icm genes. Presence defined as ≥30% identity and ≥50% query coverage; DotB in E. coli and Francisella failed reciprocal best-hit testing.*

## Limitations

- Single-gene (*rpoB*) tree — relationships only, no molecular dating.
- Presence/absence based on BLAST thresholds; only DotB received a reciprocal check.
- Small sample size (8 *Legionella* species).
- Divergent orthologues may be missed by BLAST (profile HMM methods would be more sensitive).

## Repository Contents

- `genomes.tsv` — list of genomes and accessions
- `02_Markers/rpoB_all.fasta` — extracted rpoB sequences
- `03_Tree/PhyML_newick_tree.nhx` — phylogenetic tree
- `04_DotIcm/` — presence/absence tables and analysis scripts
- `05_Figures/` — final figure
