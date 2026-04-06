from flask import Flask, request, jsonify
from rag_pipeline import recommend_policy

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    result = recommend_policy(user_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
