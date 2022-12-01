# graph renderer
def printGraph(height, val):
    i = 0
    x = 0
    for i in range(int(height)):
        print("", end = '\n')
        line = height - i
        for x in range(int(len(val))):
            if val[x] == height - i:
                print("•", end = "               ")
            else:
                print("               ", end = "")
printGraph(10, [3, 3, 7, 5, 6, 9, 8, 1, 3, 5, 6, 6])
