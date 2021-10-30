from Tests.TestCRUD import *
from Tests.TestFunctionalitati import *


def test_all():
    test_adaugare()
    test_modificare()
    test_stergere()
    test_stergere_cheltuieli()
    test_adunare_valoare()