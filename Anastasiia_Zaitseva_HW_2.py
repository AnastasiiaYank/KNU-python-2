# 11.12.Дана непорожня послiдовнiсть слiв iз малих українських літер; мiж сусiднiми словами -пропуск, за останнiм символом -крапка. Надрукувати в алфавiтному порядку:
# д) всi приголоснi, які входять тiльки в одне слово;
# е) всi глухi приголоснi лiтери, які не входять тiльки в одне слово;
# Вказiвка.До голосних лiтер належать а, е, и, i, о, у, є, ю, ї; до приголосних -всi iншi крiм й, ь; дзвiнкi приголоснi -б, в, г, д, ж, з, л, м, н, р; глухі приголосні: к, п, с, т, ф, х, ц, ч, ш, щ.

vowels = 'аеиіоуєюї'
voiced_consonants = 'бвгґджзлмнр'
unvoiced_consonants = 'кпстфхцчшщ'
consonants = voiced_consonants + unvoiced_consonants
# д,е
words = input('Введіть послідовність слів: ').split()

# д
consonants_in_one_word = []
for consonant in consonants:
    count = 0
    for word in words:
        if consonant in word:
            count += 1
    if count == 1:
        consonants_in_one_word.append(consonant)
print('Всі приголосні, які входять тільки в одне слово:',
      sorted(consonants_in_one_word))

# е
unvoiced_consonants_not_in_one_word = []
for consonant in unvoiced_consonants:
    count = 0
    for word in words:
        if consonant in word:
            count += 1
    if count == len(words)-1:
        unvoiced_consonants_not_in_one_word.append(consonant)
print('Всі глухі приголосні літери, які не входять тільки в одне слово:',
      sorted(unvoiced_consonants_not_in_one_word))
