import fnmatch
from typing import List
from cedict_parser import CEDICTRow

def match_english(needle: str, haystack: List[CEDICTRow]) -> List[CEDICTRow]:
    """
    Search for English definitions matching the given pattern.

    This uses Unix shell-style wildcards:
        \\*  matches any sequence of characters
        \\?  matches any single character
        [seq] matches any character in seq
        [!seq] matches any character not in seq

    Example:
        ```
        match_english("to *", entries)        # Matches definitions starting with "to "  
        match_english("* love *", entries)    # Matches definitions containing " love "  
        match_english("to ?ay", entries)      # Matches "to say", "to pay", etc.  
        match_english("[Tt]he *", entries)    # Matches definitions starting with "The" or "the"  
        match_english("[!Tt]he *", entries)   # Matches definitions starting with anything except "The" or "the"  
        ```

    Args:
        needle: The search pattern (supports shell-style wildcards).
        haystack: A list of CEDICTRow entries to search through.

    Returns:
       List[CEDICTRow]: A list of CEDICTRow objects whose English definitions match the pattern.
    """
    return [
        entry for entry in haystack
        if any(fnmatch.fnmatch(definition, needle) for definition in entry.english)
    ]

def match_simplified(needle: str, haystack: List[CEDICTRow]) -> List[CEDICTRow]:
    """
    Search for a simplified Chinese word matching the given pattern.

    This uses Unix shell-style wildcards:
        \\*  matches any sequence of characters
        \\?  matches any single character
        [seq] matches any character in seq
        [!seq] matches any character not in seq

    Example:
        ```
        match_simplified("我*", entries)         # Matches words starting with 我
        match_simplified("*学*", entries)        # Matches words containing 学
        match_simplified("你?", entries)         # Matches two-character words starting with 你
        match_simplified("[他她]*", entries)     # Matches words starting with 他 or 她
        match_simplified("[!我你]*", entries)    # Matches words not starting with 我 or 你
        ```

    Args:
        needle: The search pattern (supports shell-style wildcards).
        haystack: A list of CEDICTRow entries to search through.

    Returns:
       List[CEDICTRow]: A list of CEDICTRow objects whose simplified Chinese characters match the pattern.
    """
    return [
        entry for entry in haystack
        if fnmatch.fnmatch(entry.simplified, needle)
    ]

def match_traditional(needle: str, haystack: List[CEDICTRow]) -> List[CEDICTRow]:
    """
    Search for a traditional Chinese word matching the given pattern.

    This uses Unix shell-style wildcards:
        \\*  matches any sequence of characters
        \\?  matches any single character
        [seq] matches any character in seq
        [!seq] matches any character not in seq

    Example:
        ```
        match_traditional("愛*", entries)        # Matches words starting with 愛
        match_traditional("*國*", entries)       # Matches words containing 國
        match_traditional("你?", entries)        # Matches two-character words starting with 你
        match_traditional("[學教]*", entries)    # Matches words starting with 學 or 教
        match_traditional("[!愛心]*", entries)   # Matches words not starting with 愛 or 心
        ```

    Args:
        needle: The search pattern (supports shell-style wildcards).
        haystack: A list of CEDICTRow entries to search through.

    Returns:
       List[CEDICTRow]: A list of CEDICTRow objects whose traditional Chinese characters match the pattern.
    """
    return [
        entry for entry in haystack
        if fnmatch.fnmatch(entry.traditional, needle)
    ]
