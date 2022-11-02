import csv
import re
import sys

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from TextExtractedModificator import text_modificator
from Abreviation_Slang import other_clean
from Contractions import main_contraction
from EmojiRemover import remove_emoji
from NumberRemover import remove_number
from URLRemover import remove_URL


def prediction(TextExtracted):
    if TextExtracted == '':
        print('No text detected. Try to take a better picture or add some light to it.')
        import textscanner
        textscanner.textscanner()
    else:
        # transfer du doc csv
        df = pd.read_csv('language-identification-datasets.csv')
        # division en 2 array pour text et language
        x = df['Text']
        y = df['Language']
        X_train = x[0:24326]
        y_train = y[0:24326]

        df.apply(
         lambda row: main_contraction(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)
        x.apply(remove_number)
        x.apply(remove_URL)
        df.apply(
            lambda row: remove_emoji(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)
        df.apply(
             lambda row: other_clean(row["Text"]) if row["Language"] == "English" else row["Text"], axis=1)

        text_modificator(TextExtracted)
        TextExtracted = [TextExtracted]
        print(TextExtracted[0])
        confirmation = input('Is this the text you want to translate? (y/n) ')

        if confirmation == 'y':
            model = Pipeline([('vect', CountVectorizer()), ('clf', DecisionTreeClassifier())])
            model.fit(X_train, y_train)
            x_prediction = model.predict(TextExtracted)
            print("The language used in this text is " + str(x_prediction))
        else:
            Option = input('Do you want to type the text you want to detect or try again? (s/t) ')
            if Option == 's':
                TextExtracted = input('Type the text you want to detect: ')
                prediction(TextExtracted)
            else:
                import textscanner
                textscanner.textscanner()
                import MLrecognition
                MLrecognition.prediction(MLrecognition.TextExtracted)
