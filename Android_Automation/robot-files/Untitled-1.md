

 # Perform your test actions on the main activity
     # Enter username
    Input Text    xpath=//*[@resource-id='username_input']    your_username

    # Enter password
    Input Text    xpath=//*[@resource-id='password_input']    your_password

    # Click the login button
    Click Element    xpath=//*[@resource-id='login_button']