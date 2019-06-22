from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello World</h1>
    <p>It is currently {time}.</p>
    """.format(time=the_time)


@app.route('/user', methods = ['GET'])
def get_user():
	user_id = request.args.get('user_id')
	return "User ID is " + user_id

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

