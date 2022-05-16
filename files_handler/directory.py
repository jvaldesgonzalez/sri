import os
from format_handling import extract_text_from_txt, extract_text_from_pdf

class Directory:
    def __init__(self) -> None:
        pass
    def file_extension(filename):
        return filename.split('.')[-1]


    def extract_text(self,path, filename):
        ext = self.file_extension(filename)
        if ext == 'txt':
            text = extract_text_from_txt(path+'/'+filename)
        elif ext == 'pdf':
            text = extract_text_from_pdf(path+'/'+filename)
        else:
            raise Exception('Format not allowed by the system.')

        return text


    def list_directory(self,basepath):
        # N: number of document that have extension .txt or .pdf
        files = (entry for entry in os.listdir(basepath) if os.path.isfile(
            os.path.join(basepath, entry)) and self.file_extension(entry) in {'txt', 'pdf'})
        for doc in files:
            yield (doc, self.extract_text(basepath, doc))
