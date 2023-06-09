# # 3.3
# x = -25
# abs_x = abs(x)
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = abs_x
# ans = (high + low) / 2.0
#
# while abs(ans ** 2 - abs_x) >= epsilon:
#     print("low =", low, "high =", high, "ans =", ans)
#     numGuesses += 1
#     if ans ** 2 < abs_x:
#         low = ans
#     else:
#         high = ans
#
#     ans = (high + low) / 2.0
#
# if x < 0:
#     ans = -ans
#
# print("numGuesses =", numGuesses)
# print(ans, "is close to square root of", x)
# print()
#
# # 3.5
# # Newton-Raphson for square root
# # Find x such that x**2 - 24 is within epsilon of 0
# epsilon = 0.01
# k = 25.0
# guess = k / 2.0
# numGuesses = 0
# while abs(guess * guess - k) >= epsilon:
#     numGuesses += 1
#     guess = guess - (((guess ** 2) - k) / (2 * guess))
# print('Square root of', k, 'is about', guess)
# print("numGuesses =", numGuesses)
#
#
# # 4.1.1
# def is_in(str1, str2):
#     return str1 in str2 or str2 in str1
#
#
# print(is_in("hello", "hello world"))
#
#
# def f(x):
#     def g():
#         x = 'abc'
#         print('x =', x)
#
#     def h():
#         z = x
#         print('z =', z)
#
#     x = x + 1
#     print('x =', x)
#     h()
#     g()
#     print('x =', x)
#     return g
#
#
# x = 3
# z = f(x)
# print('x =', x)
# print('z =', z)
# z()
#
#
# # 5.1.1
# def find_extreme_divisors(n1, n2):
#     min_val, max_val = (None, None)
#     for i in range(2, min(n1, n2) + 1):
#         if n1 % i == 0 and n2 % i == 0:
#             if min_val == None:
#                 min_val = i
#             max_val = i
#
#     return (min_val, max_val)
#
#
# print(find_extreme_divisors(100, 200))


# def fib(x):
#     """assumes x an int >= 0
#        returns Fibonacci of x"""
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)


# def sum_digits(s):
#     """Assumes s iis a string
#         Returns the sum of the decimal digits in s
#         For exmaple, if s is 'a2b3c' it returns 5 """


# while True:
#     val = input('Enter an integer: ')
#     try:
#         val = int(val)
#         print('The square of the number you entered is', val**2)
#         break
#     except Exception:
#         print("'{}' is not an integer.".format(val))

