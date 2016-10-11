from flask import render_template


from app.db import connect_db
from app.flasky import app


@app.route('/')
def homepage():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            *
        FROM
            todo
    """)
    rows = cur.fetchall()

    return render_template(
        'homepage.html',
        rows=rows
    )


app.run(host='0.0.0.0', port=8080)
