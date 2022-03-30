i = 0
while i < 3:
    print(i)
    i += 1
print()


while True:
    # calculate guess
    user_name = input("What is your name (or q to quit)? ")
    quit()
    if user_name == 'q':   # h, l, y, q
        break  # exit loop
    if user_name == '':
        print("Please enter a name.")
        continue  # continue at top
    print(f"Welcome, {user_name}")
