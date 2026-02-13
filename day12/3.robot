*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.youtube.com/
${BROWSER}    chrome

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
*** Test Cases ***
Test Open
    Open Application
    ${title}=    Get Title
    Should Contain    ${title}    YouTube
    Close Browser