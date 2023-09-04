from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# 01.首頁
@views.route('/')
def index():
    return render_template('index.html')

# 02.關於我們
@views.route('/about')
def about():
    return render_template('about.html')

# 03.產品與技術服務
@views.route('/service')
def service():
    return render_template('service.html')
# 03-1.網站設計
@views.route('/service/web_design')
def web_design():
    return render_template('service/S_WebDesign.html')
# 03-2.企業資訊系統
@views.route('/service/erp')
def erp():
    return render_template('service/S_ERP.html')
# 03-3.影像安防偵測
@views.route('/service/dynamic_detection')
def dynamic_detection():
    return render_template('service/S_DynamicDetection.html')
# 03-4.缺陷檢測系統AOI
@views.route('/service/AOI')
def AOI():
    return render_template('service/S_AOI.html')
# 03-5.光學盤點系統
@views.route('/service/Optical_Inventory')
def Optical_Inventory():
    return render_template('service/S_OpticalInventory.html')
# 03-6.AI預測系統
@views.route('/service/AI_Prediction')
def AI_Prediction():
    return render_template('service/S_AIPrediction.html')

# 04.聯絡我們
@views.route('/contact')
def contact():
    return render_template('contact.html')

