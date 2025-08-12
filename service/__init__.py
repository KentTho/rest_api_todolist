from flask import Flask
# Khởi tạo Flask app
app = Flask(__name__)
app.debug = True  # Bật chế độ debug để dễ theo dõi lỗi


from service.todoRest import blueprint
app.register_blueprint(blueprint)