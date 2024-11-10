from helper import get_file_contents

list_of_stop_words: str = get_file_contents("list_of_stop_words.txt")
characters_to_remove: list[str] = ["!", ",", ".", "?", ":", ";", "-", "_"]
translation_table = str.maketrans("", "", "".join(characters_to_remove))


class BagOfWords:
    raw_text: str
    preprocessed_text: str
    model: dict[str, int]

    def __init__(self, review: str):
        self.raw_text: str = review

    def preprocess_text(self):
        review_no_stop_words: list[str] = [
            f
            for f in self.raw_text.lower().translate(translation_table).split(" ")
            if f not in list_of_stop_words
        ]
        self.preprocessed_text: str = (" ").join(review_no_stop_words)

    def get_count(self):
        self.model: dict[str, int] = {}
        for eachWord in [
            f
            for f in self.raw_text.lower().translate(translation_table).split(" ")
            if f not in list_of_stop_words
        ]:
            self.model[eachWord] = [
                f
                for f in self.raw_text.lower().translate(translation_table).split(" ")
                if f not in list_of_stop_words
            ].count(eachWord)
