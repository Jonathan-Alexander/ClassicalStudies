"""
Script run on rlogin as

python data_augment.py
"""
import pandas as pd

from time import clock
from math import floor

from sentiment_analysis import sentiment_analyzer_scores

if __name__ == '__main__':
    # Augment dataset with sentiment scores
    df = pd.read_csv('full-sample.csv')
    df = df.head().copy()
    print('START')
    start = clock()

    df['pos'], df['neg'], df['neu'] = zip(*df.apply(lambda row: sentiment_analyzer_scores(row['Text']), axis=1))
    stop = clock()
    df.to_csv('full-sample-with-sent.csv', sep=',', encoding='utf-8', index=False)
    print("Time elapsed =", floor((stop-start)/60), "minute(s), and", round((stop-start)%60, 1), "second(s)")
