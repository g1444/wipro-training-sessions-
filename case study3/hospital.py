from flask import Flask,request,jsonify

app=Flask(__name__)

patients = [
    {
        "id": 1,
        "patient_name": "Ravi Kumar",
        "age": 25,
        "gender": "Male",
        "contact": "9876543210",
        "disease": "Fever",
        "doctor_assigned": "Dr. Sharma"
    },
    {
        "id": 2,
        "patient_name": "Anitha Devi",
        "age": 32,
        "gender": "Female",
        "contact": "9123456780",
        "disease": "Diabetes",
        "doctor_assigned": "Dr. Priya"
    }
]

@app.route("/",methods=['GET'])
def get_all_patients():
    return jsonify(patients)

@app.route("/patients/<int:patient_id>",methods=["GET"])
def get_patient_by_id(patient_id):
    for p in patients:
        if p["id"]==patient_id:
            return jsonify(p)
    return jsonify({"message": "patient not found"})
@app.route("/patients",methods=['POST'])
def add_patient():
    data=request.json
    new_patient={"id": 2,
        "patient_name": "Anitha Devi",
        "age": data.get("age"),
        "gender": data.get("gender"),
        "contact": data.get("contact"),
        "disease":data.get("disease"),
        "doctor_assigned":data.get("doctor_assigned")}
    return jsonify(new_patient),201
@app.route("/patients/<int:patient_id>",methods=['DELETE'])
def remove_patient(patient_id):
    for patient in patients:
        if patient["id"]==patient_id:
            patients.remove(patient)
            return jsonify({"message":"patient removed"}),200
    return jsonify({"message":"patient not found"}),404
if __name__=="__main__":
    app.run(port=5001,debug=True)