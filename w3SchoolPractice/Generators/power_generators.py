def power_generator(base,exponent):
    result= 1
    for i in range(exponent + 1):
        yield result
        result = result*base

base = int(input("enter base "))
exponent = int(input("enter exponent "))


power_gen = power_generator(base , exponent)

print(f"power of base {base} up to exponent {exponent}")

for power in power_gen:
    print(power)