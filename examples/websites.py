import pandas as pd

from visions.core.implementations import visions_complete_set
from visions.core.functional import type_cast, type_inference
from visions.core.summaries.summary import CompleteSummary


# Load dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/berkmancenter/url-lists/master/lists/et.csv",
    parse_dates=["date_added"],
)

# Type
typeset = visions_complete_set()

# Type inference
inferred_types = type_inference(df, typeset)
print(inferred_types)

# Type cast
cast_df, cast_types = type_cast(df, typeset)
print(cast_types)

# Summarization
summary = CompleteSummary()
summaries = summary.summarize(cast_df, cast_types)
for key, variable_summary in summaries["series"].items():
    print(key, variable_summary)
