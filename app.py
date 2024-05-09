# 8. Hospital Management System

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

patients = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        id = len(patients) + 1  
        patients.append({'id': id, 'name': name, 'age': age})
        return redirect(url_for('view_patients'))
    return render_template('add_patient.html')

@app.route('/view_patients')
def view_patients():
    return render_template('view_patients.html', patients=patients)

@app.route('/search_patient', methods=['GET', 'POST'])
def search_patient():
    if request.method == 'POST':
        patient_id = int(request.form['id'])
        for patient in patients:
            if patient['id'] == patient_id:
                return render_template('search_result.html', patient=patient)
        return "Patient not found!"
    return render_template('search_patient.html')

if __name__ == '__main__':
    app.run(debug=True)