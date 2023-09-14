import pytest
from hamming import distance

def test_identical_strands():
    assert distance("A", "A") == 0
    assert distance("GGACTGA", "GGACTGA") == 0

def test_complete_distance():
    assert distance("A", "G") == 1
    assert distance("AG", "CT") == 2

def test_small_distance():
    assert distance("AT", "CT") == 1
    assert distance("GGACG", "GGTCG") == 1
    assert distance("ACCAGGG", "ACTATGG") == 2

def test_non_unique_characters():
    assert distance("AGA", "AGG") == 1
    assert distance("AGG", "AGA") == 1

def test_same_nucleotides_in_different_positions():
    assert distance("TAG", "GAT") == 2

def test_large_distance():
    assert distance("GATACA", "GCATAA") == 4
    assert distance("GGACGGATTCTG", "AGGACGGATTCT") == 9

def test_empty_strands():
    assert distance("", "") == 0

def test_different_strand_lengths():
    with pytest.raises(ValueError):
        distance("AATG", "AAA")
    with pytest.raises(ValueError):
        distance("ATA", "AGTG")
    with pytest.raises(ValueError):
        distance("", "G")
    with pytest.raises(ValueError):
        distance("G", "")

if __name__ == "__main__":
    pytest.main()
