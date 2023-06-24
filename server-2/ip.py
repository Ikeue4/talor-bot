import socket

def get_ip_address():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to a remote server (doesn't matter which)
        sock.connect(("8.8.8.8", 80))
        
        # Get the local IP address from the socket's address
        ip_address = sock.getsockname()[0]
        return ip_address
    except socket.error:
        return None
    finally:
        # Close the socket
        sock.close()

# Call the function to get the IP address
ip_address = get_ip_address()

# Print the IP address
if ip_address:
    print("Your IP address is:", ip_address)
else:
    print("Unable to retrieve IP address.")