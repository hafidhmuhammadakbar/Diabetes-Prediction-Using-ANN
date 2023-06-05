import PySimpleGUI as sg
from data_splitting import predict_data

# Define the layout of the window
sg.theme("Reddit")
layout = [
    [sg.T("Diabetes Prediction Using ANN", font="Any 20")],
    # gender
    [sg.Text('Choose your gender:')],
    [sg.Combo(['Female', 'Male'], key='-gender-', enable_events=True)],
    # age
    [sg.Text('Enter your age:')],
    [sg.InputText(key='-age-', enable_events=True)],
    # hypertension
    [sg.Text('Do you have hypertension?')],
    [sg.Combo(['Yes', 'No'], key='-hypertension-', enable_events=True)],
    # heart_disease
    [sg.Text('Do you have heart disease?')],
    [sg.Combo(['Yes', 'No'], key='-heart_disease-', enable_events=True)],
    # smoking_history
    [sg.Text('What is your smoking history?')],
    [sg.Combo(['Never', 'Former', 'Current'], key='-smoking_history-', enable_events=True)],
    # bmi
    [sg.Text('Enter your BMI:')],
    [sg.InputText(key='-bmi-', enable_events=True)],
    # hbA1c_level
    [sg.Text('What is your hbA1c level?')],
    [sg.InputText(key='-hbA1c_level-', enable_events=True)],
    # blood_glucose
    [sg.Text('Enter your blood glucose:')],
    [sg.InputText(key='-blood_glucose-', enable_events=True)],
    # submit button
    [sg.Button('Submit')]
]

# Create the window
window = sg.Window('Diabetes Prediction Using ANN', layout)

# Event loop
while True:
    event, values = window.read() 

    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Submit':
        # check if all values are filled
        if not all(values.values()):
            sg.popup('Please fill all the values')
            continue
        else:
            # Read all input values
            selected_gender = values['-gender-']
            if selected_gender == 'Female':
                selected_gender = 0
            else:
                selected_gender = 1

            selected_age = int(values['-age-'])

            selected_hypertension = values['-hypertension-']
            if selected_hypertension == 'Yes':
                selected_hypertension = 1
            else:
                selected_hypertension = 0

            selected_heart_disease = values['-heart_disease-']
            if selected_heart_disease == 'Yes':
                selected_heart_disease = 1
            else:
                selected_heart_disease = 0
            
            selected_smoking_history = values['-smoking_history-']
            if selected_smoking_history == 'Never':
                selected_smoking_history = 0
            elif selected_smoking_history == 'Former':
                selected_smoking_history = 1
            elif selected_smoking_history == 'Current':
                selected_smoking_history = 2

            selected_bmi = float(values['-bmi-'])

            selected_hbA1c_level = float(values['-hbA1c_level-'])
            
            selected_blood_glucose = int(values['-blood_glucose-'])
            
            # Create a person
            person = [[selected_gender, selected_age, selected_hypertension, selected_heart_disease, selected_smoking_history, selected_bmi, selected_hbA1c_level, selected_blood_glucose]]

            result = predict_data(person)

            sg.popup(f'Results of predictions: {result}')
            # sg.popup(f'Gender : {selected_gender} Age : {selected_age}, Hypertension : {selected_hypertension}, Heart Disease : {selected_heart_disease}, Smoking History : {selected_smoking_history}, BMI : {selected_bmi}, hbA1c Level : {selected_hbA1c_level}, Blood Glucose : {selected_blood_glucose}')
            continue

# Close the window
window.close()