import string

# Допоміжна функція для очищення тексту від пунктуації та приведення до нижнього регістру
def get_clean_words(text):
    text = text.lower()
    for p in string.punctuation:
        text = text.replace(p, '')
    words = text.split()
    return words

# 1. Загальна кількість слів
def count_total_words(words):
    return len(words)

# 2. Кількість унікальних слів
def count_unique_words(words):
    return len(set(words))

# 3. Найкоротше слово (список найкоротших слів, якщо їх кілька)
def get_shortest_words(words):
    if not words:
        return []
    min_len = min(len(w) for w in words)
    return [w for w in set(words) if len(w) == min_len]

# 4. Найдовше слово (список таких слів, якщо їх кілька)
def get_longest_words(words):
    if not words:
        return []
    max_len = max(len(w) for w in words)
    return [w for w in set(words) if len(w) == max_len]

# 5. Частотний словник у % (використовуємо словник для накопичення)
def word_frequency_percentage(words):
    total = len(words)
    if total == 0:
        return {}
    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    # Переводимо кількість у відсотки
    freq_percent = {word: (count / total) * 100 for word, count in freq.items()}
    return freq_percent

# 6. Літери, що використовувалися у тексті
def get_used_letters(text):
    letters = [char.lower() for char in text if char.isalpha()]
    return sorted(list(set(letters)))

# 7. Літера, що зустрічалась найчастіше (з використанням словника)
def most_frequent_letter(text):
    letters = [char.lower() for char in text if char.isalpha()]
    if not letters:
        return None
    
    letter_counts = {}
    for l in letters:
        letter_counts[l] = letter_counts.get(l, 0) + 1
        
    most_common = max(letter_counts, key=letter_counts.get)
    return most_common


# ДЕМОНСТРАЦІЯ РОБОТИ
if __name__ == "__main__":
    # Читаємо текст із файлу text.txt, який лежить у тій самій папці
    try:
        with open('text.txt', 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print("Попередження: файл text.txt не знайдено у папці проєкту!")
        raw_text = ""

    if raw_text:
        words_list = get_clean_words(raw_text)
        
        print("=== РЕЗУЛЬТАТИ АНАЛІЗУ ТЕКСТУ ===")
        print(f"Загальна кількість слів: {count_total_words(words_list)}")
        print(f"Кількість унікальних слів: {count_unique_words(words_list)}")
        print(f"Найкоротші слова: {get_shortest_words(words_list)}")
        print(f"Найдовші слова: {get_longest_words(words_list)}")
        print(f"Використані літери: {get_used_letters(raw_text)}")
        print(f"Найчастіша літера: {most_frequent_letter(raw_text)}")
        
        # Виведемо перші 5 слів із частотного словника для прикладу
        freq_dict = word_frequency_percentage(words_list)
        sample_freq = dict(list(freq_dict.items())[:5])
        print(f"Частотний словник (перші 5 слів у %): {sample_freq}")