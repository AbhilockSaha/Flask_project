from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Pass optional dynamic data (like username) to the HTML file
    return render_template('index.html', username='Alex')

if __name__ == '__main__':
    app.run(debug=True)
