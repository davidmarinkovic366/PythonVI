table = [
    # [2, 0, 1, 0],
    # [1, 2, 0, 0],
    # [0, 0, 0, 3],
    # [0, 0, 3, 1]
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


# status = {
#     table: {
#         'prev': None,
#         'selected': (0, 0),
#         'stat': None
#     }
# }

status = dict()


def algorithm(table: list[list[int]]) -> list[list[int]] or None:

    if table is not None:
        # Ukoliko smo dosli do situacije da nemamo cvor sa vrednoscu 0:
        if is_end(table):
            return table

        # Ukoliko imamo cvor koji je 0, a nema mogucnosti da dobije neku vrednost:
        if not check_valid(status[transform_to_string(table)]['stat']):
            return None
    
        current_status = status[transform_to_string(table)]
        lista = get_all_unprocessed(current_status['stat'])

        for pos in lista:
            new_table = table
            new_table[pos[0]][pos[1]] = current_status['stat'][pos]['available'].pop(0)
            status[transform_to_string(new_table)] = {
                'prev': transform_to_string(table),
                'selected': pos,
                'stat': caclulate_stat(new_table)
            }

            res = algorithm(new_table)
            if res:
                return new_table
            else:
                return None


# Kreira dict koji sadrzi ogranicenja za sve elemente u matrici:
def caclulate_stat(table: list[list[int]]) -> dict:

    stat = {}

    for i in range(len(table)):
        for j in range(len(table[i])):
            if not table[i][j] == '0':
                stat[(i, j)] = {
                    'processed': True,
                    'available': [table[i][j]]
                }
            else:
                available = check_available(table, i, j)
                stat[(i, j)] = {
                    'processed': False,
                    'available': list(filter(lambda x: x not in available, ['1', '2', '3', '4']))
                }
    
    # for k in stat.keys():
    #     print(k, ":", stat[k])
    
    return stat



def check_available(table: list[list[int]], x: int, y: int) -> list[int]:
    
    constraints = set()
    # Provera po redu (horizontalno)
    for i in range(0, 4):
        if not table[x][i] == '0' and table[x][i] not in constraints:
            constraints.add(table[x][i])
    
    # Provera po koloni (vertikalno)
    for j in range(0, 4):
        if not table[j][y] == '0' and table[j][y] not in constraints:
            constraints.add(table[j][y])

    # Provera u podpolju? Moze i bez ovog, radi, ali celu tablu 4x4 gleda kao jednu kocku, ne razdvaja na 4 manje dimenzija 2x2:
    # Nije ni navedeno u zadatku da treba, ali eto, moze;
    posX = int(x / 2)
    posY = int(y / 2)

    if posX == 1:
        posX += 1

    if posY == 1:
        posY += 1

    for i in range(posX, posX+2):
        for j in range(posY, posY+2):
            if not table[i][j] == '0' and table[i][j] not in constraints:
                constraints.add(table[i][j])

    # [1, 2, 3] npr;
    # print(list(constraints))
    return list(constraints)


def get_all_unprocessed(stat: dict) -> list[tuple]:

    unprocessed_list = list()
    for k in stat.keys():
        if stat[k]['processed'] == False:
            unprocessed_list.append((k, stat[k]['available']))
    
    unprocessed_list.sort(key=lambda x: len(x[1]))
    unprocessed_list = list(map(lambda x: x[0], unprocessed_list))

    return(unprocessed_list)


def main(table):

    # Status trenutnog cvora koji obradjujemo
    stat = caclulate_stat(table)
    # Lista cvorova koju trebamo da obradimo
    lista = get_all_unprocessed(stat)

    status[transform_to_string(table)] = {
        'prev': None,
        'selected': lista.pop(0),
        'stat': stat
    }

    result = algorithm(table)

    if result:

        # history_list = list()
        # history_list.append(result)

        # tmp = status[transform_to_string(result)]['prev']
        # while tmp is not None:
        #     history_list.append(transform_to_matrix(tmp))
        #     tmp = status[tmp]['prev']

        # history_list.reverse()

        # print("Result is:")
        # for i in range(history_list):
        #     print("Step: 1")
        #     for j in history_list[i]:
        #         print(j)
        #     print("")

        print("Result is: ")
        for i in result:
            print (i)

    else:
        print("Unsolvable!")




# Da li postoji pozicija/cvor koji nije obranjen, a nema ni jedno moguce stanje u koje moze da predje?
def check_valid(stat: dict) -> bool:
    for key in stat.keys():
        if stat[key]['processed'] == False and len(stat[key]['available']) == 0:
            return False
    return True

# Da li smo dosli do kraja/ sve pozicije obradjene?
def is_end(table: list[list[str]]) -> bool:
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == '0':
                return False
    return True


# Liste u pythonu ne mogu da se koriste kao key vrednost unutar dict, morao sam ovako da napravim
# 'workaround' resenje gde listu pretvaramo u string i obrnuto:

def transform_to_matrix(data: str) -> list[list['str']]:

    lista = list()
    for i in range(4):
        lista.append(list())
        for j in range(4):
            lista[i].append(data[i*4 + j])
    
    # for i in lista:
    #     print(i)

    return lista

def transform_to_string(table: list[list[str]]):
    data = ''
    for i in range(len(table)):
        for j in range(len(table[i])):
            data += table[i][j]

    return data

# Unos inicijalne tabele, od 1 do 4, 0 oznacava prazno mesto:
dim = 4
initial_table = list()
for i in range(dim):
    initial_table.append(list())
    for j in range(dim):
        initial_table[i].append((input(f"Enter val for [{i}][{j}]: ")))

main(initial_table)

