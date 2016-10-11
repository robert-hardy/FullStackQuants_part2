from flask import render_template


from app.flasky import app


@app.route('/')
def homepage():
    return render_template(
        'homepage.html'
    )


app.run(host='0.0.0.0', port=8080)
