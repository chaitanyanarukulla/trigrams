"""This is the testing module for trigrams.py."""
import pytest

def test_read_file():
	"""Tests the read_file function in trigrams.py."""
	from trigrams import read_file
	assert type(read_file("text.txt")) == str

# def test_read_file2():
# """."""


