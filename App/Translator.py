
import os
import pickle
from datetime import datetime
from deep_translator import GoogleTranslator


class Translator:
    """This will translate the words into another language

    German to English language conversions were done through https://www.onlinedoctranslator.com/app/translationprocess-pdf

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        file (str): Path to root directory containing all of the pdf documents to extract.

    Attributes:
        root_dir (str): Path to root directory containing all of the pdf documents to extract.
        pdf_list (list(tuple))): List of tuples information extracted from pdf files.
    """
    def __init__(self, file):
        # Check root directory path
        if not os.path.isfile(file):
            print("Not a proper directory path.")
            return
        self.file = file
        # self.flashcards = self.extract_data(self.file)
        # self.save_flashcards(self.flashcards, "English_Flashcards")
        # self.spanish_cards = self.translate_flashcards(self.flashcards, 'es')
        # self.save_flashcards(self.spanish_cards, "Spanish_Flashcards")
        # self.german_cards = self.translate_flashcards(self.flashcards, 'de')
        # self.save_flashcards(self.spanish_cards, "German_Flashcards")


    def extract_data(self, file):
        fcards = {}
        name = 'Non-Group'
        fcards[name] = []
        freader = open(file)
        data = freader.readlines()
        for line in data:
            line = line.replace('\n', '')
            # Check line not empty
            if not line:
                continue
            # Create flashcard group
            if line[0] == '/':
                name = line[1:]
                fcards[name] = []
                continue
            # Add word to flashcard group
            # line = line.replace(' ', '')
            if line[-1] == ',':
                line = line[:-1]
            words = line.split(',')
            fcards[name].extend(words)
        if not fcards['Non-Group']:
            del fcards['Non-Group']
        return fcards

    def translate_flashcards(self, fcards, output_lang):
        input_lang = 'en'
        new_fcards = {}
        count = 1
        total = str(len(fcards))
        for key in fcards:
            new_fcards[key] = []
            print(str(datetime.now()) + ":\tTranslating '" + str(key) + "' w/ " + str(len(fcards[key])) + " words")
            new_fcards[key].extend(GoogleTranslator(output_lang, input_lang).translate_batch(fcards[key]))
            print(str(datetime.now()) + ":\tCompletion: " + str(count) + "/" + total)
            count += 1
        return new_fcards

    def translate_save(self, fcards, filename):
        fname = "C:/Projects/PyCharm/MBV_Docs/.venv/App/LearnLang/" + filename + ".pkl"
        with open(fname, 'wb') as file:
            pickle.dump(fcards, file)



if __name__ == "__main__":
    pass