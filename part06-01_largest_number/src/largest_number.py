# write your solution here

def largest():
    with open("numbers.txt") as new_file:
        
        numbers_list = []
        for line in new_file:
            line = line.replace("\n", "")
            numbers_list.append(int(line))
    
    return max(numbers_list)

if __name__ == "__main__":
    result = largest()
    print(result)
