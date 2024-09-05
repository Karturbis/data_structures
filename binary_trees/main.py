class MorseNode():
    def __init__(self, value):
        self.dot = None
        self.dash = None
        self.value = value

root = MorseNode("")
root.dot = MorseNode("E")
root.dot.dot = MorseNode("I")
root.dot.dot.dot = MorseNode("S")
root.dot.dot.dot.dot = MorseNode("H")
root.dot.dot.dot.dash = MorseNode("V")
root.dot.dot.dash = MorseNode("U")
root.dot.dot.dash.dot = MorseNode("F")
root.dot.dash = MorseNode("A")
root.dot.dash.dot = MorseNode("R")
root.dot.dash.dot.dot = MorseNode("L")
root.dot.dash.dash = MorseNode("W")
root.dot.dash.dash.dot = MorseNode("P")
root.dot.dash.dash.dash = MorseNode("J")
root.dash = MorseNode("T")
root.dash.dot = MorseNode("N")
root.dash.dot.dot = MorseNode("D")
root.dash.dot.dot.dot = MorseNode("B")
root.dash.dot.dot.dash = MorseNode("X")
root.dash.dot.dash = MorseNode("K")
root.dash.dot.dash.dot = MorseNode("C")
root.dash.dot.dash.dash = MorseNode("Y")
root.dash.dash = MorseNode("M")
root.dash.dash.dot = MorseNode("G")
root.dash.dash.dot.dot = MorseNode("Z")
root.dash.dash.dot.dash = MorseNode("Q")
root.dash.dash.dash = MorseNode("O")

while True:
    user_input: str = input("Put in the morse code as . and - : ")
    morse_letters: [] = user_input.split(" ")

    def str_to_sub_obj(obj, character):
        return obj.dash if character == "-" else obj.dot


    output = ""
    for letter in morse_letters:
        minioutput = root
        for morsebin in letter:
            minioutput = str_to_sub_obj(minioutput, morsebin)
        output += minioutput.value

    print(output)
