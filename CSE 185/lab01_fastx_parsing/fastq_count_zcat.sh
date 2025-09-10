#!/usr/bin/env bash
# Usage: bash fastq_count_zcat.sh reads.fastq.gz

zcat "$1" | grep -c '^+'
