*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx

Suite Setup       Open Site
Suite Teardown    Close Browser

Test Setup        Log    Starting Test
Test Teardown     Capture Page Screenshot

Test Template     Login Test


*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    chrome


*** Keywords ***

Open Site
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window


Login Test
    [Arguments]    ${username}    ${password}

    Wait Until Element Is Visible    name=username    10s
    Input Text    name:username    ${username}
    Input Text    name:password    ${password}
    Click Button    xpath://button[@type="submit"]

    Sleep    2s
    Log To Console    Login Done for ${username}


*** Test Cases ***

OrangeHRM Login
    [Tags]    smoke
    ${username}    ${password}
