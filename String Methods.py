# strings
course = 'Python for Beginners'
another = course[:]
print(another)
name = 'Jennifer'
print(name[1:-1])

# Formatted strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder '
print(message)
print(msg)

# string Methods
course = 'Python for Beginners'
print('Python' in course)
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.find('Beginners'))
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
