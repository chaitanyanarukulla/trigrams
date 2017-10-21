"""This is the testing module for trigrams.py."""
import pytest

def test_read_file():
	"""Tests the read_file function in trigrams.py for whether a string."""
	from trigrams import read_file
	assert type(read_file("text.txt")) == str
