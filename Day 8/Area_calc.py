def print_calc(height, width):
    number_of_cans = round((height * width) / coverage)
    print(f"You need to buy {number_of_cans} cans.")


test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
print_calc(height = test_h, width = test_w)