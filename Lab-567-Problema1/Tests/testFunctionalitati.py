from Logic.functionalitate import stergere_toate_cheltuielile, adunare_valoare, determinare_maxim_cheltuieli, ordonare_dupa_suma, sume_lunare
from Domain.apartament import creeaza_cheltuiala


def test_stergere_toate_cheltuielile():
    lista = []
    lista.append(creeaza_cheltuiala(20,300,'10.10.2020', 'canal'))
    lista.append(creeaza_cheltuiala(20, 1000,'12.10.2019', 'alte cheltuieli'))
    lista.append(creeaza_cheltuiala(21, 1000, '12.10.2019', 'alte cheltuieli'))
    lista.append(creeaza_cheltuiala(30, 1000, '12.10.2019', 'alte cheltuieli'))
    lista.append(creeaza_cheltuiala(30, 1000, '12.10.2019', 'alte cheltuieli'))
