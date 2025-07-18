# Write your solution here
def list_sum(list1, list2):
    new_list = []
    index = 0
    while index < len(list1):
        new_list.append(list1[index] + list2[index])
        index += 1
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]