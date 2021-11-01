from UI.console import menu
from UI.meniu_nou import meniu_nou
from Tests.TestAll import test_all

lista = []


def main():
    test_all()
    meniu_nou(lista)



if __name__ == '__main__':
    main()