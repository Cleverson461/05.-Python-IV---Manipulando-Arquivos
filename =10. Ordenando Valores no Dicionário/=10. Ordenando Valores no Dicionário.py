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

def get_language(course):
    return course["language"]

def get_category(course):
    return course["category"]

for course in sorted(courses, key=get_language):
    print(f"{course['language']}-{course['category']}")
    

print(10 * ' ')

for course in sorted(courses, key=get_category):
    print(f"{course['language']}-{course['category']}")