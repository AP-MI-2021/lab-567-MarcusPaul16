from Logic.CRUD import adaugare_cheltuiala, creeaza_cheltuiala, stergere_cheltuiala

show_menu = """
Puteti da mai multe comenzi simultan, pe care le puteti separa prin ';',inclusiv la final, fiecare functia avand structura
Adaugare: add,id, numarul apartamentului, suma, data, tipul cheltuielii
Stergere: delete,id-ul cheltuielii
Afisare Lista: showall
Stop: stop
"""
def meniu_nou(lista):
    while True:
        print(show_menu)
        stop = False
        comanda = input("Scrieti comenzile, despartite de ';'").split(';')
        for i in range(len(comanda)):
            det = comanda[i].split(',')
            if det[0] == 'add':
                try:
                    lista = adaugare_cheltuiala(det[1],det[2],det[3],det[4],det[5],lista)
                except IndexError as ie:
                    print(f"Eroare: {ie}")
            elif det[0] == 'delete':
                    lista = stergere_cheltuiala(det[1],lista)
            elif det[0] == 'showall':
                print(lista)
            elif det[0] == 'stop':
                stop = True
                break
        if stop is True:
            print("Programul s-a oprit")
            break