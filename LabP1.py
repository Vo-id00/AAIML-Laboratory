import random

class GridEnvironment:
    def __init__(self, width, height, obstacles, tasks):
        self.width = width
        self.height = height
        self.obstacles = obstacles  # list of (x,y)
        self.tasks = tasks          # list of (x,y)
        self.agent_pos = (0, 0)     # starting position

    def percept(self):
        x, y = self.agent_pos
        percepts = {
            "current_position": (x, y),
            "is_obstacle": self.agent_pos in self.obstacles,
            "is_task": self.agent_pos in self.tasks
        }
        return percepts

    def execute_action(self, action):
        x, y = self.agent_pos
        if action == "UP" and y > 0 and (x, y - 1) not in self.obstacles:
            self.agent_pos = (x, y - 1)
        elif action == "DOWN" and y < self.height - 1 and (x, y + 1) not in self.obstacles:
            self.agent_pos = (x, y + 1)
        elif action == "LEFT" and x > 0 and (x - 1, y) not in self.obstacles:
            self.agent_pos = (x - 1, y)
        elif action == "RIGHT" and x < self.width - 1 and (x + 1, y) not in self.obstacles:
            self.agent_pos = (x + 1, y)
        elif action == "CLEAN" and self.agent_pos in self.tasks:
            print(f"Task completed at {self.agent_pos}!")
            self.tasks.remove(self.agent_pos)

    def print_grid(self):
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if (x, y) == self.agent_pos:
                    row += " A "
                elif (x, y) in self.obstacles:
                    row += " X "
                elif (x, y) in self.tasks:
                    row += " T "
                else:
                    row += " . "
            print(row)
        print("\n")

class SimpleReflexAgent:
    def __init__(self, environment):
        self.env = environment

    def rule_match(self, percepts):
        if percepts["is_task"]:
            return "CLEAN"
        else:
            return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def run(self, steps=20):
        # Print initial grid once
        print("Initial Grid:")
        self.env.print_grid()

        for step in range(steps):
            percepts = self.env.percept()
            action = self.rule_match(percepts)
            self.env.execute_action(action)
            print(f"Step {step+1}: Agent at {self.env.agent_pos}, Action: {action}")

# Example setup
env = GridEnvironment(width=5, height=5,
                      obstacles=[(1,1), (2,2), (3,3)],
                      tasks=[(0,2), (4,4)])
agent = SimpleReflexAgent(env)
agent.run(15)
