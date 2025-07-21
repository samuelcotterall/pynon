# PyNon

PyNon is a simple Python tool that uses Microsoft Presidio to anonymize text containing personally identifiable information (PII).

## Features

- Detects and anonymizes PII in English text using Presidio Analyzer and Anonymizer
- Command-line interface for quick anonymization

## Requirements

- Python 3.7+
- presidio-analyzer
- presidio-anonymizer
- spaCy (with the `en_core_web_lg` model)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/samuelcotterall/pynon.git
   cd pynon
   ```
2. (Recommended) Create and activate a virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Install the required spaCy model:
   ```sh
   python -m spacy download en_core_web_lg
   ```

## Usage

### As a script

```sh
python anon.py 'My name is John Doe and my phone number is 555-123-4567.'
```

### As a CLI tool

You can use the provided CLI script:

```sh
./pynon 'My name is John Doe and my phone number is 555-123-4567.'
```

If you want to run `pynon` from anywhere, add it to your PATH or symlink it to a directory in your PATH.

**Note:** Always activate your virtual environment before running the tool to ensure all dependencies and models are available.

## Troubleshooting

If you see an error about the spaCy model not being installed, run:

```sh
python -m spacy download en_core_web_lg
```

## License

MIT
