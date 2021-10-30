from Domain.apartament import creeaza_cheltuiala, to_string, get_numar, get_id


def adaugare_cheltuiala(id, numar, suma, data, tip, lista):
    '''
    Adauga o noua cheltuiala in lista
    :param numar: numar intreg
    :param suma: float
    :param data: string
    :param tip: string
    :return: returneaza o noua lista in care se afla si noua cheltuiala, pe langa cele existente
    '''
    cheltuiala = creeaza_cheltuiala(id, numar, suma, data, tip)
    return lista + [cheltuiala]


def stergere_cheltuiala(id, lista):
    '''
    :param id: numar apartament
    :param lista: lista cu cheltuielile
    :return: returneaza lista din care s-a sters o cheltuiala
    '''
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
    listanoua = []
    for cheltuiala in lista:
        if cheltuiala[0] == id:
            cheltuiala_noua = creeaza_cheltuiala(id, numar, suma, data, tip)
            listanoua.append(cheltuiala_noua)
        else:
            listanoua.append(cheltuiala)
    return listanoua






