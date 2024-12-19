import hashlib
import time
import sys

# A OTP generator that refreshes every 15 secs
def generate_otp(username, password, interval=15):
    # time.time() returns the current time in seconds and dividing by the interval of 15 secs
    time_window = int(time.time() / interval)
    # A formatted string is created by combining username, password, and time_window
    data = f"{username}{password}{time_window}".encode()
    # Generates a SHA-256 hash of the input data
    hash_digest = hashlib.sha256(data).hexdigest()
    # The modulo operation % 10**6 reduces this large integer to a 6-digit number.
    otp = int(hash_digest, 16) % 10**6
    return f"{otp:06d}"

def device_main(username, password):

    print(f"Device started for user: {username}")
    try:
        while True:
            otp = generate_otp(username, password)
            print("Device: {0}".format(otp))
            time.sleep(15)  # Wait 15 seconds before generating a new OTP
    
    # CTRL-C to stop the device
    except KeyboardInterrupt:
        print("\nDevice stopped.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 device.py <username> <password>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        device_main(username, password)