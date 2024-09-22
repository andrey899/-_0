#Задача "Всё не так уж просто":
#Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Используя этот список составьте второй список primes содержащий только простые числа.
#А так же третий список not_primes, содержащий все не простые числа.
#Выведите списки primes и not_primes на экран(в консоль).
numbers = list(range(1, 15 + 1))

primes = []
not_primes = []

for number in numbers:
    is_prime = number > 1
    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print(numbers)
print(primes)
print(not_primes)