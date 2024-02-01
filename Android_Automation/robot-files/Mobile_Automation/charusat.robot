*** Settings ***
Library    AppiumLibrary
Library    SeleniumLibrary


*** Variables ***
${PLATFORM_NAME}    Android
${PLATFORM_VERSION}    12
${DEVICE_NAME}    Drashti Chetta
${APP_PACKAGE}    charuemp.charusat.edu.charuemp
${APP_ACTIVITY}    charuemp.charusat.edu.charuemp.SplashActivity
${APPIUM_SERVER}    http://localhost:4723/wd/hub
${customTimeout}    60s  # Set your desired timeout value

*** Test Cases ***
Open App with Splash Screen
    Open Application    ${APPIUM_SERVER}    platformName=${PLATFORM_NAME}    platformVersion=${PLATFORM_VERSION}    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}

    # Wait for the splash screen to disappear
    My Wait Until Page Contains Element    xpath=//android.widget.ImageView[@resource-id="charuemp.charusat.edu.charuemp:id/imageView2"]    timeout=${customTimeout}

    # Continue with interactions on the main activity
    # For example, navigate to the main activity
    Open Activity    ${APP_PACKAGE}    charuemp.charusat.edu.charuemp.LoginActivity

    # Perform your test actions on the main activity
    # ...


*** Keywords ***
My Wait Until Page Contains Element
    [Arguments]    ${xpath}    ${timeout}
    Wait Until Keyword Succeeds    10s    1s    AppiumLibrary.Element Should Be Visible    ${xpath}    msg=The element '${xpath}' did not become visible within the specified timeout: ${timeout}
    Element Should Not Be Visible    ${xpath}    msg=The element '${xpath}' did not become invisible within the specified timeout: ${timeout}


*** Keywords ***
Open Activity
    [Arguments]    ${app_package}    ${app_activity}
    Open Application    ${APPIUM_SERVER}    platformName=${PLATFORM_NAME}    platformVersion=${PLATFORM_VERSION}    deviceName=${DEVICE_NAME}    appPackage=${app_package}    appActivity=${app_activity}
