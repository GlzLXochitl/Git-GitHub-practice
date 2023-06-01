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