*** Settings ***
Resource    ../Locators/Filters.robot
Resource    ../Locators/URL.robot
Resource    ../Locators/Searching.robot
Library    SeleniumLibrary     timeout=5500

*** Keywords ***
Apply_Filters and Add_to_cart
    Go To                 ${Deliver_today} 
    Execute JavaScript    window.scrollBy(0,500)  
    Input Text            ${Low_price}    500
    Input Text            ${High_price}    1000
    Click Element         ${Go}
    Execute JavaScript    window.scrollBy(0,500)    
    Go To                 ${All_dis}
    Execute JavaScript    window.scrollBy(0,500)    
    Click Element         ${Size}
    Click Element         ${Product1} 
    ${tab2}               Switch Window    NEW
    Execute JavaScript    window.scrollBy(0,350)
    Click Element         ${Add_to_cart}
    Go To                 ${Go_to_cart}   
    Click Element         ${Check-out}