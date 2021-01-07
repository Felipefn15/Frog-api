import flask_restful as restful
from flask import jsonify
from flask import request
import json 
import numpy as np

class Order(restful.Resource):

    def get(self):
        type = request.args.get('type')
        f = open('data\data.json', encoding='utf-8')
        data = json.load(f) 
        if type != 'none':
            value = []
            for item in data['products']:
                value.append(item[type])
            results = [x for x in data['products'] if x[type] == max(value)]
        else:
            results = data['products'] 
        print(results)
        return jsonify({
             "data": results
        })