import numpy as np
import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt
from collections import defaultdict
# from os import path
# from PIL import Image
# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


file_path_stop_words = "stopwords_ua.txt"
with open(file_path_stop_words, 'r', encoding='utf-8') as file:
    stop_words = file.read()

stop_words_list = re.findall(r'\b\w+\b', stop_words.lower())

file_paths = ['speech/NY_2020.txt', 'speech/NY_2021.txt', 'speech/NY_2022.txt', 'speech/NY_2023.txt']

words_num = 15

def count_common_words(file_path, words_num = words_num):
    """
    Count the most common words in text.

    Keyword argument:
    file_path -- file's path in list format
    words_num -- number of common words in the result in int format (default words_num)
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b(?![0-9]+\b)\w+\b', text.lower())
    filtered_words = [word for word in words if word not in stop_words_list]
    word_counts = Counter(filtered_words)
    most_common_words = word_counts.most_common(words_num)
    year = re.sub(r'\D', '', file_path)

    return [year,  most_common_words]

def draw_plot(data_point):
    """
    Draw plot of the most common words.

    Keyword argument:
    text -- list of tulpes, where 1st value is a word and 2nd value is frequencies
    """

    words = [word for word, _ in data_point[1]]
    frequencies = [freq for _, freq in data_point[1]]
    max_freq = max(frequencies)

    plt.figure(figsize=(words_num, max_freq))
    plt.bar(words, frequencies, color='blue')
    plt.xlabel('Words')
    plt.ylabel('Frequencies')
    plt.title('Most Common Words and Their Frequencies')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.tight_layout()

    plt.show()

def draw_multiple_plots(data):
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    plots_list = [ax1, ax2, ax3, ax4]

    for plot in plots_list:
        index = plots_list.index(plot)
        words = [word for word, _ in data[index][1]]
        frequencies = [freq for _, freq in data[index][1]]
        max_freq = max(frequencies)
        plot.bar(words,frequencies)
        plot.set_title(data[index][0])
        # plot.set_xlabel("Words")
        # plot.set_ylabel("Frequencies ")

        # Rotate x-axis labels for each plot
        plot.set_xticklabels(words, rotation=45, ha='right')

    # Adjust the spacing between subplots
    plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9, hspace=0.4)

    # Show the plot
    plt.show()


data = list()
for path in file_paths:
    data.append(count_common_words(path, 15))

# draw_multiple_plots(data)

def count_common_words_2(file_path, words_num = words_num):
    """
    Count the most common words in text.

    Keyword argument:
    file_path -- file's path in list format
    words_num -- number of common words in the result in int format (default words_num)
    """

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b(?![0-9]+\b)\w+\b', text.lower())
    word_frequencies = defaultdict(int)
    # Count word frequencies while considering different cases as the same word
    for word in words:
        word_frequencies[word] += 1

    # Print the word frequencies
    for word, frequency in word_frequencies.items():
        print(f"{word}: {frequency}")


count_common_words_2('speech/NY_2022.txt')