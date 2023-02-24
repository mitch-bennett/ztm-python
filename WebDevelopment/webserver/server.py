from flask import Flask, render_template, url_for
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, MITCH!'


@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs'

@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my dog'

# @app.route('/')
# def hello_world():
#     print(url_for('static', filename='favicon.ico'))
#     return render_template('./index.html')

@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('./index.html', name=username, post_id=post_id)

@app.route('/about.html')
def about():
    return render_template('./about.html')

# @app.route('/favicon.ico')
# def fav():
#     return 'These are my thoughts on blogs'