my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
current_index = 0
while current_index < len(my_list):
    if my_list[current_index] < 0:
        break
    if my_list[current_index] != 0:
        print(my_list[current_index])
    current_index += 1