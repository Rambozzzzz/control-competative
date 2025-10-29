# a=[1,11,2,3,,15]
# b=10
# sum of subarray which is less than b

arr = [1, 11, 2, 3, 15]
b = 10

n = len(arr)
count = 0
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += arr[j]
        if current_sum < b:
            count += 1
        else:
            break

print(count)