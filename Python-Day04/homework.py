# Q1. List Creation & Element Insertion

numbers = []

numbers.append(10)
numbers.append(20)
numbers.append(30)

numbers.insert(1, 15)

numbers.extend([40, 50])

print(numbers)


# Q2. Element Removal & Retrieval

items = ["Python", "Java", "C++", "JavaScript", "Ruby"]

items.remove("C++")

last_item = items.pop()

print(items)
print(last_item)


# Q3. Element Frequency & Index Lookup

scores = [85, 92, 75, 92, 88, 92, 70]

count = scores.count(92)

index = scores.index(88)

print("Count of 92:", count)
print("Index of 88:", index)


# Q4. Sorting & Reversing

marks = [45, 89, 12, 67, 95, 34]

marks.sort()

print("Ascending:", marks)

marks.reverse()

print("Descending:", marks)


# Q5. List Slicing Challenge

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("First 5 elements:", arr[:5])

print("Last 3 elements:", arr[-3:])

print("Every second element:", arr[1:9:2])

print("Reverse:", arr[::-1])


# Q6. Sum and Average of List Elements

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0

for num in numbers:
    total = total + num

average = total / 5

print("Sum =", total)
print("Average =", average)


# Q7. Find Largest and Smallest Number

def find_min_max(numbers):

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum


numbers = [34, 12, 89, 5, 67]

maximum, minimum = find_min_max(numbers)

print("Max =", maximum)
print("Min =", minimum)


# Q8. Remove Duplicates (Preserve Order)

numbers = [1, 3, 2, 3, 4, 1, 5, 2]

new_list = []

for num in numbers:
    if num not in new_list:
        new_list.append(num)

print(new_list)


# Q9. Separate Even and Odd Numbers

numbers = [10, 15, 22, 33, 40, 55, 60]

even_list = []
odd_list = []

for num in numbers:

    if num % 2 == 0:
        even_list.append(num)

    else:
        odd_list.append(num)

print("Even:", even_list)
print("Odd:", odd_list)


# Q10. Second Largest Element

numbers = [10, 45, 20, 99, 80, 99]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:

    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest =", second_largest)


# Q11. List Comprehension: Square Odds

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [num * num for num in nums if num % 2 != 0]

print(result)


# Q12. Rotate List Elements Left by K Positions

def rotate_left(lst, k):

    k = k % len(lst)

    return lst[k:] + lst[:k]


lst = [1, 2, 3, 4, 5]

k = 2

result = rotate_left(lst, k)

print(result)


# Q13. Merge Two Sorted Lists

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8, 10]

merged = []

i = 0
j = 0

while i < len(list1) and j < len(list2):

    if list1[i] < list2[j]:
        merged.append(list1[i])
        i = i + 1

    else:
        merged.append(list2[j])
        j = j + 1


while i < len(list1):
    merged.append(list1[i])
    i = i + 1


while j < len(list2):
    merged.append(list2[j])
    j = j + 1


print(merged)


# Q14. Flatten a Nested List

def flatten(nested_list):

    result = []

    for item in nested_list:

        if isinstance(item, list):
            result.extend(flatten(item))

        else:
            result.append(item)

    return result


nested_list = [1, [2, 3], [4, [5, 6]], 7]

result = flatten(nested_list)

print(result)


# Q15. Pair Sum Target

def find_pairs(nums, target):

    pairs = []

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))

    return pairs


nums = [2, 4, 3, 5, 7, 8, 9]

target = 7

result = find_pairs(nums, target)

print("Pairs:", result)


# Q16. Longest Consecutive Subsequence

numbers = [100, 4, 200, 1, 3, 2]

number_set = set(numbers)

longest = 0

for num in number_set:

    if num - 1 not in number_set:

        current = num
        count = 1

        while current + 1 in number_set:
            current = current + 1
            count = count + 1

        if count > longest:
            longest = count

print("Output Length:", longest)


# Q17. Group Anagrams

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:

    key = "".join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

result = list(groups.values())

print(result)


# Q18. Predict the Output
# Shallow Copy vs Reference

a = [1, 2, [3, 4]]

b = a.copy()

b[0] = 99

b[2][0] = 77

print("a:", a)
print("b:", b)


# Q19. Debugging Challenge
# Remove all negative numbers

numbers = [-5, -2, 3, -4, -1, 6, 8]

numbers = [num for num in numbers if num >= 0]

print(numbers)


# Q20. Matrix Transposition using List Comprehension

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [
    [matrix[row][column] for row in range(len(matrix))]
    for column in range(len(matrix[0]))
]

print(transpose)