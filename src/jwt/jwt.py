import jwt
import time

from ..utils.utils import read_file

# https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-json-web-token-jwt-for-a-github-app
# note: for whatever reason, (60*10) or (10 minutes) does not seems to work in spite of the docs saying time must be no more than 10 minutes
def create_jwt(config):
    private_key = config.private_key
    client_id = config.client_id

    payload = {
        # Issued at time
        'iat': int(time.time()),
        # JWT expiration time - Be aware there is a max value here.
        'exp': int(time.time()) + 540, # 9 mins
        # GitHub App's client ID
        'iss': client_id
    }
    encoded_jwt = jwt.encode(payload, private_key, algorithm='RS256')

    # print(encoded_jwt)

    return encoded_jwt
