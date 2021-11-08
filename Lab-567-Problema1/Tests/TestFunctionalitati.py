from UI.meniu_nou import meniu_nou

from Logic.functionalitate import *
from Logic.CRUD import *


def test_stergere_cheltuieli():
    lista = []
    lista = adaugare_cheltuiala(1, 16, 100, '10.10.2020', 'canal', lista)
    lista = adaugare_cheltuiala(2, 20, 200, '16.12.2020', 'alte cheltuieli', lista)
    lista = adaugare_cheltuiala(3, 16, 1000, '10.10.2020', 'intretinere', lista)
    lista = adaugare_cheltuiala(4, 20, 1000, '10.10.2020', 'intretinere', lista)
    lista = stergere_toate_cheltuielile(16, lista)
    assert lista == [[2, 20, 200, '16.12.2020', 'alte cheltuieli'], [4, 20, 1000, '10.10.2020', 'intretinere']]
    lista = stergere_toate_cheltuielile(20, lista)
    assert lista == []


def test_adunare_valoare():
    lista = []
    lista = adaugare_cheltuiala(1, 16, 100, '10.10.2020', 'canal', lista)
    lista = adaugare_cheltuiala(2, 20, 200, '16.12.2020', 'alte cheltuieli', lista)
    lista = adaugare_cheltuiala(3, 16, 1000, '10.10.2020', 'intretinere', lista)
    lista = adaugare_cheltuiala(4, 20, 1000, '10.10.2020', 'intretinere', lista)
    lista = adunare_valoare(1000, '10.10.2020', lista)
    assert lista == [[1, 16, 1100, '10.10.2020', 'canal'], [2, 20, 200, '16.12.2020', 'alte cheltuieli'],
                     [3, 16, 2000, '10.10.2020', 'intretinere'], [4, 20, 2000, '10.10.2020', 'intretinere']]
    lista = adunare_valoare(5000, '16.12.2020', lista)
    assert lista == [[1, 16, 1100, '10.10.2020', 'canal'], [2, 20, 5200, '16.12.2020', 'alte cheltuieli'],
                     [3, 16, 2000, '10.10.2020', 'intretinere'], [4, 20, 2000, '10.10.2020', 'intretinere']]


def test_ordonare_suma():
    lista = [
        [1, 10, 2000, '10.10.2020', 'canal'],
        [2, 30, 5000, '10.10.2020', 'canal'],
        [3, 20, 500, '10.10.2020', 'intretinere'],
        [4, 16, 10000, '10.10.2020', 'alte cheltuieli']
    ]
    ordonare_dupa_suma(lista)
    assert lista == [
        [4, 16, 10000, '10.10.2020', 'alte cheltuieli'],
        [2, 30, 5000, '10.10.2020', 'canal'],
        [1, 10, 2000, '10.10.2020', 'canal'],
        [3, 20, 500, '10.10.2020', 'intretinere']
    ]

    lista = modificare_cheltuiala(3, 20, 100000, '16.05.2013', 'intretinere', lista)
    ordonare_dupa_suma(lista)

    assert lista == [
        [3, 20, 100000, '16.05.2013', 'intretinere'],
        [4, 16, 10000, '10.10.2020', 'alte cheltuieli'],
        [2, 30, 5000, '10.10.2020', 'canal'],
        [1, 10, 2000, '10.10.2020', 'canal']
    ]


def test_determinare_maxim_cheltuieli():
    lista = [
        [1, 10, 2000, '10.10.2020', 'canal'],
        [2, 30, 5000, '10.10.2020', 'canal'],
        [3, 20, 500, '10.10.2020', 'intretinere'],
        [4, 16, 10000, '10.10.2020', 'alte cheltuieli'],
        [5, 13, 50, '10.10.2020', 'alte cheltuieli'],
        [6, 6, 2200, '10.10.2020', 'intretinere']
    ]
    maxim_cheltuieli = determinare_maxim_cheltuieli(lista)
    assert maxim_cheltuieli == {
        'canal': 5000,
        'intretinere': 2200,
        'alte cheltuieli': 10000
    }

    lista = modificare_cheltuiala(2, 30, 50, '10.10.2020', 'canal', lista)
    maxim_cheltuieli = determinare_maxim_cheltuieli(lista)
    assert maxim_cheltuieli == {
        'canal': 2000,
        'intretinere': 2200,
        'alte cheltuieli': 10000
    }


def test_sume_lunare():
    lista = [
        [1, 10, 2000, '10.10.2020', 'canal'],
        [2, 30, 5000, '10.10.2020', 'canal'],
        [3, 20, 500, '05.06.2020', 'intretinere'],
        [4, 16, 10000, '20.10.2020', 'alte cheltuieli'],
        [5, 13, 50, '10.10.2020', 'alte cheltuieli'],
        [6, 6, 2200, '20.09.2020', 'intretinere'],
        [7, 13, 560, '12.09.2020', 'intretinere']
    ]

    lista1 = sume_lunare(lista, 10)
    assert lista1 == [
        [10, 2000],
        [13, 50],
        [16, 10000],
        [30, 5000]
    ]

    lista1 = sume_lunare(lista, 6)
    assert lista1 == [
        [20, 500]
    ]

    lista1 = sume_lunare(lista, 9)
    assert lista1 == [[6, 2200], [13, 560]]


def test_undo_redo_scenariu():
    scenariu = """
    add,1,10,200,'10.10.2021','canal';add,2,15,500,16.08.2021,alte cheltuieli;add,3,12,250,'05.11.2021,intretinere;undo;undo;undo;undo;add,1,10,200,10.10.2021,canal;add,2,15,500,16.08.2021,alte cheltuieli;add,3,12,250,05.11.2021,intretinere;redo;undo;undo;redo;redo;undo;undo;redo;redo;undo;undo;add,4,20,1000,07.11.2021,canal;redo;undo;undo;redo;redo;redo;
    """
    undolist = [[]]
    redolist = []
    lista = []
    for j in range(len(scenariu.split(";"))):
        comanda = scenariu.split(";")[j]
        det = comanda.split(",")
        if 'add' in det[0]:
            redolist.clear()
            undolist.append(lista)
            lista = adaugare_cheltuiala(int(det[1]), int(det[2]), int(det[3]), det[4], det[5], lista)
        elif 'undo' in det[0]:
            if len(undolist) > 0:
                lista, undolist, redolist = undo(lista, undolist, redolist)
        elif 'redo' in det[0]:
            if len(redolist) > 0:
                lista, undolist, redolist = redo(lista, undolist, redolist)
    assert lista == [[1, 10, 200, '10.10.2021', 'canal'], [4, 20, 1000, '07.11.2021', 'canal']]
