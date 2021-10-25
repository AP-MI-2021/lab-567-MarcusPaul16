from Logic.CRUD import *
def test_adaugare():
    lista = []
    assert adaugare_cheltuiala(10, 100,'10.10.2020','canal',lista) == [[10, 100,'10.10.2020','canal']]
    assert adaugare_cheltuiala(200, 300,'20.06.2019','intretinere',lista) == [[200, 300,'20.06.2019','intretinere']]
    assert adaugare_cheltuiala(50, 1200, '06.10.2020', 'alte intretineri', lista) == [[50, 1200, '06.10.2020', 'alte intretineri']]


def test_stergere():
    lista = []
    lista = adaugare_cheltuiala(10, 100, '10.10.2020', 'canal', lista)
    lista = adaugare_cheltuiala(200, 300, '20.06.2019', 'intretinere', lista)
    lista = adaugare_cheltuiala(50, 1200, '06.10.2020', 'alte intretineri', lista)
    assert stergere_cheltuiala(10,lista) == [[200, 300, '20.06.2019', 'intretinere'],[50, 1200, '06.10.2020', 'alte intretineri']]
    assert stergere_cheltuiala(200,lista) == [[10, 100, '10.10.2020', 'canal'], [50, 1200, '06.10.2020', 'alte intretineri']]
    assert stergere_cheltuiala(50,lista) == [[10, 100, '10.10.2020', 'canal'],[200, 300, '20.06.2019', 'intretinere']]


def test_modificare():
    lista = []
    lista = adaugare_cheltuiala(10, 100, '10.10.2020', 'canal', lista)
    lista = adaugare_cheltuiala(200, 300, '20.06.2019', 'intretinere', lista)
    lista = adaugare_cheltuiala(50, 1200, '06.10.2020', 'alte intretineri', lista)
    lista = modificare_cheltuiala(50, 100, '06.10.2020', 'alte intretineri',lista)
    assert lista == [[10, 100, '10.10.2020', 'canal'], [200, 300, '20.06.2019', 'intretinere'],[50, 100, '06.10.2020', 'alte intretineri']]
    lista = modificare_cheltuiala(200, 300, '20.06.2019', 'canal',lista)
    assert lista == [[10, 100, '10.10.2020', 'canal'],[200, 300, '20.06.2019', 'canal'],[50, 100, '06.10.2020', 'alte intretineri']]
    lista = modificare_cheltuiala(10, 11100, '10.10.2020', 'canal', lista)
    assert lista == [[10, 11100, '10.10.2020', 'canal'], [200, 300, '20.06.2019', 'canal'], [50, 100, '06.10.2020', 'alte intretineri']]

test_modificare()
test_stergere()
test_adaugare()