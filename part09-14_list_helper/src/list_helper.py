# WRITE YOUR SOLUTION HERE:
class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        # max_frequency = 0
        # max_item = None
        # for item in my_list:
        #     frequency = my_list.count(item)
        #     if not max_item or frequency > max_frequency:
        #         max_frequency = frequency
        #         max_item = item
 
        # return max_item

        ordered_list = sorted(my_list)
        count = 0
        max_count = 0
        max_number = 0
        for i in range(len(ordered_list)):
            if i == 0:
                count += 1
            elif ordered_list[i] == ordered_list[i-1]:
                count += 1
                if i == len(ordered_list) - 1:
                    if count > max_count:
                        max_count = count
                        max_number = ordered_list[i-1]
            elif ordered_list[i] != ordered_list[i-1]:
                if count > max_count:
                    max_count = count
                    max_number = ordered_list[i-1]
                count = 1
        return max_number

    @classmethod
    def doubles(cls, my_list: list):
        checker = []
        doubled_list = []
        for number in my_list:
            if number not in checker:
                # if it's the first time a number appears, add it to the checker list to check against
                checker.append(number)
            else:
                if number not in doubled_list:
                    doubled_list.append(number)
        return len(doubled_list)

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
