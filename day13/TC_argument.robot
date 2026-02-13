*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    edge

*** Keywords ***
opening orangehrm in edge
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
login orangehrm
    [Arguments]    ${Username}    ${password}
    Input Text    name:username    ${Username}
    Input Text    name:password    ${password}
    Click Button    xpath://button[@type="submit"]
    Sleep    3s

*** Test Cases ***
argument
    opening orangehrm in edge
    Sleep     4s
    Capture Page Screenshot    ${OUTPUT_DIR}/beforelogin.png
    login orangehrm    Admin    admin123
    Sleep    3s
    Capture Page Screenshot    ${OUTPUT_DIR}/afterlogin.png
    Close Browser