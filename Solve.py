def chec_tab(tab):
    if len(tab) != 9:
        return False

    for e in tab:
        print(e)
        if len(tab) != 9:
            return False

        for i in e:

            if type(i) != type(1) or i < 0 or i > 9:
                return False

    return True

def wys_tab(tab):
    for e in tab:
        print(e)


def count_zeros(tab):
    wynik = 0

    for e in tab:
        for i in e:
            if i == 0: wynik +=1

    return wynik


def clear_after_wstaw(x,y, numer, pos_array):

    pos_array[y][x] = []

    # czyszczenie w kolumnie i wierszu
    for e in pos_array:
        if numer in e[x]:
            e[x].remove(numer)

    for l in pos_array[y]:
        if numer in l:
            l.remove(numer)

    # czyszczenie w kwadracie
    x_k = 3 * (x//3)
    y_k = 3 * (y//3)

    for i in range(3):
        for j in range(3):
            if numer in pos_array[y_k+i][x_k+j]:
                pos_array[y_k+i][x_k+j].remove(numer)
def wstaw(x,y,numer,tab,pos_array):
    print(f"Wstawiam {numer} na pozycji [{x+1},{y+1}]")
    tab[y][x]=numer
    clear_after_wstaw(x,y,numer,pos_array)

def make_posibility_array(tab):

    pos_array = []
    for i in range(9):
        pos_array.append([])
        for j in range(9):
            pos_array[i].append([])

    for i in range(9):
        for j in range(9):
            if tab[i][j] == 0:
                pos_array[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for y in range(9):
        for x in range(9):
            if tab[y][x] != 0:
                clear_after_wstaw(x, y, tab[y][x], pos_array)


    return pos_array

def alg_single(tab,pos_array):

    flag = False

    for y in range(9):
        for x in range(9):
            if len(pos_array[y][x])==1:
                wstaw(x,y,pos_array[y][x][0],tab,pos_array)
                flag=True

    return flag


def alg_single_in_row(tab, pos_array):

    flag = False
    for y in range(9):
        pom = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pozycja = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for x in range(9):
            for i in range(len(pos_array[y][x])):
                pom[pos_array[y][x][i]] += 1
                pozycja[pos_array[y][x][i]] = [x, y]

        for i in range(1,10):
            if pom[i] == 1:
                wstaw(pozycja[i][0], pozycja[i][1], i, tab, pos_array)
                flag = True
    return flag


def alg_single_in_column(tab, pos_array):

    flag = False
    for x in range(9):
        pom = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pozycja = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for y in range(9):
            for i in range(len(pos_array[y][x])):
                pom[pos_array[y][x][i]] += 1
                pozycja[pos_array[y][x][i]] = [x, y]

        for i in range(1,10):
            if pom[i] == 1:
                wstaw(pozycja[i][0], pozycja[i][1], i, tab, pos_array)
                flag = True
    return flag


def solve(tab):

    if not chec_tab(tab):
        print("Error dane wejsciowe")
        return -1

    zeros = count_zeros(tab)

    pos_array = make_posibility_array(tab)
    works = True

    while(works):
        works=False
        if alg_single(tab,pos_array) \
                or alg_single_in_row(tab, pos_array) \
                or alg_single_in_column(tab, pos_array):
            works = True


    # while alg_single(tab,pos_array):pass
    #
    # print(pos_array)
    # alg_single_in_row(tab, pos_array)
    # print(pos_array)
    # alg_single_in_column(tab, pos_array)
    # print(pos_array)
    wys_tab(tab)
    print(pos_array)



problem_tab\
    = [[4,0,0,3,0,5,0,6,8],
       [3,0,0,0,9,0,0,0,0],
       [0,0,2,7,6,0,3,0,0],

       [0,0,0,4,3,2,7,1,6],
       [0,0,0,0,0,0,0,0,3],
       [0,4,3,0,0,0,0,0,2],

       [0,0,0,9,8,0,6,0,1],
       [8,0,7,0,1,6,0,0,0],
       [6,0,0,0,0,0,2,8,0]]

solve(problem_tab)