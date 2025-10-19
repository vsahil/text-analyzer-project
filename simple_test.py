import os
import argparse
from collections import Counter
from typing import List, Tuple, Dict
import string


def read_file(filename: str) -> str:
    '''
    Args: filename of the file to read
    Functionality: Reads the file and returns its content
    Raises: Raises error if filename does not exist
    '''
    
    try:
        with open(filename, "r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"{filename} does not exist")
        raise


def get_file_stats(content: str) -> dict:
    '''
        Args: content from a file
        Functionality: remove punctuations, converts words to lowercase, and 
        Returns: 4 statistics from them: number of words, number of unique words, most frequent word and its count
    '''
    translator = str.maketrans('', '', string.punctuation)

    # Apply the translation to the string
    clean_content = content.translate(translator)
    clean_content = clean_content.lower()
    clean_content_split = clean_content.split()
    
    if len(clean_content_split) == 0:
        return {"character_count": 0, "word_count": 0, "unique_word_count": 0, "most_frequent_word": None, "frequency": 0}
    
    words_counter = Counter(clean_content_split)
    num_words = sum(words_counter.values())
    num_unique_words = len(words_counter)
    most_frequent = words_counter.most_common(1)
    return {"character_count": len(clean_content), "word_count": num_words, "unique_word_count": num_unique_words, "most_frequent_word": most_frequent[0][0], "frequency": most_frequent[0][1]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A sample program')
    parser.add_argument('filename', help='The name of the file to process')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    args = parser.parse_args()
    
    try:
        file_content = read_file(args.filename)
        stats = get_file_stats(file_content)
        print(f"Total character count: {stats['character_count']}")
        print("Number of words in the file: ", stats["word_count"])
        print("Number of unique words in the file: ", stats["unique_word_count"])
        print("Most frequent word in the file: ", stats["most_frequent_word"])
        print("Count of the most frequent word in the file: ", stats["frequency"])
    except FileNotFoundError:       ## Question what happens if the except is of a different kind than this one? 
        print(f"{args.filename} not found")
    
