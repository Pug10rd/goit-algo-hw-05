import timeit

# Алгоритм Кнута-Морріса-Пратта
def compute_lps(pattern):
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

def kmp_search(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = compute_lps(pattern)
    i = j = 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
        if j == M:
            return i - j
    return -1  # якщо підрядок не знайдено

# Алгоритм Боєра-Мура
def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
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

# Алгоритм Рабіна-Карпа
def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value

def rabin_karp_search(text, pattern):
    substring_length = len(pattern)
    main_string_length = len(text)
    base = 256 
    modulus = 101  
    substring_hash = polynomial_hash(pattern, base, modulus)
    current_slice_hash = polynomial_hash(text[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1) % modulus
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if text[i:i+substring_length] == pattern:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(text[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(text[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1

# Функція для заміру часу виконання
def measure_time(search_func, text, pattern):
    return timeit.timeit(lambda: search_func(text, pattern), number=1000)

# Приклад для заміру часу для кожного алгоритму
text1 = open("task_3/text1.txt").read()
text2 = open("task_3/text2.txt").read()
pattern_existing = "знайдений підрядок"  # Підрядок, який є в тексті
pattern_fake = "вигаданий підрядок"      # Підрядок, якого немає

# Замір часу для статті 1 з наявним підрядком
print("Article 1 - Existing substring")
print("KMP:", measure_time(kmp_search, text1, pattern_existing))
print("Boyer-Moore:", measure_time(boyer_moore_search, text1, pattern_existing))
print("Rabin-Karp:", measure_time(rabin_karp_search, text1, pattern_existing))

# Замір часу для статті 1 з вигаданим підрядком
print("\nArticle 1 - Non-existing substring")
print("KMP:", measure_time(kmp_search, text1, pattern_fake))
print("Boyer-Moore:", measure_time(boyer_moore_search, text1, pattern_fake))
print("Rabin-Karp:", measure_time(rabin_karp_search, text1, pattern_fake))

# Замір часу для статті 2 з наявним підрядком
print("\nArticle 2 - Existing substring")
print("KMP:", measure_time(kmp_search, text2, pattern_existing))
print("Boyer-Moore:", measure_time(boyer_moore_search, text2, pattern_existing))
print("Rabin-Karp:", measure_time(rabin_karp_search, text2, pattern_existing))

# Замір часу для статті 2 з вигаданим підрядком
print("\nArticle 2 - Non-existing substring")
print("KMP:", measure_time(kmp_search, text2, pattern_fake))
print("Boyer-Moore:", measure_time(boyer_moore_search, text2, pattern_fake))
print("Rabin-Karp:", measure_time(rabin_karp_search, text2, pattern_fake))
