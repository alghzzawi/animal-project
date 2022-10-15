import pytest
from animals_app.animals import Animals
'''
note: don't make more than one mark skip comment
      (just test each def alone )
'''
@pytest.mark.skip("todo")
def test_name_of_animal(one_animal):
    one_animal.set_name('Abyssinian') 
    actual = one_animal.get_full_name()
    expected = 'Abyssinian'
    assert actual == expected

@pytest.mark.skip("todo")
def test_lifespan_animal(one_animal):
    one_animal.set_name('Abyssinian') 
    actual = one_animal.get_lifeSpan()
    expected = '13-15 years'
    assert actual == expected

@pytest.mark.skip("todo")
def test_locations_animal(one_animal):
    one_animal.set_name('Abyssinian') 
    actual = one_animal.get_locations()
    expected = 'Africa'
    assert actual == expected

@pytest.mark.skip("todo")
def test_llength_animal(one_animal):
    one_animal.set_name('Spider Ball Python') 
    actual = one_animal.get_color()
    expected = 'Black'
    assert actual == expected


#=========================
#        fixture
#=========================

@pytest.fixture
def one_animal():
    some_animal=Animals()
    return some_animal


    
     
    