class MorseNode():
    def __init__(self, value):
        self.dot = None
        self.dash = None
        self.value = value

class MorseTree():
    def __init__(self):
        self.root = MorseNode("root")
        self.root.dot = MorseNode("E")
        self.root.dot.dot = MorseNode("I")
        self.root.dot.dot.dot = MorseNode("S")
        self.root.dot.dot.dot.dot = MorseNode("H")
        self.root.dot.dot.dot.dash = MorseNode("V")
        self.root.dot.dot.dash = MorseNode("U")
        self.root.dot.dot.dash.dot = MorseNode("F")
        self.root.dot.dash = MorseNode("A")
        self.root.dot.dash.dot = MorseNode("R")
        self.root.dot.dash.dot.dot = MorseNode("L")
        self.root.dot.dash.dash = MorseNode("W")
        self.root.dot.dash.dash.dot = MorseNode("P")
        self.root.dot.dash.dash.dash = MorseNode("J")
        self.root.dash = MorseNode("T")
        self.root.dash.dot = MorseNode("N")
        self.root.dash.dot.dot = MorseNode("D")
        self.root.dash.dot.dot.dot = MorseNode("B")
        self.root.dash.dot.dot.dash = MorseNode("X")
        self.root.dash.dot.dash = MorseNode("K")
        self.root.dash.dot.dash.dot = MorseNode("C")
        self.root.dash.dot.dash.dash = MorseNode("Y")
        self.root.dash.dash = MorseNode("M")
        self.root.dash.dash.dot = MorseNode("G")
        self.root.dash.dash.dot.dot = MorseNode("Z")
        self.root.dash.dash.dot.dash = MorseNode("Q")
        self.root.dash.dash.dash = MorseNode("O")

    def str_to_sub_obj(self, obj, character):
        return obj.dash if character == "-" else obj.dot

    def user_input_morse_decoder(self):
        user_input: str = input("Put in the morse code as . and - : ")
        morse_letters: [] = user_input.split(" ")
        output = ""
        for letter in morse_letters:
            minioutput = self.root
            for morsebin in letter:
                minioutput = self.str_to_sub_obj(minioutput, morsebin)
            output += minioutput.value
        return output



morsetree = MorseTree()


while True:
    print(morsetree.user_input_morse_decoder())
