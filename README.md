
# ClassicalStudies
Capstone Project

## Setup
Using Anaconda 3.6:

```
$ python3 -m virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Also clone [pubmed_parser](https://github.com/titipata/pubmed_parser) and add it to the working directory.

## Data Collection, Sampling, Augmentation
1. Generate ids of retracted papers (`pubmed_retracted_pmcids.txt`)

Using Node v.10.4.0 and npm 6.1.0

```
$ npm install bionode-ncbi
$ npm install node-jq
$ ./pubmed_retractions.sh
```

2. Download index `PMC-ids.csv` and `oa_file_list.csv` from [Pubmed FTP server](https://ftp.ncbi.nlm.nih.gov/pub/pmc/)

3. Run `data_collection.ipynb`
This file merges the three indices together:  `pubmed_retracted_pmcids.txt`, `PMC-ids.csv`, `oa_file_list.csv`.
This file also 
* handles logic for creating control groups using stratified random sampling (stratified by journal titles)
* retrieves full text for all articles in our dataset
* computes readability scores

Running this file creates `full-sample.csv`

4. Run `python data_augment.py`, which augments dataset with sentiment scores and creates `full-sample-with-sent.csv`

5. Run `liwc_analysis.ipynb` to add LIWC features and combine datasets to produce `full-data.csv`

6. Run `clean.py` to clean the full text we retrieved (changes case, and removes numbers, punctuation, and stop words) to produce `full-data-clean.csv`

7. Run `take_measurments.py` (adds metadata features such as number of citations, authors, keywords, times cited) to produce `full-sample-test.csv`

8. Run `combined.ipynb` to combine intermediate datasets and produce a final dataset used for classification, named `data.csv` 

## Statistical Analysis and Visualizations
 Statistical analysis contained in `stats.ipynb`, `visualizations.ipynb` , `classical-studies-milestone-2.ipynb`, `wordcloud.ipynb`:
* Normality testing for each feature in each sample type
* Nonparametric testing for sample means for retracted vs. nonretracted articles
* Visualizes differences in sample means
* Confusion matrix visualization

## Feature Analysis
Contained in `feature-selection.py` and in `stats.ipynb`

## Classifiers
Run `compare_classifiers.py`
