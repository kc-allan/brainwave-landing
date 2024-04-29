from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def landing():
    return make_response(render_template('index.html'))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        use_reloader=True
	)