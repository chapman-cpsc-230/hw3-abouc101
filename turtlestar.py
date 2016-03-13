import turtle
bob = turtle.Pen()

sides_inp =raw_input("Enter an odd number of Sides")
sides = int(sides_inp)

if sides%2 != 0:
    length_inp =raw_input("Enter how long you want each side to be")
    length = int(length_inp)

    for side in range(sides):
        bob.forward(length)
        bob.right (180-(180.0000/sides)) ### 180.0 is the same as 180.0000

else:
    print 'Please enter an odd number'

inp = raw_input('Press Enter to Exit')

turtle.bye()
