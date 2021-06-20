# Import some dependencies
from turtle import Turtle

# Initialize Some Variables
aligment = "center"
font = ("Vardana", 24, "bold")

# Make the ScoreBoard class inherit from the turtle class so that the scoreboard is a turtle
class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.hideturtle()
		self.pencolor("white")
		self.penup()
		self.goto(0, 250)
		self.write(f"Score: {self.score}", align=aligment, font=font)

	def update(self):
		self.clear()
		self.score += 1
		self.write(f"Score: {self.score}", align=aligment, font=font)

	def game_over(self):
		self.goto(0, 0)
		self.write(f"Game Over.", align=aligment, font=font)