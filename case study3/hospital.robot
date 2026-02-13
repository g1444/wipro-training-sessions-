*** Settings ***
Library    RequestsLibrary
Suite Setup    Setup hospital api
Suite Teardown    Teardown hospital api

*** Variables ***
${base_url}    http://127.0.0.1:5001

*** Keywords ***
Setup hospital api
    Create Session    hospital    ${base_url}
Teardown hospital api
    Delete All Sessions
Get all patients
    ${resp}=    GET On Session    hospital    url=/
    RETURN    ${resp}
Get patient by id
    [Arguments]    ${patient_id}
    ${resp}=    GET On Session    hospital    url=/patients/${patient_id}
    RETURN    ${resp}
Add patients
    [Arguments]    ${patient_name}    ${age}   ${gender}    ${contact}    ${disease}    ${doctor_asssigned}
    &{data}=    Create Dictionary    
    ...    patient_name:${patient_name}    
    ...    age:${age}    
    ...    gender:${gender}    
    ...    contact:${contact}    
    ...    disease:${disease}    
    ...    doctor_assigned:${doctor_asssigned}
    ${resp}=    POST On Session    hospital    url=/patients    json=${data}
    RETURN    ${resp}

*** Test Cases ***
get all patients
    ${resp}=     Get all patients
    Status Should Be    200    ${resp}
    Log    ${resp.json()}
get patient by id
    ${resp}=    Get patient by id    1
    Status Should Be    200
    Log    ${resp.json()}
posting patient
    ${resp}=    Add patients    gowtham    21    male    7095602721    brokenheart    varsha
    Status Should Be    201    ${resp}
    Log    ${resp.json()}
