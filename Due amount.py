def dueAmount(b,g):
    return g-b

bill = int(input("Enter the bill: "))
given = int(input("Enter the given amount: "))

res = dueAmount(bill,given)

print(f"Bill: {bill}\n Given Amount: {given}\n Due Amount: {res}")
print("Hello world")