import arrow
a = arrow.utcnow()
print("Current datetime:")
print(a)
print("\nCurrent local datetime:")
b = arrow.now()
print(b)
print("\nSpecified local datetime (US/Mountain):")
c = arrow.now('US/Mountain')
print(c)
