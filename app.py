import tkinter as tk
from serial import Serial, SerialException
from web3 import Web3
import threading

# Function to initialize Serial connection
def initialize_serial():
    while True:
        com_port = 'COM5'  # Hardcode COM5 as the Arduino is connected to this port
        try:
            ser = Serial(com_port, 9600, timeout=1)
            print(f"Connected to {com_port}")
            return ser
        except SerialException as e:
            print(f"Error: {e}")
            print("Could not open port. Please check the connection.")

# Initialize Serial
ser = initialize_serial()

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"  # Update with your Ganache URL
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load contract ABI
abi = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "_count", "type": "uint256"}
        ],
        "name": "setCount",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "count",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
]

contract_address = "0xd9145CCE52D386f254917e481eB44e9943F39138"  # Replace with your contract's address
contract = web3.eth.contract(address=contract_address, abi=abi)

# Initialize variables
counts = {"BJP": 0, "AAP": 0, "JDU": 0, "OTHERS": 0, "nota": 0}
voting_active = True

# Function to process serial data from Arduino
def process_serial_data():
    while voting_active:
        try:
            if ser:
                data = ser.readline().decode().strip()  # Read data from serial port
                print(f"Received data: {data}")  # For debugging, print the incoming data

                if len(data) == 5:  # We expect 5 characters, one for each vote (BJP, AAP, JDU, OTHERS, nota)
                    for i, key in enumerate(counts.keys()):
                        if data[i] == '1':  # If Arduino sends '1', increment that candidate's count
                            counts[key] += 1
        except Exception as e:
            print(f"Error in serial data: {e}")
            break

# Function to handle local votes (manual input)
def process_local_votes():
    global voting_active
    while voting_active:
        user_input = input("Enter vote (BJP/AAP/JDU/OTHERS/nota) or 'stop voting': ").strip().upper()
        if user_input in counts:
            counts[user_input] += 1
            print(f"Vote added for {user_input}. Current counts: {counts}")
        elif user_input == "STOP VOTING":
            voting_active = False
            print("Voting stopped.")
        else:
            print("Invalid input. Please vote for a valid candidate or type 'stop voting'.")

# Tkinter GUI Setup
def update_gui():
    for key, label in labels.items():
        label.config(text=f"{key.capitalize()} Count: {counts[key]}")
    if voting_active:
        root.after(1000, update_gui)  # Update every second
    else:
        declare_winner()

def declare_winner():
    max_votes = max(counts.values())
    winners = [key for key, value in counts.items() if value == max_votes]

    if len(winners) > 1:
        result_label.config(text=f"Draw: {' & '.join(winners).capitalize()} with {max_votes} votes!", fg="orange", font=("Arial", 16))
    else:
        result_label.config(text=f"Winner: {winners[0].capitalize()} with {max_votes} votes!", fg="green", font=("Arial", 16))

root = tk.Tk()
root.title("Live Voting Interface")
labels = {}

# Create labels dynamically
for key in counts.keys():
    labels[key] = tk.Label(root, text=f"{key.capitalize()} Count: 0", font=("Arial", 14))
    labels[key].pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Start background thread for serial and local voting
threading.Thread(target=process_serial_data, daemon=True).start()
threading.Thread(target=process_local_votes, daemon=True).start()

# Start GUI update loop
update_gui()

# Start Tkinter main loop
root.mainloop()
