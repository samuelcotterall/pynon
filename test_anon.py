
from anon import anonymize_text

def test_anonymize_text_removes_pii():
    text = "My name is John Doe and my phone number is 555-123-4567."
    result = anonymize_text(text)
    # Presidio replaces PII with <PERSON> and <PHONE_NUMBER> or similar
    assert "John Doe" not in result
    assert "555-123-4567" not in result

def test_anonymize_text_no_pii():
    text = "This is a generic sentence with no PII."
    result = anonymize_text(text)
    # Accept that Presidio may over-detect PII, but output should be a string and not error
    assert isinstance(result, str)
    # Check that no <PERSON> or <PHONE_NUMBER> markers are present
    assert "<PERSON>" not in result
    assert "<PHONE_NUMBER>" not in result


