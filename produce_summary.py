def print_delivery_total_price(day, day_file):
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

# print("Day 1")
# the_file = open("um-deliveries-20140519.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
