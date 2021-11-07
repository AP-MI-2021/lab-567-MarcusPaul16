from Logic.CRUD import stergere_cheltuiala, adaugare_cheltuiala, modificare_cheltuiala
from Logic.functionalitate import stergere_toate_cheltuielile, adunare_valoare, determinare_maxim_cheltuieli, ordonare_dupa_suma, afisare_sume_lunare

def print_menu():
    optiuni = """
    Daca doriti sa adaugati, sa stergeti sau sa modificati o cheltuiala, scrieti 1.
    Daca doriti sa stergeti cheltuielile unui apartament, scrieti 2.
    Daca doriti sa adunati o valoare la toate cheltuielile dintr-o data, scrieti 3.
    Daca doriti sa aflati cea mai mare cheltuiala din fiecare tip pentru o data citita, scrieti 4.
    Daca doriti sa ordonati cheltuielile descrescator dupa suma, scrieti 5.
    Daca doriti sa afisati sumele lunare pentru fiecare apartament, scrieti 6.
    Daca doriti un UNDO, scrieti 7.
    Daca doriti un REDO, scrieti 8.
    Daca doriti sa afisati lista, scrieti 9.
    Daca doriti sa opriti programul, scrieti 10.
    """
    print(optiuni)


def menu(lista):
    i = 0
    undo_list = []
    undo_list.append(lista)
    while True:
        print_menu()
        alegere = input("Optiunea dumneavoastra:")
        if alegere == '1':
            optiune = input(
            """
            Scrieti 1 pentru stergerea unei cheltuieli.
            Scrieti 2 pentru adaugarea unei cheltuieli.
            Scrieti 3 pentru modificarea unei cheltuieli.
            """
                            )
            if optiune == '1':
                numar = input("Scrieti id-ul cheltuielii")
                lista = stergere_cheltuiala(int(numar), lista)
            elif optiune == '2':
                ad = input("Scrieti datele in ordinea: id, numar,suma,data,tip, scrise cu virgula intre ele: ").split(',')
                lista = adaugare_cheltuiala(int(ad[0]),int(ad[1]),int(ad[2]),ad[3],ad[4], lista)
            elif optiune == '3':
                id = int(input("Scrieti id-ul cheltuielii"))
                print("Scrieti valorile datelor pe care le modificati")
                numar = int(input("Scrieti numarul apartamentului"))
                suma = int(input("Scrieti suma"))
                data = input("Scrieti data sub forma DD.MM.YYYY")
                tip = input("Scrieti tipul")
                lista = modificare_cheltuiala(id, numar, suma, data, tip, lista)
            else: print("Comanda inexistenta")
        elif alegere == '2':
            numar = int(input("Scrieti numarul apartamentului"))
            lista = stergere_toate_cheltuielile(numar,lista)
        elif alegere == '3':
            data = input("Scrieti data cheltuielilor la care doriti sa adaugati valoarea")
            valoare = input("Scrieti valoarea")
            lista = adunare_valoare(valoare,data,lista)
        elif alegere == '4':
            print(determinare_maxim_cheltuieli(lista))
        elif alegere == '5':
            lista = ordonare_dupa_suma(lista)
        elif alegere == '6':
            afisare_sume_lunare(lista)
        elif alegere == '7':
            if i - 1 < 0:
                print("Nu mai puteti da UNDO, ati ajuns la inceput.")
            else:
                i = i - 1
                lista = undo_list[i]
        elif alegere == '8':
            if i + 1 >= len(undo_list):
                print("Nu mai puteti da REDO, ati ajuns la cea mai recenta lista")
            else:
                i = i + 1
                lista = undo_list[i]
        elif alegere == '9':
            print(lista)
        elif alegere == '10':
            print("Programul s-a terminat")
            break
        else:
            print("Comanda inexistenta")
        if alegere != '7' and alegere!= '8' and  alegere!='9':
            i = i + 1
            undo_list.append(lista)