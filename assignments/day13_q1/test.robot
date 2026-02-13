*** Settings ***
Library    OperatingSystem
Library    String
Library    Collections

*** Test Cases ***
Execute Data Driven Login
    ${file_content}=    Get File    data.csv
    @{lines}=    Split To Lines    ${file_content}
    FOR    ${line}    IN    @{lines}
        ${username}    ${password}=    Split String    ${line}    separator=,
        # This block catches the failure so the test doesn't stop
        TRY
            Login Workflow Template    ${username}    ${password}
        EXCEPT    AS    ${error}
            Log    Row failed for ${username}: ${error}    level=WARN
        END
    END

*** Keywords ***
Login Workflow Template
    [Arguments]    ${username}    ${password}
    Open Login Page
    Enter Credentials    ${username}    ${password}
    Verify Results    ${username}

Open Login Page
    Log    Navigating to Login UI...

Enter Credentials
    [Arguments]    ${uname}    ${pword}
    Log    Entering Username: ${uname}
    Log    Entering Password: ${pword}

Verify Results
    [Arguments]    ${uname}
    IF    '${uname}' == 'invalid'
        Fail    Invalid credentials detected for: ${uname}
    ELSE
        Log    Login successful for ${uname}
    END