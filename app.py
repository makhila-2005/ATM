from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "atm_secret_key"


# ✅ Ensure correct database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "atm.db")


def get_db():
    return sqlite3.connect(DB_PATH)


# ✅ LOGIN ROUTE
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pin = request.form["pin"]

        conn = get_db()
        cur = conn.cursor()

        cur.execute("SELECT id, name FROM users WHERE pin = ?", (pin,))
        user = cur.fetchone()

        conn.close()

        if user:
            session["user_id"] = user[0]
            session["user_name"] = user[1]
            return redirect(url_for("menu"))
        else:
            return render_template("login.html", error="Invalid PIN")

    return render_template("login.html")


# ✅ REGISTER ROUTE
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        pin = request.form["pin"]

        # Check PIN length
        if len(pin) != 4 or not pin.isdigit():
            return render_template("register.html", error="PIN must be 4 digits")

        conn = get_db()
        cur = conn.cursor()

        # Check if PIN already exists
        cur.execute("SELECT * FROM users WHERE pin = ?", (pin,))
        existing_user = cur.fetchone()

        if existing_user:
            conn.close()
            return render_template("register.html", error="PIN already exists")

        # Insert new user
        cur.execute(
            "INSERT INTO users (name, pin, balance) VALUES (?, ?, ?)",
            (name, pin, 0)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


 #✅ MENU ROUTE
@app.route("/menu")
def menu():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("menu.html", name=session["user_name"])

# ✅ BALANCE ROUTE
@app.route("/balance")
def balance():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT balance FROM users WHERE id = ?",
        (session["user_id"],)
    )

    balance = cur.fetchone()[0]

    conn.close()

    return render_template("balance.html", balance=balance)


# ✅ DEPOSIT ROUTE
@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        amount = int(request.form["amount"])

        if amount <= 0:
            return render_template("deposit.html", error="Enter valid amount")

        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "UPDATE users SET balance = balance + ? WHERE id = ?",
            (amount, session["user_id"])
        )

        conn.commit()
        conn.close()

        return redirect(url_for("balance"))

    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT balance FROM users WHERE id = ?", (session["user_id"],))
    balance = cur.fetchone()[0]

    if request.method == "POST":
        amount = int(request.form["amount"])

        if amount <= 0:
            conn.close()
            return render_template("withdraw.html", error="Enter valid amount")

        if amount > balance:
            conn.close()
            return render_template("withdraw.html", error="Insufficient balance")

        cur.execute(
            "UPDATE users SET balance = balance - ? WHERE id = ?",
            (amount, session["user_id"])
        )

        conn.commit()
        conn.close()

        return redirect(url_for("balance"))

    conn.close()
    return render_template("withdraw.html")

# ✅ WITHDRAW ROUTE


# ✅ LOGOUT ROUTE
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ✅ RUN APP
if __name__ == "__main__":
    app.run(debug=True)
