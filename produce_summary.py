def print_delivery_total_price(day, day_file):
    """Takes in the day number and melon data, and
    prints the number of melons delivered at what price"""
    print(f'Day {day}')
    the_file = open(day_file)
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
        
        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f'Delivered {count} {melon}s for total of ${amount}')
    
    the_file.close()

print_delivery_total_price(1, "um-deliveries-20140519.txt")
print()
print_delivery_total_price(2, "um-deliveries-20140520.txt")
print()
print_delivery_total_price(3, "um-deliveries-20140521.txt")
