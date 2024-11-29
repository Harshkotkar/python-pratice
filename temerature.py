#Convert the temperature from degre to fera and from fera to degre
while True:
    unit1=int(input("Enter the unit to  converte :-\n1)Celsius to Kelvin\n2)Kelvin to Celcius\n3)Fahrenheit to Celcius\n4)Celcius to Fahrenheit\n5)Fahrennheit to Kelvin\n6)Kelvin to Fahrenheit\n7)Exit"))
    temp, unit = input("Enter the temperature:: ").split()
    unit3=""
    oldtemp=temp
    temp=int(temp)

    if unit1==1:
        temp +=273.15
        unit="Celsius"
        unit3="Kelvin"
    elif unit1==2:
        temp -=273.15
        unit="Kelvin"
        unit3="Celcius"
    elif unit1==3:
        temp= (temp-32)*5/9
        unit="Fahrenheit"
        unit3="Celsius"
    elif unit1==4:
        temp= (temp*9/5)+32
        unit="Celcius"
        unit3="Fahrenheit"
    elif unit1==5:
        temp=(temp-32)*5/9+273.15
        unit="Fahrenheit"
        unit3="Kelvin"
    elif unit1==6:
        temp=(temp-273.15)*9/5+32
        unit="Kelvin"
        unit3="Fahrenheit"
    elif unit==7:
        print("Exiting.....tata,byebye")
    else:
        print("Enter the valid option.....")

    print(f"Temperature {oldtemp}{unit} converted into {temp:.2f}{unit3}")

    retry=input("Do U want to convert more temperature again (yes/no):: ").strip().lower();
    if retry!="no":
        print("Exiting.....tata,bye-bye....")
        break





