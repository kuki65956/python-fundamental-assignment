

i1 = 10
i2 = 20
f1= 15.5
f2 = 4.5
s1 = "Hello"
s2 = "World"
b1= True
b2 = False

int_sum = i1 + i2
float_sum = f1+ f2


string = s1 + " " + s2

logical_and = b1 and b2
logical_or = b1 or b2

data_dict = {
    'int': [i1, i2, int_sum],
    'float': [f1, f2, float_sum],
    'str': [s1, s2, string],
    'bool': [b1, b2, logical_and, logical_or]
}


print("Results of Operations:")
print(f"Integer Sum: {int_sum}")
print(f"Float Sum: {float_sum}")
print(f" String: '{string}'")
print(f"Logical AND: {logical_and}")
print(f"Logical OR: {logical_or}")

print("\nVariables categorized by type:")
for key in data_dict:
    print(f"{key}: {data_dict[key]}")