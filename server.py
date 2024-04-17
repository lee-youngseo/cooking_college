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


@app.route('/get_recipes', methods=['GET'])
def get_recipes():
    return jsonify(recipe_data)


@app.route('/get_quiz', methods=['GET'])
def get_quiz():
    return jsonify(quiz_data)


if __name__ == '__main__':
    app.run(debug=True)
