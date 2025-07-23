# Broadcast
# prices = [100, 200, 300, 400]
# discount = 10 # 10 %

# final_prices = []

# for price in prices:
#   final_price = price - (price * discount/100)
#   final_prices.append(final_price)

# print(final_prices)


# #  solution
import numpy as np

# second_prices = np.array([100, 200, 300, 400])
# final_second_prices = second_prices - (second_prices  * discount/100)
# print(final_second_prices)


# # print(np.array([10, 11, 12]) + 10)

# arr = np.array([10, 11, 12])
# res = arr * 2
# print(res)

# # Broadcast from 1d array to 2d array
# matrix = np.array([[1, 2, 3], [4, 5, 6]])
# vector = np.array([10, 20, 30])
# result = matrix + vector
# print(result)

# # incompatiable shapes -- getting errors
# arraaay = np.array([[10, 11, 12], [13, 14, 15]])
# arrraaay = np.array([1, 2])

# print(arraaay + arrraaay)


# vactoraization
#  normal using list python old method
list1 = [1, 2, 3]
list2 = [4, 5, 6]

res = [x+y for x,y in zip(list1, list2)]
print(res)


l1 = np.array([1, 2, 3])
l2 = np.array([4, 5, 6])

res = l1+l2
print(res)



