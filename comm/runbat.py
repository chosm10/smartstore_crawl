import os
from flask import Flask  # 서버 구현을 위한 Flask 객체 import
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
from flask_cors import CORS

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
CORS(app)
api = Api(app)  # Flask 객체에 Api 객체 등록


@api.route('/runtask/<string:task_name>')  # 데코레이터 이용, '/hello' 경로에 클래스 등록
class HelloWorld(Resource):
    def get(self, task_name):  # GET 요청시 리턴 값에 해당 하는 dict를 JSON 형태로 반환
        os.system("C:\\Users\\Administrator\\rpa_naver_brandmall\\batch\\naver_daily_selling\\{}.bat".format(task_name))
        return {"hello": "world!"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)