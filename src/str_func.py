"""Возвращает все заглавные буквы"""
def upper_case(s):
   return s.upper()

"""Возвращает заглавными первые буквы каждого слова в строке"""
def capitalize_words(string):
    return " ".join(word.capitalize() for word in string.split())
