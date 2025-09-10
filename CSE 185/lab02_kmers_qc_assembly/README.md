# Lab 2 — K-mers, QC, Assembly & Assessment

**Goal**  
Implement simple k-mer logic in Python and document a short-read assembly pipeline with common tools:
- Unique k-mers and k-mer counts from a DNA sequence
- Paired-end QC plots (QUACK), adapter/quality trimming (fastp)
- De novo assembly (SPAdes), assembly QC (QUAST), and gene prediction (Prodigal)

**Why it matters**  
K-mers underpin many algorithms (assembly, indexing, error correction). The toolchain reflects a typical early-stage NGS workflow.

---

## Files
- `unique_kmers.py` — Print unique k-mers (alphabetically).
- `kmer_counts.py` — Print `kmer,count` in alphabetical order.
- **Pipeline drivers (documented commands below)**  
  - QUACK (QC plots)  
  - fastp (trimming)  
  - SPAdes (assembly)  
  - QUAST (assembly quality)  
  - Prodigal (gene prediction)

---

## Usage (k-mers)

Given a FASTA with one sequence (multi-line OK), e.g. `../lab01_fastx_parsing/sample.fa`:

```bash
# Unique k-mers
python unique_kmers.py 3 ../lab01_fastx_parsing/sample.fa

# K-mer counts
python kmer_counts.py 3 ../lab01_fastx_parsing/sample.fa

# https://github.com/IGBB/quack
# quack -1 <R1.fastq.gz> -2 <R2.fastq.gz> -n <job_name>
quack -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz -n sample_qc
# Output: sample_qc.svg (plus report assets)

# https://ablab.github.io/spades/
# Output directory name is the "job name" for this run
spades.py --pe1-1 trimmed_R1.fastq.gz --pe1-2 trimmed_R2.fastq.gz -o spades_out
# Output: contigs.fasta in spades_out/

# https://quast.sourceforge.net/quast.html
quast -o quast_out spades_out/contigs.fasta
# Output: quast_out/report.tsv, etc.

# https://github.com/hyattpd/Prodigal
# -i input FASTA, -o GFF, -a proteins, -d nucleotide CDS
prodigal -i spades_out/contigs.fasta \
         -o prodigal.gff \
         -a prodigal_proteins.faa \
         -d prodigal_cds.fna
