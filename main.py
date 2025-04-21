from cedict_parser import cedit_ts_parser
from cedict_utils import match_english, match_simplified, match_traditional

def main():
    entries = cedit_ts_parser(path="cedict_ts.u8")

    # English definition search
    en_results = match_english("to ?ay", entries)
    for result in en_results:
        # Access values
        print(f"English: {result.english}, Pinyin: {result.pinyin}, Chinese: {result.simplified}")

    # Simplified Chinese search
    s_zh_results = match_simplified("学*", entries)
    for result in s_zh_results:
        # Access values
        print(f"English: {result.english}, Pinyin: {result.pinyin}, Chinese: {result.simplified}")

    # Traditional Chinese search
    t_zh_results = match_traditional("愛*", entries)
    for result in t_zh_results:
        # Access values
        print(f"English: {result.english}, Pinyin: {result.pinyin}, Chinese: {result.simplified}")

if __name__ == "__main__":
    main()