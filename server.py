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
      'image': 'https://www.kitchentreaty.com/wp-content/uploads/2020/01/super-simple-miso-ramen-5-420x560.jpg'
   }
}

quiz_data = {
    'feta+salad': {
        'problems': {
            1: {
                'prompt': '',
                'image': '',
                'responses': [],
                'correct_response': ''
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

@app.route('/get_recipes', methods=['GET'])
def get_recipes():
   return jsonify(recipe_data)

if __name__ == '__main__':
   app.run(debug = True)