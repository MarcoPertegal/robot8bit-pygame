import random
class world_1:
    """
    def load_map(self):
        map_file = 'mapa.txt'
        with open('map.txt', 'r') as archivo:
            first_line = archivo.readline().strip().split(', ')
            objets = {item.split(':')[0]: int(item.split(':')[1]) for item in first_line}
            map = [linea.strip() for linea in archivo]

        return objets, map"""

    def load_map(self):
        map_file = 'mapa.txt'
        with open('map.txt', 'r') as archivo:
            first_line = archivo.readline().strip().split(', ')
            objets = {item.split(':')[0]: int(item.split(':')[1]) for item in first_line}
            mapa = [linea.strip() for linea in archivo]

        # Obtener las coordenadas donde hay puntos
        point_coords = []
        for y in range(len(mapa)):
            for x in range(len(mapa[y])):
                if mapa[y][x] == '.':
                    point_coords.append((x, y))

        # Colocar las letras en lugares aleatorios en el mapa
        for obj, count in objets.items():
            for _ in range(count):
                if len(point_coords) == 0:
                    break
                coord = random.choice(point_coords)
                point_coords.remove(coord)
                mapa[coord[1]] = mapa[coord[1]][:coord[0]] + obj + mapa[coord[1]][coord[0] + 1:]

        return objets, mapa
