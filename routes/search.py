from flask import Blueprint, jsonify, request
from flask_login import login_required
from ..main import ontology

search_routes = Blueprint('search',__name__)

# Ruta para la búsqueda de archivos
@search_routes.route('/search', methods=['POST'])
@login_required
def search():
    query = request.get_json()['query']
    results = ontology.search(query) # Realizar la búsqueda ontológica en Protegé
    return jsonify({'results': results})