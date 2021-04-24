from flask import Blueprint, json, request, jsonify, abort
from ..db.model import db
import os

routes_blueprint = Blueprint("routes_blueprint",
                             __name__)

@routes_blueprint.route("/status", methods=["GET"])
def status():
    message = {"healthy": True}
    return jsonify(message)

@routes_blueprint.route("/query", methods=["GET"])
def get_suggestions():
    query_string = request.args.get("string")
    parts = query_string.split(",")
    print(parts)
    if len(parts) > 3 or len(parts) == 3:
        w1, w2 = parts[-2].lower(), parts[-1].lower()
        res = db.engine.execute(f'''
        SELECT w3, score from trigrams
        where w1 = '{w1}' and w2 = '{w2}'
        order by score desc
        limit 5;
        ''')
        suggestions = [(i.w3, i.score) for i in res]
        return jsonify({"suggestions":suggestions})
      
    if len(parts) == 2:
        w1, w2 = parts[0].lower(), parts[1].lower()
        res = db.engine.execute(f'''
        SELECT w3, score from trigrams
        where w1 = '{w1}' and w2 = '{w2}'
        order by score desc
        limit 5;
        ''')
        suggestions = [(i.w3, i.score) for i in res]
        return jsonify({"suggestions":suggestions})
    
    if len(parts) == 1:
        w1 = parts[0].lower()
        res = db.engine.execute(f'''SELECT w2, score from bigrams
         where w1 ='{w1}' 
         order by score desc limit 5;
        ''')
        suggestions = [(i.w2,i.score) for i in res]
        return jsonify({"suggestions":suggestions})
    if len(parts) == 0:
        abort(400)
