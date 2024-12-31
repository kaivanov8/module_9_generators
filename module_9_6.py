# Генераторы

def all_variants(text):
    for k in range(1, len(text) + 1):  # k-длина подстроки
        for i in range(0, len(text) - k + 1):  # i-позиция начала подстроки
            yield text[i:i + k]

a=all_variants('abc')
for i in a:
    print(i)
