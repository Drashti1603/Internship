*** Settings ***
Resource   ../Keywords/Details(all).robot
Resource   ../Keywords/Names,Price,shipping,rating,num.robot
Resource   ../Locators/URL.robot
Resource   ../Locators/Output_Path.robot
Resource   ../Locators/X-path(Searching).robot


*** Test Cases ***
Search and Extract Product Details
    Open Browser                     ${URL}      chrome
    Maximize Browser Window
    Set Selenium Implicit Wait       20 seconds
    Input Text                       ${Search}          ${SEARCH_QUERY}
    Click Element                    ${Search_button}    # Equivalent to pressing ENTER key
    Wait Until Element Is Visible    ${PRODUCT_LIST}

    @{product_details} =            Get WebElements     ${Prodct_elements} 
    # FOR  ${product}  IN  @{product_details}
    #     Log Many ${product.text}
    # END
    
    Save Names To CSV                ${OUTPUT_FILE}     ${product_details}
    Save Details To CSV              ${OUTPUT_FILE1}    ${product_details}

