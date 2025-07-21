# PyNon

A simple Python script that uses Microsoft Presidio to anonymize text containing personally identifiable information (PII).

## Features

- Detects and anonymizes PII in English text using Presidio Analyzer and Anonymizer.
- Command-line interface for quick anonymization.

## Requirements

- Python 3.7+
- presidio-analyzer
- presidio-anonymizer

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/PyNon.git
   cd PyNon
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

```sh
python pynon.py 'My name is John Doe and my phone number is 555-123-4567.'
```

## License

MIT
