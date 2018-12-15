from flask import render_template
from app import app
from flask import request

@app.route('/')
@app.route('/index',methods = ['POST','GET'])
def index():
    page_title = '测试页面'
    if request.method == 'GET':
        return render_template('index.html',page_title = page_title)
    elif request.method == 'POST':
        search_content = request.form['search_content']
        return render_template('index.html',page_title = search_content)



