import base64
string = input("Some text here : ")
data = base64.b64encode(string.encode())
print("Encoded : ", data)
print("Decoded : ", base64.b64decode(data))
