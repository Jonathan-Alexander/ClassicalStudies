from sklearn.metrics import mean_absolute_error
class Classifier:
    '''
    Classifier using basic random train/test
    '''
    def __init__(self, skmodel, args={}):
        self.model = skmodel(**args)
    def fit(self, X, y):
        self.model.fit(X, y)
    def mae(self, X_val, y_val):
        return mean_absolute_error(self.model.predict(X_val), y_val)

if __name__ == '__main__':
    # sample usage, pick any model
    from sklearn.tree import DecisionTreeRegressor
    import pandas as pd
    from sklearn.model_selection import train_test_split

    df = pd.read_csv('data.csv')

    features = ['gunning_fog', 'wps', 'neu']
    target = ['Retracted']

    X = df[features]
    y = df[target]
    model = Classifier(DecisionTreeRegressor, args={'random_state': 1})
    X_train, X_val, Y_train, Y_val = train_test_split(X, y, random_state=0)
    model.fit(X_train, Y_train)
    print(model.mae(X_val, Y_val))
