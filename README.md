# Smallest_K_Value
This repository contains a Python script and a set of pytest tests designed for analyzing genome sequences through k-mer identification. The main script processes genome sequence data to find the smallest k-mer size such that each k-mer has exactly one unique subsequent k-mer across all sequences. The pytest tests ensure the reliability and correctness of the script functionalities.

# Scripts
## Main Script (kmers.py)
The script kmers.py is designed to read genome sequence data from a file and determine the smallest k-mer size where each k-mer in any sequence has exactly one subsequent k-mer. This information is crucial for genome assembly and other bioinformatics analyses.

Run the script from the command line by providing the path to the sequence data file (in FASTA format). For example:

python3 kmers.py path to your reads.fa

# Features
**K-mer Identification:** Generates all possible k-mers for a given size k from the DNA sequences.

**Subsequent K-mer Mapping:** Maps each k-mer to its subsequent k-mers to trace possible sequence continuations.

**Minimal K Calculation:** Determines the smallest k such that each k-mer has a unique subsequent k-mer, facilitating simpler and more certain genome assembly.

## Pytest Test Script (test_kmers.py)
test_kmers.py contains tests written using pytest to validate the functionality of the main script. These tests ensure that only valid nucleotide sequences are processed, the k value is appropriate for given sequences, and the correct k-mers are identified.

## Running Tests
Execute the following command in the terminal:

pytest test_kmers.py

# Tests Included
**Valid Nucleotide Check:** Ensures that sequences contain only valid nucleotides (A, T, C, G, a, t, c, g).

**K Value Appropriateness:** Verifies that the k value does not exceed the length of any sequence.

**K-mer Generation:** Checks the generation of k-mers for various k sizes on a fixed-length sequence to ensure accurate processing.
