"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."

@app.route("/game")
def show_madlib_form():
    """This determines if our user wants to play Madlibs."""

    play_game = request.args.get("game")

    if play_game == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route("/madlib")
def show_madlib():
    """This is our Mablib game."""

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    noun2 = request.args.get("noun2")
    
    return render_template("madlib.html",
    person = person,
    color = color,
    noun = noun,
    adjective = adjective,
    noun2 = noun2)
    



@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    return render_template("compliment.html", person=player)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
