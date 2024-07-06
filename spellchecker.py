import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

def getWords():
    words = []

    # Fetch HTML content
    response = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        text = soup.get_text()
    
        words = text.splitlines()

        words = [word.strip() for word in words if word.strip()]
    return words

def suggest_words(trie, word):
    results = []
    visited = set()
    queue = [(trie.root, '')]

    while queue:
        node, prefix = queue.pop(0)

        if node.end_of_word and prefix not in visited and edit_distance(prefix, word) <= 1:
            results.append(prefix)
            visited.add(prefix)

        for char, child_node in node.children.items():
            queue.append((child_node, prefix + char))

    return results

def check_spelling():
    input_word = entry.get().strip()
    
    if not input_word:
        result_label.config(text="Please enter a word.")
        return
    
    is_correct = trie.search(input_word)

    if not is_correct:
        suggestions = suggest_words(trie, input_word)
        result_label.config(text=f"Word '{input_word}' is misspelled.\nSuggestions: {', '.join(suggestions)}")
    else:
        result_label.config(text=f"Word '{input_word}' is spelled correctly.")

if __name__ == "__main__":
    dictionary = getWords()
    trie = Trie()


    for word in dictionary:
        trie.insert(word)

    root = tk.Tk()
    root.title("Spell Checker")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    label = ttk.Label(main_frame, text="Enter a word:")
    label.grid(row=0, column=0, sticky="w")

    entry = ttk.Entry(main_frame, width=30)
    entry.grid(row=0, column=1)

    check_button = ttk.Button(main_frame, text="Check Spelling", command=check_spelling)
    check_button.grid(row=1, column=0, columnspan=2, pady=10)

    result_label = ttk.Label(main_frame, text="")
    result_label.grid(row=2, column=0, columnspan=2)

    root.mainloop()
