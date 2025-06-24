import re


def read_txt(filename):
    with open(filename, 'r') as f:
        return f.read()


def write_txt(filename, text):
    with open(filename, 'w') as f:
        f.write(text)


def append_txt(filename, text):
    with open(filename, 'a') as f:
        f.write(text)


def check_line_if_number(line):
    for char in line:
        if char.isdigit():
            return line
    return None


def read_lines(filename):
    with open(filename, 'r') as f:
        return [line for line in f.readlines() if check_line_if_number(line)]


def analyze_file(filename):
    even_word_lines = 0
    total_word_count = 0
    letter_count = 0
    word_freq = {}

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                continue  # Skipping empty lines

            # Splitting words and numbers using regex
            words = re.findall(r"\b\w+(?:['/]\w+)*\b", stripped)

            # Counting the words in line
            if len(words) % 2 == 0:
                even_word_lines += 1

            # Getting only words without numbers
            word_only = [w for w in words if not w.isnumeric()]
            total_word_count += len(word_only)

            # Counting letters without numbers and special characters
            letters = [c for c in stripped if c.isalpha()]
            letter_count += len(letters)

            # update word frequency
            for word in word_only:
                if word:
                    word_freq[word.lower()] = word_freq.get(word.lower(), 0) + 1

    # Finding the most common word
    if word_freq:
        most_common_word = max(word_freq, key=word_freq.get)
        max_count = word_freq[most_common_word]
    else:
        most_common_word = ""
        max_count = 0

    # printing result
    print(f"Number of lines with even number of words: {even_word_lines}")
    print(f"Total number of words (excluding numbers): {total_word_count}")
    print(f"Total number of letters (excluding spaces and empty lines): {letter_count}")
    print(f"Most frequent word: '{most_common_word}' (appeared {max_count} times)")


def summarize_file(filename):
    summery_file = 'summary.txt'
    write_txt(summery_file, f'Summary of {filename}:\n')
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                continue  # Skipping empty lines

            # Splitting words and numbers using regex
            words = re.findall(r"\b\w+(?:['/]\w+)*\b", stripped)
            append_txt(summery_file, f'{" ".join(words)} - ({len(words)} words)\n')


if __name__ == '__main__':
    my_filename = 'my_text.txt'
    my_text = ("Hello world\nIt's the first exercise in I/O\nThat mean it is number 1\n"
               "Not 2\nNot three\nIt is exciting\nAnd i am all 4 it\n")
    write_txt(my_filename, my_text)

    lines = read_lines(my_filename)
    print("".join(lines))

    analyze_file(my_filename)
    summarize_file(my_filename)
