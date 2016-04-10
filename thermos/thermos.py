from datetime import datetime
from flask import Flask, flash, render_template, request, url_for, redirect

app = Flask(__name__)
app.config[
    'SECRET_KEY'] = '28\xc0x\x04\xea#\xd7\xe2\xf2\x19-\xe9\x8b\x81\xa5\x86\x03v\xbe\x85\xfdm\x8a'


class User:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return '{}. {}'.format(self.firstname[0], self.lastname[0])


def new_bookmarks(num):
    return sorted(bookmarks, key=lambda bm: bm['date'], reverse=True)[:num]
    
    
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Social Bookmarking", new_bookmarks=new_bookmarks(5))


@app.route('/profile')
def profile():
    return render_template('profile.html')


bookmarks = []


def store_bookmarks(url):
    bookmarks.append(dict(
        url=url,
        user='Rowland',
        date=datetime.utcnow()
    ))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        store_bookmarks(url)
        flash('Stored url in {}'.format(url))
        return redirect(url_for('index'))
    return render_template('add.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
