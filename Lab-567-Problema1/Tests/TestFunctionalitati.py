from Logic.functionalitate import *
from Logic.CRUD import *

def test_stergere_cheltuieli():
    lista = []
    lista = adaugare_cheltuiala(1, 16, 100, '10.10.2020', 'canal', lista)
    lista = adaugare_cheltuiala(2, 20, 200, '16.12.2020', 'alte cheltuieli', lista)
    lista = adaugare_cheltuiala(3, 16, 1000, '10.10.2020', 'intretinere', lista)
    lista = adaugare_cheltuiala(4, 20, 1000, '10.10.2020', 'intretinere', lista)
    lista = stergere_toate_cheltuielile(16, lista)
    assert lista == [[2, 20, 200, '16.12.2020', 'alte cheltuieli'],[4, 20, 1000, '10.10.2020', 'intretinere']]
    lista = stergere_toate_cheltuielile(20, lista)
    assert lista == []


def test_adunare_valoare():
    lista = []
    lista = adaugare_cheltuiala(1, 16, 100, '10.10.2020', 'canal', lista)
    lista = adaugare_cheltuiala(2, 20, 200, '16.12.2020', 'alte cheltuieli', lista)
    lista = adaugare_cheltuiala(3, 16, 1000, '10.10.2020', 'intretinere', lista)
    lista = adaugare_cheltuiala(4, 20, 1000, '10.10.2020', 'intretinere', lista)
    lista = adunare_valoare(1000, '10.10.2020', lista)
    assert lista == [[1, 16, 1100, '10.10.2020', 'canal'],[2, 20, 200, '16.12.2020', 'alte cheltuieli'],[3, 16, 2000, '10.10.2020', 'intretinere'],[4, 20, 2000, '10.10.2020', 'intretinere']]
    lista = adunare_valoare(5000, '16.12.2020', lista)
    assert lista == [[1, 16, 1100, '10.10.2020', 'canal'],[2, 20, 5200, '16.12.2020', 'alte cheltuieli'],[3, 16, 2000, '10.10.2020', 'intretinere'],[4, 20, 2000, '10.10.2020', 'intretinere']]


