"""This is the testing module for trigrams.py."""
import pytest

def test_read_file():
	"""Tests the read_file function in trigrams.py for whether a string."""
	from trigrams import read_file
	assert type(read_file("text.txt")) == str

def test_read_file2():
	"""Tests the read_file function in trigrams.py for length of text."""
	from trigrams import read_file
	assert len(read_file("text.txt")) > 100

def test_change_string_text_to_list():
	from trigrams import change_string_text_to_list
	assert len(change_string_text_to_list("string of words")) < 100

