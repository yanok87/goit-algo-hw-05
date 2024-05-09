"""Compares efficiency of the search algorithms: Boyer-Moore, Knuth-Morris-Pratt, Rabin-Karp"""

import timeit


def read_file(file_path):
    """File reader"""
    with open(file_path, "r", encoding="cp1251") as file:
        return file.read()


text1 = read_file("article_1.txt")
text2 = read_file("article_2.txt")
pattern1 = "Пошук – поширена дія, яка виконується в бізнес-додатках."
pattern2 = "Було проведено серію експериментів для порівняння ефективності використання розглянутих структур даних за затратами часу"
no_pattern = "some random text, that is not to be found in any text"


# Boyer-Moore
def build_shift_table(pattern):
    """Creates a table with shifts"""
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    """Boyer-Moore search algorythm"""

    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


boyer_moore_text1_pattern = timeit.timeit(
    lambda: boyer_moore_search(text1, pattern1), number=1000
)
print("boyer_moore_text1_pattern:", boyer_moore_text1_pattern)

boyer_moore_text1_no_pattern = timeit.timeit(
    lambda: boyer_moore_search(text1, no_pattern), number=1000
)
print("boyer_moore_text1_no_pattern:", boyer_moore_text1_no_pattern)

boyer_moore_text2_pattern = timeit.timeit(
    lambda: boyer_moore_search(text2, pattern2), number=1000
)
print("boyer_moore_text2_pattern:", boyer_moore_text2_pattern)

boyer_moore_text2_no_pattern = timeit.timeit(
    lambda: boyer_moore_search(text2, no_pattern), number=1000
)
print("boyer_moore_text2_no_pattern:", boyer_moore_text2_no_pattern)


# Knuth-Morris-Pratt
def compute_lps(pattern):
    """Longest prefix suffix table"""
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    """Knuth-Morris-Pratt search algorythm"""

    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


kpm_text1_pattern = timeit.timeit(lambda: kmp_search(text1, pattern1), number=1000)
print("kpm_text1_pattern:", kpm_text1_pattern)

kpm_text1_no_pattern = timeit.timeit(lambda: kmp_search(text1, no_pattern), number=1000)
print("kpm_text1_no_pattern:", kpm_text1_no_pattern)

kpm_text2_pattern = timeit.timeit(lambda: kmp_search(text2, pattern2), number=1000)
print("kpm_text2_pattern:", kpm_text2_pattern)

kpm_text2_no_pattern = timeit.timeit(lambda: kmp_search(text2, no_pattern), number=1000)
print("kpm_text2_no_pattern:", kpm_text2_no_pattern)


# Rabin-Karp
def polynomial_hash(s, base=256, modulus=101):
    """Function for polynomial hash"""
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    """Rabin-Karp search algorythm"""
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i : i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (
                current_slice_hash - ord(main_string[i]) * h_multiplier
            ) % modulus
            current_slice_hash = (
                current_slice_hash * base + ord(main_string[i + substring_length])
            ) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


rabin_karp_text1_pattern = timeit.timeit(
    lambda: rabin_karp_search(text1, pattern1), number=1000
)
print("rabin_karp_text1_pattern :", rabin_karp_text1_pattern)

rabin_karp_text1_no_pattern = timeit.timeit(
    lambda: rabin_karp_search(text1, no_pattern), number=1000
)
print("rabin_karp_text1_no_pattern :", rabin_karp_text1_no_pattern)

rabin_karp_text2_pattern = timeit.timeit(
    lambda: rabin_karp_search(text2, pattern2), number=1000
)
print("rabin_karp_text2_pattern :", rabin_karp_text2_pattern)

rabin_karp_text2_no_pattern = timeit.timeit(
    lambda: rabin_karp_search(text2, no_pattern), number=1000
)
print("rabin_karp_text2_no_pattern :", rabin_karp_text2_no_pattern)
