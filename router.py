from flask import Flask,Blueprint,render_template,request,redirect
from shorterner import shortener

myshortener = shortener()
short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    act_url = myshortener.revbook[short_url]
    return redirect(act_url)


@short.route('/')
def index():
    return render_template('index.html')


@short.route('/add_link', methods=['POST'])
def add_link():
    org_url = request.form['originalurl']
    new_url = myshortener.redirect(org_url)
    print(myshortener.revbook)
    print(myshortener.book)
    return render_template('new_link.html',newurl=new_url,origurl=org_url)

@short.route('/stats')
def stats():
    pass

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(short)
    app.run()