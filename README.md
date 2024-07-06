# Spell Checker Application

## Overview

The Spell Checker Application is a Python-based tool designed to help users verify the correctness of English words and provide suggestions for misspelled words. It utilizes a Trie data structure for efficient word storage and lookup, along with web scraping techniques using BeautifulSoup to fetch a list of common English words for spell checking.

## Features

- **Spell Checking**: Enter a word and instantly check if it is spelled correctly.
- **Suggestions**: If a word is misspelled, the application provides suggestions based on edit distance, recommending similar words.
- **Web Scraping**: scraps a list of approximately 10,000 common English words from a https://www.mit.edu/~ecprice/wordlist.10000 URL for comprehensive spell checking.

## Technologies Used

- **Python**: The core programming language used for the application logic.
- **tkinter**: Python's standard GUI toolkit used for creating the graphical user interface.
- **BeautifulSoup**: Python library for parsing HTML and XML documents, utilized here for web scraping.
- **Requests**: Python HTTP library used for making HTTP requests.
- **Trie Data Structure**: Implemented to efficiently store and retrieve dictionary words.
- **Edit Distance Algorithm**: Utilized to calculate the similarity between words and suggest alternatives.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Aayush-lad/webscrap-editdist-trie-spellchecker-suggestion.git
   cd webscrap-editdist-trie-spellchecker-suggestion
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**

   ```bash
   python spellchecker.py
   ```

2. **Using the Application:**

   - Enter a word into the provided input field and click on the "Check Spelling" button.
   - If the word is spelled correctly, a confirmation message will be displayed .
   - If the word is misspelled, the application will suggest corrected words .
  

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.


## Author

- **Aayush Lad**
- **aayushlad1973@gmail.com**
