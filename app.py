from flask import Flask, render_template, request, redirect, url_for, session
from search import search

app = Flask(__name__)
app.secret_key = "#$%#$%^%^BFGBFGBSFGNSGJTNADFHH@#%$%#T#FFWF$^F@$F#$FW"


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/search", methods=["POST", "GET"])
def searchr():
	if request.method == "POST":
		query = request.form["query"]
		results = search(query, num_results=35)
		session["results"] = results
		session["query"] = query
		return redirect(url_for("searchr"))
	return render_template("search.html", results=session["results"], query=session["query"])


if __name__ == '__main__':
	app.run(debug=True)