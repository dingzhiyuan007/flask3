


from flask import Flask,url_for,redirect,render_template
import config
app = Flask(__name__)


@app.route('/')
def hello_world():
    # print(url_for('page',num=3987))
    return '3 World!'

@app.route('/index')
def index():
    return render_template('index.html',username='王松')

@app.route('/page/<num>')
def page(num):
    return '页码是：{}'.format(num)





if __name__ == '__main__':
    app.run()
