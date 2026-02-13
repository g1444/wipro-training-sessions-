*** Test Cases ***
Using if else if and else
    ${marks}=    Set Variable    87
    IF    ${marks} >= 80
        Log To Console    \nGrade a
    ELSE IF    ${marks} >= 70
        Log To Console    \nGrade b
    ELSE
        Log To Console     \nGrade c
    END

