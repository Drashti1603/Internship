*** Settings ***
Documentation    To test basic automation
Library  AppiumLibrary
Suite Setup  Open Calculator App
Suite Teardown  Close Application
*** Variables ***
${DEV.APPIUM_SERVER}    http://localhost:4723/wd/hub
${DEV.PLATFORM_NAME}    Android
${DEV.PLATFORM_VERSION}    12
${DEV.DEVICE_NAME}    Drashti Chetta
${DEV.APP_PACKAGE}    com.miui.calculator
${DEV.APP_ACTIVITY}    com.miui.calculator.cal.CalculatorActivity

${EQUALS_SIGN} =    xpath=//*[contains(@text,'=')]
${DISPLAYED_RESULT} =    xpath=//*[contains(@text,'=')]

${td_Digit1} =    9
${td_Digit2} =    1
${td_Expected_Addition_Result} =    10
${td_Expected_Subtraction_Result} =    8

*** Keywords ***
Open Calculator App

[Documentation]
Open Application    ${DEV.APPIUM_SERVER}    platformName=${DEV.PLATFORM_NAME}    platformVersion=${DEV.PLATFORM_VERSION}    deviceName=${DEVICE_NAME}    appPackage=${APP_PACKAGE}    appActivity=${APP_ACTIVITY}

*** Test Cases ***




