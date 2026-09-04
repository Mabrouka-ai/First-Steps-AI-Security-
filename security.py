print("--- Smart Security Authentication System ---")
authorized_user = " Eng_Engineer"
username_input = input("Enter Your username:")
if username_input == authorized_user:
    print("Access Granted! Welcome to secure dashboard.")
else:
    print("Security Warning: Unauthorized access attempt detected!")
