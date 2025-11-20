## Write the program for password check;

password = "Dixith!123"
is_upper = False
is_digit = False
is_special = False
is_lower = False
special_chars = "!@#$%^&*(),.?\":{}|<>"

for char in password:
    if 'A' <= char <= 'Z':
        is_upper = True
    if 'a' <= char <= 'z':
        is_lower = True
    if '0' <= char <= '9':
        is_digit = True
    if char in special_chars:
        is_special = True

if is_upper and is_digit and is_special and is_lower:
    print("Password is valid.")
else:
    print("Password is invalid")

