*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections
*** Keywords ***
Append Product Details To File
    [Arguments]       ${file_name}    ${name}       ${price}        ${rating}       ${Number}
    Append To File    ${file_name}    ${name}${\n} ,${price}${\n}   
    Append To File    ${file_name}    ${rating}
    Append To File    ${file_name}    ${Number}${\n}
    Append To File    ${file_name}    ${\n}