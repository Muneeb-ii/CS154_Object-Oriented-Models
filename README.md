# Object-Oriented Bag of Words Dataset

This project explores **object-oriented programming** (OOP) principles by structuring an NLP Bag-of-Words model using Python classes. Two core classes — `BagOfWords` and `Dataset` — are implemented across modules to demonstrate modular code organization and interaction between objects. Developed for **CS154**, an introductory Python course with NLP components.

---

## 📌 Features

- Built from scratch using pure Python and OOP design
- Modular file structure:
  - `bag_of_words.py`: for text preprocessing and word counting
  - `dataset.py`: for dataset splitting and object management
  - `main.py`: driver script for data reading and execution
- Random train-test splitting using `random` module
- Review preprocessing and token count generation stored in `.model`

---

## 🧠 Reflections

- Learned how to encapsulate logic within classes and define clear object responsibilities.
- Implemented interactions between objects (e.g., `Dataset` creating multiple `BagOfWords`).
- File I/O and method chaining helped reinforce the need for modular, clean code.
- This project helped shift my approach from linear scripting to thinking in terms of classes and objects.

---

## 🛠️ How to Use

1. Clone the repository and make sure you have Python installed.

2. Ensure your folder structure contains:
   ```
   bag_of_words.py
   dataset.py
   main.py
   reviews.csv (or similar input file)
   ```

3. Run the project:
   ```bash
   python main.py
   ```

4. The script will:
   - Read reviews from a file
   - Initialize a `Dataset` object
   - Split into train/test sets
   - Preprocess each review and print token counts

---

## 📚 Resources

- [Python Random Module – W3Schools](https://www.w3schools.com/python/module_random.asp)
- [Python Classes – W3Schools](https://www.w3schools.com/python/python_classes.asp)

---

## 🪪 License

This project is licensed under the MIT License.
