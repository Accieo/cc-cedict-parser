# cc-cedict-parser
Simple Python tool with no external dependencies to parse and search [CC-CEDICT](https://cc-cedict.org/wiki/), a Chinese-English dictionary. Useful for language learning, linguistic research, and NLP tasks involving Mandarin Chinese.

## Features

- Parses the [official](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) `cedict_ts.u8` file into structured Python objects.
- Supports shell-style wildcard searches for:
  - English definitions
  - Simplified Chinese
  - Traditional Chinese  

Example:
```python
match_english("to *", entries)        # Matches definitions starting with "to "  
match_english("* love *", entries)    # Matches definitions containing " love "  
match_english("to ?ay", entries)      # Matches "to say", "to pay", etc.  
match_english("[Tt]he *", entries)    # Matches definitions starting with "The" or "the"  
match_english("[!Tt]he *", entries)   # Matches definitions starting with anything except "The" or "the"  
```

## Installation

1. Clone the repository.
```bash
git clone https://github.com/Accieo/cc-cedict-parser.git && cd cc-cedict-parser
```

2. Download the `cedict_ts.u8` dictionary file from an [official](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) source.
  
3. See `main.py` and use it as reference to develop your own scripts.

## License

MIT License © 2025 Accieo

This tool **does not include** CC-CEDICT data. It is only designed to parse and work with data from [CC-CEDICT](https://cc-cedict.org/wiki/), which is licensed separately under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). If you use their data, you must follow their license.