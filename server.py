from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

recipe_data = {
   '1': {
      'name': 'Feta Salad',
      'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/06/Greek-Brown-and-Wild-Rice-Bowls_EXPS_SDAS18_204870_C03_28__10b-3.jpg',
      'supplies': {
         '1':{
            'name': 'Cutting Board',
            'image': 'https://www.buildmat.com.au/cdn/shop/products/buildmat-kitchen-accessories-buildmat-wooden-chopping-board-sn101088-36435068059868_800x.png'
         },
         '2':{
            'name': 'Bowl',
            'image': 'https://www.heathceramics.com/cdn/shop/products/large-serving-bowl-opaque-white-heath-ceramics_108-05.jpg'
         },
         '3':{
            'name': 'Kitchen Knife',
            'image': 'https://www.opinel-usa.com/cdn/shop/products/Les-Forges-1890-8-Chef-Knife-Large-Kitchen-Knife_2000x.jpg'
         },
      },
      'ingredients': {
         '1': {
            'name': 'Ready to Serve Rice',
            'image': 'https://www.goya.com/media/8420/brown-heat-serve-rice.png?width=274'
         },
         '2': {
            'name': 'Greek Vinaigrette',
            'image': 'https://images.heb.com/is/image/HEBGrocery/000081144-1'
         },
         '3': {
            'name': 'Feta Cheese',
            'image': 'https://target.scene7.com/is/image/Target/GUEST_c63a48a6-c099-4522-a0bb-8932bf34a521?wid=488&hei=488&fmt=pjpeg'
         },
         '4': {
            'name': 'Cherry Tomatoes',
            'image': 'https://target.scene7.com/is/image/Target/GUEST_95c07dd1-974a-436b-8faa-808f100e7950?wid=488&hei=488&fmt=pjpeg'
         },
         '5': {
            'name': 'Avocadoes',
            'image': 'https://cdn.britannica.com/72/170772-050-D52BF8C2/Avocado-fruits.jpg'
         },
         '6':{
            'name': 'Black Olives',
            'image': "https://m.media-amazon.com/images/S/assets.wholefoodsmarket.com/PIE/product/64624093c4228d2fcce84d1e_99482416843-2023-cen-ecommerce-directship-ripelargepittedolives.jpg"
         }
      },
      'instructions': {
         '1': {
            'step': 'On a plate (or cutting board), cut the avocado and cherry tomatoes.',
            'image': 'https://feelgoodfoodie.net/wp-content/uploads/2023/10/How-to-Cut-an-Avocado-TIMG.jpg'
         },
         '2': {
            'step': 'In a microwave-safe bowl, combine rice mix and 2 tablespoons vinaigrette. Cover and cook on high until heated through, about 2 minutes.',
            'image': 'https://cdn.apartmenttherapy.info/image/upload/f_auto,q_auto:eco,c_fill,g_center,w_730,h_487/k%2FPhoto%2FLifestyle%2F2021-04-Taste-Test-Microwavable-White-Rice%20%2FKitchn-2021-Microwave-Rice-Taste-Test-1'
         },
         '3': {
            'step': 'Divide between 2 bowls. Top with avocado, tomatoes, cheese, olives, remaining dressing and, if desired, parsley.',
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVU5iTKckCfI0tZS0USg_g5kO_9L6fk4fjg7sqv5gA6VtB15zG'
         },
         '4': {
            'step': 'Mix it all up and add the rest of your dressing! And Enjoy!',
            'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/06/Greek-Brown-and-Wild-Rice-Bowls_EXPS_SDAS18_204870_C03_28__10b-3.jpg'
         },
      }
   },
   '2': {
      'name': 'Glazed Squash',
      'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/01/Coconut-Acorn-Squash_exps149543_TH132767C04_25_1bC_RMS.jpg',
      'supplies': {
         '1':{
            'name': 'Aluminum Foil',
            'image': 'https://www.allrecipes.com/thmb/BoxoiPyfiLYcAc2GWY2HVIURbzA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/102368196_aluminum-foil-2000-4af779937cc9438cbe9be9d54c1f2e34.jpg'
         },
         '2':{
            'name': 'Baking Sheet',
            'image': 'https://www.nordicware.com/wp-content/uploads/2021/04/44600_The_Big_Sheet_002_780x780__55006.1648753775.1280.1280.jpg'
         },
         '3':{
            'name': 'Kitchen Knife',
            'image': 'https://www.opinel-usa.com/cdn/shop/products/Les-Forges-1890-8-Chef-Knife-Large-Kitchen-Knife_2000x.jpg'
         },
         '4':{
            'name': 'Cutting Board',
            'image': 'https://www.buildmat.com.au/cdn/shop/products/buildmat-kitchen-accessories-buildmat-wooden-chopping-board-sn101088-36435068059868_800x.png'
         },
         '5':{
            'name': 'Spoon',
            'image': 'https://i.pinimg.com/originals/70/41/50/7041508df360f4517d9dc88b178c0419.png'
         }
      },
      'ingredients': {
         '1': {
            'name': 'Vegetable Oil',
            'image': 'https://i5.peapod.com/c/YS/YS0IE.jpg'
         },
         '2': {
            'name': 'Brown Sugar',
            'image': 'https://i5.walmartimages.com/asr/0d74547e-9e21-42f4-bb95-7dc1a85f907d.713258977353ca217077f6d73d545bf7.jpeg?odnHeight=768&odnWidth=768&odnBg=FFFFFF'
         },
         '3': {
            'name': 'Acorn Squash',
            'image': 'https://www.kroger.com/product/images/large/back/0000000004750'
         },
         '4': {
            'name': 'Black Pepper',
            'image': 'https://badiaspices.com/wp-content/uploads/2018/01/033844012311.jpg'
         },
         '5': {
            'name': 'Salt',
            'image': 'https://www.containerstore.com/catalogimages/212810/670060SaltOrPepperShaker2ozV2_600.jpg'
         },
      },
      'instructions': {
         '1': {
            'step': 'Cut the squash in half using a knife on a cutting board and scrape the seeds out with a spoon.',
            'image': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTu8IdrA9fyUjg84kK0DaFOfZKKTCVHkW1_8v_uGTEvI-UHzUZJ'
         },
         '2': {
            'step': 'Preheat the oven to 400 and add aluminum foil to a baking sheet with some oil covering the top.',
            'image': 'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTaw5eCwcMS4lKvpbD0NlMUf4W0pKvc4V8zh8Ye31J2NMGCl2GT'
         },
         '3': {
            'step': 'Lay squash pieces on baking sheets. Season with salt and pepper; sprinkle squashes evenly with half the sugar.',
            'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwwlrOMIC_F_nVt3mPj7RRmDKLxcbjd9AtTI53RdrAuR3dfmmG'
         },
         '4': {
            'step': 'Roast until sugar has melted, about 5 minutes. Remove baking sheets from oven.',
            'image': 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRqvcVdfttkj8GzBnj2KaTyj7r-05gyNiFpndIgMnQ3iYQVuK0a'
         },
         '5': {
            'step': 'Flip the pieces over with a spoon. Season with salt and pepper; sprinkle evenly with remaining sugar. Roast until tender, about 20 minutes. Enjoy',
            'image': 'https://www.foodandwine.com/thmb/Q-4ciItjPFjSSQrUnHjt_TelVAs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/brown-sugar-roasted-acorn-squash-recipe-FT-BLOG1019-f14d448c609a4c09b595baa6fe04d7ec.jpg'
         },
      }
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


quiz_data = {
    1: {
        'name': 'Feta Salad',
        'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/06/Greek-Brown-and-Wild-Rice-Bowls_EXPS_SDAS18_204870_C03_28__10b-3.jpg',
        'problems': {
            1: {
                'prompt': 'For how long do you have to microwave the precooked rice?',
                'image': 'https://www.marthastewart.com/thmb/R5e-wnZBjNbvQiYmd1CtBQTFcVY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/924877_master-recipe-brown-rice-05-13126d75658249b48e7c9ac32d180ab2.jpg',
                'responses': {
                    1: '2 minutes',
                    2: '30 seconds',
                    3: '5 minutes',
                },
                'correct_response': 1,
                'response_type': 'ul'
            }
        }
    },
    2: {
       'name': 'Glazed Squash',
       'image': 'https://www.tasteofhome.com/wp-content/uploads/2018/01/Coconut-Acorn-Squash_exps149543_TH132767C04_25_1bC_RMS.jpg',
       'problems': {
            1: {
                'prompt': 'What is the ingredient that makes the squash sweet?',
                'responses': {
                    1: 'White Sugar',
                    2: 'Cocoa Powder',
                    3: 'Brown Sugar',
                },
                'correct_response': 3,
                'response_type': 'ul'
            },
            2: {
                'prompt': 'How many times do you flip squash over when roasting?',
                'responses': {
                    1: '2',
                    2: '4',
                    3: 'trick question, 1',
                },
                'correct_response': 1,
                'response_type': 'ul'
            },
            3: {
                'prompt': 'How much time do you roast the squash for the last step',
                'responses': {
                    1: '5 minutes',
                    2: '20 minutes',
                    3: 'however amount of time its takes for the sugar to be golden',
                },
                'correct_response': 1,
                'response_type': 'ul'
            }
        }
    },
    3: {
       'name': 'Garlic Scallion Ramen',
       'image': 'https://www.kitchentreaty.com/wp-content/uploads/2020/01/super-simple-miso-ramen-5-420x560.jpg',
       'problems': {
            1: {
                'prompt': 'For how long should you cook the noodles?',
                'responses': {
                    1: '3 minutes',
                    2: '1 minute',
                    3: 'the package instructions',
                },
                'correct_response': 3,
                'response_type': 'ul'
            },
            2: {
                'prompt': 'What should you do after cooking the noodles?',
                'responses': {
                    1: 'Eat the noodles',
                    2: 'Drain the noodles and set aside',
                    3: 'Add sauces to the noodles',
                },
                'correct_response': 2,
                'response_type': 'ul'
            },
            3: {
                'prompt': 'What does the sauce consist of?',
                'responses': {
                    1: 'Soy sauce, peanut butter, garlic, and scallions',
                    2: 'Soy sauce, peanut butter, and garlic',
                    3: 'Soy sauce, garlic, and scallions',
                },
                'correct_response': 1,
                'response_type': 'ul'
            }
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


@app.route('/test_recipe/<quiz_id>')
def quiz_start(quiz_id: int):
    quiz_info = quiz_data[int(quiz_id)]
    return render_template('quiz_start.html', id=quiz_id, name=quiz_info['name'], image=quiz_info['image'])


@app.route('/test_recipe/<quiz_id>/problems/<problem_id>')
def quiz_problem(quiz_id: int, problem_id: int):
    quiz_info = quiz_data[int(quiz_id)]
    problem = quiz_info['problems'][int(problem_id)]
    return render_template('quiz_problem.html', id=quiz_id, problem_id=problem_id, problem=problem)

@app.route('/test_recipe/<quiz_id>/score')
def quiz_score(quiz_id):
    score = 3
    return render_template('quiz_score.html', id=quiz_id, score=score,recipe_id = quiz_id, name = recipe_data[quiz_id]['name'], image = recipe_data[quiz_id]['image'])


@app.route('/hints')
def hints():
   return render_template('hints.html')

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipe_data)


@app.route('/get_quiz', methods=['GET'])
def get_quiz():
    return jsonify(quiz_data)


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
    app.run(debug=True)
