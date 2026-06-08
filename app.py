from flask import Flask, request, jsonify, redirect
import services

app = Flask(__name__)

@app.route("/shorten", methods=["POST"])
def api_shorten_url():
    print("--- INSIDE THE FUNCTION ---") # <-- Add this line
    
    data = request.get_json() or {}
    long_url = data.get("url")
    
    try:
        new_record = services.shorten_url(long_url)
        return jsonify(new_record), 201
    except ValueError as err:
        return jsonify({"error": str(err)}), 400

@app.route("/shorten/<shortcode>", methods=["DELETE"])
def api_delete_url(shortcode):
    success = services.delete_url(shortcode)
    if not success:
        return jsonify({"error": "Short URL not found"}), 404
    
    return "", 204


@app.route("/shorten/<shortcode>", methods=["GET"])
def api_get_url(shortcode):
    record = services.get_shortened_url(shortcode)
    if record is None:
        return jsonify({"error": "Short URL not found"}), 404
    return jsonify(record), 200

@app.route("/<shortcode>", methods=["GET"])
def redirect_to_url(shortcode):
    record = services.get_shortened_url(shortcode)
    if record is None:
        return jsonify({"error": "Short URL not found"}), 404
    
    # This sends an HTTP 302 redirect to the browser using the saved long URL
    return redirect(record["url"])

if __name__ == "__main__":
    app.run(port=8080, debug=True)