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

matriz = [
 ['1', '1', '0', '0', '0'],
 ['0', '1', '0', '0', '1'],
 ['1', '0', '0', '1', '1'],
 ['0', '0', '0', '0', '0'],
 ['1', '0', '1', '1', '0']
]




coord_set = set()



ilhas = []
for x,i in enumerate(matriz):
    for y,j in enumerate(i):
        if ((x,y) not in coord_set) and j == '1':
            ilha, new_set = ilha_coord((x,y),coord_set)
            coord_set = coord_set.union(new_set)
            ilhas.append(ilha)


maior_ilha = []
menor_ilha = ['0' for _ in range(len(matriz)*len(matriz[0]))]
for ilha in ilhas:
    if len(maior_ilha) < len(ilha):
        maior_ilha = ilha
    
    if len(menor_ilha) > len(ilha):
        menor_ilha = ilha

centroide_menor = []
print(menor_ilha)
x_sum,y_sum = 0,0
for i in menor_ilha:
    xn, yn = i
    x_sum += xn
    y_sum += yn

centroide_maior = []
print(maior_ilha)
x_sum1,y_sum1 = 0,0
for i in menor_ilha:
    xn, yn = i
    x_sum1 += xn
    y_sum1 += yn



print((x_sum/len(menor_ilha),y_sum/len(menor_ilha)))

print((x_sum1/len(maior_ilha),y_sum1/len(maior_ilha)))