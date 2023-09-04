from flask import Flask, render_template, request

app = Flask(__name__)

# 01.首頁
@app.route('/')
def index():
    return render_template('index.html')

# 02.關於我們
@app.route('/about')
def about():
    return render_template('about.html')

# 03.產品與技術服務
@app.route('/service')
def service():
    return render_template('service.html')
# 03-1.網站設計
@app.route('/service/web_design')
def web_design():
    return render_template('service/S_WebDesign.html')
# 03-2.企業資訊系統
@app.route('/service/erp')
def erp():
    return render_template('service/S_ERP.html')
# 03-3.影像安防偵測
@app.route('/service/dynamic_detection')
def dynamic_detection():
    return render_template('service/S_DynamicDetection.html')
# 03-4.缺陷檢測系統AOI
@app.route('/service/AOI')
def AOI():
    return render_template('service/S_AOI.html')
# 03-5.光學盤點系統
@app.route('/service/Optical_Inventory')
def Optical_Inventory():
    return render_template('service/S_OpticalInventory.html')
# 03-6.AI預測系統
@app.route('/service/AI_Prediction')
def AI_Prediction():
    return render_template('service/S_AIPrediction.html')

# 04.線上服務
@app.route('/free_func')
def free_func():
    return render_template('free_func.html')
# 03-1.網站設計
@app.route('/free_func/promote_word')
def promote_word():
    return render_template('service/promote_word.html')

# 05.聯絡我們
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    