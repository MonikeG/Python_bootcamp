

#Love Calculator by buzzfeed


print("Welcome to the Love Calculator!")
print('on this calculator you will find if your love matches with you')
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

name_combine = name1_lower  + name2_lower
#print(name_combine)

T = name_combine.count('t')
#print(T)

R = name_combine.count('r')
#print(R)

U = name_combine.count('u')
#print(U)

E = name_combine.count('e')
#print(E)

sum1 = T+R+U+E
#print (sum1)

L = name_combine.count('l')
#print(L)

O = name_combine.count('o')
#print(O)

V = name_combine.count('v')
#print(V)

E = name_combine.count('e')
#print(E)

sum2 = L+O+V+E
#print (sum2)

if sum1 >= 10:
    sum1_list = list(str(sum1))
    sum1_sum = int(sum1_list[0]) + int(sum1_list[1])
    #print(sum1_sum)
    sum1_str = str(sum1_sum)


if sum2 > 9:
    sum2_list = list(str(sum2))
    sum2_sum = int(sum2_list[0]) + int(sum2_list[1])
    #print(sum2_sum)
    sum2_str = str(sum2_sum)

    result = sum1_str + sum2_str

else:
    sum1_str = str(sum1)
    sum2_str = str(sum2)


    result = sum1_str + sum2_str

result_int = int(result)
#print(result_int)

if result_int < 10 or result_int > 90:
    print (f'Your score is {result}, you go together like coke and mentos.')
elif result_int >=40 and result_int <= 50:
    print (f'Your score is {result}, you are alright together')
else:
    print(f'Your score is {result}. You are awesome together!!!')


