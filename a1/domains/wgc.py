## ORDER: wolf, goat, cabbage, farmer --> 0 represents entity on left bank, 1 represents entity on right
## represented by tuple --> (0, 0, 0, 0) = all on left
## (0, 1, 0, 0) --> all on left except goat

class wgc:
    def __init__(self):
        self.init_state = (0, 0, 0, 0)
        self.goat_state = (1, 1, 1, 1)

    def possibleActions(self, state):
        pass

    def goal_test(self, state):
        pass
