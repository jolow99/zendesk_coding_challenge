from base64 import b64encode

def get_auth_header(username, password):
    userAndPass = b64encode(bytes(username + ':' + password, 'utf-8')).decode('ascii')
    return userAndPass

print(get_auth_header("INSERT USERNAME", "INSERT PASSWORD"))