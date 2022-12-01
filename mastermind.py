
# start_state = pokusaj za otkrivanje koda (rucno unosimo)
# result = kod koji pokusavako da otkrijemo
def masterMind(start_state, result):

    open_set = set()            # za obradu
    closed_set = set()          # obradjene
    prev_state = {}             # istorija koraka
    g = {}                      # tezina samog cvora
    heur = {}                   # procena kombinacije
    path = []                   # putanja (istorija)

    store = {}
    store[start_state] = {
        'combo': start_state,
        'used': start_state,
        'free': list(map(lambda x: x * (4 - start_state.count(x)), ['r', 'b', 'g', 'w', 'y']))
        # free: ['www', 'yyy', 'rrr', 'gggg', 'bbb']
    }

    found_end = False
    open_set.add(start_state)
    g[start_state] = 0                                          # tezina cvora grafa
    heur[start_state] = calc_heur(store[start_state], result)   # procena grafa
    prev_state[start_state] = None                              # kako smo dosli do ove komb?

    while open_set and not found_end:
        # Trazimo stanje sa min. heur:
        state = None
        for next_state in open_set:
            heur[next_state] = calc_heur(store[next_state], result)
            if state is None or g[next_state] + heur[next_state] < g[state] + heur[state]:
                state = next_state

        # Da li smo dosli do ciljnog stanja?
        if state == result:
            found_end = True
            break

        for next_state in findNext(store[state]):
            store[next_state['combo']] = next_state
            # Ako nije obradjivano stanje do sada, i ako nije navedeno kao stanje koje treba da se obradi, dodajemo ga u listu, 
            # racunamo heuristiku i dodajemo prethodni korak kao istoriju:
            if next_state['combo'] not in open_set and next_state['combo'] not in closed_set:
                open_set.add(next_state['combo'])
                prev_state[next_state['combo']] = state
                heur[next_state['combo']] = calc_heur(next_state, result)
                g[next_state['combo']] = g[state] + heur[next_state['combo']]
            # Inace, ako je recimo u setu za obradu, ili ako je vec obradjeno stanje, i ako je cena sada dosta povoljnija:
            elif g[next_state['combo']] > g[state] + heur[next_state['combo']]:
                # Menjamo cene vezane za dato stanje i cvor iz koga je bolja cena do istog:
                g[next_state['combo']] = g[state] + heur[next_state['combo']]
                prev_state[next_state['combo']] = state
                # Ukoliko smo ga vec obradili, vracamo ga nazad na obradu:
                if next_state['combo'] in closed_set:
                    closed_set.remove(next_state['combo'])
                    open_set.add(next_state['combo'])

        open_set.remove(state)
        closed_set.add(state)

    if found_end:
        prev = state
        while prev_state[prev] is not None:
            path = [prev] + path
            prev = prev_state[prev]
        path = [start_state] + path

    return path


def calc_heur(state, result):
    val = 0
    for i in range(0, 4):
        if result[i] == state['combo'][i]:
            val += 5
        elif result[i] in state['combo']:
            val += 1

    return len(state['used']) * 5 - val


def findNext(start_state):

    possibleStates = []                     # lista u koju postavljamo stanja
    state = start_state['combo']            # kombinacija koju transformisemo
    free = start_state['free']              # dostupne kuglice trenutne kombinacije
    used = start_state['used']              # iskoriscene kuglice trenutne kombinacije

    # u trenutnoj situaciji, 'wryb', za sva dostupna slova probati sve moguce 
    # kombinacije, odnosno:
    # [ 
    #   (w:)['wryb', 'wwyb', 'wrwb', 'wryw']
    #   (y:)['yryb', 'wyyb', 'wryb', 'wryy']
    #   (r:)['rryb', 'wryb', 'wrrb', 'wryr']
    #   (g:)['gryb', 'wgyb', 'wrgb', 'wryg']
    #   (b:)['bryb', 'wbyb', 'wrbb', 'wryb']
    # ]

    for f in range(len(free)):
        # Provera da li smo elemente za dati simbol iskoristili?
        if not free[f] == '':
            possibleStates += [
                {
                    'combo': free[f][0] + state[1:],
                    'used': used + free[f][0],
                    # Izbacujemo jedan simbol, ali samo za element na koji pokazuje free[f];
                    'free': list(map(lambda x: (x if x is not free[f] else x.replace(x[0], "", 1)), free))
                },
                {
                    'combo': state[0] + free[f][0] + state[2:],
                    'used': used + free[f][0],
                    'free': list(map(lambda x: (x if x is not free[f] else x.replace(x[0], "", 1)), free))
                },
                {
                    'combo': state[:2] + free[f][0] + state[3],
                    'used': used + free[f][0],
                    'free': list(map(lambda x: (x if x is not free[f] else x.replace(x[0], "", 1)), free))
                },
                {
                    'combo': state[:3] + free[f][0],
                    'used': used + free[f][0],
                    'free': list(map(lambda x: (x if x is not free[f] else x.replace(x[0], "", 1)), free))
                }
            ]

    # Moze i ovako, svejedno, stanje je validno ako je manje od 20 kuglica istroseno:
    # return list(filter(lambda x: len(x) <= 20, possibleStates))
    return list(filter(is_valid, possibleStates))


def is_valid(state):
    return len(state['used']) <= 20

end_state = input('Enter final state: ')
start_state = input('Enter start state: ')

solution = masterMind(start_state, end_state)

step_counter = 0
for step in solution:
    print(f"Step[{step_counter}]: ", step)
    step_counter += 1

print(f"Combination is found in: {step_counter} steps!~")
