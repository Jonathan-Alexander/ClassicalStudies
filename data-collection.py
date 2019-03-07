import pandas as pd

df = pd.read_csv('PMC-ids.csv')
# Bash script to generated this txt file
retracted_df = pd.read_csv('pubmed_retracted_pmcids.txt', header=None, skip_blank_lines=False)
def clean(pmcid):
    pmcid = pmcid.split()[1]
    pmcid = pmcid.split(';')[0]
    return pmcid

# Rename column
retracted_df.columns = ['PMCID']
retracted_df['PMCID'] = retracted_df['PMCID'].map(lambda r: clean(r))
# Dataframe of open access subset
oa_df = pd.read_csv('oa_file_list.csv')
oa_df.head()
oa_df.columns
# Rename Accession ID -> PMCID to match
oa_df = oa_df.rename(columns={'Accession ID': 'PMCID'})
# Contains things in open subset AND in the main PMC-id csv
joined = df.merge(oa_df, how='inner', left_on='PMCID', right_on='PMCID')
joined.head()
oa_retracted_df = joined.merge(retracted_df, how='inner', left_on='PMCID', right_on='PMCID')
oa_retracted_df.shape
oa_retracted_df.head()
# Clean table for duplicate columns PMID_x/PMID_y => True means they are duplicates
(oa_retracted_df['PMID_x'] == oa_retracted_df['PMID_y']).all()
# axis = 1 means drop column
oa_retracted_df.drop(labels=['PMID_y'], axis=1, inplace=True)
# Rename PMID_x -> PMID
oa_retracted_df = oa_retracted_df.rename(columns={'PMID_x': 'PMID'})
oa_retracted_df
# Write to file
oa_retracted_df.to_csv('oa-table.csv', sep=',', encoding='utf-8')
# pd.show_versions()

