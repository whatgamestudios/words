import random

def shuffle_word_file(input_filename, output_filename):
    try:
        # Open the file and read lines into a list, stripping whitespace/newlines
        with open(input_filename, 'r', encoding='utf-8') as file:
            # Use a list comprehension to filter out any empty lines
            words = [line.strip() for line in file if line.strip()]
        
        # Randomise the order of the list in place
        random.shuffle(words)
        
        # Write the shuffled list to the new output file
        with open(output_filename, 'w', encoding='utf-8') as file:
            for word in words:
                file.write(word + '\n')
                
        print(f"Success! Shuffled {len(words)} words into '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
shuffle_word_file('five_words.txt', 'shuffled_words.txt')