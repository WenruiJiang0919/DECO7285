from flask import  request, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app import app
from app.models import User,Recipe,RecipeLike,RecipeComment,RecipeFavorite
from app import db
import time
import datetime
import os
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print(username)
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        access_token = create_access_token(identity=user.username)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'message': f'Hello, {current_user}! This is a protected resource.'})

@app.route('/uploadImg', methods=['POST'])
def upload_image():
    print(request.files)
    if 'image' not in request.files:
        return jsonify({'message': 'No file part'})
    
    file = request.files['image']

    if file.filename == '':
        return jsonify({'message': 'No selected file'})

    if file:
        # Process and save the uploaded image as needed
        # You can use libraries like Pillow or OpenCV to manipulate the image

        # Save the image to a directory or perform other operations
        # For example, save to a directory named 'uploads'
        timestamp = int(time.time())
        # 根据时间戳创建一个格式化的日期时间字符串
        formatted_datetime = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d_%H-%M-%S')
        file_type=file.filename.split('.')[-1]
        save_file_name = formatted_datetime+'.'+file_type
        path = './uploads/' + save_file_name
        file.save(path)

        return jsonify({'imgPath': save_file_name})

image_root_directory = './uploads'

@app.route('/get-image', methods=['GET'])
def get_image():
    image_filename = request.args.get('image_filename')
    # 使用send_from_directory提供图片，从static目录开始查找
    return send_from_directory('../uploads', image_filename)
    
# 菜谱上传接口
@app.route('/upload-recipe', methods=['POST'])
def upload_recipe():
    # current_user = get_jwt_identity()

    # data = request.json
    # data['username'] = current_user  # 将用户名添加到菜谱数据中
    data = request.json
    recipe = Recipe(**data)

    db.session.add(recipe)
    db.session.commit()

    return jsonify({'message': '菜谱上传成功'})

