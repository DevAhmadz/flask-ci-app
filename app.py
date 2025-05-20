from flask import Flask #
app = Flask (__name__ ) # create the Flask app

@app.route('/') # route for the home page
def hello_world(): # function to return the string
    return "Hello DevOps!" #

if __name__ == '__main__': # on running python app.py
    app.run(host='0.0.0.0', port=81) # run the flask app