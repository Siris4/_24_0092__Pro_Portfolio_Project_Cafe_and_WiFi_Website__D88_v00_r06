from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Placeholder cafe data
    cafes = [
        {'name': 'Cafe One', 'location': 'London'},
        {'name': 'Cafe Two', 'location': 'London'},
        {'name': 'Cafe Three', 'location': 'London'},
    ]
    return render_template('index.html', cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)
