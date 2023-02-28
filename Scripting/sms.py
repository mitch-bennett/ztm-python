from twilio.rest import Client 
 
account_sid = 'ACd513a9bc24efe6fb02827bf71f4e3e92' 
auth_token = '2f6d7039cdf1e4115e9d6d6f30938d06' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG0011fa1bd450ad82b2110e463ffa5150', 
                              body='HEYYY AGAIN',      
                              to='+15857491761' 
                          ) 
 
print(message.sid)