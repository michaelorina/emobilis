def say_my_name():
    print("Hey, I am Michael")


def say_my_name(name):  # a parameter or an argument
    print("Hey, My name is " + name)


say_my_name("Michael")


def calculate_volume_cylinder(radius, height):
    vol = 22 / 7 * radius ** 2 * height
    print(vol)
    return vol


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)


v1 = calculate_volume_cylinder(10, 18)
print(round(v1))
print(v1 * 5)

print(calculate_volume_cylinder(height=21, radius=14))  # named args or params

# add_numbers(2,3)
# add_numbers(8.3,2,67,6)
# calculate_volume_cylinder(7,2)
# calculate_volume_cylinder(9,10)
# calculate_volume_cylinder(6,3)
# say_my_name()
# say_my_name()
