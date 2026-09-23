import pytest

from webseccheck import analyze, validate_target


def test_validate_target_accepts_localhost():
    validate_target("http://127.0.0.1:8000")

def test_validate_target_rejects_external_target():
    with pytest.raises(ValueError):
        validate_target("https://example.com")

def test_analyze_detects_missing_headers():
    present, missing = analyze({"content-security-policy": "default-src 'self'"})
    assert "content-security-policy" in present
    assert "x-frame-options" in missing
