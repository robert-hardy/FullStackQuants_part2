from flask import render_template


from app.flasky import app


@app.route('/')
def homepage():
    rows = [
        {
            'title': 'Buy a big book',
            'notes': 'A red one'
        },
        {
            'title': 'Buy a shiny pen',
            'notes': 'blue ink'
        }
    ]

    return render_template(
        'homepage.html',
        rows=rows
    )


app.run(host='0.0.0.0', port=8080)
