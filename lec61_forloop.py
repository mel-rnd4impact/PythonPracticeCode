word = "hello world"

for letter in word:
    print(letter)


userstring = input("Enter a string")
count = 0
for letter in userstring:
    count += 1

print("The word you entered was" + userstring)
print("The number of characters is" + str(count))

three_inp = range(1, 20, 3)

for num in three_inp:
    print(num)
