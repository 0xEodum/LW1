import math

#EX1_START
#EX1_1_START
def sum_of_prime_divisors(n):
    sum = 0
    i = 2
    while i*i <= n:
        if n % i == 0:
            sum += i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        sum += n
    return sum
#EX1_1_END

#EX1_2_START
def find_odd_digits_of_number_more_than_3(n):
    k = 0
    while n != 0:
        digit = n % 10
        if (digit %2 != 0 and digit > 3):
            k += 1
        n = n // 10
    return k
#EX1_2_END

#EX1_3_START
def find_divisors(n):
    divisors = []
    border = int(math.sqrt(n))
    for i in range(2, border + 1):
        if n % i == 0:
            divisors.append(i)
            if i**2 != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def find_sum_of_digits(n):
    sum = 0
    while n != 0:
        digit = n % 10
        sum += digit
        n //= 10
    return sum

def check_number(n):
    product = 1
    divisors = find_divisors(n)
    main_sum = find_sum_of_digits(n)
    for d in divisors:
        local_sum = find_sum_of_digits(d)
        if local_sum < main_sum:
            product *= d
    return product
#EX1_3_END

if __name__ == '__main__':
    print(check_number(400))

