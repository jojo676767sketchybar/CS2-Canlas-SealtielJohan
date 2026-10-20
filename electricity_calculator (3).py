# Electricity Bill Calculator
RATE = 12.90

while True:
    name = input("Enter student name: ")
    previous = float(input("Enter previous meter reading: "))
    current = float(input("Enter current meter reading: "))
    
    if name.strip() != "" and previous >= 0 and current >= 0 and current >= previous:
        break
    else:
        print("One value is incorrect! Remember, there must be a name present, and the currect must be atleast the same as your previous!")

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity consumption:", consumption, "kWh")
print("Total bill: PHP", round(total_bill, 2))
