*** Settings ***
Library    Browser

*** Test Cases ***
Open example
    New Browser    chromium    headless=False
    New Page       https://google.com
    ${title}=    Get Title
    Should Contain    ${title}    Google

    Close Browser