*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections
*** Keywords ***
Save Details To CSV
    [Arguments]                     ${file_name1}       ${details}
    FOR    ${index}    IN RANGE  3  ${details.__len__()}

        ${name}        Get Text     //*[@data-cel-widget="search_result_${index}"] 
        Append To File              ${file_name1}       ${name}${\n}
        Append To File              ${file_name1}       ${\n}
    END

