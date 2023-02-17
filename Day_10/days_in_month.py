'''In the starting code, you'll find the solution from the Leap Year challenge. 
First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
it should return True if it is a leap year and return False if it is not a leap year.'''

def is_leap(year):
    '''Verify if a year is a leap or not'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



def days_in_month(year, month):
    '''Return the number of the days of a month'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    if is_leap(year) == True:
        month_days[1] = 29
        number_of_days = month_days[month-1]
    else:
        number_of_days = month_days[month-1]
    
    return number_of_days
        

# fazer com que days = month_days[month]


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)