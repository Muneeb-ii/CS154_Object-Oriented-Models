from bag_of_words import BagOfWords
import random


class Dataset:
    samples: list[str]
    training_set: list[str]
    testing_set: list[str]

    def __init__(self, reviews: list[str], split_ratio: float):
        random.shuffle(reviews)
        self.samples: list[str] = [BagOfWords(review) for review in reviews]
        self.training_set: list[str] = self.samples[: round(len(reviews) * split_ratio)]
        self.testing_set: list[str] = self.samples[round(len(reviews) * split_ratio) :]

    def preprocess_samples(self):
        for sample in self.training_set + self.testing_set:
            sample.preprocess_text()
            sample.get_count()
