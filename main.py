import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import pymorphy2

import global_params

years = global_params.YEARS
speech_regex = global_params.SPEECH_REGEX
stop_words_list = global_params.STOP_WORDS_LIST


def get_speech_path(year):
    """
    Create speech path.

    Keyword argument:
    year -- year of the speech, int.
    """
    file_path = f"speech/NY_{year}.txt"

    return file_path


def get_text(path):
    """
    Get the text from the path.

    Keyword argument:
    path -- path of the text, str.
    """
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


def get_words(text, regex=speech_regex):
    """
    Get the list of the words.

    Keyword argument:
    text -- the text to split to the words, str
    regex -- the reges to split the text by, str.
    """
    words = re.findall(regex, text.lower())

    return words


def get_cleaned_words(words):
    """
    Get the list of words cleaned from dashes in the start and in the end.

    Keyword argument:
    words -- words to be filtered, list.
    """
    cleaned_words = [word[1:] if word.startswith("-") else word for word in words]
    cleaned_words = [
        word[:-1] if word.endswith("-") else word for word in cleaned_words
    ]

    return cleaned_words


def get_filtered_words(cleaned_words):
    """
    Get the list of filtered words.

    Keyword argument:
    words -- words to be filtered, list.
    """
    filtered_words = [word for word in cleaned_words if word not in stop_words_list]

    return filtered_words


def get_lemma_words(filtered_words):
    """
    Get the list of words after lemmatization.

    Keyword argument:
    words -- words to be executed lemmatization, list.
    """
    morph = pymorphy2.MorphAnalyzer(lang="uk")
    lemma_words = [morph.parse(word)[0].normal_form for word in filtered_words]

    return lemma_words


def get_speech_words(year):
    """
    Get the dictionary with year as key and lemma words as value.

    Keyword argument:
    year -- year of speech to get the dictionary from, int.
    """
    speech_path = get_speech_path(year)
    text = get_text(speech_path)
    words = get_words(text, speech_regex)
    cleaned_words = get_cleaned_words(words)
    filtered_words = get_filtered_words(cleaned_words)
    lemma_words = get_lemma_words(filtered_words)

    return {year: lemma_words}


def get_year_sets(years):
    """
    Get the dictionary with years as keys and lemma words as values.

    Keyword argument:
    years -- years of speeches to get the dictionary from, list.
    """
    year_sets = dict()

    for year in years:
        year_sets.update(get_speech_words(year))

    return year_sets


def get_all_words(years):
    """
    Get the set of all words for all years.

    Keyword argument:
    years -- years of speeches to get the all words from, list.
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
    years -- years of speeches to get the dictionary from, list.
    """
    all_words = get_all_words(years)
    year_sets = get_year_sets(years)

    # Create a dictionary to hold the counts
    word_counts = {"word": [], "2020": [], "2021": [], "2022": [], "2023": []}

    # Populate the word_counts dictionary with counts
    for word in all_words:
        word_counts["word"].append(word)
        for year, words in year_sets.items():
            word_counts[str(year)].append(list(words).count(word))

    return word_counts


def get_df(data):
    """
    Convert data to DataFrame.

    Keyword argument:
    data -- data to be converted, dictionary.
    """
    df = pd.DataFrame(data)

    return df


data = get_data(years)
df = get_df(data)
df.set_index("word", inplace=True)


def save_df_to_csv(df):
    """
    Save dataframe to .csv file.

    Keyword argument:
    df -- dataframe to be saved
    """
    df.to_csv("speeches_df.csv")


def get_dict_content(word):
    """
    Get from the dictionary article of the word

    Keyword argument:
    word -- a word which article to get, str.
    """
    DICT_URL = "http://sum.in.ua/?swrd="
    req = requests.get(f"{DICT_URL}{word}")
    soup = BeautifulSoup(req.text, "lxml")
    return soup


def get_typo(words):
    typo_words = []
    target_text = "не знайдено"
    for word in words:
        content = get_dict_content(word)
        if target_text in content.text:
            typo_words.append(word)

    return typo_words


# Uncomment only when necessary since it takes a lot of time to run this function
# print("Words non existed in the ukrainian dictionary: ", get_typo())


lemma_errors_index_names = global_params.LEMMA_ERRORS

# Correcting lemmatization errors
def correct_lemma_errors(df=df, index_names=lemma_errors_index_names):
    for main_index, *to_merge in index_names:
        df.loc[main_index] += df.loc[to_merge].sum()
        df = df.drop(to_merge, axis=0)

    return


lemma_typos_index_name = global_params.LEMMA_TYPOS

# Correcting Lemmatization typos
def correct_lemma_typos(df=df, new_indexes=lemma_typos_index_name):
    df = df.rename(new_indexes, axis="index")

    return


def fix_lemma(
    df=df, index_names=lemma_errors_index_names, new_indexes=lemma_typos_index_name
):
    correct_lemma_errors(df, index_names)
    correct_lemma_typos(df, new_indexes)

    return


fix_lemma()

# save_df_to_csv(df)
