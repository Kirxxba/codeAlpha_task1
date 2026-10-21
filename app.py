from flask import Flask, render_template_string, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "codealpha-local-demo-key"
DB_NAME = "data.db"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Data Redundancy Removal System</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            margin: 0;
            padding: 30px 16px;
            color: #172033;
        }
        .container { max-width: 850px; margin: auto; }
        header, .card {
            background: white;
            padding: 24px;
            border-radius: 14px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px #0000000c;
        }
        h1 { margin-top: 0; color: #2446a6; }
        input, button {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            border-radius: 8px;
            font-size: 15px;
        }
        input { border: 1px solid #cbd5e1; }
        button {
            background: #2446a6;
            color: white;
            border: none;
            cursor: pointer;
        }
        table { width: 100%; border-collapse: collapse; }
        th, td {
            padding: 12px 8px;
            border-bottom: 1px solid #e2e8f0;
            text-align: left;
            overflow-wrap: anywhere;
        }
        .message { padding: 12px; background: #e0f2fe;
                   border-radius: 8px; margin-bottom: 15px; }
        .count { font-size: 28px; font-weight: bold; }
        .table-wrap { overflow-x: auto; }
    </style>
</head>
<body>
<div class="container">
    <header>
        <h1>Data Redundancy Removal System</h1>
        <p>Validate records and prevent duplicate email entries.</p>
        <p>Total unique records</p>
        <div class="count">{{ records|length }}</div>
    </header>

    {% with messages = get_flashed_messages() %}
      {% for message in messages %}
        <div class="message">{{ message }}</div>
      {% endfor %}
    {% endwith %}

    <section class="card">
        <h2>Add New Record</h2>
        <form method="POST" action="{{ url_for('add_record') }}">
            <label>Name</label>
            <input name="name" required maxlength="100"
                   placeholder="Enter name">
            <label>Email</label>
            <input name="email" type="email" required maxlength="254"
                   placeholder="Enter email">
            <button type="submit">Validate and Save</button>
        </form>
    </section>

    <section class="card">
        <h2>Saved Records</h2>
        {% if records %}
        <div class="table-wrap">
        <table>
            <tr><th>ID</th><th>Name</th><th>Email</th></tr>
            {% for record in records %}
            <tr>
                <td>{{ record[0] }}</td>
                <td>{{ record[1] }}</td>
                <td>{{ record[2] }}</td>
            </tr>
            {% endfor %}
        </table>
        </div>
        {% else %}
        <p>No records saved yet.</p>
        {% endif %}
    </section>
</div>
</body>
</html>
"""


def get_records():
    with sqlite3.connect(DB_NAME) as conn:
        return conn.execute(
            "SELECT id, name, email FROM records ORDER BY id DESC"
        ).fetchall()


@app.route("/")
def home():
    return render_template_string(HTML, records=get_records())


@app.route("/add", methods=["POST"])
def add_record():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()

    if not name or not email or "@" not in email:
        flash("Please enter a valid name and email.")
        return redirect(url_for("home"))

    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute(
                "INSERT INTO records (name, email) VALUES (?, ?)",
                (name, email)
            )
        flash("Unique record saved successfully!")
    except sqlite3.IntegrityError:
        flash("Duplicate detected! Record was not saved.")

    return redirect(url_for("home"))


if __name__ == "__main__":
    # Local development only; do not expose this server publicly.
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
