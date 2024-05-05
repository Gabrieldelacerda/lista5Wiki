def quadrado_magico():
    numeros = list(range(1, 10))

    def backtrack(pos=0):
        if pos == 9:
            if numeros[0] + numeros[1] + numeros[2] == numeros[3] + numeros[4] + numeros[5] == numeros[6] + numeros[7] + numeros[8] == \
               numeros[0] + numeros[3] + numeros[6] == numeros[1] + numeros[4] + numeros[7] == numeros[2] + numeros[5] + numeros[8] == \
               numeros[0] + numeros[4] + numeros[8] == numeros[2] + numeros[4] + numeros[6]:
                print(numeros[0], numeros[1], numeros[2])
                print(numeros[3], numeros[4], numeros[5])
                print(numeros[6], numeros[7], numeros[8])
                print()

        for i in range(pos, 9):
            numeros[i], numeros[pos] = numeros[pos], numeros[i]
            backtrack(pos + 1)
            numeros[i], numeros[pos] = numeros[pos], numeros[i]

    backtrack()

quadrado_magico()
