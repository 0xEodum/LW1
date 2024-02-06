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


if __name__ == '__main__':


