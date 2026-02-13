*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    testdata.xlsx
Test Template    Orange Login

*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    chrome

*** Keywords ***
Orange Login
    [Arguments]    ${username}    ${password}

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s

    Input Text      name:username    ${username}
    Input Password  name:password    ${password}
    Click Button    xpath://button[@type='submit']

    Sleep    2s
    Close Browser

*** Test Cases ***
Login With Data
    ${username}    ${password}
