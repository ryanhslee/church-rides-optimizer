from pathlib import Path
import pandas as pd
from address_parser import find_complexes, find_addresses

file_path = (
    Path(__file__).parent
    / "data"
    / "church_rides_mixed_campuses_four_weeks.xlsx"
)

responses = pd.read_excel(file_path, sheet_name=0)
responses.columns = responses.columns.str.strip() #clean leading whitespace in column headers

usc_responses = responses.loc[
    responses["School"] == "USC"
].copy()

#1 - defining friday attendees
friday_column = "Will you be attending CG's this Friday Night?"
attending_friday = usc_responses[friday_column] == "Yes"

friday_early_column = next(
    column
    for column in usc_responses.columns
    if column.startswith("Do you need to leave early on Friday to serve for worship?")
)
friday_early = usc_responses[friday_early_column] == "Early for worship"

friday_felly_column = next(
    column
    for column in usc_responses.columns
    if column.startswith("Would you prefer to stay for fellowship after CG's,")
)
friday_felly = usc_responses[friday_felly_column] == "Stay for felly"

#2 - defining sunday attendees
sunday_column = "Will you be attending church service this Sunday?"
attending_sunday = usc_responses[sunday_column] == "Yes"

sunday_early_column = next(
    column
    for column in usc_responses.columns
    if column.startswith("Do you need to leave early on Sunday to serve")
)
sunday_early = usc_responses[sunday_early_column] == "Early for Children's/Youth"

sunday_felly_column = next(
    col
    for col in usc_responses.columns
    if col.startswith("Would you prefer to stay for fellowship after service on Sunday,")
)
sunday_felly = usc_responses[sunday_felly_column] == "Stay for lunch"

'''
#3 - show results
print(f"Total responses: {len(responses)}")
print(f"USC responses: {len(usc_responses)}")

print(f"Friday attendees: {attending_friday.sum()}")
print(f"Friday early: {(attending_friday & friday_early).sum()}")
print(f"Friday fellowship: {(attending_friday & friday_felly).sum()}")

print(f"Sunday attendees: {attending_sunday.sum()}")
print(f"Sunday early: {(attending_sunday & sunday_early).sum()}")
print(f"Sunday fellowship: {(attending_sunday & sunday_felly).sum()}")
'''

#3 - location
location_column = "Where are you located?"
comments_column = "Any questions, comments, or concerns?"

comments_column = "Any questions, comments, or concerns?"

usc_responses["complex_candidates"] = (
    usc_responses[comments_column].apply(find_complexes)
)
usc_responses["address_candidates"] = (
    usc_responses[comments_column].apply(find_addresses)
)

print(
    usc_responses[
        [
            "Name (First and Last)",
            comments_column,
            "complex_candidates",
            "address_candidates",
        ]
    ].to_string(index=False)
)