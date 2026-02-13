*** Settings ***
Library    RequestsLibrary
Library    SeleniumLibrary

*** Variables ***
${Base_url}    http://127.0.0.1:5000


*** Test Cases ***
Verify get user
    Create Session    mysession    ${Base_url}
    ${response}=    GET On Session    mysession    /users
    Status Should Be    200    ${response}
    ${res_json}=    To Json    ${response.content}
    Log    ${res_json}=    console=True
verify get user1
    Create Session    usersession    ${Base_url}
    ${response_user}=    GET On Session    usersession    /users/1
    Status Should Be    200    ${response_user}
    ${user_json}=    Evaluate    $response_user.json()
    Log    ${user_json}=    console=True
POSTING THE NEW USER
    Create Session    postingsession    ${Base_url}
    &{data}=    Create Dictionary    name=varsha
    ${response}=    POST On Session    postingsession    /users    json=&{data}
    Status Should Be    201    ${response}
    ${user_json}=    Evaluate    $response.json()
    Log    ${user_json}=    console=True
update user
    Create Session    putsession    ${Base_url}
    &{data}=    Create Dictionary    name=Gowtham1
    ${response}=    PUT On Session    putsession    /users/1    json=${data}
    Status Should Be    200    ${response}
    ${user_json}=    Evaluate    $response.json()
    Log    ${user_json}=    console=True
patch user
    Create Session    putsession    ${Base_url}
    &{data}=    Create Dictionary    course=python with selenium
    ${response}=    PATCH On Session    putsession    /users/1    json=${data}
    Status Should Be    200    ${response}
    ${user_json}=    Evaluate    $response.json()
    Log    ${user_json}=    console=True
delete user
    Create Session    deletesession    ${Base_url}
     ${response}=    DELETE On Session    deletesession    /users/1
    Status Should Be    201    ${response}
    ${user_json}=    Evaluate    $response.json()
    Log    ${user_json}=    console=True