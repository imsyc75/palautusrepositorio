*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  matti
    Set Password  matti123
    Set Password Confirmation  matti123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  matti123
    Set Password Confirmation  matti123
    Submit Registration
    Registration Should Fail With Message  Username should contain at least 3 letters

Register With Valid Username And Too Short Password
    Set Username  heikki
    Set Password  heik12
    Set Password Confirmation  heik12
    Submit Registration
    Registration Should Fail With Message  Password should contain at least 8 characters

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  liisa
    Set Password  liisaliisa
    Set Password Confirmation  liisaliisa
    Submit Registration
    Registration Should Fail With Message  Password should contain at least one number or symbol

Register With Nonmatching Password And Password Confirmation
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija456
    Submit Registration
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username is already in use

Login After Successful Registration
    Set Username  leena
    Set Password  leena123
    Set Password Confirmation  leena123
    Submit Registration
    Registration Should Succeed
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  leena
    Set Password  leena123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  tiina
    Set Password  tiina
    Set Password Confirmation  tiina
    Submit Registration
    Registration Should Fail With Message  Password should contain at least 8 characters
    Click Link  Login
    Set Username  tiina
    Set Password  tiina
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Pages Should Be Open

Login Should Succeed
    Main Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page