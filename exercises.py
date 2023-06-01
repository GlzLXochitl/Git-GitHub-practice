print("Gonzalez Leos America Xochitl utm22030603 .. OOP - U2 - Git & GitHub practice") # Data for the assignment
print("\n")

#1. A list with 5 elements, add a new element and print it using a for loop. 1 commit
lista = [2397862, 697234, 90563217, 72548, 363729] # List with data
print("Exercise 1*********************************") # Start of the exercise
respuesta = input("Start process (y/n): ") # Ask for permission to start the process
if respuesta.lower() == "y": # Start conditional with 'y'
    print("Current data:")
    for element in lista: # Print current data
        print(element)
    print("\n")
    new = input("Add new element (y/n): ") # Ask for permission to add a new element
    if new.lower() == "y": # Start conditional with 'y'
        folionew = input("Enter the new element: ") # Ask and receive a new element
        lista.append(int(folionew))
        print("Updated data:")
        for element in lista: # Print updated data
            print(element)
        print("End (Exercise 1)*********************************") # End of the exercise
    else:
        print("End (Exercise 1)*********************************") # End of the exercise
else:
    print("End (Exercise 1)*********************************") # End of the exercise

#2. A tuple with 7 elements and print it using a while loop. 2 commit
tupla = ("xochitl", "emile", "farfetch", "mario", "corpus", "jaime", "emilio") # Tuple with 7 elements
print("\n")
print("Start Exercise 2*********************************") # Start of the exercise
respuesta = input("Start process (y/n): ") # Ask for permission to start the process
if respuesta.lower() == "y": # Start conditional with 'y'
    indice = 0 # Index at 0
    print("Available elements:")
    while indice < len(tupla): # Print the elements
        print(tupla[indice])
        indice += 1
    print("End (Exercise 2)*********************************") # End of the exercise
    print("\n")
else:
    print("End (Exercise 2)*********************************") # End of the exercise
    print("\n")

#3. A dictionary with 3 properties, modify any of them, and print it. 3rd commit
dictionary = {"Last Medical Appointment Month": "September", "Last Name": "Medina", "First Name": "Mario"} # dictionary with assigned data
print("Start exercise3*********************************") # start the exercise
response = input("Start the process (y/n): ") # prompt with y or n to continue the process
if response.lower() == "y": # this line begins a conditional with y
    print("Current data:")
    for key, value in dictionary.items(): # print the current elements
        print(key + ": " + str(value))
    print("\n")
    modification = input("Modify last medical appointment month? (y/n): ") # ask if modification is desired
    if modification.lower() == "y": # this line begins a conditional with y
        newData = input("Last medical appointment month: ") # prompt and receive the data to be modified
        dictionary["Last Medical Appointment Month"] = newData
        print("Updated data:")
        for key, value in dictionary.items(): # print the updated elements
            print(key + ": " + str(value))
        print("Ends (exercise3)") # end the exercise
    print("\n")
else:
    print("Ends (exercise3)") # end the exercise
    print("\n")
