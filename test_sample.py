# content of test_sample.py
import pytest
from main import string_to_DNA



def test_string_to_DNA():
    assert string_to_DNA("TACACCTTGGCGACGACT") == "TACACCTTGGCGACGACT"
    
