"""This is the testing module for trigrams.py."""
import pytest


def test_read_file():
    """Tests the read_file function in trigrams.py for whether a string."""
    from trigrams import read_file
    assert type(read_file("text.txt")) == str


Test = [("this is long", {("this", "is"): ["long"]}),
        ("is very long", {("is", "very"): ["long"]}),
        ("is very long", {("is", "very"): ["long"]})]


@pytest.mark.parametrize('input, output', Test)
def test_changes_text_into_dict(input, output):
    """Test to see if string changes in to key value pair"""
    from trigrams import changes_text_into_dict
    assert changes_text_into_dict(input) == output


Test2 = "this is a test string"


def test2_changes_text_into_dict():
    """tests changes_text_into_dict() returns a dict"""
    from trigrams import changes_text_into_dict
    assert type(changes_text_into_dict(Test2)) == dict
