*** Settings ***

*** Variables ***
${NAME}        Gowtham
${COURSE}      Robot Framework Testing

@{FRIENDS}      Varsha    Vinoliya     Harsha    Vishal

*** Test Cases ***

Test Case 1 - Simple Logging
    Log    Hello ${NAME}, welcome to ${COURSE}
    Log To Console    Running Test Case 1 Successfully 
    Should Be Equal    ${NAME}    Gowtham


Test Case 2 - List Variable Demo
    Log    Friends list is: @{FRIENDS}
    Log To Console    First friend is ${FRIENDS}[0]
    Should Contain    ${FRIENDS}    Varsha
    Log To Console    Test Case 2 Completed 
