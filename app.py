from flask import Flask, render_template, request

app = Flask(__name__)

appointments = []  # simple in-memory storage

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/book', methods=["POST"])
def book():
    name = request.form.get("name")
    date = request.form.get("date")
    reason = request.form.get("reason")

    appointments.append({"name": name, "date": date, "reason": reason})

    return render_template("success.html", name=name, date=date, reason=reason)

@app.route('/appointments')
def view_appointments():
    return {"appointments": appointments}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
