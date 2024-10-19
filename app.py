from flask import Flask
from pyngrok import ngrok

# Create the Flask app
app = Flask(__name__)

@app.route('/htop')
def htop():
    return 'This is the htop endpoint!'

# Start ngrok tunnel
public_url = ngrok.connect(5000)
print('Public URL:', public_url)

# Run the Flask app
app.run(port=5000)
