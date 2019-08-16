# __init__.py
from flask import Flask, request, jsonify, render_template
from PIL import Image
import os
import sys


def create_app(classifier):
    # Flaskアプリを作成
    app = Flask(__name__)
    @app.route("/")
    def main_page():
        return render_template("index.html")

    @app.route('/', methods=['GET', 'POST'])
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
        # return jsonify({
        #    "result": result
        # })
        return render_template("result.html", result=result)

        # return "result"+result
    if __name__ == "__main__":
        # webサーバー立ち上げ
        app.run()

    return app
