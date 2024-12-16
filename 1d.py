totstu = int(input("Enter total number of students: "))
print("Student details:")

stu = []
numsub = 3  # Assuming there are 3 subjects

for i in range(totstu):
    name = input(f"Enter name of student {i+1}: ")
    marks = []
    for j in range(numsub):
        mark = float(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)
    stu.append((name, marks))

highavg = 0
topper = ""
subtop = [("", 0) for _ in range(numsub)]

for student in stu:
    name, marks = student
    avg = sum(marks) / len(marks)
    if avg > highavg:
        highavg = avg
        topper = name
    
    for j in range(numsub):
        if marks[j] > subtop[j][1]:
            subtop[j] = (name, marks[j])

print("\nStudent Details and Marks:")
for student in stu:
    name, marks = student
    avg = sum(marks) / len(marks)
    print(f"Name: {name}, Marks: {marks}, Average: {avg:.2f}")

print(f"\nHighest average marks: {highavg:.2f} by {topper}")

for j in range(numsub):
    print(f"Topper in Subject {j+1}: {subtop[j][0]} with {subtop[j][1]} marks")
