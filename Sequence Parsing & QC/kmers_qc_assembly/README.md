# K-mers, Quality Control, and Genome Assembly

**Problem**  
How can we analyze short-read sequencing data to identify unique k-mers, perform quality control, assemble genomes, and evaluate assembly quality?

**Approach**  
This workflow combines Python scripts for k-mer exploration with standard bioinformatics tools for read trimming, assembly, and annotation.  
It reflects the early stages of a typical NGS (Next-Generation Sequencing) data processing pipeline.

---

## Files
- `unique_kmers.py` — Print all unique k-mers (alphabetically).  
- `kmer_counts.py` — Print `kmer,count` in alphabetical order.  
- **Pipeline drivers (documented commands below)**  
  - QUACK — read quality control plots  
  - fastp — adapter/quality trimming  
  - SPAdes — de novo assembly  
  - QUAST — assembly quality assessment  
  - Prodigal — gene prediction  

---

## Usage

Given a FASTA with one sequence (multi-line OK), e.g. `../sequence_parsing_qc/sample.fa`:

```bash
# ---------------------------
# Unique k-mers
python unique_kmers.py 3 ../sequence_parsing_qc/sample.fa

# ---------------------------
# K-mer counts
python kmer_counts.py 3 ../sequence_parsing_qc/sample.fa

# ---------------------------
# https://github.com/IGBB/quack
# Generate read quality plots
quack -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz -n sample_qc
# Output: sample_qc.svg (plus report assets)

# ---------------------------
# https://github.com/OpenGene/fastp
# Adapter and quality trimming
fastp -i reads_R1.fastq.gz -I reads_R2.fastq.gz -o trimmed_R1.fastq.gz -O trimmed_R2.fastq.gz -h fastp_report.html -j fastp_report.json

# ---------------------------
# https://ablab.github.io/spades/
# De novo assembly; output directory name is the "job name" for this run
spades.py --pe1-1 trimmed_R1.fastq.gz --pe1-2 trimmed_R2.fastq.gz -o spades_out
# Output: contigs.fasta in spades_out/

# ---------------------------
# https://quast.sourceforge.net/quast.html
# Evaluate assembly quality
quast -o quast_out spades_out/contigs.fasta
# Output: quast_out/report.tsv, etc.

# ---------------------------
# https://github.com/hyattpd/Prodigal
# Gene prediction: -i input FASTA, -o GFF, -a proteins, -d nucleotide CDS
prodigal -i spades_out/contigs.fasta \
         -o prodigal.gff \
         -a prodigal_proteins.faa \
         -d prodigal_cds.fna