# 菜谱修改接口
@app.route('/update-recipe/<int:recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    data = request.json
    recipe = Recipe.query.get(recipe_id)

    if recipe:
        for key, value in data.items():
            setattr(recipe, key, value)

        db.session.commit()
        return jsonify({'message': '菜谱修改成功'})
    else:
        return jsonify({'message': '菜谱不存在'})

# 菜谱删除接口
@app.route('/delete-recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)

    if recipe:
        db.session.delete(recipe)
        db.session.commit()
        return jsonify({'message': '菜谱删除成功'})
    else:
        return jsonify({'message': '菜谱不存在'})

# 获取特定用户上传的所有菜谱
@app.route('/get-recipes/<string:username>', methods=['POST'])
def get_user_recipes(username):
    recipes = Recipe.query.filter_by(username=username).all()
    recipe_list = []
    data = request.json
    currrent=data['username']
    for recipe in recipes:
        recipe_id=recipe.id
        like = RecipeLike.query.filter_by(user_id=currrent, recipe_id=recipe_id).first()
        favorite = RecipeFavorite.query.filter_by(user_id=currrent, recipe_id=recipe_id).first()
        comments = RecipeComment.query.filter_by(recipe_id=recipe_id).all()

        recipe_data = {
            'recipe_id':recipe_id,
            'recipeName': recipe.recipeName,
            'imgPath': "http://127.0.0.1:5000/get-image?image_filename="+recipe.imgPath,
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
        recipe_list.append(recipe_data)
    return jsonify(recipe_list)
# 获取特定用户上传的所有菜谱
@app.route('/get-all-recipes', methods=['POST'])
def get_all_recipes():
    recipes = Recipe.query.filter_by().all()
    recipe_list = []
    data = request.json
    currrent=data['username']
    for recipe in recipes:
        recipe_id=recipe.id
        like = RecipeLike.query.filter_by(user_id=currrent, recipe_id=recipe_id).first()
        favorite = RecipeFavorite.query.filter_by(user_id=currrent, recipe_id=recipe_id).first()
        comments = RecipeComment.query.filter_by(recipe_id=recipe_id).all()

        recipe_data = {
            'recipe_id':recipe_id,
            'recipeName': recipe.recipeName,
            'imgPath': "http://127.0.0.1:5000/get-image?image_filename="+recipe.imgPath,
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
        recipe_list.append(recipe_data)
    return jsonify(recipe_list)
@app.route('/like-recipe/<int:recipe_id>', methods=['POST'])
def like_recipe(recipe_id):
    data = request.json
    username=data['username'] # 编写获取用户名的函数，根据具体的身份验证方式

    like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    if like:
        return jsonify({'message': '已点赞'})
    else:
        like = RecipeLike(user_id=username, recipe_id=recipe_id)
        db.session.add(like)
        db.session.commit()
        return jsonify({'message': '点赞成功'})
@app.route('/unlike-recipe/<int:recipe_id>', methods=['POST'])
def unlike_recipe(recipe_id):
    data = request.json
    username = data['username']

    like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return jsonify({'message': '取消点赞成功'})
    else:
        return jsonify({'message': '未点赞'}, 404)

# 菜谱收藏接口
@app.route('/favorite-recipe/<int:recipe_id>', methods=['POST'])
def favorite_recipe(recipe_id):
    data = request.json
    username = data['username'] # 编写获取用户名的函数，根据具体的身份验证方式

    favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    if favorite:
        return jsonify({'message': '已收藏'})
    else:
        favorite = RecipeFavorite(user_id=username, recipe_id=recipe_id)
        db.session.add(favorite)
        db.session.commit()
        return jsonify({'message': '收藏成功'})
    
@app.route('/unfavorite-recipe/<int:recipe_id>', methods=['POST'])
def unfavorite_recipe(recipe_id):
    data = request.json
    username = data['username']

    favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return jsonify({'message': '取消收藏成功'})
    else:
        return jsonify({'message': '未收藏'}, 404)
# 菜谱评论接口
@app.route('/comment-recipe/<int:recipe_id>', methods=['POST'])
def comment_recipe(recipe_id):
    data = request.json
    username=data['username'] # 编写获取用户名的函数，根据具体的身份验证方式
    comment = data.get('comment')

    if not comment:
        return jsonify({'message': '评论内容不能为空'}), 400  # 请求数据无效时返回400 Bad Request

    recipe_comment = RecipeComment(user_id=username, recipe_id=recipe_id, comment=comment)
    db.session.add(recipe_comment)
    db.session.commit()
    return jsonify({'message': '评论成功'})

# 获取菜谱基础信息、点赞数、收藏数、评论数、以及当前用户是否点赞、收藏
@app.route('/get-recipe/<int:recipe_id>', methods=['POST'])
def get_recipe(recipe_id):
    data = request.json
    username=data['username'] # 编写获取用户名的函数，根据具体的身份验证方式
    # recipe_id=data['id']
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if not recipe:
        return jsonify({'message': '菜谱不存在'}), 404  # 菜谱不存在时返回404 Not Found

    like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe_id).first()
    comments = RecipeComment.query.filter_by(recipe_id=recipe_id).all()

    recipe_data = {
        'recipe_id':recipe_id,
        'recipeName': recipe.recipeName,
        'imgPath': "http://127.0.0.1:5000/get-image?image_filename="+recipe.imgPath,
        'LengthOfTime': recipe.LengthOfTime,
        'Cuisine': recipe.Cuisine,
        'Ingredients': recipe.Ingredients,
        'Description': recipe.Description,
        'Steps': recipe.Steps,
        'likeCount': RecipeLike.query.filter_by(recipe_id=recipe_id).count(),
        'favoriteCount': RecipeFavorite.query.filter_by(recipe_id=recipe_id).count(),
        'commentCount': len(comments),
        'comments': [{'user_id': comment.user_id, 'comment': comment.comment} for comment in comments],
        'isLiked': bool(like),
        'isFavorite': bool(favorite)
    }

    return jsonify(recipe_data)

@app.route('/get-user-recipes', methods=['GET'])
def get_user_recipesById():
    data = request.json
    username=data.username # 编写获取用户名的函数，根据具体的身份验证方式

    user_recipes = Recipe.query.filter_by(username=username).all()
    user_recipe_data = []

    for recipe in user_recipes:
        recipe_data = {
            'recipeName': recipe.recipeName,
            'imgPath': recipe.imgPath,
            'LengthOfTime': recipe.LengthOfTime,
            'Cuisine': recipe.Cuisine,
            'Ingredients': recipe.Ingredients,
            'Description': recipe.Description,
            'Steps': recipe.Steps,
            'likeCount': RecipeLike.query.filter_by(recipe_id=recipe.id).count(),
            'favoriteCount': RecipeFavorite.query.filter_by(recipe_id=recipe.id).count(),
            'commentCount': RecipeComment.query.filter_by(recipe_id=recipe.id).count()
        }
        
        user_recipe_data.append(recipe_data)

    return jsonify(user_recipe_data)

# 获取用户点赞的菜谱
@app.route('/get-user-liked-recipes', methods=['POST'])
def get_user_liked_recipes():
    data = request.json
    username=data['username'] # 编写获取用户名的函数，根据具体的身份验证方式
    user_liked_recipes = Recipe.query.join(RecipeLike, Recipe.id == RecipeLike.recipe_id).filter(RecipeLike.user_id == username).all()
    user_liked_data = []

    for recipe in user_liked_recipes:
        recipe_id=recipe.id
        like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe_id).first()
        favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe_id).first()
        comments = RecipeComment.query.filter_by(recipe_id=recipe_id).all()

        recipe_data = {
            'recipe_id':recipe_id,
            'recipeName': recipe.recipeName,
            'imgPath': "http://127.0.0.1:5000/get-image?image_filename="+recipe.imgPath,
            'LengthOfTime': recipe.LengthOfTime,
            'Cuisine': recipe.Cuisine,
            'Ingredients': recipe.Ingredients,
            'Description': recipe.Description,
            'Steps': recipe.Steps,
            'likeCount': RecipeLike.query.filter_by(recipe_id=recipe_id).count(),
            'favoriteCount': RecipeFavorite.query.filter_by(recipe_id=recipe_id).count(),
            'commentCount': len(comments),
            'comments': [{'user_id': comment.user_id, 'comment': comment.comment} for comment in comments],
            'isLiked': bool(like),
            'isFavorite': bool(favorite)
        }
        user_liked_data.append(recipe_data)

    return jsonify(user_liked_data)

# 获取用户收藏的菜谱
@app.route('/get-user-favorite-recipes', methods=['POST'])
def get_user_favorite_recipes():
    data = request.json
    username=data['username'] # 编写获取用户名的函数，根据具体的身份验证方式

    user_favorite_recipes = Recipe.query.join(RecipeFavorite, Recipe.id == RecipeFavorite.recipe_id).filter(RecipeFavorite.user_id == username).all()
    user_favorite_data = []

    for recipe in user_favorite_recipes:
        recipe_id=recipe.id
        like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe_id).first()
        favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe_id).first()
        comments = RecipeComment.query.filter_by(recipe_id=recipe_id).all()

        recipe_data = {
            'recipe_id':recipe_id,
            'recipeName': recipe.recipeName,
            'imgPath': "http://127.0.0.1:5000/get-image?image_filename="+recipe.imgPath,
            'LengthOfTime': recipe.LengthOfTime,
            'Cuisine': recipe.Cuisine,
            'Ingredients': recipe.Ingredients,
            'Description': recipe.Description,
            'Steps': recipe.Steps,
            'likeCount': RecipeLike.query.filter_by(recipe_id=recipe_id).count(),
            'favoriteCount': RecipeFavorite.query.filter_by(recipe_id=recipe_id).count(),
            'commentCount': len(comments),
            'comments': [{'user_id': comment.user_id, 'comment': comment.comment} for comment in comments],
            'isLiked': bool(like),
            'isFavorite': bool(favorite)
        }
        user_favorite_data.append(recipe_data)

    return jsonify(user_favorite_data)

