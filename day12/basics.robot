*** Settings ***
#hahahahah
#built in libraries are always imported so no need to import that

*** Variables ***
${Name}    Gowtham
@{Friends}    varsha    vinoliya    vishal1    vishal2

*** Test Cases ***
Test Case 1 - Logging Messages
    Log    Hello world
    Log To Console    Running test case 1
    Log    Welcome ${Name}

Test Case 2 - variables
    Log To Console    \nrunning test case 2
    Log    First friend is ${Friends}[2]
    Log    all friends are @{Friends}