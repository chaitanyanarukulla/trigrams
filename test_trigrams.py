"""This is the testing module for trigrams.py."""
import pytest

def test_read_file():
	"""Tests the read_file function in trigrams.py for whether a string."""
	from trigrams import read_file
	assert type(read_file("text.txt")) == str


TEST_for_dictinory = [
    ("this is long text!", {("this", "is"): ["long"], ("is", "long."): ["text!"]})
]

@pytest.mark.parametrize('input, outout', TEST_For_dictonery)
def test_trigramize(input, output):
    """Test to see if string changes in to key value pair"""
    from trigrams import trigramize
    assert trigramize(input) == output

