import random;

letters = [
    'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'];

password_list = [];

print("Welcome to the password generator!.");
nr_letters = int(input("How many letters would you like in your password.\n"));
nr_numbers = int(input("How many numbers would you like inside your password.\n"));
nr_symbols = int(input("How many symbols would you like inside your password.\n"));

length_of_password = nr_letters + nr_numbers + nr_symbols;

password_list.extend(random.sample(letters, k = nr_letters));
password_list.extend(random.sample(numbers, k = nr_numbers));
password_list.extend(random.sample(symbols, k = nr_symbols));

password_list = random.sample(password_list, k = length_of_password);

password = "";

for chr in password_list:
    password += chr;

print(password);

