*** Settings ***
Library    RequestsLibrary
Suite Setup    Setup movie api
Suite Teardown    Teardown movie api

*** Variables ***
${base_url}    http://127.0.0.1:5000



   
*** Keywords ***
Setup movie api
    Create Session    movie    ${base_url}

Teardown movie api
    Delete All Sessions

Get all movies
    ${resp}=    GET On Session    movie    url=/
    RETURN    ${resp}

Add new movie
    [Arguments]    ${movie_name}    ${duration}    ${language}    ${price}
    &{data}=    Create Dictionary
    ...    movie_name:${movie_name}
    ...    duration:${duration}
    ...    language:${language}
    ...    price:${price}

    ${resp}=    POST On Session    movie    url=/movies    json=${data}
    RETURN    ${resp}
booking
    [Arguments]    ${movie_id}    ${tickets}    ${customer}
    &{data}=    Create Dictionary
    ...    movie_id=${movie_id}
    ...    tickets=${tickets} 
    ...    customer=${customer}
    ${resp}=    POST On Session    movie    url=/bookings    json=${data}
    RETURN    ${resp}
*** Test Cases ***
 
get all movies
    ${resp}=    Get all movies
    Status Should Be    200    ${resp}
    Log    ${resp.json()}

add new movie
    ${resp}=    Add new movie    your name    1hr 48m    japanese    220
    Status Should Be    201    ${resp}
    Log    ${resp.json()}
new booking
    ${resp}=    booking    2    2    gowtham
    Status Should Be    201    ${resp}
    Log    ${resp.json()}