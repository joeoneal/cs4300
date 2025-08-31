## ORDER: wolf, goat, cabbage, farmer --> 0 represents entity on left bank, 1 represents entity on right
## represented by tuple --> (0, 0, 0, 0) = all on left
## (0, 1, 0, 0) --> all on left except goat

class wgc:
    def __init__(self):
        self.init_state = (0, 0, 0, 0)
        self.goat_state = (1, 1, 1, 1)
        
    def nothing_eaten(self, state):  
        w = state[0]
        g = state[1]
        c = state[2]
        f = state[3]

        if f == 0:
            if g == 1 and w == 1: 
                return False
            if g ==1 and c == 1:
                return False
        if f == 1:
            if g == 0 and w == 0:
                return False
            if g == 0 and c == 0:
                return False
        
        return True

    def result(self, state, action):
        next_state = list(state)
        bank = 1 - state[3]
        for i in action:
            next_state[i] = bank

        return tuple(next_state)

    
    def possibleActions(self, state):
        actions = []
        f = state[3]

        ## 0 = with wolf, 1 = with goat, 2 = with cabbage, 3 = alond

        actions.append((3,))

        # need to check if the entity is on the same bank as the farmer
        for i in range(3):
            if state[i] == f:
                actions.append((3, i))

        # filter out illegal actions
        good_boys = []
        for action in actions:
            if self.nothing_eaten(self.result(state, action)):
                good_boys.append(action)

        return good_boys
            
    def goal_test(self, state):
        return state == self.init_state
