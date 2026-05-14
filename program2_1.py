import random
n_min = 1
n_max = 3


nums = []
for i in range (3):
    while True:
        try:
            n = int(input('Podaj liczbe: '))
            if n < n_min or n > n_max:
                print(f'liczba spoza zakresu od {n_min} do {n_max}')
            else:
                nums.append(n)            
                break
        except:
            print('musisz wpisac liczbe')
nums.sort()
print(nums)

random_nums = []
for i in range (3):
    while True:
        liczba = random.randint(n_min, n_max)
        if not liczba in random_nums:
            break
#         if liczba in random_nums:
#             continue
#         else:
#             break
    random_nums.append(liczba)
random_nums.sort()



print(random_nums)

hits = 0

for nums in random_nums:
    hits = hits + 1

print(hits)

