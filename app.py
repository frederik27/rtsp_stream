from flask import Flask, Response, render_template, request
# from camera import Camera

app = Flask(__name__)
URL = 0


@app.route('/')
def index():
    return render_template('index.html')

#
# def gen(get_frame):
#     while True:
#         frame = get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#
#
# @app.route('/stream_data')
# def stream_data():
#     global URL
#     ex = Camera(URL)
#     return Response(gen(ex.get_frame), mimetype='multipart/x-mixed-replace; boundary=frame')
#
#
# #
# @app.route('/', methods=['GET', 'POST'])
# def camera_link():
#     if request.method == 'POST':
#         global URL
#         URL = request.form['url']
#     return render_template('index.html')
#

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
