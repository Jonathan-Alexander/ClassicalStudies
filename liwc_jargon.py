from Liwc import LiwcAnalyzer
from text_processing import get_full_text_by_pmcid
import pandas as pd

def get_jargon():
    full_df = pd.read_csv('full-sample.csv')
    liwc = LiwcAnalyzer()
    liwc_results = liwc.parse(full_df["Text"])
    new_df = pd.DataFrame()
    new_df["PMCID"] = full_df["PMCID"]
    new_df["Jargon"] = liwc_results["dic"].map(lambda r: 1 - r)
    print(new_df.head())
    return new_df

get_jargon()