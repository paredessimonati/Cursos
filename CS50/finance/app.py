import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
# if not os.environ.get("API_KEY"):
# raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session.get("user_id")
    # getting neccesary info from db
    rows = db.execute("SELECT symbol, SUM(number_of_shares) AS total_share FROM purchases WHERE person_id = ? GROUP BY symbol", user_id)
    # setting up variables
    portfolio = []
    cash = 0
    stock_value = 0
    # loop to append neccesary data to portfolio array and update the cash
    for row in rows:
        stock = lookup(row["symbol"])
        portfolio.append({
            "symbol": stock["symbol"],
            "name": stock["name"],
            "shares": row["total_share"],
            "price": usd(stock["price"]),
            "total": usd(stock["price"] * row["total_share"])
        })
        stock_value += (stock["price"] * row["total_share"])
    # totals
    total = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = total[0]["cash"]
    total = total[0]["cash"] + stock_value

    return render_template("index.html", port=portfolio, cash=cash, total=total, usd=usd)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        # validating
        if not request.form.get("symbol"):
            return apology("Please enter a valid symbol")
        elif lookup(request.form.get("symbol")) == None:
            return apology("NOT A STOCK")
        elif request.form.get("shares").isdigit() == False:
            return apology("Please enter a number -.-")
        elif int(request.form.get("shares")) <= 0:
            return apology("Please enter positive integer")
        # setting up variables
        stock = lookup(request.form.get("symbol"))
        sum = float(stock["price"]) * float(request.form.get("shares"))
        user_id = session.get("user_id")
        rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)
        total = rows[0]["cash"]
        cash = total - sum
        if rows[0]["cash"] < sum:
            return apology("Too poor :sadface")
        # updating database
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash, user_id)
        # updating purchases table
        db.execute("INSERT INTO purchases (person_id, symbol, name, price_of_transaction, number_of_shares) VALUES (?, ?, ?, ?, ?)",
                   user_id, stock["symbol"], stock["name"], stock["price"], request.form.get("shares"))

        # returning all variables
        return render_template("bought.html", stock=stock, usd=usd, shares=int(request.form.get("shares")), sum=usd(sum), cash=usd(cash), total=usd(total))
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    user_id = session.get("user_id")
    rows = db.execute("SELECT * FROM purchases WHERE person_id = ? ORDER BY datetime", user_id)
    print(rows)
    return render_template("history.html", rows=rows, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    # if get creates page to imput symbol
    if request.method == "GET":
        return render_template("quote.html")
    # when i get post, i extract the values from stock and render them on quoted.html
    elif lookup(request.form.get("symbol")) == None:
        return apology("NOT A STOCK")
    else:
        stock = lookup(request.form.get("symbol"))
        return render_template("quoted.html", name=stock["name"], price=usd(stock["price"]), symbol=stock["symbol"])


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # checking for valid inputs
        if not request.form.get("username"):
            return apology("Please enter username")
        elif not request.form.get("password"):
            return apology("Please enter your password")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Password dont match")
        # using variable rows to count how many matches
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 0:
            return apology("Username already in use")
        # hashing password
        hash = generate_password_hash(request.form.get("password"))
        # inserting data into database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hash)
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_id = session.get("user_id")
    # getting data to fill select object
    if request.method == "GET":
        rows = db.execute(
            "SELECT symbol, SUM(number_of_shares) AS total_share FROM purchases WHERE person_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", rows=rows)
    # getting POST
    else:
        # getting data from page and db
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        stock = lookup(symbol)
        if not request.form.get("shares"):
            return apology("Enter number of shares to sell")
        rows = db.execute(
            "SELECT SUM(number_of_shares) AS total_share FROM purchases WHERE person_id = ? AND symbol = ?", user_id, symbol)
        if not rows or int(shares) > rows[0]["total_share"]:
            return apology("Not enough shares")
        price = stock["price"]
        total = price * int(shares)
        # updating DB with sell data
        db.execute("INSERT INTO purchases (person_id, symbol, number_of_shares, price_of_transaction) VALUES (?, ?, ?, ?)",
                   user_id, symbol, -int(shares), price)
        # updating database with user cash
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total, user_id)
        return redirect("/")


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    user_id = session.get("user_id")
    if request.method == "POST":
        # getting hash
        rows = db.execute("SELECT hash FROM users WHERE id = ?", user_id)
        print(rows)
        # checking for valid inputs
        if not request.form.get("password"):
            return apology("Please enter current password")
        elif not request.form.get("newpassword"):
            return apology("Please enter your new password")
        elif request.form.get("newpassword") != request.form.get("confirmation"):
            return apology("Passwords dont match")
        # comparing current password
        elif not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("H4XX0R D3T3CT3D")
        # hashing new password
        hash = generate_password_hash(request.form.get("newpassword"))
        # inserting data into database
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, user_id)
        return redirect("/")
    else:
        return render_template("password.html")


@app.route("/funds", methods=["GET", "POST"])
@login_required
def funds():
    user_id = session.get("user_id")
    if request.method == "POST":
        # validatin input
        if not request.form.get("funds"):
            return apology("Please enter desired funds...")
        elif request.form.get("funds").isdigit() == False:
            return apology("Please enter a number...")
        elif int(request.form.get("funds")) <= 0:
            return apology("Please enter positive integer")
        # setting up variable and update db
        funds = request.form.get("funds")
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", funds, user_id)
        return redirect("/")
    else:
        return render_template("funds.html")