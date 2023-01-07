# https://flask.palletsprojects.com/en/2.1.x/quickstart/

"""
Actualizar Flask:

conda activate base
conda remove flask
conda install -c conda-forge flask=2.1.3
"""
import os
import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
from flask import Flask, request, jsonify
from flask import send_from_directory

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(error):
    print("Exception : ", type(error))
    if isinstance(error, FileNotFoundError):
        return 'Archivo no encontrado', 400

    return error
    
    
@app.route('/airports', methods=['GET'])
def filter_bolivian_airports():

    return jsonify({})
    
    
@app.route('/file/<path:name>', methods=['GET'])
def get(name):
    path_file = os.path.join(".", "maps", name)
    print(path_file)
    if not os.path.exists(path_file):
        raise FileNotFoundError()
        
    return send_from_directory(os.path.join(".", "maps"), name, as_attachment=False)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)