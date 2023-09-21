import app
from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
import datetime as dt
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm

now = dt.datetime.now()
year = now.year

MORSE_CODE = {
    "a": '.-',
    "b": '-...',
    "c": '-.-.',
    "d": '-..',
    "e": '.',
    "f": '..-.',
    "g": '--.',
    "h": '....',
    "i": '..',
    "j": '.---',
    "k": '-.-',
    "l": '.-..',
    "m": '--',
    "n": '-.',
    "o": '---',
    "p": '.--.',
    "q": '--.-',
    "r": '.-.',
    "s": '...',
    "t": '-',
    "u": '..-',
    "v": '...-',
    "w": '.--',
    "x": '-..-',
    "y": '-.--',
    "z": '--..',
    "1": '.----',
    "2": '..---',
    "3": '...--',
    "4": '....-',
    "5": '.....',
    "6": '-....',
    "7": '--...',
    "8": '---..',
    "9": '----.',
    "0": '-----',
    " ": '/'}

################ APP INITS ##################

app = Flask(__name__)
app.secret_key = "sdkfgnslkdfnslkdfn"
Bootstrap(app)


################ FORM CLASSES ##############


class CreateConverterForm(FlaskForm):
    input = TextAreaField(label="", validators=[DataRequired()],render_kw={"placeholder": "Input:"})
    convert_button = SubmitField(label='Convert')


################ FUNCTION DECLARATIONS ##############

def encode(text):
    output = ""
    # Check is symbol in the entry. If it is a letter, convert to lower case
    for s in text:
        if s.isalpha():
            s = s.lower()
        # Check if symbol is in the Morse Code dictionary
        try:
            encoded_s = MORSE_CODE[s]
        # If symbol is not found, pass
        except KeyError:
            pass
        # If symbol is in dictionary, add it to the output string
        else:
            output += encoded_s + " "

    # Print the output string
    print(f"\nOUTPUT: \n{output}")


def text_accepted(text):
    if input_text == '@':
        return False
    else:
        return True


def is_morse(input_text):
    for char in input_text:
        if char in [".", "-", "/", " "]:
            it_is_morse = True
        else:
            it_is_morse = False
        return it_is_morse


def decode(input_text):
    decoded_word = ""
    list_of_chars = input_text.split(" ")
    print(list_of_chars)
    for char in list_of_chars:
        for sym in MORSE_CODE:
            if MORSE_CODE[sym] == char:
                decoded_char = sym
                decoded_word += decoded_char
    print(decoded_word)


def need_another_encoding():
    response = ""
    if response != "Y" or response != "N":
        response = input("\nNeed More Encoding/Decoding? Y/N: ")
        if response == "N":
            return False
        elif response == "Y":
            print("\n\n/////////// NEW ENCODING ///////////")
            return True


################ ROUTES ##################
@app.route('/', methods=["GET", "POST"])
def index():
    output = ""
    form = CreateConverterForm()
    return render_template("index.html", year=year, form=form, output=output)


# # set while variable
# need_encoding = True
#
# # While encoding is needed, request input
# while need_encoding:
#     print("---Type @ to quit---")
#     input_text = input("\nINPUT: ")
#
#     # Check if user wants to quit or encode/decode
#     if text_accepted(input_text):
#         # Check if input is text or morse code
#         if is_morse(input_text):
#             decode(input_text)
#         else:
#             encode(input_text)
#     else:
#         break
#
#
#     # Does user want to do another decoding/encoding session?
#     need_encoding = need_another_encoding()
#
#
#
# print("\n//////////// Good Bye! /////////////")
#


app.run(debug=True, port=7000)
