*** Test Cases ***
using if else blocks
    ${age}=    Set Variable    15
    IF    ${age} > 18
        Log To Console    you are eligible to vote
    ELSE
        Log To Console    You are not eligible to vote
    END