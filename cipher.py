##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################
import random

##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # minimum "printable" character
        self._value_minimum = ' '
        # maximum "printable" character
        self._value_maximum = '~'
        # size of alphabet used
        self._size_alphabet = ord(self._value_maximum) \
                              - ord(self._value_minimum) + 1
        self.homophonic_substitution = {
            'A': ['01', '@4'],
            'B': ['?8', 'b*'],
            'C': ['/c', 'C='],
            'D': ['d)', '#D'],
            'E': ['37', '!7', 'e*', 'D#', 'S@'],
            'F': ['f/', 'F'],
            'G': ['6G', '9g'],
            'H': ['02', 'h#'],
            'I': ['|-', 'i1'],
            'J': ['i)', '77'],
            'K': ['L8'],
            'L': ['10', '&|'],
            'M': ['%#'],
            'N': ['^/', '9*'],
            'O': ['0#', 'o:'],
            'P': ['p[', 'Qz'],
            'Q': ['0+'],
            'R': ['2f', 'y&'],
            'S': ['5a', '$5'],
            'T': ['ah', 'sa'],
            'U': ['Jj', 'ut'],
            'V': ['bo', 'y '],
            'W': ['bi'],
            'X': ['0l'],
            'Y': ['r0'],
            'Z': ['kk'],
            'a': ['&t','p4'],
            'b': ['Ul'],
            'c': ['ku', 'bl'],
            'd': ['h1', 'u2'],
            'e': ['%*', 'cO', 'rt', 'wA', 'ts'],
            'f': ['ON', 'By'],
            'g': ['eM','iN'],
            'h': ['eR'],
            'i': ['JJ', '`#'],
            'j': ['PP'],
            'k': ['Xl'],
            'l': ['xS'],
            'm': ['Oo'],
            'n': ['F0'],
            'o': ['n#', '()'],
            'p': ['ms'],
            'q': ['yH'],
            'r': ['Ur', 'yy'],
            's': ['pK'],
            't': [':0'],
            'u': ['82', '97'],
            'v': ['Ni', 'Ci'],
            'w': ['d1'],
            'x': ['ww'],
            'y': ['Z1'],
            'z': ['s5'],
            '0': ['ou', 'wa'],
            '1': ['L6', 'l1'],
            '2': ['zZ'],
            '3': ['nn'],
            '4': ['AA'],
            '5': ['Ss'],
            '6': ['69'],
            '7': ['99'],
            '8': ['**'],
            '9': ['Ye'],
            ' ': [',,', '--', '__', '~~', '::'],
            '!': ['?!'],
            '"': ['`@'],
            '#': ['&S'],
            '$': [':I'],
            '%': ['TT'],
            '&': ['||'],
            "'": ["QQ"],
            '(': ['[['],
            ')': ['}0'],
            '*': ['+-'],
            '+': ['%L'],
            ',': ['/.', '`1', '`$'],
            '-': ['}{'],
            '.': ['&F', '?1', 'dd'],
            '/': ['|,'],
            ':': [';>'],
            ';': ['0<'],
            '<': ['=='],
            '=': ['><'],
            '>': ['>0'],
            '?': ['Gi'],
            '@': ['At'],
            '[': ['"*'],
            '\\': ['X0'],
            ']': ['b]'],
            '^': ['pb'],
            '_': ['Th'],
            '`': ['`m'],
            '{': ['n/'],
            '|': ['19'],
            '}': ['02'],
            '~': ['Ks']
        }

    def get_author(self):
        return "Vinnicius Castro"

    def get_cipher_name(self):
        return "Homophonic Substitution Cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        s = "practicalcryptography.com," \
            "\"Homophonic Substitution Cipher\', \n   retrieved: " \
            "http://practicalcryptography.com/ciphers/classical-era/homophonic-substitution/"
        return s
        

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # The encrypt pseudocode
        pc = "ciphertext = empty\n"
        "function encrypt(plainText, password)\n" \
             "   for each character in plaintext\n" \
             "      if character in password\n" \
             "          substitutions = password[character] \n" \
             "          substitute = random.choice(substitutions)\n" \
             "          ciphertext += substitute\n" \
             "       else ciphertext += char\n" \
             "   RETURN ciphertext\n\n"

        # The decrypt pseudocode
        pc += "function decrypt(cipherText, password)\n" \
              "   plaintext = empty\n" \
              "   For each character in ciphertext\n" \
              "     found = False\n" \
              "     for letter, substitutes in password.items()\n" \
              "         if character in substitutes\n" \
              "            plaintext += letter\n" \
              "            found = True\n" \
              "   RETURN plainText\n\n"

        return pc

    ##########################################################################
    # ENCRYPT
    # Shift each character in the plaintext by a random set of 2 other characters
    ##########################################################################
    
    def encrypt(self, plaintext, password):
        ciphertext = ''
        random.seed(password)
        for characters in plaintext:
            if characters in self.homophonic_substitution:
                substitution = random.choice(self.homophonic_substitution[characters])
                ciphertext += substitution
            else:
                ciphertext += characters
        
        return ciphertext

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        plaintext = ''
        random.seed(password)
        i = 0
        while i < len(ciphertext):
            pair = ciphertext[i:i+2]
            found = False
            for plaintext_char, substitutions in self.homophonic_substitution.items():
                if pair in substitutions:
                    plaintext += plaintext_char
                    found = True
                    break 
            if not found:
                plaintext += pair
            i += 2
        return plaintext
    