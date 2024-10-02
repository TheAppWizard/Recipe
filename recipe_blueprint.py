from flask import Blueprint, request, jsonify , render_template
import pandas as pd
from datetime import datetime

recipe_blueprint = Blueprint('recipe_blueprint', __name__,template_folder='doc')

FILE_PATH = 'data/recipe.xlsx'
COLUMNS = ['dish_id', 'dish_name', 'description', 'spice', 'prep_time', 'views', 'rating', 'votes', 'serves', 'dietry_info', 'cook_time', 'ingredients', 'instructions', 'image_url']
UPDATABLE_COLUMNS = ['dish_name', 'description', 'spice', 'prep_time', 'serves', 'dietry_info', 'cook_time', 'ingredients', 'instructions', 'image_url']

def read_excel():
    return pd.read_excel(FILE_PATH, usecols=COLUMNS)

def write_excel(df):
    df.to_excel(FILE_PATH, index=False, columns=COLUMNS)

@recipe_blueprint.route('/doc')
def doc():
     return render_template('doc.html')

@recipe_blueprint.route('/recipes', methods=['GET'])
def get_recipes():
    df = read_excel()
    return jsonify(df.to_dict(orient='records'))

@recipe_blueprint.route('/recipe/<int:dish_id>', methods=['GET'])
def get_recipe(dish_id):
    df = read_excel()
    recipe = df[df['dish_id'] == dish_id].to_dict(orient='records')
    return jsonify(recipe[0] if recipe else {"error": "Recipe not found"}), 200 if recipe else 404

@recipe_blueprint.route('/recipe', methods=['POST'])
def create_recipe():
    new_recipe = request.json
    df = read_excel()
    
    for col in COLUMNS:
        if col not in new_recipe and col not in ['dish_id', 'views', 'rating', 'votes']:
            return jsonify({"error": f"Missing required field: {col}"}), 400
    
    new_recipe['dish_id'] = int(df['dish_id'].max() + 1) if not df.empty else 1
    new_recipe['views'] = 0
    new_recipe['rating'] = 0
    new_recipe['votes'] = 0
    
    df = pd.concat([df, pd.DataFrame([new_recipe])], ignore_index=True)
    write_excel(df)
    return jsonify({"message": "Recipe created successfully", "recipe": new_recipe}), 201

@recipe_blueprint.route('/recipe/<int:dish_id>', methods=['PUT'])
def update_recipe(dish_id):
    df = read_excel()
    if dish_id not in df['dish_id'].values:
        return jsonify({"error": "Recipe not found"}), 404
    
    updated_recipe = request.json
    for key in updated_recipe:
        if key not in UPDATABLE_COLUMNS:
            return jsonify({"error": f"Invalid or non-updatable field: {key}"}), 400
    
    df.loc[df['dish_id'] == dish_id, updated_recipe.keys()] = updated_recipe.values()
    write_excel(df)
    updated_row = df[df['dish_id'] == dish_id].to_dict(orient='records')[0]
    return jsonify({"message": "Recipe updated successfully", "recipe": updated_row}), 200

@recipe_blueprint.route('/recipe/<int:dish_id>', methods=['DELETE'])
def delete_recipe(dish_id):
    df = read_excel()
    if dish_id not in df['dish_id'].values:
        return jsonify({"error": "Recipe not found"}), 404
    
    df = df[df['dish_id'] != dish_id]
    write_excel(df)
    return jsonify({"message": "Recipe deleted successfully"}), 200