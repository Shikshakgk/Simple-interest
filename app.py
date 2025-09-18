# from flask import Flask, render_template, request

# app = Flask(__name__)

# def calculate_simple_interest(principal, rate, time):
#     return (principal * rate * time) / 100

# @app.route("/", methods=["GET", "POST"])
# def index():
#     si = None
#     if request.method == "POST":
#         try:
#             principal = float(request.form["principal"])
#             rate = float(request.form["rate"])
#             time = float(request.form["time"])
#             si = round(calculate_simple_interest(principal, rate, time), 2)
#         except Exception:
#             si = None
#     return render_template("index1.html", si=si)

# if __name__ == "__main__":
#     app.run(debug=True,port=5100)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    si = None
    if request.method == "POST":
        try:
            p = float(request.form["principal"])
            r = float(request.form["rate"])
            t = float(request.form["time"])
            si = round((p * r * t) / 100, 2)
        except Exception as e:
            si = f"Error: {str(e)}"
    return render_template("index1.html", si=si)

if __name__ == "__main__":
    app.run(debug=True,port=5100)

