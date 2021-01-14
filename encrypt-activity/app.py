from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def mainPage():
    inputted = False
    return render_template("index.html"), inputted

@app.route('/', methods=['POST'])
def formPost():
    word = request.form['password']
    inputted = True
    key = "specialkey"
    encrypted = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(word)):
        encrypted += alphabet[alphabet.index(word[i]) + alphabet.index(key[i % len(key)]) + 1]
        encrypted += key[i % len(key)]
    return encrypted, inputted

if __name__ == "__main__":
    app.run()
