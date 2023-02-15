def remove_from_list(my_list, item):
    """
    Function that removes all accurrances of item from my_list
    """
    # YOUR CODE STARTS HERE
    while (item in my_list):
        my_list.remove(item)
    return my_list


list1 = [1, 2, 3, 5, 6, 87, 5, 5, 74, 6, 6, 6, 4]
print(list1)
print(remove_from_list(list1, 6))
