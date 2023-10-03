# This file is to create additional DataFrame with intermediate numbers of words for its further visualisation and analysis on trends
import main

years = main.years


def count_final_words():
    df = main.df
    # Count non-zero values in each column
    non_zero_counts = df.astype(bool).sum(axis=0).to_list()
    rows_num = len(df)

    return non_zero_counts, rows_num


final_words_count, rows_num = count_final_words()


def get_all_words_nums(years):
    data = {
        "Total_words": [
            "All words",
            "Unique words",
            "Filtered unique words",
        ]
    }
    data_set_cleaned = set()
    data_set_filtered = set()

    for year in years:
        speech_path = main.get_speech_path(year)
        text = main.get_text(speech_path)
        words_total = main.get_words(text, main.speech_regex)
        cleaned_words = main.get_cleaned_words(words_total)
        filtered_words = main.get_filtered_words(cleaned_words)
        cleaned_words_unique = set(cleaned_words)
        filtered_words_unique = set(filtered_words)
        data_item = {
            str(year): [
                len(cleaned_words),
                len(cleaned_words_unique),
                len(filtered_words_unique),
            ]
        }
        data.update(data_item)
        data_set_cleaned.update(cleaned_words_unique)
        data_set_filtered.update(filtered_words_unique)

    print(data)
    return data, len(data_set_cleaned), len(data_set_filtered)


(
    data,
    data_set_cleaned,
    data_set_filtered,
) = get_all_words_nums(years)

df_evaluate = main.get_df(data)
df_evaluate.set_index("Total_words", inplace=True)
df_evaluate.loc["Lemma words"] = final_words_count

all_words_num = df_evaluate.loc["All words"].sum()


print(df_evaluate.head())
print("Total number of cleaned initial words: ", all_words_num)
print("Total number of unique cleaned words: ", data_set_cleaned)
print("Total number of unique cleaned and filtered words: ", data_set_filtered)
print(
    "Total number of words after lemmatization and all fixes (final): ",
    df_evaluate.loc["Lemma words"].sum(),
)
print("Number of final tokens: ", rows_num)
