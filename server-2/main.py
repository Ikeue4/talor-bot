import requests
import time
import socket
status = ''

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


def ping_webpage(url):
  # Send an HTTP GET request to the webpage
  response = requests.get(url)
  if response.status_code == 200:  # Check if the request was successful
    # Retrieve the content of the webpage
    content = response.text

    # Compare the content with the previous version (if any)
    with open("current_content.txt", "w") as file:
      file.write(content)
    compare_webpage_content()
  else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)


def compare_webpage_content():
  global status
  try:
    # Read the previous version of the content from a file
    with open("previous_content.txt", "r") as file:
      old_content = file.readlines()

    with open("current_content.txt", "r") as file:
      new_content = file.readlines()

    if len(new_content) != len(old_content):
      print('change')
      status = 'yes'
    else:
      status = 'no'

    print(len(new_content), len(old_content))

    print("Comparison complete.")

  except FileNotFoundError:
    # If the file doesn't exist, assume it's the first ping
    print("Initial ping. Storing the webpage content...")
    store_webpage_content(new_content)


def store_webpage_content(content):
  # Store the content in a file for future comparisons
  with open("previous_content.txt", "w") as file:
    file.write(content)
  print("Webpage content stored.")


def send_to_server():
  global status
  data_P = status
  response = requests.post('https://bowedutterregisters.poeple.repl.co/send_data_status', json=data_P)
  print(response)


# Call the function to get the IP address
ip_address = get_ip_address()

# Print the IP address
if ip_address:
  print("Your IP address is:", ip_address)
else:
  print("Unable to retrieve IP address.")

while True:
  # Example usage
  url = "https://taylorswift.ticketek.com.au/"
  ping_webpage(url)
  send_to_server()
  time.sleep(1)