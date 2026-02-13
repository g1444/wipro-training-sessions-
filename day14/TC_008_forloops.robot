*** Variables ***
@{names}    varsha    vinoliya    gowtham
${i}    0
@{USERS}=    Create List   admin    users
@{PASSWORDS}=    Create List    admin123    user123
*** Test Cases ***
print names
    FOR    ${name}     IN    @{names}
        Log To Console    ${name}
    END
printing names without variables
    FOR    ${name}    IN    varsha    vinoliya    gowtham
        Log To Console    ${name}
    END
printing using while loops
    WHILE    ${i} < 5
        Log To Console  ${i}
        ${i}=    Evaluate    ${i}+1
    END
printing using range
    FOR     ${i}    IN RANGE    0    6
        Log To Console    ${i}
    END
For loops with step
    FOR    ${i}    IN RANGE    1    10    2
        Log To Console    \nvalue:${i}
    END
For using Enumerate
    FOR    ${index}    ${value}    IN ENUMERATE    a    b    c
        Log To Console    \n${index}:${value}
    END
*** Test Cases ***
For loops using zip
    FOR    ${u}    ${p}    IN ZIP    @{USERS}    @{PASSWORDS}
        Log To Console    ${u} / ${p}
    END
