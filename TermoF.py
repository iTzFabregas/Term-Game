import os

word = 'WORDS' # put a 5 letters word here
showed_word = []
for i in word:
    showed_word.append('_') 

game_table = []
for i in range(6):
    game_table.append(showed_word)


k = 0
error = 0
while k < 6:
    os.system('clear')
    if error == 1:
        print('>>>> Invalid word!!!')
        error = 0

    for i in game_table:
        for j in i:
            print(j, end=' ')
        print()

    divided_word = []
    for i in word:
        divided_word.append(i)

    given_word = str(input('\n')).upper()
    if len(given_word) != len(word):
        error = 1
        continue

    result_given_word = []
    divided_given_word = []
    for i in given_word:
        divided_given_word.append(i)
        result_given_word.append("\033[1;31m" + i + "\033[m")


    cnt = 0
    for i in divided_given_word:
        if i == divided_word[cnt]:
            result_given_word.pop(cnt)
            i = "\033[1;32m" + i + "\033[m"
            result_given_word.insert(cnt, i)
            divided_word.pop(cnt)
            divided_word.insert(cnt, '_')
            divided_given_word.pop(cnt)
            divided_given_word.insert(cnt, '_')
        cnt += 1

    cnt = 0
    for i in divided_given_word:
        if i in divided_word and i != '_':
            result_given_word.pop(cnt)
            new_i = "\033[1;33m" + i + "\033[m"
            result_given_word.insert(cnt, new_i)
            divided_word.insert(divided_word.index(i), '_')
            divided_word.pop(divided_word.index(i))
            divided_given_word.pop(cnt)
            divided_given_word.insert(cnt, '_')     
        cnt += 1     



    game_table.insert(k, result_given_word)
    game_table.pop()
    if given_word == word:
        break
    k += 1


os.system('clear')
for i in game_table:
    for j in i:
        print(j, end=' ')
    print()

if k != 6:
    print('\n\n>>> YOU WIN!!!')
else:
    print('\n\n>>> YOU LOSE')