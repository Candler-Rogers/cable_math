#implement Drop or maybe Cable class with attributes and methods
#attributes: length, hi freq loss, low freq loss, tx gain, splitters,splitter loss, outlet count
#inherit to RG 6 and Rg 11 classes with unique loss/gain values
#create an instance for each new question
import random
import sys

class Drop():
    def __init__(self, length):
        #attributes
        self.length = length
        cable_type__is_6 = cable_type(length)
        #splitter details how many outlets
        splitter = get_splitter()
        starting_TX = round(random.uniform(37.9,47.9),1)
        starting_low_RX = round(random.uniform(3.5,12.5),1)
        starting_hi_RX = round(random.uniform(8.9,19.9),1)
        gb_TX, gb_low_RX, gb_hi_RX = get_GB(length, cable_type_is_6, starting_TX, starting_low_RX, starting_hi_RX)
        
        
   def get_GB(length, RG_6,tap_TX, tap_lo_RX, tap_hi_RX):
    if RG_6:
        return tap_Tx+get_attenuation(length, loss_table{"6_tx"}), tap_lo_RX-get_attenuation(length, loss_table{"6_lo"}), tap_hi_RX-get_attenuation(length, loss_table{"6_hi"})
    else
        return tap_Tx+get_attenuation(length, loss_table{"11_tx"}), tap_lo_RX-get_attenuation(length, loss_table{"11_lo"}), tap_hi_RX-get_attenuation(length, loss_table{"11_hi"})

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
        return False
    return True
    
def get_attenuation(footage, loss_per_100_feet):
    """given a cable length, and a known loss value, returns total loss"""
    return footage/100*loss_per_100_feet

def build_drop():
    """creates an instance of the Drop class"""
    drop_instance = Drop(random.randint(20,250))
    drop_instance.splitters = get_splitter()
    return drop_instance

def get_splitter():
    """this asks the user to select a splitter legs they want and returns it to the build drop function for addition into the instance attributes"""
    return int(input"\n Enter the number of outlets between 1 and 4 you would like to create (more than 1 outlet will include splitters): "))

def math_practice():
    """main loop for the practice half of the program as opposed to future "quiz" loop"""
    while True:
        start = input("\nTo create the drop system enter 'Y'. To Quit enter 'Q': ")
        if start.lower() == "y":
            practice_drop = build_drop()
            #display the beginning values of the drop
            #ask user to continue when they have attempted to compute the GB levels
            #?possible add in a Reminder option 'R' that displays the loss formulas.
        if start.lower() == "q":
            sys.exit()
        else:
            print("Invalid input. Try again")
