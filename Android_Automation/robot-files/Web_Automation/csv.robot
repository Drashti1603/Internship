*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    OperatingSystem

*** Variables ***
${URL}            https://www.amazon.com
${SEARCH_QUERY}   laptop
${OUTPUT_FILE}    /home/drashti/Documents/Android_Automation/robot-files/Web_Automation/output.csv
${OUTPUT_FILE1}   /home/drashti/Documents/Android_Automation/robot-files/Web_Automation/output1.csv
${PRODUCT_LIST}   //div[starts-with(@data-component-type,'s-search-result')]

*** Test Cases ***
Search and Extract Product Details
    Open Browser                     ${URL}      chrome
    Maximize Browser Window
    Set Selenium Implicit Wait       20 seconds
    Input Text                       //*[@id="twotabsearchtextbox"]         ${SEARCH_QUERY}
    Click Element                    //*[@id="nav-search-submit-button"]    # Equivalent to pressing ENTER key
    Wait Until Element Is Visible    ${PRODUCT_LIST}

    @{product_details} =  Get WebElements   //div[starts-with(@data-component-type,'s-search-result')]
    FOR  ${product}  IN  @{product_details}
        Log Many ${product.text}
    END
    
    Save Names To CSV                ${OUTPUT_FILE}     ${product_details}
    Save Details To CSV              ${OUTPUT_FILE1}    ${product_details}

*** Keywords ***
Save Details To CSV
    [Arguments]                     ${file_name1}       ${details}
    FOR    ${index}    IN RANGE  3  ${details.__len__()}

        ${name}        Get Text     //*[@data-cel-widget="search_result_${index}"] 
        Append To File              ${file_name1}       ${name}${\n}
        Append To File              ${file_name1}       ${\n}
    END
*** Keywords ***
Save Names To CSV
    [Arguments]                     ${file_name}        ${details}
    FOR    ${index}    IN RANGE  3  ${details.__len__()}

        ${name}        Get Text     //*[@data-cel-widget="search_result_${index}"] //h2[starts-with(@class,'a-size-mini a-spacing-none a-color-base s-line-clamp-2')]
        ${price}       Get Text     //*[@data-cel-widget="search_result_${index}"] //span[@class='a-price']
        ${rating}      Get Text     //*[@data-cel-widget="search_result_${index}"] //span[@class='a-icon-alt']
        ${shipping}    Get Text     //*[@data-cel-widget="search_result_${index}"] //div[@data-cy="delivery-recipe"]

        Append To File              ${file_name}        ${name}${\n} ,${price}${\n}   
        Append To File              ${file_name}        ${rating}   
        Append To File              ${file_name}        ${shipping}${\n}
        Append To File              ${file_name}        ${\n}   
    
    END
