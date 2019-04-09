#pubmed_parser_test

import pandas
import pubmed_parser as pp
from sqlalchemy import create_engine
from sets import Set

df = pandas.read_csv('full-table.csv')
JCR_df = pandas.read_csv('JournalHomeGrid_withISSN.csv', index_col = "ISSN")


for index, row in df.iterrows():
    if(row['_merge'] == 'both'):
        #print(count)
        pmid = row['PMID_x']
        pmcid = row['PMCID'][3:]
        issn = row['ISSN']
        
        #print(pmcid)
        web_xml_out = pp.parse_xml_web(pmid)
        num_citations = pp.parse_citation_web(pmcid, id_type ='PMC')
        times_cited = pp.parse_outgoing_citation_web(pmcid)
        JIF_row = JCR_df.loc[issn]
        JIF = JIF_row['Journal Impact Factor']
        num_citations = num_citations['n_citations'] if (num_citations != None) else 'Article Not Found'
        times_cited = times_cited['n_citations'] if (num_citations != None) else 'Article Not Found'
        #results.append([web_xml_out['title'], web_xml_out['journal'], web_xml_out['authors'], web_xml_out['keywords'], num_citations, times_cited])
                
        
        print('Title: ' + web_xml_out['title'])
        print("\t- Journal: " + web_xml_out['journal'])
        print("\t- Authors: " + web_xml_out['authors'])
        print("\t- Keywords: " + web_xml_out['keywords'])
        print("\t- Articles Cited: " + str(num_citations))
        print("\t- Times Cited: " + str(times_cited))
        print("\t- Journal Impact Factor: " + str(JIF))



