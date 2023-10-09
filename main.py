import io
from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from flask_cors import CORS

app = Flask(__name__)
CORS(app, allow_methods=["GET", "POST", "PUT", "DELETE"])

@app.route('/purchase', methods=['POST'])
def purchase():
    params = request.get_json()

    generate_proof_of_purchase(params['formData'])

    image = open("/Users/sheep/project/marsbuysell_client/src/static/result.png", 'rb').read()
    image, 200, {'Content-Type': 'image/jpeg'}
    return send_file(
        io.BytesIO(image),
        mimetype='image/jpeg',
        as_attachment=True,
        download_name='image.jpg'
    )

FONT_PATH = '/System/Library/Fonts/ヒラギノ明朝 ProN.ttc'

def generate_proof_of_purchase(params):
    print(params)
    # 背景画像の読み込み
    background = Image.open("template4.png")
    # background = Image.open("template3.jpg")

    # フォントの設定
    font_size = 50
    # font = ImageFont.load_default()
    font = ImageFont.truetype(FONT_PATH, font_size)
    draw = ImageDraw.Draw(background)

    # 文字列を描画
    # text = f"Congratulations\n{'hoge'}\nYou are now a Jedi Knight"
    draw.text((500, 300), '購入証明', font=font, fill=(1, 1, 1))

    font_size = 50
    font = ImageFont.truetype(FONT_PATH, font_size)
    draw.text((400, 500), params['nameAlphabet'], font=font, fill=(1, 1, 1))

    font_size = 50
    font = ImageFont.truetype(FONT_PATH, font_size)
    tmp = 'あなたは以下の土地の\n所有者となりました'
    draw.text((400, 700), tmp, font=font, fill=(1, 1, 1))

    font_size = 30
    font = ImageFont.truetype(FONT_PATH, font_size)
    draw.text((400, 1000), params['placeName'], font=font, fill=(1, 1, 1))

    # 画像を保存
    background.save("/Users/sheep/project/marsbuysell_client/src/static/result.png")

if __name__ == '__main__':
    app.run(debug=True)
