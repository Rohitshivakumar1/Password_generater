print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count('t')
r = lower_names.count('u')
u = lower_names.count('r')
e = lower_names.count('e')

first = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')


second = l + o + v + e

final = int(str(first) + str(second))
if (final < 10 ) or (final > 90):
    print(f"Your score is {final}, you go together like coke and mentos.")
elif ( final >= 40 ) and ( final <= 50 ):
    print(f"Your score is {final}, you are alright together.")
else:
    print(f"Your score is {final}.")