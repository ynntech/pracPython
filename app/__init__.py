# __init__.py
from flask import Flask, request, jsonify
from PIL import Image


def create_app(classifier):
    # Flaskアプリを作成
    app = Flask(__name__)

    # POST /　に対応する関数を定義
    @app.route('/', methods=['POST'])
    def predict():
        # 受け取ったハンドラを取得
        img_file = request.files['img']

        # ファイルを空かどうかチェック
        if img_file.filename == "":
            return "BadRequest", 400

        # PILを使用して画像ファイルを読み込む
        img = Image.open(img_file)

        # 識別モデルを利用してここでタコスかぶりとーかを予測
        result = classifier.predict(img)

        # 結果をJSONに。
        return jsonify({
            "result": result
        })

    return app
