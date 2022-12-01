from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hey there!!! It is the next work using Heroku ;)'

if __name__ == '__main__':
    app.run(debug=True)
