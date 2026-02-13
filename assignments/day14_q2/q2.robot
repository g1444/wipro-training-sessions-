*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://tutorialsninja.com/demo/
${BROWSER}  chrome

*** Test Cases ***
QAfox Form Automation
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Click Element    xpath://span[text()='My Account']
    Click Element    xpath://a[text()='Register']

    Input Text    id:input-firstname    Gowtham
    Input Text    id:input-lastname     Reddy
    Input Text    id:input-email        gowtham67.com@gmail.com
    Input Text    id:input-telephone    9876543210
    Input Text    id:input-password     Test@123
    Input Text    id:input-confirm      Test@123

    Click Element    xpath://input[@name='newsletter' and @value='1']

    Click Element    xpath://input[@name='agree']

    Sleep    2s
    Click Button    xpath://input[@value='Continue']

    ${heading}=    Get Text    xpath://h1
    Should Be Equal    ${heading}    Qafox.com

    Run Keyword If    '${heading}' == 'Qafox.com'
    ...    Log To Console    ✅ Registration Successful
    ...  ELSE
    ...    Log To Console    ❌ Registration Failed

    Sleep    2s
    Close Browser
