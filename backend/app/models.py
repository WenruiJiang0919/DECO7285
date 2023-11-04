from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

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

