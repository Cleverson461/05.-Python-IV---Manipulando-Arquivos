courses = []

with open("courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        course =  {}
        course["language"] = language
        course["category"] = category
        courses.append(course)
print(courses)
print()

for course in sorted(courses, key=lambda course: course['language']):
    print(f"{course['language']}-{course['category']}")
    
print(10 * ' ')

for course in sorted(courses, key=lambda course: course['category']):
    print(f"{course['language']}-{course['category']}")