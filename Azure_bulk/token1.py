import requests



def token():
    tkn=input("Get your offline token from the below endpoint\n::- https://access.redhat.com/management/api:----\n")
    
    
    
    return "This is token::-"+tkn 

# def get_token():
#     url = "https://access.redhat.com/management/api/token"
#     client_id = "goutam61"
#     client_secret = "reset1212@12"
#     data = {
#         "client_id": client_id,
#         "client_secret": client_secret
#     }

#     response = requests.post(url, data=data)
#     if response.status_code == 200:
#         token = response.json().get("access_token")
#         return token
#     else:
#         # Handle error cases
#         print(f"Error: {response.status_code} - {response.text}")
#         return None
    

# print(get_token())

print(token())

