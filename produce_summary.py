def print_delivery_total_price(day, day_file):
    """Takes in the day number and melon data, and
    prints the number of melons delivered at what price"""

    #Prints day that data is for
    print(f'Day {day}')

    #Opens the desired file
    the_file = open(day_file)

    #Iterates through each line of the file
    for line in the_file:
        #Strips line of any space at the end
        line = line.rstrip()
        # Splits each line and puts words into a list
        words = line.split('|')
        
        #Assigns melon name
        melon = words[0]
        #Assigns number of melons delivered
        count = words[1]
        #Assigns total amount sold in $
        amount = words[2]

        # Prints this data all in one line
        print(f'Delivered {count} {melon}s for total of ${amount}')
    # Closes file
    the_file.close()

# Calls function to print the melon delivery data for the past three days
print_delivery_total_price(1, "um-deliveries-20140519.txt")
print()
print_delivery_total_price(2, "um-deliveries-20140520.txt")
print()
print_delivery_total_price(3, "um-deliveries-20140521.txt")
