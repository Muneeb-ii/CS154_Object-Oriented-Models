from bag_of_words import BagOfWords
import random


class Dataset:
    """
    A class to represent a dataset of reviews, split into training and test sets.

    Attributes:
        samples (list[BagOfWords]): The list of all samples as BagOfWords objects.
        training_set (list[BagOfWords]): The training set samples.
        testing_set (list[BagOfWords]): The test set samples.
    """
    samples: list[BagOfWords]
    training_set: list[BagOfWords]
    testing_set: list[BagOfWords]

    def __init__(self, reviews: list[str], split_ratio: float):
        """
        Initializes the Dataset by creating BagOfWords objects and splitting into training and test sets.

        Args:
            reviews (list[str]): The list of review texts.
            split_ratio (float): The ratio of data to be used for training (between 0 and 1).
        """
        random.shuffle(reviews)
        self.samples: list[BagOfWords] = [BagOfWords(review) for review in reviews]
        self.training_set: list[BagOfWords] = self.samples[: round(len(reviews) * split_ratio)]
        self.testing_set: list[BagOfWords] = self.samples[round(len(reviews) * split_ratio) :]

    def preprocess_samples(self):
        """
        Preprocesses samples and forms word count dictionaries for each review in the training and test sets.
        """
        for sample in self.training_set + self.testing_set:
            sample.preprocess_text()
            sample.get_count()
