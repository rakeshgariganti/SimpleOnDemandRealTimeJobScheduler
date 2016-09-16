from flask import Flask,render_template
from flask_socketio import SocketIO, emit
from config import SCRIPTS
import subprocess
import eventlet
import shlex
eventlet.monkey_patch()

app = Flask(__name__,template_folder="./")
app.config['SECRET_KEY'] = 'really secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html',scripts = SCRIPTS)

# This is to allow users to invoke scripts from devices which do not support websockets protocal
@app.route('/<int:script_index>')
def run(script_index):
    script = SCRIPTS[int(script_index)]
    process = subprocess.Popen(shlex.split(script), stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    return 'STDOUT:{}'.format(stdout)

@socketio.on('invoked')
def handle_my_custom_event(data):
    emit('started',{})
    script = SCRIPTS[int(data["script_index"])]
    process = subprocess.Popen(shlex.split(script), stdout=subprocess.PIPE,shell=False)
    while True:
        output = process.stdout.readline()
        if output:
            emit('output', {'output':str(output)})
        if output == b'' and process.poll() is not None:
            break
    rc = process.poll()
    process.stdout.close()
    # process.wait()
    emit('terminated', {'return_code':rc})


if __name__ == '__main__':
    socketio.run(app)