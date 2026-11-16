# Name: Aunist Hope
# Section: CSE 174 G-H
# Date: 2/13/2025
# This program encrypts the digits of a phone number.
 
def main():
    # Prompting the user with a message
    print('Enter a 10 digit phone number (e.g. 5131234567): ', \
          end = '')
 
    # Saving the given number inside a constant variable
    phone_num = int(input())
 
    # Step 1: Seperating Digits
    area_code = phone_num // 10000000
    central_office_code = (phone_num // 10000) % 1000
    station_number = phone_num % 10000
 
    print('(%d) %d - %d' \
          % (area_code, central_office_code, station_number))
 
    # Part 2: Encrpiting the Station Number
    num_1 = (station_number // 100) + 33
    num_2 = (station_number % 100) + 33
 
    chr_1 = chr(num_2)
    chr_2 = chr(num_1)
 
    print('(%d) %d - %s%s' \
          % (area_code, central_office_code, chr_1, chr_2))
 
    # Part 3 Encrypting the Rest of the Digits
    num_3 = area_code * 1000 + central_office_code
    num_4 = 99756473822 - num_3
    print(num_4)
 
    # Rearranging the Results
    print('%s%d%s' % (chr_1, num_4, chr_2))
 
# Using the variable __name__
if __name__=="__main__":
    main()