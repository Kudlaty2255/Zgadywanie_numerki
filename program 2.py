# i = 1
# while i <= 200:
#     print(i)
#     i = i + 1


# n_min = 10
# n_max = 25
# while True:
#     try:
#         n = int(input('Wpisz liczbe do ktorej mam policzyc: '))
#         if n_min < n < n_max :
#             break
#         else:
#             print(f'Liczba musi miescic sie w przedziale od {n_min} do {n_max}')
#     except:
#         print('Musisz wpisac liczbe')
# i = 1
# while n >= i:
#     print(i)
#     i = i + 1

playstate = 0
while playstate == 0:
    while playstate == 1 or playstate == 2:
        try:
            end = int(input('Czy chcesz grać dalej? ( 1 TAK    2 NIE )'))
            if end == 1:
                break
            elif end == 2:
                 playstate = playstate + 1    
            else:
                print('Niepoprawna odpowiedz')
        except:
            print('Niepoprawna odpowiedz')
        





    #Zmienne i generowanie liczby
    while True:
        if playstate == 2:
            break

        n_min = 1
        n_max = 5
        import random
        liczba = random.randint(n_min, n_max)
    #Pętla do zgadywania
        while True:
            try:
                n = int(input(f'Odgadnij moja liczbe! (Znajduje się w przedziale od {n_min} do {n_max}) : '))
                if n == liczba:
                    break
                elif n <= liczba:
                    print('za malo')
                elif n >= liczba:
                    print('za dużo')
            except:
                print('Musisz wpisac liczbe')
    #Odpowiedz
        print('BRAWO!')
        break
    playstate = playstate + 1
