import copy


def graph_search(problema):
    frontera = []
    explored = []
    estado = problema.start
    camino = []

    while True:
        if len(frontera):
            camino = problema.criterio(frontera)
            explored.append(camino)
            if problema.goal_test(estado):
                return camino
            for a in problema.actions(estado):
                if a not in explored:
                    new_path = copy.deepcopy(camino)
                    new_path.append(a)
                    frontera.append(new_path)
        else:
            return False
