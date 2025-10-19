import pytest

from simple_test import get_file_stats

def test_analyze_text_normal_case():
    """Tests the basic functionality."""
    text = "Hello world! This is a test. Hello again."
    result = get_file_stats(text)
    assert result["word_count"] == 8
    assert result["unique_word_count"] == 7
    assert result["most_frequent_word"] == "hello"
    assert result["frequency"] == 2


def test_analyze_text_normal_case():
    """Tests empty string functionality."""
    text = ""
    result = get_file_stats(text)
    assert result["word_count"] == 0
    assert result["unique_word_count"] == 0
    assert result["most_frequent_word"] == None
    assert result["frequency"] == 0
    

def test_analyze_text_normal_case():
    """Tests the punctuation functionality."""
    text = "Hello world! This is a test. Hello! again."
    result = get_file_stats(text)
    assert result["word_count"] == 8
    assert result["unique_word_count"] == 7
    assert result["most_frequent_word"] == "hello"
    assert result["frequency"] == 2
    

def test_analyze_text_normal_case():
    """Tests the casing functionality."""
    text = "Hello world! This is a test. hello! again."
    result = get_file_stats(text)
    assert result["word_count"] == 8
    assert result["unique_word_count"] == 7
    assert result["most_frequent_word"] == "hello"
    assert result["frequency"] == 2

