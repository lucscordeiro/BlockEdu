from flask import jsonify, request, render_template
from .Blockchain import Blockchain

blockchain = Blockchain()

def init_routes(app):
    
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

    @app.route('/add_block/<data>', methods=['GET'])
    def add_block(data):
        block = blockchain.add_block(data)
        return jsonify(block.__dict__)

    @app.route('/chain', methods=['GET'])
    def get_chain():
        return jsonify(blockchain.get_chain())
