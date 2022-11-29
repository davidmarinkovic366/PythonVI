
# codeBreaker = pokusaj za otkrivanje koda
# codeMaker = kod koji pokusavako da otkrijemo
def masterMind(codeBreaker, codeMaker):
    open_set = set()            # za obradu
    closed_set = set()          # obradjene
    prev_state = {}             # istorija koraka
    g = {}                      # tezina samog cvora
    h = {}                      # procena kombinacije
    path = []                   # putanja (istorija)

    store = {}
    store[codeBreaker] = {
        'attempt': codeBreaker,
        'taken': codeBreaker,
        'free': list([i * (4 - codeBreaker.count(i)) for i in ['w', 'y', 'r', 'g', 'b']])
        # free: ['www', 'yyy', 'rrr', 'gggg', 'bbb']
    }

    end = False
    open_set.add(codeBreaker)
    g[codeBreaker] = 0  # tezina cvora grafa
    h[codeBreaker] = heuristics(store[codeBreaker], codeMaker) # procena grafa
    prev_state[codeBreaker] = None  # kako smo dosli do ove komb?

    while open_set and not end:
        state = None
        for next_state in open_set:
            h[next_state] = heuristics(store[next_state], codeMaker)
            if state is None or g[next_state] + h[next_state] < g[state] + h[state]:
                state = next_state

        if state == codeMaker:
            end = True
            break

        for ns in findNext(store[state]):
            store[ns['attempt']] = ns
            # Ako nije obradjivano stanje do sada, i ako nije navedeno kao stanje koje treba da se obradi, dodajemo ga u listu, 
            # racunamo heuristiku i dodajemo prethodni korak kao istoriju:
            if ns['attempt'] not in open_set and ns['attempt'] not in closed_set:
                open_set.add(ns['attempt'])
                prev_state[ns['attempt']] = state
                h[ns['attempt']] = heuristics(ns, codeMaker)
                g[ns['attempt']] = g[state] + h[ns['attempt']]
            # Inace, ako je recimo u setu za obradu, ili ako je vec obradjeno stanje, i ako je cena sada dosta povoljnija:
            elif g[ns['attempt']] > g[state] + h[ns['attempt']]:
                g[ns['attempt']] = g[state] + h[ns['attempt']]
                prev_state[ns['attempt']] = state
                # Ukoliko smo ga vec obradili, vracamo ga nazad na obradu:
                if ns['attempt'] in closed_set:
                    closed_set.remove(ns['attempt'])
                    open_set.add(ns['attempt'])

        open_set.remove(state)
        closed_set.add(state)

    if end:
        prev = state
        while prev_state[prev] is not None:
            path = [prev] + path
            prev = prev_state[prev]
        path = [codeBreaker] + path

    return path


def heuristics(state, codeMaker):
    ret = 0
    for i in range(0, 4):
        if codeMaker[i] == state['attempt'][i]:
            ret += 5
        elif codeMaker[i] in state['attempt']:
            ret += 1

    return len(state['taken'])*5 - ret


def findNext(state):

    newStates = []                  # lista u koju postavljamo stanja
    codeBreaker = state['attempt']  # kombinacija koju transformisemo
    free = state['free']            # dostupne kuglice trenutne kombinacije
    taken = state['taken']          # iskoriscene kuglice trenutne kombinacije

    # u trenutnoj situaciji, 'wryb', za sva dostupna slova probati sve moguce 
    # kombinacije, odnosno:
    # [ 
    #   (w:)['wryb', 'wwyb', 'wrwb', 'wryw']
    #   (y:)['yryb', 'wyyb', 'wryb', 'wryy']
    #   (r:)['rryb', 'wryb', 'wrrb', 'wryr']
    #   (g:)['gryb', 'wgyb', 'wrgb', 'wryg']
    #   (b:)['bryb', 'wbyb', 'wrbb', 'wryb']
    # ]

    # Naravno, neke kombinacije ce se istrositi pre ostalih, tako da necemo uvek da imamo 5
    # lista, mozda nekad budu 2?

    for f in range(len(free)):
        if not free[f] == '':
            newStates += [
                {
                    'attempt': free[f][0] + codeBreaker[1:],
                    'taken': taken + free[f][0],
                    'free': list(map(lambda x: (x if x is not free[f] else x.replace(x[0], "", 1)), free))
                },
                {
                    'attempt': codeBreaker[0] + free[f][0] + codeBreaker[2:],
                    'taken': taken + free[f][0],
                    'free': list(map(lambda x: (x if x is not free[f] else x.replace(x[0], "", 1)), free))
                },
                {
                    'attempt': codeBreaker[:2] + free[f][0] + codeBreaker[3],
                    'taken': taken + free[f][0],
                    'free': list(map(lambda x: (x if x is not free[f] else x.replace(x[0], "", 1)), free))
                },
                {
                    'attempt': codeBreaker[:3] + free[f][0],
                    'taken': taken + free[f][0],
                    'free': list(map(lambda x: (x if x is not free[f] else x.replace(x[0], "", 1)), free))
                }
            ]

    # Moze i ovako, svejedno, stanje je validno ako je manje od 20 kuglica istroseno:
    # return list(filter(lambda x: len(x) <= 20, newStates))
    return list(filter(isValid, newStates))


def isValid(state):
    return len(state['taken']) <= 20


end_state = input('Enter final state: ')
start_state = input('Enter start state: ')

solution = masterMind(start_state, end_state)
step_counter = 0
for step in solution:
    print(f"Step[{step_counter}]: ", step)
    step_counter += 1
