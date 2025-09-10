# Lab 4 — Consensus & Variant Calling

**Goal**  
Generate a consensus genome from mapped reads and call variants with two different callers:
- Build consensus sequence (ViralConsensus)  
- Sort and index alignments (Samtools)  
- Call variants with LoFreq & FreeBayes  

**Why it matters**  
Consensus sequences and variant calls are essential outputs for viral genomics and many clinical/epi workflows. Comparing multiple callers helps understand tool assumptions and strengths.

---

## Files
- **Pipeline drivers (documented commands below)**  
  - ViralConsensus (consensus FASTA)  
  - Samtools (sort + index)  
  - LoFreq (variant calling with/without indels)  
  - FreeBayes (variant calling with ploidy options)  

---

## Usage

```bash
# ---------------------------
# ViralConsensus
# https://github.com/niemasd/ViralConsensus
# Call consensus sequence from mapped reads

viral_consensus -i aln.bam -r ref.fa -o consensus.fa

# Optional outputs:
#   -op pos_counts.tsv   # per-position counts
#   -oi ins_counts.tsv   # insertion counts

# ---------------------------
# Samtools (sort + index)
# https://www.htslib.org/doc/samtools-sort.html
# https://www.htslib.org/doc/samtools-index.html
# Prepare alignments for downstream tools

# Sort BAM
samtools sort -@ 4 -o aln.sorted.bam aln.bam

# Index BAM
samtools index aln.sorted.bam

# ---------------------------
# LoFreq
# https://csb5.github.io/lofreq/
# Variant calling (SNVs by default, add --call-indels for indels)

# (Optional) Add indel qualities for indel calling
lofreq indelqual --dindel -f ref.fa -o aln.indelq.bam aln.sorted.bam
samtools index aln.indelq.bam

# Call SNVs only
lofreq call -f ref.fa -o vars_lofreq.vcf aln.sorted.bam

# Call SNVs + indels (requires indel qualities)
lofreq call --call-indels -f ref.fa -o vars_lofreq_indels.vcf aln.indelq.bam

# ---------------------------
# FreeBayes
# https://github.com/freebayes/freebayes
# Variant calling; adjust ploidy (-p). Viruses are usually haploid (-p 1).

# Haploid (typical viral data)
freebayes -f ref.fa -p 1 aln.sorted.bam > vars_freebayes.vcf

# Example with polyploid (-p 4)
# freebayes -f ref.fa -p 4 aln.sorted.bam > vars_freebayes.vcf
