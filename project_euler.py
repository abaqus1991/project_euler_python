# 1 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# s = 0
# for i in range(3,1000):
#     if i % 3 == 0 or i % 5 == 0:
#         s += i
# print(s)


# #2 Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


# seq = [1, 2]
# next_item = sum(seq)
# while next_item <= 4000000:
#     seq.append(next_item)
#     next_item = seq[-2]+seq[-1]
# print(seq)


# 3 The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# import time

# ts = time.time()
# num = 851475143
# num_2 = num//2+1
# lpf = 0
# for i in range(2, num_2):
#     if num % i == 0:
#         i_2 = i//2+1
#         for j in range(2, i_2):
#             if i % j == 0:
#                 break
#             if j == i_2-1:
#                 lpf = i
# te = time.time()
# total_operation_time = te-ts
# print(num, lpf, total_operation_time)

# 4 A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# p_num = 0
# for i in range(10000, 1000, -1):
#     for j in range(10000, i-1, -1):
#         num = i * j
#         s_num = str(num)
#         if s_num == s_num[::-1] and num > p_num:
#             print(f'{i}*{j}={num}')
#             p_num = num

# 5 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# num = 20
# finish = False
# while True:
#     for i in range(1, 21):
#         if num % i != 0:
#             break
#         if i == 20:
#             finish = True
#     if finish == True:
#         break
#     print(num)
#     num += 20
# print(f'final {num}')

# 6 The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# sum_of_squares = sum([n**2 for n in range(101)])
# square_of_sum = sum([n for n in range(101)])**2

# print(square_of_sum-sum_of_squares)


# 7 By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def look_for_prime_2(position_to_look_for=10001):
    start = time.time()

    number = 3
    current_prime_position = 2

    while current_prime_position != position_to_look_for:
        number += 1
        finish = int(number/2)
        for i in range(2, finish+1):
            if number % i == 0:
                break
            if i == finish:
                current_prime_position += 1
                break
    return number
