from seasons import minutes, convert
import pytest

def test_date_in_minutes():
    assert minutes("2022-02-20") == 525600

def test_convert():
    assert convert("525600") == "five hundred twenty-five thousand, six hundred"

