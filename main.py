from flat import Bill, Flatmates
from report import pdfReport

user_bill = int(input("Hey user give an amount: "))
period = input("Hey user give the period: ")

flatmate1_name = input("What's first flatmate's name?")
flatemate1_days = int(input(f"How many days {flatmate1_name} stayed at home?"))

flatmate2_name = input("What's second flatmate's name?")
flatemate2_days = int(input(f"How many days {flatmate2_name} stayed at home?"))

the_bill = Bill(user_bill, period)
flatmate1 = Flatmates(flatmate1_name, flatemate1_days)
flatmate2 = Flatmates(flatmate2_name, flatemate2_days)

print(f"{flatmate1_name} pays", flatmate1.pay(the_bill, flatmate2))
print(f"{flatmate2_name} pays", flatmate2.pay(the_bill, flatmate1))
pdf = pdfReport("bill.pdf")

pdf.generate(flatmate1, flatmate2, the_bill)