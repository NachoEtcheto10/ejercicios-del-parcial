
def listando_a_la_inversa(lista):
    if not lista:  
        return []
    else:
        return listando_a_la_inversa(lista[1:]) + [lista[0]]

mi_lista_para_el_parcial = [40, 90, 200, 999, ]
print("Lista inicial:", mi_lista_para_el_parcial)
print("Lista en orden inverso:", listando_a_la_inversa(mi_lista_para_el_parcial))