from flask import (
    jsonify,
    render_template,
    request
)


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


@app.route('/todos')
def get_todos():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            *
        FROM
            todo
    """)
    rows = cur.fetchall()
    return jsonify(rows)


@app.route('/todos', methods=['POST'])
def create_todo():
    title = request.json.get('title', None)
    notes = request.json.get('notes', None)
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO
            todo
        (
            title,
            notes
        )
        VALUES
        (?, ?)
    """, (title, notes))
    conn.commit()
    id = cur.lastrowid
    cur.execute("""
        SELECT
            *
        FROM
            todo
        WHERE
            id = '{0}';
    """.format(id))
    rows = cur.fetchall()
    return jsonify(rows)


@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM todo WHERE id='{0}';
    """.format(id))
    conn.commit()
    return jsonify({'message': 'successfully deleted'})


app.run(host='0.0.0.0', port=8080)
