import re

housing_aliases = {
    "heritage": "Heritage",
    "century": "Century",
    "mccarthy": "McCarthy",
    "west 27th": "West 27th Place",
    "cardinal": "Cardinal Gardens",
    "webb tower": "Webb Tower",
    "parkside" : "Parkside",
    "jefferson flats": "Jefferson Flats",
    "the standard": "The Standard",
    "gateway": "University Gateway",
    "lorenzo": "Lorenzo",
    "tuscany": "Tuscany",
    "usc village": "USC Village",
    "the village": "USC Village",
}

def find_complexes(comment):
    text = str(comment).casefold()
    matches = set()

    for alias, canonical_name in housing_aliases.items():
        pattern = r"\b" + re.escape(alias) + r"\b"

        if re.search(pattern, text):
            matches.add(canonical_name)

    return sorted(matches)

address_pattern = re.compile(
    r"\b\d{1,6}\s+"
    r"(?:(?:North|South|East|West|N|S|E|W)\.?\s+)?"
    r"(?:[A-Za-z0-9'-]+\s+){1,5}"
    r"(?:Avenue|Ave|Street|St|Road|Rd|Boulevard|Blvd|"
    r"Drive|Dr|Lane|Ln|Place|Pl|Court|Ct)\b\.?",
    re.IGNORECASE,
)

def find_addresses(comment):
    return [
        match.group(0)
        for match in address_pattern.finditer(str(comment))
    ]