import threading
from flask import Flask
from System.Core.Core import GlobalObjects
from System.Utils.Utils import print_error, print_info, print_log, print_warning
  
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home_page():
    return f"<h1>{GlobalObjects().computer_name}</h1>"

class Network:
    def __init__(self):
        import random
        port = random.randint(2000, 5000)
        print_info(f"START NETWORK {GlobalObjects().ip}, {port}")
        GlobalObjects().set_network(app, port)
        threading.Thread(target=lambda: app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)).start()

def set_port(port, func):
    app.add_url_rule(f"/{port}", f"port_function_{port}", func)

