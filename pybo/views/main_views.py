# Created by user at 2024-02-14
#가나다
from flask import Blueprint,url_for,jsonify
from werkzeug.utils import redirect

#__name__: main_views.py
bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return "Hello, world!!!"
@bp.route('/json_text')
def json_text():
    data = {'name':'이상무','age':23}
    jsonString = jsonify(data)
    print(f'jsonString:{jsonString}')
    return jsonString
@bp.route('/server_info')
def server_json():
    data = {'server_name':'0.0.0.0', 'server_port':'8080'} # Json 형식
    return jsonify(data)
@bp.route('/')
def index():
    #redirect(URL) : URL로 페이지 이동
    #url_for(라우팅함수명): 라우팅 함수에 매핑되어 있는 URL return
    print("-"*50)
    print(f'url_for(question._list):{url_for('question._list')}') #/question/list
    print("-" * 50)
    return redirect(url_for('question._list'))