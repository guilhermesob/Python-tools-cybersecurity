import urllib.parse

# Codificando
url = 'https://www.example.com?param=value'
encoded_url = urllib.parse.quote(url)
print(encoded_url)

# Decodificando
decoded_url = urllib.parse.unquote(encoded_url)
print(decoded_url)
