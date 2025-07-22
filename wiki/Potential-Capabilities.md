# Potential Capabilities for PyNon

### Effort/Reward Key

- 🟢 = Low (1) | 🟡 = Medium (3) | 🔴 = High (5)
- ⭐ = Low (1) | ⭐⭐ = Medium (3) | ⭐⭐⭐ = High (5)

Below are some features that could be added to PyNon by leveraging Microsoft Presidio's advanced capabilities:

## 1. Custom Recognizers 🔴 / ⭐⭐⭐

Let users add their own regex or ML-based recognizers for domain-specific PII.

## 2. Customizable Entities 🟢 / ⭐⭐⭐

Allow users to specify which PII entities to detect/anonymize (e.g., only names, only phone numbers, etc.).

## 3. Redaction Methods 🟡 / ⭐⭐⭐

Support different anonymization strategies (replace with labels, mask, hash, or randomize).

## 4. Batch Processing 🟡 / ⭐⭐⭐

Accept a file or directory of files and anonymize all at once.

## 5. Output Formats � / ⭐⭐⭐

Support output as JSON, CSV, or annotated text.

## 6. Reversible Anonymization 🔴 / ⭐⭐⭐

Allow anonymization to be reversible by storing a mapping of substitutions, so anonymized data can be restored to its original form if needed.

## 7. Entity Highlighting � / ⭐⭐

Output the detected PII entities and their types before/after anonymization.

## 8. Language Support 🟡 / ⭐⭐

Allow selection of language for PII detection (Presidio supports multiple languages).

## 9. Confidence Threshold 🟢 / ⭐⭐

Let users set a minimum confidence score for PII detection.

## 10. Interactive Mode 🔴 / ⭐⭐

Prompt the user for confirmation before anonymizing each detected entity.

---

For more details or to suggest additional features, please open an issue or contribute to the project!
