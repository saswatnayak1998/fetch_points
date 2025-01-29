from flask import Flask, request, jsonify
from utils import calculate_points
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# In-memory storage for receipts 
receipts_db = {}
points_db = {}

users_db = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        receipt_data = request.get_json()
        
        if not receipt_data:
            return jsonify({'error': 'Invalid receipt data'}), 400
        
        receipt_id = str(uuid.uuid4())
        
        receipts_db[receipt_id] = receipt_data
        
        return jsonify({'id': receipt_id}), 200
    
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/receipts/<string:id>/points", methods = ["GET"])
def get_points(id):
    if id not in receipts_db:
        return "ID doesn't exist"
    points = calculate_points(receipts_db[id])
    points_db[id] = points
    points = points_db[id]
    return points
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Change port to 5001


