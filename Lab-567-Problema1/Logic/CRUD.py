from Domain.apartament import creeaza_cheltuiala, to_string

def adaugare_cheltuiala(numar, suma, data, tip, lista):
    '''
    Adauga o noua cheltuiala in lista
    :param numar: numar intreg
    :param suma: float
    :param data: string
    :param tip: string
    :return: returneaza o noua lista in care se afla si noua cheltuiala, pe langa cele existente
    '''
    cheltuiala = creeaza_cheltuiala(numar, suma, data, tip)
    return lista + [cheltuiala]


def stergere_cheltuiala(numar, lista):
    '''
    :param numar: numar apartament
    :param lista: lista cu cheltuielile
    :return: returneaza lista din care s-a sters o cheltuiala
    '''
    return [x for x in lista if get_numar(x) != numar]


def modificare_cheltuiala(numar, suma, data, tip, lista):
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
        cheltuiala_noua = creeaza_cheltuiala(numar, suma, data, tip)
        if to_string(cheltuiala) == to_string(cheltuiala_noua):
            listanoua.append(cheltuiala_noua)
        else:
            listanoua.append(cheltuiala)
    return listanoua






