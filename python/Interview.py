## Write the program for password check;

password = input("Enter your password: ")
is_upper = False
is_digit = False
is_special = False
is_lower = False
special_chars = "!@#$%^&*(),.?\":{}|<>"

for char in password:
    if char.isupper():
        is_upper = True
    elif char.islower():
        is_lower = True
    elif char.isdigit():
        is_digit = True
    elif char in special_chars:
        is_special = True

if is_upper and is_lower and is_digit and is_special:
    print("Password is valid.")
else:
    print("Password is invalid.")


## Occurance of the same letter in the name;

s = 'Dixith G R'
freq = {}

for char in s:
    freq[char] = freq.get(char, 0) +1

print(freq)


#write a program to check the atm withdrawal

balance = 5000
pin : int(input("Enter your pin: "))
read_card = False
pin_number = False

print("Welcome Please Insert your ATM card ")

if read_card:
    print("Enter your personal identification number")
    if read_card:
        print("Enter pin number")
        if pin_number:
            print("Please ennter the amount")
            amount = int(input("Enter the amount: "))
            if amount >= balance:
                balance - amount
                print("Withdrawn successfull")
            else:
                print("Insufficient balance")
        else:
            print("Entered incorrect pin")
else:
    print("error reading card")
    print("There has been an error")
    print("End of transaction")

#Age criteria to match job

age = 10
degree = True
experience = 3

if age > 18:
    if degree:
        if experience>=3:
            print("Eligible")
        else: 
            print("Not much experience")
    else:
        print("degree not met")
else:
    print("Age not matched")
    print("Not eligible")

#multiplication table

num = int(input("Enter the number to get multiplication table: "))

for i in range(1,11):
    mul = num * i
    print(f"{num} X {i} = {mul}")

# Calculating the natural numbers sum

number = int(input("Enter the number to which it has to be calculated: "))
total = 0
for num in range(0,number+1):
    total = total + num
print(total)

#highest number in a list without inbuilt function

numbers = [23, 45, 12, 67, 34, 89, 56]
max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print(f"Maximum number is: {max_number}")

## most important code in the class (interview question)
nums = [10, 5, 20, 20, 2, 18] 

largest = float('-inf')    
second_largest = float('-inf')

for n in nums:
    if n > largest:
        second_largest = largest 
        largest = n 
    elif n > second_largest and n != largest:
        second_largest = n 
        
print("Second largest :", second_largest)

#reversing the string

try_one = 'Python is fun to learn'
reverse = try_one.split()
wording = [a[::-1] for a in reverse]
outputs = " ".join(wording)
print(outputs)

# Checking prime number or not

def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Calculating factorial


