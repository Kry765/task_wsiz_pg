#A
# numbers = [10, 2, 3, 49, 72, 20]
# print(max(numbers) - min(numbers))
# max1 = max(numbers)
# min1 = min(numbers)

#B
# numbers.remove(max1)
# numbers.remove(min1)
# print(numbers)
# numbers2 = numbers
# max2 = max(numbers2)
# min2 = min(numbers2)
# print(max2- min2)

#C
# import math
# numbers = [10, 2, 3, 49, 72, 20]

# for x in numbers:
#   print(math.sqrt(x))
#   print(x**2)
#   print(x**3)

#D
points = [10, 2, 3, 49, 72, 20]
points.remove(max(points))
points.remove(min(points))
print(points)
print(sum(points)/len(points))