# Read Mapping & Alignment Statistics

**Problem**  
How can we align short sequencing reads to a reference genome and evaluate the quality of those alignments?

**Approach**  
This workflow uses multiple short-read aligners (Bowtie2, BWA-MEM, HISAT2, Minimap2) to map paired-end reads and generate alignment summaries.  
`Samtools` is used for file conversion, sorting, indexing, and basic alignment statistics.

---

## Files
- **Bowtie2** — index and paired-end alignment  
- **BWA-MEM** — alignment for reads > 70 bp  
- **HISAT2** — fast spliced aligner for general read mapping  
- **Minimap2** — short-read alignment (`-ax sr`)  
- **Samtools** — convert, sort, index, and compute stats  

---

## Usage

```bash
# ---------------------------
# https://github.com/BenLangmead/bowtie2
# Build Bowtie2 index and align paired-end reads
bowtie2-build ref.fa refidx
bowtie2 --no-unal -p 4 -x refidx -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz -S bt2.sam

# ---------------------------
# https://github.com/lh3/bwa
# Index reference and align with BWA-MEM (suitable for reads >70 bp)
bwa index ref.fa
bwa mem -t 4 ref.fa reads_R1.fastq.gz reads_R2.fastq.gz > bwa.sam

# ---------------------------
# https://daehwankimlab.github.io/hisat2/
# Build HISAT2 index and align paired-end reads
hisat2-build ref.fa hisatidx
hisat2 -p 4 -x hisatidx -1 reads_R1.fastq.gz -2 reads_R2.fastq.gz -S hisat2.sam

# ---------------------------
# https://github.com/lh3/minimap2
# Align paired-end reads with Minimap2 (short-read preset)
minimap2 -t 4 -ax sr ref.fa reads_R1.fastq.gz reads_R2.fastq.gz > mm2.sam

# ---------------------------
# https://www.htslib.org/doc/samtools.html
# Convert, sort, index, and summarize alignments
samtools view -@ 4 -bS bt2.sam > bt2.bam
samtools sort -@ 4 -o bt2.sorted.bam bt2.bam
samtools index bt2.sorted.bam
samtools stats bt2.sorted.bam > bt2.stats.tsv
