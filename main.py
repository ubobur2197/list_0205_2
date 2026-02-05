# 1
letters_list = ['a', 'b', 'c']
other_letters = ['x', 'y', 'z']
letters_list.extend(other_letters)
print(letters_list)


# 2
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]
merged_numbers = odd_numbers + even_numbers
print(merged_numbers)


# 3
numbers_list = [2, 3, 4, 5]
user_num = int(input("Son kiriting: "))
numbers_list.insert(0, user_num)
print(numbers_list)


# 4
letters_list = ['a', 'b', 'c', 'd']
letters_list.insert(2, 'X')   # 3-pozitsiya (index 2)
print(letters_list)


# 5
odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.insert(1, 0)
print(odd_numbers)
