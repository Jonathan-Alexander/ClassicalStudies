from bs4 import BeautifulSoup
import requests
import textstat # pip install textstat
import nltk
from time import sleep

def get_full_text_by_pmcid(pmcid):
    '''
    pmcid: str, assumes formatted as ex. PMC3933519
    returns the full text as a string
    '''
    pmcid = pmcid[3:]
    st = []
    try:
        sleep(0.4)
        r = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={}'.format(pmcid))
        if r.status_code == 200:
            # Get rid of the bracket citation in the raw text
            text = r.text.replace('[', '').replace(']', '')
            soup = BeautifulSoup(text, 'lxml') 
            tags = soup.find_all(name='sec')
            for tag in tags:
                for x in tag.find_all('xref'):
                    x.extract()
                for x in tag.find_all('title'):
                    x.extract()
                full_text = tag.text.replace(',', '')
                full_text = full_text.replace('\n', ' ')
                full_text = full_text.replace('(', '')
                full_text = full_text.replace(')', '')
                st.append(full_text)
                
            return ''.join(st)
        else:
            raise Exception('GET for PMC{} failed, not status 200, status of {}, text={}'.format(pmcid, r.status_code, r.text))
    except requests.exceptions.RequestException as e:
        print('GET for PMC{} failed, {}'.format(pmcid, str(e)))
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    # test out textstat library
    full = get_full_text_by_pmcid('PMC3933519')
    textstat.lexicon_count(full)
    print(textstat.smog_index(full))
