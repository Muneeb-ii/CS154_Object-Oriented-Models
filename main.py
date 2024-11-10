from dataset import Dataset

def read_file_contents(file_name):
    with open(file_name, "r") as file:
        each_line: list[str] = file.readlines()[1:]
    return each_line


list_of_reviews = [f[1:len(f)-11] for f in read_file_contents("test_reviews.csv")]

movie_review_dataset: Dataset = Dataset(list_of_reviews, 0.6)

training_set_list = [f.raw_text for f in movie_review_dataset.training_set]
print(f"Model is trained on {len(training_set_list)} reviews")
print(f"Training Set: {training_set_list}\n")

testing_set_list = [f.raw_text for f in movie_review_dataset.testing_set]
print(f"Model will be tested on {len(testing_set_list)} reviews")
print(f"Testing Set: {testing_set_list}\n")

movie_review_dataset.preprocess_samples()

training_set_reviews = [f.model for f in movie_review_dataset.training_set]
print(f"Training Set Model: {training_set_reviews}\n")

testing_set_reviews = [f.model for f in movie_review_dataset.testing_set]
print(f"Testing Set Model: {testing_set_reviews}")






