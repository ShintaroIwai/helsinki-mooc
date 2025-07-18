# Write your solution here
def longest_series_of_neighbours(my_list : list):
    # Default is set to 1 because consecutive would mean if there is 1 pair of numbers that has
    # difference of 1, then you would need the count to be 2
    count = 1
    max_count = 1
    # The last number doesn't have a difference so I subtracted 1 from range
    for i in range(len(my_list) - 1):
        difference = my_list[i + 1] - my_list[i]
        if difference == 1 or difference == -1:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
    return max_count

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))

    my_list2 = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list2))

    my_list3 = [5, 3, 4, 2, 3, 1, 2, 3, 9, 8, 7, 8, 7, 6, 7, 6]
    print(longest_series_of_neighbours(my_list3))