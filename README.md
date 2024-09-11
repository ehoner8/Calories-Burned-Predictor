# Calories-Burned-Predictor
A machine learning model to predict the number of calories somebody has burned in a workout.

**Description**

This is a project that analyzes and predicts the number of calories burned during a workout given 7 features: age, height, weight, duration of workout, heart rate, body temperature, and gender. The dataset consists of 15,000 entries and can be found on kaggle (link below). 

I took up this project shortly after starting to go to the gym, and seeing how the fitness industry has changed. Many people are very analytical in their fitness journey, and keep track of every calorie they burn or consume, largely thanks to the introduction of apple watches. These types of people would make great use of this program, which only requires 7 input fields. 

To create the model, I used the sklearn library. I used the polynomial feature converter with a degree of 3 to transform the data, which improved performance significantly. I tried using both an elasticnet model and a support vector regressor. It was ultimately the SVR that performed the best with a MAE of 0.25 and a RMSE of 0.08 calories. That's much better than I expected since the average label value was 90 calories. 

App.py is the API for this model, and uses streamlit to provide easy user interaction with the model. Make sure you have all the right dependencies installed as seen in requirements.txt, and simply run streamlit run app.py. Input the appropriate values for each of the seven fields, and you can see how many calories you burned in your latest workout!



**Credits**
https://github.com/siddhardhan23/multiple-disease-prediction-streamlit-app/blob/main/app.py 
https://www.kaggle.com/datasets/fmendes/fmendesdat263xdemos 

