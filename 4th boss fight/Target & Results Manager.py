Target_ip = input("Enter the target IP here :")
open_port = input("Enter the opend port: ")
with open("result.txt", "a") as file:
    file.write(f"Target ip : {Target_ip}\n Open port : {open_port}\n")

print("Data saved successfully!")
