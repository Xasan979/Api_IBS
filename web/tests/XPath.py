get_xpath_valid = [                                                     # GET_URL_VALID
    '//*[@id="console"]/div[1]/ul/li[1]',
    '//*[@id="console"]/div[1]/ul/li[2]',
    '//*[@id="console"]/div[1]/ul/li[4]',
    '//*[@id="console"]/div[1]/ul/li[5]',
    '//*[@id="console"]/div[1]/ul/li[15]'
]
get_xpath_valid_element = [
    '//*[@id="console"]/div[1]/ul/li[1]/a',
    '//*[@id="console"]/div[1]/ul/li[2]/a',
    '//*[@id="console"]/div[1]/ul/li[4]/a',
    '//*[@id="console"]/div[1]/ul/li[5]/a',
    '//*[@id="console"]/div[1]/ul/li[15]/a'
]
get_xpath_invalid = [                                                     # GET_URL_INVALID
    '//*[@id="console"]/div[1]/ul/li[3]',
    '//*[@id="console"]/div[1]/ul/li[6]'
]
get_xpath_invalid_element = [
    '//*[@id="console"]/div[1]/ul/li[3]/a',
    '//*[@id="console"]/div[1]/ul/li[6]/a'
]


post_xpath_valid = [                                                      # POST_URL_VALID
    '//*[@id="console"]/div[1]/ul/li[7]',
    '//*[@id="console"]/div[1]/ul/li[11]',
    '//*[@id="console"]/div[1]/ul/li[13]'

]

post_xpath_valid_element = [
    '//*[@id="console"]/div[1]/ul/li[7]/a',
    '//*[@id="console"]/div[1]/ul/li[11]/a',
    '//*[@id="console"]/div[1]/ul/li[13]/a'
]
post_data_valid = [
    {'name': 'morpheus', 'job': 'leader'},
    {'email': 'eve.holt@reqres.in', 'password': 'pistol'},
    {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
]

post_xpath_invalid = [                                                      # POST_URL_INVALID
    '//*[@id="console"]/div[1]/ul/li[12]',
    '//*[@id="console"]/div[1]/ul/li[14]'
]

post_xpath_invalid_element = [
    '//*[@id="console"]/div[1]/ul/li[12]/a',
    '//*[@id="console"]/div[1]/ul/li[14]/a'

]
post_data_invalid = [
    {'email': 'sydney@fife'},
    {'email': 'peter@klaven'}
]

put_xpath_valid = [                                                      # PUT_URL_VALID
    '//*[@id="console"]/div[1]/ul/li[8]'


]

put_xpath_valid_element = [
    '//*[@id="console"]/div[1]/ul/li[8]/a'

]
put_data_valid = [
    {'name': 'morpheus', 'job': 'zion resident'}
]

put_xpath_invalid = [                                                      # PUT_URL_INVALID
    '//*[@id="console"]/div[1]/ul/li[8]'


]

put_xpath_invalid_element = [
    '//*[@id="console"]/div[1]/ul/li[8]/a'

]
put_data_invalid = [
    {'name': 'morpheus', 'job': 'zion resident'}
]

patch_xpath_valid = [                                                      # PATCH_URL_VALID
    '//*[@id="console"]/div[1]/ul/li[9]'


]

patch_xpath_valid_element = [
    '//*[@id="console"]/div[1]/ul/li[9]/a'

]
patch_data_valid = [
    {'name': 'morpheus', 'job': 'zion resident'}
]

patch_xpath_invalid = [                                                      # PATCH_URL_INVALID
    '//*[@id="console"]/div[1]/ul/li[9]'


]

patch_xpath_invalid_element = [
    '//*[@id="console"]/div[1]/ul/li[9]/a'

]
patch_data_invalid = [
    {'name': 'morpheus', 'job': 'zion resident'}
]


delete_xpath_valid = [                                                     # DELETE_URL_VALID
    '//*[@id="console"]/div[1]/ul/li[10]'

]
delete_xpath_valid_element = [
    '//*[@id="console"]/div[1]/ul/li[10]/a'
]
delete_xpath_invalid = [                                                     # DELETE_URL_INVALID
    '//*[@id="console"]/div[1]/ul/li[10]'
]
delete_xpath_invalid_element = [
    '//*[@id="console"]/div[1]/ul/li[10]/a'
]