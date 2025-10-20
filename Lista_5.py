matriz = [
 ['1', '1', '0', '0', '0'],
 ['0', '1', '0', '0', '1'],
 ['1', '0', '0', '1', '1'],
 ['0', '0', '0', '0', '0'],
 ['1', '0', '1', '1', '0']
]




def vizinhos(coord):
    mov = [-1,0,1]
    vizinhos = []
    x,y = coord
    for i in mov:
        for j in mov:
            if (0<=x+i<len(matriz)) and (0<=y+j<len(matriz[0])) :
                vizinhos.append((x+i,y+j))

    return vizinhos


def ilha_coord(coord,coord_set):
    ilha_list = []
    def ilha(coord,coord_set):
        for i in vizinhos(coord):
            x,y = i
            if (matriz[x][y] == '1') and (i not in coord_set):
                ilha_list.append(i)
                coord_set.add(i)
                ilha(i,coord_set)

    ilha(coord,coord_set)
    return ilha_list, coord_set


coord_set = set()



ilhas = []
for x,i in enumerate(matriz):
    for y,j in enumerate(i):
        if ((x,y) not in coord_set) and j == '1':
            ilha, new_set = ilha_coord((x,y),coord_set)
            coord_set = coord_set.union(new_set)
            ilhas.append(ilha)
    
    
print(ilhas)
            


        


