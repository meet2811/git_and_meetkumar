from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# CORS is required because the frontend (port 3000) will make requests to the backend (port 5000)
CORS(app) 

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name', 'Unknown')
    email = data.get('email', 'Unknown')
    
    # In a real app, you would process or save this data here
    return jsonify({
        "status": "success", 
        "message": f"Hello {name}, your email ({email}) was successfully received by the Flask backend!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)