import stopwords_ua
import errors_dictionary

SPEECH_REGEX = r"\b[А-ЯІЇЄҐа-яіїєґ\'\-’]+\b"
YEARS = [2020, 2021, 2022, 2023]
STOP_WORDS_LIST = stopwords_ua.STOP_WORDS
LEMMA_ERRORS = errors_dictionary.lemma_errors
LEMMA_TYPOS = errors_dictionary.lemma_typos
