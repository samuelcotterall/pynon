# anon.py
# This script uses Microsoft Presidio to anonymize a string of text.
# Requirements: presidio-analyzer, presidio-anonymizer

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

def anonymize_text(text):
    analyzer = AnalyzerEngine()
    anonymizer = AnonymizerEngine()
    # Analyze the text for PII entities
    results = analyzer.analyze(text=text, language='en')
    # Anonymize the detected entities
    anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results)
    return anonymized_result.text

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python anon.py '<text to anonymize>'", file=sys.stderr)
        sys.exit(1)
    input_text = sys.argv[1]
    print(anonymize_text(input_text))
