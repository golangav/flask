from datetime import datetime
from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/env')
def env():
    html = "System Time: \n\n"
    html += datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    import logging  # 引入logging模块
    logging.basicConfig(level=logging.NOTSET)  # 设置日志级别
    logging.info(u"%s-----%s"%(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),receive data))
    return Response(html, mimetype='text/plain')
