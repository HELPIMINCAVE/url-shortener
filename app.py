from flask import Flask, request, jsonify
import services

app = Flask(__name__)


@app.route("/shorten", methods=["POST"])
def api_shorten_url():
    data = request.get_json() or {}
    long_url = data.get("url")
    
    try:
        new_record = services.shorten_url(long_url)
        return jsonify(new_record), 201
    except ValueError as err:
        return jsonify({"error": str(err)}), 400

if __name__ == "__main__":
    app.run(port=8000, debug=True)