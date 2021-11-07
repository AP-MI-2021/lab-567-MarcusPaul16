from Domain.apartament import get_numar, get_data, get_suma, get_tip
from Logic.CRUD import get_by_numar


def stergere_toate_cheltuielile(numar, lista):
    '''
    sterge toate cheltuielile unui apartament
    :param numar: numarul apartamentului
    :param lista: lista cu dictionare pentru fiecare apartament
    :return: returneaza lista fara chetuielile apartamentului
    '''
    if get_by_numar(numar, lista) is False:
        raise ValueError("Apartamentul cu numarul dat nu exista")
    return [cheltuiala for cheltuiala in lista if get_numar(cheltuiala) != numar]


def adunare_valoare(valoare, data, lista):
    '''
    :param valoare: valoarea pe care o adaugam
    :param data: data cheltuielilor la care adaugam valoarea
    :param lista: lista cu dictionare
    :return: returneaza lista, cu sumele adaugate
    '''
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            cheltuiala[2] += int(valoare)
    return lista


def determinare_maxim_cheltuieli(lista):
    '''
    determinam maximul pentru fiecare tip de cheltuiala
    :param lista: lista cu cheltuieli
    :return: un dictionar, ca si chei, cele 3 tipuri de cheltuieli, respectiv valoarea maxima din fiecare tip
    '''
    dictionar_cheltuieli = {
        'canal' : 0,
        'intretinere': 0,
        'alte cheltuieli' : 0
    }
    for cheltuiala in lista:
        if get_suma(cheltuiala) > dictionar_cheltuieli[get_tip(cheltuiala)]:
            dictionar_cheltuieli[get_tip(cheltuiala)] = get_suma(cheltuiala)
    return dictionar_cheltuieli


def ordonare_dupa_suma(lista):
    '''
    ordoneaza lista dupa suma cheltuielii
    :param lista: lista cu cheltuieli
    :return: lista ordonata
    '''
    lista.sort(key = lambda x: x[2], reverse = True)
    return lista


def sume_lunare(lista, numar_luna):
    '''
    pentru numarul lunii date, realizeaza o lista de liste, de tipul [numar_apartament, suma]
    :param lista:
    :param numar_luna:
    :return:
    '''
    lista_luna = []
    suma = 12000*[0]
    for cheltuiala in lista:
        string_data = cheltuiala[3].split('.')
        if int(string_data[1]) == numar_luna:
            suma[cheltuiala[1]] += cheltuiala[2]
    for i in range(len(suma)):
        if suma[i]!=0:
            lista_luna.append([i,suma[i]])
    return lista_luna


def afisare_sume_lunare(lista):
    '''
    afiseaza sumele lunare ale apartamentelor, pentru fiecare luna
    :param lista: lista cu cheltuieli
    :return: none
    '''
    luni = {
        '1' : 'Ianuarie',
        '2' : 'Februarie',
        '3' : 'Martie',
        '4' : 'Aprilie',
        '5' : 'Mai',
        '6' : 'Iunie',
        '7' : 'Iulie',
        '8' : 'August',
        '9' : 'Septembrie',
        '10' : 'Octombrie',
        '11' : 'Noiembrie',
        '12' : 'Decembrie'
    }
    i = 1
    while i <= 12:
        lista_sume = sume_lunare(lista, i)
        if lista_sume != []:
            print(luni[str(i)] + ': ')
            for j in range(len(lista_sume)):
                print(f"Apartamentul {lista_sume[j][0]} : {lista_sume[j][1]} RON")
        i = i + 1



