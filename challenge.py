# Bonus calculation with user input
# The program must ask for the name, salary and the bonus received

name = input("Enter your name: ")
salary = float(input("Enter your salary: "))
bonus = float(input("Enter the bonus received: ")) 
annual_value = 1000
total = annual_value + salary + (salary * bonus)


print(f"\nHi {name}! Your salary is {salary}. \nThe total amount of your salary this month is {total}.")