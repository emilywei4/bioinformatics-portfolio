# Lab 3 — Read Mapping & Alignment Stats

**Goal**  
Practice short-read mapping to a reference genome with common aligners and generate basic alignment stats:
- Build indices, align paired-end reads → SAM/BAM
- Summarize alignment quality with `samtools stats`

**Why it matters**  
Accurate mapping is foundational for downstream analyses (variant calling, expression, consensus). Knowing multiple aligners + stats helps you choose tools and diagnose problems.

---

## Files
- **Bowtie2** — index + paired-end alignment  
- **BWA-MEM** — paired-end alignment  
- **HISAT2** — index + paired-end alignment  
- **Minimap2** — short-read alignment (`-ax sr`)  
- **Samtools** — conversion, sort, index, stats  

---

# Lab 3 — Read Mapping & Alignment Stats

**Goal**  
Practice short-read mapping to a reference genome with common aligners and generate basic alignment stats:
- Build indices, align paired-end reads → SAM/BAM  
- Summarize alignment quality with `samtools stats`

**Why it matters**  
Accurate mapping is foundational for downstream analyses (variant calling, expression, consensus). Knowing multiple aligners + stats helps you choose tools and diagnose problems.

---

## Files
- **Pipeline drivers (documented commands below)**  
  - Bowtie2 (index + paired-end alignment)  
  - BWA-MEM (paired-end alignment)  
  - HISAT2 (index + paired-end alignment)  
  - Minimap2 (short-read alignment, `-ax sr`)  
  - Samtools (convert, sort, index, stats)  

---

## Usage

```bash
# ---------------------------
# Bowtie2
# https://github.com/BenLangmead/bowtie2
# Map paired-end reads to reference genome

# Index reference (prefix = refidx)
bowtie2-build ref.fa refidx

# Align paired-end reads → SAM
bowtie2 --no-unal -p 4 -x refidx -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz -S bt2.sam

# ---------------------------
# BWA-MEM
# https://github.com/lh3/bwa
# Suitable for reads > ~70bp

# Index reference
bwa index ref.fa

# Align paired-end reads → SAM
bwa mem -t 4 ref.fa reads_R1.fastq.gz reads_R2.fastq.gz > bwa.sam

# ---------------------------
# HISAT2
# https://daehwankimlab.github.io/hisat2/
# Fast spliced aligner, works for general read mapping

# Index reference (prefix = hisatidx)
hisat2-build ref.fa hisatidx

# Align paired-end reads → SAM
hisat2 -p 4 -x hisatidx -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz -S hisat2.sam

# ---------------------------
# Minimap2
# https://github.com/lh3/minimap2
# Use `-ax sr` for short genomic paired-end reads

# Align paired-end reads → SAM
minimap2 -t 4 -ax sr ref.fa reads_R1.fastq.gz reads_R2.fastq.gz > mm2.sam

# ---------------------------
# Samtools
# https://www.htslib.org/doc/samtools.html
# Convert, sort, index, and summarize alignment

# Convert SAM → BAM
samtools view -@ 4 -bS bt2.sam > bt2.bam

# Sort BAM
samtools sort -@ 4 -o bt2.sorted.bam bt2.bam

# Index BAM
samtools index bt2.sorted.bam

# Generate alignment stats → TSV
samtools stats bt2.sorted.bam > bt2.stats.tsv
