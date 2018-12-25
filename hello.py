from datetime import datetime
from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def root():
    import logging
    logging.basicConfig(level=logging.NOTSET)
    logging.info(u"%s-----%s"%(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),"receive data"))
    return app.send_static_file('index.html')


@app.route('/env')
def env():
    html = "System Time: \n\n"
    html += datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    import logging
    logging.basicConfig(level=logging.NOTSET)
    logging.info(u"%s-----%s"%(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),"receive data"))
    return Response(html, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,threaded=True,debug=True)
