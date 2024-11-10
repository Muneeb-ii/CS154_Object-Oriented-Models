from helper import get_file_contents

list_of_stop_words: str = get_file_contents("list_of_stop_words.txt")
characters_to_remove: list[str] = ["!", ",", ".", "?", ":", ";", "-", "_", "\n"]
translation_table = str.maketrans("", "", "".join(characters_to_remove))


class BagOfWords:
    """
    A class to represent the Bag of Words model for a given text.

    Attributes:
        raw_text (str): The original raw text of the review.
        preprocessed_text (str): The text after preprocessing.
        model (dict[str, int]): A dictionary mapping words to their counts.
    """
    raw_text: str
    preprocessed_text: str
    model: dict[str, int]

    def __init__(self, review: str):
        """
        Initializes the BagOfWords object with the raw review text.

        Args:
            review (str): The raw text of the review.
        """
        self.raw_text: str = review
        self.preprocessed_text: str = ""
        self.model: dict[str, int] = {}

    def preprocess_text(self):
        """
        Preprocesses the raw text by converting it to lowercase, removing punctuation,
        and removing stopwords.
        """
        review_no_stop_words: list[str] = [
            f
            for f in self.raw_text.lower().translate(translation_table).split(" ")
            if f not in list_of_stop_words
        ]
        self.preprocessed_text: str = (" ").join(review_no_stop_words)

    def get_count(self):
        """
        Generates the word count model from the preprocessed text.
        """
        self.model: dict[str, int] = {}
        for eachWord in [
            f for f in self.preprocessed_text if f not in list_of_stop_words
        ]:
            self.model[eachWord] = [
                f
                for f in self.raw_text.lower().translate(translation_table).split(" ")
                if f not in list_of_stop_words
            ].count(eachWord)
