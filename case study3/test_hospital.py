import pytest,requests,json

base_url="http://127.0.0.1:5001"

def test_get_patients():
    r=requests.get(base_url)
    print(r.json())
    assert r.status_code==200

patient_url=base_url+"/patients/1"
def test_patient_by_id():
    r=requests.get(patient_url)
    print(r.json())
    assert r.status_code==200

posts_patient=base_url+"/patients"

def test_add_patients():
    # patient body in dictionary
    patient_body={
        "patient_name":"gowtham",
        "age":21,
        "disease":"broken heart",
        "gender":"male",
        "contact":7095602721,
        "doctor_assigned":"varsha vivekanandan"
    }
    r=requests.post(posts_patient,json=patient_body)
    print(r.json())
    assert r.status_code==201