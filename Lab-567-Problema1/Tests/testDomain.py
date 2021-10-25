from Domain.apartament import creeaza_cheltuiala, get_tip, get_data, get_suma, get_numar, to_string

def test_cheltuiala():
    cheltuiala1 = creeaza_cheltuiala(23, 545.5, '20.10.2021', 'canal')
    assert get_numar(cheltuiala1) == 23
    assert get_suma(cheltuiala1) == 545.5
    assert get_data(cheltuiala1) == '20.10.2021'
    assert get_tip(cheltuiala1) == 'canal'