"""
Task link: https://stepik.org/lesson/3380/step/3?unit=963

Простейшая система проверки орфографии основана на использовании списка известных слов.
Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.

Напишем подобную систему. Через стандартный ввод подаётся следующая структура:
первой строкой — количество d записей в списке известных слов,
после передаётся  d строк с одним словарным словом на строку,
затем — количество l строк текста, после чего — l строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре.
Регистр слов не учитывается. Порядок вывода слов произвольный.
Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.

﻿
Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa

Sample Output:
aab
aba
c
aaa

"""

known = set()
unknown = set()

for _ in range(int(input())):
    known.add(input().strip().lower())

for _ in range(int(input())):
    for word in input().strip().lower().split():
        if word not in known:
            unknown.add(word)

for word in unknown:
    print(word)
