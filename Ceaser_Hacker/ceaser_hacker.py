# Get the message from user
message_to_decrypt = input("Enter the message you want ot decrypt: ")
  

# list stores all the decrypted message 
decrypted_message = []

# loop through all the possible values that are from 1 to 26
for j in range(1,27):
    message = "" # this is to store each decrypted versions
    
    for i in message_to_decrypt:
        alphabets_to_num = ord(i) # change the given alphabets to numbers 
        decrytion_num = alphabets_to_num -j # Substract each keys  
        decypted_message = chr(decrytion_num) # get the substrated number to alphabets 
        message += decypted_message # adds that to message 
    decrypted_message.append(f"{j}: {message}") # stores it in the list 


# prints each words 
for x in decrypted_message:
    print(x)




