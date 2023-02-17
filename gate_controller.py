import serial
import time

# Configure the serial port for the barcode scanner
barcode_ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

# Configure the serial port for the gate operator
gate_ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Configure the serial port for the GSM module
gsm_ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)

# Define the barcode format and length
barcode_format = 'CODE128'
barcode_length = 12

# Define the command to send to the gate operator to open the gate
gate_command = b'<01>0x01<02>0x05<03>0x07<04>0x02<05>0x01<06>0x07<07>0x80<08>0x80<09>0x80<10>0x80<11>0x80<12>0x80<13>0x80<14>0x80<15>0x80<16>0x80<17>0x80<18>0x80<19>0x80<20>0x80<21>0x80<22>0x80<23>0x80<24>0x80<25>0x80<26>0x80<27>0x80<28>0x80<29>0x80<30>0x80<31>0x80<32>0x80<33>0x80'

# Main loop to listen for incoming text messages
while True:
    # Check for incoming text messages
    gsm_ser.write('AT+CMGL="ALL"\r\n'.encode())
    response = gsm_ser.read(1024).decode()
    if '+CMGL:' in response:
        # Extract the message text and sender phone number
        msg_index = response.index('+CMGL:')
        msg = response[msg_index:]
        sender_index = msg.index('+', 1, -1)
        sender = msg[sender_index:].split('"')[0].strip()
        text_index = msg.index('\n')+1
        text = msg[text_index:].split('"')[1]
        
        # Check if the message contains a valid barcode
        if text.startswith(barcode_format) and len(text) == barcode_length:
            # Send the command to the gate operator to open the gate
            gate_ser.write(gate_command)
            time.sleep(1)

