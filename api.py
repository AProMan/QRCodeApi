from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
from amzqr import amzqr
import base64

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text', type=str)

NORMALQRCODE_DIR = './qrCode/normal/'


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'API'}


class NormalQRCode(Resource):
    def post(self):
        args = parser.parse_args()
        text = args['text']
        version, level, qr_name = amzqr.run(text, save_dir=NORMALQRCODE_DIR)
        with open(qr_name, 'rb') as f:
            res = base64.b64encode(f.read())
            return {'file': res}, 201


api.add_resource(HelloWorld, '/')
api.add_resource(NormalQRCode, '/NormalQRCode')

if __name__ == '__main__':
    app.run(debug=True)
