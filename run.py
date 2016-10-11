from flask import Response


from app.flasky import app


@app.route('/')
def homepage():
    return Response("Hello")


app.run(host='0.0.0.0', port=8080)
