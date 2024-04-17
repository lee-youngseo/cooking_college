from flask import Flask, render_template, request, jsonify, Markup, redirect, url_for

app = Flask(__name__)

recipe_data = {
   '1': {
      'name': 'Feta Salad',
      'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/06/Greek-Brown-and-Wild-Rice-Bowls_EXPS_SDAS18_204870_C03_28__10b-3.jpg'
   },
   '2': {
      'name': 'Glazed Squash',
      'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/01/Coconut-Acorn-Squash_exps149543_TH132767C04_25_1bC_RMS.jpg'
   },
   '3': {
      'name': 'Garlic Scallion Ramen',
      'image': 'https://www.kitchentreaty.com/wp-content/uploads/2020/01/super-simple-miso-ramen-5-420x560.jpg',
      'supplies': {
         '1':{
            'name': 'Pot',
            'image': 'https://www.ikea.com/us/en/images/products/hemkomst-pot-with-lid-stainless-steel-glass__1083743_pe859078_s5.jpg'
         },
         '2':{
            'name': 'Bowl',
            'image': 'https://www.heathceramics.com/cdn/shop/products/large-serving-bowl-opaque-white-heath-ceramics_108-05.jpg'
         },
         '3':{
            'name': 'Kitchen Knife',
            'image': 'https://www.opinel-usa.com/cdn/shop/products/Les-Forges-1890-8-Chef-Knife-Large-Kitchen-Knife_2000x.jpg'
         },
         '4':{
            'name': 'Cutting Board',
            'image': 'https://www.buildmat.com.au/cdn/shop/products/buildmat-kitchen-accessories-buildmat-wooden-chopping-board-sn101088-36435068059868_800x.png'
         }
      },
      'ingredients': {
         '1': {
            'name': 'Instant Noodles',
            'image': 'https://images.heb.com/is/image/HEBGrocery/prd-medium/001616095.jpg'
         },
         '2': {
            'name': 'Soy Sauce',
            'image': 'https://www.nikankitchen.com/Images/Products/kikkoman-shoyu-soy-sauce-150ml.png'
         },
         '3': {
            'name': 'Garlic',
            'image': 'https://i5.walmartimages.com/seo/Garlic-Bulb-Fresh-Whole-Each_a4f114d9-93ab-4d39-a8d6-9170536f57a9.f9f8e58c8e3e74894050c7c2267437e3.jpeg'
         },
         '4': {
            'name': 'Scallions',
            'image': 'https://www.purveyd.com/cdn/shop/products/SCALLION.jpg'
         },
         '5': {
            'name': 'Peanut Butter',
            'image': 'https://media.cdn.kaufland.de/product-images/1024x1024/6e563e9c36fe0c6dd539e823ec38e0ad.jpg'
         },
      },
      'instructions': {
         '1': {
            'step': 'Boil water in a pot and cook the noodles according to the package instructions.',
            'image': 'https://images.saymedia-content.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:eco%2Cw_1200/MjAyMjMxNzQ3NDk5MjcxMTgw/shutterstock_1816629980.jpg'
         },
         '2': {
            'step': 'Drain the noodles and set aside.',
            'image': 'https://media.blueapron.com/recipes/40165/recipe_steps/96835/1691526712-48-0019-5460/FP_Ramen_Stockpot_Web.jpg?width=512'
         },
         '3': {
            'step': 'On a cutting board, mince the garlic and chop the scallions.',
            'image': 'https://images.cutco.com/learn/2018/slice-green-onion-l.jpg'
         },
         '4': {
            'step': 'In a bowl, add the soy sauce, peanut butter, garlic, and scallions. Mix well.',
            'image': 'https://pinchofyum.com/wp-content/uploads/Peanut-Sauce-3.jpg'
         },
         '5': {
            'step': 'Add the noodles to the bowl and mix well. Enjoy',
            'image': 'https://i0.wp.com/thefoodiediaries.co/wp-content/uploads/2022/01/img_1427.jpg'
         },
      }
      
      }
   }


@app.route('/')
def home():
   return render_template('home_page.html')  

@app.route('/recipes')
def recipes():
   return render_template('recipes.html')

@app.route('/quizzes')
def quizzes():
   return render_template('quizzes.html')

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
   return jsonify(recipe_data)

@app.route('/learn_recipe/<recipe_id>')
def recipe(recipe_id):
   return render_template('recipe.html', recipe_id = recipe_id, name = recipe_data[recipe_id]['name'], image = recipe_data[recipe_id]['image'])
   #return render_template('supplies_ingredients.html', recipe_id = recipe_id)

@app.route('/learn_recipe/<recipe_id>/supplies')
def supplies(recipe_id):
   return render_template('supplies_ingredients.html', recipe_id = recipe_id, supplies = recipe_data[recipe_id]['supplies'], key='Supplies')

@app.route('/learn_recipe/<recipe_id>/ingredients')
def ingredients(recipe_id):
   return render_template('supplies_ingredients.html', recipe_id = recipe_id, ingredients = recipe_data[recipe_id]['ingredients'], key='Ingredients')

@app.route('/get_supplies_ingredients/<recipe_id>', methods=['GET'])
def get_supplies_ingredients(recipe_id):
    return jsonify(recipe_data[recipe_id])

@app.route('/learn_recipe/<recipe_id>/instructions')
def instructions(recipe_id):
   return render_template('instructions.html', recipe_id = recipe_id, instructions = recipe_data[recipe_id]['instructions'])

@app.route('/get_instructions/<recipe_id>', methods=['GET'])
def get_instructions(recipe_id):
    return jsonify(recipe_data[recipe_id]['instructions'])

if __name__ == '__main__':
   app.run(debug = True)