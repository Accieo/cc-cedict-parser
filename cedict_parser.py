from dataclasses import dataclass, field
from typing import List

@dataclass
class CEDICTRow:
    traditional: str = ""
    simplified: str = ""
    pinyin: str = ""
    english: List[str] = field(default_factory=list)

def cedit_ts_parser(path: str = "cedict_ts.u8") -> List[CEDICTRow]:
    """
    Parses the CC-CEDICT Chinese-English dictionary data.

    Content of cedict_ts.u8 is expected to be as follows:
        traditional simplified [pinyin] /english/

    CC-CEDICT is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.

    For more information, see:
        https://www.mdbg.net/chinese/dictionary?page=cc-cedict

    Args:
        path (str): Path to the cedict_ts.u8 file.

    Returns:
        list[CEDICTRow]: Parsed entries as a list of CEDICTRow objects.
    """
    entries: List[CEDICTRow] = []
    with open(path, "r") as file:
        for line in file:
            rec = CEDICTRow()

            # traditional
            space_index = line.find(" ")
            rec.traditional = line[:space_index]
            line = line[space_index:].strip()
            # simplified
            space_index = line.find(" ")
            rec.simplified = line[:space_index]
            line = line[space_index:].strip()
            # pinyin
            closing_bracket_index = line.find("]")
            rec.pinyin = line[1:closing_bracket_index]
            line = line[closing_bracket_index + 1:].strip()
            # english
            rec.english = list(filter(None, line.split("/")))
            
            entries.append(rec)

    return entries