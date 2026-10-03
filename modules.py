from random import *
import string


def user_id_gen_by_user() -> str:
    id_length = int(input("How long: "))
    id_amount = int(input("How much: "))
    characters = string.ascii_letters
    numbers = string.digits
    random_user = str()
    character_list = characters + numbers
    random_user_list = str()
    for i in range(id_amount):
        random_user = ""
        for index in range(id_length):
            random_user += choice(character_list)
        random_user_list += f"{random_user} \n"
    return random_user_list


def list_of_rgb_colors(amount) -> list:
    list_of_colors = list()
    for i in range(amount):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        rgb = f"rgb ({red}, {green}, {blue})"
        list_of_colors.append(rgb)
    return list_of_colors


def list_of_hexa_colors(amount_of_colors) -> list:
    characters = string.ascii_lowercase
    numbers = string.digits
    hexa_characters = numbers + characters[0: 6]
    hexa = ""
    list_of_colors = list()
    for i in range(amount_of_colors):
        hexa = "#"
        for i in range(6):
            hexa += choice(hexa_characters)
        list_of_colors.append(hexa)
    return list_of_colors


def generate_colors(type, amount) -> list:
    if type == "hexa":
        return list_of_hexa_colors(amount)
    if type == "rgb":
        return list_of_rgb_colors(amount)


def shuffle_list(first_list) -> list:
    old_list = first_list
    new_list = list()
    while (len(old_list) != 0):
        random_item = choice(old_list)
        for item in old_list:
            if item == random_item:
                new_list.append(item)
                old_list.remove(item)
    return new_list


a_list = ["Ethan", "AC", "Haseeb", "Hitesh", "Aidan", "Tej"]
print(shuffle_list(a_list))


def random_numbers() -> list:
    numbers = string.digits
    random_numbers_list = list()
    while len(random_numbers_list) != len(numbers):
        random_number = int(choice(numbers))
        if random_number not in random_numbers_list:
            random_numbers_list.append(int(random_number))
    return random_numbers_list


print(random_numbers())
