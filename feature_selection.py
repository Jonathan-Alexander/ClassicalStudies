if __name__ == '__main__':
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVR
    from sklearn.feature_selection import RFE

    df = pd.read_csv('data.csv')

    features = ['gunning_fog', 'pos', 'neg', 'neu', 'Citations', 'Times Cited', 'Number Authors', 'Journal Impact Factor', 'wc', 'sc', 'wps', 'dic', 'sixltr', 'insight', 'cause', 'discrep', 'tentat', 'certain', 'quant', 'numbers', 'jargon']
    # features = ['article-type']
    target = ['Retracted']

    X = df[features]
    y = df[target]
    X_train, X_val, Y_train, Y_val = train_test_split(X, y, random_state=0)

    estimator = SVR(kernel="linear")
    selector = RFE(estimator, 5, step=1)
    selector = selector.fit(X, y)
    print(selector.support_)
    print(selector.ranking_)

    # Results from running above code with just the training datasets
    # print("Recursive Feature Elimination Results from Most to Least Significant:")
    # print(features[1], ",", features[11], ",", features[15], ",", features[19], ",", features[20])
    # print(features[2])
    # print(features[14])
    # print(features[18])
    # print(features[16])
    # print(features[17])
    # print(features[6])
    # print(features[0])
    # print(features[3])
    # print(features[13])
    # print(features[7])
    # print(features[5])
    # print(features[10])
    # print(features[4])
    # print(features[9])
    # print(features[8])
    # print(features[12])

    # Feature Elimination Results:
    # [ 8  1  2  9 14 12  7 11 16 15 13  1 17 10  3  1  5  6  4  1  1]
    # Feature Elimination Results from Most to Least Significant:
    # pos , dic , discrep , numbers , jargon
    # neg
    # cause
    # quant
    # tentat
    # certain
    # Number Authors
    # gunning_fog
    # neu
    # insight
    # Journal Impact Factor
    # Times Cited
    # wps
    # Citations
    # sc
    # wc
    # sixltr





    # Results from running above code with the full datasets
    # print("Recursive Feature Elimination Results from Most to Least Significant:")
    # print(features[1], ",", features[11], ",", features[14], ",", features[19], ",", features[20])
    # print(features[18])
    # print(features[15])
    # print(features[2])
    # print(features[3])
    # print(features[13])
    # print(features[17])
    # print(features[16])
    # print(features[6])
    # print(features[0])
    # print(features[5])
    # print(features[7])
    # print(features[4])
    # print(features[10])
    # print(features[9])
    # print(features[8])
    # print(features[12])

    # Feature Elimination Results from Most Significant to Least Significant
    # pos , dic , cause , numbers , jargon
    # quant
    # discrep
    # neg
    # neu
    # insight
    # certain
    # tentat
    # Number Authors
    # gunning_fog
    # Times Cited
    # Journal Impact Factor
    # Citations
    # wps
    # sc
    # wc
    # sixltr