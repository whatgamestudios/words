# Words

This repo contains a list of English words.

[words_alpha.txt](./words_alpha.txt) is copied from https://github.com/dwyl/english-words

[new_words.txt](./new_words.txt) contains "modern" words that [words_alpha.txt](./words_alpha.txt) does not contain.

[all_words.txt](./all_words.txt) is a combination of [new_words.txt](./new_words.txt) and [words_alpha.txt](./words_alpha.txt), generated using [combine_word_lists.py](./combine_word_lists.py).

[game_words.txt](./game_words.txt) is a specialisation of [all_words.txt](./all_words.txt) for a game, removing words that are a single letter or are longer than eleven letters, or contain duplicate letters (that is two of any letter). It is generated using [game_filter.py](./game_filter.py).

[common_words.txt](./common_words.txt) is a list of 3000 common English words.

[seed_words.cs](./seed_words.cs) is a filtered, randomly ordered subset of [common_words.txt](./common_words.txt) suitable for seed words in a game. It is not committed to the repository; generate it locally with `seed_words.py`.

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


## Game word list

[game_filter.py](./game_filter.py) reads [all_words.txt](./all_words.txt) and writes [game_words.txt](./game_words.txt). It drops words that are:

- a single letter,
- longer than eleven letters, or
- contain any letter more than once (duplicate letters in the same word).

Run:

```bash
python game_filter.py
```


## Seed word list

[seed_words.py](./seed_words.py) reads [common_words.txt](./common_words.txt) and writes [seed_words.cs](./seed_words.cs). It drops words that:

- contain any character other than lowercase a–z,
- are a single letter,
- are longer than eleven letters, or
- contain any repeated character.

The remaining words are written in random order. The output file is not committed to the repository.

Use the same virtual environment as above, then run:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed_words.py
```
