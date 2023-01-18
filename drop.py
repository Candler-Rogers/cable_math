#implement Drop or maybe Cable class with attributes and methods
#attributes: length, hi freq loss, low freq loss, tx gain, splitters,splitter loss, outlet count
#inherit to RG 6 and Rg 11 classes with unique loss/gain values
#create an instance for each new question

class Drop ):
    def __init__(self, length, cable_type, splitter, outlets):
        #attributes
        self.length = length
        self.cable_type = cable_type
        #splitter expects boolean
        self.splitters = splitter
        self.outlets = outlets
