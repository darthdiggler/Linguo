
import csv


class Flashcards:
    """This will convert data into Anki flashcards in various ways

    German to English language conversions were done through https://www.onlinedoctranslator.com/app/translationprocess-pdf

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        file (str): Path to root directory containing all of the pdf documents to extract.

    Attributes:
        root_dir (str): Path to root directory containing all of the pdf documents to extract.
    """
    def __init__(self, file):
        pass

    def create_anki_flashcard(self, word_pairs, filename='anki_flashcards.csv'):
        """
        Takes a list of word pairs and generates a CSV file formatted for Anki.

        :param word_pairs: List of tuples, where each tuple contains two values (front and back of the card).
        :param filename: The name of the output CSV file.
        """
        # Open the file in write mode
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write each word pair (front and back) as a row
            for front, back in word_pairs:
                writer.writerow([front, back])

if __name__ == "__main__":
    pass