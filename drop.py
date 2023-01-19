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
    if length

drop_instance = Drop(random.randint(20,250),random.randint(1,4))


def build_drop(drop_instance):
    
