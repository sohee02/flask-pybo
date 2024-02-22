# Created by user at 2024-02-14
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flaskext.markdown import Markdown
from flask_simplemde import SimpleMDE

import config

# SQLite bug 처리
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


# 애플리케이션 팩토리
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.config["SIMPLEMDE_JS_IIFE"] = True
    app.config["SIMPLEMDE_USE_CDN"] = True

    # ORM
    db.init_app(app)
    # 제약 조건이름은 MetaData클래스의 사용 규칙을 정의
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)  #
    else:  # SQLite가 아닌 경우
        migrate.init_app(app, db)

    from . import models

    # print(f"__name__:{__name__}")

    # Blueprint등록
    from .views import main_views, question_views, answer_views, auth_views

    app.register_blueprint(main_views.bp)  # main
    app.register_blueprint(question_views.bp)  # Question
    app.register_blueprint(answer_views.bp)  # Answer
    app.register_blueprint(auth_views.bp)

    # 필터:datetime으로 등록
    from .filter import formatDateTime
    app.jinja_env.filters['datetime'] = formatDateTime

    # markdown : nl2br은 줄바꿈 문자를 <br/> 바꿔 준다.
    Markdown(app, extensions=["nl2br", "fenced_code"])
    SimpleMDE(app)

    return app