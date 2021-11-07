from Tests.TestCRUD import *
from Tests.TestFunctionalitati import *


def test_all():
    test_adaugare()
    test_modificare()
    test_stergere()
    test_stergere_cheltuieli()
    test_adunare_valoare()
    test_ordonare_suma()
    test_determinare_maxim_cheltuieli()
    test_sume_lunare()