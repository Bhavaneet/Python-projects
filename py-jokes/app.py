from flask import Flask
import pyjokes

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    joke = pyjokes.get_joke()
    return f"<h1>{joke}</h1>"

@app.route("/multiplejokes")
def jokes():
    jokes = pyjokes.get_jokes()
    return f"<h2>{jokes}\n</h2>"

if __name__ == "__main__":
    app.run(debug = True)