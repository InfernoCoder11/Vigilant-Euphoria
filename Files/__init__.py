from flask import Flask, render_template, request
import subprocess as sub

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("main.html")

@app.route("/handle_data", methods = ["POST"])
def handle_data():
	heading = request.form["heading"]
	message = request.form["message"]
	sub.call (["notify-send", heading, message])
	return render_template("main.html")

if (__name__ == "__main__"):
	app.run(port = 5567)
