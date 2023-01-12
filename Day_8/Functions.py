#Create a function called greet()
#Write 3 print statements inside the function
#Call the greet() function and run your code

def greet(name):
    print(f"Hello, {name}")
    print("You can hire me")
    print("I'm available to work")

greet('recruiter')

#Function with more than 1 input

def greet_with(name, location):
    print(f"Dear {name}")
    print(f"It would be great to work at {location}!")

greet_with('recruiter', 'your company')