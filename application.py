# importing the necessary dependencies
from flask import Flask, render_template, request, jsonify
from flask_cors import cross_origin
import pickle

application = Flask(__name__)  # initializing a flask app

cross_origin(application)  # Enable CORS for your Flask app


# app=application
@application.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


# @application.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
# @cross_origin()
# def index():
#     if request.method == 'POST':
#         try:
#             #  reading the inputs given by the user
#             Age = float(request.form['Age'])
#             Height = float(request.form['Height'])
#             Weight = float(request.form['Weight'])
#             Sit_Reach = float(request.form['Sit_Reach'])
#             fifty_m_Dash = float(request.form['fifty_m_Dash'])
#             PushUps = float(request.form['PushUps'])
#             one_min_SitUps = float(request.form['one_min_SitUps'])
#             Run_Walk = float(request.form['Run_Walk'])
#             filename = 'utsav_rf.pickle'
#             loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
#             # predictions using the loaded model file
#             prediction = loaded_model.predict(
#                 [[Age, Height, Weight, Sit_Reach, fifty_m_Dash, PushUps, one_min_SitUps, Run_Walk]])
#             print('prediction is', prediction)
#             # showing the prediction results in a UI
#             return render_template('results.html', prediction=prediction)
#         except Exception as e:
#             print('The Exception message is: ', e)
#             return 'something is wrong'
#     # return render_template('results.html')
#     else:
#         return render_template('index.html')


@application.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        # Parse JSON data from the request body
        data = request.get_json()
       
        # Extract data from the JSON
        Age = float(data.get('age'))
        Height = float(data.get('height'))
        Weight = float(data.get('weight'))
        Sit_Reach = float(data.get('sit_reach'))
        fifty_m_Dash = float(data.get('fifty_m_dash'))
        PushUps = float(data.get('pushups'))
        one_min_SitUps = float(data.get('one_min_situps'))
        Run_Walk = float(data.get('run_walk'))

        filename = 'utsav_rf.pickle'
        loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
        # predictions using the loaded model file
        prediction = loaded_model.predict(
            [[Age, Height, Weight, Sit_Reach, fifty_m_Dash, PushUps, one_min_SitUps, Run_Walk]])
        print('prediction is', prediction)

        result = {
            "prediction": prediction.tolist()
        }

        return jsonify(result)
    except Exception as e:
        print('The Exception message is: ', e)
        return jsonify({"error": "Something went wrong"})

if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=8001, debug=True)
    application.run(debug=True)  # running the app
