from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'  # 使用SQLite数据库，你可以根据需要更改数据库类型和连接信息
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

class RecipeLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    user_id = db.Column(db.String(80))

class RecipeFavorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    user_id = db.Column(db.String(80))

class RecipeComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    user_id = db.Column(db.String(80))
    comment = db.Column(db.Text)

# 菜谱点赞接口
@app.route('/like-recipe/<int:recipe_id>', methods=['POST'])
def like_recipe(recipe_id):
    token = request.headers.get('Authorization')  # 假设token作为Authorization请求头发送
    if not token:
        return jsonify({'message': '未提供有效的token'}), 401  # 未提供token时返回401 Unauthorized

    username = get_username_from_token(token)  # 编写获取用户名的函数，根据具体的身份验证方式

    if not username:
        return jsonify({'message': '无法验证token'}), 401  # 无法验证token时返回401 Unauthorized

    like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    if like:
        return jsonify({'message': '已点赞'})
    else:
        like = RecipeLike(user_id=username, recipe_id=recipe_id)
        db.session.add(like)
        db.session.commit()
        return jsonify({'message': '点赞成功'})

# 菜谱收藏接口
@app.route('/favorite-recipe/<int:recipe_id>', methods=['POST'])
def favorite_recipe(recipe_id):
    token = request.headers.get('Authorization')  # 假设token作为Authorization请求头发送
    if not token:
        return jsonify({'message': '未提供有效的token'}), 401  # 未提供token时返回401 Unauthorized

    username = get_username_from_token(token)  # 编写获取用户名的函数，根据具体的身份验证方式

    if not username:
        return jsonify({'message': '无法验证token'}), 401  # 无法验证token时返回401 Unauthorized

    favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    if favorite:
        return jsonify({'message': '已收藏'})
    else:
        favorite = RecipeFavorite(user_id=username, recipe_id=recipe_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify({'message': '收藏成功'})

# 菜谱评论接口
@app.route('/comment-recipe/<int:recipe_id>', methods=['POST'])
def comment_recipe(recipe_id):
    token = request.headers.get('Authorization')  # 假设token作为Authorization请求头发送
    if not token:
        return jsonify({'message': '未提供有效的token'}), 401  # 未提供token时返回401 Unauthorized

    username = get_username_from_token(token)  # 编写获取用户名的函数，根据具体的身份验证方式

    if not username:
        return jsonify({'message': '无法验证token'}), 401  # 无法验证token时返回401 Unauthorized

    data = request.json
    comment = data.get('comment')

    if not comment:
        return jsonify({'message': '评论内容不能为空'}), 400  # 请求数据无效时返回400 Bad Request

    recipe_comment = RecipeComment(user_id=username, recipe_id=recipe_id, comment=comment)
    db.session.add(recipe_comment)
    db.session.commit()
    return jsonify({'message': '评论成功'})

# 获取菜谱基础信息、点赞数、收藏数、评论数、以及当前用户是否点赞、收藏
@app.route('/get-recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    token = request.headers.get('Authorization')  # 假设token作为Authorization请求头发送
    username = get_username_from_token(token) if token else None  # 编写获取用户名的函数，根据具体的身份验证方式

    recipe = Recipe.query.get(recipe_id)

    if not recipe:
        return jsonify({'message': '菜谱不存在'}), 404  # 菜谱不存在时返回404 Not Found

    like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    comments = RecipeComment.query.filter_by(recipe_id=recipe_id).all()

    recipe_data = {
        'recipeName': recipe.recipeName,
        'imgPath': recipe.imgPath,
        'LengthOfTime': recipe.LengthOfTime,
        'Cuisine': recipe.Cuisine,
        'Ingredients': recipe.Ingredients,
        'Description': recipe.Description,
        'Steps': recipe.Steps,
        'likeCount': RecipeLike.query.filter_by(recipe_id=recipe_id).count(),
        'favoriteCount': RecipeFavorite.query.filter_by(recipe_id=recipe_id).count(),
        'commentCount': len(comments),
        'comments': [comment.comment for comment in comments],
        'isLiked': bool(like),
        'isFavorite': bool(favorite)
    }

    return jsonify(recipe_data)

# 编写获取用户名的函数，根据具体的身份验证方式
def get_username_from_token(token):
    # 在实际应用中，根据token验证用户身份并返回用户名
    # 这里只是一个示例，你需要根据你的身份验证机制进行实际实现
    return 'example_username'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
