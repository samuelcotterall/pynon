# anon.py
# This script uses Microsoft Presidio to anonymize a string of text.
# Requirements: presidio-analyzer, presidio-anonymizer


from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_analyzer.nlp_engine import NlpEngineProvider

def anonymize_text(text):
    # Use Presidio's NlpEngineProvider to load spaCy model
    try:
        provider = NlpEngineProvider(nlp_configuration={
            "nlp_engine_name": "spacy",
            "models": [{"lang_code": "en", "model_name": "en_core_web_lg"}]
        })
        nlp_engine = provider.create_engine()
    except OSError:
        print(
            "Error: spaCy model 'en_core_web_lg' is not installed.\n"
            "Install it in your environment with:"
            "\n    python -m spacy download en_core_web_lg\n",
            file=sys.stderr
        )
        sys.exit(1)
    analyzer = AnalyzerEngine(nlp_engine=nlp_engine)
    anonymizer = AnonymizerEngine()
    # Analyze the text for PII entities
    results = analyzer.analyze(text=text, language='en')
    # Anonymize the detected entities
    anonymized_result = anonymizer.anonymize(
        text=text, analyzer_results=results
    )
    return anonymized_result.text

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python anon.py '<text to anonymize>'", file=sys.stderr)
        sys.exit(1)

    input_text = sys.argv[1]
    print(anonymize_text(input_text))
