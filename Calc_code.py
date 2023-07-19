import math
def func(x):
    f  = 4*x**8 - math.cos(x)**3 +17*x -3 +math.sin(x) - math.tan(x)**9 #user input of function (change the function tested)
    return f
def dfunc(x):
    h =  0.0000001
    dfunc = ((func(x+h)-func(x))/h) #derivative of function
    return dfunc

def bisection(func, a, b): #function, lower bound, upper bound
    error = abs(int(b)-int(a)) #error helps narrow down the solution to a root
    
    while error > 0.0001: #while a and b aren't essentially equal, set c up.
        c = (a+b)/2
        
        if func(a) * func(b) > 0: #both functions are positive, so there won't be a x intercept
            print("hmm, i don't think there are any roots in this range. sorry, but bisection isn't gonna work!")
            return
        
        elif func(a) * func(c) < 0: #if both a and c are less than 0, then b must move closer
            b = c
            error = abs(a-b) #check the error
        
        elif func(b) * func(c) < 0: #if both functions are less than 0, a must move closer
            a = c
            error = abs(a-b) #check the error

        else:
            print('huh, somehow you broke me. try again and do better, i guess?') #messed something up, oops lol
            return
        
    print("\nthe approximate root of your function is ", c) #display c, the root

def newton(func, dfunc, x): #function, derivative, guess
    for xintercept in range(1, 1000):
        i = x - (func(x)/dfunc(x))
        if dfunc(x) == 0:
            print("hmm, this isn't the vibe, sorry but i can't!")
            return
        x = i
    
    print("\nthe root of the function is ", x) #display x, the root

def secant_bounded(func, a, b): #function, lower guess, upper guess
    for intercept in range(1,1000):
        d = b-a
        if d == 0:
            print("huh, i don't feel so good. something is wrong.")
            return
        k = ((func(b) - func(a))/ (d))  #slope formula
        x = a - (func(a)/k) #new point
        
        if func(x) > 0: #narrowing
            b = x 
            
        elif func(x) < 0: #narrowing
            a = x
            
        
    print("\nthe root of the function is ", x) #display x, the root
    
def secant_consecutive(func, a, b):
    for intercept in range(1,1000):
        d = b-a
        if d == 0:
            print("something is wrong, dividing by 0 isn't the move")
            return
        k = ((func(b) - func(a))/ (d))  #slope formula
        if k==0:
            print("something doesn't feel right, i can't do this.")
            return
        x = a - (func(a)/k) #new point
        
        a = b
        b = x
        
        if abs(func(x)) < 0.0001:
            break
        
    print("\nthe root of the function is ", x) #display x, the root
    
#actual user interface printing below
print("hi! i'm here to help find the root to your function!")
method = input('which method would you like me to use? (bisection, newton, or secant) ')
print('sounds good! ' + method + ' method, here we go!')

if method in ["bisection", "Bisection", "1", "One", "one", "First", "first", "1st"]:
    
    a = int(input("what's your lower bound? ")) #value of a
    print(a, "it is!")

    b = int(input("what's your upper bound? ")) #value of b
    print(b,"okay, let's do it!")
    
    bisection(func, a, b)

elif method in ["newton", "Newton", "2", "Two", "two", "Second", "second", "2nd"]:
    
    x = int(input("give me your best guess, please! ")) #value of x
    print(x,"is a pretty good guess!")
    
    newton(func, dfunc, x)
    
elif method in ["secant", "Secant", "3", "Three", "three", "Third", "third", "3rd"]:
    choice = input("bounded or consecutive? ")
    print(choice, "good choice!")
    
    if choice in ["bounded", "Bounded", "1", "First", "first", "1st", "One", "one"]:

        a = int(input("what is your lower bound? ")) #value of a 
        print(a,"good point!")
    
        b = int(input("what is your upper bound? ")) #value of b
        print(b,"nice one!")
        secant_bounded(func, a, b)
    
    elif choice in ["consecutive", "Consecutive", "2nd", "2", "Two", "two", "Second", "second"]:

        a = int(input("what is your lower bound? ")) #value of a 
        print(a,"good point!")
    
        b = int(input("what is your upper bound? ")) #value of b
        print(b,"nice one!")
        secant_consecutive(func, a, b)
        
    else:
        print("is that a secant method? i couldn't tell.")
    
else:
    print("huh, i don't know that method. try again i guess?") #invalid user input 
