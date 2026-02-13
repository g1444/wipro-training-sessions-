*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Screenshot Test
    Open Browser    https://example.com    chrome
    Capture Page Screenshot    example.png
    Close Browser
