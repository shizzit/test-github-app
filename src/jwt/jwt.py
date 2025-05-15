import jwt
import time

from ..utils.utils import read_file

def create_jwt(config):
    private_key = config.private_key
    client_id = config.client_id

    payload = {
        # Issued at time
        'iat': int(time.time()),
        # JWT expiration time (10 minutes maximum)
        'exp': int(time.time()) + 600,
        # GitHub App's client ID
        'iss': client_id
    }
    encoded_jwt = jwt.encode(payload, private_key, algorithm='RS256')

    # print(encoded_jwt)

    return encoded_jwt
