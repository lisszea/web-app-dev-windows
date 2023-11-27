from flask import Flask

def create_app(test_config=None):   
    app = Flask(__name__, instance_relative_config=True)

    from modules.CLIENTE import bp as bpcliente
    from modules.MASCOTA import bp as bpmascota
 
    app.register_blueprint(bpcliente)
    app.register_blueprint(bpmascota) 

    return app