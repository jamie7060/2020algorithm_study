def roll_call(A):
    if A in students:
        return students[A]
    else:
        return "?"

students = {
39: "Justin",
14: "John",
67: "Mike",
105: "Summer"
}

print(roll_call(105))
print(roll_call(33))
print(roll_call(106))
print(roll_call(39))

