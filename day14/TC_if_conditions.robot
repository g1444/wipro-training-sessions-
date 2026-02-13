*** Test Cases ***
using if condition normally
    ${age}=    Set Variable    43
    Set Global Variable    ${age}
    IF    ${age} > 18
        Log To Console    you are eligible to vote
    END
using if condition inline
    IF     ${age} > 19    Log To Console    you are eligible to vote
