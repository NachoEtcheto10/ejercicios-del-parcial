
def contar_especies(dinosaurios):
    especies = set()  
    for dino in dinosaurios:
        especies.add(dino["especie"])
    return len(especies)

def contar_descubridores(dinosaurios):
    descubridores = set()  
    for dino in dinosaurios:
        descubridores.add(dino["descubridor"])
    return len(descubridores)

def mostrar_dinosaurios_T(dinosaurios):
    dinosaurios_con_T = [dino for dino in dinosaurios if dino["nombre"].startswith("T")]
    return dinosaurios_con_T

def mostrar_dinosaurios_ligeros(dinosaurios):
    dinosaurios_ligeros = [dino for dino in dinosaurios if int(dino["peso"].split()[0]) < 275]
    return dinosaurios_ligeros

def separar_dinosaurios_letra(pila_dinosaurios, letras):
    pila_aparte = []
    while pila_dinosaurios:
        dino = pila_dinosaurios.pop()
        if dino["nombre"][0] in letras:
            pila_aparte.append(dino)
    return pila_aparte


dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    }
]

# a) Contar cuantas especies hay
print("a) Número de especies:", contar_especies(dinosaurios))

# b) Determinar cuantos descubridores distintos hay
print("b) Número de descubridores distintos:", contar_descubridores(dinosaurios))

# c) Mostrar todos los dinosaurios que empiecen con T
print("c) Dinosaurios que empiezan con T:")
dinosaurios_T = mostrar_dinosaurios_T(dinosaurios)
for dino in dinosaurios_T:
    print("-", dino["nombre"])

# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
print("d) Dinosaurios que pesan menos de 275 kg:")
dinosaurios_ligeros = mostrar_dinosaurios_ligeros(dinosaurios)
for dino in dinosaurios_ligeros:
    print("-", dino["nombre"])

# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S
letras = {"A", "Q", "S"}
pila_dinosaurios = dinosaurios[::-1] 
pila_dinosaurios_aparte = separar_dinosaurios_letra(pila_dinosaurios, letras)
print("e) Dinosaurios que comienzan con A, Q, S (en una pila aparte):")
for dino in pila_dinosaurios_aparte:
    print("-", dino["nombre"])
