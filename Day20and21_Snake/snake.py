from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        self.segment_gap = 0
        self.creat_snake()

    def creat_snake(self):
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.teleport(self.segment_gap, 0)
            self.segment_gap -= 20
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].teleport(new_x, new_y)

        self.segments[0].forward(20)
