import csv
import random
fn = input('Podaj nazwe pliku: ')
with open(fn, encoding= 'utf-8') as f:
    reader = csv.reader(f, delimiter=':')
    words = {}
    for row in reader:
        k = row[0].strip()
        v = row[1].strip()
        words[k] = v
    

a_words = len(words)
c_words = 0
w_words = 0
pkt = 0
ocena = [1,1,2,3,4,5]

    



# words = {'Hej':'Ciao','Dzięukje':'Grazie','Miłość':'Amore','Dom':'Casa','Dzień':'Giorno'}




# words_it = ['Ciao', 'Grazie', 'Amore', 'Casa', 'Giorno']
# words_pl = ['Hej','Dziękuje','Miłość','Dom','Dzień']

# print(words)
# print(words[0])
# print(len(words))
# print(len(words[0]))

# a = 0
# for _ in words:
#     print(words[a])
#     input()
#     a += 1

# random.shuffle(words)
# 
# n= len(words_it)
# pkt = 0
# for i in range(n):
#     words_it[i] == words_pl[i]
#     print(words_pl[i])
#     odp = input('A jak to będzie po włosku? : ')
#     if odp.lower() == words_it[i].lower(): 
#         print('Dobrze')
#         pkt += 1 
#     else:
#         print('Źle')
#         
# print(f'Twoja ocena to: {ocena[pkt]}')


for k, v in words.items():
    print(k)
    odp = input('A jak to będzie po włosku? : ')
    if odp.lower() == v.lower(): 
        print('Dobrze')
        pkt += 1
        c_words += 1
    else:
        print('Źle')
        w_words += 1

print(f'Liczba słów : {a_words}      Poprawne słowa : {c_words}      Błędne słowa: {w_words}      Twoja ocena to: {ocena[pkt]}')
