*** Settings ***
Resource   Append_to_CSV.robot
*** Keywords ***
Save Names To CSV
    [Arguments]                     ${file_name}        ${details}
    FOR    ${index}    IN RANGE  3  ${details.__len__()}

        ${name}              Get Text                     //*[@data-cel-widget="search_result_${index}"] //h2[starts-with(@class,'a-size-mini a-spacing-none a-color-base s-line-clamp-2')]
        ${price}             Get Text                     //*[@data-cel-widget="search_result_${index}"] //span[@class='a-price']
        ${rating}            Get Text                     //*[@data-cel-widget="search_result_${index}"] //span[@class='a-icon-alt']
        ${shipping}          Get Text                     //*[@data-cel-widget="search_result_${index}"] //div[@data-cy="delivery-recipe"]
        ${Num_is_visible}    Element Should Be Visible    //*[@data-cel-widget="search_result_${index}"] //div[@class="a-row a-size-base"]
        Run Keyword If    ${Num_is_visible}    Append Product Details To File    ${file_name}    ${name}    ${price}    ${rating}    ${Num_is_visible}

    END