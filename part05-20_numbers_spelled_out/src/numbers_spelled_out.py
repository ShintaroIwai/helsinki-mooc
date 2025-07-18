# Write your solution here
def dict_of_numbers():
    # 0-19 are basic numbers
    new_dict = {}
    list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
    'nineteen']
    
    # 20-99 is a combination of twenty, thirty, etc. + 1-9
    list2 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    for j in range(20, 100):
        if j % 10 == 0:
            list1.append(list2[(j // 10) - 2])
        if j % 10 != 0:
            list1.append(list2[(j // 10) - 2] + "-" + list1[j % 10])
    
    for k in range(0, 100):
        new_dict[k] = list1[k]
    
    return new_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])