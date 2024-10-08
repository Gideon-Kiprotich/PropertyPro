from flask import Flask, request
import os
import subprocess

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Run the deploy.sh script when a webhook is received
        subprocess.call(['/var/www/html/your_project/deploy.sh'])
        return 'Webhook received!', 200
    else:
        return 'Not allowed', 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
