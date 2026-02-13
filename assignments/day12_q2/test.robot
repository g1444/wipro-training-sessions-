*** Settings ***
Library    BuiltIn
Library    Process
Library    SeleniumLibrary


*** Test Cases ***
Verify Environment Setup

    Log To Console    ==============================
    Log To Console    Starting Environment Check
    Log To Console    ==============================

    Run Keyword And Ignore Error    Check Python Installed
    Run Keyword And Ignore Error    Check Robot Installed
    Run Keyword And Ignore Error    Print Robot Version

    Log To Console    ==============================
    Log To Console    Environment Verification Done
    Log To Console    ==============================


*** Keywords ***

Check Python Installed
    Log    Checking Python installation...
    ${result}=    Run Process    python    --version    stdout=TRUE    stderr=TRUE
    Should Contain    ${result.stdout}    Python
    Log To Console    Python Installed: ${result.stdout}


Check Robot Installed
    Log    Checking Robot Framework installation...
    ${result}=    Run Process    robot    --version    stdout=TRUE    stderr=TRUE
    Should Contain    ${result.stdout}    Robot Framework
    Log To Console    Robot Installed: ${result.stdout}


Print Robot Version
    Log    Printing Robot Framework Version...
    ${result}=    Run Process    robot    --version    stdout=TRUE
    Log To Console    Robot Framework Version: ${result.stdout}
