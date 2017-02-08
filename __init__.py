from openedoo.core.libs import blueprint
from flask import jsonify

module_namaku = blueprint('module_namaku', __name__)

@module_namaku.route('/', methods=['GET'])
def index():
    namaku = {"nama": "Dwi purnomo"}
    return jsonify(namaku)
