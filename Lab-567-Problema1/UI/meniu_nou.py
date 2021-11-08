from Logic.CRUD import adaugare_cheltuiala, creeaza_cheltuiala, stergere_cheltuiala
from Logic.functionalitate import *


show_menu = """
Puteti da mai multe comenzi simultan, pe care le puteti separa prin ';',inclusiv la final, fiecare functia avand structura
Adaugare: add,id, numarul apartamentului, suma, data, tipul cheltuielii
Stergere: delete,id-ul cheltuielii
Afisare Lista: showall
Stergerea unor cheltuieli pentru un apartament: delete_cheltuiala, numar_apartament
Adunarea unei valori la toate cheltuielile dintr-o data citita: adunare, valoare, data
Determinarea celei mai mari cheltuieli din fiecare tip: maxim
Ordonarea cheltuielilor descrescator dupa suma: sort
Afisarea sumelor lunare pentru fiecare apartament: sume_lunare
Undo: undo
Redo: redo
Stop: stop
"""


def meniu_nou(lista):
    undolist= []
    redolist= []
    while True:
        print(show_menu)
        stop = False
        comanda = input("Scrieti comenzile, despartite de ';'").split(';')
        for i in range(len(comanda)):
            det = comanda[i].split(',')
            if det[0] == 'add':
                try:
                    redolist.clear()
                    undolist.append(lista)
                    lista = adaugare_cheltuiala(int(det[1]), int(det[2]), int(det[3]), det[4],det[5], lista)
                except IndexError as ie:
                    print(f"Eroare: {ie}")
            elif det[0] == 'delete':
                undolist.append(lista)
                redolist.clear()
                lista = stergere_cheltuiala(det[1],lista)
            elif det[0] == 'showall':
                print(lista)
            elif det[0] == 'stop':
                stop = True
                break
            elif det[0] == 'delete_cheltuiala':
                undolist.append(lista)
                redolist.clear()
                lista = stergere_toate_cheltuielile(int(det[1]), lista)
            elif det[0] == 'adunare':
                undolist.append(lista)
                redolist.clear()
                lista = adunare_valoare(det[1], det[2], lista)
            elif det[0] == 'maxim':
                print(determinare_maxim_cheltuieli(lista))
            elif det[0] == 'sort':
                undolist.append(lista)
                redolist.clear()
                lista = ordonare_dupa_suma(lista[:])
            elif det[0] == 'sume_lunare':
                afisare_sume_lunare(lista)
            elif det[0] == 'undo':
                if len(undolist) > 0:
                    lista, undolist, redolist = undo(lista, undolist, redolist)
            elif det[0] == 'redo':
                if len(redolist) > 0:
                    lista, undolist, redolist = redo(lista, undolist, redolist)
            else: print("comanda inexistenta")
        if stop is True:
            print("Programul s-a oprit")
            break