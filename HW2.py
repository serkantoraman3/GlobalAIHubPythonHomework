N = input("Name: ")
S = input("Surname: ")
A = int(input("Age: "))
DoB = input("Date of Birth(Just Year): ")
mylist = [N, S, A, DoB]


for i in mylist:
    print('\n', i)

    
if A < 18:
    print("\n You can't go out because it's too dangerous!")
else:
    print("\n You can go out to the street.")