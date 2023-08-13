import numpy as np
import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt
from collections import defaultdict
import pymorphy2

speech_regex = r'\b[А-ЯІЇЄҐа-яіїєґ\'’]+\b'
stop_words_regex = r'\b\w+\b'
years = [2020, 2021, 2022, 2023]

def get_speech_path(year):
    """
    Create speech path.

    Keyword argument:
    year -- year of the speech, int
    """
    file_path = f'speech/NY_{year}.txt'

    return file_path

def get_text(path):
    """
    Get the text from the path.

    Keyword argument:
    path -- path of the text, str
    """
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    return text

def get_words(text, regex):
    """
    Get the list of the words.

    Keyword argument:
    text -- the text to split to the words, str
    regex -- the reges to split the text by
    """
    words = re.findall(regex, text.lower())

    return words

stop_words_path = get_text('stopwords_ua.txt')
stop_words_list = get_words(stop_words_path, stop_words_regex)

def get_filtered_words(words):
    """
    Get the list of filtered words.

    Keyword argument:
    words -- words to be filtered
    """
    filtered_words = [word for word in words if word not in stop_words_list]

    return filtered_words

def get_lemma_words(filtered_words):
    """
    Get the list of words after lemmatization.

    Keyword argument:
    words -- words to be executed lemmatization
    """
    morph = pymorphy2.MorphAnalyzer(lang='uk')
    lemma_words = set([morph.parse(word)[0].normal_form for word in filtered_words])

    return lemma_words

def get_speech_words(year):
    """
    Get the dictionary with year as key and lemma words as value.

    Keyword argument:
    year -- year of speech to get the dictionary from
    """
    speech_path = get_speech_path(year)
    text = get_text(speech_path)
    words = get_words(text, speech_regex)
    filtered_words = get_filtered_words(words)
    lemma_words = get_lemma_words(filtered_words)

    return {year : lemma_words}

def get_year_sets(years):
    """
    Get the dictionary with years as keys and lemma words as values.

    Keyword argument:
    years -- years of speeches to get the dictionary from
    """
    year_sets = dict()

    for year in years:
        year_sets.update(get_speech_words(year))

    return year_sets


def get_all_words(years):
    """
    Get the set of all words for all years.

    Keyword argument:
    years -- years of speeches to get the all words from
    """
    year_sets = get_year_sets(years)
    all_words = set()

    for words in year_sets.values():
        all_words.update(words)
    
    return all_words


def get_data(years):
    """
    Get the dictionary with column name as key and lemma words as value.

    Keyword argument:
    years -- years of speeches to get the dictionary from
    """
    all_words = get_all_words(years)
    year_sets = get_year_sets(years)
   
    # Create a dictionary to hold the counts
    word_counts = {'word': [], '2020': [], '2021': [], '2022': [], '2023': []}

    # Populate the word_counts dictionary with counts
    for word in all_words:
        word_counts['word'].append(word)
        for year, words in year_sets.items():
            word_counts[str(year)].append(list(words).count(word))

    return word_counts

def get_df(data):
    """
    Convert data to DataFrame.

    Keyword argument:
    data -- data to be converted
    """
    df = pd.DataFrame(data)

    return df

data = get_data(years)
df = get_df(data)

def save_df_to_csv(df):
    """
    Save dataframe to .csv file.

    Keyword argument:
    df -- dataframe to be saved
    """
    df.to_csv('speeches_df.csv', index=False)









# def draw_plot(data_point):
#     """
#     Draw plot of the most common words.

#     Keyword argument:
#     text -- list of tulpes, where 1st value is a word and 2nd value is frequencies
#     """

#     words = [word for word, _ in data_point[1]]
#     frequencies = [freq for _, freq in data_point[1]]
#     max_freq = max(frequencies)

#     plt.figure(figsize=(words_num, max_freq))
#     plt.bar(words, frequencies, color='blue')
#     plt.xlabel('Words')
#     plt.ylabel('Frequencies')
#     plt.title('Most Common Words and Their Frequencies')
#     plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
#     plt.tight_layout()

#     plt.show()

# def draw_multiple_plots(data):
    
#     fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
#     plots_list = [ax1, ax2, ax3, ax4]

#     for plot in plots_list:
#         index = plots_list.index(plot)
#         words = [word for word, _ in data[index][1]]
#         frequencies = [freq for _, freq in data[index][1]]
#         max_freq = max(frequencies)
#         plot.bar(words,frequencies)
#         plot.set_title(data[index][0])
#         # plot.set_xlabel("Words")
#         # plot.set_ylabel("Frequencies ")

#         # Rotate x-axis labels for each plot
#         plot.set_xticklabels(words, rotation=45, ha='right')

#     # Adjust the spacing between subplots
#     plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9, hspace=0.4)

#     # Show the plot
#     plt.show()


# data = list()
# for path in file_paths:
#     data.append(count_common_words(path, 15))

# draw_multiple_plots(data)
