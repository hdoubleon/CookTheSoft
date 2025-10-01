# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import tkinter as tk
import turtle, random
import time


class RunawayGame:
    def __init__(
        self, canvas, runner, chaser, catch_radius=15
    ):  # Changed from 50 to 15
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Timer-related variables
        self.start_time = None
        self.game_time_limit = 30  # 30 second time limit
        self.score = 0
        self.game_over_flag = False

        # Initialize 'runner' and 'chaser'
        self.runner.shape("turtle")
        self.runner.color("blue")
        self.runner.penup()

        self.chaser.shape("turtle")
        self.chaser.color("red")
        self.chaser.penup()

        # Instantiate another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_catched(self):
        """Check if turtles are completely touching (considering turtle size)"""
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        distance = (dx**2 + dy**2) ** 0.5

        # Default turtle size is about 20 pixels, need distance within 10 to be touching
        turtle_size = 10  # turtle radius
        return distance <= turtle_size

    def game_over(self, message):
        """Handle game over processing"""
        self.game_over_flag = True

        # Display game over message
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(0, 0)
        self.drawer.color("red")
        self.drawer.write(
            f"GAME OVER!\n{message}\nFinal Score: {self.score}",
            align="center",
            font=("Arial", 16, "bold"),
        )

        # Restart instructions
        self.drawer.setpos(0, -50)
        self.drawer.color("blue")
        self.drawer.write(
            "Press 'R' to restart or close window to exit",
            align="center",
            font=("Arial", 12, "normal"),
        )

    def restart_game(self):
        """Restart the game"""
        self.game_over_flag = False
        self.score = 0
        self.drawer.clear()
        self.start()

    def start(self, init_dist=400, ai_timer_msec=100):
        self.runner.setpos((-init_dist / 2, 0))
        self.runner.setheading(0)
        self.chaser.setpos((+init_dist / 2, 0))
        self.chaser.setheading(180)

        # TODO) You can do something here and follows.
        self.ai_timer_msec = ai_timer_msec
        self.start_time = time.time()  # Record game start time
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        # Check game over
        if self.game_over_flag:
            return

        # Calculate elapsed time
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.game_time_limit - elapsed_time)

        # Calculate score (based on survival time)
        self.score = int(elapsed_time * 10)

        # Check time out
        if remaining_time <= 0:
            self.game_over("Time's up! Runner wins!")
            return

        self.runner.run_ai(self.chaser.pos(), self.chaser.heading())
        self.chaser.run_ai(self.runner.pos(), self.runner.heading())

        # TODO) You can do something here and follows.
        is_catched = self.is_catched()

        # Calculate distance between turtles
        p = self.runner.pos()
        q = self.chaser.pos()
        distance = ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5

        # Game over when caught
        if is_catched:
            self.game_over("Caught! Chaser wins!")
            return

        # Display game information (added distance info)
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        self.drawer.write(
            f"Time: {remaining_time:.1f}s | Score: {self.score} | Distance: {distance:.1f}",
            font=("Arial", 12, "normal"),
        )

        # Dynamic speed adjustment (gets faster over time)
        dynamic_timer = max(50, self.ai_timer_msec - int(elapsed_time * 2))

        # Note) The following line should be the last of this function to keep the game playing
        self.canvas.ontimer(self.step, dynamic_timer)


class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), "Up")
        canvas.onkeypress(lambda: self.backward(self.step_move), "Down")
        canvas.onkeypress(lambda: self.left(self.step_turn), "Left")
        canvas.onkeypress(lambda: self.right(self.step_turn), "Right")
        canvas.listen()

        # Store game reference (for restart)
        self.game = None

    def run_ai(self, opp_pos, opp_heading):
        pass


class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, opp_pos, opp_heading):
        mode = random.randint(0, 2)
        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)


if __name__ == "__main__":
    # Use 'TurtleScreen' instead of 'Screen' to prevent an exception from the singleton 'Screen'
    root = tk.Tk()
    canvas = tk.Canvas(root, width=700, height=700)
    canvas.pack()
    screen = turtle.TurtleScreen(canvas)

    # TODO) Change the follows to your turtle if necessary
    runner = RandomMover(screen)
    chaser = ManualMover(screen)

    game = RunawayGame(screen, runner, chaser)

    # Add restart key binding
    def restart_handler():
        game.restart_game()

    screen.onkeypress(restart_handler, "r")
    screen.onkeypress(restart_handler, "R")
    screen.listen()

    game.start()
    screen.mainloop()
