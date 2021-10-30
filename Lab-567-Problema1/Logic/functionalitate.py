from Domain.apartament import get_numar, get_data, get_suma, get_tip


def stergere_toate_cheltuielile(numar, lista):
    '''
    sterge toate cheltuielile unui apartament
    :param numar: numarul apartamentului
    :param lista: lista cu dictionare pentru fiecare apartament
    :return: returneaza lista fara chetuielile apartamentului
    '''
    return [cheltuiala for cheltuiala in lista if get_numar(cheltuiala) != numar]


def adunare_valoare(valoare, data,lista):
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
    for i in range(len(lista)-1):
        for j in range(i,len(lista)):
            if lista[i]['suma'] < lista[j]['suma']:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


def sume_lunare(lista, numar_luna):
    lista_luna = []
    suma = 10000*[0]
    for cheltuiala in lista:
        string_data = cheltuiala['data'].split('.')
        if int(string_data[1]) == numar_luna:
            suma[cheltuiala['numar']] += cheltuiala['suma']
    for i in range(len(suma)):
        if suma[i]!=0:
            lista_luna.append([i,suma[i]])
    return lista_luna


def afisare_sume_lunare(lista):
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




