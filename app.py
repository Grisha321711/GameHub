from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        nickname = request.form["nickname"]
        email = request.form["email"]
        code = request.form["code"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (nickname, email, password) VALUES (?, ?, ?)",
            (nickname, email, code)
        )

        conn.commit()
        conn.close()

        return "Аккаунт успешно создан!"

    return render_template("register.html")


@app.route("/admin")
def admin():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()

    return render_template("admin.html", users=users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)