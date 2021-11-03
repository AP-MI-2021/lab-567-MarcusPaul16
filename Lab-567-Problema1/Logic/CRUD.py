from Domain.apartament import creeaza_cheltuiala, to_string, get_numar, get_id


def get_by_numar(numar, lista):
    for cheltuiala in lista:
        if cheltuiala[1] == numar:
            return True
    return False


def get_by_id(id, lista):
    for cheltuiala in lista:
        if cheltuiala[0] == id:
            return True
    return False


def adaugare_cheltuiala(id, numar, suma, data, tip, lista):
    '''
    Adauga o noua cheltuiala in lista
    :param numar: numar intreg
    :param suma: float
    :param data: string
    :param tip: string
    :return: returneaza o noua lista in care se afla si noua cheltuiala, pe langa cele existente
    '''
    if int(suma) < 0:
        raise ValueError("Valoarea este negativa")
    elif get_by_id(id,lista) is not False:
        raise ValueError("Id-ul exista deja")
    else:
        cheltuiala = creeaza_cheltuiala(id, numar, suma, data, tip)
        return lista + [cheltuiala]


def stergere_cheltuiala(id, lista):
    '''
    :param id: numar apartament
    :param lista: lista cu cheltuielile
    :return: returneaza lista din care s-a sters o cheltuiala
    '''
    if get_by_id(id, lista) is False:
        raise ValueError("Id-ul nu exista")
    return [x for x in lista if get_id(x) != id]


def modificare_cheltuiala(id, numar, suma, data,tip, lista):
    '''
    modifica o cheltuiala, prin suprascrierea acesteia
    :param numar: numarul apartamentului
    :param suma: suma cheltuielii
    :param data: data efectuarii cheltuielii
    :param tip: tipul cheltuielii
    :param lista: lista cu cheltuieli initiala
    :return: lista in care s-a efectuat modificarea cheltuielii
    '''
    if get_by_id(id, lista) is False:
        raise ValueError("Id-ul nu exista")
    if suma < 0:
        raise ValueError("Suma este negativa")
    if tip != 'canal' and tip !='alte cheltuieli' and tip!=' intretinere':
        raise ValueError("Nu exista acest tip de cheltuiala")
    listanoua = []
    for cheltuiala in lista:
        if cheltuiala[0] == id:
            try:
                cheltuiala_noua = creeaza_cheltuiala(id, numar, suma, data, tip)
            except ValueError as ve:
                print(f"Eroare: {ve}")
                return lista
            listanoua.append(cheltuiala_noua)
        else:
            listanoua.append(cheltuiala)
    return listanoua







