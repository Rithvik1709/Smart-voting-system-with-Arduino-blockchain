# Voting System with Arduino, Python GUI, and Blockchain Integration

## Overview
This project is an electronic voting system that integrates an **Arduino-based hardware setup**, a **Python GUI for live vote tracking**, and **blockchain technology (Ganache) for vote storage**. It allows users to vote using physical buttons connected to an Arduino, displays vote counts on an LCD screen, and logs the votes into a Python-based graphical user interface (GUI). Additionally, votes can be stored on a local blockchain using Web3.

---

## Features
- **Arduino-based voting system** with physical buttons for casting votes.
- **LCD display** to show the available voting options.
- **Live vote tracking GUI** using Python's Tkinter.
- **Serial communication** between Arduino and Python.
- **Blockchain integration** using Ganache and Web3.py for vote storage.
- **Manual voting option** via the command line.
- **Automatic winner declaration** based on highest votes.

---

## Components Required
### **Hardware:**
- Arduino board (e.g., Arduino Uno)
- I2C LCD Display
- Push buttons (5 total)
- Resistors (10kΩ, if needed)
- Jumper wires
- Breadboard

### **Software:**
- Arduino IDE
- Python 3
- Required Python libraries:
  - `tkinter` (for GUI)
  - `pyserial` (for serial communication)
  - `web3` (for blockchain interaction)
  - `threading` (for background processes)
- Ganache (for blockchain simulation)

---

## Setup and Installation
### **1. Arduino Setup**
1. Connect the buttons to Arduino digital pins (with `INPUT_PULLUP` mode enabled).
2. Connect the I2C LCD display.
3. Upload the **Arduino code** (`arduino.txt`) using the Arduino IDE.
4. Ensure that the Arduino is connected to your PC via USB.

### **2. Python Setup**
1. Install required Python libraries:
   ```sh
   pip install pyserial web3
   ```
2. Ensure that the Arduino is connected to **COM5** (update the port if needed in the Python script).
3. Start Ganache and ensure it's running on `http://127.0.0.1:7545`.
4. Update the **smart contract address** in the Python script.

### **3. Running the System**
1. **Run the Arduino Code**: Upload the script to the Arduino board.
2. **Run the Python GUI**: Execute the Python script (`python.txt`):
   ```sh
   python python.txt
   ```
3. **Voting Process**:
   - Press the corresponding button on Arduino to vote.
   - Votes will be displayed on the LCD and sent to Python via serial communication.
   - The Python GUI updates in real-time and stores votes in the blockchain.
   - Votes can also be manually entered via the command line.
   - The winner is displayed once voting stops.

---

## Expected Output
1. LCD displays voting options and updates when a vote is cast.
2. The Python GUI shows real-time vote counts.
3. Serial communication logs votes in the terminal.
4. Votes are stored in the blockchain (Ganache).
5. The system declares the winner after voting stops.

---
