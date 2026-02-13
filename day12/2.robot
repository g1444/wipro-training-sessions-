*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://google.com
${BROWSER}        chrome

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

*** Test Cases ***
Open Google
    Open Application
    Capture Page Screenshot    ${OUTPUT DIR}/page.png
    Title Should Be    Google
    Close Browser
