from flask import jsonify, request, render_template
from .Blockchain import Blockchain
from .Transaction import Transaction

blockchain = Blockchain()

def init_routes(app):
    @app.route('/', methods=['GET'])
    def home():
        return render_template('index.html')

    @app.route('/blockchain', methods=['GET'])
    def blockchain_page():
        return render_template('blockchain.html')

    @app.route('/mining', methods=['GET'])
    def mining_page():
        return render_template('mining.html')

    @app.route('/add_block/<data>', methods=['GET'])
    def add_block(data):
        block = blockchain.add_block(data)
        return jsonify(block.__dict__)

    @app.route('/chain', methods=['GET'])
    def get_chain():
        return jsonify(blockchain.get_chain())

    @app.route('/add_transaction', methods=['POST'])
    def add_transaction():
        data = request.get_json()
        transaction = Transaction(data['sender'], data['receiver'], data['amount'])
        blockchain.add_transaction(transaction)
        return jsonify(transaction.to_dict()), 201

    @app.route('/pending_transactions', methods=['GET'])
    def get_pending_transactions():
        return jsonify(blockchain.get_pending_transactions())

    @app.route('/transactions', methods=['GET'])
    def transaction_page():
        return render_template('transaction.html')
