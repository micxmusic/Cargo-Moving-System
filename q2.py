"""
find takes the state and current container name to return the next pair
that contains that container name if it exists, else it returns 0
"""
def find(state, curr):
    for pair in state:
        #looking for the pair where the specified container is on the
        #bottom and returns said pair
        if pair[1] == curr:
            return pair
    #if the pair is not found then 0 is returned
    return 0

"""
build_stack takes in the state, current container (string) and the 
stack(list) and returns a list of the containers in the order of bottom 
to top
"""
def build_stack(state, curr, stack):
    #base case: find does not return a value (reached top of container
    #stack)
    if not find(state, curr):
        return stack
    #recursive case: adds the next container to the stack before
    #before calling itself again
    else:
        curr_pair = find(state,curr)
        stack.append(curr_pair[0])
        return build_stack(state, stack[len(stack)-1], stack)    

"""
height takes in the state of the containers and returns the height of
the tallest stack
"""
def height(state):
    max_height = 0
    for pair in state:
        #checking for ground to find the start of a container stack
        if pair[1] == "ground":
            curr_height = len(build_stack(state, pair[0], [pair[0]]))
            #checking for height of the stacks for the tallest one
            if curr_height > max_height:
                max_height = curr_height
    return max_height