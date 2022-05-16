from text_processor.text_processor import *
import re
import unicodedata
import nltk

import contractions
import inflect
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer

class TextProcessor:
    def __init__(self) -> None:
        pass

    def strip_html(self,text):
        """Remove html markup."""
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()


    def remove_between_square_brackets(text):
        """Remove open and close double brackets and anything in between."""
        return re.sub('\[[^]]*\]', '', text)


    def denoise_text(self,text):
        text = self.strip_html(text)
        text = self.remove_between_square_brackets(text)
        return text


    def replace_contractions(self,text):
        """Replace contractions in string of text."""
        return contractions.fix(text)


    def get_tokenized_list(self,doc_text):
        tokens = word_tokenize(doc_text)
        return tokens


    def remove_non_ascii(self,words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode(
                'ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words


    def to_lowercase(self,words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words


    def remove_punctuation(self,words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words


    def replace_numbers(self,words):
        """Replace all interger occurrences in list of tokenized words with textual representation"""
        p = inflect.engine()
        new_words = []
        for word in words:
            if word.isdigit():
                new_word = p.number_to_words(word)
                new_words.append(new_word)
            else:
                new_words.append(word)
        return new_words


    def remove_stopwords(self,words, language):
        """Remove stop words from list of tokenized words"""
        stop_words = set(stopwords.words(language))
        new_words = []
        for word in words:
            if word not in stop_words:
                new_words.append(word)
        return new_words


    def stem_words(self,words):
        """Stem words in list of tokenized words"""
        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems


    # def stem_words_1(words):
    #     ps = nltk.stem.PorterStemmer()
    #     stems = []
    #     for word in words:
    #         stems.append(ps.stem(word))
    #     return stems


    def lemmatize_words(self,words):
        """Lemmatize words in list of tokenized words"""
        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='n')
            lemma = lemmatizer.lemmatize(lemma, pos='v')
            lemma = lemmatizer.lemmatize(lemma, pos='a')
            lemma = lemmatizer.lemmatize(lemma, pos='r')
            lemma = lemmatizer.lemmatize(lemma, pos='s')
            lemmas.append(lemma)
        return lemmas


    def normalize(self,words, normalization_type, language):
        words = self.remove_non_ascii(words)
        words = self.to_lowercase(words)
        words = self.remove_punctuation(words)
        words = self.replace_numbers(words)
        words = self.remove_stopwords(words, language)

        if(normalization_type == 'stems'):
            return self.stem_words(words)

        elif(normalization_type == 'lemmas'):
            return self.lemmatize_words(words)

        elif(normalization_type == 'lemmas and stems'):
            return self.stem_and_lemmatize(words)

        elif(normalization_type == 'none'):
            return words

        else:
            return words


    def stem_and_lemmatize(self,words):
        lemmas = self.lemmatize_words(words)
        stems = self.stem_words(lemmas)
        return stems


    def preprocess_text(self,text, normalization_type, text_type, language):
        pt = text
        if text_type == 'html':
            pt = self.denoise_text(text)

        pt = self.replace_contractions(pt)
        words = self.get_tokenized_list(pt)
        words = self.normalize(words, normalization_type, language)
        return words
