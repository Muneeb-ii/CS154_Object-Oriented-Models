# Project 5 - Models

### Name

_Muneeb Azfar Nafees_

### Introspection

Working with classes is a new concept; navigating object-oriented programming (OOP) for the first time was quite challenging. Specifically, creating the Dataset class was difficult because it involved handling lists and utilizing another class, BagOfWords, on each item of the list. This layering of classes and their interaction was complicated and took some time to understand fully.

Reading a file was also a new task for me. Although it was relatively straightforward compared to implementing the classes, it required careful attention to ensure the data was read and processed correctly.

Through this project, I learned a great deal about OOP principles, such as using classes and objects to organize code. I now better understand how to structure programs in a more modular and maintainable way. The experience has also highlighted the importance of planning and breaking complex problems into smaller, manageable parts.

### Resources

1. https://www.w3schools.com/python/module_random.asp
2. https://www.w3schools.com/python/python_classes.asp

This will be your first programming project! Read this README carefully and follow the instructions.

---


## Goal

The goals of this project are:

* Starting to organize code in modules and using them
* Use classes and objects

## Description

In this project, you will not create anything new in NLP but you will reorganize your code into classes and create objects.

Following are the main tasks for this project:

### Modules

Create three modules - `bag_of_words`, `dataset`, and `main`.


### BagOfWords

Inside `bag_of_words` module, create a class called `BagOfWords`. This class contains three attributes `raw_text`, `preprocessed_text`, and `model`. Apart from the constructor, there should be methods to preprocess text (recall how to preprocess a text from Project 4a), get unique words, and get the count of each word. 


```python
>>> review_1: str = "This was a horrible movie. I do not like this movie"
>>> review_1_bag_of_words: BagOfWords = BagOfWords(review_1)
>>> review_1_bag_of_words.raw_text
"This was a horrible movie. I do not like this movie"
>>> review_1_bag_of_words.preprocess_text()
>>> review_1_bag_of_words.preprocessed_text
"horrible movie like movie"
>>> review_1_bag_of_words.get_count()
>>> review_1_bag_of_words.model
{"horrible": 1, "like": 1, "movie": 2}
```

### Dataset


Inside the `dataset` module, create a class called Dataset. The dataset should have three attributes, `samples`, `training_set`, and `test_set`. Apart from the constructor, it should have a method for `preprocess_samples`. The constructor should take in the list of movie reviews and a `split_ratio` which should be a value between 0 and 1. After taking in a list of movie reviews, it should convert them into a list of BagOfWords. Then based on the split ratio, it should randomly select samples from the list of BagOfWords and have them stored in `training_set` and `test_set`. For example, if there are 10 movie reviews and the split ratio is 0.8, then 8 movie reviews should go in the `training_set` and 2 movie reviews should go in the `test_set`. _The reviews in the training and the test set should be randomized_ (Hint: Look into the `random` module and look at the methods that can be helpful).

Apart from the specified attributes, think of additional attributes that a dataset class should have!


```python
>>> list_of_reviews: list[str] = [
    "this is a good movie",
    "horrible movie, hated it",
    "great movie, a classic",
    "it is ok, not too bad",
    "meh, would not watch it twice"
    ]

>>> movie_review_dataset = Dataset(list_of_reviews, 0.6)
>>> training_set_list = [f.raw_text for f in movie_review_dataset.training_set]
[
    "this is a good movie",
    "it is ok, not too bad",
    "meh, would not watch it twice"
]
>>> test_set_list = [f.raw_text for f in movie_review_dataset.test_set]
>>> print(test_set_list)
[
    "horrible movie, hated it",
    "great movie, a classic"
]
```

When you call the `preprocess_samples` method in BagOfWords, it should then call the `preprocess_text` and `get_count` methods for each review in the training and test set.

```python
...
>>> movie_review_dataset.preprocess_samples()
>>> test_set = movie_review_dataset.training_set
>>> test_set_reviews = [f.model for f in movie_review_dataset.test_set]
>>> print(test_set_reviews)
[
    {"horrible": 1, "movie": 1, "hated": 1},
    {"great": 1, "classic": 1, "movie": 1}
]
... # similarly for training_set
```

### Main

In the main module, write your own functions to read the csv file and get the list of reviews. Then create a dataset object that takes in the list of reviews you read from the csv file. Call the `preprocess_sample` method from the dataset and print the training and test set samples. 
