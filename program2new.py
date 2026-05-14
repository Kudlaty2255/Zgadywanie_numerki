import random
state = 0

def play():
  
    #Pętla do zgadywania
    while state == 0:
        n_min = 1
        n_max = 5
        liczba = random.randint(n_min, n_max)
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
    try:
        end = int(input('Czy chcesz grać dalej? ( 1 TAK    2 NIE )'))
        if end == 1:
            state = 0
        elif end == 2:
            state = 1    
        else:
            print('Niepoprawna odpowiedz')
    except:
        print('Niepoprawna odpowiedz')   
    
while state == 0:
    if state == 0:
        play()

        
    


        