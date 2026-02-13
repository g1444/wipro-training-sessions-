*** Test Cases ***
for using zip
    @{Users}=    Create List    admin    user
    @{Pwds}=     Create List    admin123    user123

    @{pairs}=    Evaluate    list(zip($Users, $Pwds))

    FOR    ${pair}    IN    @{pairs}
        Log To Console    ${pair}[0] / ${pair}[1]
    END
