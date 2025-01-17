#new font file including the following punctuation
#. , ! ? " ' [ ] ( ) { } ; : - _ + = * / \ | < >
'''
Left arrow: U+2190 (←)  	enter as \u2190
Right arrow: U+2192 (→)		enter as \u2192
Up arrow: U+2191 (↑)  		enter as \u2191
Down arrow: U+2193 (↓)		enter as \u2193
Check mark: U+2713 			enter as \u2713

Two methods to enter my glyphs
render_text_on_row("custom_char1", (255, 0, 255), 0)  # Purple
    bigfont = {
    "custom_char1": [
        0b00111000,
        0b01000100,
        0b10000010,
        0b10000010,
        0b10000010,
        0b01000100,
        0b00111000,
        0b00000000,
    ],
}
or
render_text_on_row("\g1", (255, 127, 0), 1)  # Orange
    bigfont = {
    "\g1": [
        0b00111000,
        0b01000100,
        0b10000010,
        0b10000010,
        0b10000010,
        0b01000100,
        0b00111000,
        0b00000000,
    ],
}



'''


bigfont = {
    # Digits
    "0": [
        0b01111100,
        0b11000110,
        0b11001110,
        0b11011110,
        0b11110110,
        0b11100110,
        0b01111100,
        0b00000000,
    ],
    "1": [
        0b00110000,
        0b01110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b11111100,
        0b00000000,
    ],
    "2": [
        0b01111000,
        0b11001100,
        0b00001100,
        0b00111000,
        0b01100000,
        0b11001100,
        0b11111100,
        0b00000000,
    ],
    "3": [
        0b01111000,
        0b11001100,
        0b00001100,
        0b00111000,
        0b00001100,
        0b11001100,
        0b01111000,
        0b00000000,
    ],
    "4": [
        0b00011100,
        0b00111100,
        0b01101100,
        0b11001100,
        0b11111110,
        0b00001100,
        0b00011110,
        0b00000000,
    ],
    "5": [
        0b11111100,
        0b11000000,
        0b11111000,
        0b00001100,
        0b00001100,
        0b11001100,
        0b01111000,
        0b00000000,
    ],
    "6": [
        0b00111000,
        0b01100000,
        0b11000000,
        0b11111000,
        0b11001100,
        0b11001100,
        0b01111000,
        0b00000000,
    ],
    "7": [
        0b11111100,
        0b11001100,
        0b00001100,
        0b00011000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b00000000,
    ],
    "8": [
        0b01111000,
        0b11001100,
        0b11001100,
        0b01111000,
        0b11001100,
        0b11001100,
        0b01111000,
        0b00000000,
    ],
    "9": [
        0b01111000,
        0b11001100,
        0b11001100,
        0b01111100,
        0b00001100,
        0b00011000,
        0b01110000,
        0b00000000,
    ],

    # Uppercase Letters (A-Z)
    "A": [
        0b00110000,
        0b01111000,
        0b11001100,
        0b11001100,
        0b11111100,
        0b11001100,
        0b11001100,
        0b00000000,
    ],
    
    "\As": [
        0b00000000,
        0b00111110,
        0b01111110,
        0b11001000,
        0b11001000,
        0b01111110,
        0b00111110,
        0b00000000,
        ],    
    
     
    
    
    "B": [
        0b11111100,
        0b01100110,
        0b01100110,
        0b01111100,
        0b01100110,
        0b01100110,
        0b11111100,
        0b00000000,
    ],
    "C": [
        0b00111100,
        0b01100110,
        0b11000000,
        0b11000000,
        0b11000000,
        0b01100110,
        0b00111100,
        0b00000000,
    ],
    "D": [
        0b11111000,
        0b01101100,
        0b01100110,
        0b01100110,
        0b01100110,
        0b01101100,
        0b11111000,
        0b00000000,
    ],
    "E": [
        0b11111110,
        0b01100010,
        0b01101000,
        0b01111000,
        0b01101000,
        0b01100010,
        0b11111110,
        0b00000000,
    ],
    "F": [
        0b11111110,
        0b01100010,
        0b01101000,
        0b01111000,
        0b01101000,
        0b01100000,
        0b11110000,
        0b00000000,
    ],
    "G": [
        0b00111100,
        0b01100110,
        0b11000000,
        0b11000000,
        0b11001110,
        0b01100110,
        0b00111110,
        0b00000000,
    ],
    "H": [
        0b11001100,
        0b11001100,
        0b11001100,
        0b11111100,
        0b11001100,
        0b11001100,
        0b11001100,
        0b00000000,
    ],
    "I": [
        0b01111000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b01111000,
        0b00000000,
    ],
    "J": [
        0b00011110,
        0b00001100,
        0b00001100,
        0b00001100,
        0b11001100,
        0b11001100,
        0b01111000,
        0b00000000,
    ],
    "K": [
        0b11100110,
        0b01100110,
        0b01101100,
        0b01111000,
        0b01101100,
        0b01100110,
        0b11100110,
        0b00000000,
    ],
    "L": [
        0b11110000,
        0b01100000,
        0b01100000,
        0b01100000,
        0b01100010,
        0b01100110,
        0b11111110,
        0b00000000,
    ],
    "M": [
        0b11000110,
        0b11101110,
        0b11111110,
        0b11111110,
        0b11010110,
        0b11000110,
        0b11000110,
        0b00000000,
    ],
    "N": [
        0b11000110,
        0b11100110,
        0b11110110,
        0b11011110,
        0b11001110,
        0b11000110,
        0b11000110,
        0b00000000,
    ],
    "O": [
        0b00111000,
        0b01101100,
        0b11000110,
        0b11000110,
        0b11000110,
        0b01101100,
        0b00111000,
        0b00000000,
    ],
    "P": [
        0b11111100,
        0b01100110,
        0b01100110,
        0b01111100,
        0b01100000,
        0b01100000,
        0b11110000,
        0b00000000,
    ],
    "Q": [
        0b01111000,
        0b11001100,
        0b11001100,
        0b11001100,
        0b11011100,
        0b01111000,
        0b00011100,
        0b00000000,
    ],
    "R": [
        0b11111100,
        0b01100110,
        0b01100110,
        0b01111100,
        0b01101100,
        0b01100110,
        0b11100110,
        0b00000000,
    ],
    "S": [
        0b01111000,
        0b11001100,
        0b11100000,
        0b01110000,
        0b00011100,
        0b11001100,
        0b01111000,
        0b00000000,
    ],
    "T": [
        0b11111100,
        0b10110100,
        0b00110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b01111000,
        0b00000000,
    ],
    "U": [
        0b11001100,
        0b11001100,
        0b11001100,
        0b11001100,
        0b11001100,
        0b11001100,
        0b11111100,
        0b00000000,
    ],
    "V": [
        0b11001100,
        0b11001100,
        0b11001100,
        0b11001100,
        0b11001100,
        0b01111000,
        0b00110000,
        0b00000000,
    ],
    "W": [
        0b11000110,
        0b11000110,
        0b11000110,
        0b11010110,
        0b11111110,
        0b11101110,
        0b11000110,
        0b00000000,
    ],
    "X": [
        0b11000110,
        0b11000110,
        0b01101100,
        0b00111000,
        0b00111000,
        0b01101100,
        0b11000110,
        0b00000000,
    ],
    "Y": [
        0b11001100,
        0b11001100,
        0b11001100,
        0b01111000,
        0b00110000,
        0b00110000,
        0b01111000,
        0b00000000,
    ],
    "Z": [
        0b11111110,
        0b11000110,
        0b10001100,
        0b00011000,
        0b00110010,
        0b01100110,
        0b11111110,
        0b00000000,
    ],
	

 
    

    # Punctuation

    # Punctuation
    ".": [
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00110000,
        0b00110000,
        0b00000000,
    ],
    ",": [
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b01100000,
    ],
    "!": [
        0b00110000,
        0b01111000,
        0b01111000,
        0b01111000,
        0b00110000,
        0b00000000,
        0b00110000,
        0b00000000,
    ],
    "?": [
        0b01111000,
        0b11001100,
        0b00001100,
        0b00111000,
        0b00110000,
        0b00000000,
        0b00110000,
        0b00000000,
    ],
    "@": [
        0b01111100,
        0b10000010,
        0b10111010,
        0b10101010,
        0b10111010,
        0b10000010,
        0b01111100,
        0b00000000,
    ],
    "#": [
        0b00000000,
        0b01101100,
        0b01101100,
        0b11111110,
        0b01101100,
        0b11111110,
        0b01101100,
        0b00000000,
    ],
    "$": [
        0b00110000,
        0b01111100,
        0b11000000,
        0b01111000,
        0b00001100,
        0b11111000,
        0b00110000,
        0b00000000,
    ],
    "%": [
        0b00000000,
        0b11000010,
        0b11000100,
        0b00001000,
        0b00010000,
        0b00100000,
        0b01000110,
        0b10000110,
    ],
    "&": [
        0b00111000,
        0b01101100,
        0b00111000,
        0b01110110,
        0b11011100,
        0b11001100,
        0b01110110,
        0b00000000,
    ],
    "(": [
        0b00011000,
        0b00110000,
        0b01100000,
        0b01100000,
        0b01100000,
        0b00110000,
        0b00011000,
        0b00000000,
    ],
    ")": [
        0b01100000,
        0b00110000,
        0b00011000,
        0b00011000,
        0b00011000,
        0b00110000,
        0b01100000,
        0b00000000,
    ],
    "\\": [
        0b10000000,
        0b11000000,
        0b01100000,
        0b00110000,
        0b00011000,
        0b00001100,
        0b00000110,
        0b00000010,
    ],
    "/": [
        0b00000010,
        0b00000110,
        0b00001100,
        0b00011000,
        0b00110000,
        0b01100000,
        0b11000000,
        0b10000000,
    ],
    "-": [
        0b00000000,
        0b00000000,
        0b00000000,
        0b11111100,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
    ],
    "+": [
        0b00000000,
        0b00011000,
        0b00011000,
        0b11111100,
        0b00011000,
        0b00011000,
        0b00000000,
        0b00000000,
    ],
    "=": [
        0b00000000,
        0b00000000,
        0b11111100,
        0b00000000,
        0b11111100,
        0b00000000,
        0b00000000,
        0b00000000,
    ],
    "_": [
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b11111100,
        0b00000000,
    ],
    "`": [
        0b00110000,
        0b00110000,
        0b00011000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
        0b00000000,
    ],

":": [
        0b00000000,
        0b00000000,
        0b00011000,
        0b00011000,
        0b00000000,
        0b00011000,
        0b00011000,
        0b00000000,
    ],









 "a": [
        0b00000000,
        0b00000000,
        0b01111000,
        0b00001100,
        0b01111100,
        0b11001100,
        0b01110110,
        0b00000000,
    ],
    "b": [
        0b11100000,
        0b01100000,
        0b01100000,
        0b01111100,
        0b01100110,
        0b01100110,
        0b11011100,
        0b00000000,
    ],
    "c": [
        0b00000000,
        0b00000000,
        0b01111000,
        0b11001100,
        0b11000000,
        0b11001100,
        0b01111000,
        0b00000000,
    ],
    "d": [
        0b00011100,
        0b00001100,
        0b00001100,
        0b01111100,
        0b11001100,
        0b11001100,
        0b01110110,
        0b00000000,
    ],
    "e": [
        0b00000000,
        0b00000000,
        0b01111000,
        0b11001100,
        0b11111100,
        0b11000000,
        0b01111000,
        0b00000000,
    ],
    "f": [
        0b00111000,
        0b01101100,
        0b01100000,
        0b11110000,
        0b01100000,
        0b01100000,
        0b11110000,
        0b00000000,
    ],
    "g": [
        0b00000000,
        0b00000000,
        0b01110110,
        0b11001100,
        0b11001100,
        0b01111100,
        0b00001100,
        0b11111000,
    ],
    "h": [
        0b11100000,
        0b01100000,
        0b01101100,
        0b01110110,
        0b01100110,
        0b01100110,
        0b11100110,
        0b00000000,
    ],
    "i": [
        0b00110000,
        0b00000000,
        0b01110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b01111000,
        0b00000000,
    ],
    "j": [
        0b00001100,
        0b00000000,
        0b00001100,
        0b00001100,
        0b00001100,
        0b11001100,
        0b11001100,
        0b01111000,
    ],
    "k": [
        0b11100000,
        0b01100000,
        0b01100110,
        0b01101100,
        0b01111000,
        0b01101100,
        0b11100110,
        0b00000000,
    ],
    "l": [
        0b01110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b00110000,
        0b01111000,
        0b00000000,
    ],
    "m": [
        0b00000000,
        0b00000000,
        0b11001100,
        0b11111110,
        0b11111110,
        0b11010110,
        0b11000110,
        0b00000000,
    ],
    "n": [
        0b00000000,
        0b00000000,
        0b11111000,
        0b11001100,
        0b11001100,
        0b11001100,
        0b11001100,
        0b00000000,
    ],
    "o": [
        0b00000000,
        0b00000000,
        0b01111000,
        0b11001100,
        0b11001100,
        0b11001100,
        0b01111000,
        0b00000000,
    ],
    "p": [
        0b00000000,
        0b00000000,
        0b11011100,
        0b01100110,
        0b01100110,
        0b01111100,
        0b01100000,
        0b11110000,
    ],
    "q": [
        0b00000000,
        0b00000000,
        0b01110110,
        0b11001100,
        0b11001100,
        0b01111100,
        0b00001100,
        0b00011110,
    ],
    "r": [
        0b00000000,
        0b00000000,
        0b11011100,
        0b01110110,
        0b01100110,
        0b01100000,
        0b11110000,
        0b00000000,
    ],
    "s": [
        0b00000000,
        0b00000000,
        0b01111100,
        0b11000000,
        0b01111000,
        0b00001100,
        0b11111000,
        0b00000000,
    ],
    "t": [
        0b00010000,
        0b00110000,
        0b01111100,
        0b00110000,
        0b00110000,
        0b00110100,
        0b00011000,
        0b00000000,
    ],
    "u": [
        0b00000000,
        0b00000000,
        0b11001100,
        0b11001100,
        0b11001100,
        0b11001100,
        0b01110110,
        0b00000000,
    ],
    "v": [
        0b00000000,
        0b00000000,
        0b11001100,
        0b11001100,
        0b11001100,
        0b01111000,
        0b00110000,
        0b00000000,
    ],
    "w": [
        0b00000000,
        0b00000000,
        0b11000110,
        0b11010110,
        0b11111110,
        0b11111110,
        0b01101100,
        0b00000000,
    ],
    "x": [
        0b00000000,
        0b00000000,
        0b11000110,
        0b01101100,
        0b00111000,
        0b01101100,
        0b11000110,
        0b00000000,
    ],
    "y": [
        0b00000000,
        0b00000000,
        0b11001100,
        0b11001100,
        0b11001100,
        0b01111100,
        0b00001100,
        0b11111000,
    ],
    "z": [
        0b00000000,
        0b00000000,
        0b11111100,
        0b10011000,
        0b00110000,
        0b01100100,
        0b11111100,
        0b00000000,
     ],   
       "\u2190": [
      0b00010000,
      0b00110000,
      0b01111111,
      0b11111111,
      0b01111111,
      0b00110000,
      0b00010000,
      0b00000000,
    ],
	
    "\u2713": [
      0b00000000,
      0b00000001,
      0b00000010,
      0b00000100,
      0b10001000,
      0b01010000,
      0b00100000,
      0b00000000,
      ],
      
    "\u2193": [
      0b00111000,
      0b00111000,
      0b00111000,
      0b00111000,
      0b11111110,
      0b01111100,
      0b00111000,
      0b00010000,
      ],
    "\u2192":[
      0b00001000,
      0b00001100,
      0b11111110,
      0b11111111,
      0b11111110,
      0b00001100,
      0b00001000,
      0b00000000,
      ],
    "\u2191": [
      0b00010000,
      0b00111000,
      0b01111100,
      0b11111110,
      0b00111000,
      0b00111000,
      0b00111000,
      0b00111000,
      ]
  

}



# Add consistent spacing
#for char in font:
#    font[char].append(0b00000)

 
