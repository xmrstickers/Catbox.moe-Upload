import sys
import os
import requests
import random

print("Placing cat in box....")
print()
print("                          ,")
print("   ,-.       _,---._ __  / \\") #fun fact: this ascii art is sourced from the catbox.moe HTML source code :)
print("  /  )    .-'       `./ /   \\")
print(" (  (   ,'            `/    /|")
print("  \  `-\"             \'\   / |")
print("   `.              ,  \ \ /  |")
print("    /`.          ,'-`----Y   |")
print("   (            ;        |   '")
print("   |  ,-.    ,-'         |  /")
print("   |  | (   |            | /")
print("   )  |  \  `.___________|/")
print("   `--'   `--'")
print()

# Catbox file-upload URL
url = "https://catbox.moe/user/api.php"

#CatBox generates a random 29-digit integer string to be used in the content boundary -- see: <input type="hidden" name="userhash" value=""> on their HTML source
    #appears to be arbitrary, random-gen on our end works fine. I could _not_ find out where catbox generates it in their JavaScript to confirm this, however.
user_hash = str(random.randint(1000000000000000000000000, 999999999999999999999999999))

# Set the boundary string; see:  https://www.w3.org/Protocols/rfc1341/7_2_Multipart.html
boundary = "-----------------------------"+user_hash
headers = {
    "Content-Type": f"multipart/form-data; boundary={boundary}"
}

#           File to Upload
# Check if a file was passed as a command-line argument
if len(sys.argv) < 2:
    print("Error: No file specified")
    exit(1)

# Get the file path from the command-line argument
file_path = sys.argv[1]

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: File not found: {file_path}")
    exit(1)

file_name = file_path #file is found, let's load the contents and prepare the request...
#print("Attempting "+file_name+" upload...")
# Open the file in binary mode
with open(file_name, "rb") as file:    
    # Set the reqtype form of payload
    reqtype = f"--{boundary}\r\nContent-Disposition: form-data; name=\"reqtype\"\r\n\r\nfileupload\r\n"     
    # Set the file form portion of payload
    file_form = f"--{boundary}\r\nContent-Disposition: form-data; name=\"fileToUpload\"; filename=\"{file_name}\"\r\nContent-Type: application/octet-stream\r\n\r\n{file.read().decode()}\r\n--{boundary}--"
     # Combine the form fields and add the closing boundary
    data = f"{reqtype}{file_form}--{boundary}--"
    #print(data)
    print()
# Send the POST request with the file as the body
response = requests.post(url, headers=headers, data=data)   
# Print the server's response, the file-upload link
if response.status_code == 200:
    print(file_name+" successfully uploaded!")
    print(response.text)
else:
    print("Request failed - expected 200, received "+str(response.status_code))