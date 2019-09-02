import bottle
from bottle import route, run


app = bottle.default_app()


@route('/')
def hello_world():
    return "Hello, world! (From Full Stack Python)"


if __name__ == "__main__":
    run(host="0.0.0.0", port=8080, debug=True, reloader=True)
