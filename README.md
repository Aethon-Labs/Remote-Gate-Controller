# Raspberry Pi Parking Lot Gate Controller

This is a Python program that runs on a Raspberry Pi and controls a commercial gate operator for a parking lot via a barcode scanner and text messages. The program listens for incoming text messages, reads the barcode from the message, and sends the appropriate command to the gate operator to open the gate.

## Requirements

To use this program, you'll need the following hardware:

- Raspberry Pi 4 Model B
- MicroSD card with Raspbian installed
- USB barcode scanner
- RS-232 to USB adapter for the gate operator
- SIM800L GSM module for sending text messages

You'll also need to install the following software on your Raspberry Pi:

- PySerial library for serial communication

## Installation

To install the program and its dependencies, follow these steps:

1. Clone this repository to your Raspberry Pi.
2. Install the PySerial library by running the following command:
`pip3 install -r requirements.txt`


## Usage

To use the program, follow these steps:

1. Connect the USB barcode scanner, RS-232 to USB adapter, and SIM800L GSM module to your Raspberry Pi.
2. Customize the program for your specific gate operator and barcode scanner by modifying the variables at the top of the Python file.
3. Run the program by running the following command:
`python3 gate_controller.py`


The program will listen for incoming text messages and open the gate when it receives a message with a valid barcode.

## Contributing

If you find any issues with the program or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This program is released under the MIT License. See the LICENSE file for details.

