GET_URL_VALID = [
    'api/users?page=2',
    'api/users/2',
    'api/unknown',
    'api/unknown/2',
    'api/users?delay=3'
]
GET_URL_INVALID = [
    'api/users/23',
    'api/unknown/23'
]

POST_URL_VALID = [
    ('api/users', {'name': 'morpheus', 'job': 'leader'}),
    ('api/register', {'email': 'eve.holt@reqres.in', 'password': 'pistol'}),
    ('api/login', {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
]
POST_URL_INVALID = [
    ('api/register', {'email': 'sydney@fife'}),
    ('api/login', {'email': 'peter@klaven'})
]

PUT_URL_VALID = [
    ('api/users/2', {'name': 'morpheus', 'job': 'zion resident'})
]
PUT_URL_INVALID = [
    ('api/users/10', {'name': 'neo', 'job': 'the one'})
]

PATCH_URL_VALID = [
    ('api/users/2', {'name': 'morpheus', 'job': 'zion resident'})
]
PATCH_URL_INVALID = [
    ('api/users/2', {'name': 'morpheus', 'job': 'zion resident'})
]

DELETE_URL_VALID = [
    'api/users/2'
]
DELETE_URL_INVALID = [
    'api/users/2'
]
