#EX1_START
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

def find_odd_digits_of_number_more_than_3(n):
    k = 0
    while n != 0:
        digit = n % 10
        if (digit %2 != 0 and digit > 3):
            k += 1
        n = n // 10
    return k

if __name__ == '__main__':
    print(find_odd_digits_of_number_more_than_3(555))

