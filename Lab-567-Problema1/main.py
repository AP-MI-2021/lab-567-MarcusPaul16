from UI.console import menu
from Tests.TestAll import test_all

lista = []


def main():
    test_all()
    menu(lista)


if __name__ == '__main__':
    main()