import os
import string
from collections import Counter

FILE_NAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"

def get_text():
    if not os.path.exists(FILE_NAME):
        print("File not found. Please enter a paragraph to create 'sample.txt':")
        text = input()
        with open(FILE_NAME, "w") as file:
            file.write(text)
    else:
        with open(FILE_NAME, "r") as file:
            text = file.read()
    return text

def count_words(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))  # Remove punctuation & lowercase
    words = text.split()
    return Counter(words)

def save_report(word_count):
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)

    with open(REPORT_FILE, "w") as file:
        file.write(f"Word Count Report\nTotal Words: {total_words}\nTop 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")

def main():
    text = get_text()
    word_count = count_words(text)

    print(f"Total words: {sum(word_count.values())}")
    print("Top 5 most common words:")
    for word, count in word_count.most_common(5):
        print(f"{word} - {count} times")

    save_report(word_count)
    print("\nWord count report saved to 'word_count_report.txt'.")

if __name__ == "__main__":
    main()

