from flask import Flask, render_template, abort, request, redirect, url_for
from models import db, Message
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'
app.template_folder = 'templates'
db.init_app(app)


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
def guestbook_html():
    return render_template('guestbook.html')



@app.route('/error_denied')
def error_denied():
    abort(401)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.route('/guestbook')
def guestbook():
    messages = Message.query.all()
    return render_template('guestbook.html', messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    nick = request.form['nick']
    text = request.form['text']
    date_str = request.form['date']
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    message = Message(nick=nick, text=text, date=date)
    db.session.add(message)
    db.session.commit()
    return redirect(url_for('guestbook'))


@app.route('/edit_message/<int:message_id>', methods=['GET', 'POST'])
def edit_message(message_id):
    message = Message.query.get(message_id)
    if request.method == 'POST':
        message.nick = request.form['nick']
        message.text = request.form['text']
        message.date = request.form['date']
        db.session.commit()
        return redirect(url_for('guestbook'))
    return render_template('edit_message.html', message=message)

@app.route('/delete_message/<int:message_id>')
def delete_message(message_id):
    message = Message.query.get(message_id)
    db.session.delete(message)
    db.session.commit()
    return redirect(url_for('guestbook'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
