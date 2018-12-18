#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, send_from_directory
import os


from dxf_playground.data_access.db_handler import DB_Handler
from dxf_playground.dxf import export_dxf




app = Flask(__name__, static_url_path='/assets', static_folder='assets')
root = os.path.dirname(os.path.realpath(__file__)) + "/nest.cache"



@app.route('/nest.cache/<path:filepath>')
def data(filepath):
    return send_from_directory('nest.cache', filepath)

@app.route('/dxf', methods=['GET', 'POST'])
def download():
    try:
        os.chdir(os.path.dirname(__file__))
    except:
        os.chdir(os.getcwd())
        os.getcwd()

    scenario_id = request.form.get('scenario_id')
    bounding_box = [float(i) for i in request.form.get('boundingBox')[1:-1].split(",")]
    uri = export_dxf(scenario_id,bounding_box)

    return uri

@app.route('/inspect', methods=['GET', 'POST'])
def map_inspect2():
    try:
        scenario_id = request.form.get('scenario_id')
    except:
        return -1
    try:
        bounding_box = [float(i) for i in request.form.get('boundingBox')[1:-1].split(",")]
    except:
        return -2
    dbh = DB_Handler()
    return str(len(dbh.queryBoxes(scenario_id,bounding_box)))

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    return 'ping'


@app.route('/close', methods=['GET', 'POST'])
def close():
    shutdown_server()
    return 'Server shutting down...'

from flask import request

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == "__main__":

    app.run('127.0.0.1', 5000, threaded=True, debug=False)
