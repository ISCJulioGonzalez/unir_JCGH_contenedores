#Este script python es el encargado de la lógica de la aplicación. Específicamente se está creando un servidor web con Flask que muestra el hostname y la fecha actual.

from flask import Flask, render_template
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    host_name = socket.gethostname()
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', 
                         hostname=host_name,
                         time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)