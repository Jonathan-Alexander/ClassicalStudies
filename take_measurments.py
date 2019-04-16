#Create Data.csv

import pandas as pd
import numpy
import pubmed_parser as pp 
import time

JCR = pd.read_csv('JournalHomeGrid_withISSN.csv', index_col = 2, thousands=',', na_values=['Not Available'], dtype={'Rank' : 'int', 'Full Journal Title' : 'str', 'ISSN': 'str', 'Total Cites' : 'int', 'Journal Impact Factor' : 'float', 'Eigenfactor Score' : 'float'})
sample = pd.read_csv('full-sample-with-sent.csv', sep=',', keep_default_na=False, dtype={"ISSN":"str"})

citations = []
t_cited = []
authors = []
keys = []
JIF = []

for index, row in sample.iterrows():
    
    time.sleep(0.33)
    issn = row["ISSN"] if (row["ISSN"] != "") else row["eISSN"]    
    pmid = row['PMID']
    pmcid = row['PMCID'][3:]
    try:
        web_xml_out = pp.parse_xml_web(pmid)
    except Exception as e:
        web_xml_out = {'authors':'Parse XML Web Failed for PMID: {}'.format(pmid), 'keywords':'Parse XML Web Failed for PMID: {}'.format(pmid)}
        print('Parse XML Web Failed for PMID: {}'.format(pmid))
    num_citations = pp.parse_citation_web(pmcid, id_type ='PMC')
    times_cited = pp.parse_outgoing_citation_web(pmcid)
    if times_cited is not None:
        times_cited = times_cited['n_citations']
    else:
        times_cited = -1
    if(num_citations != None):
        num_citations = num_citations['n_citations']
    else:
        num_citations = -1    
    num_authors = len(web_xml_out['authors'].split(';'))
    keywords = web_xml_out['keywords']
    #assert keywords != ''
    try:
        impact_factor = JCR.loc[issn,'Journal Impact Factor'] if (issn != '') else -1
    except KeyError as e:
        impact_factor = 0

    citations.append(num_citations)
    t_cited.append(times_cited)
    authors.append(num_authors)
    keys.append(keywords)
    JIF.append(impact_factor)
   
sample['Citations'] = citations
sample['Times Cited'] = t_cited
sample['Number Authors'] = authors
sample['Keywords'] = keys
sample['Journal Impact Factor'] = JIF
sample.to_csv('full-sample-test.csv', sep=',', encoding='utf-8')




    

