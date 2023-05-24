from flask import Flask, render_template, abort, url_for
from flask import request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/gallery.html')
def gallery():
    return render_template('gallery.html')


@app.route('/contact.html')
def contact():
    return render_template('kontakt.html')


@app.route('/guestbook.html')
def guestbook():
    return render_template('guestbook.html')


@app.route('/error_denied')
def error_denied():
    abort(401)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
