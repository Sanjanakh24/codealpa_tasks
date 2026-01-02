from flask import Flask, request, render_template_string
import pymysql

app = Flask(__name__)

# ---------- DATABASE CONNECTION ----------
def get_db():
    return pymysql.connect(
        host="Enter yor RDS Host",
        user="admin",
        password="123456789",     # move to env variable in production
        database="buspass"
    )

# ---------- HTML TEMPLATES ----------
HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Bus Pass System</title>
</head>
<body>
    <h2>Cloud-Based Bus Pass System</h2>

    <form method="post" action="/book">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Route:</label><br>
        <input type="text" name="route" required><br><br>

        <label>Price:</label><br>
        <input type="number" name="price" required><br><br>

        <button type="submit">Book Pass</button>
    </form>

    <br>
    <a href="/passes">View All Passes</a>
</body>
</html>
"""

SUCCESS_HTML = """
<h3>✅ Pass booked successfully!</h3>
<a href="/">Go Back</a>
"""

PASSES_HTML = """
<h2>All Bus Passes</h2>
<table border="1" cellpadding="5">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Route</th>
        <th>Price</th>
    </tr>
    {% for p in passes %}
    <tr>
        <td>{{ p[0] }}</td>
        <td>{{ p[1] }}</td>
        <td>{{ p[2] }}</td>
        <td>{{ p[3] }}</td>
    </tr>
    {% endfor %}
</table>
<br>
<a href="/">Go Back</a>
"""

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/book", methods=["POST"])
def book_pass():
    name = request.form["name"]
    route = request.form["route"]
    price = request.form["price"]

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO passes (name, route, price) VALUES (%s, %s, %s)",
        (name, route, price)
    )

    db.commit()
    db.close()

    return render_template_string(SUCCESS_HTML)

@app.route("/passes")
def view_passes():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM passes")
    passes = cursor.fetchall()
    db.close()

    return render_template_string(PASSES_HTML, passes=passes)

# ---------- RUN SERVER ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