# 获取用户评论的菜谱及评论信息
@app.route('/get-user-commented-recipes', methods=['POST'])
def get_user_commented_recipes():
    data = request.json
    username=data['username'] # 编写获取用户名的函数，根据具体的身份验证方式
    user_commented_recipes = Recipe.query.join(RecipeComment, Recipe.id == RecipeComment.recipe_id).filter(RecipeComment.user_id == username).all()
    user_commented_data = []

    for recipe in user_commented_recipes:
        recipe_id=recipe.id
        like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe_id).first()
        favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe_id).first()
        comments = RecipeComment.query.filter_by(recipe_id=recipe_id,user_id=username).all()
        comments_all = RecipeComment.query.filter_by(recipe_id=recipe_id).all()
        recipe_data = {
            'recipe_id':recipe_id,
            'recipeName': recipe.recipeName,
            'imgPath': "http://127.0.0.1:5000/get-image?image_filename="+recipe.imgPath,
            'LengthOfTime': recipe.LengthOfTime,
            'Cuisine': recipe.Cuisine,
            'Ingredients': recipe.Ingredients,
            'Description': recipe.Description,
            'Steps': recipe.Steps,
            'likeCount': RecipeLike.query.filter_by(recipe_id=recipe_id).count(),
            'favoriteCount': RecipeFavorite.query.filter_by(recipe_id=recipe_id).count(),
            'commentCount': len(comments_all),
            'comments': [{'user_id': comment.user_id, 'comment': comment.comment} for comment in comments],
            'isLiked': bool(like),
            'isFavorite': bool(favorite)
        }
        user_commented_data.append(recipe_data)

    return jsonify(user_commented_data)

