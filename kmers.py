#!/usr/bin/env python3

import sys

def find_kmers(sequence, k):
    """
    This function takes a DNA sequence and an integer k, and returns a dictionary where
    each key is a k-mer (substring of length k) from the sequence, and each value is a set of
    unique k-mers that immediately follow the key k-mer in the sequence.

    Args:
    sequence (str): The DNA sequence.
    k (int): The length of the k-mers.

    Returns:
    dict: A dictionary of k-mers and their subsequent k-mers.
    """
    kmers = {}
    length = len(sequence)
    for i in range(length - k + 1):
        kmer = sequence[i:i + k]
        if i + k < length:
            next_kmer = sequence[i + 1:i + 1 + k]
            if kmer in kmers:
                kmers[kmer].add(next_kmer)
            else:
                kmers[kmer] = {next_kmer}
    return kmers



def process_file(filename, k):
    """
    This function reads multiple DNA sequences from a file, computes the k-mers for each sequence
    using find_kmers function, and aggregates them into a single dictionary.

    Args:
    filename (str): The path to the file containing DNA sequences.
    k (int): The length of the k-mers.

    Returns:
    dict: A dictionary of all k-mers and their subsequent k-mers from all sequences.
    """
    all_kmers = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith(">"):
                continue
            sequence = line.strip()
            kmers = find_kmers(sequence, k)
            for kmer, next_kmers in kmers.items():
                if kmer in all_kmers:
                    all_kmers[kmer].update(next_kmers)
                else:
                    all_kmers[kmer] = next_kmers
    return all_kmers

def find_smallest_unique_k(filename):
    """
    This function identifies the smallest value of k such that each k-mer in any sequence
    in the file has exactly one unique subsequent k-mer.

    Args:
    filename (str): The path to the file containing DNA sequences.

    Returns:
    int: The smallest value of k meeting the condition, or -1 if no such k exists.
    """
    k = 1
    while True:
        all_kmers = process_file(filename, k)
        if all(len(v) == 1 for v in all_kmers.values()):
            return k
        if not all_kmers:  # No k-mers were found, probably k is too large
            return -1
        k += 1
    return -1



def main():
    """
    Main function to handle command line input and process the DNA sequences file.
    It prints the smallest k where each k-mer has exactly one subsequent k-mer.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    smallest_k = find_smallest_unique_k(filename)
    print(f"The smallest k with a unique subsequent k-mer for each k-mer is: {smallest_k}")


if __name__ == "__main__":
    main()
