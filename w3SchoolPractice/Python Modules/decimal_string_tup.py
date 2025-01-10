import decimal 
print("Construct a decimal form a float ")
pi_val = decimal.Decimal(3.1415)
print(pi_val)
print(pi_val.as_tuple())
print("Construct a decimal from a string")
num_str = decimal.Decimal("123.25")
print(num_str)
print(num_str.as_tuple)