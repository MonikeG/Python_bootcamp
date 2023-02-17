
#Functions with output

def format_name(f_name,l_name):

    if f_name == "" or l_name == "":
        return "Any name was inputed"

    f_name = f_name.title()
    l_name = l_name.title()

    # #first_name
    # first_letter = str(f_name[0]).upper()
    # name_rest = str(f_name[1:]).lower()
    
    # #last name
    # first_letter_l_name = str(l_name[0]).upper()
    # name_rest_l_name= str(l_name[1:]).lower()
    #print(f_name, l_name)
    return f"Your name is {f_name} {l_name}?"

print(format_name(input("Type your first name:"),input('Type your last name:')))



