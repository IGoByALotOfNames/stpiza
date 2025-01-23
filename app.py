from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy/<path:url>', methods=['GET'])
def proxy(url):
    response = requests.get(f"https://{url}")
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
