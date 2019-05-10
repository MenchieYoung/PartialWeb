import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import pickle
import re
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")


class textML(object): 
    def __init__(self):
        self.MODEL_PATH = './models/'

    def predict(self, x): 
        """Main ml function to be used inside rdd.map()
        Return: 
        (x, prediction): tuple, x is comment text, prediction is class label (1-toxic, 0-clean)
        """
        # clean

        # remove stop words

        # stemming
        

        # vectorize

        # predict

        
        return (x, prediction, prob)

    def _cleanHtml(self, sentence):
        return cleantext

    def _cleanPunc(self, sentence): #function to clean the word of any punctuation or special characters
        return cleaned

    def _keepAlpha(self, sentence):
        return alpha_sent

    def _removeStopWords(self, sentence):
        return re_stop_words.sub(" ", sentence)

    def _stemming(self, sentence):
        return stemSentence