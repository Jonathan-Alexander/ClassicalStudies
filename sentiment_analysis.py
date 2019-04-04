from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # pip install vaderSentiment
from text_processing import get_full_text_by_pmcid
import pandas as pd

# Gets the positive, negative, or neutral sentiment scores of a given text
def sentiment_analyzer_scores(sentence):
    analyser = SentimentIntensityAnalyzer()
    if sentence is not None and type(sentence) == str:
        score = analyser.polarity_scores(sentence)
        return score['pos'], score['neg'], score['neu']
    else:
        return 0
    # print("{:-<40} {}".format(sentence, str(score)))

if __name__ == "__main__":
    df = pd.read_csv('full-table.csv')
    avg_pos_retracted = 0
    avg_neg_retracted = 0
    avg_neu_retracted = 0
    avg_pos_non_retracted = 0
    avg_neg_non_retracted = 0
    avg_neu_non_retracted = 0
    count_retracted = 0
    count_non_retracted = 0

    # print(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][0]), "pos"))
    # print(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][1]), "pos"))
    # print(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][2]), "pos"))
    
    # Finds the average sentiment score for retracted and non-retracted articles
    for row in range(len(df.index)):
        type = df['_merge'][row]
        if type == "both" and get_full_text_by_pmcid(df["PMCID"][row]) is not None:
            avg_pos_retracted += int(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][row]), "pos"))
            avg_neg_retracted += int(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][row]), "neg"))
            avg_neu_retracted += int(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][row]), "neu"))
            # print("BOTH: " + str(avg_pos_retracted))
            count_retracted += 1
        elif type == "left_only" and get_full_text_by_pmcid(df["PMCID"][row]) is not None:
            avg_pos_non_retracted += int(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][row]), "pos"))
            avg_neg_non_retracted += int(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][row]), "neg"))
            avg_neu_non_retracted += int(sentiment_analyzer_scores(get_full_text_by_pmcid(df["PMCID"][row]), "neu"))
            # print("LEFT: " + str(avg_pos_non_retracted))
            count_non_retracted += 1

    avg_pos_retracted /= count_retracted
    avg_neg_retracted /= count_retracted
    avg_neu_retracted /= count_retracted

    avg_pos_non_retracted /= count_non_retracted
    avg_neg_non_retracted /= count_non_retracted
    avg_neu_non_retracted /= count_non_retracted

    # Prints out the scores
    print("AVG POS RETRACTED: " + str(avg_pos_retracted))
    print("AVG NEG RETRACTED: " + str(avg_neg_retracted))
    print("AVG NEU RETRACTED: " + str(avg_neu_retracted))
    print("AVG POS NON-RETRACTED: " + str(avg_pos_non_retracted))
    print("AVG POS NON-RETRACTED: " + str(avg_pos_non_retracted))
    print("AVG POS NON-RETRACTED: " + str(avg_pos_non_retracted))
