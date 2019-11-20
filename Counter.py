import keyboard

print("add 1 '+'")
print("minus 1 '-'")
print("reset to 0 press '*'")
print("to enter a number press '.'")
print("to change file press '/'")

filename = input("Enter file name(add .txt for text file): ")
deaths = 0
print(deaths)

while True:
    #enter number
    if keyboard.is_pressed('.'):
        if not was_pressed_3:
            print('\n')
            try:
                deaths = int(input("Enter number of deaths(You must enter a number): "))
            except ValueError:
                print("You must enter a number!!!  If you dont It wont dont well, nothing will happpen")
            print(deaths)
            was_pressed_3 = True
    else:
        was_pressed_3 = False
    
    #New File
    if keyboard.is_pressed('/'):
        if not was_pressed_2:
            print('\n')
            filename = input("Enter file name(add .txt for text file): ")
            deaths = 0
            print(deaths)
            was_pressed_2 = True
    else:
        was_pressed_2 = False

    #+1
    if keyboard.is_pressed('+'):
        if not was_pressed:
            deaths += 1
            print(deaths)
            was_pressed = True
            
            f = open(filename, "w+")
            f.write(str(deaths))
            f.close()
    else:
        was_pressed = False

    #-1
    if keyboard.is_pressed('-'):
        if not was_pressed_1:

            f = open('file.txt', 'w').close()
            deaths -= 1
            print(deaths)
            was_pressed_1 = True

            f = open(filename, "w+")
            f.write(str(deaths))
            f.close()
    else:
        was_pressed_1 = False

    #Re-set to 0
    if keyboard.is_pressed('*'):
        if not was_pressed_0:
            deaths = 0
            print(deaths)
            was_pressed_0 = True
                
            f = open(filename, "w+")
            f.write(str(deaths))
            f.close()
    else:
         was_pressed_0 = False
