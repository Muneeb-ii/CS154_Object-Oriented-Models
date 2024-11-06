[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/eSOd7i2b)
# Project 5 - Models

### Name

_Muneeb Azfar Nafees_

### Introspection

_Describe the challenges you faced and what you learned_

### Resources

_List the people and resources you used to complete the project_

This will be your first programming project! Read this README carefully and follow the instructions.


### *DO NOT EDIT BELOW THIS LINE*
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


## Rubric

**1. Code Quality and Documentation** - **10 points**

- **Code Readability and Organization**: *5 points*
  - Meaningful variable and function names
  - Modules and classes created as specified
- **Comments and Docstrings**: *5 points*
  - Clear explanations of functions and complex code sections
  - Proper use of docstrings for all functions

**2. Version Control Practice** - **10 points**

- **Commit Numbers and Sizes**: *5 points*
  - The commits are made at regular intervals and of coherent pieces 
- **Commit Messages**: *5 points*
  - Easy to follow along the commit history

**3. bag_of_words ** - **40 points**

- **Attributes**: *10 points*
  - The specified attributes are created in the class
- **Constructor**: *10 points*
  - The constructor assigns the specific values in the attributes
- **Methods**: *20 points*
  - All specified methods are implemented and use the `self` keyword

**4. dataset ** - **30 points**

- **Attributes** - *10 points*
    - The specified attributes are created in class
- **Constructor** - *10 points*
    - The samples are randomized
    - The training and test set are split according to the split_ratio
- **Methods** - *10 points*
    - The `preprocess_sample` calls the necessary methods in `BagOfWords` object.
  
**5. main ** - **10 points**

- **read_file** - *5 points*
  - A function to read the reviews from the csv files is created. 
- **imports** - *2 points*
  - Necessary modules, classes, and functions are imported
- **creating objects** - *3 points*
  - `Dataset` objects are created and the necessary methods are called

**Total Points: 100**


## Tips On How To Excel


### General Advise

* Start early!
* Ask for help when stuck. Remember the 30 minute rule? No? Look into the syllabus.
* Break down the task into smaller tasks and try to implement them in Jupyter Notebook. Once implemented in the notebook successfully, transfer it into `.py` file.
* Run the `.py` file to make sure the new addition did not break any changes.
* After implementing each small task, commit changes.
* Review the notebooks from classes available on GitHub if you cannot remember syntax for anything.
* Run your code multiple times and vary the inputs to ensure it works as intended. 
* Use a debugger to ensure that the code behave as intended. 

## Feedback

