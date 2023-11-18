from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/one_cupcake")
def individual_cupcake():
    return render_template("one_cupcake.html")

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html")

@app.route("/active_order")
def current_order():
    return render_template("active_order.html")


if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")