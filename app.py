import os
from flask import Flask

app = Flask(__name__)

@app.route("/q/<message>")
def get_response(message):
  if message == "hello":
    return "hi"
  return "I don't understand."

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
