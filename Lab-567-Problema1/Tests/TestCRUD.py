from Logic.CRUD import *
def test_adaugare():
    lista = []
    assert adaugare_cheltuiala(1,10, 100,'10.10.2020','canal',lista) == [[1, 10, 100, '10.10.2020','canal']]
    assert adaugare_cheltuiala(15, 200, 300,'20.06.2019','intretinere',lista) == [[15, 200, 300, '20.06.2019','intretinere']]
    assert adaugare_cheltuiala(14, 50, 1200, '06.10.2020', 'alte intretineri', lista) == [[14, 50, 1200, '06.10.2020', 'alte intretineri']]


def test_stergere():
    lista = []
    lista = adaugare_cheltuiala(1,10, 100, '10.10.2020', 'canal', lista)
    lista = adaugare_cheltuiala(2,200, 300, '20.06.2019', 'intretinere', lista)
    lista = adaugare_cheltuiala(3,50, 1200, '06.10.2020', 'alte intretineri', lista)
    assert stergere_cheltuiala(1,lista) == [[2,200, 300, '20.06.2019', 'intretinere'],[3,50, 1200, '06.10.2020', 'alte intretineri']]
    assert stergere_cheltuiala(2,lista) == [[1, 10, 100, '10.10.2020', 'canal'], [3, 50, 1200, '06.10.2020', 'alte intretineri']]
    assert stergere_cheltuiala(3,lista) == [[1, 10, 100, '10.10.2020', 'canal'],[2, 200, 300, '20.06.2019', 'intretinere']]


def test_modificare():
    lista = []
    lista = adaugare_cheltuiala(1, 10, 100, '10.10.2020', 'canal', lista)
    lista = adaugare_cheltuiala(2, 200, 300, '20.06.2019', 'intretinere', lista)
    lista = adaugare_cheltuiala(3, 50, 1200, '06.10.2020', 'alte intretineri', lista)
    lista = modificare_cheltuiala(1, 50, 100, '06.10.2020', 'alte intretineri',lista)
    assert lista == [[1, 50, 100, '06.10.2020', 'alte intretineri'], [2, 200, 300, '20.06.2019', 'intretinere'],[3 ,50, 1200, '06.10.2020', 'alte intretineri']]
    lista = modificare_cheltuiala(2, 200, 300, '20.06.2019', 'canal',lista)
    assert lista == [[1, 50, 100, '06.10.2020', 'alte intretineri'],[2, 200, 300, '20.06.2019', 'canal'],[3, 50, 1200, '06.10.2020', 'alte intretineri']]
    lista = modificare_cheltuiala(3, 10, 11100, '10.10.2020', 'canal', lista)
    assert lista == [[1, 50, 100, '06.10.2020', 'alte intretineri'],[2, 200, 300, '20.06.2019', 'canal'],[3, 10, 11100, '10.10.2020', 'canal']]


test_modificare()
test_adaugare()
test_stergere()