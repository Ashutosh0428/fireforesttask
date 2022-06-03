'''import pickle
from flask import Flask,request,app,jsonify
import numpy as np 
import pandas as pd 

app=Flask(__name__)
model=pickle.load(open('model.pkl,'rb'))
 
@app.route('/predict_api',methods=["POST"])

def predict_api():
    data=request.json['data']
    print(data)
    new_data=[list(data.values())]
    output=model.prdict(new_data)[0]
    return jsonify(output)



if __name__=="__main__":
    app.run(debug=True)''' #for postman

import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
from flask_cors import CORS, cross_origin
import numpy as np
import pandas as pd
from application_logging import logger
import logging
logging.basicConfig(filename = "app.log" , level = logging.DEBUG , format ='%(asctime)s %(levelname)s %(message)s' )

app = Flask(__name__)
model = pickle.load(open('model1.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        if request.json is not None:
            data = request.json['data']
            print(data)
            new_data = [list(data.values())]
            output = model.predict(new_data)[0]
            return jsonify(output)
        else:
            print('Nothing Matched')
    except ValueError:
        return ("Error Occurred! %s" %ValueError)
    except KeyError:
        return ("Error Occurred! %s" %KeyError)
    except Exception as e:
        return ("Error Occurred! %s" %e)






@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.form is not None:
            logging.info("taking request from form")
            data = [float(x) for x in request.form.values()]
            final_features = [np.array(data)]
            logging.info("successfully taken data from form")
            logging.info(data)
            print(data)
            logging.info("predicting the output")
            output = model.predict(final_features)[0]
            logging.info("successfully got prediction ")
            logging.info(output)
            print(output)
            # output = round(prediction[0], 2)
            return render_template('home.html', prediction_text="Forest Fires Prediction is  {}".format(output))
        else:
            print('Nothing Matched')
    except ValueError:
        return ("Error Occurred! %s" %ValueError)
    except KeyError:
        return ("Error Occurred! %s" %KeyError)
    except Exception as e:
        return ("Error Occurred! %s" %e)



if __name__ == "__main__":
    app.run(debug=True)


