
from currency import convert_currency


from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
amount = float(input("Amount: "))

result = convert_currency(from_currency, to_currency, amount)

if result is not None:
    print("Conversion successful!")
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
else:
    print("Error: Could not get exchange rate.")

