def main():
    plate = input("please insert your req- ")

    print(testing(plate))


def testing(plate):
    # check if plate is between 2 -6
    if 2 <= len(plate) <= 6:
        # check if the first two characters are letters
        if plate[:2].isalpha():
            # check if the  last character is a number
            if plate[-1].isdigit():
                # check if the first number is not 0
                if plate[0] != "0":
                    # check if there are no (periods ,spaces , punctuation marks)
                    if plate.isalnum():
                        return "valid"

    return "invalid"

    #     return "Invalid"
    # elif plate[0].isdigit() or plate[1].isdigit():
    #     return "valid"
    # elif not plate[:2].isalpha():
    #     return "Invalid"

    # first_plate = [num for num in plate if plate.isdigit()][0]
    # first_plate = plate.index(first_plate)
    # plate_list = plate[first_plate]

    # if plate_list.isdigit():
    #     return "valid"
    # else:
    #     return "Invalid"


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(license_plate: str) -> bool:
    return all(
        [
            license_plate[:2].isalpha(),
            2 <= len(license_plate) <= 6,
            has_number(license_plate),
            license_plate.isalnum(),
        ]
    )
    # if 2 <= len(license_plate) <= 6:

    #     has_number(license_plate)

    #     return True

    # return False


# def has_number(license_plate: str):
#     for i, character in enumerate(license_plate):
#         if character.isdigit() and character != "0":
#             for inner_character in license_plate[i + 1 :]:
#                 if not inner_character.isdigit():
#                     return False

#     return True

# return any(char.isdigit()for char in s)


def has_number(license_plate: str):
    has_seen_number_before = False
    for character in license_plate:
        if has_seen_number_before and not character.isdigit():
            return False
        if not has_seen_number_before and character.isdigit():
            if character == "0":
                return False
            has_seen_number_before = True

    return True


if __name__ == "__main__":
    assert not is_valid("55cs50")
    assert  is_valid("ch50")
    assert is_valid("cs555")
    assert not is_valid("cs055")
    assert not is_valid("cs 5")
