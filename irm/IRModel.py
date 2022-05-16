class IRModel:  # Receive an iterable of docs
    def __init__(self, normalization_type='lemmas and stems', language='english'):
        self.normalization_type = normalization_type
        self.language = language
        self.doc_names = {}  # dict of num_doc -> url
        self.doc_vector = []  # Wij
        self.corpus = []
        self.cleaned_corpus = []
        self.num_docs = 0
        self.terms = []

    
    def processDocuments(self, docs, idiom):
        pass

    
    def processQuery(self, query):
        pass
