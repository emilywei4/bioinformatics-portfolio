# Consensus Generation & Variant Calling

**Problem**  
How can we generate a consensus genome from mapped reads and identify single-nucleotide and indel variants using different variant callers?

**Approach**  
This workflow demonstrates how to sort and index mapped reads, build a consensus sequence, and call variants with both **LoFreq** and **FreeBayes**.  
Each tool provides unique capabilities for variant detection and accuracy assessment in viral and microbial genomics.

---

## Files
- **ViralConsensus** — generate consensus FASTA from mapped reads  
- **Samtools** — sort and index BAM files for downstream use  
- **LoFreq** — variant calling (SNVs and optional indels)  
- **FreeBayes** — variant calling with adjustable ploidy  

---

## Usage

```bash
# ---------------------------
# https://github.com/niemasd/ViralConsensus
# Generate consensus sequence from mapped reads
viral_consensus -i aln.bam -r ref.fa -o consensus.fa
# Optional outputs:
#   -op pos_counts.tsv   # per-position base counts
#   -oi ins_counts.tsv   # insertion counts

# ---------------------------
# https://www.htslib.org/doc/samtools-sort.html
# https://www.htslib.org/doc/samtools-index.html
# Sort and index BAM for variant calling
samtools sort -@ 4 -o aln.sorted.bam aln.bam
samtools index aln.sorted.bam

# ---------------------------
# https://csb5.github.io/lofreq/
# Call variants using LoFreq
# SNVs only:
lofreq call -f ref.fa -o vars_lofreq.vcf aln.sorted.bam

# Add indel qualities (recommended for indel calling)
lofreq indelqual --dindel -f ref.fa -o aln.indelq.bam aln.sorted.bam
samtools index aln.indelq.bam

# SNVs + indels:
lofreq call --call-indels -f ref.fa -o vars_lofreq_indels.vcf aln.indelq.bam

# ---------------------------
# https://github.com/freebayes/freebayes
# Variant calling with FreeBayes; adjust ploidy (-p)
# Viruses are typically haploid (-p 1)
freebayes -f ref.fa -p 1 aln.sorted.bam > vars_freebayes.vcf

# Example for polyploid organisms (-p 4)
# freebayes -f ref.fa -p 4 aln.sorted.bam > vars_freebayes.vcf
