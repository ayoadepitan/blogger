from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Ayo Adepitan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Jan 18, 2022'
    },
    {
        'author': 'Johnny Depp',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Jan 19, 2022'
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')
