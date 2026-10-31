import math
import time

restarting = "Restarting the Calculator..."
errormessage= "This is not an option"
#logo

title_top = "\033[33m██████████████████████████████████████\033[0m"
title_mid = "\033[33m█   SMILEY CALCULATORS *Alpha v2.0*  █\033[0m"
title_bot = "\033[33m██████████████████████████████████████\033[0m"

width = 200

print("Developer: Ibrahim A. Mohammed")

print(title_top.center(width))
print(title_mid.center(width))
print(title_bot.center(width))

print("An imprint of Smiley Apps")

#border
print("\033[33m-\033[0m" * 200)

while True:
    formofmath = input("Type what kind of equation you are doing (SA for Simple Arithmetic, CI for Circles, TR for Triangles, SGC for simple graphing calculator (if you want to see the update log, please type in UL)): ")

    formofmath = formofmath.upper()

    if formofmath == "UL":
        print("-" * 200)
        print("Welcome to the update log")
        print("Current version: *Alpha v2.0*")
        print("The *Alpha* Version was updated with a simple graphing calculator on 10/3/26")
        print("The *Beta* version will be postponed until further notice")
        print('The name of the program was changed from "Everything Math Calculators" to "Smiley Calculators"')
        print("Announcement: The *Beta* version is expected to come out by 10/20/26")
        print("The *Alpha* Version was updated with a logo on 10/3/26")
        print("The *Alpha* Version was updated with easier to type functions on 10/3/26")
        print("The *Alpha* Version was updated with a triangular calculator on 10/3/ 26")
        print("The *Alpha* version was updated with a circular calculator on 9/21/26")
        print("The *Alpha* Version was created on 9/18/2026")
        

    elif formofmath == "SA":
        print("-" * 200)
        print("You chose Simple Arithmetic!")
        operator = input("Great! What are you trying to do? (+ for addition, - for subtraction, * for multiplication, / for division) ")

        num1 = input("Type in the first number: ")
        num2 = input("Type in the second number: ")

        num1 = float(num1)
        num2 = float(num2)

        if True:
            
            if operator == "+":
                result = num1 + num2
                print(f"The sum is: {result}") 

                
            elif operator == "-":
                result = num1 - num2
                print(f"The difference is: {result}") 

            
            elif operator == "*":
                result = num1 * num2
                print(f"The product is: {result}") 

                    
            elif operator == "/":
                result = num1 / num2
                print(f"The quotient is: {result}") 
            
                
            else:
                print("The operator you picked was not valid")

            
        
        else:
            print("These values are not numbers...")       

    
    
    elif formofmath == "CI":
        print("-" * 200)
        print("You chose Circles!")
       
        circlemethod = input("Great! What are you trying to do/find? (C for circumference, R for radius, D for diameter, P for pi, A for area) ")

        circlemethod = circlemethod.upper()

        if circlemethod == "C":
            print("You are searching for the circumference")
            whatisthetypeofmethod = input("Do you have the radius (type R) or diameter (type D)?: ")
            whatisthetypeofmethod = whatisthetypeofmethod.upper()
            if whatisthetypeofmethod == "R":
                print("You have the radius")
                radius= float(input("Type in the radius"))
                roundingval = int(input("How many digits are you rounding to?: "))
                result= radius * math.pi * 2
                print(f"The circumference is:")
                print(round(result, roundingval))
            

            elif whatisthetypeofmethod == "D":
                print("You have the diameter")
                diameter= float(input("Type in the diameter: "))
                roundingval = int(input("How many digits are you rounding to?: "))
                result= diameter * math.pi
                print(f"The circumference is: {result}")
        
        
        elif circlemethod =="R":
            print("You are searching for the radius")
            whatisthetypeofmethod = input("Do you have the circumference (type C) diameter (type D)?: ")
            whatisthetypeofmethod = whatisthetypeofmethod.upper()
            
            
            if whatisthetypeofmethod == "C":
                print("You have the circumference of the circle")
                circumference= float(input("Type in the circumference: "))
                result = circumference / (math.pi * 2)
                print(f"The radius is: {result}")
            
            
            elif whatisthetypeofmethod == "D":
                print("You have the diameter of the circle")
                diameter = float(input("Type in the diameter: "))
                result = diameter / 2
                print(f"The radius is: {result}")   
        
        
        elif circlemethod =="D":
            print("You are searching for the diameter")
            whatisthetypeofmethod = input("Do you have the circumference (type C) or radius (type R)?: ")
            whatisthetypeofmethod = whatisthetypeofmethod.upper()
        
        
            if whatisthetypeofmethod == "C":
                print("You have the circumference of the circle")
                circumference= float(input("Type in the circumference: "))
                result = circumference / math.pi
                print(f"The diameter is: {result}")
        
        
            elif whatisthetypeofmethod == "R":
                print("You have the radius of the circle")
                radius = float(input("Type in the radius: "))
                result = radius * 2
                print(f"The diameter is: {result}")
        
        
        elif circlemethod =="P":
            print("You are searching for pi")
            print(f"According to top sources, pi is: {math.pi}")
            print("The most common approximation of pi is 3.14")
        
        
        elif circlemethod =="A":
            print("You are searching for the area")
            whatisthetypeofmethod = input("Do you have the radius (type R) or diameter (type D)?: ")
            whatisthetypeofmethod = whatisthetypeofmethod.upper()
        
        
            if whatisthetypeofmethod == "R":
                print("You have the radius of the circle")
                radius = float(input("Type in the radius: "))
                result = math.pi * radius ** 2
                print(f"The area is: {result}")
        
        
            elif whatisthetypeofmethod == "D":
                print("You have the diameter of the circle")
                diameter = float(input("Type in the diameter: "))
                radius = diameter / 2
                result = math.pi * radius ** 2
                print(f"The area is: {result}")
        
            else:
                print(errormessage)
        
        else:
            print(" ")
            print("That is not a current option. We will restart the calculator. Please wait...")

    elif formofmath == "TR":
        print("-" * 200)
        print("You are using the Triangular calculator")
        whatisthetypeofmethod = input("What are you looking for (PT for pythagorean theorum, A for area)?: ")
        whatisthetypeofmethod = whatisthetypeofmethod.upper()
        if whatisthetypeofmethod == "PT":
            print("Your equation includes the pythagorean theorum")
            trianglemethod = input("Are you looking for the hypotinuse (H), or one of the other sides if you have the hypotinuse (OS)?: ")
            trianglemethod = trianglemethod.upper()

            if trianglemethod == "H":
                print("You are looking for the hypotinuse")
                a = float(input("What is the value of a?: "))
                b = float(input("What is the value of b?: "))
                c2 = (a*a) + (b*b)
                c = math.sqrt(c2)
                print(f"The hypotinuse is {c} units long")

            elif trianglemethod == "OL":
                print("You are looking for one side of the triangle that isn't the hypotinuse")
                a = float(input("What is the value of a or b?: "))
                c = float(input("What is the value of c?: "))
                b = (c*c)-(a*a)
                b = math.sqrt(b)
                print(f"The other side is {b} units long")

            else:
                print(errormessage)

        elif whatisthetypeofmethod == "A":

            print("You are looking for the area of a triangle...")
            base = float(input("Type in the base of the triangle: "))
            height = float(input("Type in the height of the triangle: "))
            areaoftriangle = 0.5*base*height
            print(f"The area of the triangle is: {areaoftriangle}^2 units")
            
        else:
            print(errormessage)
    

    elif formofmath == "SGC":
        print("-" * 200)
        print("You are using the brand new Graphing calculator")
        
        
        
        print("Please keep in mind that this is a new feature and may have some limitations, such as not displaying graphs. This calculator is to create a table of values for the given function.")
        equation= input("Are you looking for y=mx+b? (Y/N): ")
        equation = equation.upper()
        if equation == "Y":
            print("You are about to generate a table of values for the equation y=mx+b.")
            howmanyvalues = int(input("How many values do you want to generate? "))
            m = float(input("Enter the slope (m): "))
            b = float(input("Enter the y-intercept (b): "))
            print("x | y")
            print("-" * 20)
            for x in range(-howmanyvalues, howmanyvalues + 1):
                y = m * x + b
                print(f"{x} | {y}")
        else:
            print("Since you chose not to use the y=mx+b form, the calculator will not generate a table of values. We are extremely sorry for the inconvenience.")
        




    
    else:
        print(" ")
        print("That is not a current option. We will restart the calculator. Please wait...")

    print("-" * 200)
    print(restarting)
    print("-" * 200)
    time.sleep(5)
