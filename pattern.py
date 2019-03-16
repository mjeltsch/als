dots = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

def getopposite(dot):
    if dot == [0,1]: return [2,1]
    if dot == [1,0]: return [1,2]
    if dot == [2,1]: return [0,1]
    if dot == [1,2]: return [1,0]

def getvaliddots2(dot, filled_dots):
    if dot == [0,0]:
        valid = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]
        if [1,0] in filled_dots:
            valid.append([2,0])
        if [0,1] in filled_dots:
            valid.append([0,2])
        if [1,1] in filled_dots:
            valid.append([2,2])
            
    elif dot == [0,1]:
        valid = [[0, 0], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 2]]
        if [1,1] in filled_dots:
            valid.append([2,1])
            
    elif dot == [0,2]:
        valid = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]
        if [0,1] in filled_dots:
            valid.append([0,0])
        if [1,2] in filled_dots:
            valid.append([2,2])
        if [1,1] in filled_dots:
            valid.append([2,0])

    elif dot == [1,0]:
        valid = [[0, 0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]
        if [1,1] in filled_dots:
            valid.append([1,2])

    elif dot == [1,1]:
        valid = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]
        
    elif dot == [1,2]:
        valid = [[0, 0], [0, 1], [0, 2], [1, 1], [2, 0], [2, 1], [2, 2]]
        if [1,1] in filled_dots:
            valid.append([1,0])

    elif dot == [2,0]:
        valid = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]
        if [1,0] in filled_dots:
            valid.append([0,0])
        if [2,1] in filled_dots:
            valid.append([2,2])
        if [1,1] in filled_dots:
            valid.append([0,2])

    elif dot == [2,1]:
        valid = [[0, 0], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 2]]
        if [1,1] in filled_dots:
            valid.append([0,1])

    elif dot == [2,2]:
        valid = [[0, 1], [1, 0], [1, 1], [1, 2], [2, 1]]
        if [2,1] in filled_dots:
            valid.append([2,0])
        if [1,2] in filled_dots:
            valid.append([0,2])
        if [1,1] in filled_dots:
            valid.append([0,0])

    return [item for item in valid if item not in filled_dots]

def getpaths(n):
    paths = []
    for d in dots:
        valid = getvaliddots2(d, [])
        for e in valid:
            valid2 = getvaliddots2(e, [d])
            for f in valid2:
                valid3 = getvaliddots2(f, [d, e])
                for g in valid3:
                    if n == 4:
                        paths.append([d, e, f, g])
                    else:
                        valid4 = getvaliddots2(g, [f, d, e])
                        for h in valid4:
                            if n == 5:
                                paths.append([d, e, f, g, h])
                            else:
                                valid5 = getvaliddots2(h, [f, d, e, g])
                                for i in valid5:
                                    if n == 6:
                                        paths.append([d, e, f, g, h, i])
                                    else:
                                        valid6 = getvaliddots2(i, [d, e, f, g, h])
                                        for j in valid6:
                                            if n == 7:
                                                paths.append([d, e, f, g, h, i, j])
                                            else:
                                                valid7 = getvaliddots2(j, [d, e, f, g, h, i])
                                                for k in valid7:
                                                    if n == 8:
                                                        paths.append([d, e, f, g, h, i, j, k])
                                                    else:
                                                        valid8 = getvaliddots2(k, [d, e, f, g, h, i, j])
                                                        for l in valid8:
                                                            if n == 9:
                                                                paths.append([d, e, f, g, h, i, j, k, l])
                                                            else:
                                                                valid9 = getvaliddots2(l, [d, e, f, g, h, i, j, k])
                                                                for m in valid9:
                                                                    if n == 9:
                                                                        paths.append([d, e, f, g, h, i, j, k, l, m])




                                
    return paths

def getpaths2(n, i, path, valid):
    paths = []
    for d in valid:
        if n == i:
            paths.append(path)
        else:
            newvalid = getvaliddots2(d, path)
            paths.append(getvaliddots(n, i+1, path, valid))


def getallpaths():
    paths = 0
    for i in range(4,10):
        paths += len(getpaths(i))
    return paths
