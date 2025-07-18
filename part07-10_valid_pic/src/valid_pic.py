# Write your solution here
def is_it_valid(pic: str):
    validity = True
    from datetime import datetime
    # check length
    if len(pic) != 11:
        validity = False
    # check the first six characters
    day = int(pic[0:2])
    month = int(pic[2:4])
    year = int(pic[4:6])
    # adjust year
    if pic[6] == "+":
        year += 1800
    elif pic[6] == "-":
        year += 1900
    elif pic[6] == "A":
        year += 2000
    try:
        # how do I test for year = 00?
        datetime(year, month, day)
    except ValueError:
        validity = False
    # check 7th character
    index6 = "+-A"
    if pic[6] not in index6:
        validity = False
    # check validity of the control character
    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    control_check = pic[0:6] + pic[7:10]
    control = int(control_check) % 31
    if pic[10] != control_string[control]:
        validity = False

    return validity

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
    print(is_it_valid("100400A644E"))