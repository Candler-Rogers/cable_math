#implement Drop or maybe Cable class with attributes and methods
#attributes: length, hi freq loss, low freq loss, tx gain, splitters,splitter loss, outlet count
#inherit to RG 6 and Rg 11 classes with unique loss/gain values
#create an instance for each new question
import random
import sys

class Drop():
    def __init__(self, length, splitter):
        #attributes
        self.length = length
        cable_type = cable_type(length)
        #splitter details how many outlets
        self.splitter = splitter
        starting_TX = round(random.uniform(37.9,47.9),1)
        starting_low_RX = round(random.uniform(3.5,12.5),1)
        starting_hi_RX = round(random.uniform(8.9,19.9),1)
        
   def get_GB():
    pass


#sets constant key:values for known dB loss per 100 ft on RG-6 and RG-11
loss_table = {
    "11_hi": 3.98,
    "11_lo": .96,
    "11_tx": .38,
    "6_hi": 6.1,
    "6_lo": 1.6,
    "6_tx": .57
}

def cable_type(length):
    if length > 150:
        return 'RG-11'
    return "RG-6"
    
def get_attenuation(footage, loss_per_100_feet):
    """given a cable length, and a known loss value, returns total loss"""
    return footage/100*loss_per_100_feet

drop_instance = Drop(random.randint(20,250),random.randint(1,4))


def build_drop(drop_instance):
    pass

def math_practice():
    """main loop for the practice half of the program as opposed to future "quiz" loop"""
    while True:
        start = input("\nTo create the drop system enter 'Y'. To Quit enter 'Q': ")
        if start.lower() == "y":
            build_drop()
        if start.lower() == "q":
            sys.exit()
        else:
            print("Invalid input. Try again")
