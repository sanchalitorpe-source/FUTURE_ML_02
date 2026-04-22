from src.preprocessing import clean_text

def test_clean_text_basic():
    text = "Hello!!! This is TESTING 123"
    result = clean_text(text)
    assert isinstance(result, str)
    assert "test" in result