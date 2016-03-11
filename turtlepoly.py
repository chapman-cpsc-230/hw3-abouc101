import turtle
bob = turtle.Pen()

sides_inp =raw_input("Enter number of Sides")
sides = int(sides_inp)

length_inp =raw_input("Enter how long you want each side to be")
length = int(length_inp)

for side in range(sides):
    bob.forward(length)
    bob.right(360.0/sides)

inp = raw_input('Press Enter to Exit')

turtle.bye()
