# Example 1
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))

if hours > 40:
    rate = rate * 1.5

pay = hours * rate

print('Pay: ' + str(pay))

# Example 2
try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    if hours > 40:
        rate = rate * 1.5

    pay = hours * rate

    print('Pay: ' + str(pay))
except:
    print('Error please enter numeric input')

# Exercise 3
score = float(input('Enter score:'))
if score > 0.0 and score < 1.0:
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
else:
    print('Bad score')
