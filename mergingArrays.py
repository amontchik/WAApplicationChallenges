arr1 = [1, 4, 8, 12, 16]
arr2 = [3, 9, 18, 20, 30]

for i in range(len(arr2)):
    arr1.append(arr2[i])

arr1.sort()

# for i in range(len(arr1)):
#     num = i
#     for j in range(i + num, len(arr1)):
#         if (arr1[i] > arr1[j]):
#             temp = arr1[j]
#             arr1[j] = arr1[i]
#             arr1[i] = temp

# counter = 0
# checkDone = False
# while (not checkDone):
#     for i in range(len(arr1) - 1):
#         if (arr1[i] > arr1[i+1]):
#             counter += 1
#         if (counter == 0):
#             checkDone = True
#     for i in range(len(arr1) - 1):
#         temp = arr1[i]
#         arr1[i + 1] = arr1[i]
#         arr1[i] = temp