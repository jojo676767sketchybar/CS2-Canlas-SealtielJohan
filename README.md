# Electricity Calculator


## Description
This program calculates the electricity change from past records to newer records

## Version 1 - Original code with no input validation
- Input: Accepts the students name and values of the records of recent meter readings and older ones.
- Process: Calculates the consumption by subtracting the current reading with the previous reading, then multiplies it with the rate.
- Output: Name of customer, Consumption amount and total bill.
- No input validation
## Version 2 - New code containing input validation
- Input: Accepts the students name and values of the records of recent meter readings and older ones.
- Process: Calculates the consumption by subtracting the current reading with the previous reading, then multiplies it with the rate.
- Output: Name of customer, Consumption amount and total bill.
- input validation: Checks if the name of the customer is present, the values of both readings are at least 0, and if the current reading is at least the same as the previous reading, if any of these conditions are not fulfilled, it will loop back to the start, asking you to input your values and your name until all conditions are met.
