#Lab3_3.py-Matthew Kim
#had to use int(input('enter a number: ')) because I am working with integers if I only use input('enter a number') the result would be a string which python cannot perform mathematical equations with a string
try:
    a=int(input('enter a number: '))
    b=int(input('enter a number: '))
    c=int(input('enter a number: '))
    print("Please enter the first integer:",a)
    print("Please enter the second integer:",b)
    print("Please enter the third integer:",c)
#used the max() function to determine the largest number in the arrangements
    d=max(a,b,c)
#used the min() function to determine the smallest number in the arrangements
    e=min(a,b,c)
#used another variable to find the middle number added all the numbers and subtracted the min and max number the result would be the remaining number which in this case is the number in between min and max number. 
    f=a+b+c-d-e
    print("Before sorting:",a,b,c)
    print("After sorting:",e,f,d)
except:
    print("Exception:Invalid Input")