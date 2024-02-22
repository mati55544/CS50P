from bank import split 

# def main():
#     test_upper_lower_cases()
#     test_numbers()
#     test_punctuation()



def test_upper_lower_cases():
    assert split('HELLo') == '$0'
    assert split('Hhh') == '$20'
    assert split('GGhello') == '$100'


def test_numbers():
    assert split('8877') == '$100'
    assert split('h9') == '$20'
    assert split ('hello545') == '$0'


def test_punctuation():
    assert split('h!!') == '$20'
    assert split('hello$$') == '$20' 


