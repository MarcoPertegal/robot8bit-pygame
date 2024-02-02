import random
class world_1:
    def load_map(self):
        with open('map.txt', 'r') as file:
            first_line = file.readline().strip().split(', ')
            objets = {item.split(':')[0]: int(item.split(':')[1]) for item in first_line}
            mapa = [linea.strip() for linea in file]
        point_coords = []
        for y in range(len(mapa)):
            for x in range(len(mapa[y])):
                if mapa[y][x] == '.':
                    point_coords.append((x, y))

        for obj, count in objets.items():
            for _ in range(count):
                if len(point_coords) == 0:
                    break
                coord = random.choice(point_coords)
                point_coords.remove(coord)
                mapa[coord[1]] = mapa[coord[1]][:coord[0]] + obj + mapa[coord[1]][coord[0] + 1:]

        return objets, mapa
