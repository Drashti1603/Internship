*** Settings ***
Library    AppiumLibrary

*** Variables ***
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    12
${DEVICE_NAME}    Drashti Chetta
${APP_PACKAGE}    com.ril.ajio
${APP_ACTIVITY}    com.ril.ajio.home.AjioHomeActivity
${APPIUM_SERVER}    http://localhost:4723/wd/hub

*** Test Cases ***
Search and Add to Cart on Ajio Mobile App
    Open Application    ${APPIUM_SERVER}    platformName=${PLATFORM_NAME}    platformVersion=${PLATFORM_VERSION}    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}

    # Perform a search (replace with actual locators)
    Click Element    xpath=//android.view.ViewGroup[@content-desc="Coachmark"]
    Click Element    xpath=//android.widget.TextView[@resource-id="com.ril.ajio:id/laTvAllow"]
    Wait Until Element Is Visible   xpath=//android.widget.ImageView[@content-desc="Ajio Search box, Search by product, brand..."]

    # Press Enter (keycode 66)
    Press Keycode    66

    # Select the first search result (replace with actual locators)
    Click Element    xpath=//android.widget.ImageView[@content-desc="Ajio Search box, Search by product, brand..."][1]

    # Add the item to the cart (replace with actual locators)
    Click Element    xpath=//*[@resource-id='your_add_to_cart_locator']

    # Verify that the item is added to the cart (replace with actual locators)
    Wait Until Element Is Visible    xpath=//*[@resource-id='your_cart_icon_locator']
    Click Element    xpath=//*[@resource-id='your_cart_icon_locator']

    # Check if the item is in the cart (replace with actual locators)
    Element Should Be Visible    xpath=//*[@text='Product Name']

*** Keywords ***
Maximize Browser Window
    Maximize Browser Window