# 获取菜谱的评论信息
@app.route('/get-recipe-comments/<int:recipe_id>', methods=['GET'])
def get_recipe_comments(recipe_id):
    comments = RecipeComment.query.filter_by(recipe_id=recipe_id).all()
    comment_data = [{'user_id': comment.user_id, 'comment': comment.comment} for comment in comments]

    return jsonify(comment_data)

@app.route('/get-recipes-grouped-by-cuisine', methods=['POST'])
def get_recipes_grouped_by_cuisine():
    data = request.json
    print(data)
    username=data['username'] # 编写获取用户名的函数，根据具体的身份验证方式

    # 获取所有的菜谱
    all_recipes = Recipe.query.all()

    # 创建一个字典，用于按Cuisine分组
    recipes_grouped_by_cuisine = {}

    for recipe in all_recipes:
        # 检查当前用户是否点赞
        user_like = RecipeLike.query.filter_by(user_id=username, recipe_id=recipe.id).first()
        is_liked = bool(user_like)

        # 构建菜谱信息
        recipe_data = {
            'recipe_id':recipe.id,
            'recipeName': recipe.recipeName,
            'imgPath': "http://127.0.0.1:5000/get-image?image_filename="+recipe.imgPath,
            'LengthOfTime': recipe.LengthOfTime,
            'Cuisine': recipe.Cuisine,
            'Ingredients': recipe.Ingredients,
            'Description': recipe.Description,
            'Steps': recipe.Steps,
            'isLiked': is_liked  # 当前用户是否点赞
        }
        user_favorite = RecipeFavorite.query.filter_by(user_id=username, recipe_id=recipe.id).first()
        recipe_data['userFavorited'] = bool(user_favorite)

        # 按Cuisine分组，将菜谱信息添加到相应的分组
        if recipe.Cuisine in recipes_grouped_by_cuisine:
            recipes_grouped_by_cuisine[recipe.Cuisine].append(recipe_data)
        else:
            recipes_grouped_by_cuisine[recipe.Cuisine] = [recipe_data]

    return jsonify(recipes_grouped_by_cuisine)

    