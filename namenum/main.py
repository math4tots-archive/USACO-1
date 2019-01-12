import interpools

touch_stone = {2:["A", "B", "C"], 3:["D", "E", "F"], 4:["G", "H", "I"], 5:["J", "K", "L"], 6:["M", "N", "O"], 7:["P", "R", "S"], 8:["T", "U", "V"], 9:["W", "X", "Y"]}

def possible_names(serial):
    '''
    Serial is the string version of the serial number given

    '''
    N = len(serial)
    indexes = list(intertools.combination('012'*N, N))
    current = 0
    all = []
    for ind in indexes:
        name = []
        for i in ind:
            name.append(touch_stone[serial[current]][int(ind[current])])
        all.append("".join(name))

    return all













# def get_story_string():
#     """
#     Returns: a story in encrypted text.
#     """
#     f = open("story.txt", "r")
#     story = str(f.read())
#     f.close()
#     return story