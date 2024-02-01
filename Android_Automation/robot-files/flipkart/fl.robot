User

*** Settings ***
Documentation    Tests to validate Flipkart mobile app
Library    AppiumLibrary    timeout=5000
Test Timeout    15 minutes
*** Variables ***
${AppiumServerURL}    http://localhost:4723/wd/hub
${PlatformName}    Android  # or iOS
${DeviceName}    Drashti Chetta
${AppPackage}    com.flipkart.android  # replace with your app's package
${AppActivity}    .activity.HomeFragmentHolderActivity  # replace with your app's main activity
${categories}    //android.widget.TextView[@text="Categories"]
${SearchButton}    //android.widget.ImageView[@content-desc="Search"]
${SearchFieldLocator}     //android.widget.EditText[@text="Search for products"]
${SearchButton1}    //android.widget.TextView[@text="shoes for women"]
${Product}      //android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]
${skip}          //android.widget.TextView[@text="Skip"]
${PriceFilterClass}       //android.widget.TextView[@text="Filter"]
${PriceMaxFilter}         //android.widget.TextView[@text="Price"]
${PriceMaxValue}          //android.widget.TextView[@text="Rs. 3000 and Above"]
${allow}          //android.widget.Button[@resource-id="com.flipkart.android:id/not_now_button"]
${brand}          //android.widget.TextView[@text="Brand"]
${adidas}        //android.widget.TextView[@text="ADIDAS"]
${CART}    //android.widget.TextView[@text="Buy now"]

${size}    //android.widget.TextView[@text="6"]
${phone}    //android.widget.EditText[@content-desc="Phone Number"]
${PLACEORDER}     //android.widget.TextView[@text="Place order "]

*** Keywords***
Apply Filters on Price and Brand
    # Wait for the Price filter element to be visible
    Wait Until Element Is Visible    ${brand}    timeout=10    
    Click Element   ${brand}
    
    Wait Until Element Is Visible    ${adidas}    timeout=10 	 
    # Select from the price filter list by value
    Click Element   ${adidas}
    # Add a sleep to allow time for the filter to be applied (adjust as needed)
    Click Element   //android.widget.TextView[@text="Apply"]

    # Capture a screenshot
    Capture Page Screenshot    filename=avd.png
 Product Selection
    # Wait for the product element to be visible
    Wait Until Element Is Visible    ${Product}

    # Get the product element
    Click Element    ${Product}

    # Capture a screenshot
    Capture Page Screenshot
Search Validation
    Open Application    ${AppiumServerURL}    platformName=${PlatformName}    deviceName=${DeviceName}    appPackage=${AppPackage}    appActivity=${AppActivity}

    Click Element    ${skip} 
    Wait Until Element Is Visible   ${categories}    timeout=50

    # Input text into the search field
    Click Element    ${categories}

    Wait Until Element Is Visible    ${SearchButton}    timeout=50

    # Capture a screenshot
    # Click the search button
    Click Element    ${SearchButton}

    Input Text    ${SearchFieldLocator}    shoes

    Wait Until Element Is Visible    ${SearchButton1}    timeout=10s

    Click Element    ${SearchButton1}
    Click Element    ${allow}

    # Wait for the product data element to be visible

    # Capture a screenshot
    Capture Page Screenshot  filename=categories.png




*** Test Cases ***
# Open Test Application
#     Open Application    ${AppiumServerURL}
#     ...    platformName=${PlatformName}
#     ...    deviceName=${DeviceName}
#     ...    appPackage=${AppPackage}
#     ...    appActivity=${AppActivity}
#     ...    noReset=true
#     ...    allowInsecure=true
Flipkart Webpage Search Validation
    Search Validation

Flipkart Webpage Filter Validation
    Apply Filters on Price and Brand
    
Flipkart Webpage Product Selection Validation
    Product Selection         

Go to cart
    Wait Until Element Is Visible   ${CART}   timeout=10

    Click Element    ${CART}
    Wait Until Element Is Visible   ${size}   timeout=10
    Click Element    ${size}
    Click Element    //android.widget.TextView[@text="Continue"]
    Wait Until Element Is Visible  ${phone}     timeout=10
    Click Element    ${phone} 
    Input Text    //android.widget.FrameLayout[@resource-id="com.flipkart.android:id/container"]     '9409718078'
    Click Element    //android.widget.TextView[@text="Continue"]

    Wait Until Element Is Visible   ${PLACEORDER}    timeout=10
    Click Element    ${PLACEORDER}