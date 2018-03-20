"""
The number of containers that are clear is equal to the number of
containers that are on the ground. Thus the function checks the
nested lists for the "ground" element and increments the counter by 1
whenever it is found. 
"""
def count_clear(state):
    count = 0
    for pair in state:
        if pair[1] == "ground":
            count += 1
    return count 