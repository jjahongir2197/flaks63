from flask import Flask, render_template, request, redirect

app = Flask(__name__)

attempts = 0

@app.route("/", methods=["GET", "POST"])
def login():

    global attempts

    message = ""

    if request.method == "POST":

        attempts += 1

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            message = "Success!"
            attempts = 0
        else:
            message = "Wrong credentials!"

    return render_template("index.html", message=message, attempts=attempts)

if __name__ == "__main__":
    app.run(debug=True)
