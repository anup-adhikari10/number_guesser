from flask import Flask, request
import random

# Generate a random number between 0 and 9
random_number = random.randint(0, 9)
print(f"Random number to guess: {random_number}")

# Create Flask app
app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    # Home page with instructions and an input form
    return '''
        <h1>Guess a number between 0 and 9</h1>
        <form action="/guess" method="post">
            <input type="number" name="guess" min="0" max="9" required>
            <button type="submit">Submit</button>
        </form>
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>
    '''

@app.route('/guess', methods=["POST"])
def guess_number():
    # Get the user's guess from the form
    guess = int(request.form["guess"])
    # Compare the guess with the random number
    if guess > random_number:
        return '''
            <h1 style="color: purple">Too high, try again!</h1>
            <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>
            <br>
            <a href="/">Try Again</a>
        '''
    elif guess < random_number:
        return '''
            <h1 style="color: red">Too low, try again!</h1>
            <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>
            <br>
            <a href="/">Try Again</a>
        '''
    else:
        return '''
            <h1 style="color: green">You found me!</h1>
            <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>
            <br>
            <a href="/">Play Again</a>
        '''

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
