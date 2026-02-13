*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.saucedemo.com/
${BROWSER}    edge
${USERNAME}   problem_user
${PASSWORD}   secret_sauce

*** Test Cases ***
Log Into Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    2s

    Capture Page Screenshot    ${OUTPUT DIR}/beforelogin.png

    Input Text       id:user-name    ${USERNAME}
    Input Password   id:password     ${PASSWORD}
    Click Button     id:login-button
    Sleep    2s

    Capture Page Screenshot    ${OUTPUT DIR}/afterlogin.png

    Title Should Be    Swag Labs
    Close Browser
