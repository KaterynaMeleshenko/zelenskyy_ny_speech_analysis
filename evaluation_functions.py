import main

years = main.years


def get_all_cleaned_initial_words_nums(years):
    data = {"total_words": ["All words", "Unique words"]}
    data_set = set()
    for year in years:
        speech_path = main.get_speech_path(year)
        text = main.get_text(speech_path)
        words_total = main.get_words(text, main.speech_regex)
        cleaned_words = main.get_cleaned_words(words_total)
        words_unique = set(cleaned_words)
        data_item = {str(year): [len(cleaned_words), len(words_unique)]}
        data.update(data_item)
        data_set.update(words_unique)

    return data, len(data_set)


data, data_set = get_all_cleaned_initial_words_nums(years)
df_cleaned_initial = main.get_df(data)
df_cleaned_initial.set_index("total_words", inplace=True)


all_cleaned_initial_words_num = df_cleaned_initial.loc["All words"].sum()

print(df_cleaned_initial.head())
print("Total number of cleaned initial words: ", all_cleaned_initial_words_num)
print("Total number of unique words: ", data_set)
