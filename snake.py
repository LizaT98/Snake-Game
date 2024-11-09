# constant (position)
from turtle import Turtle
from score import Score
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
#create a constant for the distance
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
# create a head attribute,  so we use it instead of typing self.segments[0]
        self.head = self.segments[0]

# these 2 functions below create our snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def reset_snake(self):
        #we use the same attributes and methods as in init because we are resetting our snake
        # create a for loop so the snake from the previous round disappers from the screen
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
# this function adds segments when the snake eats food
    def extend(self):
        self.add_segment(self.segments[-1].position())
        # position() method returns the current position as (x,y)

    def move_snake(self):
    # we start looping through the list of segments
    # now the length is 3, so the index of the last seg on the list is 2
    # instead of 3, we use len(segments)-1 because our list will be growing
    # 0 is the last segment if we loop backwards
    # since we loop in the reverse order, -1 is the step
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # segments[seg_num-1].xcor() returns the x coordinates of the segments
            # in front of the given segment, e.g. if seg_num is 3, it returns
            # the x coordinates of the segment number 2
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # so now we send the segment number 3 to
            # the coordinates of the segment number 2
            self.segments[seg_num].goto(new_x, new_y)
        # the first segment (index 0) will always move the direction ordered by the user,
        # because it's the leading segment
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: # heading()Returns the turtle’s current heading coordinates
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


