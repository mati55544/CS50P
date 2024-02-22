from twttr import returns_str


def main():
    test_upper_lower_cases()
    test_numbers()
    test_punctuation()


#tets letters upper and lower cases
def test_upper_lower_cases():

    assert returns_str('Aref') == 'rf'
    assert returns_str('EEko') == 'k'
    assert returns_str('aEiOu') == ''

#test numbers     
def test_numbers():
    assert returns_str('5544') == '5544'
    assert returns_str('668877') == '668877'


#test punctuation
def test_punctuation():
    assert returns_str('!!@@') == '!!@@'
    assert returns_str('$$##') == '$$##'


if __name__ == "__main__":
    main()
