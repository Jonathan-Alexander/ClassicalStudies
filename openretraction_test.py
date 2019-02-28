#Test script of integrating the open retraction database with PMC Data
#Takes ID of article from articles list and prints JSON of it it's retracted
import requests
import csv

def get_dois(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            # Instead of printing, make a GET request with each row["DOI"]
            # print(row["DOI"] + '\n')
            print(is_retracted(row['DOI']))

def is_retracted(doi):
    r = requests.get('http://openretractions.com/api/doi/{}/data.json'.format(doi)).json()
    # print(r)
    if 'retracted' in r and r['retracted']:
        return True
    return False

if __name__ == '__main__':
    # r = requests.get('http://openretractions.com/api/doi/10.1002/job.1787/data.json')

    # print(is_retracted('10.1016/j.atherosclerosis.2009.08.003'))
    # print(r.json())
    
    # top-level script stuff
