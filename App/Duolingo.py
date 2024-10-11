

class Duolingo:
    """This will extract.

    German to English language conversions were done through https://www.onlinedoctranslator.com/app/translationprocess-pdf

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        file (str): Path to root directory containing all of the pdf documents to extract.

    Attributes:
        root_dir (str): Path to root directory containing all of the pdf documents to extract.
    """
    def __init__(self):
        pass
    def convert_duo_words(self, filename):
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
        values = content.split('\n\n')
        flashcard = []
        for item in values:
            if item:
                word, definition = item.split('\n')
                flashcard.append((word, definition))
        return flashcard

    def convert_duo_notes(self, filename):
        pass


if __name__ == "__main__":
    filename = "../Resources/Duolingo/DuoWords.txt"
    duo = Duolingo()
    fc = duo.convert_duo_words(filename)
    # fcfile = os.path.dirname(filename) + "/DuoCards.csv"
    # cards.create_anki_flashcard(fc, fcfile)
    pass