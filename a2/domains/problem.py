import random

def createStart():
    while True:
        start = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        random.shuffle(start)
        tiles = [num for num in start if num !=0]
        count = 0

        length = len(tiles)
        for i in range(length):
            for j in range(i+1, length):
                if tiles[i] > tiles[j]:
                    count +=1

        if count % 2 == 0:
            print(count)
            return start

class Problem:
    def __init__(self):
        self.init_state = createStart()
        self.goal_state = [1, 2, 3, 
                           4, 5, 6, 
                           7, 8, 0]
        self.total_nodes = 0
        self.nodes_expanded = 0
        self.max_frontier = 0
        self.depth = 0

    def Actions(self, state):
        index_zero = state.index(0)
        row = index_zero // 3
        column = index_zero % 3
        valid =[]

        if row > 0:
            valid.append('n')
        if row < 2:
            valid.append('s')
        if column > 0:
            valid.append('w')
        if column < 0: 
            valid.append('e')

        return valid
    
    def Transition(self, state, action):
        i0 = state.index(0)
        
        if action == 'n':
            temp = state[i0 - 3]
            state[i0-3] = 0
            state[i0] = temp
        if action == 's':
            temp = state[i0 + 3]
            state[i0 + 3] = 0
            state[i0] = temp
        if action == 'e':
            temp = state[i0 + 1]
            state[i0 + 1] = 0
            state[i0] = temp
        if action == 'w':
            temp = state[i0 + 1]
            state[i0 + 1] = 0
            state[i0] = temp
        
        return state