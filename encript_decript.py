import base64

# Codificando
data = b'Hello, World!'
encoded_data = base64.b64encode(data)
print(encoded_data)

# Decodificando
decoded_data = base64.b64decode(encoded_data)
print(decoded_data)
