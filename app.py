from flask import Flask, request, jsonify
from flasgger import Swagger
from profanity import mask_profanity

app = Flask(__name__)
# Initialize Flasgger
swagger = Swagger(app)

@app.route("/")
def index():
    """
    Welcome Endpoint
    ---
    responses:
      200:
        description: Returns a welcome message
    """
    return "WELCOME TO MY WEB DEVELOPMENT JOURNAL API!"

@app.route("/mask", methods=['POST'])
def mask_text():
    """
    Mask profanity in input text.
    Preserves the first letter, masks the rest with *.
    Case-insensitive banned words: damn, hell, crap.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - text
          properties:
            text:
              type: string
              description: The text you want to filter
              example: "This is a damn test."
    responses:
      200:
        description: Successfully masked text
        schema:
          type: object
          properties:
            masked_text:
              type: string
              example: "This is a d*** test."
      422:
        description: Invalid input
    """
    data = request.get_json()
    
    if not data or 'text' not in data or data['text'] is None:
        return jsonify({"detail": "Invalid input: text cannot be None"}), 422
        
    try:
        masked = mask_profanity(data['text'])
        return jsonify({"masked_text": masked}), 200
    except ValueError as e:
        return jsonify({"detail": str(e)}), 422

# This block ensures the server stays running!
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)