print("Hello! I can calculate how long you live")
print("Enter your name:")
name = (input())
print("Enter your age:")
age = int(input())
month = age * 12
days = age * 365
hours = age * 8760
minutes = age * 525600
print ("Your name:", name)
print ("You have been living for",month,"months,",days,"days,",hours,"hours and",minutes,"minutes")