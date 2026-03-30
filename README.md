# Words

This repo contains a list of English words.

[words_alpha.txt](./words_alpha.txt) is copied from https://github.com/dwyl/english-words

[new_words.txt](./new_words.txt) contains "modern" words that [words_alpha.txt](./words_alpha.txt) does not contain.

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
