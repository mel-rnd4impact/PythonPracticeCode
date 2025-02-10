user_string = "It is me."
ll = len(user_string)
revv = ""

for item in range(ll-1, -1, -1):
    revv += user_string[item]

print(revv)
