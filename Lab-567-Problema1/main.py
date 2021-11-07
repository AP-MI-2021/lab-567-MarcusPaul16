from UI.console import menu
from UI.meniu_nou import meniu_nou
from Tests.TestAll import test_all

lista = [
    [1, 10, 2000, '10.10.2020', 'canal'],
    [2, 30, 5000, '10.10.2020', 'canal'],
    [3, 20, 500, '10.10.2020', 'intretinere'],
    [4, 16, 10000, '10.10.2020', 'alte cheltuieli']
]


def main():
    test_all()
    menu(lista)



if __name__ == '__main__':
    main()