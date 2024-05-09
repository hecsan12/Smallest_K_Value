import pytest
from kmers import kmers_value, file_acquisition, find_smallest_unique_k

def test_valid_nucleotides():
    """
    Test to ensure that only valid nucleotide characters (A, T, C, G, a, t, c, g) are present in the file.
    """
    filename = "./Coding\ With\ Python/Test_Sequence"
    with open(filename, 'w') as f:
        f.write(">Test Sequence\n")
        f.write("ATCGatcgXYZ\n")
    with pytest.raises(ValueError):
        file_acquisition(filename, 2)

def test_k_value_exceeds_sequence_length():
    """
    Ensure that the k value does not exceed the length of the sequence.
    """
    sequence = "ATCGATCG"
    k = 9  # Larger than the sequence length
    with pytest.raises(ValueError):
        kmers_value(sequence, k)

@pytest.mark.parametrize("k", [1, 5, 10])
def test_kmer_length_variations(k):
    """
    Test with a 10 nucleotide long sequence for various k values.
    """
    sequence = "ATCGATCGAT"  # 10 nucleotides long
    kmers = kmers_value(sequence, k)
    assert len(kmers) == len(sequence) - k + 1, "Incorrect number of kmers for k = {}".format(k)

def setup_module(module):
    """
    Setup function to create a sample file with only valid nucleotides.
    """
    filename = "./Coding\ With\ Python/Test_Sequence2"
    with open(filename, 'w') as f:
        f.write(">Test Sequence\n")
        f.write("ATCGATCGatcgatcg\n")  # Only valid characters
