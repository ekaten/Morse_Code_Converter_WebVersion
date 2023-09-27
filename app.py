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
app.secret_key = "sdkfgnslkdfnslkdfndf"
Bootstrap(app)


################ FORM CLASSES ##############


class CreateConverterForm(FlaskForm):
    input = TextAreaField(label="", validators=[DataRequired()], render_kw={"placeholder": "Input:"})
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
    return output


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
    return decoded_word


################ ROUTES ##################
@app.route('/', methods=["GET", "POST"])
def index():
    output = ""
    form = CreateConverterForm()
    if form.validate_on_submit():
        print("Success")
        input_text = form.input.data
        # Check if input is text or morse code
        if is_morse(input_text):
            output = decode(input_text)
        else:
            output = encode(input_text)
        return render_template("index.html", year=year, form=form, output=output)
    else:
        return render_template("index.html", year=year, form=form, output=output)


if __name__ == "__main__":
    app.run(debug=True)
