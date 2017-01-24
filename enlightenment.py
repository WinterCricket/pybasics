import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    sam = turtle.Turtle()
    sam.shape("turtle")
    sam.color("black", "black")
    sam.speed("slow")
    
    total_turns = 3
    turn_count = 0

    while (turn_count <= total_turns):
        sam.forward(100)
        sam.right(90)
        turn_count = turn_count + 1
    sam.color("black","black")

    total_cycle = 3
    cycle_count = 0

    while (cycle_count <= total_cycle):

        total_turns = 3
        turn_count = 0
        while (turn_count <= total_turns):
            sam.forward(100)
            sam.right(90)
            turn_count = turn_count + 1
        sam.right(45)
        cycle_count = cycle_count + 1
    sam.color("black","yellow")

    total_cycle = 3
    cycle_count = 0
    while(cycle_count <= total_cycle):
        total_turns = 3
        turn_count = 0
        while (turn_count <= total_turns):
            sam.forward(100)
            sam.right(90)
            turn_count = turn_count + 1
        sam.right(45)
        cycle_count = cycle_count + 1
        
    sam.color("yellow") 
    window.bgcolor("green")
    window.exitonclick() 
    
draw_square() 
