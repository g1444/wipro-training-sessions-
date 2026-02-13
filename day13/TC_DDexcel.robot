*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.csv  
Test Template    OrangeHRM login with excel
Test Setup    open Orangehrm
Test Teardown    Close OrangeHRM

*** Variables ***
${URL}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${Browser}    chrome

*** Keywords ***
open Orangehrm
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
OrangeHRM login with excel
    [Arguments]    ${username}    ${password}
    Wait Until Element Is Visible    name=username    10s
    Input Text    name:username    ${username}
    Input Text    name:password    ${password}
    Click Button    xpath://button[@type='submit']
    Wait Until Element Is Visible    xpath://span[@class='oxd-userdropdown-tab']    15s
    Capture Page Screenshot    ${OUTPUT DIR}/ddexcel afterlogout.png
    Logout From OrangeHRM
Logout From OrangeHRM
    Click Element    xpath://span[@class='oxd-userdropdown-tab']
    Wait Until Element Is Visible     xpath://a[text()='Logout']     5s
    Click Element    xpath://a[text()='Logout']
    Wait Until Element Is Visible    xpath://input[@name='username']    5s
Close OrangeHRM
    Close Browser
*** Test Cases ***
Login with user from Excel
    Log    Executed via DataDriver