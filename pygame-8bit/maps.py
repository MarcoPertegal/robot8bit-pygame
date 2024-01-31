class world_1:
    def load_map(self):
        map_file = 'mapa.txt'
        with open('map.txt', 'r') as archivo:
            first_line = archivo.readline().strip().split(', ')
            objets = {item.split(':')[0]: int(item.split(':')[1]) for item in first_line}
            map = [linea.strip() for linea in archivo]

        return objets, map
