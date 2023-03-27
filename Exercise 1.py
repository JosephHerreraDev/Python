# Exercise 1
name = input("Enter your name: ")
print('hello ' + name)

# Exercise 2
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = round((hours * rate), 2)
print("Pay: " + str(pay))

# Exercise 3
width = 17
height = 12.0

print(str(width // 2)) # 8
print(str(width/2.0)) # 8.5
print(str(height / 3)) # 4.0
print(str(1 + 2 * 5)) # 11

# Exercise 4
celcius = float(input("Temperature in celcius: "))
fahrenheit = celcius * 33.8

print("The temperature in fahrenheit is: " + str(fahrenheit))