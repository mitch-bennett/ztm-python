from twilio.rest import Client 
 
account_sid = '[account]' 
auth_token = '[token]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG0011fa1bd450ad82b2110e463ffa5150', 
                              body='HEYYY AGAIN',      
                              to='+1--number' 
                          ) 
 
print(message.sid)