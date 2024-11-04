import bisect
from collections import defaultdict

class Pokemon:
    def __init__(self, number, name, types):
        self.number = number
        self.name = name
        self.types = types

class PokemonIndex:
    def __init__(self):
        self.by_number = {}
        self.by_name = defaultdict(list)
        self.by_type = defaultdict(list)

    def add_pokemon(self, pokemon):
        self.by_number[pokemon.number] = pokemon
        bisect.insort(self.by_name[pokemon.name.lower()], pokemon)
        for t in pokemon.types:
            self.by_type[t.lower()].append(pokemon)

    def search_by_number(self, number):
        return self.by_number.get(number)

    def search_by_name_proximity(self, query):
        results = []
        for name in self.by_name:
            if query.lower() in name:
                results.extend(self.by_name[name])
        return results

    def search_by_type(self, ptype):
        return self.by_type[ptype.lower()]

    def list_by_number_name(self):
        return sorted(self.by_number.values(), key=lambda x: (x.number, x.name))

    def list_by_name_level(self):
        result = []
        for name in sorted(self.by_name.keys()):
            result.extend(self.by_name[name])
        return result

    def get_pokemons_by_names(self, names):
        return [pokemon for name in names for pokemon in self.by_name[name.lower()]]

    def count_by_type(self, ptype):
        return len(self.by_type[ptype.lower()])

index = PokemonIndex()

index.add_pokemon(Pokemon(1, "Bulbasaur", ["Planta", "Venenoso"]))
index.add_pokemon(Pokemon(2, "Ivysaur", ["Planta", "Venenoso"]))
index.add_pokemon(Pokemon(3, "Venusaur", ["Planta", "Venenoso"]))
index.add_pokemon(Pokemon(4, "Charmander", ["Fuego"]))
index.add_pokemon(Pokemon(5, "Charmeleon", ["Fuego"]))
index.add_pokemon(Pokemon(6, "Charizard", ["Fuego", "Volador"]))
index.add_pokemon(Pokemon(7, "Squirtle", ["Agua"]))
index.add_pokemon(Pokemon(8, "Wartortle", ["Agua"]))
index.add_pokemon(Pokemon(9, "Blastoise", ["Aguar"]))
index.add_pokemon(Pokemon(25, "Pikachu", ["Electrico"]))
index.add_pokemon(Pokemon(135, "Jolteon", ["Electrico"]))
index.add_pokemon(Pokemon(745, "Lycanroc", ["Tierra"]))
index.add_pokemon(Pokemon(697, "Tyrantrum", ["Tierra", "Dragon"]))
index.add_pokemon(Pokemon(133, "Eevee", ["Normal"]))

nombre_query = "bul"
resultados_nombre = index.search_by_name_proximity(nombre_query)

pokemons_tipo_agua = index.search_by_type("Agua")

listado_ordenado = index.list_by_number_name()
listado_por_nivel = index.list_by_name_level()

consulta_nombres = ["Jolteon", "Lycanroc", "Tyrantrum"]
pokemons_seleccionados = index.get_pokemons_by_names(consulta_nombres)

total_electricos = index.count_by_type("electrico")
total_acero = index.count_by_type("Acero")

print("Resultados de búsqueda por proximidad:", resultados_nombre)
print("Pokémons de tipo agua:", [p.name for p in pokemons_tipo_agua])
print("Listado en orden por número y nombre:", [(p.number, p.name) for p in listado_ordenado])
print("Listado por nivel por nombre:", [p.name for p in listado_por_nivel])
print("Datos de Jolteon, Lycanroc y Tyrantrum:", [(p.number, p.name, p.types) for p in pokemons_seleccionados])
print("Total de Pokémon de tipo eléctrico:", total_electricos)
print("Total de Pokémon de tipo acero:", total_acero)
