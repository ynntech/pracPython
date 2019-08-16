# __init__.py
from flask import Flask, request, jsonify, render_template
from PIL import Image
import os
import sys


def create_app(classifier):
    # Flaskアプリを作成
    app = Flask(__name__)

    @app.route('/')
    def main_page():
        print("POST GET！！！")
        print("mainがよばれてるよ！！！")
        return render_template("index.html", result="なにもなし")

    @app.route('/', methods=["GET", "POST"])
    def predict():
        flag = '0'
        print("flagは" + flag)
        if request.method == 'POST':
            print("POST受け取り")
            # 受け取ったハンドラを取得
            img_file = request.files['img']

            # ファイルを空かどうかチェック
            if img_file.filename == "":
                return "BadRequest", 400

            # PILを使用して画像ファイルを読み込む
            img = Image.open(img_file)

            # 識別モデルを利用してここでタコスかぶりとーかを予測
            result = classifier.predict(img)
            print("flagは" + flag)
            flag = '1'
            print("flagがかわった" + flag)

        if flag == '0':
            print("さいごflagは" + flag)
            return render_template("index.html", result="なにもなし2")
        else:
            print("さいごflagは" + flag)
            print("resultは"+result)
            return render_template("index.html", result=result)

            # 結果をJSONに。
            # return jsonify({
            #    "result": result
            # })

            # return "result"+result

    if __name__ == "__main__":
        # webサーバー立ち上げ
        print("よばれたよ")
        app.run(debug=True)

    return app
