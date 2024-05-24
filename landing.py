from flask import Flask, render_template, make_response,request, flash, redirect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'not-advisable-string-for-prod'

@app.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        flash("This is still work under progress.")
        return redirect('/')
    return make_response(render_template('index.html'))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        use_reloader=True
	)