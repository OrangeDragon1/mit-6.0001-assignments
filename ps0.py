import math
# alternative way is to use numpy or pylab packages

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

print("X**y =", x**y)
print("log(x) = ", int(math.log2(x)))
# log_result = 0
# while x > 1:
#     x /= 2 # log2, divide x by 2 until x is less than 1
#     log_result += 1
#
# print("log(x) =", log_result)