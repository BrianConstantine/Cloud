import serial
import time

# Replace 'COM5' with your port, or '/dev/rfcomm0' for Linux
bluetooth_port = 'COM5'
baud_rate = 115200

try:
    print("Connecting to Bluetooth Weighing Scale...")
    ser = serial.Serial(bluetooth_port, baud_rate)
    time.sleep(2)  # Wait for connection to stabilize

    print("Connected. Reading weight data...\n")
    while True:
        if ser.in_waiting:
            weight_data = ser.readline().decode().strip()
            print(f"Received: {weight_data}")
except KeyboardInterrupt:
    print("\nDisconnected by user.")
except serial.SerialException:
    print("Could not connect. Check Bluetooth pairing and port.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
