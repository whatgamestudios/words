# Words

This repo contains a list of English words.

[words_alpha.txt](./words_alpha.txt) is copied from https://github.com/dwyl/english-words

[new_words.txt](./new_words.txt) contains "modern" words that [words_alpha.txt](./words_alpha.txt) does not contain.

[all_words.txt](./all_words.txt) is a combination of [new_words.txt](./new_words.txt) and [words_alpha.txt](./words_alpha.txt).

[game_words.txt](./game_words.txt) is a specialisation of [all_words.txt](./all_words.txt) for a game, removing words that are a single letter or are longer than eleven letters, or contain duplicate letters (that is two of any letter).

The scripts described below manipulate the word lists.


## Checking for overlap

[check_new_words.py](./check_new_words.py) prints any word from `new_words.txt` that also appears in `words_alpha.txt` (one line per word, first occurrence order).

Create a virtual environment, install dependencies (there are none beyond the standard library), and run:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python check_new_words.py
```

Output goes to standard output; missing word list files cause a non-zero exit and a message on standard error.

## Combining word lists

[combine_word_lists.py](./combine_word_lists.py) merges [words_alpha.txt](./words_alpha.txt) and [new_words.txt](./new_words.txt) into [all_words.txt](./all_words.txt). Words are normalized to lowercase, deduplicated, and written one per line in alphabetical order.

Use the same virtual environment as above, then run:

```bash
python combine_word_lists.py
```

The script prints when processing starts and when it finishes (including how many unique words were written). Missing input files cause a non-zero exit and a message on standard error.

## Game word list

[game_filter.py](./game_filter.py) reads [all_words.txt](./all_words.txt) and writes [game_words.txt](./game_words.txt). It drops words that are:

- a single letter,
- longer than eleven letters, or
- contain any letter more than once (duplicate letters in the same word).

Run:

```bash
python game_filter.py
```

The script prints when processing starts and when it finishes (including how many lines were written). If `all_words.txt` is missing, it exits with a non-zero status and a message on standard error.
