def to_matrix(start):
    filas = []
    mat = []
    numfilas = 0
    for a in start:
        filas.append(a)
        numfilas += 1
        if numfilas == 4:
            mat.append(filas)
            filas = []

        return mat
