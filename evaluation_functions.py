import main

years = main.years


def get_all_initial_words(years):
    all_initial_words = set()
    for year in years:
        speech_path = main.get_speech_path(year)
        text = main.get_text(speech_path)
        words_total = main.get_words(text, main.speech_regex)
        words_unique = set(words_total)
        all_initial_words.update(words_unique)
        print("Total words in ", year, " is ", len(words_total))
        print("Total unique words in ", year, " is ", len(words_unique))

    print("The number of raw unique words: ", len(all_initial_words))
    return


get_all_initial_words(years)
