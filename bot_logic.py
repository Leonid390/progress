import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return " орёл! Удача не на твоей стороне!"
    else:
        return " решка! Удача не на твоей стороне!"
def gen_emodji():
    emodji = [":flag_ru:", ":nerd:"]
    return random.choice(emodji)