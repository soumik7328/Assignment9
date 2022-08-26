#Assignment - 9 Full Stack Web Development using Python MySirG While Loop
#1. Write a python script to print MySirG N times on the screen
j=1
i=eval(input("How many time you want to print MySirG:-"))
while(j<=i):
    print("MySirG")
    j=j+1
#2. Write a python script to print first N natural numbers
j=1
i=eval(input("How many first N natural numbers you want to print:-"))
while(j<=i):
    print(j)
    j=j+1
#3. Write a python script to print first N natural numbers in reverse order
j=1
i=eval(input("How many first N natural numbers you want to print in reverse order:-"))
while(i>=j):
    print(i)
    i=i-1
#4. Write a python script to print first N odd natural numbers
i=eval(input("How many first N odd natural numbers want to print:-"))
for a in range(1,2*i,2):
    print(a, end=" ")
#5. Write a python script to print first N odd natural numbers in reverse order
i=eval(input("How many first N odd natural numbers want to print in reverse order:-"))
for j in range(2*n-1,0,-1):
    print(i,end=" ")
#6. Write a python script to print first N even natural numbers
i=eval(input("How many first N even natural numbers want to print:-"))
for a in range(2,i*2+1,2):
    print(a, end=" ")
#7. Write a python script to print first N even natural numbers in reverse order
i=eval(input("How many first N even natural numbers want to print in reverse order:-"))
for a in range(2*i,1,-2):
    print(a, end=" ")
#8. Write a python script to print squares of first N natural numbers
j=1
i=eval(input("How many first N natural numbers squares you want to print:-"))
while(j<=i):
    print(j**2)
    j=j+1
#9. Write a python script to print cubes of first N natural numbers
j=1
i=eval(input("How many first N natural numbers squares you want to print:-"))
while(j<=i):
    print(j**3)
    j=j+1 
#10. Write a python script to print first 10 multiples of N
j=1
i=eval(input("Enter a number whose first 10 multiples you want:-"))
while j<=10:
    print(j*i)
    j=j+1
