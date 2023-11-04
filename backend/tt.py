from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'  # 替换为你的MySQL连接信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    recipeName = db.Column(db.String(200))
    imgPath = db.Column(db.String(200))
    LengthOfTime = db.Column(db.String(50))
    Cuisine = db.Column(db.String(50))
    Ingredients = db.Column(db.Text)
    Description = db.Column(db.Text)
    Steps = db.Column(db.Text)

# 菜谱上传接口
@app.route('/upload-recipe', methods=['POST'])
def upload_recipe():
    token = request.headers.get('Authorization')  # 假设token作为Authorization请求头发送
    if not token:
        return jsonify({'message': '未提供有效的token'}), 401  # 未提供token时返回401 Unauthorized

    username = get_username_from_token(token)  # 编写获取用户名的函数，根据具体的身份验证方式

    if not username:
        return jsonify({'message': '无法验证token'}), 401  # 无法验证token时返回401 Unauthorized

    data = request.json
    data['username'] = username  # 将用户名添加到菜谱数据中
    recipe = Recipe(**data)

    db.session.add(recipe)
    db.session.commit()

    return jsonify({'message': '菜谱上传成功'})

# 编写获取用户名的函数，根据具体的身份验证方式
def get_username_from_token(token):
    # 在实际应用中，根据token验证用户身份并返回用户名
    # 这里只是一个示例，你需要根据你的身份验证机制进行实际实现
    return 'example_username'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
