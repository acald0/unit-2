from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary, random_cupcake

@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/one_cupcake")
def individual_cupcake():
    return render_template("one_cupcake.html", cupcake = random_cupcake("cupcakes.csv"))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html")

@app.route("/active_order")
def current_order():
    return render_template("active_order.html")

@app.route("/find-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    if cupcake:
        add_cupcake_dictionary("current.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Cupcake is not found"

# Can't get this to work


if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")