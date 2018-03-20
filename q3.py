def find_top(state, curr):
    for pair in state:
        #looking for the pair where the specified container is on the
        #top and returns said pair
        if pair[0] == curr:
            return pair
    return 0

def update(plan, state):
    #looping through every move in plan
    for move in plan:
        #checks for valid move
        if move[0] == "stack":
            #checks for an addition of a new container onto the ground
            if move[2] == "ground":
                state += [[move[1], move[2]]]
            #checks if the container to be moved is on top of another
            #container, removes that list from the plan and adds in
            #the new list in state
            if find_top(state, move[1]):
                pair = find_top(state, move[1])
                state.remove(pair)
                state+= [[move[1], move[2]]]
            #if it is an addition of a new container, container is put
            #on top of one of the existing containers
            else:
                state += [[move[1], move[2]]]
         
    return sorted(state)