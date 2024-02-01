*** Settings ***
Library    SeleniumLibrary     timeout=5500

*** Variables ***
${HOMEPAGE}   https://www.amazon.in

${Search}     //*[@id="twotabsearchtextbox"]
${check}      //a-checkbox a-checkbox-fancy s-navigation-checkbox aok-float-left[@id="p_90/6741117031"]
${searchResultURL}   https://www.amazon.in/s?k=shoes&rh=p_90%3A6741117031&dc&ds=v1%3AHPjd0UYRr2jpK9TZTPSfbBj3XuxWj7xRPOgIoQnwUQI&qid=1706618545&rnid=6741116031&ref=sr_nr_p_90_1
${window_handles}    Get Window Handles


*** Test Cases ***
Search on Amazon
    Open Browser    ${HOMEPAGE}    Chrome
    Maximize Browser Window
    Input Text    ${Search}    shoes asian
    Click Element   //*[@id="nav-search-submit-button"] 
#    Wait Until Element Is Visible    //*[@id="p_90/6741117031"]   timeout=15s
#    Click Element    ${check}
    Go To    ${searchResultURL}
    Execute JavaScript    window.scrollBy(0,500)
    Go To    https://www.amazon.in/s?k=shoes+asian&rh=n%3A1571283031%2Cp_89%3AASIAN&dc&ds=v1%3AotwcMt3yo16FdR0%2FG8RvfL8TBlz5MMwsYuw6I4iKEP4&crid=1FR4EOSWXARGQ&qid=1706692550&rnid=3837712031&sprefix=shoes+asian%2Caps%2C255&ref=sr_nr_p_89_1
    Execute JavaScript    window.scrollBy(0,500)  
    Input Text    //*[@id="low-price"]    500
    Input Text    //*[@id="high-price"]    1000
    Click Element    //*[@id="a-autoid-1-announce"]
    Execute JavaScript    window.scrollBy(0,500)    
    Go To    https://www.amazon.in/s?k=shoes&i=shoes&rh=n%3A1571283031%2Cp_90%3A6741117031%2Cp_89%3AASIAN%2Cp_n_deal_type%3A26921226031&dc&ds=v1%3AMaIMcoFuwmH1YAZQDXLbWdnGbNwH%2FsJzL0p6pq3Qg3U&qid=1706678247&rnid=26921223031&ref=sr_nr_p_n_deal_type_1
    Execute JavaScript    window.scrollBy(0,500)    
    Click Element    //*[p_n_size_browse-vebin/2022653031"]
    Click Element    //*[@data-csa-c-item-id="amzn1.asin.1.B07FS383T1"]
    ${tab2}    Switch Window    NEW
    Execute JavaScript    window.scrollBy(0,350)
    Click Element    //*[@id="add-to-cart-button"]
    Go To    https://www.amazon.in/cart?ref_=sw_gtc
    Click Element    //*[@data-feature-id="proceed-to-checkout-action"]
    Wait Until Element Is Visible    //*[@id="createAccountSubmit"]  timeout=5s
    Input Text    //*[@id="ap_email"]    drashti.chetta2002@gmail.com
    Click Element    //*[@id="continue"]
    Input Password    //*[@id="ap_password"]    Drashti*123
    Click Element    //*[@id="signInSubmit"]
    Go To    https://www.amazon.in/cart?ref_=sw_gtc
#         ${price}    Get Text    //div[starts-with(@data-cy,'price-recipe')]
# *** Keywords ***
# Save Product Details To CSV
#     [Arguments]    ${file_name}    ${details}
#     FOR    ${detail}    IN    @{details}
#         ${name}    Get Text    //h2[starts-with(@class,'a-size-mini a-spacing-none a-color-base s-line-clamp-2')]
#         ${csv_line}=    Evaluate    '${name}' 
#         Append To File    ${file_name}    ${csv_line}${\n}
