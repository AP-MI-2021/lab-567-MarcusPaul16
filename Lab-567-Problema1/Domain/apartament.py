def creeaza_cheltuiala(numar, suma, data, tip):
    '''
    Creeaza o cheltuiala
    :param numar: nr intreg
    :param suma: float
    :param data: string
    :param tip: string
    :return: returneaza un dictionar cu atributele date
    '''
    return [numar,suma,data,tip]


def get_numar(apartament):
    '''
    returneaza numarul unui apartament
    :param apartament: dictionar ce contine o cheltuiala
    :return: numarul apartamentului
    '''
    return apartament[0]


def get_suma(apartament):
    '''
    returneaza suma cheltuielii
    :param apartament: dictionar ce contine o cheltuiala
    :return: suma cheltuielii
    '''
    return apartament[1]


def get_data(apartament):
    '''
    returneaza data cheltuielii
    :param apartament: dictionar ce contine o cheltuiala
    :return: data in care s-a efectuat cheltuiala
    '''
    return apartament[2]


def get_tip(apartament):
    '''
    returneaza tip-ul cheltuielii
    :param apartament: dictionar ce contine o cheltuiala
    :return: tip-ul cheltuielii
    '''
    return apartament[3]


def to_string(apartament):
    return "Numar: {}, suma: {}, data: {}, tip:{} ".format(
        get_numar(apartament), get_suma(apartament), get_data(apartament), get_tip(apartament)
    )




